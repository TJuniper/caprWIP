#!/usr/bin/env python3
"""Bucket PGmc→OE mismatches with a split for true i‑umlaut vs fronting misses."""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple
from oe_pipeline import evaluation_input, load_rows

PROTO_STRIP_RE = re.compile(r"[{}*\s\-/()]")

# Treat these as vowels in the proto stream when looking for an i/j trigger.
PROTO_VOWELS = set("aeiouyāēīōūǣȳ")
PROTO_TRIGGERS = set("ijī")
PROTO_DIPHTHONGS = ("ai", "au", "eu", "iu")

FRONT_VOWELS = set("æǣeiīyȳ")
BACK_VOWELS = set("aāoōuū")
LONG_VOWELS = set("āēīōūǣȳ")
PALATAL_MARKERS = ("ċ", "ġ", "sc", "cg")
BREAKING_DIPHTHONGS = ("ēa", "ēo", "īe", "ea", "eo", "ie")


def normalize_proto(raw: str) -> str:
    return PROTO_STRIP_RE.sub("", raw or "")


def apply_down(bin_path: Path, form: str) -> List[str]:
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=(form + "\n").encode("utf-8"),
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


def has_front(s: str) -> bool:
    return any(ch in s for ch in FRONT_VOWELS) or any(d in s for d in ("ie", "īe", "eo", "ēo", "ea", "ēa"))


def has_back(s: str) -> bool:
    return any(ch in s for ch in BACK_VOWELS)


def has_long(s: str) -> bool:
    return any(ch in s for ch in LONG_VOWELS) or any(d in s for d in ("ēa", "ēo", "īe"))


def has_breaking_diph(s: str) -> bool:
    return any(d in s for d in BREAKING_DIPHTHONGS)


def consonant_skeleton(s: str) -> str:
    """Strip vowels/diphthongs to compare consonant material."""
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    for ch in LONG_VOWELS | FRONT_VOWELS | BACK_VOWELS:
        s = s.replace(ch, "")
    return s


def has_palatal_marker(s: str) -> bool:
    return any(marker in s for marker in PALATAL_MARKERS)


def trigger_in_next_syllable(proto_norm: str) -> bool:
    """Heuristic: an i/ī/j appears before any other vowel after the first vowel."""
    first_vowel_idx = None
    for idx, ch in enumerate(proto_norm):
        if ch in PROTO_VOWELS:
            first_vowel_idx = idx
            break
    if first_vowel_idx is None:
        return False
    for ch in proto_norm[first_vowel_idx + 1 :]:
        if ch in PROTO_TRIGGERS:
            return True
        if ch in PROTO_VOWELS:
            return False
    return False


def proto_first_vowel_unit(proto_norm: str) -> str:
    for i in range(len(proto_norm)):
        for diph in PROTO_DIPHTHONGS:
            if proto_norm.startswith(diph, i):
                return diph
        ch = proto_norm[i]
        if ch in PROTO_VOWELS:
            return ch
    return ""


def is_a_fronting_context(proto_norm: str) -> bool:
    first = proto_first_vowel_unit(proto_norm)
    return first in {"a", "ā"}


def bucket_mismatches(
    rows: Iterable[Dict[str, str]], bin_path: Path
) -> Dict[str, List[Tuple[str, str, str]]]:
    buckets: Dict[str, List[Tuple[str, str, str]]] = defaultdict(list)
    for row in rows:
        outputs = apply_down(bin_path, evaluation_input(row))
        expected = row["counterpart"]
        if not outputs:
            buckets["no_output"].append((row["proto"], "+?", expected))
            continue
        if expected in outputs:
            continue
        out = outputs[0]
        if has_breaking_diph(expected) and not has_breaking_diph(out):
            buckets["breaking_missing"].append((row["proto"], out, expected))
            continue
        if has_long(expected) and not has_long(out):
            expected_cons = consonant_skeleton(expected)
            out_cons = consonant_skeleton(out)
            if expected_cons and expected_cons != out_cons and expected_cons in out_cons:
                buckets["other"].append((row["proto"], out, expected))
            else:
                buckets["long_vowel_missing"].append((row["proto"], out, expected))
            continue
        if has_front(expected) and has_back(out):
            if trigger_in_next_syllable(row["proto_norm"]):
                buckets["i_umlaut_missing_true"].append((row["proto"], out, expected))
            elif is_a_fronting_context(row["proto_norm"]):
                buckets["fronting_missing_no_trigger"].append((row["proto"], out, expected))
            else:
                buckets["other"].append((row["proto"], out, expected))
            continue
        if has_palatal_marker(expected) and not has_palatal_marker(out):
            buckets["palatalization_missing"].append((row["proto"], out, expected))
            continue
        buckets["other"].append((row["proto"], out, expected))
    return buckets


def write_report(buckets: Dict[str, List[Tuple[str, str, str]]], output_path: Path) -> None:
    order = [
        "i_umlaut_missing_true",
        "fronting_missing_no_trigger",
        "other",
        "breaking_missing",
        "no_output",
        "long_vowel_missing",
        "palatalization_missing",
    ]
    mismatch_total = sum(len(v) for v in buckets.values())
    lines: List[str] = []
    lines.append(f"Total mismatches: {mismatch_total}")
    lines.append("")
    for key in order:
        lines.append(f"{key}: {len(buckets.get(key, []))}")
    lines.append("")
    lines.append("Examples:")
    for key in order:
        lines.append(f"{key}:")
        for proto, out, expected in buckets.get(key, [])[:5]:
            lines.append(f"  {proto} -> {out} (expected {expected})")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
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
        "--output",
        default=str(Path("docs/debug_snapshots/oe_mismatch_patterns_i_umlaut_split.txt")),
        help="Report output path (default: %(default)s)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = load_rows(tsv_path)
    buckets = bucket_mismatches(rows, bin_path)
    write_report(buckets, output_path)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
