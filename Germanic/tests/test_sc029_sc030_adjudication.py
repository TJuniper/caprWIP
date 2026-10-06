#!/usr/bin/env python3
"""Regression for the joint SC029/SC030 adjudication (2026).

Governing memo:
Germanic/docs/sound_changes/audits/sc029-sc030-awj-resolution-and-au-fronting-adjudication.md

Protected scientific conclusions:

  * SC029 is NOT "glide formation". It is the reversal of the West Germanic
    gemination of *w before *j, restoring the diphthong: PNWGmc *awj >
    PWGmc *[aw'w'] > pre-OE *[auj] (Ringe and Taylor p. 53 §3.1.3, "it was
    reversible"; Campbell §120.2 p. 46, "auj > auuj > auj").
  * The retained handbook analysis describes SC030 as brightening applied
    to the first element of the diphthong *au
    (Campbell §132 p. 52 lists "West Gmc. a > OE ae; West Gmc. au > OE aeu"
    as one and the same ordered step; Fulk §4.12 p. 73, "This fronting of a
    applied also to the diphthong au in OE").
  * SC030's retained executable scope is English. Its historical identity
    relative to SC043 remains unresolved pending the full English/Frisian
    chronology; different surface outcomes alone do not establish independence.
  * They are TWO changes and SC029 feeds SC030: "These new *au also
    underwent the development to ea" (Ringe and Taylor p. 173).
  * SC030's historical identity comes from INHERITED *au, which supplies 16
    of its 18 live firings. `hay` and `strew` are 2 further inputs and must
    never be treated as defining the rule.
  * The old registry claim that SC029/SC030 are "post-AF-brightening"
    developments placed too early is RETRACTED. The executable domains of
    SC030 and SC043 are disjoint, so that interaction does not require a
    reorder; disjointness does not establish their historical contemporaneity.
  * Verdict RETAIN for both: no rule change, no move, no output change.

The complete firing populations are deliberately NOT frozen here; they come
from the generated census. Only the scientifically load-bearing witnesses and
the rule identities are protected.

Run: cd Germanic/tests && python3 -m unittest test_sc029_sc030_adjudication
"""
from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
SC_DIR = GERMANIC / "docs" / "sound_changes"
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
BASELINE = SC_DIR / "cascade_baseline" / "cascade_baseline_outputs.tsv"
MEMO = SC_DIR / "audits" / "sc029-sc030-awj-resolution-and-au-fronting-adjudication.md"
READER = SC_DIR / "reader_facing" / "029-030-awj-glide-and-au-fronting.md"
DOSSIER = (SC_DIR / "book_dossiers"
           / "028-030-glide-and-fronting-entry.book-dossier.md")

# The two words whose *au is created by SC029.
SECONDARY_AU = {"hay": "hīeġ", "strew": "strīeġan"}

# Inherited *au. These are the historical core of SC030 and must keep working
# whatever happens to the awj material. A representative subset of the 16.
INHERITED_AU = {
    "believe": "ġelīefan",
    "bread": "brēad",
    "dream": "drēam",
    "leaf": "lēaf",
    "stream": "strēam",
    "leek": "lēac",
    "seam": "sēam",
}


def _tsv_rows(path: Path):
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()
             if not line.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


