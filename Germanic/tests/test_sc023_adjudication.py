#!/usr/bin/env python3
"""Focused regression for the SC023 scope/stage adjudication (2026).

Adjudication memo: Germanic/docs/sound_changes/audits/sc023-adjudication.md

Protected invariants:

  * The executable rule `PNWGmcNStemNLoss` is unchanged (stable identifier;
    `{*ō} {*n} -> {*ǭ}` word-finally) and remains in the numbered cascade.
  * The 17 adjudicated weak-noun citation stems in `*-ōn-` all fire, the
    protected `-un` controls do not, and every live firing satisfies the
    rule's formal domain (final `*ōn` -> `*ǭ`); the complete current firing
    population is machine-derived and owned by the coverage census.
  * The verb `do` (`*dōną`) does NOT undergo SC023 — it is a counterfeeding
    (negative) witness only: SC047 later strips `*ą` and the secondary final
    `-n` of `dōn` must survive.
  * PGmc `*sebun`/`*nigun`/`*tehun`/`*hebun-` keep final `-un` (numeral
    analogy, Ringe 2017: 103); the `{*ō}`-restricted proxy must never touch
    them.
  * Canonical historical metadata says (pre-)Proto-Germanic / pan-Germanic,
    not Northwest Germanic, even though the executable identifier keeps the
    `PNWGmc` prefix (stage comes from metadata, not the name prefix).

Run: cd Germanic/tests && python3 -m unittest test_sc023_adjudication
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
ARCHIVAL_ORDERS = SC_DIR / "registry" / "archival_orders.tsv"
CENSUS = SC_DIR / "cascade_baseline" / "rule_coverage_census.tsv"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
HISTORICAL_AUDIT = SC_DIR / "cascade_baseline" / "historical_audit_table.tsv"
RENAME_MANIFEST = SC_DIR / "cascade_baseline" / "rename_migration_manifest.tsv"
CARD = SC_DIR / "order_tests" / "chronology_cards" / "SC023-nwgmc-n-stem-n-loss.md"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
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

# The adjudicated firing population: weak-noun citation stems in *-ōn-.
EXPECTED_FIRING_CONCEPTS = {
    "adder", "earth", "flask", "heart", "line", "list", "nettle",
    "nightmare", "side", "sun", "swallow", "toe", "tongue", "wart",
    "weasel", "whore", "widow",
}

# -un# inputs that the (pre-)PGmc law's reconstructed lexicon already
# exempts (numeral analogy; Ringe 2017: 103) and the proxy must not touch.
UN_FINAL_CONCEPTS = {"seven", "nine", "ten", "heaven"}


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


class SC023AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        # Strip only full-line comments; inline stripping would mangle the
        # word-boundary symbol `.#.` inside rule bodies.
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

    # ------------------------------------------------------------------
    # Executable rule stability
    # ------------------------------------------------------------------

    def test_rule_definition_is_unchanged(self):
        match = re.search(
            r"define\s+PNWGmcNStemNLoss\s*\[\s*\{\*ō\}\s*\{\*n\}\s*->\s*\{\*ǭ\}"
            r"\s*\|\|\s*_\s*\.#\.\s*\];",
            self.uncommented,
        )
        self.assertIsNotNone(
            match,
            "PNWGmcNStemNLoss must stay the byte-stable {*ō}{*n} -> {*ǭ} / _ .#. proxy",
        )

    def test_rule_is_a_live_numbered_cascade_stage(self):
        # The executable slot number is a projection of the current cascade
        # and is never pinned: the semantic invariants are (a) the rule is a
        # live numbered stage, and (b) the stable identifier ordering (SC023)
        # is asserted against the frozen archival order space below.
        self.assertIn("PNWGmcNStemNLoss", self.positions)
        archival = {
            r["sc_id"]: r for r in _tsv_rows(ARCHIVAL_ORDERS)
        }
        self.assertEqual(archival["SC023"]["inventory_order"], "23")

    # ------------------------------------------------------------------
    # Firing population pinned (live stage bins)
    # ------------------------------------------------------------------

    @requires_runtime
    def test_required_weak_nouns_fire_and_the_domain_is_respected(self):
        """§17 semantics: the 17 adjudicated weak-noun diagnostics must fire,
        the protected -un controls must not, and every live firing must
        satisfy the rule's formal domain (final *ōn -> *ǭ). The complete
        current firing population is machine-derived (coverage census); a
        legitimate new weak noun in *-ōn- passes automatically."""
        fired = {}
        candidates = {
            concept: row for concept, row in self.baseline.items()
            if row["proto"].endswith("n")
        }
        # Every possible live firing must involve a proto in final -n;
        # censusing only those rows keeps the test fast while remaining
        # exhaustive for this rule (a firing requires a final *ōn match).
        for concept, row in sorted(candidates.items()):
            form = row["proto"].lstrip("*")
            before = self.stage("pnwgmc_mn_dissimilation", form)
            after = self.stage("pnwgmc_n_stem_n_loss", form)
            if before != after:
                fired[concept] = (before[0], after[0])
        self.assertTrue(
            EXPECTED_FIRING_CONCEPTS <= set(fired),
            f"required SC023 diagnostics missing: "
            f"{sorted(EXPECTED_FIRING_CONCEPTS - set(fired))}",
        )
        self.assertFalse(
            UN_FINAL_CONCEPTS & set(fired),
            "a protected -un control fired on SC023 (numeral analogy, "
            "Ringe 2017: 103)",
        )
        for concept, (before, after) in sorted(fired.items()):
            with self.subTest(concept=concept):
                self.assertTrue(
                    before.replace("*", "").endswith("ōn"),
                    f"{concept}: SC023 fired outside its *ōn# domain "
                    f"({before!r})")
                self.assertTrue(
                    after.replace("*", "").endswith("ǭ"),
                    f"{concept}: SC023 output does not end in *ǭ ({after!r})")

    @requires_runtime
    def test_do_is_not_a_live_application_and_don_keeps_secondary_n(self):
        row = self.baseline["do"]
        self.assertEqual(row["proto"], "*dōną")
        before = self.stage("pnwgmc_mn_dissimilation", "dōną")
        after = self.stage("pnwgmc_n_stem_n_loss", "dōną")
        self.assertEqual(before, after, "do must pass SC023 untouched")
        # Counterfeeding: SC047 creates the secondary final -n and it must
        # survive to the accepted output dōn.
        apocope = self.stage("oe_heavy_syllable_nasal_apocope", "dōną")
        self.assertEqual(apocope, ["*d*ō*n"])
        self.assertEqual(row["outputs"], "dōn")

    @requires_runtime
    def test_un_final_words_are_untouched_by_sc023(self):
        for concept in sorted(UN_FINAL_CONCEPTS):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            before = self.stage("pnwgmc_mn_dissimilation", form)
            after = self.stage("pnwgmc_n_stem_n_loss", form)
            self.assertEqual(
                before, after,
                f"{concept} ({row['proto']}) retained -un must not undergo SC023",
            )

    @requires_runtime
    def test_tongue_normalizes_citation_stem_to_nasalized_nom_sg(self):
        after = self.stage("pnwgmc_n_stem_n_loss", "túngōn")
        self.assertEqual(after, ["*t*ú*n*g*ǭ"])

    # ------------------------------------------------------------------
    # Canonical metadata: stage from metadata, not from the name prefix
    # ------------------------------------------------------------------

    def test_staging_map_says_proto_germanic(self):
        row = {r["sc_id"]: r for r in _tsv_rows(STAGING_MAP)}["SC023"]
        self.assertEqual(row["hist_stage"], "pgmc")
        self.assertEqual(row["hist_scope"], "pan_germanic")
        self.assertEqual(row["display_name"],
                         "Proto-Germanic Word-Final N Loss")
        self.assertEqual(row["action_status"], "metadata_corrected")
        self.assertEqual(row["fst_identifier"], "PNWGmcNStemNLoss")

    def test_inventory_says_proto_germanic_holding_zone(self):
        row = {r["change_id"]: r for r in _tsv_rows(INVENTORY)}["SC023"]
        self.assertEqual(row["stage"], "Proto-Germanic")
        self.assertEqual(row["historical_stage"], "Proto-Germanic")
        self.assertEqual(row["pipeline_stage"], "SC018-SC025 editorial holding zone")
        # The firing count is machine evidence: assert it AGREES with the
        # canonical census rather than pinning a hand-copied number.
        census = {r["sc_id"]: r for r in _tsv_rows(CENSUS)}["SC023"]
        self.assertEqual(row["firing_count"], census["corpus_firing_count"])
        self.assertEqual(row["firing_lexemes"], census["lexical_witnesses"])
        self.assertEqual(row["literature_status"], "adjudicated")
        self.assertIn("counterfeeding", row["notes"])

    def test_historical_audit_and_rename_manifest_are_corrected(self):
        audit = {r["sc_id"]: r for r in _tsv_rows(HISTORICAL_AUDIT)}["SC023"]
        rename = {r["sc_id"]: r for r in _tsv_rows(RENAME_MANIFEST)}["SC023"]
        self.assertEqual(audit["proposed_hist_stage"], "pgmc")
        self.assertEqual(audit["proposed_hist_scope"], "pan_germanic")
        self.assertEqual(audit["required_action"], "metadata_or_prose_only")
        self.assertEqual(rename["canonical_hist_stage"], "pgmc")
        self.assertEqual(rename["canonical_hist_scope"], "pan_germanic")
        self.assertEqual(rename["canonical_foma_identifier"], "PNWGmcNStemNLoss")

    def test_chronology_card_narrates_do_as_counterfeeding_negative_witness(self):
        card = CARD.read_text(encoding="utf-8")
        self.assertIn("counterfeeding", card)
        self.assertIn("negative", card)
        self.assertIn("sc023-adjudication.md", card)
        self.assertNotIn("must feed the later apocope", card)
        # The card must not present the stage as Northwest Germanic.
        self.assertNotIn("# SC023 NWGmc", card)


if __name__ == "__main__":
    unittest.main()
