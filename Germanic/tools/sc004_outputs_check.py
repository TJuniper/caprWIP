#!/usr/bin/env python3
"""SC004 split: does the genuine-history placement preserve the corpus outputs?

Builds the experimental OldEnglish transducer with:
  - component A (final unstressed *ai -> *ē) as SC014 at the old SC004 head slot;
  - the old SC014 *ăi no-op removed;
  - the general component B+C (*ai/*ái -> *ā) inserted at the requested position;
and applies the actual corpus, reporting outputs_sha256 and any per-lexeme diffs
vs the production old_english.bin. This is the decisive test (whole-language
equivalence over EnglishProtoInput is NOT required — a genuine reorder differs on
non-corpus inputs; what matters is that the attested OE outputs are unchanged).

Run in the backend container, CWD /usr/app.
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "tools")
import cascade_baseline as cb  # noqa: E402

MANIFEST = Path("docs/sound_changes/cascade_baseline/cascade_order_manifest.tsv")
TSV = Path("data/germanic-aligned-final.tsv")

FROZEN_SHA = "aaf19ba919cafbe86ea59d482ce74d0944f541336e246da481a3f37b20da480e"


def b_def(mode: str) -> str:
    if mode == "nonfinal":
        return "define SC004ExpUnstressed [ {*ai} -> {*ā} || _ ? ];"
    return "define SC004ExpUnstressed [ {*ai} -> {*ā} ];"


def build_script(after_rule: str, b_mode: str, out_bin: str) -> str:
    rules = [r["foma_identifier"] for r in csv.DictReader(MANIFEST.open(encoding="utf-8"), delimiter="\t")]
    assert rules[0] == "PWGmcAiMonophthongization", rules[0]
    seq = ["SC014Exp"] + rules[1:]
    seq = [r for r in seq if r != "PNWGmcUnstressedAiMonophthongization"]
    idx = seq.index(after_rule)
    seq = seq[:idx + 1] + ["SC004ExpGeneral"] + seq[idx + 1:]
    comp = "\n    .o. ".join(seq)
    return f"""source fsts/germanic.txt
define SC014Exp [ {{*ai}} -> {{*ē}} || _ .#. ];
{b_def(b_mode)}
define SC004ExpStressed [ {{*ái}} -> {{*ā}} ];
define SC004ExpGeneral [ SC004ExpUnstressed .o. SC004ExpStressed ];
define ExpEnglishProtoToOE (
    {comp}
);
define ExpOldEnglishCore EnglishProtoInput .o. EarlyGermanicConsonantPipeline .o. ExpEnglishProtoToOE;
define ExpOldEnglishAfterEpenthesis ExpOldEnglishCore .o. OEEpentheticVowel;
define ExpOldEnglishRules ExpOldEnglishAfterEpenthesis .o. OELateUnstressedAgSuffix .o. OECjCleanup .o. OEXsMerge .o. OldEnglishOrthography .o. OEWsPalatalGlide .o. OldEnglishRemoveStars;
define ExpOldEnglishReflexes ExpOldEnglishRules .o. OldEnglishSurface;
define ExpOldEnglish ExpOldEnglishReflexes;
clear stack
regex ExpOldEnglish;
save stack {out_bin}
quit
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--after", default="PNWGmcPreconsonantalXLoss")
    ap.add_argument("--b-mode", default="unrestricted", choices=["unrestricted", "nonfinal"])
    args = ap.parse_args()

    tmp = tempfile.mkdtemp()
    out_bin = f"{tmp}/old_english_exp.bin"
    sp = Path(tmp) / "build.foma"
    sp.write_text(build_script(args.after, args.b_mode, out_bin), encoding="utf-8")
    r = subprocess.run(["foma", "-q", "-f", str(sp)], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if not Path(out_bin).exists():
        print("FAIL: experimental bin not built", file=sys.stderr)
        print(r.stderr.decode("utf-8", "replace")[-800:], file=sys.stderr)
        return 2

    exp = cb.build_baseline(TSV, Path(out_bin))
    prod = cb.build_baseline(TSV, Path("old_english.bin"))
    s = exp["summary"]
    print(f"after={args.after}  b_mode={args.b_mode}")
    print(f"  experimental outputs_sha256 = {s['outputs_sha256']}")
    print(f"  production   outputs_sha256 = {prod['summary']['outputs_sha256']}")
    print(f"  frozen       outputs_sha256 = {FROZEN_SHA}")
    print(f"  matched={s['matched']} mismatched={s['mismatched']} accepted={s['accepted']}")
    same = s["outputs_sha256"] == prod["summary"]["outputs_sha256"] == FROZEN_SHA
    print(f"  OUTPUTS PRESERVED: {same}")
    if not same:
        # per-lexeme diffs from records
        def omap(b):
            return {r["proto_norm"]: r.get("outputs", "") for r in b["records"]}
        eo, po = omap(exp), omap(prod)
        keys = sorted(set(eo) | set(po))
        diffs = [(k, po.get(k), eo.get(k)) for k in keys if eo.get(k) != po.get(k)]
        # map proto_norm -> concept for readability
        concept = {}
        for row in csv.DictReader(TSV.open(encoding="utf-8"), delimiter="\t"):
            if row["DOCULECT"] == "Old_English":
                concept[cb.normalize_proto(row.get("PROTO") or row.get("PROTOFORM") or "")] = row["CONCEPT"]
        print(f"  {len(diffs)} lexeme(s) differ (concept proto_norm: production -> experimental):")
        for k, p, e in diffs[:40]:
            print(f"    {concept.get(k,'?')} {k}: {p} -> {e}")
    return 0 if same else 1


if __name__ == "__main__":
    raise SystemExit(main())
