#!/usr/bin/env python3
"""Consistency invariants tying the SC004/SC014 chronology artefacts together.

Host-runnable (no foma/Docker). These tests enforce that the first-break
summaries, the chronology cards, the chronology-card index, and the frozen
semantic baseline all agree, and that no chronology run was frozen while still
in progress.

Run: cd Germanic/tests && python3 -m unittest test_sc004_chronology_consistency
"""
from __future__ import annotations

import csv
import importlib.util
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SC = REPO / "Germanic/docs/sound_changes"
SUMMARIES = SC / "order_tests/summaries"
CARDS = SC / "order_tests/chronology_cards"
INDEX = CARDS / "chronology_card_index.tsv"
BASELINE = SC / "cascade_baseline/post_sc004_split_semantic_baseline.tsv"
TOOLS = REPO / "Germanic/tools"


def _load_builder():
    spec = importlib.util.spec_from_file_location(
        "build_post_sc004_split_semantic_baseline",
        TOOLS / "build_post_sc004_split_semantic_baseline.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _read_first_break(name: str) -> dict:
    path = SUMMARIES / f"sc004corr_first_break_{name}.tsv"
    with path.open(encoding="utf-8") as h:
        return {r["direction"]: r for r in csv.DictReader(h, delimiter="\t")}


def _index_rows() -> dict:
    with INDEX.open(encoding="utf-8") as h:
        lines = [line for line in h if not line.startswith("#")]
    return {r["change_id"]: r for r in csv.DictReader(lines, delimiter="\t")}


class FirstBreakTerminalTests(unittest.TestCase):
    """SC004 and SC014 chronology runs must be terminal in both directions."""

    def setUp(self):
        self.builder = _load_builder()

    def test_sc004_earlier_and_later_are_terminal(self):
        fb = _read_first_break("sc004")
        for d in ("earlier", "later"):
            self.assertIn(d, fb, f"SC004 missing {d} first-break row")
            self.assertIn(fb[d]["result"], self.builder.TERMINAL_RESULTS,
                          f"SC004 {d} first-break is not terminal: {fb[d]['result']!r}")

    def test_sc014_earlier_and_later_are_terminal(self):
        fb = _read_first_break("sc014")
        for d in ("earlier", "later"):
            self.assertIn(d, fb)
            self.assertIn(fb[d]["result"], self.builder.TERMINAL_RESULTS,
                          f"SC014 {d} first-break is not terminal: {fb[d]['result']!r}")


class IndexAgreesWithFirstBreakTests(unittest.TestCase):
    """The chronology-card index must match the first-break TSVs."""

    def setUp(self):
        self.index = _index_rows()

    def _check_later(self, sc: str, name: str):
        fb = _read_first_break(name)["later"]
        row = self.index[sc]
        if fb["result"] == "first_break_found":
            self.assertEqual(row["later_boundary_change_id"], fb["crossed_change_id"],
                             f"{sc} index later boundary disagrees with first-break TSV")
            self.assertEqual(row["later_boundary_order"], fb["first_break_order"],
                             f"{sc} index later boundary order disagrees with TSV")

    def test_sc004_index_matches_tsv(self):
        self._check_later("SC004", "sc004")

    def test_sc014_index_matches_tsv(self):
        self._check_later("SC014", "sc014")

    def test_sc036_earlier_index_matches_tsv(self):
        fb = _read_first_break("sc036")["earlier"]
        row = self.index["SC036"]
        if fb["result"] == "first_break_found":
            self.assertEqual(row["earlier_boundary_change_id"], fb["crossed_change_id"])
            self.assertEqual(row["earlier_boundary_order"], fb["first_break_order"])


class CardsAgreeWithFirstBreakTests(unittest.TestCase):
    """The SC004/SC014 chronology cards must cite the actual first-break boundary."""

    def test_sc014_card_cites_later_boundary(self):
        fb = _read_first_break("sc014")["later"]
        if fb["result"] == "first_break_found":
            text = (CARDS / "SC014-nwgmc-unstressed-ai-monophthongization.md").read_text(encoding="utf-8")
            self.assertIn(fb["crossed_change_id"], text)
            self.assertIn(fb["first_break_order"], text)

    def test_sc004_card_cites_later_boundary(self):
        fb = _read_first_break("sc004")["later"]
        if fb["result"] == "first_break_found":
            text = (CARDS / "SC004-pwgmc-ai-monophthongization.md").read_text(encoding="utf-8")
            self.assertIn(fb["crossed_change_id"], text)
            self.assertIn(fb["first_break_order"], text)


class BaselineDerivesFromTsvTests(unittest.TestCase):
    """The semantic baseline's boundary rows must be derived from the first-break
    TSVs (via the builder), not hardcoded."""

    def setUp(self):
        self.builder = _load_builder()
        with BASELINE.open(encoding="utf-8") as h:
            self.baseline = {r["artifact"]: r["value_or_sha256"]
                             for r in csv.DictReader(h, delimiter="\t")}

    def test_baseline_boundaries_match_builder_derivation(self):
        checks = [
            ("sc014_later_boundary", "sc014", "later"),
            ("sc014_earlier_boundary", "sc014", "earlier"),
            ("sc004_later_boundary", "sc004", "later"),
            ("sc004_earlier_boundary", "sc004", "earlier"),
            ("sc036_earlier_boundary", "sc036", "earlier"),
        ]
        for key, name, direction in checks:
            fb = _read_first_break(name).get(direction)
            self.assertIsNotNone(fb, f"{name} {direction} row missing")
            expected = self.builder.boundary_str(fb)
            self.assertEqual(self.baseline.get(key), expected,
                             f"baseline {key} is not derived from the first-break TSV "
                             f"(expected {expected!r}, got {self.baseline.get(key)!r})")

    def test_baseline_freezes_the_frozen_checksum(self):
        self.assertEqual(self.baseline.get("lexical_outputs_sha256"),
                         "aaf19ba919cafbe86ea59d482ce74d0944f541336e246da481a3f37b20da480e")


if __name__ == "__main__":
    unittest.main()
