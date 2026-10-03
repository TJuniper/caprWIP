#!/usr/bin/env python3
"""Phase 1 baseline invariants for the historical-cascade-order project.

These tests are host-runnable (no foma/flookup/Docker required). They protect
the frozen baseline artifacts against accidental drift and prove that the
executable-order manifest is an exact, reproducible projection of the current
``germanic.txt`` composition.

The *output-hash* reproducibility contract (that two independent recompiles
produce the same ``outputs_sha256``) is verified by the Docker wrapper
``build_cascade_baseline_docker.sh`` because it requires the transducer; here we
verify the committed artifacts are internally consistent and that the manifest
regenerates identically from source.

Run: cd Germanic/tests && python3 -m unittest test_cascade_baseline
"""
from __future__ import annotations

import csv
import importlib.util
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
BASELINE_DIR = REPO_ROOT / "Germanic/docs/sound_changes/cascade_baseline"
OUTPUTS_TSV = BASELINE_DIR / "cascade_baseline_outputs.tsv"
SUMMARY_JSON = BASELINE_DIR / "cascade_baseline_summary.json"
ORDER_MANIFEST = BASELINE_DIR / "cascade_order_manifest.tsv"
FST_SOURCE = REPO_ROOT / "Germanic/fsts/germanic.txt"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


class BaselineArtifactTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(OUTPUTS_TSV.exists(), f"missing {OUTPUTS_TSV}")
        self.assertTrue(SUMMARY_JSON.exists(), f"missing {SUMMARY_JSON}")
        self.summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
        with OUTPUTS_TSV.open(encoding="utf-8") as handle:
            self.rows = list(csv.DictReader(handle, delimiter="\t"))

    def test_summary_partitions_are_consistent(self):
        s = self.summary
        self.assertEqual(s["accepted"] + s["rejected"], s["total_lexemes"],
                         "accepted + rejected must equal total")
        self.assertEqual(s["matched"] + s["mismatched"], s["total_lexemes"],
                         "matched + mismatched must equal total")

    def test_outputs_hash_is_sha256_hex(self):
        self.assertRegex(self.summary["outputs_sha256"], r"^[0-9a-f]{64}$")

    def test_row_count_matches_summary(self):
        self.assertEqual(len(self.rows), self.summary["total_lexemes"],
                         "per-lexeme row count must equal summary total")

    def test_per_row_flags_are_consistent_with_outputs(self):
        for r in self.rows:
            outs = [o for o in r["outputs"].split("|") if o] if r["outputs"] else []
            self.assertEqual(int(r["output_count"]), len(outs),
                             f"output_count mismatch for {r['proto_norm']!r}")
            self.assertEqual(r["accepted"] == "1", bool(outs),
                             f"accepted flag mismatch for {r['proto_norm']!r}")
            self.assertEqual(r["match"] == "1", r["counterpart"] in outs,
                             f"match flag mismatch for {r['proto_norm']!r}")

    def test_aggregate_flag_counts_match_summary(self):
        accepted = sum(1 for r in self.rows if r["accepted"] == "1")
        matched = sum(1 for r in self.rows if r["match"] == "1")
        ambiguous = sum(1 for r in self.rows if int(r["output_count"]) > 1)
        self.assertEqual(accepted, self.summary["accepted"])
        self.assertEqual(matched, self.summary["matched"])
        self.assertEqual(ambiguous, self.summary["ambiguous_outputs"])

    def test_rows_are_deterministically_sorted(self):
        keys = [(r["proto_norm"], r["counterpart"], r["concept"]) for r in self.rows]
        self.assertEqual(keys, sorted(keys),
                         "baseline rows must be sorted by (proto_norm, counterpart, concept)")


