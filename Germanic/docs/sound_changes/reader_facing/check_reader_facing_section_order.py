#!/usr/bin/env python3
"""Verify the assembled reader-facing order against the generated authorities.

The presentation order comes from the GENERATED registry/reader_manifest.tsv
(files ordered by minimum cascade position inside human-assigned chapters);
per-SC cascade positions come from the GENERATED registry/current_sc_state.tsv.
This checker holds no file list and reads no hand-maintained order column.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SC_DIR = ROOT.parent
DEFAULT_MANIFEST = SC_DIR / "registry" / "reader_manifest.tsv"
CURRENT_SC_STATE = SC_DIR / "registry" / "current_sc_state.tsv"


def read_tsv(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def load_cascade_positions() -> dict[str, int]:
    positions: dict[str, int] = {}
    for row in read_tsv(CURRENT_SC_STATE):
        pos = (row.get("cascade_position") or "").strip()
        if pos:
            positions[row["sc_id"]] = int(pos)
    if not positions:
        raise ValueError(f"No cascade positions found in {CURRENT_SC_STATE}")
    return positions


def chapter_sc_numbers(path: Path) -> list[str]:
    numbers: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"##\s+SC(\d{3})\.\s", line)
        if match:
            numbers.append(f"SC{match.group(1)}")
    if not numbers:
        raise ValueError(f"No SC-numbered rule headings found in {path}")
    return numbers


def verify(manifest: Path) -> tuple[list[str], list[str], list[str]]:
    positions = load_cascade_positions()
    rows = read_tsv(manifest)
    if not rows:
        raise ValueError(f"No rows found in {manifest}")
    chapter_files = [row["reader_file"] for row in rows]

    flattened: list[str] = []
    for row in rows:
        name = row["reader_file"]
        chapter_path = ROOT / name
        if not chapter_path.exists():
            raise FileNotFoundError(f"Missing chapter file in manifest: {chapter_path}")
        numbers = chapter_sc_numbers(chapter_path)
        missing = [change_id for change_id in numbers if change_id not in positions]
        if missing:
            raise ValueError(f"SC id(s) without a cascade position in {name}: {missing}")
        # Internal SC order within each file must follow the cascade order
        chapter_expected = sorted(numbers, key=lambda change_id: positions[change_id])
        if numbers != chapter_expected:
            raise ValueError(f"Internal SC order mismatch in {name}: {numbers} vs {chapter_expected}")
        flattened.extend(numbers)

    # Files must be ordered by strictly increasing minimum cascade position
    mins = [min(positions[sc] for sc in chapter_sc_numbers(ROOT / name))
            for name in chapter_files]
    if mins != sorted(mins) or len(mins) != len(set(mins)):
        raise ValueError(
            f"Manifest file order does not follow cascade order (min positions {mins})")

    unique_flattened: list[str] = []
    seen_nonadjacent: set[str] = set()
    for change_id in flattened:
        if unique_flattened and unique_flattened[-1] == change_id:
            continue
        if change_id in seen_nonadjacent:
            raise ValueError(f"Non-adjacent repeated SC id in build order: {change_id}")
        unique_flattened.append(change_id)
        seen_nonadjacent.add(change_id)

    return chapter_files, flattened, unique_flattened


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify the reader-facing chapter order against the generated book manifest."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Generated reader manifest (registry/reader_manifest.tsv).",
    )
    args = parser.parse_args()

    chapter_files, flattened, unique_flattened = verify(args.manifest.resolve())
    print(f"Verified reader-facing order for {args.manifest} [generated manifest]")
    print("Chapters:")
    for chapter in chapter_files:
        print(f"  - {chapter}")
    print("SC order:")
    print("  " + ", ".join(flattened))
    print("Unique SC order:")
    print("  " + ", ".join(unique_flattened))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
