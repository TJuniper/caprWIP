#!/usr/bin/env python3
"""Triage the OE mismatch report against the known-problems ledger.

Reads:
  - Germanic/data/germanic-aligned-final.tsv (aligned PGmc → OE rows)
  - backend/old_english.bin (compiled FST, via flookup)
  - Germanic/data/oe_known_problems.tsv (ledger of triaged mismatches)

Writes:
  - Germanic/docs/debug_snapshots/oe_known_problems_report.txt

Categorizes each mismatch as 'tractable' (no ledger entry, candidate for
the mismatch loop) or as one of the ledger statuses (parked / wontfix /
exception / open). Also flags stale ledger entries whose proto no longer
mismatches.

Usage:
  python3 Germanic/tools/oe_known_problems_report.py
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

# Reuse the mismatch detector to stay in lock-step with its definitions.
TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))
from oe_mismatch_report import (  # noqa: E402
    apply_down,
    base_bucket,
    load_rows,
    other_subtype,
)
from oe_pipeline import evaluation_input


VALID_STATUSES = {"parked", "wontfix", "exception", "open"}


def load_ledger(path: Path) -> Dict[str, Dict[str, str]]:
    """Read the known-problems ledger TSV. Key on the literal proto string."""
    if not path.exists():
        return {}
    ledger: Dict[str, Dict[str, str]] = {}
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        required = {"proto", "status", "category", "reason", "refs", "added"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Ledger {path} missing columns: {sorted(missing)}")
        for row in reader:
            proto = (row.get("proto") or "").strip()
            if not proto:
                continue
            status = (row.get("status") or "").strip()
            if status not in VALID_STATUSES:
                raise SystemExit(
                    f"Ledger {path}: invalid status {status!r} for {proto!r}; "
                    f"expected one of {sorted(VALID_STATUSES)}"
                )
            ledger[proto] = {
                "status": status,
                "category": (row.get("category") or "").strip(),
                "reason": (row.get("reason") or "").strip(),
                "refs": (row.get("refs") or "").strip(),
                "added": (row.get("added") or "").strip(),
            }
    return ledger


def collect_mismatches(
    rows: List[Dict[str, str]], bin_path: Path
) -> List[Dict[str, str]]:
    """Return list of mismatch dicts: proto, output, expected, bucket."""
    mismatches: List[Dict[str, str]] = []
    for row in rows:
        outputs = apply_down(bin_path, evaluation_input(row))
        expected = row["counterpart"]
        if outputs and expected in outputs:
            continue
        out = outputs[0] if outputs else "+?"
        if outputs:
            bucket = base_bucket(row["proto_norm"], out, expected)
            if bucket == "other":
                bucket = "other__" + other_subtype(out, expected, row["proto_norm"])
        else:
            bucket = "no_output"
        mismatches.append(
            {
                "proto": row["proto"],
                "output": out,
                "expected": expected,
                "bucket": bucket,
            }
        )
    return mismatches


def write_report(
    mismatches: List[Dict[str, str]],
    ledger: Dict[str, Dict[str, str]],
    output_path: Path,
) -> None:
    # Partition mismatches by ledger lookup.
    tractable: List[Dict[str, str]] = []
    triaged: Dict[str, List[Tuple[Dict[str, str], Dict[str, str]]]] = defaultdict(list)
    matched_protos = set()
    for mm in mismatches:
        entry = ledger.get(mm["proto"])
        if entry is None:
            tractable.append(mm)
        else:
            triaged[entry["status"]].append((mm, entry))
            matched_protos.add(mm["proto"])

    stale = sorted(set(ledger) - matched_protos)
    total = len(mismatches)
    n_tractable = len(tractable)
    n_by_status = {s: len(triaged.get(s, [])) for s in sorted(VALID_STATUSES)}

    lines: List[str] = []
    lines.append("=" * 72)
    lines.append("OE KNOWN PROBLEMS / MISMATCH TRIAGE REPORT")
    lines.append("=" * 72)
    lines.append("")
    lines.append(f"Total mismatches:         {total}")
    lines.append(f"  Tractable (no ledger):  {n_tractable}")
    for status in sorted(VALID_STATUSES):
        lines.append(f"  {status:23s} {n_by_status[status]}")
    lines.append(f"Stale ledger entries:     {len(stale)}")
    lines.append("")
    lines.append("Tractable = candidate for the mismatch-loop methodology.")
    lines.append("Parked    = investigated, recorded as notable finding, no fix.")
    lines.append("Wontfix   = known structural issue, deliberately not addressing.")
    lines.append("Exception = documented in literature/notes as genuine exception.")
    lines.append("Open      = currently being investigated (transient).")
    lines.append("")

    # === TRACTABLE ===
    lines.append("=" * 72)
    lines.append(f"TRACTABLE MISMATCHES  ({n_tractable})")
    lines.append("=" * 72)
    lines.append("These mismatches have no ledger entry and are candidates for the")
    lines.append("mismatch-loop workflow (research dossier → review → implement).")
    lines.append("")
    if tractable:
        # Group by bucket for easier scanning.
        by_bucket: Dict[str, List[Dict[str, str]]] = defaultdict(list)
        for mm in tractable:
            by_bucket[mm["bucket"]].append(mm)
        for bucket in sorted(by_bucket):
            entries = by_bucket[bucket]
            lines.append(f"--- {bucket} ({len(entries)}) ---")
            for mm in entries:
                lines.append(
                    f"  {mm['proto']:18s} -> {mm['output']:20s} (expected {mm['expected']})"
                )
            lines.append("")
    else:
        lines.append("  (none)")
        lines.append("")

    # === TRIAGED ===
    for status in ("parked", "wontfix", "exception", "open"):
        items = triaged.get(status, [])
        lines.append("=" * 72)
        lines.append(f"{status.upper()}  ({len(items)})")
        lines.append("=" * 72)
        if not items:
            lines.append("  (none)")
            lines.append("")
            continue
        # Group by category.
        by_cat: Dict[str, List[Tuple[Dict[str, str], Dict[str, str]]]] = defaultdict(list)
        for mm, entry in items:
            by_cat[entry["category"] or "(uncategorized)"].append((mm, entry))
        for cat in sorted(by_cat):
            cat_items = by_cat[cat]
            lines.append(f"--- {cat} ({len(cat_items)}) ---")
            for mm, entry in cat_items:
                lines.append(
                    f"  {mm['proto']:18s} -> {mm['output']:20s} (expected {mm['expected']})"
                )
                if entry["reason"]:
                    lines.append(f"    reason: {entry['reason']}")
                if entry["refs"]:
                    lines.append(f"    refs:   {entry['refs']}")
                lines.append(f"    added:  {entry['added']}")
            lines.append("")

    # === STALE ===
    lines.append("=" * 72)
    lines.append(f"STALE LEDGER ENTRIES  ({len(stale)})")
    lines.append("=" * 72)
    lines.append("Ledger protos that no longer appear in the mismatch report.")
    lines.append("These may indicate fixed mismatches whose ledger entry should be")
    lines.append("removed, or proto-string drift between TSV and ledger.")
    lines.append("")
    if stale:
        for proto in stale:
            entry = ledger[proto]
            lines.append(
                f"  {proto:18s}  status={entry['status']}  category={entry['category']}"
            )
    else:
        lines.append("  (none)")
    lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    germanic_dir = TOOLS_DIR.parent
    repo_root = germanic_dir.parent
    parser.add_argument(
        "--tsv",
        default=str(germanic_dir / "data" / "germanic-aligned-final.tsv"),
    )
    parser.add_argument(
        "--bin",
        default=str(repo_root / "backend" / "old_english.bin"),
    )
    parser.add_argument(
        "--ledger",
        default=str(germanic_dir / "data" / "oe_known_problems.tsv"),
    )
    parser.add_argument(
        "--output",
        default=str(
            germanic_dir / "docs" / "debug_snapshots" / "oe_known_problems_report.txt"
        ),
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    ledger_path = Path(args.ledger).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()

    rows = load_rows(tsv_path)
    ledger = load_ledger(ledger_path)
    mismatches = collect_mismatches(rows, bin_path)
    write_report(mismatches, ledger, output_path)
    print(f"Wrote {output_path}", file=sys.stderr)
    print(
        f"Total mismatches: {len(mismatches)}; "
        f"tractable: {sum(1 for m in mismatches if m['proto'] not in ledger)}; "
        f"triaged: {sum(1 for m in mismatches if m['proto'] in ledger)}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
