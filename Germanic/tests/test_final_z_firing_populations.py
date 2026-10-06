"""Fail-closed regression tests for the three final-*z* rules (SC096/SC020/SC097).

Adjudication of the SC020 three-rule split, restated as SEMANTIC invariants
(control plane §17): required diagnostic witnesses must fire, negative
controls must not, every observed firing must satisfy the adjudicated
domain, and each lexeme is claimed by at most one of the three rules. The
complete current firing population is machine-derived and owned by the
coverage census — a legitimate new corpus witness that satisfies the domain
passes automatically, while a domain violation still fails closed.

- SC096 RootNounNomZLoss: the adjudicated root nouns book/flea/goose/louse
  must fire on their adjudicated inputs, and every firing must match the
  rule's computational proxy environment (word-final *z after a consonant
  in a monosyllable; see the GUARD comment at the rule definition in
  Germanic/fsts/germanic.txt). The separate proxy-environment guard below
  censuses the whole TSV for new forms entering that environment.
- SC020 EAFFinalZDeletion: friend/milk/month (adjudication memo §5) and you
  (corpus-maturation pass 01) must fire; the SC096 root nouns must NOT fire
  here; every firing input must end in *-z.
- SC097 MonosyllabicFinalZLoss: who :: *xwáz (corpus-maturation pass 01:
  R&T 2014 p.86; Campbell §125) must fire, and every firing must be a
  monosyllabic final-*z* input. Its synthetic controls must still genuinely
  demonstrate loss of final *-z with compensatory lengthening of a short
  nucleus (*hwaz > *hwā, *hiz > *hī) and nucleus preservation for bimoric
  inputs (*maiz > *mai; *mā arises only via later ai-monophthongization).

The frozen 114-row before/after firing table keeps its exact historical
counts: it is an ARCHIVE snapshot of the split adjudication, not a live
population.

Population tests are host-runnable (no foma/Docker): they read the committed
full trace report, the committed firing table, and the live TSV. The
synthetic-control tests run the real MonosyllabicFinalZLoss definition
extracted from germanic.txt and are skipped when foma is not installed.
"""

from __future__ import annotations

import csv
import hashlib
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
GERMANIC_DIR = TESTS_DIR.parent
FULL_TRACE = GERMANIC_DIR / "docs" / "debug_snapshots" / "oe_full_trace_report.txt"
FIRING_TABLE = (
    GERMANIC_DIR
    / "docs"
    / "sound_changes"
    / "audits"
    / "sc020-split-before-after-firing-table.tsv"
)
CORPUS_TSV = GERMANIC_DIR / "data" / "germanic-aligned-final.tsv"
FST_SOURCE = GERMANIC_DIR / "fsts" / "germanic.txt"

# Required SC096 diagnostic witnesses (Dossier A + adjudication memo §6;
# flea reopened and retained at the pre-push adjudication).
SC096_REQUIRED_WITNESSES = {
    "book": "*bōkz",
    "flea": "*fláuxz",
    "goose": "*gánsz",
    "louse": "*lūsz",
}
# Legacy SC020 population (the frozen 114-row before/after firing table).
SC020_LEGACY_TABLE_COUNT = 110
SC020_MUST_INCLUDE = {"friend": "*fríjōndz", "milk": "*mélukz",
                      "month": "*mḗnōθz", "you": "*ízwiz"}
# Required SC097 diagnostic witness (corpus-maturation pass 01 §1).
SC097_REQUIRED_WITNESSES = {"who": "*xwáz"}

# Mirrors normalize_proto in tools/oe_full_trace_report.py.
PROTO_STRIP_RE = re.compile(r"[{}*\s/()]")


def normalize_proto(raw: str) -> str:
    return PROTO_STRIP_RE.sub("", raw or "").replace("þ", "θ")


# Segment inventory for the proxy-environment guard. Deliberately explicit:
# a protoform containing a character in NEITHER set fails the guard test, so
# the classification itself is fail-closed against inventory drift.
VOWEL_CHARS = set(
    "aeiouy"
    "áéíóúý"
    "àèìòù"
    "âêîôû"
    "āēīōūȳ"
    "ḗḯṓ"
    "ąįųęǭ"
    "æǣǽ"
)
CONSONANT_CHARS = set("bcdfghjklmnpqrstvwxzðθβçʃʧʤʒŋ")
MARKER_CHARS = set("-")  # compound/stress separator; never in a monosyllable


def matches_sc096_proxy(norm: str) -> bool:
    """True iff the normalized protoform matches SC096's proxy environment:
    C* V+ C+ z (word-final *z after a consonant in a monosyllable)."""
    if not norm.endswith("z") or len(norm) < 3:
        return False
    if set(norm) & MARKER_CHARS:
        return False  # hyphenated forms are not monosyllables
    body = norm[:-1]
    # Segment into runs of vowels/consonants; require exactly [C*] V+ C+.
    kinds: list[str] = []
    for ch in body:
        kind = "V" if ch in VOWEL_CHARS else "C"
        if not kinds or kinds[-1] != kind:
            kinds.append(kind)
    return "".join(kinds) in ("VC", "CVC")


