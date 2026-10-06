#!/usr/bin/env python3
"""Generate the executable-order views from the shared pipeline model.

The ONE authority for executable order is the production ``OldEnglish``
composition in ``Germanic/fsts/germanic.txt``, parsed by
``Germanic/tools/oe_pipeline.py`` (structural bundles are marked
``# capr:bundle`` in the FST source and expanded recursively).

This tool emits two GENERATED views under
``Germanic/docs/sound_changes/cascade_baseline/``:

``cascade_order_manifest.tsv``
    Legacy-compatible SC cascade-position view (columns ``position``,
    ``foma_identifier``, ``origin_block``).  Covers exactly the stages that
    carry a ``cascade_position`` — the numbering used throughout the
    scientific records.  Unchanged format; do not renumber.

``executable_model.tsv``
    The complete physical execution sequence from the Proto-Germanic input
    filter to the Old English surface, including the prelude and surface
    stages that the legacy numbering omits.  Columns: ``exec_index``,
    ``cascade_position`` (empty for prelude/surface stages),
    ``foma_identifier``, ``origin_block``, ``kind``, ``snapshot_bin``,
    ``sc_id``.  This is also the exec_index <-> cascade_position mapping.

The views are *descriptive*: they record what the cascade currently does.
Historical stage/scope judgements live in the semantic registry.

Pure text parsing; needs neither foma nor flookup and runs on the host.

Usage:
    python3 Germanic/tools/cascade_order_manifest.py            # write views
    python3 Germanic/tools/cascade_order_manifest.py --check    # verify clean
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import layout  # noqa: E402

BASELINE_DIR = layout().docs_dir / "sound_changes" / "cascade_baseline"
MANIFEST_OUT = BASELINE_DIR / "cascade_order_manifest.tsv"
MODEL_OUT = BASELINE_DIR / "executable_model.tsv"


def manifest_text() -> str:
    lines = ["position\tfoma_identifier\torigin_block"]
    for s in oe_pipeline.named_stages():
        if s.cascade_position is None:
            continue
        lines.append(f"{s.cascade_position}\t{s.foma_identifier}\t{s.origin_block}")
    return "\n".join(lines) + "\n"


def model_text() -> str:
    lines = [
        "# GENERATED FILE — DO NOT EDIT.",
        "# Complete production Old English execution sequence (root: regex OldEnglish).",
        "# Source: Germanic/fsts/germanic.txt; model: Germanic/tools/oe_pipeline.py;",
        "# generator: Germanic/tools/cascade_order_manifest.py.",
        "# cascade_position is the legacy SC position space (empty for the",
        "# proto-input/PGmc prelude and the surface filter); exec_index is the",
        "# complete physical order. sc_id is joined from registry/sc_registry.tsv.",
        "exec_index\tcascade_position\tfoma_identifier\torigin_block\tkind\tsnapshot_bin\tsc_id",
    ]
    for s in oe_pipeline.stages():
        pos = "" if s.cascade_position is None else str(s.cascade_position)
        if s.kind == "named":
            lines.append(f"{s.exec_index}\t{pos}\t{s.foma_identifier}\t"
                         f"{s.origin_block}\tnamed\t{s.snapshot_bin}\t"
                         f"{oe_pipeline.sc_id(s.foma_identifier)}")
        else:
            lines.append(f"{s.exec_index}\t{pos}\t<inline>\t{s.origin_block}\t"
                         f"inline\t\t")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fst", type=Path, default=None,
                        help="Override germanic.txt path (debugging)")
    parser.add_argument("--check", action="store_true",
                        help="Fail if the committed views differ from the model")
    args = parser.parse_args()

    if args.fst is not None:
        stages = oe_pipeline.parse_stages(args.fst)
        for s in stages:
            print(f"{s.exec_index}\t{s.cascade_position or ''}\t"
                  f"{s.foma_identifier or s.inline_text}\t{s.origin_block}")
        return 0

    outputs = {MANIFEST_OUT: manifest_text(), MODEL_OUT: model_text()}
    stale = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        if args.check:
            stale.append(path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path}")
    if args.check:
        if stale:
            for p in stale:
                print(f"STALE VIEW: {p} does not match germanic.txt — run "
                      "python3 Germanic/tools/cascade_order_manifest.py",
                      file=sys.stderr)
            return 1
        print("executable-order views are clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
