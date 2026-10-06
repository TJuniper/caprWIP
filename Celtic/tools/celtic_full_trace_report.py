#!/usr/bin/env python3
"""Full Celtic bucket report with traces using the Celtic transducer(s).

This is an adapted copy of Germanic/tools/oe_full_trace_report.py that
defaults to the Celtic dataset and FSTs. It supports either a staged
cascade (if you supply a --bin-dir containing stage .bin files and set
STAGES appropriately) or a simple single-step application of the provided
binary via --bin (the common case: pass one language bin such as
Celtic/fsts/old_irish.bin).
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple, Optional

# Reuse most helper logic from the OE report — vowel/consonant heuristics
# remain useful for simple mismatch bucketing.
PROTO_STRIP_RE = re.compile(r"[{}*\s/()]")

PROTO_VOWELS = set("aeiouyāēīōūǣȳ")
PROTO_TRIGGERS = set("ijī")
PROTO_DIPHTHONGS = ("ai", "au", "eu", "iu")

FRONT_VOWELS = set("æǣeiīyȳ")
BACK_VOWELS = set("aāoōuū")
LONG_VOWELS = set("āēīōūǣȳ")
HIGH_FRONT_VOWELS = set("iīyȳ")
OE_DIPHTHONGS = ("īe", "ie", "ēo", "eo", "ēa", "ea")
PALATAL_MARKERS = ("ċ", "ġ", "sc", "cg")
BREAKING_DIPHTHONGS = ("ēa", "ēo", "īe", "ea", "eo", "ie")

# For Celtic there is no prefilled staged cascade here. If needed, populate
# STAGES with tuples (label, bin_name) that exist in --bin-dir. When empty
# the script will simply apply the single provided --bin to each protoform.
STAGES: List[Tuple[str, str]] = []
STAGE_HEADERS: Dict[str, str] = {}


def normalize_proto(raw: str) -> str:
    normalized = PROTO_STRIP_RE.sub("", raw or "")
    return normalized


def load_rows(tsv_path: Path, doculect: Optional[str] = None) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if doculect and row.get("DOCULECT") != doculect:
                continue
            proto = (row.get("PROTOFORM") or "").strip()
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not proto or not counterpart or counterpart == "-":
                continue
            norm = normalize_proto(proto)
            if not norm:
                continue
            rows.append(
                {
                    "concept": row.get("CONCEPT", ""),
                    "proto": proto,
                    "proto_norm": norm,
                    "counterpart": counterpart,
                }
            )
    return rows


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
    # dedupe while preserving order
    seen = set()
    deduped: List[str] = []
    for item in outputs:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def run_stage(bin_dir: Path, bin_name: str, form: str) -> List[str]:
    stage_path = (bin_dir / bin_name).resolve()
    proc = subprocess.run(
        ["flookup", "-i", str(stage_path)],
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
        out = parts[1] if len(parts) == 2 else raw
        outputs.append(out or "+?")
    if not outputs:
        outputs.append("+?")
    seen = set()
    deduped: List[str] = []
    for item in outputs:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


# --- reuse helper predicates from the original script ---

def has_front(s: str) -> bool:
    return any(ch in s for ch in FRONT_VOWELS) or any(d in s for d in ("ie", "īe", "eo", "ēo", "ea", "ēa"))


def has_back(s: str) -> bool:
    return any(ch in s for ch in BACK_VOWELS)


def has_long(s: str) -> bool:
    return any(ch in s for ch in LONG_VOWELS) or any(d in s for d in ("ēa", "ēo", "īe"))


def has_high_front(s: str) -> bool:
    return any(ch in s for ch in HIGH_FRONT_VOWELS) or any(d in s for d in ("ie", "īe"))


def oe_first_vowel_unit(s: str) -> str:
    for i in range(len(s)):
        for diph in OE_DIPHTHONGS:
            if s.startswith(diph, i):
                return diph
        ch = s[i]
        if ch in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS):
            return ch
    return ""


def oe_first_is_front(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in FRONT_VOWELS or unit in {"ie", "īe", "eo", "ēo", "ea", "ēa"}


def oe_first_is_back(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in BACK_VOWELS


def oe_first_is_high_front(s: str) -> bool:
    unit = oe_first_vowel_unit(s)
    return unit in HIGH_FRONT_VOWELS or unit in {"ie", "īe"}


def vowel_sequence(s: str) -> List[str]:
    seq: List[str] = []
    i = 0
    while i < len(s):
        pair = s[i : i + 2]
        if pair in BREAKING_DIPHTHONGS:
            seq.append(pair)
            i += 2
            continue
        if s[i] in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS):
            seq.append(s[i])
        i += 1
    return seq


def consonant_sequence(s: str) -> str:
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    return "".join(ch for ch in s if ch not in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS))


def has_palatal_variant_mismatch(out: str, expected: str) -> bool:
    exp_fine = ("ċ" in expected) or ("ġ" in expected)
    exp_sc = ("sc" in expected) or ("cg" in expected)
    out_fine = ("ċ" in out) or ("ġ" in out)
    out_sc = ("sc" in out) or ("cg" in out)
    return (exp_fine and out_sc and not out_fine) or (exp_sc and out_fine and not out_sc)


def has_consonant_gemination(s: str) -> bool:
    vowels = FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i] not in vowels:
            return True
    return False


def has_breaking_diph(s: str) -> bool:
    return any(d in s for d in BREAKING_DIPHTHONGS)


def consonant_skeleton(s: str) -> str:
    for diph in BREAKING_DIPHTHONGS:
        s = s.replace(diph, "")
    for ch in LONG_VOWELS | FRONT_VOWELS | BACK_VOWELS:
        s = s.replace(ch, "")
    return s


def has_palatal_marker(s: str) -> bool:
    return any(marker in s for marker in PALATAL_MARKERS)


def trigger_in_next_syllable(proto_norm: str) -> bool:
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
    return proto_first_vowel_unit(proto_norm) in {"a", "ā"}


def ends_with_vowel(s: str) -> bool:
    return bool(s) and s[-1] in (FRONT_VOWELS | BACK_VOWELS | LONG_VOWELS)


def proto_mismatch_suspect(proto_norm: str, out: str, expected: str) -> bool:
    if trigger_in_next_syllable(proto_norm):
        return False
    if not oe_first_is_high_front(expected):
        return False
    if oe_first_is_high_front(out):
        return False
    if not oe_first_is_back(out):
        return False
    first = proto_first_vowel_unit(proto_norm)
    if first in {"e", "ē", "i", "ī", "æ", "ǣ", "y", "ȳ", "eu", "iu"}:
        return True
    return False


def base_bucket(proto_norm: str, out: str, expected: str) -> str:
    if proto_mismatch_suspect(proto_norm, out, expected):
        return "proto_mismatch_suspect"
    if has_breaking_diph(expected) and not has_breaking_diph(out):
        return "breaking_missing"
    if has_long(expected) and not has_long(out):
        expected_cons = consonant_skeleton(expected)
        out_cons = consonant_skeleton(out)
        if expected_cons and expected_cons != out_cons and expected_cons in out_cons:
            return "other"
        return "long_vowel_missing"
    if oe_first_is_front(expected) and oe_first_is_back(out):
        if trigger_in_next_syllable(proto_norm):
            return "i_umlaut_missing_true"
        if is_a_fronting_context(proto_norm):
            return "fronting_missing_no_trigger"
        return "other"
    if has_palatal_marker(expected) and not has_palatal_marker(out):
        return "palatalization_missing"
    return "other"


def other_subtype(out: str, expected: str) -> str:
    if expected.endswith("n") and not out.endswith("n"):
        return "final_n_missing"
    if ends_with_vowel(expected) and not ends_with_vowel(out):
        return "final_vowel_missing"
    if ends_with_vowel(out) and not ends_with_vowel(expected):
        return "final_vowel_extra"
    if has_breaking_diph(out) and not has_breaking_diph(expected):
        return "breaking_extra_other"
    if has_palatal_marker(out) and not has_palatal_marker(expected):
        return "palatal_extra_other"
    if has_palatal_variant_mismatch(out, expected):
        return "palatal_marker_variant"
    if has_long(out) and not has_long(expected):
        return "length_extra_other"
    if oe_first_is_front(expected) and oe_first_is_back(out):
        return "front_expected_back_out"
    if oe_first_is_back(expected) and oe_first_is_front(out):
        return "back_expected_front_out"
    out_cons = consonant_sequence(out)
    expected_cons = consonant_sequence(expected)
    if out_cons == expected_cons:
        out_vowels = vowel_sequence(out)
        expected_vowels = vowel_sequence(expected)
        if len(expected_vowels) > len(out_vowels):
            return "epenthetic_vowel_missing"
        if len(expected_vowels) == len(out_vowels) and expected_vowels != out_vowels:
            return "vowel_quality_other"
    if has_consonant_gemination(out) and not has_consonant_gemination(expected):
        return "gemination_extra"
    if out_cons != expected_cons:
        return "consonant_mismatch_other"
    return "uncategorized"


def bucket_entry(proto_norm: str, out: str, expected: str) -> str:
    bucket = base_bucket(proto_norm, out, expected)
    if bucket == "other":
        return other_subtype(out, expected)
    return bucket


def trace_lexeme(proto_norm: str, bin_dir: Path, single_bin: Optional[Path]) -> List[Tuple[str, List[str]]]:
    # If STAGES were supplied, run the staged cascade. Otherwise apply the
    # single binary (single_bin) and return a one-step trace.
    if STAGES:
        trace: List[Tuple[str, List[str]]] = []
        last_outputs: List[str] | None = None
        for label, bin_name in STAGES:
            outputs = run_stage(bin_dir, bin_name, proto_norm)
            usable = [out for out in outputs if out != "+?"]
            if not usable:
                outputs = last_outputs if last_outputs is not None else [proto_norm]
                label = f"{label} [no-change]"
            else:
                outputs = usable
                if last_outputs is not None and outputs == last_outputs:
                    label = f"{label} [no-change]"
            last_outputs = outputs
            trace.append((label, outputs))
        return trace
    else:
        if single_bin is None:
            raise RuntimeError("No STAGES defined and no --bin provided to apply the transducer")
        outputs = apply_down(single_bin, proto_norm)
        if not outputs:
            outputs = ["+?"]
        return [("Transducer", outputs)]


def write_report(
    rows: Iterable[Dict[str, str]],
    bin_path: Path,
    bin_dir: Path,
    output_path: Path,
    trace_all: bool = False,
) -> None:
    buckets: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    stage_fires: Dict[str, List[str]] = defaultdict(list)
    for row in rows:
        outputs = apply_down(bin_path, row["proto_norm"]) if not STAGES else apply_down(bin_path, row["proto_norm"])  # keep apply_down for immediate outputs
        expected = row["counterpart"]
        if not outputs:
            bucket = "no_output"
        elif expected in outputs:
            bucket = "exact_match"
        elif len(outputs) > 1:
            bucket = "multiple_outputs"
        else:
            bucket = bucket_entry(row["proto_norm"], outputs[0], expected)
        row_copy = dict(row)
        row_copy["outputs"] = ", ".join(outputs) if outputs else "+?"
        buckets[bucket].append(row_copy)

    order = [
        "exact_match",
        "multiple_outputs",
        "no_output",
        "proto_mismatch_suspect",
        "breaking_missing",
        "long_vowel_missing",
        "palatalization_missing",
        "final_vowel_extra",
        "length_extra_other",
        "front_expected_back_out",
        "final_vowel_missing",
        "breaking_extra_other",
        "final_n_missing",
        "palatal_extra_other",
        "back_expected_front_out",
        "palatal_marker_variant",
        "epenthetic_vowel_missing",
        "vowel_quality_other",
        "gemination_extra",
        "consonant_mismatch_other",
        "uncategorized",
    ]

    lines: List[str] = []
    for bucket in order:
        items = buckets.get(bucket, [])
        if not items:
            continue
        lines.append(f"=== BUCKET: {bucket} ({len(items)}) ===")
        lines.append("")
        for row in items:
            lines.append(f"--- {row['concept']} ---")
            lines.append(f"PROTO: {row['proto']}")
            lines.append(f"EXPECTED: {row['counterpart']}")
            lines.append(f"OUTPUTS: {row['outputs']}")
            lines.append("")
            lexeme_label = f"{row['concept']} :: {row['proto']}"
            for label, outputs in trace_lexeme(row["proto_norm"], bin_dir, bin_path):
                base_label = label.split(" [", 1)[0]
                header = STAGE_HEADERS.get(base_label)
                if header is not None:
                    lines.append("")
                    lines.append(header)
                    lines.append("")
                pretty = ", ".join(outputs)
                lines.append(f"{label}: {pretty}")
            lines.append("")
        lines.append("")

    lines.append("=== STAGE FIRING SUMMARY ===")
    lines.append("")
    for label, _bin in STAGES:
        fired = stage_fires.get(label, [])
        lines.append(f"{label}: {len(fired)}")
        if fired:
            lines.append(", ".join(fired))
        lines.append("")

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    tools_dir = Path(__file__).resolve().parent
    celtic_dir = tools_dir.parent
    repo_root = celtic_dir.parent
    parser.add_argument(
        "--tsv",
        default=str(celtic_dir / "data" / "celtic-aligned-final.tsv"),
        help="Aligned TSV with Celtic rows (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        default=str(celtic_dir / "fsts" / "old_irish.bin"),
        help="FST binary used for apply-down (default: %(default)s).",
    )
    parser.add_argument(
        "--bin-dir",
        default=str(celtic_dir / "fsts"),
        help="Directory containing stage .bin files if available (default: %(default)s)",
    )
    parser.add_argument(
        "--doculect",
        default=None,
        help="If set, only include rows whose DOCULECT column equals this value (default: include all)",
    )
    parser.add_argument(
        "--output",
        default=str(celtic_dir / "docs" / "debug_snapshots" / "celtic_full_trace_report.txt"),
        help="Report output path (default: %(default)s)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Trace all entries including exact_match (default: mismatches only)",
    )
    args = parser.parse_args()

    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    bin_dir = Path(args.bin_dir).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = load_rows(tsv_path, doculect=args.doculect)
    write_report(rows, bin_path, bin_dir, output_path, trace_all=args.all)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
