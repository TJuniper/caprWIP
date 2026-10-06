#!/usr/bin/env python3
"""SC016/SC017 chronology-repair invariants (sc016-017-adjudication.md).

Host-runnable, file-based: asserts on germanic.txt, the cascade order
manifest, the historical partial order, the audit matrix, and the committed
cascade baseline outputs. No foma at test time.

The adjudicated history (Fulk §4.3 p.56; Campbell §44, §115; Brunner §92.1;
Bülbring §§298-299; R&T pp.5, 129; Hogg p.112):

    SC017 PNWGmcULowering is Northwest Germanic phonology and executes in
    the NWGmc corridor. SC016 OEWsPalatalGlide is the Old English / West
    Saxon glide SPELLING of back vowels after word-initial ġ; it executes
    in the written-surface block after OldEnglishOrthography and is FED by
    SC017 (yoke: *juką > *joką > ġeoc). The former inverted executable
    order (SC016 before SC017 as a "technical dependency") is retired.

Run: cd Germanic/tests && python3 -m pytest test_sc016_sc017_chronology.py
"""
from __future__ import annotations

import csv
import io
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
SANDBOX = REPO_ROOT / "Germanic/fsts/old_english_sandbox.txt"
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
PARTIAL_ORDER = SC_DIR / "cascade_baseline/historical_partial_order.tsv"
BASELINE = SC_DIR / "cascade_baseline/cascade_baseline_outputs.tsv"
AUDIT = SC_DIR / "audits/sc001-sc020-chronology-audit.tsv"
ADJUDICATION = SC_DIR / "audits/sc016-017-adjudication.md"
COMPACT = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
RULE_COVERAGE = SC_DIR / "cascade_baseline/rule_coverage_census.tsv"


def _read_tsv(path):
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


class RuleBodyTests(unittest.TestCase):
    """The repaired SC016 formulation must not silently revert."""

    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")

    def _define(self, name):
        m = re.search(r"define\s+" + name + r"\s*(?:Ctx\()?\[(.*?)\]\)?;", self.text, re.S)
        self.assertIsNotNone(m, f"define {name} not found")
        return re.sub(r"(?m)^\s*#.*$", "", m.group(1))

    def test_sc016_targets_back_vowels_after_initial_palatal_g(self):
        """Domain = back vowels (o and u, long and short) after word-initial
        ġ — the o-clause is what the retired formulation lacked (Brunner
        §92.1b; Bülbring §299: gioc/geoc from WGmc *jok)."""
        body = re.sub(r"\s+", " ", self._define("OEWsPalatalGlide")).strip()
        for clause in (r"{*ó} -> {*éo} || .#. ġ _",
                       r"{*ú} -> {*éo} || .#. ġ _",
                       r"{*o} -> {*eo} || .#. ġ _",
                       r"{*u} -> {*eo} || .#. ġ _"):
            self.assertIn(clause, body,
                          f"repaired SC016 lost the clause {clause!r}")

    def test_sc016_old_insertion_formulation_is_gone(self):
        """The retired *ju > *jeu insertion (with unsatisfiable ʤ/ʧ/ʃ
        clauses) must not reappear anywhere in the cascade source."""
        stripped = re.sub(r"(?m)#.*$", "", self.text)
        self.assertNotIn("{*j} {*e} {*u}", stripped,
                         "the retired early glide-insertion body has returned")

    def test_sc093_oe_glide_u_to_eo_absorbed(self):
        """OEGlideUToEO (SC093, 0 firings) was absorbed by the repaired
        SC016 and must not survive as a separate define."""
        stripped = re.sub(r"(?m)#.*$", "", self.text)
        self.assertNotRegex(stripped, r"define\s+OEGlideUToEO\b",
                            "OEGlideUToEO should be absorbed into SC016")

    def test_sc017_formulation_unchanged(self):
        """The adjudication confirmed SC017 unchanged: onset *j does not
        block lowering (Fulk §4.3 p.56); the NoJ restriction applies only
        between target and trigger."""
        body = re.sub(r"\s+", " ", self._define("PNWGmcULowering"))
        self.assertIn("{*u} -> {*o}", body)
        self.assertIn("{*ú} -> {*ó}", body)
        self.assertIn(".#. EnglishStarConsonant* _", body,
                      "SC017 must still admit onset consonants incl. *j")
        self.assertIn("EnglishStarConsonantNoJ* EnglishStarNonHighVowel", body)


class CompositionOrderTests(unittest.TestCase):
    """Executable order = adjudicated historical chronology."""

    @classmethod
    def setUpClass(cls):
        rows = _read_tsv(MANIFEST)
        cls.pos = {r["foma_identifier"]: int(r["position"]) for r in rows}
        cls.block = {r["foma_identifier"]: r["origin_block"] for r in rows}

    def test_sc017_executes_before_sc016(self):
        self.assertLess(self.pos["PNWGmcULowering"], self.pos["OEWsPalatalGlide"],
                        "u-lowering must feed the WS glide spelling (yoke)")

    def test_sc016_sits_in_the_written_surface_block(self):
        self.assertEqual(self.block["OEWsPalatalGlide"], "OldEnglishRules",
                         "SC016 is an OE written-surface convention")
        self.assertLess(self.pos["OldEnglishOrthography"],
                        self.pos["OEWsPalatalGlide"],
                        "the glide spelling needs ġ from OldEnglishOrthography")

    def test_sc017_still_in_nwgmc_corridor(self):
        self.assertEqual(self.block["PNWGmcULowering"], "EnglishProtoToOE")
        self.assertLess(self.pos["PNWGmcULowering"],
                        self.pos["PNWGmcFinalLongORaising"],
                        "SC017 < SC019 boundary (nose/shovel/sorrow)")

    def test_sc016_not_composed_inside_english_proto_to_oe(self):
        """The old inversion worked by composing SC016 at position 13 inside
        EnglishProtoToOE. That must never return."""
        text = FST.read_text(encoding="utf-8")
        stripped = re.sub(r"(?m)#.*$", "", text)
        proto = stripped[stripped.index("define EnglishProtoToOE"):]
        proto = proto[:proto.index("define OldEnglishRules")]
        self.assertNotIn("OEWsPalatalGlide", proto,
                         "SC016 has crept back into EnglishProtoToOE")

    def test_sandbox_mirrors_the_repair(self):
        text = re.sub(r"(?m)#.*$", "", SANDBOX.read_text(encoding="utf-8"))
        i_orth = re.search(r"define S\d+OldEnglishOrthography", text).start()
        i_glide = re.search(r"define S\d+OEWsPalatalGlide", text).start()
        self.assertLess(i_orth, i_glide,
                        "sandbox stage order must mirror germanic.txt")


