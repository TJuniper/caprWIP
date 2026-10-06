#!/usr/bin/env python3
"""Formal SC004/SC014 pairwise interaction analysis with counterexamples.

For the two corrected production rules

  SC014  PNWGmcUnstressedAiMonophthongization : {*ai} -> {*ē}   (pos 1)
  SC004  EAFAiMonophthongization              : {*ái} -> {*ā}   (pos 25)

this tool tests, against every rule each one crosses, whether the two
composition orders are equivalent over the admitted input language

    Fwd = EnglishProtoInput .o. A .o. B
    Rev = EnglishProtoInput .o. B .o. A

using foma ``test equivalent`` (reusing cascade_interaction_harness). For every
non-commuting pair it extracts a concrete counterexample: it applies Fwd and Rev
to the corpus ai-forms (bare-normalised PROTOFORM) and, if the corpus does not
distinguish the orders, to a set of synthetic ai/ái probes, and reports the
first input whose two orders diverge. Formal non-commutation is recorded even
when no corpus form witnesses it.

Runs inside the backend container (needs foma). CWD = /usr/app.
Writes a TSV to --out.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import subprocess
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent


def _load_harness():
    spec = importlib.util.spec_from_file_location(
        "cascade_interaction_harness", TOOLS / "cascade_interaction_harness.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


SC014 = "PNWGmcUnstressedAiMonophthongization"
SC004 = "EAFAiMonophthongization"

import sys  # noqa: E402

sys.path.insert(0, str(TOOLS))
import oe_pipeline  # noqa: E402

# Crossed-rule sets are derived from the shared executable model
# (oe_pipeline), not hand-maintained lists: SC014 sits at the head of the
# cascade-numbered span and crosses everything down to PNWGmcILowering;
# SC004's displacement experiment spans the head through SC036
# (OEInterStressRaising).  Deriving these mechanically keeps them correct
# when rules move (e.g. SC024's relocation) or are inserted (e.g. SC102).
SC014_CROSSED = [
    r for r in oe_pipeline.rules_between(SC014, "PNWGmcILowering",
                                         inclusive=True)
    if r != SC014
]

SC004_CROSSED = [
    r for r in oe_pipeline.rules_between(SC014, "OEInterStressRaising",
                                         inclusive=True)
    if r not in (SC014, SC004)
]

def normalize_proto(proto: str) -> str:
    s = re.sub(r"[{}*\s/()]", "", proto or "")
    return s.replace("þ", "θ")


def corpus_ai_forms(tsv_path: Path) -> list[str]:
    ai = re.compile(r"[aáàāă][iíìī]")
    forms = []
    with tsv_path.open(encoding="utf-8") as handle:
        for r in csv.DictReader(handle, delimiter="\t"):
            if r.get("DOCULECT") != "Old_English":
                continue
            pf = (r.get("PROTOFORM") or "").strip()
            if pf and ai.search(pf):
                forms.append(normalize_proto(pf))
    return sorted(set(forms))


def build_order_bins(defs_image: Path, a: str, b: str, tmp: Path) -> tuple[Path, Path]:
    """Save EPI.o.a.o.b and EPI.o.b.o.a to bins (domain-restricted to corpus)."""
    fwd = tmp / "fwd.bin"
    rev = tmp / "rev.bin"
    script = (
        f"load defined {defs_image}\n"
        f"regex [ EnglishProtoInput .o. {a} .o. {b} ];\n"
        f"save stack {fwd}\n"
        "clear stack\n"
        f"regex [ EnglishProtoInput .o. {b} .o. {a} ];\n"
        f"save stack {rev}\n"
    )
    sp = tmp / "orders.foma"
    sp.write_text(script, encoding="utf-8")
    subprocess.run(["foma", "-q", "-f", str(sp)],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    return fwd, rev


def apply_one(bin_path: Path, form: str, raw: bool) -> str:
    args = ["flookup", "-i", "-x", str(bin_path)] if raw else ["flookup", "-i", str(bin_path)]
    proc = subprocess.run(args, input=(form + "\n").encode("utf-8"),
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    outs = []
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        if not line.strip():
            continue
        if raw:
            outs.append(line.strip())
        else:
            parts = line.split("\t")
            if len(parts) >= 2 and parts[1] not in ("+?", ""):
                outs.append(parts[1])
    return "|".join(sorted(set(outs))) if outs else "<none>"


def foma_witness(defs_image: Path, a: str, b: str, tmp: Path) -> str:
    """Extract one input where EPI.o.a.o.b and EPI.o.b.o.a diverge, as the upper
    (input) projection of the relation difference [Fwd - Rev]. Samples a handful
    of random witnesses and returns the shortest for readability."""
    script = (
        f"load defined {defs_image}\n"
        f"regex [ [ EnglishProtoInput .o. {a} .o. {b} ] - "
        f"[ EnglishProtoInput .o. {b} .o. {a} ] ].u;\n"
        "print random-words 12\n"
    )
    sp = tmp / "witness.foma"
    sp.write_text(script, encoding="utf-8")
    proc = subprocess.run(["foma", "-q", "-f", str(sp)],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    cands = []
    for line in proc.stdout.decode("utf-8", "replace").splitlines():
        w = re.sub(r"^\[\d+\]\s*", "", line.strip())
        if w and "?" not in w and not w.lower().startswith("loading"):
            cands.append(w)
    if not cands:
        return ""
    return min(cands, key=len)


def find_counterexample(defs_image, a, b, corpus, tmp):
    # First try corpus forms (domain-restricted EPI bins): a corpus-visible
    # counterexample would mean the split changed a real output.
    fwd, rev = build_order_bins(defs_image, a, b, tmp)
    for form in corpus:
        of, orv = apply_one(fwd, form, raw=False), apply_one(rev, form, raw=False)
        if of != orv:
            return form, of, orv, "corpus"
    # Otherwise extract a formal witness from the whole input language.
    w = foma_witness(defs_image, a, b, tmp)
    if w:
        of, orv = apply_one(fwd, w, raw=False), apply_one(rev, w, raw=False)
        return w, of, orv, "formal_noncorpus"
    return "", "", "", "none_found"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fst", default="fsts/germanic.txt")
    ap.add_argument("--tsv", default="data/germanic-aligned-final.tsv")
    ap.add_argument("--out",
                    default="docs/sound_changes/order_tests/sc004_sc014_interaction_analysis.tsv")
    args = ap.parse_args()

    harness = _load_harness()
    defs_image = harness.build_defs_image(Path(args.fst))
    corpus = corpus_ai_forms(Path(args.tsv))

    pairs = [(SC014, r) for r in SC014_CROSSED] + [(SC004, r) for r in SC004_CROSSED]
    tmp = Path(tempfile.mkdtemp())
    rows = []
    try:
        for i, (a, b) in enumerate(pairs, 1):
            commute = harness.test_pair(defs_image, a, b)
            ce_in = ce_fwd = ce_rev = ce_src = ""
            if not commute:
                ce_in, ce_fwd, ce_rev, ce_src = find_counterexample(defs_image, a, b, corpus, tmp)
            rows.append({
                "rule": "SC014" if a == SC014 else "SC004",
                "rule_foma": a,
                "crossed_rule": b,
                "commute": "yes" if commute else "no",
                "counterexample_input": ce_in,
                "forward_output": ce_fwd,
                "reversed_output": ce_rev,
                "counterexample_source": ce_src,
            })
            print(f"[{i}/{len(pairs)}] {a} x {b} -> {'commute' if commute else 'NONCOMMUTE'}"
                  + ("" if commute else f"  ce={ce_in or 'none'} ({ce_src})"))
    finally:
        defs_image.unlink(missing_ok=True)

    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    nnc = sum(1 for r in rows if r["commute"] == "no")
    print(f"pairs={len(rows)} noncommute={nnc}; wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
