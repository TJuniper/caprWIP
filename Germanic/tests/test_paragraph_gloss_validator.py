"""Regression tests for lexical forms versus sound notation in book prose."""
from pathlib import Path
import shutil
import subprocess
import unittest


FILTER = Path(__file__).resolve().parents[1] / "tools/paragraph_gloss_validator.lua"


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is required")
class ParagraphGlossValidatorTests(unittest.TestCase):
    def validate(self, markdown):
        return subprocess.run(
            [
                "pandoc", "--from=markdown+raw_tex+citations", "--to=json",
                f"--lua-filter={FILTER}",
            ],
            input=markdown, text=True, capture_output=True, timeout=30,
        )

    def test_part_one_sound_notation_is_not_lexical(self):
        for form in ("ā", "ō", "ą̄", "ēa", "īe", "sċ", "xst", "*ai", "*au"):
            with self.subTest(form=form):
                result = self.validate(f"The sequence *{form}* changes.\n")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("Total violations: 0", result.stderr)

    def test_short_lexical_forms_still_require_glosses(self):
        for form in ("cū", "cȳ", "bā", "āk", "gōs", "stān", "giftiz"):
            with self.subTest(form=form):
                result = self.validate(f"Old English *{form}* survives.\n")
                # Plain ASCII forms are checked when explicitly marked lexical.
                if form == "giftiz":
                    result = self.validate("[giftiz]{.recon .iv lang=pgmc} survives.\n")
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn(f"missing gloss for *{form}*", result.stderr)

    def test_explicit_lexical_segments_are_not_silently_exempted(self):
        for cls in ("iv", "lex"):
            with self.subTest(cls=cls):
                result = self.validate(f"[ā]{{.{cls}}} survives.\n")
                self.assertEqual(result.returncode, 2, result.stderr)

    def test_glossed_forms_pass(self):
        result = self.validate(
            "*cȳ* 'cow' and [giftiz]{.recon .iv lang=pgmc} 'gift' survive.\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_first_occurrence_is_per_paragraph(self):
        result = self.validate("*cū* 'cow' and *cū*.\n\nAgain *cū*.\n")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("Para 2: missing gloss for *cū*", result.stderr)
        self.assertNotIn("Para 1: missing", result.stderr)

    def test_prediction_and_example_exemptions_remain(self):
        result = self.validate("[cȳ]{.pred} and [giftiz]{.ex}.\n")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_combining_marks_do_not_hide_lexical_forms(self):
        result = self.validate("*cū* survives.\n")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("missing gloss for *cū*", result.stderr)

    def test_part_two_notation_and_lexical_boundary(self):
        prefix = "# Word-by-word derivations\n\n### Cow\n\n#### Old English evidence\n\n"
        notation = self.validate(prefix + "*ą̄* and *ēa*.\n")
        self.assertEqual(notation.returncode, 0, notation.stderr)
        lexical = self.validate(prefix + "*cȳ* survives.\n")
        self.assertEqual(lexical.returncode, 2, lexical.stderr)


if __name__ == "__main__":
    unittest.main()
