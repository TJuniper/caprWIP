#!/usr/bin/env python3
"""Regression for the *ē₁-complex re-adjudication (SC024/SC025/SC101, 2026).

Governing memo:
Germanic/docs/sound_changes/audits/sc024-sc025-sc101-e1-complex-adjudication.md
(supersedes in implementation sc024-adjudication.md).

Protected scientific conclusions:

  * Change A exists independently: SC024 `PNWGmcLongELowering` is
    `{*ḗ} -> {*ā}` — stressed tier only, unconditioned (nasal forms
    included), producing the reconstructed intermediate *ā (R/T 2014
    pp. 11–13, *mānōþ-, *spānuz) — at executable position 4, before
    every genuinely PWGmc innovation (2nd-c. runic dating).
  * Change B exists independently and consumes the correct input:
    SC101 `EAFLongAFronting` fronts `{*ā}` before non-nasal, non-*w
    consonants, and before *w + high front vocalic, at position 28;
    SC025 `EAFLongANasalRounding` is `{*ā} -> {*ō}` before nasal, at
    position 27. Both are fed by SC024.
  * SC102 `EAFHiatusWInsertion` (position 26) is the pre-OE/Anglo-
    Frisian hiatus *w of the verba pura (R/T p. 12, p. 151;
    Þórhallsdóttir 1993): *sāaną > *sāwaną. It is fed by SC024 and
    feeds the *w-block of SC101 (sow: sāwan, not **sǣwan).
  * lǣwan 'betray' is the positive *w + high-front control: its
    inherited *w is followed by *i at the fronting stage, and SC101
    itself (not later i-umlaut) fronts *lāwijaną > *lǣwijaną.
  * *ā < *ai arises too late to be fronted or rounded: SC004 stands at
    position 29, after both (Campbell §132; R/T pp. 169–170) — stone,
    home, loath, rope, token, soul, ghost keep back ā.
  * The old one-step `*ē/*ḗ -> *ǣ` telescoping must not silently return.
  * The five unstressed selected-input tokens (father, mother, sister,
    have, live) are NOT SC024 witnesses: their plain unstressed {*ē}
    passes the stressed rule untouched and takes the §6.8.3
    unstressed-shortening path, still surfacing short (fæder etc.).
  * SC101 < SC056: WS palatal diphthongization operated on the
    already-fronted vowel (sheep sċēap, year ġēar).
  * Canonical registry metadata matches each distinct historical change
    (SC024 pnwgmc/pan_pnwgmc; SC025 and SC101 eaf/north_sea_germanic;
    all confidence B) and each has its own reader-facing write-up.

Run: cd Germanic/tests && python3 -m unittest test_sc024_adjudication
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
BASELINE = SC_DIR / "cascade_baseline" / "cascade_baseline_outputs.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
HISTORICAL_AUDIT = SC_DIR / "cascade_baseline" / "historical_audit_table.tsv"
RENAME_MANIFEST = SC_DIR / "cascade_baseline" / "rename_migration_manifest.tsv"
CARDS = SC_DIR / "order_tests" / "chronology_cards"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
MEMO = SC_DIR / "audits" / "sc024-sc025-sc101-e1-complex-adjudication.md"
OLD_MEMO = SC_DIR / "audits" / "sc024-adjudication.md"
READER = SC_DIR / "reader_facing"
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"


# Live-probe availability: these adjudication files mix committed-evidence
# assertions (always run) with live flookup probes against the untracked
# sandbox bins built by `adjudicate --evidence`. The probes are skipped when
# the local runtime build is absent (e.g. clean CI checkout).
RUNTIME_BUILT = ((BIN_DIR / "old_english.bin").is_file()
                 and shutil.which("flookup") is not None)
requires_runtime = unittest.skipUnless(
    RUNTIME_BUILT,
    "live runtime probe: needs local sandbox bins (adjudicate --evidence) "
    "and flookup on PATH")

# Change A census: 13 stressed oral roots + the two nasal-branch lexemes,
# which historically DID undergo *ē₁ > *ā (R/T p. 11: *mānōþ-, *spānuz),
# + the two *w-conditioning witnesses (sow, betray).
ORAL_ROOT_CONCEPTS = {
    "adder", "bier", "deed", "eel", "hair", "let", "meal", "needle",
    "read", "sheep", "sleep", "weapon", "year",
}
NASAL_BRANCH_CONCEPTS = {"month", "spoon"}
W_CONDITION_CONCEPTS = {"sow", "betray"}
SC024_FIRING_CONCEPTS = (
    ORAL_ROOT_CONCEPTS | NASAL_BRANCH_CONCEPTS | W_CONDITION_CONCEPTS
)

# Unstressed selected-input tokens: plain {*ē}, outside the stressed law.
UNSTRESSED_CONCEPTS = {"father", "mother", "sister", "have", "live"}
UNSTRESSED_ATTESTED = {
    "father": "fæder", "mother": "mōder", "sister": "swester",
    "have": "hæfeþ", "live": "lifeþ",
}

# ā < *ai negative controls (never fronted/rounded).
AI_BRANCH_CONTROLS = {"stone": "stān", "home": "hām"}


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


class E1ComplexAdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        cls.trace = load_trace_tool()
        with BASELINE.open(encoding="utf-8") as handle:
            cls.baseline = {
                row["concept"]: row
                for row in csv.DictReader(handle, delimiter="\t")
            }
        with MANIFEST.open(encoding="utf-8") as handle:
            cls.positions = {
                row["foma_identifier"]: int(row["position"])
                for row in csv.DictReader(handle, delimiter="\t")
            }

    def stage(self, name, form):
        return self.trace.run_stage(
            BIN_DIR, f"old_english_sandbox_after_{name}.bin", form
        )

    def across_sc024(self, form):
        before = self.stage("pnwgmc_a_to_u_before_m", form)
        after = self.stage("pnwgmc_long_e_lowering", form)
        return before, after

    def across_w_insertion(self, form):
        # The checkpoint immediately preceding SC102 is EAFNasalSpirantLoss;
        # it was SC028 PNWGmcPreconsonantalXLoss until the SC028 adjudication
        # moved that rule to its northern West Germanic position.
        before = self.stage("eaf_nasal_spirant_loss", form)
        after = self.stage("eaf_hiatus_w_insertion", form)
        return before, after

    def across_rounding(self, form):
        before = self.stage("eaf_hiatus_w_insertion", form)
        after = self.stage("eaf_long_a_nasal_rounding", form)
        return before, after

    def across_nasalized_rounding(self, form):
        before = self.stage("eaf_long_a_nasal_rounding", form)
        after = self.stage("eaf_nasalized_low_rounding", form)
        return before, after

    def across_fronting(self, form):
        before = self.stage("eaf_long_a_nasal_rounding", form)
        after = self.stage("eaf_long_a_fronting", form)
        return before, after

    # ------------------------------------------------------------------
    # Executable rules: two changes, correct inputs and outputs
    # ------------------------------------------------------------------

    def test_change_a_is_unconditioned_stressed_lowering_to_a(self):
        match = re.search(
            r"define\s+PNWGmcLongELowering\s*Ctx\(\[\s*\[\s*\{\*ḗ\}\s*->\s*\{\*ā\}\s*\]\s*\]\);",
            self.uncommented,
        )
        self.assertIsNotNone(
            match,
            "SC024 must be the unconditioned stressed lowering "
            "{*ḗ} -> {*ā} (Change A of the e1 complex)",
        )

    def test_change_b_rules_consume_long_a(self):
        self.assertIsNotNone(re.search(
            r"define\s+EAFLongANasalRounding\s*\[\s*\{\*ā\}\s*->\s*\{\*ã\}"
            r"\s*\|\|\s*_\s*EnglishStarNasal\s*\];",
            self.uncommented,
        ), "SC025 must nasalize the historical *ā before nasals")
        self.assertIsNotNone(re.search(
            r"define\s+EAFNasalizedLowRounding\s*\[\s*"
            r"\{\*ã\}\s*->\s*\{\*ō\}\s*\];",
            self.uncommented,
        ), "SC104 must round the long nasalized low vowel to *ō")
        self.assertIsNotNone(re.search(
            r"define\s+EAFLongAFronting\s*\[\s*"
            r"\{\*ā\}\s*->\s*\{\*ǣ\}\s*\|\|\s*_\s*"
            r"\[EnglishStarConsonant\s*-\s*EnglishStarNasal\s*-\s*\{\*w\}\]\s*,\s*"
            r"\{\*ā\}\s*->\s*\{\*ǣ\}\s*\|\|\s*_\s*\{\*w\}\s*EnglishIUmlautTrigger\s*\];",
            self.uncommented,
        ), "SC101 must front non-nasalized *ā with the historical *w "
           "conditioning: blocked before *w except before *w + high front "
           "vocalic (R/T pp. 150–151)")
        self.assertIsNotNone(re.search(
            r"define\s+EAFHiatusWInsertion\s*\[\s*\[\.\.\]\s*->\s*\{\*w\}"
            r"\s*\|\|\s*\{\*ā\}\s*_\s*EnglishStarVocalic\s*\];",
            self.uncommented,
        ), "SC102 must insert the hiatus *w after long *ā (verba pura)")

    def test_one_step_telescoping_cannot_silently_return(self):
        self.assertIsNone(
            re.search(r"\{\*ē\}\s*->\s*\{\*ǣ\}|\{\*ḗ\}\s*->\s*\{\*ǣ\}",
                      self.uncommented),
            "the retired one-step *ē/*ḗ -> *ǣ telescoping has returned",
        )
        self.assertIsNone(
            re.search(r"\{\*ē\}\s*->\s*\{\*ō\}|\{\*ḗ\}\s*->\s*\{\*ō\}",
                      self.uncommented),
            "the retired direct *ē -> *ō nasal bypass has returned",
        )

    def test_cascade_positions_encode_the_chronology(self):
        # Positions are projections of the current cascade; only the
        # RELATIVE order carries the historical claims (§ chronology).
        # SC024 must be a live numbered stage ...
        self.assertIn("PNWGmcLongELowering", self.positions)
        # ... and the SC102/SC025/SC104/SC101/SC004 fronting-rounding block
        # must keep its adjudicated internal order.
        block = ["EAFHiatusWInsertion", "EAFLongANasalRounding",
                 "EAFNasalizedLowRounding", "EAFLongAFronting",
                 "EAFAiMonophthongization"]
        for earlier, later in zip(block, block[1:]):
            self.assertLess(self.positions[earlier], self.positions[later],
                            f"{earlier} must precede {later}")
        # SC024 is early pan-NWGmc: it must precede the genuinely PWGmc
        # innovations (early i-apocope, *ij contraction, j-gemination,
        # syllabic *j, dental hardening)
        for pwgmc_rule in ("PWGmcEarlyIApocope", "PWGmcIjContraction",
                           "PWGmcJGemination", "PWGmcSyllabicJ",
                           "PWGmcDentalHardening"):
            self.assertLess(
                self.positions["PNWGmcLongELowering"],
                self.positions[pwgmc_rule],
                f"SC024 (2nd-c. pan-NWGmc) must precede {pwgmc_rule}",
            )
        # SC102 feeds the *w-block of SC101 (historical chronology,
        # R/T p. 151) and follows SC024 (feeding)
        self.assertLess(self.positions["PNWGmcLongELowering"],
                        self.positions["EAFHiatusWInsertion"])
        self.assertLess(self.positions["EAFHiatusWInsertion"],
                        self.positions["EAFLongAFronting"])
        # SC101 < SC056 (sheep/year: diphthongization of already-fronted ǣ)
        self.assertLess(self.positions["EAFLongAFronting"],
                        self.positions["OEWsPalatalDiphthongization"])

    # ------------------------------------------------------------------
    # Change A firing census (live stage bins)
    # ------------------------------------------------------------------

    @requires_runtime
    def test_change_a_fires_on_exactly_the_17_stressed_e1_lexemes(self):
        fired = set()
        candidates = {
            concept: row for concept, row in self.baseline.items()
            if ("ē" in row["proto"] or "ḗ" in row["proto"])
        }
        for concept, row in sorted(candidates.items()):
            before, after = self.across_sc024(row["proto"].lstrip("*"))
            if before != after:
                fired.add(concept)
        self.assertEqual(
            fired,
            SC024_FIRING_CONCEPTS,
            "SC024 (Change A) census drifted; expected the 13 stressed "
            "oral roots, month and spoon (which pass through *ā), and "
            "the *w-conditioning witnesses sow and betray",
        )

    @requires_runtime
    def test_change_a_produces_the_reconstructed_intermediate_a(self):
        self.assertEqual(
            self.across_sc024("skḗpą"), (["*s*k*ḗ*p*ą"], ["*s*k*ā*p*ą"])
        )
        self.assertEqual(
            self.across_sc024("mḗnōθz"), (["*m*ḗ*n*ō*θ*z"], ["*m*ā*n*ō*θ*z"])
        )
        self.assertEqual(
            self.across_sc024("spḗnuz"), (["*s*p*ḗ*n*u*z"], ["*s*p*ā*n*u*z"])
        )

    @requires_runtime
    def test_unstressed_tokens_do_not_fire_and_surface_short(self):
        for concept in sorted(UNSTRESSED_CONCEPTS):
            row = self.baseline[concept]
            before, after = self.across_sc024(row["proto"].lstrip("*"))
            self.assertEqual(
                before, after,
                f"{concept} carries unstressed *ē and must not undergo "
                "the stressed lowering (R/T p. 13 n. 3)",
            )
            self.assertEqual(
                row["outputs"], UNSTRESSED_ATTESTED[concept],
                f"{concept} must still surface with its short unstressed "
                "vowel via the §6.8.3 shortening path",
            )

    # ------------------------------------------------------------------
    # Change B: rounding and fronting consume the *ā
    # ------------------------------------------------------------------

    @requires_runtime
    def test_nasal_branch_nasalizes_then_rounds_the_intermediate_a(self):
        """SC025 only nasalizes (*ā > *ą̄, spelled {*ã}); the rounding to *ō is
        the separate Anglo-Frisian SC104 EAFNasalizedLowRounding, which the
        SC025/SC104 adjudication split out of the old telescoped rule."""
        for concept in sorted(NASAL_BRANCH_CONCEPTS):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            before, after = self.across_rounding(form)
            self.assertNotEqual(
                before, after,
                f"{concept} must be nasalized by SC025 EAFLongANasalRounding",
            )
            self.assertIn("*ã", after[0])
            before, after = self.across_nasalized_rounding(form)
            self.assertNotEqual(
                before, after,
                f"{concept} must be rounded by SC104 EAFNasalizedLowRounding",
            )
            self.assertIn("*ō", after[0])
            self.assertNotIn("*ã", after[0])
        self.assertEqual(self.baseline["month"]["outputs"], "mōnaþ")
        self.assertEqual(self.baseline["spoon"]["outputs"], "spōn")

    @requires_runtime
    def test_oral_branch_fronts_the_intermediate_a(self):
        self.assertEqual(
            self.across_fronting("skāpą"), (["*s*k*ā*p*ą"], ["*s*k*ǣ*p*ą"])
        )
        self.assertEqual(
            self.across_fronting("jārą"), (["*j*ā*r*ą"], ["*j*ǣ*r*ą"])
        )
        self.assertEqual(self.baseline["sheep"]["outputs"], "sċēap")
        self.assertEqual(self.baseline["year"]["outputs"], "ġēar")

    # ------------------------------------------------------------------
    # The *w conditioning: SC102 feeds the block, lǣwan is the control
    # ------------------------------------------------------------------

    @requires_runtime
    def test_sow_undergoes_change_a(self):
        self.assertEqual(
            self.across_sc024("sḗaną"), (["*s*ḗ*a*n*ą"], ["*s*ā*a*n*ą"])
        )

    @requires_runtime
    def test_sc102_inserts_the_hiatus_w_in_sow_only(self):
        self.assertEqual(
            self.across_w_insertion("sḗaną"),
            (["*s*ā*a*n*ą"], ["*s*ā*w*a*n*ą"]),
            "SC102 must repair the *ā.a hiatus of sow with *w "
            "(R/T p. 12: *sāaną > OE sāwan)",
        )
        fired = []
        # *ā at position 25 can only come from SC024 (*ē₁) or be inherited
        # (*ā did not exist in PGmc); restrict the census accordingly
        for concept, row in sorted(self.baseline.items()):
            proto = row["proto"]
            if not ("ē" in proto or "ḗ" in proto or "ā" in proto):
                continue
            before, after = self.across_w_insertion(proto.lstrip("*"))
            if before != after:
                fired.append(concept)
        self.assertEqual(fired, ["sow"],
                         "SC102 must fire on exactly the one verba-pura "
                         "witness in the corpus")

    @requires_runtime
    def test_sc101_is_blocked_before_w_in_sow(self):
        before, after = self.across_fronting("sḗaną")
        self.assertEqual(before, after,
                         "sow's *ā must NOT front before its hiatus *w "
                         "(R/T p. 151; Hogg 1992: 81)")
        self.assertEqual(after, ["*s*ā*w*a*n*ą"])
        self.assertEqual(self.baseline["sow"]["outputs"], "sāwan")

    @requires_runtime
    def test_sc101_fronts_betray_at_its_own_boundary(self):
        # the front vowel must appear AT the SC101 stage bin, not later
        # via i-umlaut: *lāwijaną > *lǣwijaną (R/T p. 150)
        before, after = self.across_fronting("lḗwijaną")
        self.assertNotEqual(before, after,
                            "betray's *ā must front before *w + *i "
                            "(the high-front exception to the *w block)")
        self.assertEqual(before, ["*l*ā*w*i*j*a*n*ą"])
        self.assertEqual(after, ["*l*ǣ*w*i*j*a*n*ą"])
        self.assertEqual(self.baseline["betray"]["outputs"], "lǣwan")

    @requires_runtime
    def test_a_from_ai_arises_too_late_to_front_or_round(self):
        for concept, attested in sorted(AI_BRANCH_CONTROLS.items()):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            # untouched by A (no *ē₁), by w-insertion, by rounding and by
            # fronting (its ā does not exist yet at positions 26–28)
            for probe in (self.across_sc024, self.across_w_insertion,
                          self.across_rounding, self.across_fronting):
                before, after = probe(form)
                self.assertEqual(
                    before, after,
                    f"{concept} ({row['proto']}) has *ai, whose ā arises "
                    "only at SC004; it must pass positions 4/26/27/28 untouched",
                )
            self.assertEqual(row["outputs"], attested)

    # ------------------------------------------------------------------
    # Canonical registry metadata
    # ------------------------------------------------------------------

    def test_registry_metadata_matches_the_two_change_architecture(self):
        registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        sc024, sc025, sc101, sc102 = (registry["SC024"], registry["SC025"],
                                      registry["SC101"], registry["SC102"])
        self.assertEqual(sc024["fst_identifier"], "PNWGmcLongELowering")
        self.assertEqual(sc024["hist_stage"], "pnwgmc")
        self.assertEqual(sc024["hist_scope"], "pan_pnwgmc")
        self.assertEqual(sc024["verdict"], "SPLIT/REFORMULATE/REORDER")
        self.assertEqual(sc025["fst_identifier"], "EAFLongANasalRounding")
        self.assertEqual(sc025["hist_stage"], "eaf")
        self.assertEqual(sc025["hist_scope"], "north_sea_germanic")
        # SC025 was itself split by the SC025/SC104 nasalized-low-vowel
        # adjudication: it now states only the nasalization, and the
        # Anglo-Frisian rounding is SC104.
        self.assertEqual(sc025["verdict"], "SPLIT/REFORMULATE")
        self.assertEqual(sc101["fst_identifier"], "EAFLongAFronting")
        self.assertEqual(sc101["hist_stage"], "eaf")
        self.assertEqual(sc101["hist_scope"], "north_sea_germanic")
        self.assertEqual(sc101["verdict"], "SPLIT/RESTRICT")
        # SC102 is Anglo-Frisian only: OS/OHG repaired the hiatus with *j
        self.assertEqual(sc102["fst_identifier"], "EAFHiatusWInsertion")
        self.assertEqual(sc102["hist_stage"], "eaf")
        self.assertEqual(sc102["hist_scope"], "anglo_frisian")
        self.assertEqual(sc102["verdict"], "SPLIT")
        for row in (sc024, sc025, sc101):
            self.assertEqual(row["confidence"], "B",
                             "the two-step *ē₁ reconstruction is disputed "
                             "(Fulk 2018 §4.6; Bennett 1950); confidence "
                             "must stay B")
        # SC102's B has an independent rationale: the broad innovation is
        # supported by the scholarship consulted, but the phonological-
        # versus-analogical architecture has not been adjudicated from the
        # specialist source. It must NOT ride on the *ē₁ controversy.
        self.assertEqual(sc102["confidence"], "A",
                         "SC102 was raised to A when Þórhallsdóttir 1993 "
                         "was acquired and read (memo §13.4): the sole "
                         "stated ground of its B was that the phonological-"
                         "versus-analogical architecture had not been "
                         "checked against the specialist source")
        for row in (sc024, sc025, sc101, sc102):
            self.assertEqual(row["adjudication_status"], "adjudicated")
        for row in (sc024, sc101, sc102):
            self.assertIn("sc024-sc025-sc101-e1-complex-adjudication.md",
                          row["adjudication_memo"])
        # SC025's governing memo is now the nasalized-low-vowel adjudication
        self.assertIn("sc025-sc104-nasalized-low-vowel-adjudication.md",
                      sc025["adjudication_memo"])

    def test_staging_map_view_matches(self):
        staging = {r["sc_id"]: r for r in _tsv_rows(STAGING_MAP)}
        self.assertEqual(staging["SC024"]["hist_stage"], "pnwgmc")
        self.assertEqual(staging["SC025"]["fst_identifier"],
                         "EAFLongANasalRounding")
        self.assertEqual(staging["SC101"]["fst_identifier"],
                         "EAFLongAFronting")

    def test_rename_manifest_records_the_sc025_second_migration(self):
        rename = {r["sc_id"]: r for r in _tsv_rows(RENAME_MANIFEST)}
        self.assertEqual(rename["SC025"]["canonical_foma_identifier"],
                         "EAFLongANasalRounding")
        self.assertEqual(rename["SC025"]["canonical_hist_stage"], "eaf")
        self.assertEqual(rename["SC024"]["canonical_hist_stage"], "pnwgmc")

    # ------------------------------------------------------------------
    # Chronology edges
    # ------------------------------------------------------------------

    def edge(self, src, tgt):
        rows = [r for r in _tsv_rows(EDGES)
                if r["source_change_id"] == src
                and r["target_change_id"] == tgt]
        self.assertEqual(len(rows), 1, f"expected exactly one {src}->{tgt} edge")
        return rows[0]

    def test_feeding_edges_from_change_a(self):
        for tgt in ("SC025", "SC101", "SC102"):
            edge = self.edge("SC024", tgt)
            self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
            self.assertEqual(edge["relation_type"], "one_sided_chronology")

    def test_sc102_before_sc101_is_a_recorded_historical_assertion(self):
        edge = self.edge("SC102", "SC101")
        self.assertEqual(edge["direction_basis"], "later_boundary")
        self.assertIn("historically asserted", edge["notes"].lower())

    def test_pre_sc004_edges_encode_campbell_132(self):
        self.assertEqual(self.edge("SC025", "SC004")["representative_lexemes"],
                         "stone; home")
        self.assertIn("ghost", self.edge("SC101", "SC004")["representative_lexemes"])

    def test_sheep_year_sc056_edge_now_attaches_to_sc101(self):
        edge = self.edge("SC101", "SC056")
        self.assertEqual(edge["representative_lexemes"], "sheep; year")
        self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
        self.assertFalse(
            [r for r in _tsv_rows(EDGES)
             if r["source_change_id"] == "SC024"
             and r["target_change_id"] == "SC056"],
            "the old SC024->SC056 edge must not survive; it belongs to SC101",
        )

    def test_earlier_side_of_change_a_stays_runner_limited(self):
        edge = self.edge("SC024", "EarlyEnglishLineChanges")
        self.assertEqual(edge["relation_type"], "runner_limited_boundary")
        self.assertIn("not a real lower boundary", edge["notes"])

    # ------------------------------------------------------------------
    # Memos and reader-facing write-ups
    # ------------------------------------------------------------------

    def test_governing_memo_and_supersession(self):
        memo = MEMO.read_text(encoding="utf-8")
        self.assertTrue(memo.splitlines()[2].startswith(
            "Registry-verdict: SC024=SPLIT/REFORMULATE/REORDER; "
            "SC025=REFORMULATE/REORDER; SC101=SPLIT/RESTRICT; SC102=SPLIT"))
        old = OLD_MEMO.read_text(encoding="utf-8")
        self.assertIn("SUPERSEDED IN IMPLEMENTATION", old)

    def test_each_change_has_its_own_reader_chapter(self):
        for fname, anchor, cite in (
            ("024-long-e-lowering.md", "{#rule-PNWGmcLongELowering}",
             "[@RingeTaylor2014, pp. 11--13]"),
            ("025-long-a-nasal-rounding.md", "{#rule-EAFLongANasalRounding}",
             "[@RingeTaylor2014, pp. 150--151]"),
            ("101-long-a-fronting.md", "{#rule-EAFLongAFronting}",
             "[@RingeTaylor2014, pp. 146--150"),
            ("102-hiatus-w-insertion.md", "{#rule-EAFHiatusWInsertion}",
             "[@RingeTaylor2014, p. 151]"),
        ):
            text = (READER / fname).read_text(encoding="utf-8")
            self.assertIn(anchor, text, fname)
            self.assertIn(cite, text, f"{fname} must cite its sources")
        # the dispute must be recorded, not suppressed
        self.assertIn("@Fulk2018",
                      (READER / "024-long-e-lowering.md").read_text(encoding="utf-8"))
        # the SC101 chapter must document BOTH sides of the *w condition
        fronting = (READER / "101-long-a-fronting.md").read_text(encoding="utf-8")
        self.assertIn("sāwan", fronting)
        self.assertIn("lǣwan", fronting)
        self.assertNotIn("without being encoded", fronting,
                         "the SC101 chapter must no longer describe the "
                         "*w restriction as unencoded")

    def test_reader_chapters_carry_no_research_process_language(self):
        """Reader prose is scholarship, not a source-acquisition log.

        The source-status audit lives in the governing memo (§13). None
        of it may leak into the chapters.
        """
        banned = (
            "pending direct verification", "pending acquisition",
            "not locally available", "not yet consulted",
            "have not consulted", "direct verification",
            "we are waiting", "lacks the source", "SC102A",
            "PDF", "refs.bib", "repository",
        )
        for fname in ("024-long-e-lowering.md", "025-long-a-nasal-rounding.md",
                      "101-long-a-fronting.md", "102-hiatus-w-insertion.md"):
            text = (READER / fname).read_text(encoding="utf-8")
            for phrase in banned:
                self.assertNotIn(phrase.lower(), text.lower(),
                                 f"{fname} must not contain research-process "
                                 f"language ({phrase!r})")

    def test_reader_chapters_cite_only_directly_consulted_sources(self):
        """No page-precise citation to a source CAPR holds only at second hand.

        Stiles 2004 and Grønvik 1981/1998 are known through Ringe &
        Taylor or Fulk (memo §13.2). Where the present account rests on
        them, the chapters must cite the source actually consulted.
        Bennett 1950, Þórhallsdóttir 1993 and Lid 1952 are NOT on this
        list: all three were acquired and read directly (memo §13.1).
        """
        indirect = ("@Stiles2004", "@Gronvik1981", "@Gronvik1998")
        for path in sorted(READER.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            for key in indirect:
                self.assertNotIn(key, text,
                                 f"{path.name} cites {key}, which CAPR "
                                 "knows only through another source; cite "
                                 "the source actually relied upon")
        # the SC102 chapter must rest on the account actually consulted
        self.assertIn("[@RingeTaylor2014, p. 151]",
                      (READER / "102-hiatus-w-insertion.md").read_text(encoding="utf-8"))

    def test_memo_records_the_adjudicated_sc102_decomposition(self):
        """The phonology-vs-analogy question is settled from the source.

        Þórhallsdóttir 1993 was acquired and read, so the memo must now
        answer all five questions the deferral posed, and must record the
        verdict as "no split" for stated reasons rather than leaving it
        open. The reasons themselves are load-bearing: a split is refused
        because the phonological environment has no witness in a
        citation-form corpus and because the generalization is analogy.
        """
        memo = MEMO.read_text(encoding="utf-8")
        flat = " ".join(memo.replace("*", "").split())
        # the deferral is discharged, not silently dropped
        self.assertIn("The deferral is discharged", flat)
        self.assertNotIn("reserved for later direct source-led adjudication",
                         flat)
        # source-status audit present, with the three-way distinction
        self.assertIn("Directly verified", memo)
        self.assertIn("Known only indirectly", memo)
        self.assertIn("Pending direct verification", memo)
        # SC102's confidence must remain decoupled from the ē₁ controversy
        self.assertIn("Verdict: no split", flat)
        # the two mechanisms must still be described distinctly: the
        # phonological insertion is restricted to the pre-*u cells, the
        # generalization is analogy
        self.assertIn("The environment is narrow and explicit", flat)
        self.assertIn("1st person singular and plural", flat)
        self.assertIn("analogy, not sound change", flat)
        # and the reason for refusing the split must be recorded
        self.assertIn("unrepresentable in this corpus", flat)
        # the identifier rename is recorded as outstanding, not done here
        self.assertIn("EAFHiatusWInsertion", memo)
        self.assertIn("behaviour-neutral", flat)
        # Þórhallsdóttir supplies no evidence for the SC102 < SC101 order
        self.assertIn("no independent evidence", flat)

    def test_sc102_confidence_rationale_is_not_the_e1_controversy(self):
        rows = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        sc102 = rows["SC102"]
        blob = " ".join(sc102.values())
        # the A rests on the specialist source having been read directly,
        # never on the *ē₁ reconstruction dispute that governs SC024/025/101
        self.assertIn("READ DIRECTLY", blob)
        self.assertIn("citation-form proxy", blob)
        self.assertNotIn("two-step", blob,
                         "SC102's rationale must not invoke the *ē₁ "
                         "two-step reconstruction dispute")

    def test_no_canonical_claim_that_the_w_restriction_is_unencoded(self):
        """The *w condition is encoded as of a90d33cb; stale prose must go."""
        stale = ("documented, not encoded", "documented rather than encoded",
                 "has no corpus witness and is documented",
                 "no corpus row reaches the *w environment")
        for path in (REGISTRY, SC_DIR / "registry" / "sc_inventory_annotations.tsv",
                     INVENTORY, STAGING_MAP):
            text = path.read_text(encoding="utf-8")
            for phrase in stale:
                self.assertNotIn(phrase, text,
                                 f"{path.name} still claims the *w "
                                 "restriction is unencoded")

    def test_card_index_rows_exist_for_the_adjudicated_changes(self):
        """Mechanical consistency for the four adjudicated rows. The registry
        stores no positions and the card index is an experiment-time ARCHIVE
        (oe_pipeline is the sole order authority), so only identity and
        archival membership are checked here."""
        manifest = {r["foma_identifier"]: r["position"] for r in _tsv_rows(MANIFEST)}
        registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        index = {r["change_id"]: r
                 for r in _tsv_rows(CARDS / "chronology_card_index.tsv")}
        for sc_id in ("SC024", "SC025", "SC101", "SC102"):
            fst = registry[sc_id]["fst_identifier"]
            self.assertIn(fst, manifest,
                          f"{sc_id}: rule missing from the cascade manifest")
            self.assertIn(sc_id, index,
                          f"{sc_id}: missing from the archival chronology "
                          "card index")

    def test_chronology_cards_exist_for_all_four(self):
        for fname in ("SC024-nwgmc-long-e-lowering.md",
                      "SC025-eaf-long-a-nasal-rounding.md",
                      "SC101-eaf-long-a-fronting.md",
                      "SC102-eaf-hiatus-w-insertion.md"):
            card = (CARDS / fname).read_text(encoding="utf-8")
            self.assertIn("sc024-sc025-sc101-e1-complex-adjudication.md", card)


if __name__ == "__main__":
    unittest.main()
