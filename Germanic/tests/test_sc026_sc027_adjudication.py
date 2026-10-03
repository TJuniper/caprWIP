#!/usr/bin/env python3
"""Regression for the nasal-spirant adjudication (SC026/SC027/SC103, 2026).

Governing memo:
Germanic/docs/sound_changes/audits/sc026-sc027-nasal-spirant-adjudication.md

Protected scientific conclusions:

  * There are TWO nasal-loss developments, not one. Nasal loss before *x
    is Proto-Germanic and pan-Germanic (Campbell §119 p. 44; Fulk §4.1;
    Ringe vol. 1); it is SC103 `PGmcNasalLossBeforeX`. Nasal loss before
    *f/*þ/*s is the later North Sea Germanic (Ingvaeonic) law
    (Campbell §121 p. 47; Fulk §4.11; Sievers-Brunner §186.1;
    R/T 2014 §5.1.1 pp. 139-141), implemented as SC026 + SC027.
  * The consonantal domain of SC026/SC027 excludes *x. The old broad
    class `EnglishStarVoicelessFricative` (which contained *x) must not
    return in either rule.
  * Only *a, *i, *u occur before nasal + obstruent in Germanic
    (Fulk §4.1: "the vowels e and o did not occur in this environment"),
    so neither lengthening rule may map *e, *o or *æ.
  * SC026 and SC027 are ONE historical sound change implemented in two
    executable steps: SC027 carries `canonical_change_id = SC026`, and
    SC026 executes immediately before SC027.
  * `fist` is NOT a witness for SC026/SC027. PGmc *funhsti- (Kroonen
    p. 160) has the long vowel in OHG fūst / Du vuist / G Faust, so its
    nasal loss is pan-Germanic. It is SC103's only live firing, and it
    must appear in neither SC026's nor SC027's chronology witness set.
  * `goose` and `youth` are the genuine witnesses of the North Sea
    Germanic law (their OHG cognates gans, jugund keep the nasal).
  * SC103 precedes SC026/SC027 and feeds SC028
    `PNWGmcPreconsonantalXLoss`, which simplifies the *xst cluster it
    creates; `fist` still surfaces as fȳst, i.e. corpus output unchanged.

Run: cd Germanic/tests && python3 -m unittest test_sc026_sc027_adjudication
"""
from __future__ import annotations

import csv
import importlib.util
import re
import shutil
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
SC_DIR = GERMANIC / "docs" / "sound_changes"
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
ANNOTATIONS = SC_DIR / "registry" / "sc_inventory_annotations.tsv"
CENSUS = SC_DIR / "cascade_baseline" / "rule_coverage_census.tsv"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
BASELINE = SC_DIR / "cascade_baseline" / "cascade_baseline_outputs.tsv"
MEMO = SC_DIR / "audits" / "sc026-sc027-nasal-spirant-adjudication.md"
READER = SC_DIR / "reader_facing" / "026-027-nasal-spirant-changes.md"
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"

RUNTIME_BUILT = ((BIN_DIR / "old_english.bin").is_file()
                 and shutil.which("flookup") is not None)
requires_runtime = unittest.skipUnless(
    RUNTIME_BUILT,
    "live runtime probe: needs local sandbox bins (adjudicate --evidence) "
    "and flookup on PATH")

# The complete live firing census established by the adjudication.
NSGMC_WITNESSES = {"goose": "gōs", "youth": "ġeoguþ"}
PGMC_X_WITNESS = {"fist": "fȳst"}


def load_trace_tool():
    spec = importlib.util.spec_from_file_location("oe_full_trace_report", TRACE_TOOL)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def _tsv_rows(path: Path):
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()
             if not line.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


class NasalSpirantAdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        cls.registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        cls.edges = _tsv_rows(EDGES)
        cls.positions = {r["foma_identifier"]: int(r["position"])
                         for r in _tsv_rows(MANIFEST)}
        cls.baseline = {r["concept"]: r for r in _tsv_rows(BASELINE)}
        cls.trace = load_trace_tool()

    def define_body(self, name: str) -> str:
        match = re.search(
            r"define\s+" + re.escape(name) + r"\s*(?:Ctx\()?\[(.*?)\n\]\)?;",
            self.uncommented, re.S)
        self.assertIsNotNone(match, f"missing define {name}")
        return match.group(1)

    def stage(self, name, form):
        return self.trace.run_stage(
            BIN_DIR, f"old_english_sandbox_after_{name}.bin", form)

    # ------------------------------------------------------------------
    # Consonantal domain: the law is *f/*þ/*s, never *x
    # ------------------------------------------------------------------

    def test_nsgmc_spirant_class_excludes_x(self):
        match = re.search(
            r"define\s+EnglishStarNSGmcSpirant\s*\[(.*?)\];",
            self.uncommented, re.S)
        self.assertIsNotNone(
            match,
            "the North Sea Germanic law needs its own narrow spirant class")
        body = match.group(1)
        for seg in ("{*f}", "{*s}", "{*θ}"):
            self.assertIn(seg, body, f"NSGmc law must apply before {seg}")
        self.assertNotIn(
            "{*x}", body,
            "nasal loss before *x is the pan-Germanic change (Campbell §119, "
            "Fulk §4.1), not the North Sea Germanic law (Campbell §121, "
            "Fulk §4.11)")

    def test_broad_voiceless_fricative_class_does_not_return_in_the_law(self):
        for name in ("EAFNasalSpirantLengthening", "EAFNasalSpirantLoss"):
            body = self.define_body(name)
            self.assertNotIn(
                "EnglishStarVoicelessFricative", body,
                f"{name} must not use the broad class that included *x")
            self.assertIn("EnglishStarNSGmcSpirant", body)

    # ------------------------------------------------------------------
    # Vowel inventory: only *a, *i, *u occur in this environment
    # ------------------------------------------------------------------

    def test_lengthening_rules_map_only_a_i_u(self):
        allowed = {"*a", "*i", "*u", "*á", "*í", "*ú"}
        for name in ("EAFNasalSpirantLengthening", "PGmcNasalLossBeforeX"):
            body = self.define_body(name)
            inputs = set(re.findall(r"\{(\*[^}]+)\}\s*->", body))
            inputs.discard("*x")
            self.assertTrue(
                inputs <= allowed,
                f"{name} maps historically impossible inputs "
                f"{sorted(inputs - allowed)}: Fulk §4.1 states that *e and *o "
                "do not occur before nasal + obstruent in Germanic, and *æ "
                "arises long after this stage")

    def test_low_vowel_outcome_is_rounded(self):
        # Both feeders now produce the long nasalized low vowel *ą̄ (spelled
        # {*ã}); the rounding to *ō is the separate Anglo-Frisian SC104
        # EAFNasalizedLowRounding (Campbell §119 p. 44, §121 p. 47,
        # §128 n. 1 p. 50; Fulk §4.11 p. 72; Sievers-Brunner §80 Anm. 1).
        for name in ("EAFNasalSpirantLengthening", "PGmcNasalLossBeforeX"):
            body = self.define_body(name)
            self.assertRegex(
                body, r"\{\*a\}\s*->\s*\{\*ã\}",
                f"{name}: *a is lengthened and nasalized to *ą̄")
            self.assertNotRegex(
                body, r"\{\*a\}\s*->\s*\{\*ō\}",
                f"{name}: the Anglo-Frisian rounding must not be telescoped "
                "back into this rule")
        self.assertRegex(
            self.define_body("EAFNasalizedLowRounding"),
            r"\{\*ã\}\s*->\s*\{\*ō\}",
            "SC104 rounds the long nasalized low vowel in Anglo-Frisian")

    # ------------------------------------------------------------------
    # SC103 exists, is pan-Germanic, and precedes the North Sea law
    # ------------------------------------------------------------------

    def test_pgmc_rule_deletes_the_nasal_before_x_only(self):
        body = self.define_body("PGmcNasalLossBeforeX")
        self.assertRegex(
            body, r"EnglishStarNasal\s*->\s*0\s*\|\|\s*_\s*\{\*x\}",
            "SC103 must delete the nasal before *x")

    def test_pgmc_rule_precedes_the_north_sea_law_and_feeds_x_loss(self):
        self.assertLess(self.positions["PGmcNasalLossBeforeX"],
                        self.positions["EAFNasalSpirantLengthening"],
                        "a Proto-Germanic change precedes a North Sea "
                        "Germanic one")
        self.assertLess(self.positions["EAFNasalSpirantLengthening"],
                        self.positions["EAFNasalSpirantLoss"],
                        "executable dependency: the vowel rule must read the "
                        "nasal the loss rule deletes")
        self.assertLess(self.positions["PGmcNasalLossBeforeX"],
                        self.positions["PNWGmcPreconsonantalXLoss"],
                        "SC103 creates the *xst cluster SC028 simplifies")

    # ------------------------------------------------------------------
    # Registry metadata
    # ------------------------------------------------------------------

    def test_registry_records_one_historical_change_in_two_steps(self):
        sc026, sc027 = self.registry["SC026"], self.registry["SC027"]
        self.assertEqual(
            sc027["canonical_change_id"], "SC026",
            "SC026 and SC027 implement one historical sound change")
        for sc in (sc026, sc027):
            self.assertEqual(sc["adjudication_status"], "adjudicated")
            self.assertEqual(sc["verdict"], "SPLIT/RESTRICT/REFORMULATE")
            self.assertEqual(sc["hist_stage"], "eaf")
            self.assertEqual(sc["hist_scope"], "north_sea_germanic")
            self.assertEqual(sc["historical_stage_label"],
                             "North Sea Germanic")
            self.assertTrue(sc["adjudication_memo"].endswith(MEMO.name))

    def test_registry_records_the_pan_germanic_change(self):
        sc103 = self.registry["SC103"]
        self.assertEqual(sc103["fst_identifier"], "PGmcNasalLossBeforeX")
        self.assertEqual(sc103["hist_stage"], "pgmc")
        self.assertEqual(sc103["hist_scope"], "pan_germanic")
        self.assertEqual(sc103["adjudication_status"], "adjudicated")
        self.assertEqual(sc103["lifecycle_status"], "active")

    def test_memo_and_reader_prose_exist_and_state_the_verdict(self):
        memo = MEMO.read_text(encoding="utf-8")
        self.assertIn(
            "Registry-verdict: SC026=SPLIT/RESTRICT/REFORMULATE; "
            "SC027=SPLIT/RESTRICT/REFORMULATE; SC103=SPLIT", memo)
        reader = READER.read_text(encoding="utf-8")
        self.assertIn("PGmcNasalLossBeforeX", reader)
        self.assertNotIn("EnglishStarVoicelessFricative", reader)

    # ------------------------------------------------------------------
    # Witness sets: fist withdrawn, goose and youth retained
    # ------------------------------------------------------------------

    def test_fist_is_not_a_chronology_witness_for_the_north_sea_law(self):
        seen = 0
        for edge in self.edges:
            if {edge["source_change_id"], edge["target_change_id"]} != {
                    "SC026", "SC027"}:
                continue
            seen += 1
            witnesses = {w.strip() for w in
                         edge["representative_lexemes"].split(";") if w.strip()}
            self.assertEqual(
                witnesses, set(NSGMC_WITNESSES),
                "the SC026/SC027 witness set is goose and youth; fist "
                "belongs to the pan-Germanic change SC103")
        self.assertEqual(seen, 2, "expected the reciprocal edge pair")

    def test_annotation_firing_lexemes_follow_the_census(self):
        """firing_lexemes is generated FROM the census, so it can never drift
        from it; the adjudicated witnesses must be present (the complete
        current population is machine-derived and owned by the census)."""
        rows = {r["change_id"]: r for r in _tsv_rows(ANNOTATIONS)}
        census = {r["sc_id"]: r for r in _tsv_rows(CENSUS)}
        for sc in ("SC026", "SC027"):
            for witness in NSGMC_WITNESSES:
                self.assertIn(witness, rows[sc]["firing_lexemes"])
        self.assertIn("fist", rows["SC103"]["firing_lexemes"])
        for sc in ("SC026", "SC027", "SC103"):
            self.assertEqual(rows[sc]["firing_lexemes"],
                             census[sc]["lexical_witnesses"])

    # ------------------------------------------------------------------
    # Live probes: the census, and unchanged surface output
    # ------------------------------------------------------------------

    @requires_runtime
    def test_north_sea_law_fires_on_goose_and_youth(self):
        # SC103 now stands at the head of the cascade, so its snapshot still
        # shows the inherited final *-z on goose. Both steps of the North Sea
        # law leave a NASALIZED low vowel; SC104 rounds it later.
        cases = {
            "goose": (["*g*á*n*s*z"], ["*g*ã*n*s"], ["*g*ã*s"]),
            "youth": (["*j*ú*g*u*n*θ"], ["*j*ú*g*ū*n*θ"], ["*j*ú*g*ū*θ"]),
        }
        for concept, (before, mid, after) in cases.items():
            with self.subTest(concept=concept):
                form = self.baseline[concept]["proto"].lstrip("*")
                self.assertEqual(
                    self.stage("pgmc_nasal_loss_before_x", form), before)
                self.assertEqual(
                    self.stage("eaf_nasal_spirant_lengthening", form), mid)
                self.assertEqual(
                    self.stage("eaf_nasal_spirant_loss", form), after)

    @requires_runtime
    def test_fist_is_handled_by_the_pan_germanic_rule_alone(self):
        form = self.baseline["fist"]["proto"].lstrip("*")
        # SC103 now heads the cascade, so the state immediately before it is
        # the prelude stage PGmcGmSimplification.
        self.assertEqual(self.stage("pgmc_gm_simplification", form),
                         ["*f*ú*n*x*s*t*i*z"])
        after_pgmc = self.stage("pgmc_nasal_loss_before_x", form)
        self.assertEqual(after_pgmc, ["*f*ū*x*s*t*i*z"],
                         "SC103 lengthens and deletes the nasal before *x")
        # SC028 PNWGmcPreconsonantalXLoss then simplifies the *xst cluster
        # that SC103 has just created; since the SC028 adjudication it does so
        # in the northern West Germanic region, ahead of the Ingvaeonic law.
        self.assertEqual(self.stage("pnwgmc_preconsonantal_x_loss", form),
                         ["*f*ū*s*t*i*z"],
                         "SC028 deletes the *x of the *xst cluster")
        # Neither step of the North Sea Germanic law may touch it: the state
        # entering the law (after SC023 PNWGmcNStemNLoss, the stage
        # immediately preceding SC026) survives both steps unchanged.
        before_law = self.stage("pnwgmc_n_stem_n_loss", form)
        self.assertEqual(before_law, ["*f*ū*s*t*i"])
        self.assertEqual(self.stage("eaf_nasal_spirant_lengthening", form),
                         before_law)
        self.assertEqual(self.stage("eaf_nasal_spirant_loss", form),
                         before_law)
        # and the pan-Germanic rule never rounds: *ą̄ is not created here
        self.assertNotIn("*ã", before_law[0])
        self.assertNotIn("*ō", before_law[0])

    def test_surface_outputs_are_unchanged(self):
        for concept, attested in {**NSGMC_WITNESSES, **PGMC_X_WITNESS}.items():
            with self.subTest(concept=concept):
                self.assertEqual(self.baseline[concept]["outputs"], attested)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