class LegacySubsetTests(unittest.TestCase):
    """Corpus-maturation baseline policy: the original 380-row corpus is a
    frozen legacy subset. Corpus expansion may change the whole-corpus
    fingerprint, but every legacy row must persist byte-identically and the
    legacy-subset hash must reproduce the frozen constant."""

    LEGACY_TSV = BASELINE_DIR / "cascade_baseline_outputs_legacy380.tsv"
    LEGACY_SHA = "fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf"
    ACTIVE_SHA = "04a24f4cd6ad61217a43ad47d5ac5f0d957a5f4f211559a7633d77dac852c409"

    def setUp(self):
        self.assertTrue(self.LEGACY_TSV.exists(), f"missing {self.LEGACY_TSV}")
        with self.LEGACY_TSV.open(encoding="utf-8") as handle:
            self.legacy_rows = list(csv.DictReader(handle, delimiter="\t"))
        with OUTPUTS_TSV.open(encoding="utf-8") as handle:
            self.current_rows = list(csv.DictReader(handle, delimiter="\t"))
        self.summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))

    def test_legacy_file_has_exactly_380_rows(self):
        self.assertEqual(len(self.legacy_rows), 380)

    def test_legacy_file_reproduces_frozen_fingerprint(self):
        import hashlib
        hasher = hashlib.sha256()
        for r in self.legacy_rows:
            hasher.update((r["proto_norm"] + "\x1f" + r["outputs"] + "\x1e").encode("utf-8"))
        self.assertEqual(hasher.hexdigest(), self.LEGACY_SHA,
                         "frozen legacy380 file no longer reproduces the frozen fingerprint")

    def test_every_legacy_row_persists_identically_in_current_baseline(self):
        mod = _load_module("cascade_baseline", TOOLS / "cascade_baseline.py")
        with (BASELINE_DIR / "approved_input_migrations.tsv").open(encoding="utf-8") as handle:
            migrations = list(csv.DictReader(handle, delimiter="\t"))
        selected = mod.legacy_subset(self.current_rows, self.legacy_rows, migrations)
        self.assertEqual(len(selected), 380)
        self.assertEqual([m["row_id"] for m in migrations], ["2040"])
        import hashlib
        digest = hashlib.sha256()
        for row in selected:
            digest.update((row["proto_norm"] + "\x1f" + row["outputs"] + "\x1e").encode())
        self.assertEqual(digest.hexdigest(), self.ACTIVE_SHA)

    def test_summary_records_legacy_subset_invariant(self):
        self.assertEqual(self.summary["legacy_subset_count"], 380)
        self.assertEqual(self.summary["legacy_subset_sha256"], self.ACTIVE_SHA)

    def test_migration_rejects_unapproved_or_ambiguous_drift(self):
        import copy
        mod = _load_module("cascade_baseline", TOOLS / "cascade_baseline.py")
        with (BASELINE_DIR / "approved_input_migrations.tsv").open(encoding="utf-8") as handle:
            migrations = list(csv.DictReader(handle, delimiter="\t"))
        for case in ("missing", "duplicate", "output", "wrong_input", "wrong_old", "unapproved"):
            current, old, approved = copy.deepcopy((self.current_rows, self.legacy_rows, migrations))
            gift = next(r for r in current if r["row_id"] == "2040")
            if case == "missing":
                current.remove(gift)
            elif case == "duplicate":
                current.append(copy.deepcopy(gift))
            elif case == "output":
                gift["outputs"] = "ġieft"
            elif case == "wrong_input":
                gift["proto"] = "*gēftiz"
            elif case == "wrong_old":
                approved[0]["old_proto"] = "*gēftiz"
            else:
                approved = []
            with self.subTest(case=case), self.assertRaises(ValueError):
                mod.legacy_subset(current, old, approved)

    def test_all_pre_sc056_selected_outputs_are_preserved(self):
        mod = _load_module("cascade_baseline", TOOLS / "cascade_baseline.py")
        with (BASELINE_DIR / "cascade_baseline_outputs_pre_sc056.tsv").open(encoding="utf-8") as handle:
            old = list(csv.DictReader(handle, delimiter="\t"))
        with (BASELINE_DIR / "approved_input_migrations.tsv").open(encoding="utf-8") as handle:
            migrations = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(len(old), 387)
        self.assertEqual(len(mod.legacy_subset(self.current_rows, old, migrations)), 387)


