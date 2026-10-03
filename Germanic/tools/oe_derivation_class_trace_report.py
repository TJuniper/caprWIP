#!/usr/bin/env python3
"""OE trace report grouped by DERIVATION_CLASS.

Same per-stage trace machinery as oe_full_trace_report.py, but instead of
sorting words into mismatch buckets (exact_match, no_output, …) it sorts
them into the eight DERIVATION_CLASS buckets defined in the TSV:
    regular, early_analogy, late_analogy, attested_variant,
    lexeme_retarget, reconstructed_oe, known_unmodelled,
    unexplained_unmodelled
followed by an `unclassified` bucket for any Old_English row with a real
COUNTERPART but a blank DERIVATION_CLASS.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Dict, List

from oe_full_trace_report import (
    STAGE_HEADERS,
    STAGES,
    apply_down,
    normalize_proto,
    trace_lexeme,
    trace_provenance_problems,
)

DERIVATION_ORDER = [
    "regular",
    "early_analogy",
    "late_analogy",
    "attested_variant",
    "lexeme_retarget",
    "reconstructed_oe",
    "known_unmodelled",
    "unexplained_unmodelled",
    "unclassified",
]


def load_rows(tsv_path: Path) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "Old_English":
                continue
            proto = (row.get("PROTOFORM") or "").strip()
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not proto or not counterpart or counterpart == "-":
                continue
            norm = normalize_proto(proto)
            if not norm:
                continue
            klass = (row.get("DERIVATION_CLASS") or "").strip() or "unclassified"
            rows.append(
                {
                    "concept": row.get("CONCEPT", ""),
                    "proto": proto,
                    "proto_norm": norm,
                    "counterpart": counterpart,
                    "derivation_class": klass,
                    "note": (row.get("NOTE") or "").strip(),
                }
            )
    return rows


def write_report(
    rows: List[Dict[str, str]],
    bin_path: Path,
    bin_dir: Path,
    output_path: Path,
) -> None:
    buckets: Dict[str, List[Dict[str, str]]] = {k: [] for k in DERIVATION_ORDER}
    for row in rows:
        outputs = apply_down(bin_path, row["proto_norm"])
        row_copy = dict(row)
        row_copy["outputs"] = ", ".join(outputs) if outputs else "+?"
        bucket = row["derivation_class"]
        if bucket not in buckets:
            bucket = "unclassified"
        buckets[bucket].append(row_copy)

    lines: List[str] = []
    for bucket in DERIVATION_ORDER:
        items = buckets.get(bucket, [])
        if not items:
            continue
        items.sort(key=lambda r: r["concept"])
        lines.append(f"=== DERIVATION_CLASS: {bucket} ({len(items)}) ===")
        lines.append("")
        for row in items:
            lines.append(f"--- {row['concept']} ---")
            lines.append(f"PROTO: {row['proto']}")
            lines.append(f"EXPECTED: {row['counterpart']}")
            lines.append(f"OUTPUTS: {row['outputs']}")
            if row["note"]:
                lines.append(f"NOTE: {row['note']}")
            lines.append("")
            prev_outputs: List[str] | None = None
            for label, outputs in trace_lexeme(row["proto_norm"], bin_dir):
                base_label = label.split(" [", 1)[0]
                header = STAGE_HEADERS.get(base_label)
                if header is not None:
                    lines.append("")
                    lines.append(header)
                    lines.append("")
                prev_outputs = outputs
                pretty = ", ".join(outputs)
                lines.append(f"{label}: {pretty}")
            lines.append("")
        lines.append("")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def project_full_trace(rows: List[Dict[str, str]], full_trace: Path) -> str:
    """Regroup fresh canonical evidence without repeating transducer lookups."""
    text = full_trace.read_text(encoding="utf-8")
    problems = trace_provenance_problems(text)
    if problems:
        raise ValueError("stale full trace: " + "; ".join(problems))
    pattern = re.compile(
        r"^--- (.*?) ---\nPROTO: ([^\n]*)\nEXPECTED: ([^\n]*)\n"
        r"OUTPUTS: ([^\n]*)\n(.*?)(?=^--- |^=== |\Z)", re.M | re.S)
    evidence = {}
    for match in pattern.finditer(text):
        key = match.group(1, 2, 3)
        if key in evidence:
            raise ValueError(f"duplicate full-trace identity: {key}")
        evidence[key] = match.group(4, 5)
    buckets = {name: [] for name in DERIVATION_ORDER}
    selected = set()
    for row in rows:
        key = (row["concept"], row["proto"], row["counterpart"])
        if key in selected:
            raise ValueError(f"duplicate corpus identity: {key}")
        selected.add(key)
        if key not in evidence:
            raise ValueError(f"missing full-trace identity: {key}")
        bucket = row["derivation_class"]
        buckets[bucket if bucket in buckets else "unclassified"].append(row)
    if len(evidence) != len(rows):
        raise ValueError("full-trace/corpus identity count mismatch")
    lines = []
    for bucket, items in buckets.items():
        if not items:
            continue
        lines.extend([f"=== DERIVATION_CLASS: {bucket} ({len(items)}) ===", ""])
        for row in sorted(items, key=lambda r: r["concept"]):
            outputs, body = evidence[(row["concept"], row["proto"], row["counterpart"])]
            lines.extend([f"--- {row['concept']} ---", f"PROTO: {row['proto']}",
                          f"EXPECTED: {row['counterpart']}", f"OUTPUTS: {outputs}"])
            if row["note"]:
                lines.append(f"NOTE: {row['note']}")
            lines.extend([body.rstrip(), ""])
    return "\n".join(lines) + "\n"


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    germanic_dir = repo_root / "Germanic"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tsv",
        default=str(germanic_dir / "data" / "germanic-aligned-final.tsv"),
        help="Cogset TSV (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        default=str(repo_root / "backend" / "old_english.bin"),
        help="Generator FST for apply-down (default: %(default)s)",
    )
    parser.add_argument(
        "--bin-dir",
        default=str(repo_root / "backend"),
        help="Directory containing old_english_sandbox_after_*.bin (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default=str(
            germanic_dir
            / "docs"
            / "debug_snapshots"
            / "oe_derivation_class_trace_report.txt"
        ),
        help="Report output path (default: %(default)s)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    bin_dir = Path(args.bin_dir).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = load_rows(tsv_path)
    write_report(rows, bin_path, bin_dir, output_path)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
