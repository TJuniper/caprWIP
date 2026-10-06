#!/usr/bin/env python3
"""Regression for the nasalized-low-vowel adjudication (SC025/SC103/SC104, 2026).

Governing memo:
Germanic/docs/sound_changes/audits/sc025-sc104-nasalized-low-vowel-adjudication.md

Protected scientific conclusions:

  * CAPR had telescoped ONE later sound change into three earlier rules.
    Three historically distinct processes create a long nasalized low
    vowel *ą̄, and a single later Anglo-Frisian change rounds it to *ō
    (Campbell §128 n. 1 p. 50: the rounding "affected ą̄ from Prim. Gmc.
    ą̄ (§119) and from Ingvaeonic ą̄ (§121) at the same time").
  * The three feeders are:
      - SC103 PGmcNasalLossBeforeX  *aNx     > *ą̄x  (pan-Germanic)
      - SC026 EAFNasalSpirantLengthening *aNf/þ/s > *ą̄f/þ/s (North Sea Gmc)
      - SC025 EAFLongANasalRounding *āN > *ą̄N     (North Sea Germanic)
    None of them may round: rounding is SC104 EAFNasalizedLowRounding.
  * The nasalization and the rounding have DIFFERENT geographies. Old
    Saxon shares the nasalization (R/T vol. 2 §5.1.2 p. 142: stressed low
    vowels were nasalized in the northern WGmc dialects) but not the
    rounding (Campbell §119 p. 44; Fulk §4.11 p. 72). So SC025/SC026 stay
    north_sea_germanic and SC104 is anglo_frisian.
  * Confidence attaches to the historical claim being rated: the *ē₁ > *ā
    feeding pathway (SC024) and the nasalization (SC025) remain B because
    the two-step *ē₁ reconstruction is disputed, but the rounding itself
    (SC104) is A, being independently evidenced from PGmc *Nx reflexes,
    North Sea nasal-spirant reflexes and retained-*N forms.
  * *ą̄ is represented explicitly because its later development DIVERGES
    from the corresponding oral vowel. *ī̃/*ū̃ are not, because they
    "subsequently develop like original ī and ū" (Campbell §121 p. 47).
  * Making *ą̄ explicit turns a stipulated ordering constraint into a
    segmental fact: the oral *ā created later by SC004
    EAFAiMonophthongization simply is not {*ã}, so stone/home are
    representationally protected (Fulk §4.1 p. 55: the nasalized vowel
    "did not fall together with OE ā < ai").
  * SC103 is pan-Germanic and now stands at the head of the executable
    cascade, ahead of every daughter-specific NWGmc/PWGmc change.
  * The whole reformulation is output-neutral: all 385 corpus rows and
    both frozen cascade fingerprints are unchanged.
  * `thought` (PGmc *θánxtē > OE þōhte) was added afterwards as the
    live low-vowel witness of SC103 -> SC104, the one branch of the
    analysis the corpus had not previously exercised. It changes no
    existing output; see §12 of the memo.

Run: cd Germanic/tests && python3 -m unittest test_sc025_sc104_adjudication
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
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
BASELINE = SC_DIR / "cascade_baseline" / "cascade_baseline_outputs.tsv"
MEMO = SC_DIR / "audits" / "sc025-sc104-nasalized-low-vowel-adjudication.md"
READER = SC_DIR / "reader_facing"
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"

RUNTIME_BUILT = ((BIN_DIR / "old_english.bin").is_file()
                 and shutil.which("flookup") is not None)
requires_runtime = unittest.skipUnless(
    RUNTIME_BUILT,
    "live runtime probe: needs local sandbox bins (adjudicate --evidence) "
    "and flookup on PATH")

# The complete live firing census established by the adjudication.
SC025_WITNESSES = {"month": "mōnaþ", "spoon": "spōn"}
SC026_LOW_WITNESS = {"goose": "gōs"}
# SC103 fires on both branches. `fist` takes the HIGH branch and never
# reaches the rounding; `thought` takes the LOW branch and feeds SC104.
SC103_WITNESS = {"fist": "fȳst"}
SC103_LOW_WITNESS = {"thought": "þōhte"}
# Ringe 2017 pp. 136, 281: PGmc *þankijaną, *þanhtē, *þanhtaz. The
# preterite is reconstructed with the nasal still present before *h, so
# the corpus enters it un-reduced and the cascade derives the loss.
THOUGHT_PROTO = "*θánxtē"
# Counterfeeding controls: their *ā arises from *ai, after the rounding.
ORAL_A_CONTROLS = {"stone": "stān", "home": "hām"}


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


class NasalizedLowVowelAdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        cls.registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        cls.edges = _tsv_rows(EDGES)
        cls.annotations = {r["change_id"]: r for r in _tsv_rows(ANNOTATIONS)}
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
    # The nasalized low vowel exists as an explicit segment
    # ------------------------------------------------------------------

    def test_nasalized_low_vowel_is_a_single_codepoint(self):
        """foma's brace notation does not fuse a base letter with a combining
        diacritic, so *ą̄ must be spelled with the single codepoint U+00E3."""
        self.assertIn("{*ã}", self.uncommented)
        self.assertEqual(len("ã"), 1)
        self.assertNotIn("{*ą\u0304}", self.uncommented,
                         "a two-codepoint {*ą̄} silently never matches in foma")

    def test_nasalized_low_vowel_is_in_the_vowel_classes(self):
        for cls_name in ("PGmcStarVowel", "PGmcStarBackVowel",
                         "EnglishStarLongVowel"):
            self.assertIn("{*ã}", self.define_body(cls_name),
                          f"{cls_name} must contain the nasalized low vowel")

    def test_high_nasalized_vowels_are_not_represented(self):
        """Only historically consequential intermediates are made explicit.
        Campbell §121 p. 47: West Germanic ī̃ and ū̃ "subsequently develop
        like original ī and ū", so they get no separate segment."""
        for seg in ("{*ĩ}", "{*ũ}"):
            self.assertNotIn(seg, self.uncommented,
                             f"{seg} has no divergent later development and "
                             "must not be added as an unused state")

    # ------------------------------------------------------------------
    # Three feeders create *ą̄; none of them rounds
    # ------------------------------------------------------------------

    def test_sc025_only_nasalizes(self):
        self.assertRegex(
            self.define_body("EAFLongANasalRounding"),
            r"\{\*ā\}\s*->\s*\{\*ã\}\s*\|\|\s*_\s*EnglishStarNasal",
            "SC025 states the nasalization of inherited long *ā before a "
            "surviving nasal, not the rounding")
        self.assertNotRegex(self.define_body("EAFLongANasalRounding"),
                            r"->\s*\{\*ō\}")

    def test_sc026_low_branch_creates_the_nasalized_low_vowel(self):
        body = self.define_body("EAFNasalSpirantLengthening")
        self.assertRegex(body, r"\{\*a\}\s*->\s*\{\*ã\}")
        self.assertRegex(body, r"\{\*á\}\s*->\s*\{\*ã\}")
        self.assertNotRegex(body, r"\{\*[aá]\}\s*->\s*\{\*ō\}")

    def test_sc103_low_branch_creates_the_nasalized_low_vowel(self):
        body = self.define_body("PGmcNasalLossBeforeX")
        self.assertRegex(body, r"\{\*a\}\s*->\s*\{\*ã\}")
        self.assertRegex(body, r"\{\*á\}\s*->\s*\{\*ã\}")
        self.assertNotRegex(
            body, r"\{\*[aá]\}\s*->\s*\{\*ō\}",
            "a pan-Germanic rule may not produce the Anglo-Frisian rounding")

    def test_sc104_is_the_single_unconditioned_rounding(self):
        body = self.define_body("EAFNasalizedLowRounding")
        self.assertRegex(body, r"\{\*ã\}\s*->\s*\{\*ō\}")
        self.assertNotIn("||", body,
                         "the rounding is unconditioned: every source of *ą̄ "
                         "feeds it (Campbell §128 n. 1 p. 50)")

    # ------------------------------------------------------------------
    # Executable order
    # ------------------------------------------------------------------

    def test_sc103_heads_the_cascade(self):
        self.assertEqual(
            self.positions["PGmcNasalLossBeforeX"],
            min(self.positions.values()),
            "a pan-Germanic change must not be stated after daughter-specific "
            "NWGmc/PWGmc changes")

    def test_all_three_feeders_precede_the_rounding(self):
        rounding = self.positions["EAFNasalizedLowRounding"]
        for feeder in ("PGmcNasalLossBeforeX", "EAFNasalSpirantLengthening",
                       "EAFLongANasalRounding"):
            self.assertLess(self.positions[feeder], rounding,
                            f"{feeder} must feed the rounding")
        rules_between = [
            r for r, p in self.positions.items()
            if self.positions["EAFLongANasalRounding"] < p < rounding]
        self.assertEqual(rules_between, [],
                         "SC104 executes immediately after SC025")

    def test_rounding_precedes_ai_monophthongization(self):
        """Campbell §132 pp. 52-53; R/T vol. 2 pp. 169-170: the new *ā from
        *ai arises after the treatments of the old low vowel."""
        self.assertLess(self.positions["EAFNasalizedLowRounding"],
                        self.positions["EAFAiMonophthongization"])

    def test_composition_order_is_the_defined_order(self):
        self.assertRegex(
            self.uncommented,
            r"\.o\. EAFLongANasalRounding\b\s*\n\s*\.o\. EAFNasalizedLowRounding\b")

    # ------------------------------------------------------------------
    # Registry / edges
    # ------------------------------------------------------------------

    def test_registry_records_the_split(self):
        sc025, sc103, sc104 = (self.registry["SC025"], self.registry["SC103"],
                               self.registry["SC104"])
        self.assertEqual(sc025["fst_identifier"], "EAFLongANasalRounding")
        self.assertEqual(sc025["hist_scope"], "north_sea_germanic")
        self.assertEqual(sc025["verdict"], "SPLIT/REFORMULATE")
        self.assertEqual(sc104["fst_identifier"], "EAFNasalizedLowRounding")
        self.assertEqual(sc104["hist_scope"], "anglo_frisian")
        self.assertEqual(sc103["hist_scope"], "pan_germanic")
        for row in (sc025, sc103, sc104):
            self.assertEqual(row["adjudication_status"], "adjudicated")
            self.assertIn("sc025-sc104-nasalized-low-vowel-adjudication.md",
                          row["adjudication_memo"])

    def test_confidence_attaches_to_the_claim_being_rated(self):
        """The rounding is independently well evidenced even though the *ē₁
        pathway that supplies one of its inputs is disputed."""
        self.assertEqual(self.registry["SC024"]["confidence"], "B")
        self.assertEqual(self.registry["SC025"]["confidence"], "B")
        self.assertEqual(self.registry["SC104"]["confidence"], "A")
        self.assertEqual(self.registry["SC103"]["confidence"], "A")

    def test_every_feeder_has_an_edge_to_the_rounding(self):
        seen = {(e["source_change_id"], e["target_change_id"])
                for e in self.edges}
        for feeder in ("SC025", "SC026", "SC103"):
            self.assertIn((feeder, "SC104"), seen,
                          f"{feeder} feeds SC104 and the edge must be recorded")

    def test_sc104_is_annotated(self):
        self.assertIn("SC104", self.annotations)
        self.assertIn("EAFNasalizedLowRounding",
                      self.annotations["SC104"]["foma_definition_raw"])

    # ------------------------------------------------------------------
    # Reader-facing material
    # ------------------------------------------------------------------

    def test_each_change_has_its_own_reader_chapter(self):
        for fname, anchor in (
            ("103-pgmc-nasal-loss-before-x.md", "{#rule-PGmcNasalLossBeforeX}"),
            ("025-long-a-nasal-rounding.md", "{#rule-EAFLongANasalRounding}"),
            ("104-nasalized-low-vowel-rounding.md",
             "{#rule-EAFNasalizedLowRounding}"),
        ):
            text = (READER / fname).read_text(encoding="utf-8")
            self.assertIn(anchor, text, fname)
            self.assertIn("@Campbell1959", text,
                          f"{fname} must cite its sources")

    def test_memo_exists_and_records_the_verdict(self):
        text = MEMO.read_text(encoding="utf-8")
        self.assertIn("Registry-verdict:", text)
        self.assertIn("SC104", text)

    # ------------------------------------------------------------------
    # Live firing census
    # ------------------------------------------------------------------

    @requires_runtime
    def test_sc025_witnesses_are_nasalized_then_rounded(self):
        for concept in sorted(SC025_WITNESSES):
            with self.subTest(concept=concept):
                form = self.baseline[concept]["proto"].lstrip("*")
                nasalized = self.stage("eaf_long_a_nasal_rounding", form)
                self.assertIn("*ã", nasalized[0])
                rounded = self.stage("eaf_nasalized_low_rounding", form)
                self.assertIn("*ō", rounded[0])
                self.assertNotIn("*ã", rounded[0])

    @requires_runtime
    def test_sc026_low_branch_witness_is_nasalized_then_rounded(self):
        form = self.baseline["goose"]["proto"].lstrip("*")
        self.assertIn("*ã", self.stage("eaf_nasal_spirant_lengthening", form)[0])
        self.assertIn("*ã", self.stage("eaf_nasal_spirant_loss", form)[0])
        self.assertIn("*ō", self.stage("eaf_nasalized_low_rounding", form)[0])

    @requires_runtime
    def test_sc103_high_branch_witness_never_enters_the_rounding(self):
        """fist takes SC103's high branch, so it never enters the rounding
        (contrast `thought`, which takes the low branch)."""
        form = self.baseline["fist"]["proto"].lstrip("*")
        after = self.stage("pgmc_nasal_loss_before_x", form)
        self.assertIn("*ū", after[0])
        self.assertNotIn("*ã", after[0])
        self.assertNotIn(
            "*ã", self.stage("eaf_nasalized_low_rounding", form)[0])

    @requires_runtime
    def test_oral_long_a_from_ai_escapes_the_rounding(self):
        """The counterfeeding control. The *ā of stone/home arises from *ai
        only at SC004, after the rounding, and is oral, so it is not {*ã}."""
        for concept in sorted(ORAL_A_CONTROLS):
            with self.subTest(concept=concept):
                form = self.baseline[concept]["proto"].lstrip("*")
                for stage in ("eaf_long_a_nasal_rounding",
                              "eaf_nasalized_low_rounding"):
                    probe = self.stage(stage, form)
                    self.assertNotIn("*ã", probe[0])
                    self.assertNotIn("*ō", probe[0])
                after_ai = self.stage("eaf_ai_monophthongization", form)
                self.assertIn("*ā", after_ai[0])

    # ------------------------------------------------------------------
    # `thought` — the low-vowel witness of SC103 -> SC104
    # ------------------------------------------------------------------

    def test_thought_is_in_the_corpus_with_the_verified_protoform(self):
        """Ringe 2017 p. 281 gives *þankijaną, *þanhtē, *þanhtaz; p. 136
        (§3.2.4 (iv)) reconstructs the preterite stem *þanh- with the nasal
        still intact before *h.  *θánxtē is that form in the transducer's
        notation (þ = θ, PGmc voiceless velar fricative = *x, acute =
        primary stress), matching *θánkijaną (think) and *fúnxstiz (fist)."""
        row = self.baseline.get("thought")
        self.assertIsNotNone(row, "thought must be a selected corpus row")
        self.assertEqual(row["proto"], THOUGHT_PROTO)
        self.assertEqual(row["outputs"], "þōhte")

    def test_thought_enters_with_its_nasal_intact(self):
        """The nasal loss must be DERIVED by SC103, not assumed in the input;
        otherwise the row would beg the question it is meant to witness."""
        self.assertIn("n", THOUGHT_PROTO)
        self.assertIn("nx", THOUGHT_PROTO)

    def test_the_input_filter_admits_the_nxt_coda(self):
        """*θánxtē was rejected outright before `*nxt` was listed among the
        attested coda clusters; the filter applies only to the input side."""
        self.assertRegex(self.define_body("pgrmCodaComplex"),
                         r"n:\{\*n\}\s+x:\{\*x\}\s+t:\{\*t\}")

    @requires_runtime
    def test_sc103_fires_on_its_low_branch_for_thought(self):
        form = self.baseline["thought"]["proto"].lstrip("*")
        after = self.stage("pgmc_nasal_loss_before_x", form)[0]
        self.assertIn("*ã", after,
                      "SC103's low branch must create the nasalized low vowel")
        self.assertNotIn("*n", after, "SC103 deletes the nasal before *x")
        self.assertNotIn("*ō", after,
                         "a pan-Germanic rule may not do the Anglo-Frisian "
                         "rounding itself")

    @requires_runtime
    def test_sc104_rounds_what_sc103_created(self):
        form = self.baseline["thought"]["proto"].lstrip("*")
        before = self.stage("eaf_long_a_nasal_rounding", form)[0]
        self.assertIn("*ã", before,
                      "the nasalized low vowel must survive untouched from "
                      "SC103 all the way to the rounding")
        after = self.stage("eaf_nasalized_low_rounding", form)[0]
        self.assertIn("*ō", after)
        self.assertNotIn("*ã", after)

    @requires_runtime
    def test_thought_is_not_an_ingvaeonic_nasal_spirant_witness(self):
        """*x is not one of the *f/*þ/*s spirants of the North Sea Germanic
        law, so SC026/SC027 must leave the word alone."""
        form = self.baseline["thought"]["proto"].lstrip("*")
        before = self.stage("pnwgmc_n_stem_n_loss", form)[0]
        for stage in ("eaf_nasal_spirant_lengthening", "eaf_nasal_spirant_loss"):
            with self.subTest(stage=stage):
                self.assertEqual(self.stage(stage, form)[0], before)

    @requires_runtime
    def test_sc028_does_not_fire_on_thought(self):
        """This is what makes `thought` a cleaner SC103 -> SC104 diagnostic
        than `fist`: `fist` loses its *x in the *xst cluster at SC028, so its
        trace confounds the nasal-loss history with the later preconsonantal
        *x loss.  In þōhte the *x survives to the surface as orthographic h.
        SC028 itself is NOT adjudicated here; only its behaviour is observed."""
        thought = self.baseline["thought"]["proto"].lstrip("*")
        before = self.stage("eaf_nasal_spirant_loss", thought)[0]
        after = self.stage("pnwgmc_preconsonantal_x_loss", thought)[0]
        self.assertEqual(before, after, "SC028 must not fire on thought")
        self.assertIn("*x", after, "the *x survives, and surfaces as h")
        fist = self.baseline["fist"]["proto"].lstrip("*")
        self.assertNotEqual(
            self.stage("eaf_nasal_spirant_loss", fist)[0],
            self.stage("pnwgmc_preconsonantal_x_loss", fist)[0],
            "fist, by contrast, does lose its *x at SC028")

    def test_sc103_to_sc104_is_a_witnessed_feeding_edge(self):
        edge = next(e for e in self.edges
                    if e["source_change_id"] == "SC103"
                    and e["target_change_id"] == "SC104")
        self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
        self.assertEqual(edge["witness_role"], "feeding")
        self.assertEqual(edge["representative_lexemes"], "thought")
        self.assertTrue(edge["representative_forms"].strip())

    def test_claimed_chronology_witnesses_are_real_corpus_rows(self):
        """The human edge says what the relation means; the machine checks
        that any lexeme it names actually exists."""
        for edge in self.edges:
            if edge["target_change_id"] != "SC104":
                continue
            for lexeme in re.split(r"[;,]", edge["representative_lexemes"]):
                lexeme = lexeme.strip()
                if not lexeme:
                    continue
                with self.subTest(edge=edge["source_change_id"], lexeme=lexeme):
                    self.assertIn(lexeme, self.baseline)

    # ------------------------------------------------------------------
    # Output neutrality
    # ------------------------------------------------------------------

    def test_surface_outputs_are_unchanged(self):
        for concept, attested in {**SC025_WITNESSES, **SC026_LOW_WITNESS,
                                  **SC103_WITNESS, **SC103_LOW_WITNESS,
                                  **ORAL_A_CONTROLS}.items():
            with self.subTest(concept=concept):
                self.assertEqual(self.baseline[concept]["outputs"], attested)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