class OrderManifestTests(unittest.TestCase):
    def setUp(self):
        self.mod = _load_module("cascade_order_manifest", TOOLS / "cascade_order_manifest.py")
        self.assertTrue(ORDER_MANIFEST.exists(), f"missing {ORDER_MANIFEST}")
        with ORDER_MANIFEST.open(encoding="utf-8") as handle:
            self.rows = list(csv.DictReader(handle, delimiter="\t"))

    def test_manifest_matches_current_fst_source(self):
        """The committed manifest must be an exact projection of germanic.txt."""
        self.assertEqual(self.mod.manifest_text(),
                         ORDER_MANIFEST.read_text(encoding="utf-8"),
                         "cascade_order_manifest.tsv is stale relative to germanic.txt; "
                         "regenerate with tools/cascade_order_manifest.py")

    def test_positions_are_contiguous(self):
        positions = [int(r["position"]) for r in self.rows]
        self.assertEqual(positions, list(range(1, len(positions) + 1)))

    def test_manifest_begins_with_pwgmc_block(self):
        pwgmc = [r for r in self.rows if r["origin_block"] == "EarlyEnglishLineChanges"]
        # SC103 PGmcNasalLossBeforeX is pan-Germanic and leads the pipeline.
        # SC096 RootNounNomZLoss follows immediately (it must precede
        # PWGmcIjContraction, which creates monosyllabic *fríundz from
        # *fríjōndz); the EarlyEnglishLineChanges block is expanded
        # immediately after it, occupying contiguous positions.
        self.assertEqual(self.rows[0]["foma_identifier"], "PGmcNasalLossBeforeX",
                         "the pan-Germanic SC103 must lead the executable order")
        self.assertEqual(self.rows[1]["foma_identifier"], "RootNounNomZLoss",
                         "RootNounNomZLoss must lead the West Germanic block")
        head = self.rows[2: 2 + len(pwgmc)]
        self.assertTrue(all(r["origin_block"] == "EarlyEnglishLineChanges" for r in head),
                        "EarlyEnglishLineChanges members must follow RootNounNomZLoss contiguously")

    def test_required_local_dependencies_hold_in_current_order(self):
        """Baseline sanity: the demonstrated local dependencies hold in the
        current (old) order. These same edges must be preserved by any reorder.

        SC005 PNWGmcAToUBeforeM < SC017 PNWGmcULowering
        SC010 PWGmcJGemination < SC011 PWGmcSyllabicJ
        SC019 PNWGmcFinalLongORaising < SC020 EAFFinalZDeletion (final-*z* deletion)
        SC096 RootNounNomZLoss < PWGmcIjContraction (friend must reach SC096
            uncontracted/polysyllabic so its *-z falls under SC020, not SC096)
        SC020 EAFFinalZDeletion < SC097 MonosyllabicFinalZLoss (chronology:
            PWGmc unstressed loss precedes the later northern monosyllabic loss)
        SC018/SC019 raisers < SC097 MonosyllabicFinalZLoss (English-doculect
            *-ōz forms must not be exposed to final/monosyllabic ō-raising
            by premature z-loss)
        """
        pos = {r["foma_identifier"]: int(r["position"]) for r in self.rows}
        pairs = [
            ("PNWGmcAToUBeforeM", "PNWGmcULowering"),
            ("PWGmcJGemination", "PWGmcSyllabicJ"),
            ("PNWGmcFinalLongORaising", "EAFFinalZDeletion"),
            ("RootNounNomZLoss", "PWGmcIjContraction"),
            ("EAFFinalZDeletion", "MonosyllabicFinalZLoss"),
            ("PNWGmcStressedMonosyllableORaising", "MonosyllabicFinalZLoss"),
            ("PNWGmcFinalLongORaising", "MonosyllabicFinalZLoss"),
        ]
        for earlier, later in pairs:
            self.assertIn(earlier, pos, f"{earlier} missing from manifest")
            self.assertIn(later, pos, f"{later} missing from manifest")
            self.assertLess(pos[earlier], pos[later],
                            f"expected {earlier} before {later} in current cascade")


if __name__ == "__main__":
    unittest.main()
