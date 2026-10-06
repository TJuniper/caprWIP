#!/usr/bin/env python3
"""Focused regression for the SC022 literal adjacent-`mn` correction (2026-08).

These host-runnable tests protect the scientific consequences of retiring the
old cross-syllable `mV…n` proxy in `PNWGmcMnDissimilation` and making SC022 the
literal adjacent `mn > βn`, together with the two data rows that the correction
enables/repairs:

  * row 2068 (heaven): PROTOFORM `*xébun`  -> `heofon`  (early_analogy)
  * row 2216 (stem):   PROTOFORM `*stámniz` -> `stefn`   (early_analogy)

They assert against the committed rule source, the authoritative TSV rows, and
the frozen cascade baseline (the reproducibility contract), so no foma/flookup
or Docker is required. The live-cascade behaviour that produced these artifacts
(e.g. `*xémnas -> hefnes`, `*xémnum -> hefnum`, `*xémonų -> heomon`,
`*sébun -> seofon`) is recorded in the implementation audit
`Germanic/docs/audits/heaven-sc022-implementation-2026.md`.

Run: cd Germanic/tests && python3 -m unittest test_sc022_mn_dissimilation
"""
from __future__ import annotations

import csv
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST_SOURCE = GERMANIC / "fsts" / "germanic.txt"
TSV = GERMANIC / "data" / "germanic-aligned-final.tsv"
BASELINE = GERMANIC / "docs" / "sound_changes" / "cascade_baseline" / "cascade_baseline_outputs.tsv"
INVENTORY = GERMANIC / "docs" / "sound_changes" / "sound_change_inventory.tsv"
STAGING_MAP = GERMANIC / "docs" / "sound_changes" / "sound_change_historical_staging_map.tsv"
HISTORICAL_AUDIT = (
    GERMANIC / "docs" / "sound_changes" / "cascade_baseline" / "historical_audit_table.tsv"
)
INDEX_FORMS = GERMANIC / "docs" / "book" / "index_verborum_forms.tsv"


def _tsv_row(row_id: str) -> dict[str, str]:
    with TSV.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["ID"] == row_id:
                return row
    raise AssertionError(f"row {row_id} not found in {TSV}")


def _baseline_by_concept() -> dict[str, dict[str, str]]:
    with BASELINE.open(encoding="utf-8") as handle:
        return {row["concept"]: row for row in csv.DictReader(handle, delimiter="\t")}


def _metadata_row(path: Path, key: str) -> dict[str, str]:
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()
             if not line.startswith("#")]
    for row in csv.DictReader(lines, delimiter="\t"):
        if row[key] == "SC022":
            return row
    raise AssertionError(f"SC022 not found in {path}")


class SC022RuleBodyTests(unittest.TestCase):
    def setUp(self):
        self.text = FST_SOURCE.read_text(encoding="utf-8")

    def test_rule_is_literal_adjacent_mn(self):
        match = re.search(
            r"define PNWGmcMnDissimilation \[\s*(.*?)\s*\];", self.text, re.S
        )
        self.assertIsNotNone(match, "PNWGmcMnDissimilation definition not found")
        body = " ".join(match.group(1).split())
        self.assertEqual(
            body,
            "{*m} -> {*β} || EnglishStarVocalic _ {*n}",
            "SC022 must be the literal adjacent mn > β rule",
        )

    def test_cross_syllable_proxy_is_gone(self):
        self.assertNotIn(
            "EnglishStarVocalic _ EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal",
            self.text,
            "the old mV…n proxy environment must not remain in germanic.txt",
        )


class HeavenRowTests(unittest.TestCase):
    def test_tsv_row_2068(self):
        row = _tsv_row("2068")
        self.assertEqual(row["PROTOFORM"], "*xébun")
        self.assertEqual(row["COUNTERPART"], "heofon")
        self.assertEqual(row["DERIVATION_CLASS"], "early_analogy")
        self.assertEqual(row["PROTO"], "*xémenaz")

    def test_baseline_heaven_matches_via_new_input(self):
        heaven = _baseline_by_concept()["heaven"]
        self.assertEqual(heaven["proto"], "*xébun")
        self.assertEqual(heaven["outputs"], "heofon")
        self.assertEqual(heaven["output_count"], "1")
        self.assertEqual(heaven["match"], "1")

    def test_old_proxy_input_is_retired(self):
        self.assertNotEqual(
            _baseline_by_concept().get("heaven", {}).get("proto"), "*xémonų"
        )
        with TSV.open(encoding="utf-8") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                self.assertNotEqual(
                    row["PROTOFORM"], "*xémonų",
                    "the retired *xémonų proxy input must not remain in the TSV",
                )


