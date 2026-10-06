#!/usr/bin/env python3
"""SC004 Outcome-C split experiment (research; production cascade untouched).

Builds an experimental flattened cascade in which:
  - the bundled SC004 PWGmcAiMonophthongization at position 1 is replaced by the
    final-only component A  (new SC014 body, {*ai} -> {*ē} || _ .#.);
  - the old SC014 *ăi no-op is removed;
  - the general component B+C (SC004, provisional EAFAiMonophthongization) is
    inserted at the requested EAF position (after PNWGmcPreconsonantalXLoss / SC028,
    before OEAwwjResolution / SC029), or at --after <rule> if given.

Then it formally checks, over EnglishProtoInput:
  1. whole-cascade equivalence  ExpCascade == EnglishProtoToOE ;
and reports which B formulation is used. Run in the backend container (CWD /usr/app).

--b-mode unrestricted   : B = {*ai} -> {*ā}          (current impl)
--b-mode nonfinal       : B = {*ai} -> {*ā} || _ ?   (explicit non-final)
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import tempfile
from pathlib import Path

MANIFEST = Path("docs/sound_changes/cascade_baseline/cascade_order_manifest.tsv")

A_DEF = "define SC014Exp [ {*ai} -> {*ē} || _ .#. ];"
C_DEF = "define SC004ExpStressed [ {*ái} -> {*ā} ];"


def b_def(mode: str) -> str:
    if mode == "nonfinal":
        return "define SC004ExpUnstressed [ {*ai} -> {*ā} || _ ? ];"
    return "define SC004ExpUnstressed [ {*ai} -> {*ā} ];"


def build(after_rule: str, b_mode: str) -> str:
    rules = [r["foma_identifier"] for r in csv.DictReader(MANIFEST.open(encoding="utf-8"), delimiter="\t")]
    # pos1 = PWGmcAiMonophthongization -> SC014Exp (component A)
    assert rules[0] == "PWGmcAiMonophthongization", rules[0]
    seq = ["SC014Exp"] + rules[1:]
    # remove old SC014 no-op
    seq = [r for r in seq if r != "PNWGmcUnstressedAiMonophthongization"]
    # insert general SC004 (A already at pos1; here B .o. C) after `after_rule`
    idx = seq.index(after_rule)
    seq = seq[:idx + 1] + ["SC004ExpGeneral"] + seq[idx + 1:]
    comp = "\n    .o. ".join(seq)
    return f"""source fsts/germanic.txt
{A_DEF}
{b_def(b_mode)}
{C_DEF}
define SC004ExpGeneral [ SC004ExpUnstressed .o. SC004ExpStressed ];
define ExpCascade (
    {comp}
);
clear stack
regex [ EnglishProtoInput .o. ExpCascade ];
regex [ EnglishProtoInput .o. EnglishProtoToOE ];
test equivalent
quit
"""


_RESULT_RE = re.compile(r"^(\d)\s*\(1 = TRUE")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--after", default="PNWGmcPreconsonantalXLoss",
                    help="insert the general SC004 component immediately after this rule")
    ap.add_argument("--b-mode", default="unrestricted", choices=["unrestricted", "nonfinal"])
    args = ap.parse_args()
    script = build(args.after, args.b_mode)
    with tempfile.NamedTemporaryFile("w", suffix=".foma", delete=False, encoding="utf-8") as h:
        sp = Path(h.name)
        h.write(script)
    try:
        proc = subprocess.run(["foma", "-q", "-f", str(sp)],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    finally:
        sp.unlink(missing_ok=True)
    res = [m.group(1) for line in proc.stdout.decode("utf-8", "replace").splitlines()
           if (m := _RESULT_RE.match(line.strip()))]
    print(f"after={args.after}  b_mode={args.b_mode}")
    if not res:
        print("FAIL: no equivalence result", file=sys.stderr)
        print(proc.stdout.decode("utf-8", "replace")[-500:], file=sys.stderr)
        return 2
    ok = res[-1] == "1"
    print(f"whole-cascade equivalence over EnglishProtoInput: {'TRUE' if ok else 'FALSE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
