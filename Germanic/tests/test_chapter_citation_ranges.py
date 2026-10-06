"""Regression tests for the edited-volume citation guardrail.

The defect these protect against is specific and was live in the repository:
the Cambridge History of the English Language, vol. I is an edited volume
whose chapters have different authors, so a page citation to it is an
authorship claim. When the volume shared a citation key with Hogg's own
Grammar, pages written by Bammesberger, Kastovsky and Toon were all being
attributed to Hogg. The guardrail turns that into a mechanical check, and
these tests keep the guardrail itself honest: one half proves it still
catches the impossible combinations, the other proves it stays quiet about
the legitimate citation forms it must not disturb.
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))

import check_chapter_citation_ranges as guard  # noqa: E402


class ChapterRangeGuardTests(unittest.TestCase):
    """Exercise the guardrail against synthetic citation sites."""

    @classmethod
    def setUpClass(cls) -> None:
        bib = (REPO_ROOT / "docs" / "refs.bib").read_text(encoding="utf-8")
        cls.ranges, cls.volume = guard.read_bibliography(bib)

    def findings(self, markdown: str):
        """Run the guardrail over a throwaway file holding `markdown`."""
        with tempfile.TemporaryDirectory(dir=REPO_ROOT) as tmp:
            path = Path(tmp) / "probe.md"
            path.write_text(markdown, encoding="utf-8")
            return guard.scan([path], self.ranges, self.volume)

    def assertFlagged(self, markdown: str, *expected: str) -> None:
        found = self.findings(markdown)
        self.assertTrue(found, f"guardrail stayed silent about {markdown!r}")
        message = " ".join(detail for _, detail in found)
        for needle in expected:
            self.assertIn(needle, message)

    def assertClean(self, markdown: str) -> None:
        found = self.findings(markdown)
        self.assertFalse(
            found, f"guardrail wrongly flagged {markdown!r}: {found}")

    # The bibliography must actually supply the ranges the guardrail needs;
    # if it stops doing so the tests below would pass vacuously.
    def test_chapter_ranges_come_from_the_bibliography(self) -> None:
        for key, (lo, hi) in {
            "HoggIntroduction1992": (1, 25),
            "Bammesberger1992": (26, 66),
            "HoggPhonology1992": (67, 167),
            "Traugott1992": (168, 289),
            "Kastovsky1992": (290, 407),
            "Toon1992": (409, 451),
            "Clark1992": (452, 487),
        }.items():
            with self.subTest(chapter=key):
                self.assertIn(key, self.ranges)
                self.assertEqual(self.ranges[key], (lo, hi))

    def test_a_page_outside_the_chapter_is_rejected(self) -> None:
        # The concrete remnant that prompted the guardrail: a page in the 300s
        # attributed to Hogg's chapter, which ends at 167.
        self.assertFlagged("A claim [@HoggPhonology1992, p. 357].",
                           "HoggPhonology1992", "Kastovsky1992")

    def test_the_named_chapter_author_is_reported(self) -> None:
        self.assertFlagged("A claim [@Bammesberger1992, p. 100].",
                           "HoggPhonology1992")
        self.assertFlagged("A claim [@Kastovsky1992, p. 39].",
                           "Bammesberger1992")
        self.assertFlagged("A claim [@HoggPhonology1992, p. 446].",
                           "Toon1992")

    def test_a_page_outside_the_whole_volume_is_still_rejected(self) -> None:
        self.assertFlagged("A claim [@HoggPhonology1992, p. 9001].")

    def test_a_page_citation_to_the_container_key_is_flagged(self) -> None:
        # A page belongs to a chapter, and a chapter has an author; citing the
        # volume itself for one hides that.
        self.assertFlagged("A claim [@HoggCHEL1992, p. 39].",
                           "Bammesberger1992")

    def test_pages_inside_the_chapter_are_accepted(self) -> None:
        for citation in ("[@HoggPhonology1992, p. 67]",
                         "[@HoggPhonology1992, p. 113]",
                         "[@HoggPhonology1992, p. 167]",
                         "[@Bammesberger1992, p. 39]",
                         "[@Kastovsky1992, pp. 358--361]",
                         "[@Toon1992, p. 446]"):
            with self.subTest(citation=citation):
                self.assertClean(f"A claim {citation}.")

    def test_non_numeric_and_whole_work_locators_are_left_alone(self) -> None:
        # Deliberately conservative: sections, notes and bare references are
        # legitimate and carry no page claim to contradict.
        for citation in ("[@HoggPhonology1992]",
                         "[@HoggPhonology1992, §3.3.1.3]",
                         "[@HoggCHEL1992]",
                         "[@HoggGrammar1992, §4.11]",
                         "[@HoggGrammar1992, p. 357]"):
            with self.subTest(citation=citation):
                self.assertClean(f"A claim {citation}.")

    def test_the_live_repository_is_clean(self) -> None:
        paths = [p for p in guard.REPO_ROOT.rglob("*.md")
                 if not guard.is_archive(p)]
        self.assertEqual([], guard.scan(paths, self.ranges, self.volume))


if __name__ == "__main__":
    unittest.main()