class RegistryTests(unittest.TestCase):
    """Chronology metadata must record the adjudicated relation."""

    def test_partial_order_records_sc017_feeds_sc016(self):
        edges = {(r["earlier_sc"], r["later_sc"]): r
                 for r in _read_tsv(PARTIAL_ORDER)}
        self.assertIn(("SC017", "SC016"), edges,
                      "feeding edge SC017<SC016 missing")
        edge = edges[("SC017", "SC016")]
        self.assertEqual(edge["type_of_edge"], "historical_relative_chronology")
        self.assertNotIn(("SC016", "SC017"), edges,
                         "the retracted inverted edge has returned")
        self.assertNotEqual(edge["type_of_edge"], "technical_dependency")

    def test_audit_no_longer_claims_technical_dependency(self):
        rows = {r["sc_id"]: r for r in _read_tsv(AUDIT)}
        sc016 = rows["SC016"]
        self.assertEqual(sc016["entry_type"], "orthography_surface")
        self.assertEqual(sc016["technical_dependency"].strip(), "",
                         "SC016 must not carry a technical_dependency claim")
        self.assertNotIn("Do NOT move", "\t".join(sc016.values()))
        self.assertIn("SC017<SC016", sc016["relative_chronology_evidence"])

    def test_inventory_classifies_sc016_as_orthography_surface(self):
        rows = {r["change_id"]: r for r in _read_tsv(INVENTORY)}
        self.assertEqual(rows["SC016"]["entry_type"], "orthography_surface")

    def test_sc016_excluded_from_historical_rule_coverage_census(self):
        rows = {r["sc_id"]: r for r in _read_tsv(RULE_COVERAGE)}
        self.assertNotIn("SC016", rows,
                         "SC016 must not be counted among historical rule coverage totals")

    def test_adjudication_dossier_exists_and_governs(self):
        self.assertTrue(ADJUDICATION.exists(),
                        "governing adjudication dossier missing")
        text = ADJUDICATION.read_text(encoding="utf-8")
        for source in ("Fulk", "Campbell", "Brunner", "Hogg",
                       "Ringe", "Bülbring"):
            self.assertIn(source, text)


class BaselineDerivationTests(unittest.TestCase):
    """Lexical witnesses derive correctly under the repaired order."""

    @classmethod
    def setUpClass(cls):
        cls.out = {r["proto_norm"]: r for r in _read_tsv(BASELINE)}
        cls.compact = COMPACT.read_text(encoding="utf-8")

    @staticmethod
    def _lexeme_block(text, lexeme):
        start = text.index(f"# {lexeme}\n")
        tail = text[start + 1:]
        nxt = tail.find("\n# ")
        return text[start:] if nxt < 0 else text[start:start + 1 + nxt]

    def _match(self, proto_norm, expected):
        row = self.out[proto_norm]
        self.assertEqual(row["match"], "1", f"{proto_norm} does not match")
        self.assertEqual(row["outputs"], expected)

    def test_yoke_o_subcase(self):
        """*juką: SC017 lowers, SC016 spells the lowered o as eo."""
        self._match("júką", "ġeoc")
        block = self._lexeme_block(self.compact, "yoke")
        self.assertIn("PNWGmc U Lowering: *jóką", block)
        self.assertIn("### Orthography & surface", block)
        self.assertIn("Old English Orthography: ġ*ók", block)
        self.assertIn("OE Ws Palatal Glide: ġ*éok", block)
        self.assertNotIn("OE Ws Palatal Glide:", block.split("### Orthography & surface")[0],
                         "SC016 must not fire in the pre-surface derivation blocks")

    def test_youth_u_subcase(self):
        """*jugunþ-: following high vowel blocks SC017; SC016 spells the
        retained u as eo (Brunner §92.1a)."""
        self._match("júgunθ", "ġeoguþ")
        block = self._lexeme_block(self.compact, "youth")
        self.assertNotIn("PNWGmc U Lowering:", block,
                         "SC017 must not lower youth's root *u")
        self.assertIn("### Orthography & surface", block)
        self.assertIn("Old English Orthography: ġ*úguþ", block)
        self.assertIn("OE Ws Palatal Glide: ġ*éoguþ", block)
        self.assertNotIn("OE Ws Palatal Glide:", block.split("### Orthography & surface")[0],
                         "SC016 must not fire in the pre-surface derivation blocks")

    def test_sc017_positive_control_without_palatal(self):
        self._match("gúdą", "god")

    def test_sc017_positive_controls_before_sc019(self):
        self._match("núsō", "nosu")
        self._match("skúflō", "sċofl")
        self._match("súrgō", "sorg")


if __name__ == "__main__":
    unittest.main()
