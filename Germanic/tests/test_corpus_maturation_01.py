"""Corpus-maturation pass 01: WHO and YOU regression coverage.

Locks the historically motivated content of the 2026 corpus-maturation pass
(docs/sound_changes/audits/corpus-maturation-01-candidate-adjudication.md):

  * WHO (OE hwā < *xwáz) — real corpus witness for SC097
    MonosyllabicFinalZLoss; requires the narrowed long-final clause of
    Anglo-Frisian brightening (Campbell §125: *hwǣ does not exist).
  * YOU (OE ēow < *ízwiz) — real corpus witness for SC008
    PWGmcCoronalWAssimilation (the *zw branch), SC098
    PWGmcUnstressedWordFinalIApocope (R&T 2014: 57-58), and the
    chronology SC008 → SC003, SC020 → SC098 → SC055, SC033 → SC031.

Every assertion here is a chronology or witness regression: reversing the
relevant rule orders, or reverting the rule bodies, must fail this file.
"""

import csv
import io
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
TSV = GERMANIC / "data" / "germanic-aligned-final.tsv"
BASE_DIR = GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
OUTPUTS = BASE_DIR / "cascade_baseline_outputs.tsv"
LEGACY = BASE_DIR / "cascade_baseline_outputs_legacy380.tsv"
MANIFEST = BASE_DIR / "cascade_order_manifest.tsv"
PARTIAL_ORDER = BASE_DIR / "historical_partial_order.tsv"


def _read_tsv(path):
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


class CorpusRowTests(unittest.TestCase):
    """The who/you concepts are present with the adjudicated reconstructions."""

    @classmethod
    def setUpClass(cls):
        cls.rows = _read_tsv(TSV)

    def _concept(self, concept):
        return [r for r in self.rows if r["CONCEPT"] == concept]

    def test_who_rows(self):
        rows = self._concept("who")
        self.assertEqual(len(rows), 4)
        self.assertEqual({r["PROTO"] for r in rows}, {"*xwáz"})
        oe = [r for r in rows if r["DOCULECT"] == "Old_English"]
        self.assertEqual(len(oe), 1)
        self.assertEqual(oe[0]["COUNTERPART"], "hwā")
        self.assertEqual(oe[0]["DERIVATION_CLASS"], "regular")

    def test_you_rows(self):
        rows = self._concept("you")
        self.assertEqual(len(rows), 4)
        self.assertEqual({r["PROTO"] for r in rows}, {"*ízwiz"})
        oe = [r for r in rows if r["DOCULECT"] == "Old_English"]
        self.assertEqual(len(oe), 1)
        self.assertEqual(oe[0]["COUNTERPART"], "ēow")
        self.assertEqual(oe[0]["DERIVATION_CLASS"], "regular")


class BaselineWitnessTests(unittest.TestCase):
    """The committed cascade baseline derives both witnesses exactly."""

    @classmethod
    def setUpClass(cls):
        cls.out = {(r["proto_norm"], r["counterpart"]): r
                   for r in _read_tsv(OUTPUTS)}

    def test_who_derives_hwa(self):
        row = self.out[("xwáz", "hwā")]
        self.assertEqual(row["match"], "1")
        self.assertEqual(row["outputs"], "hwā")

    def test_you_derives_eow(self):
        row = self.out[("ízwiz", "ēow")]
        self.assertEqual(row["match"], "1")
        self.assertEqual(row["outputs"], "ēow")

    def test_new_rows_are_not_in_legacy_subset(self):
        legacy = {(r["proto_norm"], r["counterpart"]) for r in _read_tsv(LEGACY)}
        self.assertNotIn(("xwáz", "hwā"), legacy)
        self.assertNotIn(("ízwiz", "ēow"), legacy)
        self.assertEqual(len(legacy), 380)