def load_stage_firing_summary() -> dict[str, tuple[int, list[tuple[str, str]]]]:
    """Parse the STAGE FIRING SUMMARY block of the committed full trace
    report. Returns {stage_name: (count, [(lexeme, input), ...])}."""
    text = FULL_TRACE.read_text(encoding="utf-8")
    marker = "=== STAGE FIRING SUMMARY ==="
    idx = text.find(marker)
    if idx < 0:
        raise AssertionError(
            "oe_full_trace_report.txt has no STAGE FIRING SUMMARY; regenerate "
            "with tools/oe_full_trace_report.py --all"
        )
    summary: dict[str, tuple[int, list[tuple[str, str]]]] = {}
    current: str | None = None
    for line in text[idx + len(marker):].splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*): (\d+)$", line)
        if m:
            current = m.group(1)
            summary[current] = (int(m.group(2)), [])
            continue
        if current and " :: " in line:
            count, pairs = summary[current]
            for chunk in line.split(", "):
                lex, _, form = chunk.partition(" :: ")
                pairs.append((lex.strip(), form.strip()))
            summary[current] = (count, pairs)
            current = None
    return summary


class TraceReportProvenanceTests(unittest.TestCase):
    """The committed full trace report must be fresh w.r.t. the live sources.

    tools/oe_full_trace_report.py records sha256 hashes of its canonical live
    inputs in a PROVENANCE block. If the committed report's hashes do not
    match the live germanic.txt / old_english_sandbox.txt / TSV, every
    population assertion in this module would be testing a stale artifact —
    so this test fails closed and requires regenerating the report.
    (The compiled .bin hash in the block is informational only: foma
    compilation is byte-non-deterministic.)
    """

    LIVE_SOURCES = {
        "germanic.txt": GERMANIC_DIR / "fsts" / "germanic.txt",
        "old_english_sandbox.txt": GERMANIC_DIR / "fsts" / "old_english_sandbox.txt",
        "germanic-aligned-final.tsv": CORPUS_TSV,
    }

    @staticmethod
    def _sha256(path: Path) -> str:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1 << 20), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def test_committed_report_matches_live_sources(self):
        text = FULL_TRACE.read_text(encoding="utf-8")
        marker = "=== PROVENANCE ==="
        self.assertIn(marker, text,
                      "oe_full_trace_report.txt has no PROVENANCE block; "
                      "regenerate with tools/oe_full_trace_report.py --all")
        recorded: dict[str, str] = {}
        for line in text.split(marker, 1)[1].splitlines():
            line = line.strip()
            if not line:
                if recorded:
                    break
                continue
            m = re.match(r"^(\S+) sha256(?: \(informational\))?: ([0-9a-f]{64})$",
                         line)
            if m:
                recorded[m.group(1)] = m.group(2)
        for label, path in self.LIVE_SOURCES.items():
            self.assertIn(label, recorded,
                          f"PROVENANCE block lacks a hash for {label}")
            self.assertEqual(
                recorded[label], self._sha256(path),
                f"committed trace report is STALE w.r.t. {label}; regenerate "
                "with tools/oe_full_trace_report.py --all before trusting the "
                "firing-population assertions")


