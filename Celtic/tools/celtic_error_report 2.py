#!/usr/bin/env python3
"""Compare a Celtic foma transducer against the IPA column of CAPR's Celtic TSV.

Designed for anTadhg/caprWIP-Celtic: save as server/tools/celtic_error_report.py.
Run inside the backend Docker image, from /usr/app:
    python3 tools/celtic_error_report.py --language Old_Irish --all

No website, external Python packages, or changes to CAPR source files required.
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

# Exact DOCULECT values used by the Celtic wordlist, and corresponding bin names.
LANGUAGES = {
    "Old_Irish": "old_irish.bin",
    "Old_Welsh": "old_welsh.bin",
    "Middle_Welsh": "middle_welsh.bin",
    "Old_Breton": "old_breton.bin",
    "Middle_Breton": "middle_breton.bin",
    "Old_Cornish": "old_cornish.bin",
    "Middle_Cornish": "middle_cornish.bin",
    "Gaulish": "gaulish.bin",
    "Celtiberian": "celtiberian.bin",
}


def clean_input(value: str) -> str:
    # The FST's PCeltProtoInput expects e.g. brātīr, without the citation '*'.
    return unicodedata.normalize("NFC", re.sub(r"[{}*\s/()]", "", value or ""))


def clean_expected(value: str) -> str:
    # IPA contains unspaced surface representations; keep phonological symbols.
    return unicodedata.normalize("NFC", (value or "").strip())


def generate(bin_path: Path, form: str) -> list[str]:
    # flookup -i: input is the upper/lexical proto-form, output is the
    # lower/surface daughter-language form. Without -i the lookup is reversed.
    try:
        result = subprocess.run(
            ["flookup", "-i", str(bin_path)],
            input=form + "\n",
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=True,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("flookup is unavailable. Run this script *inside* CAPR's backend Docker image.") from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"flookup failed for {form!r}: {exc.stderr.strip()}") from exc

    outputs: list[str] = []
    for raw in result.stdout.splitlines():
        if not raw.strip():
            continue
        pieces = raw.split("\t", 2)
        # The output protocol is: protoform<TAB>result (or protoform<TAB>+?).
        if len(pieces) < 2:
            raise RuntimeError(f"Unrecognized flookup output: {raw!r}")
        candidate = unicodedata.normalize("NFC", pieces[1].strip())
        if candidate and candidate != "+?" and candidate not in outputs:
            outputs.append(candidate)
    return outputs


def main() -> int:
    server = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", required=True, choices=list(LANGUAGES),
                        help="One DOCULECT from the Celtic TSV (capitalization and underscores matter).")
    parser.add_argument("--tsv", type=Path, default=server / "data" / "celtic-aligned-final.tsv",
                        help="TSV to check; defaults to server/data/celtic-aligned-final.tsv")
    parser.add_argument("--bin", type=Path, default=None,
                        help="Compiled FST binary; defaults to server/<language>.bin")
    parser.add_argument("--output", type=Path, default=None,
                        help="Report filename; defaults to server/docs/debug_snapshots/<language>_error_report.txt")
    parser.add_argument("--all", action="store_true",
                        help="Include matching entries as well as errors in the saved report")
    args = parser.parse_args()

    tsv = args.tsv.resolve()
    bin_path = (args.bin or server / LANGUAGES[args.language]).resolve()
    output = (args.output or server / "docs" / "debug_snapshots" /
              (args.language.lower() + "_error_report.txt")).resolve()

    for name, path in (("TSV", tsv), ("compiled FST", bin_path)):
        if not path.is_file():
            parser.error(f"{name} does not exist: {path}")

    records = []
    skipped = 0
    with tsv.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp, delimiter="\t")
        required = {"DOCULECT", "PROTOFORM", "IPA", "COUNTERPART", "CONCEPT"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            parser.error("TSV missing required columns: " + ", ".join(sorted(required - set(reader.fieldnames or []))))
        for line_number, row in enumerate(reader, start=2):
            if (row.get("DOCULECT") or "").strip() != args.language:
                continue
            proto = clean_input(row.get("PROTOFORM", ""))
            ipa = clean_expected(row.get("IPA", ""))
            if not proto or not ipa or ipa == "-":
                skipped += 1
                continue
            records.append({"line": line_number, "id": (row.get("ID") or "").strip(),
                            "concept": (row.get("CONCEPT") or "").strip(),
                            "proto_citation": (row.get("PROTOFORM") or "").strip(),
                            "proto": proto, "expected": ipa,
                            "spelling": (row.get("COUNTERPART") or "").strip()})

    if not records:
        parser.error(f"No usable {args.language} entries in {tsv}. Verify DOCULECT values and TSV content.")

    cache: dict[str, list[str]] = {}
    for row in records:
        form = row["proto"]
        if form not in cache:
            cache[form] = generate(bin_path, form)
        found = cache[form]
        row["outputs"] = found
        if not found:
            row["status"] = "NO_OUTPUT"
        elif row["expected"] in found:
            row["status"] = "MATCH"
        else:
            row["status"] = "MISMATCH"

    counts = Counter(row["status"] for row in records)
    n = len(records)
    lines = [
        "CELTIC FST ERROR REPORT",
        f"Language: {args.language}",
        f"Data: {tsv}",
        f"Compiled FST: {bin_path}",
        "Compared column: IPA (not COUNTERPART, which is orthographic)",
        f"Rows checked: {n}",
        f"Exact matches: {counts['MATCH']}",
        f"Mismatches: {counts['MISMATCH']}",
        f"No output: {counts['NO_OUTPUT']}",
        f"Rows skipped (missing protoform/IPA): {skipped}",
        f"Match rate: {100 * counts['MATCH'] / n:.1f}%",
        "",
        "=== ERRORS (NO_OUTPUT and MISMATCH) ===",
        "",
    ]

    def format_item(row: dict) -> list[str]:
        return [
            f"[{row['status']}] TSV ID {row['id'] or '?'} (line {row['line']}): {row['concept']}",
            f"  Proto-Celtic input: {row['proto_citation']}",
            f"  Input sent to flookup: {row['proto']}",
            f"  Expected IPA: {row['expected']}",
            f"  Spelled word (reference only): {row['spelling']}",
            f"  FST output: {', '.join(row['outputs']) if row['outputs'] else '+?'}",
            "",
        ]

    failed = [row for row in records if row["status"] != "MATCH"]
    if not failed:
        lines.append("None: all checked rows have a matching output.")
        lines.append("")
    for row in failed:
        lines.extend(format_item(row))
    if args.all:
        lines.extend(["=== MATCHING ENTRIES ===", ""])
        for row in records:
            if row["status"] == "MATCH":
                lines.extend(format_item(row))

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Checked {n} {args.language} entries: {counts['MATCH']} matches, "
          f"{counts['MISMATCH']} mismatches, {counts['NO_OUTPUT']} with no output.")
    print(f"Report saved to: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