class RuleBodyTests(unittest.TestCase):
    """The source-backed rule bodies of the pass must not silently revert."""

    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")

    def _define(self, name):
        m = re.search(r"define\s+" + name + r"\s*(?:Ctx\()?\[(.*?)\]\)?;", self.text, re.S)
        self.assertIsNotNone(m, f"define {name} not found")
        # Strip whole-line comments only; ".#." must survive.
        return re.sub(r"(?m)^\s*#.*$", "", m.group(1))

    def test_sc098_body(self):
        body = re.sub(r"\s+", " ", self._define(
            "PWGmcUnstressedWordFinalIApocope")).strip()
        self.assertIn("[{*i}|{*u}] -> 0", body)
        self.assertIn(".#. {*ᵘ}", body)
        self.assertIn("EnglishStarLongVowel | EnglishStarLongDiphthong", body)
        self.assertIn("EnglishStarShortVowel EnglishStarConsonant EnglishStarConsonant+", body)
        self.assertNotIn("{*w} {*w} _", body)

    def test_brightening_long_final_is_narrowed(self):
        """Campbell §125 p.49: *hwǣ does not exist. The long-final clause
        must require a preceding nucleus, or *xwā would front to *xwǣ."""
        body = re.sub(r"\s+", " ", self._define("EAFBrighteningLongFinal"))
        self.assertIn("EnglishStarVocalic", body.split("||", 1)[1])
        self.assertNotRegex(
            body, r"\|\|\s*_\s*\.#\.",
            "long-final brightening reverted to the unguarded environment")

    def test_ew_long_context_admits_final_geminate(self):
        body = self._define("OEEwLongContext")
        self.assertRegex(body, r"\{\*w\}\s*\.#\.",
                         "OEEwLongContext lost the word-final geminate "
                         "alternative required for *iww > ēow")


class CompositionOrderTests(unittest.TestCase):
    """Executable order = adjudicated historical chronology."""

    @classmethod
    def setUpClass(cls):
        rows = _read_tsv(MANIFEST)
        cls.pos = {r["foma_identifier"]: int(r["position"]) for r in rows}

    def _before(self, a, b, why):
        self.assertLess(self.pos[a], self.pos[b], why)

    def test_sc020_feeds_sc098(self):
        self._before("EAFFinalZDeletion", "PWGmcUnstressedWordFinalIApocope",
                     "z-loss makes the *-i of *iwwiz word-final (R&T 41-42)")

    def test_sc098_before_sc097(self):
        self._before("PWGmcUnstressedWordFinalIApocope",
                     "MonosyllabicFinalZLoss",
                     "SC098 is PWGmc; SC097 is post-PWGmc northern")

    def test_sc008_before_rhotacism(self):
        self._before("PWGmcCoronalWAssimilation", "EAFRhotacism",
                     "*izwiz must assimilate before rhotacism or *irwiz "
                     "results and ēow is underivable")

    def test_sc097_before_rhotacism(self):
        self._before("MonosyllabicFinalZLoss", "EAFRhotacism",
                     "*hwaz must lose *-z before rhotacism or *hwar results")

    def test_sc098_bleeds_i_umlaut(self):
        self._before("PWGmcUnstressedWordFinalIApocope", "OEIUmlaut",
                     "ēow shows no umlaut: the trigger fell first (R&T 57-58)")

    def test_early_reanalysis_and_late_j_residual_are_separate(self):
        self._before("PWGmcCoronalWAssimilation", "OEWWSimplification",
                     "coronal assimilation feeds the adopted early reanalysis")
        self._before("OEWWSimplification", "OEEwLongDiphthong",
                     "early reanalysis is distinct from English long realization")
        self._before("OEEwLongDiphthong", "OEJWWSimplification",
                     "the disclosed j-created residual retains its late slot")

    def test_archived_partial_order_edges_recorded(self):
        edges = {(r["earlier_sc"], r["later_sc"])
                 for r in _read_tsv(PARTIAL_ORDER)}
        for edge in [("SC008", "SC003"), ("SC020", "SC098"),
                     ("SC098", "SC055"), ("SC033", "SC031")]:
            self.assertIn(edge, edges,
                          f"historical edge {edge} missing from "
                          "historical_partial_order.tsv")


if __name__ == "__main__":
    unittest.main()
