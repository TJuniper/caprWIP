import csv
import hashlib
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import anglo_frisian_experiments as experiments
import generate_registry_views as registry_views
from test_sc043_component_split import definition, rows

DIRECTORY = ROOT / "Germanic/docs/sound_changes/literature_dossiers/anglo_frisian"


class Sc033ComponentResearchTests(unittest.TestCase):
    def test_complete_candidate_changes_only_the_approved_knee_cell(self):
        report = json.loads((DIRECTORY / "oe_sc033_dative_candidate_result.json").read_text())
        data = experiments.load_recipes(DIRECTORY / "oe_sc033_recipes.json")
        self.assertEqual(report["recipe"],
                         next(recipe for recipe in data["recipes"]
                              if recipe["id"] == "sc033-dative-candidate"))
        self.assertTrue(report["identity_equal"])
        self.assertTrue(report["canonical_artifacts_unchanged"])
        self.assertEqual(report["changed_ids"], ["2085"])
        self.assertEqual(report["input_changed_ids"], ["2085"])
        self.assertEqual(report["missing_output_ids"], [])
        self.assertEqual(report["ambiguous_output_ids"], [])
        self.assertEqual(len(report["checked_component_fixtures"]), 10)
        self.assertEqual(len(report["checked_staged_fixtures"]), 2)
        candidate = {row["id"]: row for row in report["rows"]}
        self.assertEqual(candidate["2085"]["variant_outputs"], ["cneowe"])
        self.assertEqual(candidate["2085"]["intermediates"]["after_breaking"]["variant"],
                         ["*k*n*éo*w*ē"])
        for identifier, row in candidate.items():
            if identifier != "2085":
                self.assertEqual(row["baseline_outputs"], row["variant_outputs"], identifier)

    def test_current_knee_cell_class_and_explicit_stages(self):
        selected = next(row for row in experiments.corpus_rows(experiments.layout().corpus_tsv)
                        if row["id"] == "2085")
        self.assertEqual(selected["proto"], "*knéwai")
        self.assertEqual(selected["counterpart"], "cneowe")
        raw = next(row for row in rows(ROOT / "Germanic/data/germanic-aligned-final.tsv")
                   if row["ID"] == "2085")
        self.assertEqual(raw["PROTO"], "*knéwą")
        self.assertEqual(raw["DERIVATION_CLASS"], "late_analogy")
        stages = next(row for row in rows(ROOT / "Germanic/data/entry_stage_metadata.tsv")
                      if row["row_id"] == "2085")
        self.assertEqual(stages["proto_stage"], "pgmc")
        self.assertEqual(stages["protoform_stage"], "pgmc")
        manifest = next(row for row in rows(ROOT / "Germanic/docs/assembly/manifest_late_analogy.tsv")
                        if row["row_id"] == "2085")
        self.assertIn("2085-knee-cneowe.model.md", str(manifest))

    def test_technical_component_remains_published_without_historical_staging(self):
        registry = rows(ROOT / "Germanic/docs/sound_changes/registry/sc_registry.tsv")
        component = next(row for row in registry if row["sc_id"] == "SC033")
        self.assertEqual(component["entry_type"], "support_stage")
        self.assertEqual(component["staging_row"], "no")
        self.assertEqual(component["verdict"], "REFORMULATE/SPLIT")
        for field in ("hist_stage", "hist_scope", "confidence"):
            self.assertEqual(component[field], "")
        chapters, files = registry_views.read_reader_sources()
        manifest = registry_views.build_reader_manifest(registry, chapters, files)
        self.assertIn("033-long-eow-diphthong.md", manifest)
        changed = [dict(row) for row in registry]
        next(row for row in changed if row["sc_id"] == "SC033")["include_in_volume"] = "no"
        with self.assertRaises(SystemExit):
            registry_views.build_reader_manifest(changed, chapters, files)

    def test_changed_reader_definitions_are_exact_production_bodies(self):
        import re
        source = (ROOT / "Germanic/fsts/germanic.txt").read_text()
        reader_dir = ROOT / "Germanic/docs/sound_changes/reader_facing"
        for filename, expected in (
            ("033-long-eow-diphthong.md",
             {"OEEwLongDiphthong", "OEJWWSimplification", "OEJGlideIO"}),
            ("044-045-breaking-and-velar-fricative-palatalization.md",
             {"EnglishBreakingWContext"}),
        ):
            found = set()
            for block in re.findall(r"```foma\n([\s\S]*?)```", (reader_dir / filename).read_text()):
                names = re.findall(r"\bdefine (\w+)", block)
                self.assertEqual(len(names), 1)
                name = names[0]
                if name in expected:
                    found.add(name)
                    self.assertEqual(re.sub(r"\s+", "", definition(block, name)),
                                     re.sub(r"\s+", "", definition(source, name)))
            self.assertEqual(found, expected)

    def test_post_hue_controls_match_current_sources_and_preserve_palatal_assertions(self):
        data = experiments.load_recipes(DIRECTORY / "oe_post_hue_controls.json")
        self.assertEqual(data["baseline_fst_sha256"],
                         hashlib.sha256((ROOT / "Germanic/fsts/germanic.txt").read_bytes()).hexdigest())
        self.assertEqual(data["baseline_corpus_sha256"],
                         hashlib.sha256(experiments.layout().corpus_tsv.read_bytes()).hexdigest())
        historical = experiments.load_recipes(DIRECTORY / "oe_adopted_palatal_controls.json")
        for field in ("component_checks", "staged_checks"):
            self.assertTrue(all(check in data["recipes"][1][field]
                                for check in historical["recipes"][1][field]))

    def test_executed_production_controls_protect_all_selected_finals(self):
        data = experiments.load_recipes(DIRECTORY / "oe_post_sc033_controls.json")
        report = json.loads((DIRECTORY / "oe_post_sc033_result.json").read_text())
        self.assertEqual(report["recipe"], data["recipes"][1])
        self.assertTrue(report["identity_equal"])
        self.assertTrue(report["canonical_artifacts_unchanged"])
        self.assertEqual(report["selected_rows"], 387)
        for field in ("changed_ids", "input_changed_ids", "missing_output_ids",
                      "ambiguous_output_ids"):
            self.assertEqual(report[field], [])
        self.assertEqual(report["baseline_mismatch_ids"], report["variant_mismatch_ids"])
        self.assertEqual(report["baseline_mismatch_ids"],
                         ["1973", "2013", "2030", "2162", "2240", "2298", "2300"])
        self.assertEqual(len(report["checked_component_fixtures"]), 49)
        self.assertEqual(len(report["checked_staged_fixtures"]), 9)
        self.assertEqual(len(report["checked_fixture_ids"]), 10)
        with (DIRECTORY / data["fixture_file"]).open() as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(experiments.check_fixture_predictions(report, fixtures),
                         report["checked_fixture_ids"])
        selected = {row["id"]: row for row in
                    experiments.corpus_rows(experiments.layout().corpus_tsv)}
        with (ROOT / "Germanic/docs/sound_changes/cascade_baseline/"
              "cascade_baseline_outputs_pre_sc033_hue.tsv").open() as handle:
            historical = {row["row_id"]: row for row in csv.DictReader(handle, delimiter="\t")}
        self.assertEqual({row["id"] for row in report["rows"]}, set(selected))
        for row in report["rows"]:
            self.assertEqual(row["variant_fst_input"],
                             historical[row["id"]]["fst_input"])
            self.assertEqual(row["variant_outputs"], historical[row["id"]]["outputs"].split("|"))
            self.assertEqual(row["variant_outputs"], row["baseline_outputs"])
        knee = next(row for row in report["rows"] if row["id"] == "2085")
        self.assertEqual(knee["variant_outputs"], ["cneowe"])
        self.assertTrue(knee["variant_match"])

    def test_recipe_and_persisted_report_agree(self):
        data = experiments.load_recipes(DIRECTORY / "oe_sc033_recipes.json")
        report = json.loads((DIRECTORY / "oe_sc033_singleton_short_result.json").read_text())
        recipe = next(row for row in data["recipes"] if row["id"] == report["recipe"]["id"])
        self.assertEqual(recipe, report["recipe"])
        self.assertTrue(report["identity_equal"])
        self.assertTrue(report["canonical_artifacts_unchanged"])
        self.assertEqual(report["selected_rows"], 387)
        for field in ("input_changed_ids", "missing_output_ids", "ambiguous_output_ids"):
            self.assertEqual(report[field], [], field)
        self.assertEqual(len(report["checked_component_fixtures"]), 8)
        self.assertEqual(len(report["checked_staged_fixtures"]), 3)
        with (DIRECTORY / data["fixture_file"]).open() as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(experiments.check_fixture_predictions(report, fixtures),
                         report["checked_fixture_ids"])

    def test_partial_quantity_counterfactual_is_not_a_target_migration(self):
        report = json.loads((DIRECTORY / "oe_sc033_singleton_short_result.json").read_text())
        self.assertEqual(report["changed_ids"], ["2085"])
        self.assertEqual(report["baseline_mismatch_ids"],
                         ["1973", "2013", "2030", "2162", "2240", "2298", "2300"])
        self.assertEqual(set(report["variant_mismatch_ids"]),
                         set(report["baseline_mismatch_ids"]) | {"2085"})
        rows = {row["id"]: row for row in report["rows"]}
        self.assertEqual(rows["2085"]["baseline_outputs"], ["cnēow"])
        self.assertEqual(rows["2085"]["variant_outputs"], ["cneow"])
        self.assertEqual(rows["2085"]["intermediates"]["after_breaking"]["variant"],
                         ["*k*n*éo*w*ą"])
        self.assertEqual(rows["2332"]["variant_outputs"], ["hīew"])
        for row in report["rows"]:
            if row["id"] != "2085":
                self.assertEqual(row["baseline_outputs"], row["variant_outputs"], row["id"])

    def test_regular_oblique_suffixes_do_not_migrate_the_selected_row(self):
        data = experiments.load_recipes(DIRECTORY / "oe_sc033_recipes.json")
        report = json.loads((DIRECTORY / "oe_sc033_oblique_cells_result.json").read_text())
        recipe = next(row for row in data["recipes"] if row["id"] == report["recipe"]["id"])
        self.assertEqual(recipe, report["recipe"])
        self.assertTrue(report["identity_equal"])
        self.assertTrue(report["canonical_artifacts_unchanged"])
        self.assertEqual(report["selected_rows"], 387)
        self.assertEqual(report["changed_ids"], ["2085"])
        for field in ("input_changed_ids", "missing_output_ids", "ambiguous_output_ids"):
            self.assertEqual(report[field], [], field)
        self.assertEqual(len(report["checked_component_fixtures"]), 2)
        checks = {check["id"]: check for check in report["checked_staged_fixtures"]}
        expected = {
            "regular-knee-dative-native": ("*k*n*é*w*ai", "cneowe"),
            "regular-knee-genitive-native": ("*k*n*é*w*a*s", "cneowes"),
        }
        self.assertEqual(set(checks), set(expected))
        for identifier, (encoded_input, native_output) in expected.items():
            check = checks[identifier]
            self.assertEqual(check["stage"], "EnglishProtoInput")
            self.assertEqual(check["side"], "after")
            self.assertEqual(check["input"], encoded_input)
            self.assertEqual(check["outputs"], [native_output])
            self.assertEqual(check["expected"], native_output)
            self.assertTrue(check["evidence"])
        rows = {row["id"]: row for row in report["rows"]}
        self.assertEqual(rows["2085"]["baseline_outputs"], ["cnēow"])
        self.assertEqual(rows["2085"]["variant_outputs"], ["cneow"])
        for row in report["rows"]:
            if row["id"] != "2085":
                self.assertEqual(row["baseline_outputs"], row["variant_outputs"], row["id"])


if __name__ == "__main__":
    unittest.main()