class Sc096FiringPopulationTests(unittest.TestCase):
    """The trace-level firing populations match the adjudication exactly."""

    @classmethod
    def setUpClass(cls):
        cls.summary = load_stage_firing_summary()

    def test_sc096_required_root_nouns_fire_within_the_proxy_domain(self):
        count, pairs = self.summary["RootNounNomZLoss"]
        as_dict = dict(pairs)
        self.assertEqual(count, len(as_dict))
        for lex, form in SC096_REQUIRED_WITNESSES.items():
            self.assertEqual(as_dict.get(lex), form,
                             f"{lex} must lose *-z under SC096 "
                             "(Dossier A, memo §6)")
        # domain: every firing matches the adjudicated proxy environment
        for lex, form in as_dict.items():
            self.assertTrue(
                matches_sc096_proxy(normalize_proto(form)),
                f"SC096 fired outside its proxy environment on {lex} :: "
                f"{form}; historical adjudication required (GUARD note at "
                "RootNounNomZLoss)")

    def test_sc020_required_witnesses_fire_within_the_final_z_domain(self):
        count, pairs = self.summary["EAFFinalZDeletion"]
        as_dict = dict(pairs)
        self.assertEqual(count, len(as_dict))
        for lex, form in SC020_MUST_INCLUDE.items():
            self.assertEqual(as_dict.get(lex), form,
                             f"{lex} must lose *-z under SC020 (memo §5)")
        for lex in SC096_REQUIRED_WITNESSES:
            self.assertNotIn(lex, as_dict,
                             f"{lex} must lose *-z under SC096, not SC020")
        # domain: every firing input ends in word-final *-z
        for lex, form in as_dict.items():
            self.assertTrue(normalize_proto(form).endswith("z"),
                            f"SC020 fired on a non-final-z input {lex} :: "
                            f"{form}")

    def test_sc097_required_witness_fires_within_the_monosyllabic_domain(self):
        count, pairs = self.summary["MonosyllabicFinalZLoss"]
        as_dict = dict(pairs)
        self.assertEqual(count, len(as_dict))
        for lex, form in SC097_REQUIRED_WITNESSES.items():
            self.assertEqual(as_dict.get(lex), form,
                             f"{lex} must lose *-z under SC097 "
                             "(Dossier C; corpus-maturation-01 §1)")
        # domain: monosyllabic word-final *-z inputs only
        for lex, form in as_dict.items():
            norm = normalize_proto(form)
            self.assertTrue(norm.endswith("z"),
                            f"SC097 fired on a non-final-z input {lex} :: "
                            f"{form}")
            self.assertNotIn("-", norm,
                             f"SC097 fired on a compound (non-monosyllable) "
                             f"{lex} :: {form}")

    def test_each_lexeme_is_claimed_by_at_most_one_final_z_rule(self):
        claimed: dict[str, list[str]] = {}
        for rule in ("RootNounNomZLoss", "EAFFinalZDeletion",
                     "MonosyllabicFinalZLoss"):
            for lex, _ in self.summary[rule][1]:
                claimed.setdefault(lex, []).append(rule)
        double = {lex: rules for lex, rules in claimed.items()
                  if len(rules) > 1}
        self.assertEqual(double, {},
                         "a lexeme lost *-z under more than one of the three "
                         "split rules; the partition is broken")


class FiringTablePartitionTests(unittest.TestCase):
    """The committed 114-row firing table must agree with the adjudication."""

    @classmethod
    def setUpClass(cls):
        with FIRING_TABLE.open(encoding="utf-8") as handle:
            cls.rows = list(csv.DictReader(handle, delimiter="\t"))

    def test_all_114_former_sc020_firings_are_accounted_for(self):
        self.assertEqual(len(self.rows), 114)
        by_rule: dict[str, list[str]] = {}
        for row in self.rows:
            by_rule.setdefault(row["new_deleting_rule"], []).append(
                row["lexical_item"])
        self.assertEqual(sorted(by_rule),
                         ["SC020 EAFFinalZDeletion", "SC096 RootNounNomZLoss"])
        self.assertEqual(len(by_rule["SC020 EAFFinalZDeletion"]),
                         SC020_LEGACY_TABLE_COUNT)
        self.assertEqual(sorted(by_rule["SC096 RootNounNomZLoss"]),
                         sorted(SC096_REQUIRED_WITNESSES))

    def test_sc096_rows_carry_the_adjudicated_inputs(self):
        inputs = {row["lexical_item"]: row["selected_input"]
                  for row in self.rows
                  if row["new_deleting_rule"] == "SC096 RootNounNomZLoss"}
        self.assertEqual(inputs, SC096_REQUIRED_WITNESSES)


