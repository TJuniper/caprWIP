#!/usr/bin/env bash
# Rebuild the OE runtime bins into the ONE authoritative bin location
# (host: <repo>/backend, container: /usr/app) and record the build manifest.
#
# Steps: verify the generated executable-order views and sandbox are clean,
# clear stale snapshot bins, compile germanic.txt + the generated sandbox
# through the canonical runner, then write oe_build_manifest.json.
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/../.." && pwd)

python3 "$SCRIPT_DIR/cascade_order_manifest.py" --check
python3 "$SCRIPT_DIR/generate_oe_sandbox.py" --check

CAPR_TOOLS_DIR="$SCRIPT_DIR" python3 - <<'PY'
import os
import sys
sys.path.insert(0, os.environ["CAPR_TOOLS_DIR"])
import oe_pipeline
from capr_runtime import layout, run_in_runner, write_build_manifest

rt = layout()
run_in_runner("rm -f old_english_sandbox_after_*.bin", rt=rt, check=True)
# old_english_sandbox.txt begins with `source fsts/germanic.txt`, so one
# compile rebuilds the full production cascade AND every stage bin.
source = "fsts/old_english_sandbox.txt"
print(f"compiling {source} (sources fsts/germanic.txt) ...")
proc = run_in_runner(f"foma -q -l {source} -e quit", rt=rt,
                     capture_output=True, text=True)
if proc.returncode != 0:
    print(proc.stdout, file=sys.stderr)
    print(proc.stderr, file=sys.stderr)
    raise SystemExit(f"foma failed on {source}")
manifest = write_build_manifest(
    oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], rt=rt)
print(f"wrote {manifest}")
PY
python3 "$SCRIPT_DIR/oe_bin_sync_check.py"
