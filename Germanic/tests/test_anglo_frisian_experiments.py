from __future__ import annotations

import copy
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import anglo_frisian_chronology as chronology
import anglo_frisian_experiments as experiments
from capr_runtime import layout

RECIPES = layout().docs_dir / "sound_changes/literature_dossiers/anglo_frisian/oe_experiment_recipes.json"


class ExperimentTests(unittest.TestCase):
    def setUp(self):
        self.data = experiments.load_recipes(RECIPES)

    def load_modified(self, data):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "recipes.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            return experiments.load_recipes(path)

    def test_citations_have_real_bibliography_keys(self):
        keys = chronology.bibliography_keys(chronology.ROOT / "docs/refs.bib")
        for recipe in self.data["recipes"]:
            for source in recipe["sources"]:
                self.assertIn(source["key"], keys)

    def test_recipe_schema_rejects_duplicate_ids(self):
        self.data["recipes"].append(copy.deepcopy(self.data["recipes"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.load_modified(self.data)

    def test_identity_cannot_make_an_intervention(self):
        self.data["recipes"][0]["insert_rule"] = "AFBad"
        with self.assertRaisesRegex(ValueError, "identity"):
            self.load_modified(self.data)

    def test_science_requires_page_citations(self):
        self.data["recipes"][1]["sources"][0]["pages"] = ""
        with self.assertRaisesRegex(ValueError, "pages"):
            self.load_modified(self.data)

    def test_definition_only_no_io_commands(self):
        for command in ("save stack /usr/app/old_english.bin", "source fsts/germanic.txt", "quit"):
            data = copy.deepcopy(self.data)
            data["recipes"][1]["definitions"] += "\n" + command
            with self.subTest(command=command), self.assertRaisesRegex(ValueError, "non-definition"):
                self.load_modified(data)

    def test_relative_insertion_preserves_other_members(self):
        recipe = self.data["recipes"][1]
        order = ["first", recipe["insert_after"], "last"]
        new = experiments.inserted_order(order, recipe)
        self.assertEqual(new, ["first", recipe["insert_after"], recipe["insert_rule"], "last"])
        self.assertEqual(order, ["first", recipe["insert_after"], "last"])
        self.assertEqual(experiments.inserted_order(order, self.data["recipes"][0]), order)

    def test_missing_duplicate_anchor_or_existing_rule_is_rejected(self):
        recipe = self.data["recipes"][1]
        for order in ([], [recipe["insert_after"]] * 2,
                      [recipe["insert_after"], recipe["insert_rule"]]):
            with self.subTest(order=order), self.assertRaises(ValueError):
                experiments.inserted_order(order, recipe)

    def test_replacement_targets_must_exist_once(self):
        recipe = self.data["recipes"][2]
        anchor = recipe["insert_after"]
        target = next(iter(recipe["replace"]))
        for order in ([anchor], [anchor, target, target]):
            with self.subTest(order=order), self.assertRaisesRegex(ValueError, "replacement"):
                experiments.inserted_order(order, recipe)
        changed = experiments.inserted_order([anchor, target], recipe)
        self.assertEqual(changed[-1], recipe["replace"][target])

    def input_recipe(self):
        return {
            **copy.deepcopy(self.data["recipes"][0]),
            "id": "u-test-input",
            "sources": [{"key": "Ringe2017", "pages": "135,151-153"}],
            "input_overrides": [{"row_id": "2040", "baseline_input": "*géftiz",
                                 "variant_input": "*gíftiz", "input_stage": "pgmc"}],
        }

    def old_input_rows(self):
        rows = experiments.corpus_rows(layout().corpus_tsv)
        gift = next(row for row in rows if row["id"] == "2040")
        gift.update(proto="*géftiz", proto_norm="géftiz", reconstruction="*géftiz")
        return rows

    def test_input_only_recipe_preserves_composition_and_original_rows(self):
        recipe = self.input_recipe()
        self.data["recipes"].append(recipe)
        self.load_modified(self.data)
        order = ["first", "last"]
        self.assertEqual(experiments.inserted_order(order, recipe), order)
        rows = self.old_input_rows()
        original = copy.deepcopy(rows)
        changed = experiments.apply_input_overrides(rows, recipe)
        self.assertEqual(rows, original)
        self.assertEqual([row["id"] for row in changed], [row["id"] for row in rows])
        self.assertEqual([old["id"] for old, new in zip(rows, changed) if old != new], ["2040"])
        gift = next(row for row in changed if row["id"] == "2040")
        self.assertEqual((gift["proto"], gift["proto_norm"], gift["counterpart"]),
                         ("*gíftiz", "gíftiz", "ġift"))
        self.assertEqual(gift["reconstruction"], "*géftiz")

    def test_input_overrides_require_valid_provenance_and_pgmc_stage(self):
        mutations = [
            ("input_overrides", None),
            ("sources", []),
            ("input_stage", "preoe"),
            ("row_id", ""),
            ("variant_input", "***"),
            ("variant_input", "*gíftiz\n*other"),
            ("variant_input", "*gíftiz?"),
            ("variant_input", "*gi\u0301ftiz"),
            ("variant_input", "*géftiz"),
        ]
        for field, value in mutations:
            data = copy.deepcopy(self.data)
            recipe = self.input_recipe()
            if field in {"input_overrides", "sources"}:
                recipe[field] = value
            else:
                recipe["input_overrides"][0][field] = value
            data["recipes"].append(recipe)
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                self.load_modified(data)
        recipe = self.input_recipe()
        recipe["input_overrides"].append(copy.deepcopy(recipe["input_overrides"][0]))
        self.data["recipes"].append(recipe)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.load_modified(self.data)

    def test_identity_cannot_override_inputs(self):
        self.data["recipes"][0]["input_overrides"] = self.input_recipe()["input_overrides"]
        with self.assertRaisesRegex(ValueError, "identity"):
            self.load_modified(self.data)

    def test_input_override_rejects_missing_stale_or_later_stage_rows(self):
        rows = self.old_input_rows()
        for field, value, message in (("row_id", "999999", "missing"),
                                      ("baseline_input", "*gíftiz", "baseline")):
            recipe = self.input_recipe()
            recipe["input_overrides"][0][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, message):
                experiments.apply_input_overrides(rows, recipe)
        later = copy.deepcopy(rows)
        next(row for row in later if row["id"] == "2040")["reconstruction"] = "*different"
        with self.assertRaisesRegex(ValueError, "PROTOFORM == PROTO"):
            experiments.apply_input_overrides(later, self.input_recipe())

    def test_component_checks_reject_bad_names_inputs_and_duplicate_ids(self):
        check = {"id": "split-negative", "component": "AFPDOrd",
                 "input": "*ʧ*e*o*r*l", "expected": "*ʧ*e*o*r*l"}
        for field, value in (("component", "quit;save stack bad"), ("input", "*e\n*w"),
                             ("expected", "*"), ("id", "")):
            data = copy.deepcopy(self.data)
            data["recipes"][1]["component_checks"] = [{**check, field: value}]
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.load_modified(data)
        self.data["recipes"][1]["component_checks"] = [check, copy.deepcopy(check)]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.load_modified(self.data)

    def test_component_checks_are_not_full_cascade_probes(self):
        check = {"id": "split-negative", "component": "AFPDOrd",
                 "input": "*ʧ*e*o*r*l", "expected": "*ʧ*e*o*r*l"}
        bins = {"final": Path("final.bin"), "tap": Path("tap.bin"),
                "component:AFPDOrd": Path("component.bin")}
        with patch.object(experiments, "batch_apply_down", return_value=[["*test"]]) as apply:
            self.assertEqual(experiments.intermediate_outputs(bins, ["test"]), {"tap": [["*test"]]})
            apply.assert_called_once_with(bins["tap"], ["test"])
        recipe = {"component_checks": [check]}
        with patch.object(experiments, "batch_apply_down", return_value=[[check["expected"]]]) as apply:
            self.assertEqual(experiments.check_component_predictions(recipe, bins),
                             [{**check, "outputs": [check["expected"]]}])
            apply.assert_called_once_with(bins["component:AFPDOrd"], [check["input"]])
        for outputs in ([], ["*wrong"], [check["expected"], "*other"]):
            with self.subTest(outputs=outputs), \
                    patch.object(experiments, "batch_apply_down", return_value=[outputs]), \
                    self.assertRaisesRegex(ValueError, "component prediction"):
                experiments.check_component_predictions(recipe, bins)

    def test_invalid_json_field_types_fail_explicitly(self):
        for data in ([], {"schema_version": 1, "recipes": [None]}):
            with self.subTest(data=data), self.assertRaises(ValueError):
                self.load_modified(data)
        for source in ({"key": "Source", "pages": 41}, None):
            data = copy.deepcopy(self.data)
            data["recipes"][1]["sources"] = [source]
            with self.subTest(source=source), self.assertRaises(ValueError):
                self.load_modified(data)

    def test_live_selection_has_all_stable_ids(self):
        rows = experiments.corpus_rows(layout().corpus_tsv)
        self.assertEqual(len(rows), 387)
        self.assertEqual(len({row["id"] for row in rows}), 387)
        self.assertEqual(next(row["proto"] for row in rows if row["id"] == "2061"), "*xáwją")

    def test_fixtures_match_live_inputs_and_recipe_provenance(self):
        with (RECIPES.parent / "oe_diagnostic_fixtures.tsv").open(encoding="utf-8", newline="") as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        with layout().corpus_tsv.open(encoding="utf-8", newline="") as handle:
            corpus = {row["ID"]: row for row in csv.DictReader(handle, delimiter="\t")
                      if row["DOCULECT"] == "Old_English"}
        with (chronology.ROOT / "Germanic/data/entry_stage_metadata.tsv").open(
            encoding="utf-8", newline=""
        ) as handle:
            stages = {row["row_id"]: row["protoform_stage"]
                      for row in csv.DictReader(handle, delimiter="\t")}
        self.assertEqual(len(fixtures), 42)
        self.assertEqual(len({row["fixture_id"] for row in fixtures}), 42)
        self.assertEqual(len({row["row_id"] for row in fixtures}), 25)
        self.assertEqual({row["family"] for row in fixtures}, {"A", "B", "D", "F", "P", "U"})
        self.assertEqual({row["row_id"] for row in fixtures if row["family"] == "D"},
                         {"1976", "1989", "2029", "2074", "2326", "2332", "2061", "2227"})
        keys = chronology.bibliography_keys(chronology.ROOT / "docs/refs.bib")
        recipes = {recipe["id"] for recipe in self.data["recipes"]}
        probes = {probe["id"] for probe in self.data["probes"]}
        with (chronology.ROOT / "Germanic/docs/sound_changes/cascade_baseline/approved_input_migrations.tsv").open(
            encoding="utf-8"
        ) as handle:
            migrations = {row["row_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
        for fixture in fixtures:
            with self.subTest(fixture=fixture["fixture_id"]):
                row = corpus[fixture["row_id"]]
                selected = fixture["selected_input"]
                if fixture["row_id"] in migrations:
                    migration = migrations[fixture["row_id"]]
                    self.assertEqual(selected, migration["old_proto"])
                    self.assertEqual(row["PROTOFORM"], migration["new_proto"])
                else:
                    self.assertEqual(selected, row["PROTOFORM"])
                if row["PROTO"] == row["PROTOFORM"]:
                    self.assertEqual(fixture["input_stage"], "pgmc")
                else:
                    self.assertEqual(fixture["input_stage"], stages[row["ID"]])
                self.assertEqual(fixture["normalized_input"], experiments.oe_pipeline.normalize_proto(selected))
                self.assertEqual(fixture["target"], row["COUNTERPART"])
                self.assertIn(fixture["recipe"], recipes)
                self.assertIn(fixture["probe"], probes)
                self.assertIn(fixture["source_key"], keys)
                self.assertRegex(fixture["printed_pages"], r"^[1-9]\d*(?:-\d+)?(?:,[1-9]\d*(?:-\d+)?)*$")
                if fixture["row_id"] == "2227":
                    self.assertEqual(fixture["target_status"], "reconstructed_oe")
                    self.assertIn("not_attested_positive", fixture["witness_role"])
                if fixture["row_id"] == "2040":
                    self.assertEqual(fixture["target_status"], "selected_input_under_review")
                    self.assertIn("not_endorsed", fixture["readiness"])

    def test_duplicate_ids_and_empty_normalization_are_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "corpus.tsv"
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["ID", "DOCULECT", "CONCEPT", "PROTOFORM", "COUNTERPART"],
                                        delimiter="\t")
                writer.writeheader()
                writer.writerows([{"ID": "1", "DOCULECT": "Old_English", "CONCEPT": "test",
                                   "PROTOFORM": "*test", "COUNTERPART": "test"}] * 2)
            with self.assertRaisesRegex(ValueError, "duplicate"):
                experiments.corpus_rows(path)
            text = path.read_text(encoding="utf-8").splitlines()
            path.write_text("\n".join(text[:2]).replace("*test", "***") + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "empty normalized"):
                experiments.corpus_rows(path)

    def test_runtime_fixture_predictions_require_exact_atomic_states(self):
        fixture = {"fixture_id": "control", "recipe": "identity", "row_id": "1", "probe": "tap",
                   "baseline_prediction": "*éu*w", "variant_prediction": "*éu*w"}
        report = {"recipe": {"id": "identity"}, "rows": [
            {"id": "1", "intermediates": {"tap": {"baseline": ["*éu*w"], "variant": ["*éu*w"]}}}
        ]}
        self.assertEqual(experiments.check_fixture_predictions(report, [fixture]), ["control"])
        for outputs in (["*é*u*w"], [], ["*éu*w", "*é*u*w"]):
            bad = copy.deepcopy(report)
            bad["rows"][0]["intermediates"]["tap"]["variant"] = outputs
            with self.subTest(outputs=outputs), self.assertRaisesRegex(ValueError, "variant prediction"):
                experiments.check_fixture_predictions(bad, [fixture])
        missing = copy.deepcopy(report)
        missing["rows"][0]["intermediates"].clear()
        with self.assertRaisesRegex(ValueError, "probe missing"):
            experiments.check_fixture_predictions(missing, [fixture])
        with self.assertRaisesRegex(ValueError, "row missing"):
            experiments.check_fixture_predictions({"recipe": {"id": "identity"}, "rows": []}, [fixture])
        other = {**fixture, "recipe": "different-recipe"}
        self.assertEqual(experiments.check_fixture_predictions(report, [other]), [])

    def test_probe_compositions_include_full_input_prefix(self):
        identity = self.data["recipes"][0]
        modified = self.data["recipes"][1]
        probes = [{"id": "tap", "stage": "OEWWSimplification", "side": "before"}]
        plain, _ = experiments.probe_appendix(identity, probes)
        variant, _ = experiments.probe_appendix(modified, probes)
        self.assertIn("EnglishProtoInput", plain)
        self.assertIn("PGmcGmSimplification", plain)
        self.assertNotIn("AFVww", plain)
        self.assertIn("AFVww", variant)
        self.assertNotIn(".o. OEWWSimplification", variant)

    def test_all_six_cases_have_paired_incumbent_probes(self):
        probes = {probe["id"]: probe for probe in self.data["probes"]}
        for number in ("004", "030", "031", "032", "033", "034", "043", "044",
                       "045", "046", "051", "052", "055", "056", "057", "098"):
            with self.subTest(component=number):
                before, after = probes[f"before_sc{number}"], probes[f"after_sc{number}"]
                self.assertEqual(before["stage"], after["stage"])
                self.assertEqual((before["side"], after["side"]), ("before", "after"))
        for recipe in self.data["recipes"]:
            appendix, bins = experiments.probe_appendix(recipe, self.data["probes"])
            self.assertEqual(set(bins), set(probes))
            self.assertEqual(len(bins), len(set(bins.values())))
            self.assertIn("EnglishProtoInput", appendix)

    def test_complete_parent_wrappers_are_reused(self):
        original = experiments.parse_english_proto_to_oe_order(layout().germanic_fst)
        expanded = experiments.expand_pwgmc_changes(original, layout().germanic_fst)
        appendix = experiments.build_variant_appendix(expanded, layout().germanic_fst)
        self.assertIn("regex VariantOldEnglish;", appendix)
        self.assertIn("EnglishProtoInput", appendix)
        self.assertIn("EarlyGermanicConsonantPipeline", appendix)
        self.assertIn("OldEnglishSurface", appendix)
        self.assertIn("PWGmcCoronalWAssimilation", appendix)

    def test_host_execution_is_rejected_before_compiling(self):
        with patch.object(experiments, "layout", return_value=layout()), \
                patch.object(experiments, "compile_isolated") as compile_mock:
            with self.assertRaisesRegex(RuntimeError, "backend container"):
                experiments.run(self.data, "identity")
            compile_mock.assert_not_called()

    def test_unsafe_source_destinations_are_rejected_before_foma(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "unsafe.txt"
            for text in ("save stack /usr/app/old_english.bin\n",
                         "save stack ../old_english.bin\n",
                         "source shared.txt\n"):
                source.write_text(text, encoding="utf-8")
                with self.subTest(text=text), patch.object(experiments.subprocess, "run") as runner:
                    with self.assertRaisesRegex(ValueError, "unsafe|includes"):
                        experiments.compile_isolated(source, self.data["recipes"][0],
                                                     self.data["probes"], Path(directory))
                    runner.assert_not_called()


if __name__ == "__main__":
    unittest.main()
