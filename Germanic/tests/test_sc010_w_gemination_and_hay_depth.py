#!/usr/bin/env python3
"""Regression for the SC010 *w-gemination repair and hay's reconstruction depth.

Governing memo:
Germanic/docs/sound_changes/audits/sc010-w-gemination-and-hay-depth-adjudication.md

Protected scientific conclusions:

  * CAPR implements the Ringe-Taylor/Campbell architecture, not Fulk's.
    PGmc singleton *wj geminates to *wwj by the ordinary West Germanic
    gemination law, and pre-OE then resolves *awwj to *auj.
    Campbell §407 p. 167: "every consonant except r being affected after
    short syllables... The forms in which w is doubled are dealt with in
    §120.2."  Ringe and Taylor p. 53: "it appears that that cluster too
    underwent gemination in PWGmc."
  * hay's selected Proto-Germanic input must carry a SINGLETON *w. The old
    *xáwwją encoded a West Germanic geminate in a Proto-Germanic slot, which
    no source reconstructs: R&T p. 53 give *hawja, Campbell §120.2 p. 46
    gives *hawja-, and Kroonen p. 215 gives *hauja-.
  * The general invariant: a selected Proto-Germanic input must not
    pre-encode a West Germanic change that the cascade itself models.
  * SC010 supplies the geminate, SC029 resolves it, SC030 fronts the result.
    The reconstructed intermediate is exposed, not telescoped away.
  * SC029's singleton branches were an artifact of hay's bad protoform and
    are gone. The surviving pair are stress-notation variants.
  * The *w branch is not a hay-specific exception: it uses the same
    environment as the other thirteen members, and genuine non-members must
    stay out of its domain.

Firing populations and absolute rule positions are deliberately NOT frozen
here; they come from the generated census. Only rule identity, the corpus
invariant, and the derivational chain are protected.

Run: cd Germanic/tests && python3 -m unittest test_sc010_w_gemination_and_hay_depth
"""
from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
CORPUS = GERMANIC / "data" / "germanic-aligned-final.tsv"
SC_DIR = GERMANIC / "docs" / "sound_changes"
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
MEMO = SC_DIR / "audits" / "sc010-w-gemination-and-hay-depth-adjudication.md"
TRACE = GERMANIC / "docs" / "debug_snapshots" / "oe_full_trace_report.txt"

GEMINATION_ENV = "|| EnglishStarShortVowel _ {*j}"

# Words whose *au is created by the gemination-plus-resolution chain.
AWJ_WITNESSES = {"hay": "hīeġ", "strew": "strīeġan"}

# The *iwj witness: geminates at SC010 like the *awj words, but the later
# resolution is restricted to the low-vowel type, so it must not fire here.
IWJ_WITNESS = ("hue", "*xíwją", "hīew")

# Structural non-members of the *w branch. These are engineering near-misses,
# NOT independent demonstrations of the short-syllable conditioning: in every
# case the *w simply is not immediately before a *j. Each entry carries the
# reason it cannot geminate. Every form here is a SELECTED protoform and must
# be present in the trace; a typo or a deleted row has to fail the test rather
# than skip it.
NEGATIVE_CONTROLS = {
    "*knéwai": "selected knee dative: short *é plus *w but no following *j (contrast with hue)",
    "*lḗwijaną": "*wij, not *wj: after a heavy syllable Sievers' law gives *-ij-",
    "*smérwijaną": "*wij, not *wj, for the same reason",
    "*skáwōjaną": "*w stands before *ō, not before *j",
    "*wéljaną": "word-initial *w; it is the *l that geminates before *j",
    "*wéljô": "word-initial *w; it is the *l that geminates before *j",
    "*kéwwaną": "geminate already in Proto-Germanic by Verschärfung, and no *j",
    "*xáwwaną": "geminate already in Proto-Germanic by Verschärfung, and no *j",
    "*dáwwō": "geminate already in Proto-Germanic by Verschärfung, and no *j",
    "*snáiwaz": "*w follows a diphthong and no *j follows",
    "*sáiwiz": "*w follows a diphthong and no *j follows",
}

