#!/usr/bin/env python3
"""Summarise proto→surface generation coverage for Old English."""

import argparse
import csv
import re
import subprocess
from pathlib import Path
from typing import Dict, List
from oe_pipeline import evaluation_input, load_rows as load_selected_rows

PROTO_STRIP_RE = re.compile(r"[{}*\s\-/()]")


def normalize_proto(raw: str) -> str:
    return PROTO_STRIP_RE.sub("", raw or "")


def run_apply_down(bin_path: Path, form: str) -> List[str]:
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=f"{form}\n".encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    outputs: List[str] = []
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        parts = raw.split("\t", 1)
        out = parts[1] if len(parts) == 2 else ""
        if out and out != "+?":
            outputs.append(out)
    # Deduplicate while preserving order.
    seen = set()
    deduped: List[str] = []
    for item in outputs:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def load_rows(tsv_path: Path) -> List[Dict[str, str]]:
    return [{**row, "norm": row["proto_norm"]} for row in load_selected_rows(tsv_path)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise Old English apply-down coverage")
    default_root = Path(__file__).resolve().parents[1]
    parser.add_argument(
        "--tsv",
        default=str(default_root / "data" / "germanic-aligned-final.tsv"),
        help="Aligned TSV with Old English rows (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        default=str(default_root / "old_english.bin"),
        help="Generator FST for apply-down (default: %(default)s)",
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=10,
        help="How many mismatches to list (default: %(default)s)",
    )
    parser.add_argument(
        "--dump-multi",
        help="Optional JSON path to dump entries with multiple outputs",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()

    rows = load_rows(tsv_path)
    single_output = 0
    single_correct = 0
    no_output = 0
    multi_outputs = 0
    multi_entries: List[Dict[str, str]] = []
    mismatches: List[Dict[str, str]] = []

    for row in rows:
        outputs = run_apply_down(bin_path, evaluation_input(row))
        row_outputs = outputs
        row["outputs"] = row_outputs
        if not row_outputs:
            no_output += 1
            mismatches.append(row)
            continue
        if len(row_outputs) == 1:
            single_output += 1
            if row_outputs[0] == row["counterpart"]:
                single_correct += 1
            else:
                mismatches.append(row)
        else:
            multi_outputs += 1
            if row["counterpart"] not in row_outputs:
                mismatches.append(row)
            multi_entries.append(row)

    total = len(rows)
    print(f"Total Old English entries: {total}")
    print(f"No generator outputs: {no_output}")
    print(f"Multiple outputs: {multi_outputs}")
    print(f"Exactly one output: {single_output}")
    print(f"Exactly one correct output: {single_correct}")
    print()
    print(f"Sample mismatches (first {min(args.sample, len(mismatches))}):")
    for row in mismatches[: args.sample]:
        outs = ", ".join(row.get("outputs", [])) or "+?"
        print(
            f"- {row['concept']} ({row['proto']}): expected {row['counterpart']} | outputs: {outs}"
        )

    if args.dump_multi:
        import json

        dump_path = Path(args.dump_multi).expanduser().resolve()
        dump_path.parent.mkdir(parents=True, exist_ok=True)
        payload = [
            {
                "concept": row["concept"],
                "proto": row["proto"],
                "counterpart": row["counterpart"],
                "outputs": row.get("outputs", []),
            }
            for row in multi_entries
        ]
        dump_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
