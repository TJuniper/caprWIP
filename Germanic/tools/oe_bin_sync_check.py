#!/usr/bin/env python3
"""Validate runtime OE bin freshness against the explicit build manifest.

The freshness contract is the build manifest (``oe_build_manifest.json``)
written into the authoritative runtime bin directory (host:
``<repo>/backend``; container: ``/usr/app``) by the rebuild entry points
(``adjudicate.py --evidence``, ``rebuild_oe_bins.sh``).  The check
compares the CURRENT source hashes (germanic.txt, generated
old_english_sandbox.txt, corpus TSV) to the hashes recorded at build
time, verifies the manifest expects exactly the executable model's
snapshot bins, and verifies every expected bin exists and is
nondegenerate.  mtimes are diagnostic only, never the authority.

Usage:
    python3 Germanic/tools/oe_bin_sync_check.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import check_build_manifest, layout  # noqa: E402


def main() -> int:
    rt = layout()
    expected = oe_pipeline.expected_snapshot_bins() + ["old_english.bin"]
    problems = check_build_manifest(expected, rt=rt)
    print(f"runtime bin dir: {rt.bin_dir}")
    print(f"build manifest:  {rt.build_manifest}")
    if problems:
        for problem in problems:
            print(f"STALE: {problem}", file=sys.stderr)
        print("Rebuild with: python3 Germanic/tools/adjudicate.py SCNNN "
              "--evidence, or bash Germanic/tools/rebuild_oe_bins.sh",
              file=sys.stderr)
        return 1
    print(f"fresh: {len(expected)} expected bins match the build manifest "
          "and current sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