# A short vowel, optionally accented, immediately before *wj.
SHORT_VOWEL_WJ = re.compile(r"[aeiouáéíóúäëïöüàèìòù]wj")


def _tsv_rows(path: Path):
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()
             if not line.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


class WGeminationRepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        cls.registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        cls.edges = _tsv_rows(EDGES)
        cls.corpus = _tsv_rows(CORPUS)
        cls.memo = MEMO.read_text(encoding="utf-8")
        flat = re.sub(r"(?m)^\s*>\s?", "", cls.memo.replace("`", ""))
        cls.memo_flat = " ".join(flat.split())
        cls.trace = TRACE.read_text(encoding="utf-8")
        cls.sc010_output_shape = cls._compile_sc010_output_shape()

    @classmethod
    def _compile_sc010_output_shape(cls) -> re.Pattern:
        """Build the 'SC010 has already applied' pattern out of SC010 itself.

        The invariant has to track the rule, not a hand-copied snapshot of
        it. This reads the gemination law's own segment inventory and its own
        short-vowel environment out of germanic.txt and assembles the shape
        the rule emits: a short vowel, a doubled member of the law, *j. If
        the law's membership changes, the corpus invariant changes with it.

        A selected protoform is a plain string, so a diphthong is simply two
        vowel letters running together and its second half looks like a short
        vowel. SC010's environment is a single short-vowel symbol, so the
        match is barred from starting inside a diphthong or after a long
        vowel.
        """
        def define(name: str) -> str:
            found = re.search(r"define\s+%s\s*(?:Ctx\()?\[(.*?)\]\)?;" % name,
                              cls.uncommented, re.DOTALL)
            assert found, f"{name} not found in germanic.txt"
            return found.group(1)

        members = sorted(set(re.findall(
            r"\{\*(.)\}\s*->\s*\{\*\1\}\s*\{\*\1\}\s*\|\|",
            define("PWGmcJGemination"))))
        assert "w" in members, "SC010 must carry the *w branch"
        short = sorted(set(re.findall(r"\{\*(.)\}", define("EnglishStarShortVowel"))))
        preceding = sorted(set("".join(
            re.findall(r"\{\*([^}]+)\}",
                       define("EnglishStarLongVowel") + define("EnglishStarDiphthong"))
        )) | set(short))
        return re.compile("(?<![%s])[%s](%s)\\1j"
                          % ("".join(preceding), "".join(short), "|".join(members)))

    def define_body(self, identifier: str) -> str:
        match = re.search(r"define\s+%s\s*(?:Ctx\()?\[(.*?)\]\)?;" % re.escape(identifier),
                          self.uncommented, re.DOTALL)
        self.assertIsNotNone(match, f"rule {identifier} not found in germanic.txt")
        body = match.group(1).strip()
        if "Ctx(" in match.group(0) and body.startswith("[") and body.endswith("]"):
            body = body[1:-1]
        return body

    def protoforms(self, concept: str) -> set[str]:
        forms = {r["PROTOFORM"] for r in self.corpus if r["CONCEPT"] == concept}
        self.assertTrue(forms, f"concept {concept!r} missing from the corpus")
        return forms

    def derivation(self, protoform: str) -> str:
        """The trace block for one selected protoform."""
        start = self.trace.find(f"PROTO: {protoform}\n")
        self.assertNotEqual(start, -1,
                            f"no trace block for {protoform!r}; refresh the control plane")
        end = self.trace.find("\n--- ", start)
        return self.trace[start:end if end != -1 else len(self.trace)]

    # ------------------------------------------------------------------
    # Corpus reconstruction depth
    # ------------------------------------------------------------------

    def test_hay_enters_with_a_singleton_w(self):
        """hay's PGmc input must not pre-encode the West Germanic geminate.

        R&T p. 53 give PGmc *hawja, Campbell §120.2 p. 46 *hawja-, Kroonen
        p. 215 *hauja-. None reconstructs a Proto-Germanic *hawwja-.
        """
        for form in self.protoforms("hay"):
            self.assertNotIn("ww", form,
                             "hay must not carry a West Germanic geminate in a "
                             "Proto-Germanic slot; the cascade models that "
                             "gemination at SC010")
            self.assertIn("áwj", form,
                          "hay's PGmc input must show singleton *w before *j")

    def test_strew_keeps_its_source_correct_singleton_input(self):
        """strew was already right and must stay right (R&T p. 53 *strawjaną)."""
        for form in self.protoforms("strew"):
            self.assertIn("áwj", form)
            self.assertNotIn("ww", form)

    def test_no_selected_protoform_pre_encodes_wgmc_j_gemination(self):
        """The governing invariant, applied to the whole corpus.

        A selected Proto-Germanic input must not carry a geminate that the
        cascade itself derives at SC010 from the source-supported singleton.
        This is what went wrong with hay.

        The invariant is deliberately narrow, and is read off SC010 itself
        rather than written out here: it rejects only the exact shape SC010
        produces, namely a short vowel followed by a doubled member of the
        gemination law followed by *j. Any other pre-*j geminate is outside
        SC010's domain and is therefore a legitimate Proto-Germanic
        reconstruction, not a reconstruction-depth error. A geminate after a
        long vowel or a diphthong, or a geminate of a segment the law exempts
        (*r, *z), must pass: the cascade does not create it, so carrying it
        into a Proto-Germanic slot encodes nothing that CAPR models. If a
        source reconstructs such a form, this test must not stand in its way.
        """
        offenders = sorted({
            (r["CONCEPT"], r["PROTOFORM"]) for r in self.corpus
            if self.sc010_output_shape.search(r["PROTOFORM"])
        })
        self.assertEqual(offenders, [],
                         "these protoforms pre-encode the very geminate SC010 "
                         "derives from a singleton in this environment")

    def test_the_invariant_is_scoped_to_what_sc010_actually_derives(self):
        """Guard the guard: the invariant must not over-reject.

        The first version of this check rejected any doubled character before
        *j anywhere in a protoform. That would have failed a future
        source-supported Proto-Germanic inherited geminate for no better
        reason than that it resembles SC010's output. These probe forms are
        not corpus rows; they exist to pin the boundary of the rule.
        """
        rejected = "*xáwwją"        # short vowel + geminated *w + *j: SC010's own output
        self.assertRegex(rejected, self.sc010_output_shape,
                         "the invariant must still catch hay's old protoform")
        for allowed, why in {
            "*xāwwją": "geminate after a long vowel: outside SC010's environment",
            "*xáuwwją": "geminate after a diphthong: outside SC010's environment",
            "*xárrją": "*r is exempt from the gemination law (R&T p. 52)",
            "*xázzją": "*z is exempt from the gemination law (R&T p. 52)",
            "*xáwwaną": "geminate not before *j",
        }.items():
            with self.subTest(form=allowed):
                self.assertNotRegex(allowed, self.sc010_output_shape, why)

    def test_corpus_carries_an_iwj_witness(self):
        """The *w branch must be witnessed outside the words SC029 consumes.

        Campbell §120.2 p. 46 states both halves of the type: "auj > auuj >
        auj, and iuj > iuuj > iuj", then "the u of auuj is lost, so that the
        final result is ēg or ieg, but the j of iuuj is lost, so that the
        result is iow or iew". Before hue was added, every witness of the *w
        gemination also underwent the later resolution, so the corpus could
        not tell the two changes apart.
        """
        concept, form, _ = IWJ_WITNESS
        self.assertIn(form, self.protoforms(concept),
                      f"{concept} must enter as {form}")
        self.assertNotIn("ww", form,
                         "the *iwj witness must enter with a singleton *w too")

    # ------------------------------------------------------------------
    # Rule identity
    # ------------------------------------------------------------------

    def test_sc010_geminates_w_before_j(self):
        """Campbell §407 p. 167 makes *w an ordinary member of the law."""
        body = self.define_body("PWGmcJGemination")
        self.assertIn("{*w} -> {*w} {*w} " + GEMINATION_ENV, body,
                      "SC010 must supply the *wwj geminate that SC029 resolves")

    def test_the_w_branch_is_not_a_special_case(self):
        """It must use the same environment as every other member."""
        body = self.define_body("PWGmcJGemination")
        clauses = [c.strip() for c in body.split(",") if c.strip()]
        self.assertGreater(len(clauses), 10)
        for clause in clauses:
            self.assertTrue(clause.endswith(GEMINATION_ENV),
                            f"clause {clause!r} does not use the shared "
                            "short-vowel-before-*j environment")

    def test_r_and_z_stay_out_of_the_gemination_law(self):
        """R&T p. 52: *r and *z are its only genuine exceptions."""
        body = self.define_body("PWGmcJGemination")
        for segment in ("{*r}", "{*z}"):
            self.assertNotIn(f"{segment} -> {segment} {segment}", body,
                             f"{segment} must not geminate before *j")

    def test_sc029_takes_only_the_geminate_input(self):
        """The singleton branches were an artifact of hay's bad protoform."""
        body = self.define_body("OEAwwjResolution")
        self.assertIn("{*á} {*w} {*w} {*j}", body)
        clauses = [c.strip() for c in body.split(",") if c.strip()]
        for clause in clauses:
            source = clause.split("->")[0]
            self.assertEqual(source.count("{*w}"), 2,
                             f"SC029 clause {clause!r} does not take a geminate "
                             "input; SC010 now supplies the geminate for every "
                             "witness, so singleton branches are unwitnessed")

    def test_sc029_is_not_telescoped_into_sc010(self):
        """Both changes must remain separately visible.

        The West Germanic geminate is a reconstructed intermediate attested in
        the continental cognates (OHG houwi, gistrouwen; OS hoi). A later
        reversal is no reason to delete the earlier change.
        """
        self.assertIn("define PWGmcJGemination", self.uncommented)
        self.assertIn("define OEAwwjResolution", self.uncommented)

    # ------------------------------------------------------------------
    # Derivational chain
    # ------------------------------------------------------------------

    def test_gemination_then_resolution_then_fronting(self):
        """The full reconstructed chain must be visible for both witnesses.

        This reproduces R&T p. 53 and Campbell §120.2 step for step:
        PGmc singleton -> WGmc geminate -> pre-OE diphthong -> fronted.
        """
        for concept in AWJ_WITNESSES:
            for form in self.protoforms(concept):
                block = self.derivation(form)
                gemination = re.search(r"PWGmcJGemination: (\S+)", block)
                self.assertIsNotNone(
                    gemination,
                    f"{concept}: SC010 must FIRE (not '[no-change]'), creating "
                    "the West Germanic geminate")
                self.assertIn("*w*w*j", gemination.group(1),
                              f"{concept}: SC010 must produce the *wwj geminate")
                resolved = re.search(r"OEAwwjResolution: (\S+)", block)
                self.assertIsNotNone(resolved, f"{concept}: SC029 must fire")
                self.assertIn("*áu*j", resolved.group(1),
                              f"{concept}: SC029 must yield *au with *j surviving")
                fronted = re.search(r"OEAuBrightening: (\S+)", block)
                self.assertIsNotNone(fronted, f"{concept}: SC030 must fire")
                self.assertIn("*áeu", fronted.group(1),
                              f"{concept}: SC030 must front the new *au")

    def test_surface_outputs_are_unchanged_by_the_repair(self):
        """The repair corrects the history without moving any surface form."""
        for concept, expected in AWJ_WITNESSES.items():
            for form in self.protoforms(concept):
                block = self.derivation(form)
                self.assertIn(f"OUTPUTS: {expected}", block,
                              f"{concept} must still yield {expected}")

    def test_the_iwj_witness_geminates_but_is_not_resolved(self):
        """hue is a positive SC010 control and a negative SC029/SC030 control.

        Campbell §120.2 p. 46 has both types geminate and then diverge: the
        low-vowel type loses its *u and keeps its *j, giving hīeġ, while this
        type loses its *j and keeps its *w, giving hīew.
        """
        concept, form, expected = IWJ_WITNESS
        block = self.derivation(form)
        gemination = re.search(r"PWGmcJGemination: (\S+)", block)
        self.assertIsNotNone(
            gemination,
            f"{concept}: SC010 must FIRE, creating the West Germanic geminate")
        self.assertIn("*w*w*j", gemination.group(1),
                      f"{concept}: SC010 must produce the *wwj geminate")
        self.assertNotIn("OEAwwjResolution: ", block,
                         f"{concept}: SC029 resolves the low-vowel type only")
        self.assertNotIn("OEAuBrightening: ", block,
                         f"{concept}: SC030 fronts an *au this word never has")
        self.assertIn(f"OUTPUTS: {expected}", block,
                      f"{concept} must yield {expected}")

    def test_the_two_wj_types_diverge_after_the_geminate(self):
        """The minimal pair hay : hue must differ only after gemination.

        Both enter with a short vowel before *wj and both geminate. Thereafter
        the low-vowel word keeps its *j to the surface as orthographic g, and
        the front-vowel word keeps its *w.
        """
        hay_block = self.derivation(next(iter(self.protoforms("hay"))))
        hue_block = self.derivation(IWJ_WITNESS[1])
        for block in (hay_block, hue_block):
            self.assertRegex(block, r"PWGmcJGemination: \S*\*w\*w\*j")
        self.assertIn("OUTPUTS: hīeġ", hay_block)
        self.assertIn("OUTPUTS: hīew", hue_block)

    def test_negative_controls_do_not_geminate(self):
        """A broad *w branch must not create accidental geminates.

        Every curated control must be PRESENT before its non-application is
        checked. A missing form is a test defect, not a pass: silently
        skipping an absent control would let a typo or a deleted corpus row
        turn this into a test of nothing.
        """
        for form, reason in NEGATIVE_CONTROLS.items():
            with self.subTest(form=form):
                self.assertIn(f"PROTO: {form}\n", self.trace,
                              f"curated control {form!r} ({reason}) is not a "
                              "selected protoform; fix the list rather than "
                              "letting the check be skipped")
                block = self.derivation(form)
                fired = re.search(r"PWGmcJGemination: (\S+)", block)
                if fired is not None:
                    self.assertNotIn(
                        "*w*w", fired.group(1),
                        f"{form} must not undergo *w-gemination: {reason}")

    def test_every_selected_w_form_outside_the_domain_is_left_alone(self):
        """The same check, over the whole corpus rather than a curated list.

        Only a short vowel immediately before *wj may gain a geminate *w. Any
        other selected protoform containing *w must come through SC010 without
        one, whatever else that rule does to it.
        """
        for row in self.corpus:
            if row["DOCULECT"] != "Old_English":
                continue
            if row["COUNTERPART"] in ("", "-"):
                continue
            form = row["PROTOFORM"]
            if "w" not in form or SHORT_VOWEL_WJ.search(form):
                continue
            if f"PROTO: {form}\n" not in self.trace:
                continue
            with self.subTest(concept=row["CONCEPT"], form=form):
                block = self.derivation(form)
                fired = re.search(r"PWGmcJGemination: (\S+)", block)
                if fired is None:
                    continue
                before = form.count("w")
                self.assertLessEqual(
                    fired.group(1).count("*w"), before,
                    f"{row['CONCEPT']} {form} gained a *w at SC010 but has no "
                    "short vowel before *wj")

    def test_no_clean_long_syllable_wj_control_can_exist(self):
        """Sievers' law removes the *-j- allomorph after a heavy syllable.

        The short-syllable conditioning of the gemination law therefore cannot
        be demonstrated directly with a *wj minimal pair: a heavy stem takes
        *-ij- instead, as betray *lḗwijaną and smear *smérwijaną do. Every
        selected *wj form must consequently have a short vowel. If a genuine
        long-syllable *wj reconstruction is ever found in the sources, it
        becomes the missing negative control and this test must be revisited.
        """
        wj_forms = sorted({
            (r["CONCEPT"], r["PROTOFORM"]) for r in self.corpus
            if "wj" in r["PROTOFORM"]
        })
        self.assertTrue(wj_forms, "the *w branch has lost all its witnesses")
        for concept, form in wj_forms:
            with self.subTest(concept=concept, form=form):
                self.assertRegex(
                    form, SHORT_VOWEL_WJ,
                    f"{concept} {form} has *wj without a short vowel; if this "
                    "is source-supported it is the long-syllable control the "
                    "*w branch has so far lacked")

    # ------------------------------------------------------------------
    # Registry and chronology
    # ------------------------------------------------------------------

    def test_sc010_keeps_confidence_a(self):
        """The general law stays secure; the dispute is confined to *w.

        Fulk §4.10 n. 1 p. 73 rejects only the *w member, so the confidence
        letter for the whole law must not be lowered mechanically.
        """
        self.assertEqual(self.registry["SC010"]["confidence"], "A")
        notes = self.registry["SC010"]["staging_notes"]
        self.assertIn("Fulk", notes,
                      "SC010 must record the dispute over its *w member")

    def test_sc029_keeps_confidence_b(self):
        """Discreteness still depends on the disputed gemination analysis."""
        self.assertEqual(self.registry["SC029"]["confidence"], "B")

    def test_sc010_feeds_sc029(self):
        """The feeding relation must be registered now that SC010 creates it."""
        matches = [e for e in self.edges
                   if e["source_change_id"] == "SC010"
                   and e["target_change_id"] == "SC029"]
        self.assertTrue(matches, "missing chronology edge SC010 -> SC029")
        for edge in matches:
            self.assertEqual(edge["witness_role"], "feeding")
            self.assertIn("hay", edge["representative_lexemes"])
            self.assertIn("strew", edge["representative_lexemes"])

    def test_sc029_still_feeds_sc030(self):
        """The repair must strengthen, not alter, the 11aa99e8 conclusion."""
        matches = [e for e in self.edges
                   if e["source_change_id"] == "SC029"
                   and e["target_change_id"] == "SC030"]
        self.assertTrue(matches, "SC029 -> SC030 feeding edge disappeared")
        for edge in matches:
            self.assertEqual(edge["witness_role"], "feeding")

    # ------------------------------------------------------------------
    # Memo
    # ------------------------------------------------------------------

    def test_memo_adopts_architecture_a_explicitly(self):
        self.assertIn("CAPR adopts **architecture A**", self.memo)
        for needle in (
            "every consonant except r being affected after short syllables",
            "it appears that that cluster too underwent gemination in PWGmc",
        ):
            self.assertIn(needle, self.memo_flat,
                          f"memo must quote the source directly: {needle!r}")

    def test_memo_records_fulks_dissent_without_adopting_it(self):
        self.assertIn("Fulk", self.memo)
        self.assertIn("straujaną", self.memo_flat,
                      "memo must state Fulk's actual alternative, that the "
                      "diphthong is original, not merely that he disagrees")

    def test_memo_records_the_rename_debt(self):
        self.assertIn("rename", self.memo_flat)


if __name__ == "__main__":
    unittest.main()
