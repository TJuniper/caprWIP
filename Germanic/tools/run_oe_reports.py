#!/usr/bin/env python3
"""Run the full Old English trace report and mismatch report together."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Optional


def _find_flookup_dir() -> Optional[Path]:
    found = shutil.which("flookup")
    if found:
        return Path(found).parent
    home = Path.home()
    candidate_root = home / "build" / "foma"
    if not candidate_root.exists():
        return None
    for path in candidate_root.rglob("flookup"):
        if path.is_file():
            return path.parent
    return None


def _label_to_suffix(label: str | None) -> str:
    if not label:
        return ""
    return label if label.startswith("_") else f"_{label}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate the OE full trace report and mismatch report together."
    )
    parser.add_argument(
        "--output-dir",
        default="docs/debug_snapshots",
        help="Directory for report outputs (default: %(default)s)",
    )
    parser.add_argument(
        "--label",
        help="Optional suffix label appended to report filenames (e.g. after_move)",
    )
    parser.add_argument(
        "--tsv",
        help="Override aligned TSV path passed to report scripts",
    )
    parser.add_argument(
        "--bin",
        help="Override generator FST bin passed to report scripts",
    )
    parser.add_argument(
        "--bin-dir",
        help="Override sandbox bin directory passed to report scripts",
    )
    parser.add_argument(
        "--skip-bin-check",
        action="store_true",
        help="Skip OE bin freshness/sync check before running reports",
    )
    parser.add_argument(
        "--bin-check-warn-only",
        action="store_true",
        help="Warn instead of failing when bins are missing or stale",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = _label_to_suffix(args.label)
    today = date.today().isoformat()

    full_report = output_dir / f"oe_full_trace_report_{today}{suffix}.txt"
    mismatch_report = output_dir / f"oe_mismatch_report_{today}{suffix}.txt"
    known_problems_report = output_dir / f"oe_known_problems_report_{today}{suffix}.txt"

    env = os.environ.copy()
    flookup_dir = _find_flookup_dir()
    if flookup_dir:
        env["PATH"] = f"{flookup_dir}{os.pathsep}{env.get('PATH','')}"

    tools_dir = Path(__file__).resolve().parent

    def run_report(script: Path, output_path: Path) -> None:
        cmd = [sys.executable, str(script), "--output", str(output_path)]
        if args.tsv:
            cmd.extend(["--tsv", args.tsv])
        if args.bin:
            cmd.extend(["--bin", args.bin])
        if args.bin_dir and script.name == "oe_full_trace_report.py":
            cmd.extend(["--bin-dir", args.bin_dir])
        subprocess.run(cmd, check=True, env=env)

    if not args.skip_bin_check:
        check_cmd = [sys.executable, str(tools_dir / "oe_bin_sync_check.py")]
        result = subprocess.run(check_cmd)
        if result.returncode != 0:
            if args.bin_check_warn_only:
                print("WARNING: bin freshness check failed; continuing "
                      "(--bin-check-warn-only)", file=sys.stderr)
            else:
                raise SystemExit("bin freshness check failed; rebuild the bins "
                                 "or pass --skip-bin-check/--bin-check-warn-only")

    run_report(tools_dir / "oe_full_trace_report.py", full_report)
    run_report(tools_dir / "oe_mismatch_report.py", mismatch_report)
    run_report(tools_dir / "oe_known_problems_report.py", known_problems_report)

    print(f"Wrote {full_report}")
    print(f"Wrote {mismatch_report}")
    print(f"Wrote {known_problems_report}")


if __name__ == "__main__":
    main()