class Sc029Sc030AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        cls.registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        cls.edges = _tsv_rows(EDGES)
        cls.positions = {r["foma_identifier"]: int(r["position"])
                         for r in _tsv_rows(MANIFEST)}
        cls.baseline = {r["concept"]: r for r in _tsv_rows(BASELINE)}
        cls.memo = MEMO.read_text(encoding="utf-8")
        # Prose is hard-wrapped and partly block-quoted, so match against a
        # copy with quote markers and line breaks flattened away.
        flat = re.sub(r"(?m)^\s*>\s?", "", cls.memo.replace("`", ""))
        cls.memo_flat = " ".join(flat.split())
        cls.reader = READER.read_text(encoding="utf-8")

    def define_body(self, name: str) -> str:
        match = re.search(
            r"define\s+" + re.escape(name) + r"\s*\[(.*?)\n\];",
            self.uncommented, re.S)
        self.assertIsNotNone(match, f"missing define {name}")
        return match.group(1)

    def edge(self, source: str, target: str):
        for e in self.edges:
            if e["source_change_id"] == source and e["target_change_id"] == target:
                return e
        self.fail(f"no chronology edge {source} -> {target}")

    # ------------------------------------------------------------------
    # Rule identity
    # ------------------------------------------------------------------

    def test_sc029_resolves_awj_to_a_diphthong_plus_surviving_j(self):
        """SC029 must turn *aw(w)j into a diphthong with *j still present.

        Campbell §120.2 p. 46 and Ringe and Taylor p. 53 §3.1.3 both require
        the *j to survive into the Old English developments; it is what later
        causes i-umlaut in hīeġ and strīeġan.
        """
        body = self.define_body("OEAwwjResolution")
        self.assertIn("{*á} {*w} {*w} {*j}", body,
                      "SC029 must cover the stressed geminate input, which "
                      "SC010 now supplies for both hay and strew")
        self.assertIn("{*áu} {*j}", body,
                      "the output must be a diphthong FOLLOWED BY surviving *j")
        self.assertNotIn("{*áu} {*w}", body,
                         "SC029 must not leave a consonantal *w behind")

    def test_sc030_fronts_the_first_element_of_the_diphthong(self):
        """SC030 is brightening of the first element, so *au -> *aeu only."""
        body = self.define_body("OEAuBrightening")
        self.assertIn("{*au} -> {*aeu}", body)
        self.assertIn("{*áu} -> {*áeu}", body)
        self.assertNotIn("{*ēa}", body,
                         "SC030 must stop at the *aeu stage that Ringe and "
                         "Taylor p. 172 reconstruct; the offglide lowering "
                         "belongs to SC032")

    def test_sc032_consumes_the_aeu_that_sc030_creates(self):
        """The feeding relation must remain visible in the rule text."""
        body = self.define_body("OEDiphthongLeveling")
        self.assertIn("{*aeu} -> {*ēa}", body)
        self.assertIn("{*áeu} -> {*ēa}", body)

    # ------------------------------------------------------------------
    # The disjointness that makes the placement free
    # ------------------------------------------------------------------

    def test_brightening_cannot_reach_inside_the_au_digraph(self):
        """SC043 and SC030 are provably non-interacting.

        EAFBrightening targets only the plain low-vowel digraphs, and every
        member of EnglishStarConsonant begins with '*', so no clause can find
        its context inside `{*áu}`, where the segment after `*á` is a bare
        `u`. This establishes executable non-interaction, not historical
        contemporaneity or common-stem identity (memo §7.1).
        """
        for clause in ("EAFBrighteningUnstressed", "EAFBrighteningStressed",
                       "EAFBrighteningLongFinal"):
            body = self.define_body(clause)
            self.assertNotIn("{*au}", body)
            self.assertNotIn("{*áu}", body)
        match = re.search(r"define\s+PGmcStarConsonant\s*\[(.*?)\];",
                          self.uncommented, re.S)
        self.assertIsNotNone(match, "missing define PGmcStarConsonant")
        members = re.findall(r"\{([^}]*)\}", match.group(1))
        self.assertTrue(members, "PGmcStarConsonant should be a set of digraphs")
        for member in members:
            self.assertTrue(
                member.startswith("*"),
                f"consonant class member {member!r} does not begin with '*'; "
                "the disjointness argument for SC030 against SC043 depends on "
                "every consonant context being star-initial")

    # ------------------------------------------------------------------
    # Executable order, by rule identity and never by absolute position
    # ------------------------------------------------------------------

    def test_sc029_feeds_sc030_feeds_sc032(self):
        self.assertLess(self.positions["OEAwwjResolution"],
                        self.positions["OEAuBrightening"],
                        "the diphthong must exist before it can be fronted")
        self.assertLess(self.positions["OEAuBrightening"],
                        self.positions["OEDiphthongLeveling"],
                        "Ringe and Taylor p. 172: fronted to *aeu FIRST, "
                        "offglide unrounded and lowered LATER")

    def test_the_pair_still_follows_ai_monophthongization(self):
        """Campbell §132 p. 52 orders ai > a (step 2) before au > aeu (step 3)."""
        self.assertLess(self.positions["EAFAiMonophthongization"],
                        self.positions["OEAwwjResolution"])

    # ------------------------------------------------------------------
    # Corpus witnesses
    # ------------------------------------------------------------------

    def test_secondary_au_witnesses_still_surface(self):
        for concept, expected in SECONDARY_AU.items():
            row = self.baseline[concept]
            self.assertEqual(row["outputs"], expected,
                             f"{concept} must still yield {expected}")

    def test_inherited_au_witnesses_still_surface(self):
        """SC030's historical core. These outrank hay and strew 16 to 2."""
        for concept, expected in INHERITED_AU.items():
            row = self.baseline[concept]
            self.assertEqual(row["outputs"], expected,
                             f"{concept} must still yield {expected}")

    def test_inherited_au_is_not_derived_from_awj(self):
        """Negative control: the inherited-*au words have no *w before *j.

        If any of them did, they would be witnesses of SC029 as well, and the
        claim that SC030 has an independent population would collapse.
        """
        for concept in INHERITED_AU:
            proto = self.baseline[concept]["proto"]
            self.assertNotIn("wj", proto,
                             f"{concept} must test SC030 independently of SC029")
            self.assertIn("áu", proto,
                          f"{concept} must carry inherited *au")

    # ------------------------------------------------------------------
    # Registry metadata
    # ------------------------------------------------------------------

    def test_both_are_adjudicated_with_a_retain_verdict(self):
        for sc_id in ("SC029", "SC030"):
            row = self.registry[sc_id]
            self.assertEqual(row["adjudication_status"], "adjudicated")
            self.assertEqual(row["verdict"], "RETAIN",
                             f"{sc_id}: the rules were correct; the "
                             "descriptions around them were not")
            self.assertTrue((REPO_ROOT / row["adjudication_memo"]).is_file())
            self.assertEqual(row["hist_stage"], "preoe")
            self.assertEqual(row["hist_scope"], "english_specific")

    def test_confidence_is_dimension_specific(self):
        """SC029 stays B for the camp dispute; SC030 rises to A."""
        self.assertEqual(
            self.registry["SC029"]["confidence"], "B",
            "SC029 stays B because Fulk §4.10 n. 1 denies that *w ever "
            "geminated before *j, so whether a discrete change occurred is "
            "unresolved even though *auj as the pre-OE input is secure")
        self.assertEqual(
            self.registry["SC030"]["confidence"], "A",
            "SC030 rises to A: existence, domain, stage and scope are each "
            "secured by Campbell §132 p. 52, Fulk §4.12 p. 73 and Ringe and "
            "Taylor p. 172, plus 16 inherited-*au witnesses")

    def test_display_names_no_longer_say_glide_formation(self):
        for field in ("display_name", "inventory_display_name"):
            self.assertNotIn("Glide Formation",
                             self.registry["SC029"][field],
                             "SC029 is the reversal of a gemination, and its "
                             "effect is to make the glide vocalic")
            self.assertNotIn("glide formation",
                             self.registry["SC029"][field].lower())
        self.assertIn("brightening",
                      self.registry["SC030"]["display_name"].lower(),
                      "SC030 must be identified as brightening (Fulk §4.12)")

    def test_the_post_brightening_placement_claim_is_retracted(self):
        for sc_id in ("SC029", "SC030"):
            problem = self.registry[sc_id]["chronology_problem"]
            if sc_id == "SC029":
                self.assertIn("RETRACTED", problem)
                self.assertIn("supersedes the former universal commutation", problem)
            else:
                self.assertIn("superseded by the SC043 component decision", problem)
                self.assertIn("not universal commutation or simultaneity",
                              self.registry[sc_id]["staging_notes"])
            self.assertNotIn(
                "historically they are post-AF-brightening", problem,
                f"{sc_id}: SC030 IS brightening, so it cannot be later than it")
            self.assertNotEqual(
                self.registry[sc_id]["action_status"],
                "possible_fst_reorder_later",
                f"{sc_id}: the adopted account retains production serialization")

    # ------------------------------------------------------------------
    # Chronology edges
    # ------------------------------------------------------------------

    def test_sc029_sc030_is_recorded_as_feeding(self):
        for source, target in (("SC029", "SC030"), ("SC030", "SC029")):
            e = self.edge(source, target)
            self.assertEqual(e["witness_role"], "feeding")
            self.assertIn("hay", e["representative_lexemes"])
            self.assertIn("strew", e["representative_lexemes"])

    def test_sc030_sc032_no_output_set_is_not_promoted_to_history(self):
        """The 18 no-output rows must be classified honestly.

        They show that *aeu is a non-surface intermediate. The historical
        interval comes from Ringe and Taylor p. 172, not from the probe.
        """
        for source, target in (("SC030", "SC032"), ("SC032", "SC030")):
            e = self.edge(source, target)
            self.assertEqual(e["witness_role"], "feeding")
            notes = e["notes"]
            flat = " ".join(notes.split())
            self.assertIn("non-surface intermediate", flat)
            self.assertIn("172", flat,
                          "the notes must cite Ringe and Taylor p. 172 as the "
                          "actual source of the historical direction")
            self.assertIn("NOT", flat,
                          "the notes must warn against reading the no-output "
                          "set as historical evidence")

    # ------------------------------------------------------------------
    # Memo and prose
    # ------------------------------------------------------------------

    def test_memo_records_the_two_identifications(self):
        for needle in (
            "reversal of the West Germanic",
            "it was reversible",
            "handbook interpretation used in this adjudication",
            "brightening applied to the first element",
            "These new *au also underwent",
            "no such fronting in the development of au in OFris",
            "provably non-interacting",
        ):
            self.assertIn(needle, self.memo_flat,
                          f"memo must record: {needle!r}")

    def test_memo_defers_the_comparative_identity_without_merging_rules(self):
        self.assertIn(
            "identity of SC030 and SC043 remains unresolved pending the full "
            "English/Frisian relative chronology",
            self.memo_flat)
        self.assertIn("The registry therefore keeps two rows", self.memo_flat)

    def test_memo_keeps_the_inherited_au_population_central(self):
        self.assertIn("sixteen of the eighteen witnesses", self.memo_flat)
        self.assertIn("may be read off hay and strew", self.memo_flat,
                      "the memo must say plainly that SC030's identity does "
                      "not come from the two SC029 words")

    def test_memo_records_the_deferred_items(self):
        for needle in ("rename", "xáwwją", "Hogg1992", "OEAwwjResolution",
                       "OEAuBrightening", "HoggGrammar1992"):
            self.assertIn(needle, self.memo_flat,
                          f"memo must record deferred item: {needle!r}")

    def test_reader_chapter_cites_printed_ringe_taylor_pages(self):
        """p. 188 was the PDF sheet for printed p. 173."""
        self.assertNotIn("@RingeTaylor2014, p. 188", self.reader,
                         "CAPR cites Ringe and Taylor by printed page")
        for locator in ("p. 53", "p. 172", "p. 173"):
            self.assertIn(f"@RingeTaylor2014, {locator}", self.reader)

    def test_reader_chapter_presents_inherited_au(self):
        for form in ("lēaf", "strēam", "brēad", "drēam"):
            self.assertIn(form, self.reader,
                          "the chapter must show that SC030 is the general "
                          "*au change, not a rule about hay and strew")
        self.assertIn("Old Frisian", self.reader,
                      "the English-only scope needs its comparative evidence")

    def test_dossier_banner_points_at_the_new_adjudication(self):
        dossier = DOSSIER.read_text(encoding="utf-8")
        self.assertIn("sc029-sc030-awj-resolution-and-au-fronting-adjudication.md",
                      dossier)
        self.assertNotIn(
            "The SC029 and SC030 material in this dossier is not affected",
            dossier)


if __name__ == "__main__":
    unittest.main()
