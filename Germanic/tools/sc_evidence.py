#!/usr/bin/env python3
"""Deterministic firing census for one sound change (container-side worker).

Normally invoked FOR the agent by:

    python3 Germanic/tools/adjudicate.py SCNNN --evidence

which rebuilds the stage bins first and then runs this script inside the
backend container. Direct use (debugging only):

    docker compose exec -T backend python3 /usr/app/tools/sc_evidence.py \
        PNWGmcLongELowering --min-mtime <epoch> [--witnesses "sheep; year"]

For the named executable rule it reports, for every selected Old English
corpus row, the form immediately BEFORE the rule's sandbox stage and the
form immediately AFTER it, listing every row the rule changes (the live
firing census) plus explicit before/after lines for any requested
chronology-witness lexemes even when unchanged.

Freshness contract: the stage bins used are validated against --min-mtime
(the epoch recorded just before the rebuild) and a minimum size, and the
sha256 of the live FST sources is printed. Stale or degenerate bins are a
fatal error — this script never silently falls back to whatever .bin
happens to exist, and it never reads bins from the fsts/ source directory.
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import MIN_BIN_BYTES, layout, sha256_of  # noqa: E402
from oe_pipeline import apply_down, display_form, evaluation_input, load_rows  # noqa: E402

# Stage truth comes from the shared executable model (oe_pipeline), which
# uses canonical Foma identifiers throughout — no alias table.
STAGES = [(s.foma_identifier, s.snapshot_bin)
          for s in oe_pipeline.named_stages()]


def find_stage(fst_identifier):
    """Return (index, stage_name, bin_name) for a registry fst_identifier."""
    for index, (name, bin_name) in enumerate(STAGES):
        if name == fst_identifier:
            return index, name, bin_name
    known = ", ".join(name for name, _ in STAGES)
    raise KeyError(
        f"{fst_identifier!r} is not a stage of the production OE cascade "
        f"(fsts/germanic.txt). Known stages: {known}"
    )


def validate_bin(path, min_mtime):
    """Fail loudly on missing, degenerate, or stale stage bins."""
    if not path.is_file():
        raise SystemExit(
            f"EVIDENCE FAILED: stage bin missing: {path}\n"
            "The sandbox rebuild did not produce it. Do not fall back to "
            "other copies; fix the rebuild."
        )
    size = path.stat().st_size
    if size < MIN_BIN_BYTES:
        raise SystemExit(
            f"EVIDENCE FAILED: stage bin {path} is only {size} bytes — a "
            "degenerate/failed build, not a usable transducer."
        )
    mtime = path.stat().st_mtime
    if min_mtime is not None and mtime < min_mtime:
        raise SystemExit(
            f"EVIDENCE FAILED: stage bin {path} (mtime {int(mtime)}) predates "
            f"the rebuild timestamp ({int(min_mtime)}). The census must run "
            "on freshly rebuilt bins, never stale pre-existing ones."
        )
    return size, mtime


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fst_identifier",
                        help="registry fst_identifier of the target rule")
    parser.add_argument("--min-mtime", type=int, default=None,
                        help="epoch seconds; stage bins older than this are "
                             "rejected as stale")
    parser.add_argument("--witnesses", default="",
                        help="semicolon-separated concept names to report "
                             "before/after for even when unchanged")
    args = parser.parse_args()

    rt = layout()
    bin_dir = rt.bin_dir
    tsv_path = rt.corpus_tsv
    fsts_dir = rt.fsts_dir

    index, tracer_name, bin_name = find_stage(args.fst_identifier)
    if index == 0:
        raise SystemExit("EVIDENCE FAILED: the proto-input stage has no "
                         "preceding stage to diff against.")
    prev_name, prev_bin_name = STAGES[index - 1]
    target_bin = bin_dir / bin_name
    prev_bin = bin_dir / prev_bin_name

    print("=== SC EVIDENCE CENSUS ===")
    print(f"rule: {args.fst_identifier} (tracer stage: {tracer_name}, "
          f"stage {index} of {len(STAGES) - 1})")
    print(f"previous stage: {prev_name}")
    print(f"canonical bin dir: {bin_dir}")
    print()
    print("=== FRESHNESS ===")
    for label in ("germanic.txt", "old_english_sandbox.txt"):
        print(f"{label} sha256: {sha256_of(fsts_dir / label)}")
    print(f"germanic-aligned-final.tsv sha256: {sha256_of(tsv_path)}")
    for path in (prev_bin, target_bin):
        size, mtime = validate_bin(path, args.min_mtime)
        print(f"{path.name}: {size} bytes, mtime {int(mtime)} "
              f"({time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))})")
    for path in (prev_bin, target_bin):
        stale = fsts_dir / path.name
        if stale.exists():
            print(f"NOTE: ignoring duplicate copy {stale} "
                  f"({stale.stat().st_size} bytes) — bins in the fsts/ source "
                  "directory are never authoritative.")
    print()

    rows = load_rows(tsv_path)
    witnesses = {w.strip() for w in args.witnesses.split(";") if w.strip()}
    firings = []
    witness_lines = []
    for row in rows:
        before = apply_down(prev_bin, evaluation_input(row))
        after = apply_down(target_bin, evaluation_input(row))
        line = (f"{row['concept']}\t{row['proto']}\t"
                f"{' | '.join(display_form(form) for form in before) or '(no output)'}\t"
                f"{' | '.join(display_form(form) for form in after) or '(no output)'}\t"
                f"attested: {row['counterpart']}")
        if before != after:
            firings.append(line)
        if row["concept"] in witnesses:
            status = "CHANGED" if before != after else "unchanged"
            witness_lines.append(f"[{status}] {line}")

    print(f"=== LIVE FIRING CENSUS ({len(firings)} of {len(rows)} selected "
          "corpus rows changed) ===")
    print("concept\tprotoform\tbefore rule\tafter rule\tattested")
    for line in firings:
        print(line)
    if witnesses:
        print()
        print("=== CHRONOLOGY WITNESS PRE/POST ===")
        found = {line.split("\t")[0].split("] ", 1)[-1] for line in witness_lines}
        for line in witness_lines:
            print(line)
        for missing in sorted(witnesses - found):
            print(f"[NOT IN SELECTED CORPUS] {missing}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
