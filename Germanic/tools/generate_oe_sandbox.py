#!/usr/bin/env python3
"""Generate fsts/old_english_sandbox.txt from the shared executable model.

The sandbox is a GENERATED artifact: one cumulative trace checkpoint per
named stage of the production Old English cascade (model:
``Germanic/tools/oe_pipeline.py``; authority: the ``OldEnglish``
composition in ``Germanic/fsts/germanic.txt``).  Moving a production rule
in germanic.txt automatically moves its sandbox checkpoint on the next
regeneration — the sandbox can no longer drift silently: ``--check``
fails whenever the committed sandbox differs from what the production
FST currently implies.

Usage:
    python3 Germanic/tools/generate_oe_sandbox.py            # (re)write
    python3 Germanic/tools/generate_oe_sandbox.py --check    # verify clean
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import layout  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Fail if the committed sandbox differs from the model")
    args = parser.parse_args()

    out = layout().sandbox_fst
    text = oe_pipeline.sandbox_text()
    current = out.read_text(encoding="utf-8") if out.exists() else None
    if current == text:
        if args.check:
            print("old_english_sandbox.txt is clean")
        return 0
    if args.check:
        print(f"STALE SANDBOX: {out} does not match the production cascade — "
              "run python3 Germanic/tools/generate_oe_sandbox.py",
              file=sys.stderr)
        return 1
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out} ({len(oe_pipeline.named_stages())} checkpoints)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
