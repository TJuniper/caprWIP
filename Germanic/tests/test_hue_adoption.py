import copy
import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import adjudicate
import anglo_frisian_experiments as experiments
import cascade_baseline as baseline
import oe_pipeline
from test_sc043_component_split import rows

BASE = ROOT / "Germanic/docs/sound_changes/cascade_baseline"
RESEARCH = ROOT / "Germanic/docs/sound_changes/literature_dossiers/anglo_frisian"


class HueAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.approval = json.loads((BASE / "approved_hue_input_migration.json").read_text())
        self.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc033_hue.tsv",
            BASE / "cascade_baseline_summary_pre_sc033_hue.json",
        )
        self.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs.tsv", BASE / "cascade_baseline_summary.json",
        )

    def test_exact_hue_input_transition_preserves_every_final_and_context(self):
        baseline.validate_cell_transition(self.previous, self.current, self.approval)
        old = {row["row_id"]: row for row in self.previous["records"]}
        new = {row["row_id"]: row for row in self.current["records"]}
        self.assertEqual([identifier for identifier in old if old[identifier] != new[identifier]],
                         ["2332"])
        self.assertEqual(new["2332"]["proto"], "*xíwją")
        for identifier in old:
            for field in ("counterpart", "outputs", "accepted", "output_count", "match",
                          "word_stress", "phonological_finality"):
                self.assertEqual(old[identifier][field], new[identifier][field])
        self.assertEqual(
            self.current["summary"]["outputs_sha256"],
            "47a901e9e4a7cd663b8eb574b87fe737382e8fc1b4f1bc8afc38701af0c96872",
        )
        self.assertEqual(
            self.current["summary"]["lexical_outputs_sha256"],
            "90789094b8d8889bb478dd6077de75e1d8e1cb66b7b6d347b63e73a83d039c47",
        )
        self.assertEqual(self.current["summary"]["legacy_subset_sha256"],
                         self.previous["summary"]["legacy_subset_sha256"])
        corpus = next(row for row in rows(ROOT / "Germanic/data/germanic-aligned-final.tsv")
                      if row["ID"] == "2332")
        self.assertEqual((corpus["PROTO"], corpus["PROTOFORM"]), ("*xíwją", "*xíwją"))
        self.assertEqual(corpus["DERIVATION_CLASS"], "regular")

    def test_rejects_undeclared_hue_and_other_row_drift(self):
        for identifier, field, value in (
            ("2332", "counterpart", "hīw"), ("2332", "outputs", "hīw"),
            ("2332", "word_stress", "unstressed"), ("2332", "output_count", "2"),
            ("2085", "proto", "*knéwą"), ("2085", "outputs", "cnēow"),
        ):
            candidate = copy.deepcopy(self.current)
            next(row for row in candidate["records"] if row["row_id"] == identifier)[field] = value
            with self.subTest(identifier=identifier, field=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, candidate, self.approval)

    def test_transition_ids_fail_closed_before_archive_access(self):
        for value in ("", "../knee", "/tmp/hue", "Hue", 1, None):
            approval = {**self.approval, "transition_id": value}
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "transition id"):
                baseline.validate_cell_transition(self.previous, self.current, approval)
            with self.subTest(adoption=value), self.assertRaisesRegex(ValueError, "transition id"):
                baseline.adopt_cell_baseline(self.current, BASE, approval)

    def test_distinct_archive_preserves_knee_receipt_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for source, destination in (
                ("cascade_baseline_outputs_pre_sc033_hue.tsv", "cascade_baseline_outputs.tsv"),
                ("cascade_baseline_summary_pre_sc033_hue.json", "cascade_baseline_summary.json"),
                ("cascade_baseline_outputs_pre_sc033.tsv", "cascade_baseline_outputs_pre_sc033.tsv"),
                ("cascade_baseline_summary_pre_sc033.json", "cascade_baseline_summary_pre_sc033.json"),
                ("cascade_baseline_outputs_legacy380.tsv", "cascade_baseline_outputs_legacy380.tsv"),
                ("approved_input_migrations.tsv", "approved_input_migrations.tsv"),
                ("approved_cell_migration.json", "approved_cell_migration.json"),
            ):
                (target / destination).write_bytes((BASE / source).read_bytes())
            preserved = {name: (target / name).read_bytes() for name in (
                "cascade_baseline_outputs_pre_sc033.tsv", "cascade_baseline_summary_pre_sc033.json",
                "approved_cell_migration.json", "cascade_baseline_outputs_legacy380.tsv",
            )}
            old = (target / "cascade_baseline_outputs.tsv").read_bytes()
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual((target / "cascade_baseline_outputs_pre_sc033_hue.tsv").read_bytes(), old)
            self.assertEqual({name: (target / name).read_bytes() for name in preserved}, preserved)
            before = {path.name: path.read_bytes() for path in target.iterdir()}
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual({path.name: path.read_bytes() for path in target.iterdir()}, before)
            (target / "cascade_baseline_summary_pre_sc033_hue.json").unlink()
            with self.assertRaisesRegex(ValueError, "incomplete"):
                baseline.adopt_cell_baseline(self.current, target, self.approval)

    def test_explicit_receipt_selection_and_unsafe_filenames(self):
        result = SimpleNamespace(returncode=0, stdout=json.dumps(self.current), stderr="")
        with patch.object(sys, "argv", [
            "adjudicate.py", "SC033", "--adopt-cell-baseline", "--approval",
            "approved_hue_input_migration.json",
        ]), patch.object(adjudicate, "run_in_runner", return_value=result), \
                patch.object(baseline, "adopt_cell_baseline") as adopter:
            self.assertEqual(adjudicate.main(), 0)
            adopter.assert_called_once_with(self.current, BASE, self.approval)
        for filename in ("../approved_hue_input_migration.json", "/tmp/approval.json", "bad.json"):
            with self.subTest(filename=filename), patch.object(sys, "argv", [
                "adjudicate.py", "SC033", "--adopt-cell-baseline", "--approval", filename,
            ]), patch.object(adjudicate, "run_in_runner") as runner:
                self.assertEqual(adjudicate.main(), 2)
                runner.assert_not_called()

    def test_component_identity_order_and_no_invented_historical_metadata(self):
        order = [stage.foma_identifier for stage in oe_pipeline.stages()]
        start = order.index("OEEwLongDiphthong")
        self.assertEqual(order[start:start + 4], [
            "OEEwLongDiphthong", "OEJWWSimplification", "OEJGlideIO", "OEDiphthongLeveling",
        ])
        registry = rows(ROOT / "Germanic/docs/sound_changes/registry/sc_registry.tsv")
        realization = next(row for row in registry if row["sc_id"] == "SC110")
        self.assertEqual(realization["fst_identifier"], "OEJGlideIO")
        self.assertEqual(realization["entry_type"], "support_stage")
        for field in ("hist_stage", "hist_scope", "confidence", "verdict"):
            self.assertEqual(realization[field], "")

    def test_publication_fingerprint_declares_exact_hue_delta(self):
        declared = [
            row for row in rows(ROOT / "Germanic/docs/book/index_semantic_fingerprint_allowlist.tsv")
            if row["language"] == "pgmc" and (
                row["source_ref"] == "hue — OE hīew"
                or row["source_ref"].endswith("/2332-hue-hīew.model.md")
            )
        ]
        self.assertEqual(len(declared), 5)
        self.assertTrue(all(row["action"] == "add" for row in declared))
        self.assertEqual(
            {(row["form"], row["form_role"], row["source_scope"]) for row in declared},
            {
                ("*xíwją", "selected_input", "trace_proto_input"),
                ("*xíwją", "source_protoform", "lexical_protoform"),
                ("heuja-", "comparison_form", "explicit_tag"),
                ("hiwją", "comparison_form", "explicit_tag"),
                ("xewjan", "comparison_form", "explicit_tag"),
            },
        )

    def test_current_protected_assay_and_historical_knee_controls(self):
        data = experiments.load_recipes(RESEARCH / "oe_post_hue_controls.json")
        recipe = data["recipes"][1]
        self.assertEqual(
            data["baseline_fst_sha256"],
            hashlib.sha256((ROOT / "Germanic/fsts/germanic.txt").read_bytes()).hexdigest(),
        )
        report = json.loads((RESEARCH / "oe_post_hue_result.json").read_text())
        self.assertEqual(report["recipe"], recipe)
        self.assertEqual(report["selected_rows"], 387)
        self.assertTrue(report["identity_equal"])
        self.assertTrue(report["canonical_artifacts_unchanged"])
        for field in ("changed_ids", "input_changed_ids", "missing_output_ids",
                      "ambiguous_output_ids"):
            self.assertEqual(report[field], [])
        self.assertEqual(report["variant_mismatch_ids"],
                         ["1973", "2013", "2030", "2162", "2240", "2298", "2300"])
        self.assertEqual(len(report["checked_component_fixtures"]), len(recipe["component_checks"]))
        self.assertEqual(len(report["checked_staged_fixtures"]), len(recipe["staged_checks"]))
        with (RESEARCH / data["fixture_file"]).open() as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(experiments.check_fixture_predictions(report, fixtures),
                         report["checked_fixture_ids"])
        self.assertTrue(any(path.endswith("approved_hue_input_migration.json")
                            for path in report["canonical_protected_hashes"]))
        archived = {row["row_id"]: row for row in self.previous["records"]}
        for row in report["rows"]:
            self.assertEqual(row["variant_outputs"], archived[row["id"]]["outputs"].split("|"))
            for states in row["intermediates"].values():
                self.assertEqual(states["baseline"], states["variant"])


if __name__ == "__main__":
    unittest.main()
