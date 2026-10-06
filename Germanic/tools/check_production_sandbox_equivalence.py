#!/usr/bin/env python3
"""Semantic equivalence: production old_english.bin vs final generated sandbox stage.

Canonical infrastructure regression (fail closed). After a canonical rebuild,
the production transducer and the last generated-sandbox checkpoint
(old_english_sandbox_after_<final stage>.bin) must give IDENTICAL output
multisets for every selected Old English corpus row. This protects against
parser omission, bad recursive bundle expansion, mishandled inline
expressions, sandbox composition errors, and future bundle-marker mistakes.

Binary hashes are never compared (foma is byte-nondeterministic); semantics
are.

Runs wherever flookup is available (the backend container, or a host with
foma). On success writes a small evidence file,
docs/sound_changes/cascade_baseline/oe_equivalence_report.json, recording the
source hashes the equivalence was proven for; the guard tests validate that
evidence against the live sources fail-closed.

Usage:
    python3 Germanic/tools/check_production_sandbox_equivalence.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List, Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import check_build_manifest, layout, sha256_of  # noqa: E402

EVIDENCE_NAME = "oe_equivalence_report.json"


def evidence_path(rt=None) -> Path:
    rt = rt or layout()
    return rt.docs_dir / "sound_changes" / "cascade_baseline" / EVIDENCE_NAME


def batch_outputs(bin_path: Path, forms: Sequence[str]) -> List[List[str]]:
    """Per-input flookup output lists WITH multiplicity, in one process."""
    markers = [f"__EQUIV_BOUNDARY_{i:04d}__" for i in range(len(forms))]
    if any(form in markers for form in forms):
        raise RuntimeError("input forms collide with batch boundary markers")
    batched: List[str] = []
    for form, marker in zip(forms, markers):
        batched.append(form)
        batched.append(marker)
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=("\n".join(batched) + "\n").encode("utf-8"),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
    )
    grouped: List[List[str]] = []
    current: List[str] = []
    marker_index = 0
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        input_form, _, output = raw.partition("\t")
        if marker_index < len(markers) and input_form == markers[marker_index]:
            grouped.append(current)
            current = []
            marker_index += 1
            continue
        if output and output != "+?":
            current.append(output)
    if marker_index != len(markers) or len(grouped) != len(forms):
        raise RuntimeError("batch flookup boundary mismatch")
    return grouped


def main() -> int:
    rt = layout()
    expected_bins = oe_pipeline.expected_snapshot_bins() + ["old_english.bin"]
    problems = check_build_manifest(expected_bins, rt=rt)
    if problems:
        for problem in problems:
            print(f"EQUIVALENCE REFUSED (unvalidated bins): {problem}",
                  file=sys.stderr)
        return 1
    production = rt.bin_dir / "old_english.bin"
    final_stage = oe_pipeline.named_stages()[-1]
    sandbox_final = rt.bin_dir / final_stage.snapshot_bin

    rows = oe_pipeline.load_rows(rt.corpus_tsv)
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    prod_out = batch_outputs(production, forms)
    sand_out = batch_outputs(sandbox_final, forms)

    mismatches: List[Dict[str, str]] = []
    for row, p_out, s_out in zip(rows, prod_out, sand_out):
        if Counter(p_out) != Counter(s_out):
            mismatches.append({
                "concept": row["concept"],
                "proto": row["proto"],
                "production": " | ".join(p_out) or "+?",
                "sandbox": " | ".join(s_out) or "+?",
            })
    if mismatches:
        for m in mismatches[:10]:
            print(f"MISMATCH {m['concept']} {m['proto']}: "
                  f"production=[{m['production']}] sandbox=[{m['sandbox']}]",
                  file=sys.stderr)
        print(f"EQUIVALENCE FAILED: {len(mismatches)}/{len(rows)} rows differ "
              f"between old_english.bin and {final_stage.snapshot_bin}",
              file=sys.stderr)
        return 1

    report = {
        "generator": "Germanic/tools/check_production_sandbox_equivalence.py",
        "status": "equivalent",
        "rows_compared": len(rows),
        "production_bin": "old_english.bin",
        "sandbox_final_bin": final_stage.snapshot_bin,
        "comparison": "identical output multisets per selected corpus row",
        "sources": {
            "germanic.txt": sha256_of(rt.germanic_fst),
            "old_english_sandbox.txt": sha256_of(rt.sandbox_fst),
            "germanic-aligned-final.tsv": sha256_of(rt.corpus_tsv),
        },
    }
    out = evidence_path(rt)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"equivalent: {len(rows)} rows identical between old_english.bin "
          f"and {final_stage.snapshot_bin}; wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