class Sc096ProxyEnvironmentGuardTests(unittest.TestCase):
    """No TSV protoform may enter SC096's proxy environment unadjudicated.

    The FST proxy ("word-final *z after a consonant in a monosyllable") is an
    implementation proxy for a morphologically restricted development. This
    guard recomputes the proxy environment over the live TSV so that a future
    unrelated monosyllable in -Cz fails the suite even before any artifact is
    regenerated.
    """

    @classmethod
    def setUpClass(cls):
        cls.protoforms: dict[str, str] = {}
        with CORPUS_TSV.open(encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                if row.get("DOCULECT") != "Old_English":
                    continue
                proto = (row.get("PROTOFORM") or "").strip()
                counterpart = (row.get("COUNTERPART") or "").strip()
                if not proto or not counterpart or counterpart == "-":
                    continue
                norm = normalize_proto(proto)
                if norm:
                    cls.protoforms[proto] = norm

    def test_every_protoform_character_is_classified(self):
        known = VOWEL_CHARS | CONSONANT_CHARS | MARKER_CHARS
        unknown = {ch for norm in self.protoforms.values()
                   for ch in norm} - known
        self.assertEqual(unknown, set(),
                         "unclassified protoform character(s); extend the "
                         "inventory in this test deliberately, then re-check "
                         "the SC096 proxy population")

    def test_proxy_environment_matches_exactly_the_adjudicated_inputs(self):
        matching = {proto for proto, norm in self.protoforms.items()
                    if matches_sc096_proxy(norm)}
        self.assertEqual(matching, set(SC096_REQUIRED_WITNESSES.values()),
                         "a protoform entered/left SC096's proxy environment; "
                         "this requires historical adjudication before the "
                         "rule fires on it (GUARD note at RootNounNomZLoss)")

    def test_proxy_classifier_agrees_with_known_shapes(self):
        # Positive controls: the four adjudicated root-noun nominatives.
        for form in SC096_REQUIRED_WITNESSES.values():
            self.assertTrue(matches_sc096_proxy(normalize_proto(form)), form)
        # Negative controls: vowel-final monosyllables belong to SC097's
        # domain, polysyllables to SC020's, hyphenated forms to neither.
        for form in ("*hwaz", "*máiz", "*kūz", "*fríjōndz", "*mélukz",
                     "*θūs-èndi"):
            self.assertFalse(matches_sc096_proxy(normalize_proto(form)), form)


def _extract_define_closure(source: str, roots: list[str]) -> str:
    """Extract the transitive `define` closure for the given root networks
    from the foma source, preserving source order."""
    define_re = re.compile(r"^define\s+([A-Za-z][A-Za-z0-9]*)\s(.*?);",
                           re.M | re.S)
    defines: dict[str, tuple[int, str]] = {}
    for m in define_re.finditer(source):
        name = m.group(1)
        # Keep the FIRST definition of each name.
        if name not in defines:
            defines[name] = (m.start(), m.group(0))
    needed: set[str] = set()
    stack = list(roots)
    name_re = re.compile(r"[A-Za-z][A-Za-z0-9]*")
    while stack:
        name = stack.pop()
        if name in needed or name not in defines:
            continue
        needed.add(name)
        body = defines[name][1].split(None, 2)[2]
        for ref in name_re.findall(body):
            if ref in defines and ref not in needed:
                stack.append(ref)
    ordered = sorted((defines[n] for n in needed), key=lambda t: t[0])
    return "\n".join(text for _, text in ordered)


@unittest.skipIf(shutil.which("foma") is None, "foma not available")
class Sc097SyntheticControlTests(unittest.TestCase):
    """Run the real MonosyllabicFinalZLoss definition on synthetic controls.

    Inputs are the chronologically correct intermediate shapes at SC097's
    cascade slot, in the internal star-token notation (R/T's *h is the FST's
    *x). Expected outputs verified against R/T 2014: 86-87 and Dossier C.
    """

    # (input, expected output at the SC097 stage)
    CONTROLS = [
        ("*x*w*a*z", "*x*w*ā"),   # *hwaz > *hwā: loss + compensatory lengthening
        ("*x*i*z", "*x*ī"),       # *hiz > *hī: loss + compensatory lengthening
        ("*m*a*i*z", "*m*a*i"),   # *maiz > *mai: bimoric nucleus preserved;
                                  # OE mā arises later via EAFAiMonophthongization
        ("*k*ū*z", "*k*ū"),       # long nucleus: plain loss, no double lengthening
        ("*k*ō*z", "*k*ō"),       # long nucleus: plain loss (English-doculect kōz)
        # Negative controls: SC097 must not touch these.
        ("*b*ō*k*z", "*b*ō*k*z"),  # consonant-final monosyllable (SC096 domain)
        ("*f*r*í*u*n*d*z", "*f*r*í*u*n*d*z"),  # consonant-final (SC020 domain)
        ("*m*í*z*d*ō", "*m*í*z*d*ō"),  # medial *z: reserved for rhotacism
    ]

    @classmethod
    def setUpClass(cls):
        source = FST_SOURCE.read_text(encoding="utf-8")
        script = _extract_define_closure(source, ["MonosyllabicFinalZLoss"])
        script += "\nregex MonosyllabicFinalZLoss;\n"
        for form, _ in cls.CONTROLS:
            script += f"down {form}\n"
        with tempfile.NamedTemporaryFile(
                "w", suffix=".foma", delete=False, encoding="utf-8") as handle:
            handle.write(script)
            script_path = handle.name
        try:
            proc = subprocess.run(
                ["foma", "-q", "-f", script_path],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        finally:
            Path(script_path).unlink()
        cls.outputs = [line.strip() for line in
                       proc.stdout.decode("utf-8").splitlines() if line.strip()]

    def test_synthetic_controls_behave_as_adjudicated(self):
        self.assertEqual(len(self.outputs), len(self.CONTROLS),
                         f"unexpected foma output shape: {self.outputs}")
        for (form, expected), actual in zip(self.CONTROLS, self.outputs):
            self.assertEqual(actual, expected,
                             f"SC097 on {form}: expected {expected}, got {actual}")


if __name__ == "__main__":
    unittest.main()