class StemRowTests(unittest.TestCase):
    def test_tsv_row_2216(self):
        row = _tsv_row("2216")
        self.assertEqual(row["PROTOFORM"], "*stámniz")
        self.assertEqual(row["COUNTERPART"], "stefn")
        self.assertEqual(row["DERIVATION_CLASS"], "early_analogy")
        self.assertEqual(row["PROTO"], "*stámnaz")

    def test_baseline_stem_now_matches(self):
        stem = _baseline_by_concept()["stem"]
        self.assertEqual(stem["proto"], "*stámniz")
        self.assertEqual(stem["outputs"], "stefn")
        self.assertEqual(stem["output_count"], "1")
        self.assertEqual(stem["match"], "1")


class SevenControlTests(unittest.TestCase):
    def test_seven_regular_unchanged(self):
        seven = _baseline_by_concept()["seven"]
        self.assertEqual(seven["proto"], "*sébun")
        self.assertEqual(seven["outputs"], "seofon")
        self.assertEqual(seven["match"], "1")


class HistoricalScopeTests(unittest.TestCase):
    def test_stage_is_common_germanic_not_pnwgmc(self):
        inventory = _metadata_row(INVENTORY, "change_id")
        staging = _metadata_row(STAGING_MAP, "sc_id")
        audit = _metadata_row(HISTORICAL_AUDIT, "sc_id")
        self.assertEqual(inventory["stage"], "Common Germanic")
        self.assertEqual(inventory["trace_stage"], "SC018-SC025 editorial holding zone")
        self.assertEqual(inventory["historical_stage"], "Proto-Germanic")
        self.assertEqual(inventory["pipeline_stage"], "SC018-SC025 editorial holding zone")
        self.assertEqual(staging["hist_stage"], "pgmc")
        self.assertEqual(staging["hist_scope"], "pan_germanic")
        self.assertEqual(audit["proposed_hist_stage"], "pgmc")
        self.assertEqual(audit["proposed_hist_scope"], "pan_germanic")

    def test_stable_identifier_is_not_a_stage_claim(self):
        inventory = _metadata_row(INVENTORY, "change_id")
        staging = _metadata_row(STAGING_MAP, "sc_id")
        # The anchor is STABLE: it carries no line number, so inserting lines
        # above the definition cannot dirty a committed file.
        self.assertEqual(inventory["rule_source_anchor"], "define PNWGmcMnDissimilation")
        self.assertEqual(staging["fst_identifier"], "PNWGmcMnDissimilation")
        self.assertIn("stable Foma identifier only", inventory["notes"])

    def test_index_uses_canonical_form_stage_not_rule_name_prefix(self):
        with INDEX_FORMS.open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))

        stem_selected = [
            row for row in rows
            if row["form"] == "*stámniz"
            and row["form_role"] == "selected_input"
            and row["source_scope"] == "trace_proto_input"
        ]
        self.assertTrue(stem_selected)
        self.assertEqual({row["language"] for row in stem_selected}, {"pgmc"})

        heaven_selected = [
            row for row in rows
            if row["form"] == "*xébun"
            and row["form_role"] == "selected_input"
            and row["source_scope"] == "trace_proto_input"
        ]
        self.assertTrue(heaven_selected)
        self.assertEqual({row["language"] for row in heaven_selected}, {"nsgmc"})


class CorpusTotalsTests(unittest.TestCase):
    def test_summary_totals(self):
        summary = json.loads(
            (BASELINE.parent / "cascade_baseline_summary.json").read_text(encoding="utf-8")
        )
        # Corpus-maturation policy: the original corpus is a frozen legacy-380
        # subset; the whole-corpus total may grow, but every row (legacy and
        # new) must be accepted, the mismatch population stays the legacy 7,
        # and no row is ambiguous.
        self.assertEqual(summary["legacy_subset_count"], 380)
        self.assertGreaterEqual(summary["total_lexemes"], 380)
        self.assertEqual(summary["accepted"], summary["total_lexemes"])
        self.assertEqual(summary["matched"], summary["total_lexemes"] - 7)
        self.assertEqual(summary["mismatched"], 7)
        self.assertEqual(summary["ambiguous_outputs"], 0)


if __name__ == "__main__":
    unittest.main()
