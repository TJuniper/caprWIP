"""Secure invariants established by the SC001-SC020 chronology audit (2026).

Branch sc001-sc020-chronology-audit. These tests encode the audit's
*confirmed* determinations only. They deliberately assert the ABSENCE of
edges where chronology is unresolved, rather than inventing an ordering, and
they pin the corrected historical-stage metadata so the stale inventory labels
cannot silently regress.

Run: cd Germanic/tests && python3 -m unittest test_sc001_sc020_chronology_audit
"""

import csv
import io
import unittest
from pathlib import Path

SC_DIR = Path(__file__).resolve().parents[1] / "docs" / "sound_changes"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
PARTIAL_ORDER = SC_DIR / "cascade_baseline" / "historical_partial_order.tsv"


def _read(path):
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


class InventoryStageTests(unittest.TestCase):
    """The inventory must agree with the adjudicated staging map (the prior
    reconciliation left the inventory stale for SC003/SC012/SC016/SC020)."""

    @classmethod
    def setUpClass(cls):
        cls.inv = {r["change_id"]: r for r in _read(INVENTORY)}

    def test_sc003_rhotacism_is_west_germanic_not_pgmc(self):
        # R/T vol.2 §3.3.1 p.98; Hogg p.37; Crist2002 §6 (parallel WGmc/NGmc).
        self.assertEqual(self.inv["SC003"]["historical_stage"], "West Germanic")
        self.assertNotIn("Proto-Germanic", self.inv["SC003"]["historical_stage"])
        self.assertNotIn("Proto-Germanic", self.inv["SC003"]["display_name"])

    def test_sc020_final_z_is_west_germanic_not_pgmc(self):
        # Crist2002 §5; Campbell p.166; Hogg p.37; Kilday2024 place the loss in
        # West Germanic, not Proto-Germanic; Dossier B (2026 three-rule split,
        # sc020-three-rule-adjudication.md) fixes the stage more precisely as
        # Proto-West Germanic (R/T 2014 pp.44-45, 212).
        self.assertEqual(self.inv["SC020"]["historical_stage"], "Proto-West Germanic")
        self.assertNotEqual(self.inv["SC020"]["display_name"], "PGmc Final Z Deletion")
        self.assertIn("West Germanic", self.inv["SC020"]["display_name"])

    def test_sc012_lth_voicing_is_northern_wgmc(self):
        # R/T pp.170-171; Campbell §414: lþ>ld clearest in northern WGmc.
        self.assertEqual(self.inv["SC012"]["historical_stage"], "Northern West Germanic")

    def test_sc016_palatal_glide_is_old_english(self):
        # Campbell §§171-172; stage is OE/WS despite NWGmc cascade position.
        self.assertEqual(self.inv["SC016"]["historical_stage"], "Old English")

    def test_sc002_gm_simplification_is_pgmc(self):
        # Kroonen pp.511,101 (Verner DRV *tauma-/*drauma-); genuinely PGmc.
        self.assertEqual(self.inv["SC002"]["historical_stage"], "Proto-Germanic")

    def test_sc001_is_support_stage_not_sound_change(self):
        self.assertEqual(self.inv["SC001"]["entry_type"], "support_stage")
        self.assertEqual(self.inv["SC001"]["include_in_volume"], "no")


class PartialOrderAuditTests(unittest.TestCase):
    """Edge classifications confirmed by the audit."""

    @classmethod
    def setUpClass(cls):
        cls.edges = _read(PARTIAL_ORDER)

    def _edge(self, a, b):
        return next((e for e in self.edges
                     if e["earlier_sc"] == a and e["later_sc"] == b), None)

    def test_sc017_feeds_sc016_and_inverted_edge_is_retired(self):
        # sc016-017-adjudication.md: NWGmc u-lowering produced the *o of
        # geoc (Fulk §4.3 p.56; Campbell §115; Brunner §92.1), which the WS
        # glide spelling later rendered <eo>. The former SC016<SC017
        # "technical_dependency" was an artifact of the retired early
        # formulation and must not return.
        self.assertIsNone(self._edge("SC016", "SC017"),
                          "retracted SC016<SC017 edge has returned")
        e = self._edge("SC017", "SC016")
        self.assertIsNotNone(e, "feeding edge SC017<SC016 must exist")
        self.assertEqual(e["type_of_edge"], "historical_relative_chronology")
        self.assertEqual(e["confidence"], "A")

    def test_sc020_sc003_zdeletion_before_rhotacism(self):
        # Crist: rhotacism follows WGmc *z-deletion; implemented via scoping.
        e = self._edge("SC020", "SC003")
        self.assertIsNotNone(e, "SC020<SC003 edge must exist")
        self.assertEqual(e["type_of_edge"], "historical_relative_chronology")

    def test_sc019_sc020_raising_before_zloss(self):
        # *rástōz > ræste: final long-ō raising precedes final-*z* loss.
        e = self._edge("SC019", "SC020")
        self.assertIsNotNone(e)
        self.assertEqual(e["confidence"], "A")

    def test_sc010_sc011_gemination_before_syllabic_j(self):
        # OE nett: *natją > *nattją; gemination precedes syllabic-j.
        e = self._edge("SC010", "SC011")
        self.assertIsNotNone(e)
        self.assertEqual(e["type_of_edge"], "historical_relative_chronology")
        self.assertEqual(e["confidence"], "A")

    def test_sc018_has_no_forced_ordering(self):
        # SC018 evidence is thin (B); the audit must NOT invent an ordering.
        # Assert no historical edge forces SC018 relative to SC015 or SC019.
        forced = [e for e in self.edges
                  if e["type_of_edge"] == "historical_relative_chronology"
                  and {e["earlier_sc"], e["later_sc"]} == {"SC018", "SC015"}
                  or {e["earlier_sc"], e["later_sc"]} == {"SC018", "SC019"}
                  and e["type_of_edge"] == "historical_relative_chronology"]
        self.assertEqual(forced, [],
                         "SC018 chronology is unresolved; no edge should force it")


if __name__ == "__main__":
    unittest.main()
