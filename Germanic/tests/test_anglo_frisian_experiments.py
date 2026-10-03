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

    def test_fixture_file_and_baseline_hashes_are_validated(self):
        for filename in ("../fixtures.tsv", "/tmp/fixtures.tsv", "", None):
            with self.subTest(filename=filename), self.assertRaisesRegex(ValueError, "fixture_file"):
                self.load_modified({**self.data, "fixture_file": filename})
        for field in ("baseline_fst_sha256", "baseline_corpus_sha256"):
            for value in ("bad", None, "A" * 64):
                with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, field):
                    self.load_modified({**self.data, field: value})

    def test_post_gift_controls_preserve_their_distinct_historical_baseline(self):
        path = RECIPES.with_name("oe_adopted_u_controls.json")
        data = experiments.load_recipes(path)
        self.assertEqual(data["baseline_fst_sha256"],
                         "8437fb2b64289140458d895d7d1e24592df920960b74c5e781ca6791ff9cc47b")
        self.assertEqual(data["baseline_corpus_sha256"],
                         "a08df28912bd957452fdcbe83d49ee398cd21db171c0f85113f7d6ca575a5ac8")
        self.assertNotEqual(data["fixture_file"], "oe_diagnostic_fixtures.tsv")
        with path.with_name(data["fixture_file"]).open(encoding="utf-8", newline="") as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(len(fixtures), 12)
        self.assertEqual(len({f["fixture_id"] for f in fixtures}), 12)
        corpus = {row["id"]: row for row in experiments.corpus_rows(layout().corpus_tsv)}
        keys = chronology.bibliography_keys(chronology.ROOT / "docs/refs.bib")
        for fixture in fixtures:
            row = corpus[fixture["row_id"]]
            self.assertEqual((fixture["selected_input"], fixture["normalized_input"], fixture["target"]),
                             (row["proto"], row["proto_norm"], row["counterpart"]))
            self.assertIn(fixture["source_key"], keys)
            self.assertRegex(fixture["printed_pages"], r"^\d+(?:[-,]\d+)*$")
        self.assertEqual({f["row_id"] for f in fixtures}, {"2040", "2049", "2178"})

    def test_post_glide_controls_preserve_the_released_context_contract(self):
        path = RECIPES.with_name("oe_adopted_glide_controls.json")
        data = experiments.load_recipes(path)
        self.assertEqual(data["baseline_fst_sha256"],
                         "9016feefda56ca204cb71b8d426f1ace2486bbbd4d2334dc8440dce5cef811d0")
        for field, source in (
            ("baseline_corpus_sha256", layout().corpus_tsv),
            ("baseline_context_sha256", layout().data_dir / "entry_context_metadata.tsv"),
            ("baseline_context_helper_sha256", layout().bin_dir / "oe_input_context.py"),
        ):
            self.assertEqual(data[field], experiments.digest(source))
        recipe = data["recipes"][1]
        self.assertEqual(len(recipe["component_checks"]), 49)
        self.assertEqual(len(recipe["staged_checks"]), 7)
        with path.with_name(data["fixture_file"]).open(encoding="utf-8") as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(len(fixtures), 28)
        self.assertTrue(all(row["baseline_prediction"] == row["variant_prediction"] for row in fixtures))

    def test_identity_cannot_make_an_intervention(self):
        self.data["recipes"][0]["insert_rule"] = "AFBad"
        with self.assertRaisesRegex(ValueError, "identity"):
            self.load_modified(self.data)

    def test_private_phonetic_alphabet_requires_real_single_codepoints(self):
        for symbols in (["a\u0304"], ["ʝ", "ʝ"], ["3"], [None], [{}], "ʝ"):
            data = copy.deepcopy(self.data)
            data["recipes"][1]["phonetic_symbols"] = symbols
            with self.subTest(symbols=symbols), self.assertRaisesRegex(
                    ValueError, "phonetic symbols"):
                self.load_modified(data)
        data = copy.deepcopy(self.data)
        data["recipes"][1]["phonetic_symbols"] = ["ɟ"]
        recipe = self.load_modified(data)["recipes"][1]
        source = layout().germanic_fst.read_text()
        extended = experiments.context_source_text(source, recipe)
        self.assertIn("define EnglishPalatalConsonant [{*ɟ} | ", extended)
        self.assertNotIn("{*ɟ}", source)

    def test_staged_phonetic_checkpoint_stops_before_native_surface(self):
        recipe = {
            "replace": {}, "definitions": "", "insert_rule": "", "insert_after": "",
            "staged_checks": [{"id": "mutation", "stage": "OEVelarPalatalization",
                              "side": "before", "stop_after": "OEIUmlaut"}],
        }
        script, bins = experiments.staged_appendix(recipe)
        self.assertIn("OEIUmlaut;", script)
        self.assertNotIn("OldEnglishOrthography", script)
        self.assertIn("staged:mutation", bins)
        recipe["staged_checks"][0]["stop_after"] = "EAFBrightening"
        with self.assertRaisesRegex(ValueError, "precedes entry"):
            experiments.staged_appendix(recipe)

    def test_relative_edits_cover_the_derived_outer_wrapper(self):
        recipe = {"id": "outer", "definitions": "", "insert_after": "OELateUnstressedAgSuffix",
                  "insert_rule": "AFMerge", "replace": {"OELateUnstressedAgSuffix": "AFSuffix"}}
        order = experiments.complete_variant_order(recipe)
        self.assertEqual(order[order.index("AFSuffix") + 1], "AFMerge")
        self.assertLess(order.index("AFMerge"), order.index("OldEnglishOrthography"))

    def test_post_ai_fronting_recipe_preserves_its_historical_baseline(self):
        path = RECIPES.with_name("oe_post_ai_fronting_recipes.json")
        data = experiments.load_recipes(path)
        self.assertEqual(data["baseline_fst_sha256"],
                         "e252dece8c775a3ef544fc5006f0d899f8cc52ed4edb250b61d4b9fa75337241")
        for field, source in (
            ("baseline_corpus_sha256", layout().corpus_tsv),
            ("baseline_context_sha256", layout().data_dir / "entry_context_metadata.tsv"),
            ("baseline_context_helper_sha256", layout().bin_dir / "oe_input_context.py"),
        ):
            self.assertEqual(data[field], experiments.digest(source))
        recipe = data["recipes"][1]
        self.assertEqual(recipe["insert_after"], "EAFBrightening")
        self.assertEqual(set(recipe["replace"]),
                         {"OEAuBrightening", "OEDiphthongLeveling"})
        original = [stage.inline_text if stage.kind == "inline" else stage.foma_identifier
                    for stage in experiments.oe_pipeline.stages()]
        variant = experiments.complete_variant_order(recipe)
        retained = [stage for stage in original if stage not in recipe["replace"]]
        self.assertEqual(
            [stage for stage in variant
             if stage not in set(recipe["replace"].values()) | {recipe["insert_rule"]}],
            retained)
        self.assertLess(variant.index("AFFront"), variant.index("OEBreaking"))
        self.assertEqual(variant.index("AFFront"), variant.index("EAFBrightening") + 1)
        with path.with_name(data["fixture_file"]).open(encoding="utf-8") as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(len(fixtures), 30)
        self.assertEqual(len({row["fixture_id"] for row in fixtures}), 30)
        self.assertTrue({"1966", "1985", "1989", "2074", "2089", "2220",
                         "2061", "2227", "2326", "2040", "2049", "2178"}
                        <= {row["row_id"] for row in fixtures})

    def test_measured_fronting_variant_converges_without_input_or_final_drift(self):
        path = RECIPES.with_name("oe_post_ai_fronting_recipes.json")
        data = experiments.load_recipes(path)
        report = json.loads(path.with_name("oe_post_ai_fronting_result.json").read_text())
        self.assertEqual(report["selected_rows"], 387)
        self.assertTrue(report["identity_equal"])
        self.assertTrue(report["canonical_artifacts_unchanged"])
        for field in ("changed_ids", "input_changed_ids", "missing_output_ids",
                      "ambiguous_output_ids"):
            self.assertEqual(report[field], [])
        self.assertEqual(report["baseline_mismatch_ids"], report["variant_mismatch_ids"])
        self.assertEqual(len(report["baseline_mismatch_ids"]), 7)
        live = {row["id"]: row for row in experiments.corpus_rows(layout().corpus_tsv)}
        self.assertEqual({row["id"] for row in report["rows"]}, set(live))
        for row in report["rows"]:
            self.assertEqual(row["variant_fst_input"],
                             experiments.oe_pipeline.evaluation_input(live[row["id"]]))
            self.assertEqual(row["baseline_outputs"], row["variant_outputs"])
            self.assertEqual(len(row["variant_outputs"]), 1)
        for probe, count in (("after_sc030", 20), ("after_sc032", 20),
                             ("before_fronting", 20), ("after_fronting", 0),
                             ("after_ordinary", 0), ("after_mutation", 0),
                             ("after_late", 0)):
            changed = [row for row in report["rows"]
                       if row["intermediates"][probe]["baseline"]
                       != row["intermediates"][probe]["variant"]]
            self.assertEqual(len(changed), count, probe)
            if count:
                self.assertTrue({"1989", "2074"} <= {row["id"] for row in changed})
        with path.with_name(data["fixture_file"]).open(encoding="utf-8") as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        checked = experiments.check_fixture_predictions(
            {**report, "recipe": data["recipes"][1]}, fixtures)
        self.assertEqual(checked, report["checked_fixture_ids"])

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

    def coupled_recipe(self):
        data = experiments.load_recipes(RECIPES.with_name("oe_glide_apocope_recipes.json"))
        return data, data["recipes"][1]

    def test_context_annotation_preserves_reconstruction_and_original_rows(self):
        _, recipe = self.coupled_recipe()
        rows = experiments.corpus_rows(layout().corpus_tsv)
        original = copy.deepcopy(rows)
        annotated = experiments.apply_context_overrides(rows, recipe)
        self.assertEqual(rows, original)
        self.assertEqual([row["id"] for row in annotated], [row["id"] for row in rows])
        changes = [(old, new) for old, new in zip(rows, annotated)
                   if old["fst_input"] != new["fst_input"]]
        self.assertEqual(changes, [])
        strong_you = next(row for row in rows if row["id"] == "2326")
        strong_you.update(fst_input=strong_you["proto_norm"], word_stress="stressed")
        annotated = experiments.apply_context_overrides(rows, recipe)
        changes = [(old, new) for old, new in zip(rows, annotated)
                   if old["fst_input"] != new["fst_input"]]
        self.assertEqual([old["id"] for old, _ in changes], ["2326"])
        old, new = changes[0]
        self.assertEqual((new["proto"], new["reconstruction"]), (old["proto"], old["reconstruction"]))
        self.assertEqual(new["proto_norm"], "ízwiz")
        self.assertEqual(new["fst_input"], "ᵘízwiz")
        self.assertEqual(new["input_context"],
                         {"word_stress": "unstressed", "phonological_finality": "final"})

    def test_context_is_independent_of_lexical_accent_and_identity(self):
        for form in ("ízwiz", "fūri", "gástiz"):
            for stress, finality, prefix in (
                ("stressed", "final", ""), ("unstressed", "final", "ᵘ"),
                ("unstressed", "nonfinal", "ᶜ"),
            ):
                with self.subTest(form=form, stress=stress, finality=finality):
                    context = {"word_stress": stress, "phonological_finality": finality}
                    self.assertEqual(experiments.encode_context(form, context), prefix + form)
        for context in (
            {"word_stress": "unknown", "phonological_finality": "final"},
            {"word_stress": "stressed", "phonological_finality": "unknown"},
            {"word_stress": "stressed", "phonological_finality": "nonfinal"},
        ):
            with self.subTest(context=context), self.assertRaises(ValueError):
                experiments.encode_context("fūri", context)
        with self.assertRaisesRegex(ValueError, "unannotated"):
            experiments.encode_context("ᵘízwiz",
                                       {"word_stress": "unstressed", "phonological_finality": "final"})

    def test_context_overrides_fail_on_missing_or_stale_identity(self):
        _, recipe = self.coupled_recipe()
        rows = experiments.corpus_rows(layout().corpus_tsv)
        for field, value, message in (("row_id", "999999", "missing"),
                                      ("baseline_input", "*wrong", "baseline")):
            modified = copy.deepcopy(recipe)
            modified["context_overrides"][0][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, message):
                experiments.apply_context_overrides(rows, modified)

    def test_context_schema_requires_explicit_convention_and_input_adapter(self):
        data, _ = self.coupled_recipe()
        for field, value in (
            ("citation_context", None),
            ("citation_context", {"word_stress": "unknown", "phonological_finality": "final"}),
            ("input_replacement", ""),
            ("input_replacement", "quit"),
            ("context_overrides", None),
        ):
            modified = copy.deepcopy(data)
            modified["recipes"][1][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.load_modified(modified)
        modified = copy.deepcopy(data)
        modified["recipes"][1]["context_overrides"] *= 2
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.load_modified(modified)

    def test_input_adapter_is_mirrored_into_final_and_all_prefix_probes(self):
        data, recipe = self.coupled_recipe()
        original = experiments.complete_variant_order(recipe)
        order, definitions = experiments.context_lifted_order(recipe, original)
        probes, _ = experiments.probe_appendix(recipe, data["probes"])
        self.assertEqual(order[0], "AFInput")
        self.assertEqual(order[-1], "OldEnglishSurface")
        self.assertIn(".o. PWGmcCoronalWAssimilation", definitions)
        self.assertIn(".o. AFVww", definitions)
        self.assertNotIn(".o. AFIAp", definitions)
        self.assertIn("[EnglishStarAlphabet - [{*ᵘ}|{*ᶜ}]]* .o.", definitions)
        stop = original.index("AFIAp")
        self.assertEqual(order[stop:], original[stop:])
        self.assertNotIn("EnglishProtoInput", probes)
        self.assertEqual(probes.count(" AFInput\n"), len(data["probes"]))

    def test_staged_checks_use_derived_suffix_not_pgmc_prefix(self):
        _, recipe = self.coupled_recipe()
        appendix, bins = experiments.staged_appendix(recipe)
        self.assertEqual(len(bins), len(recipe["staged_checks"]))
        self.assertIn("define AFS00 AFIAp", appendix)
        self.assertIn("OEIUmlaut", appendix)
        self.assertIn("OldEnglishRemoveStars", appendix)
        self.assertIn("OldEnglishSurface", appendix)
        self.assertNotIn("EnglishProtoInput", appendix)
        self.assertNotIn("AFInput", appendix)
        self.assertNotIn("EarlyGermanicConsonantPipeline", appendix)
        self.assertNotIn(".o. PWGmcCoronalWAssimilation", appendix)
        bad = copy.deepcopy(recipe)
        bad["staged_checks"][0]["stage"] = "NoSuchCheckpoint"
        with self.assertRaisesRegex(ValueError, "missing"):
            experiments.staged_appendix(bad)

    def test_staged_checks_share_only_identical_derived_suffixes(self):
        _, recipe = self.coupled_recipe()
        appendix, bins = experiments.staged_appendix(recipe)
        self.assertEqual(len(bins), len(recipe["staged_checks"]))
        self.assertEqual(len(set(bins.values())), 2)
        self.assertEqual(appendix.count("define AFS"), 2)
        self.assertEqual(bins["staged:and-source-selected-sandhi"],
                         bins["staged:around-source-proclitic"])
        self.assertNotEqual(bins["staged:and-source-selected-sandhi"],
                            bins["staged:homorganic-source-suffix"])
        changed = copy.deepcopy(recipe)
        changed["staged_checks"][1]["side"] = "after"
        appendix, bins = experiments.staged_appendix(changed)
        self.assertEqual(appendix.count("define AFS"), 3)
        self.assertNotEqual(bins["staged:and-source-selected-sandhi"],
                            bins["staged:around-source-proclitic"])

    def test_staged_checks_fail_on_wrong_missing_or_ambiguous_outputs(self):
        check = {"id": "and", "input": "*ᵘ*a*n*d*i", "expected": "and"}
        bins = {"staged:and": Path("staged.bin")}
        with patch.object(experiments, "batch_apply_down", return_value=[["and"]]):
            self.assertEqual(experiments.check_staged_predictions({"staged_checks": [check]}, bins),
                             [{**check, "outputs": ["and"]}])
        for outputs in ([], ["wrong"], ["and", "other"]):
            with self.subTest(outputs=outputs), \
                    patch.object(experiments, "batch_apply_down", return_value=[outputs]), \
                    self.assertRaisesRegex(ValueError, "staged prediction"):
                experiments.check_staged_predictions({"staged_checks": [check]}, bins)
        with patch.object(experiments, "batch_apply_down", return_value=[["*state"]]) as apply:
            self.assertEqual(experiments.intermediate_outputs(
                {"tap": Path("tap.bin"), **bins}, ["form"]), {"tap": [["*state"]]})
            apply.assert_called_once()

    def test_staged_schema_rejects_unsafe_or_duplicate_entries(self):
        data, _ = self.coupled_recipe()
        for field, value in (("stage", "quit;"), ("side", "middle"), ("input", "andi"),
                             ("evidence", ""), ("expected", None)):
            modified = copy.deepcopy(data)
            modified["recipes"][1]["staged_checks"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                self.load_modified(modified)
        modified = copy.deepcopy(data)
        modified["recipes"][1]["staged_checks"] *= 2
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.load_modified(modified)

    def test_context_audit_reports_eligible_forms_not_just_selected_you(self):
        _, recipe = self.coupled_recipe()
        contexts = [
            {"word_stress": "unstressed", "phonological_finality": "final"},
            {"word_stress": "stressed", "phonological_finality": "final"},
        ]
        rows = [{"id": "2326", "concept": "you", "input_context": contexts[0]},
                {"id": "2000", "concept": "fire", "input_context": contexts[1]}]
        states = {"before_sc098": [["*ᵘ*íu*w*i"], ["*f*ū*r*i"]]}
        bins = {"component:AFIAp": Path("apocope.bin")}
        outputs = [
            [["*íu*w*i"], ["*f*ū*r*i"]],
            [["*íu*w"], ["*f*ū*r"]],
            [["*íu*w*i*ᶜ"], ["*f*ū*r*i*ᶜ"]],
        ]
        with patch.object(experiments, "batch_apply_down", side_effect=outputs):
            audit = experiments.audit_context_domain(recipe, bins, states, rows)
        self.assertEqual([record["row_id"] for record in audit], ["2326", "2000"])
        self.assertEqual(audit[1]["selected_context"], contexts[1])
        self.assertEqual(audit[1]["unstressed_final_output"], "*f*ū*r")
        for position, bad in (
            (0, [["*íu*w"], ["*f*ū*r*i"]]),
            (1, [["*íu*w", "*other"], ["*f*ū*r"]]),
            (2, [["*íu*w*ᶜ"], ["*f*ū*r*i*ᶜ"]]),
        ):
            altered = copy.deepcopy(outputs)
            altered[position] = bad
            with self.subTest(position=position), \
                    patch.object(experiments, "batch_apply_down", side_effect=altered), \
                    self.assertRaisesRegex(ValueError, "context audit"):
                experiments.audit_context_domain(recipe, bins, states, rows)

    def test_context_audit_schema_rejects_unchecked_component_or_missing_probe(self):
        data, _ = self.coupled_recipe()
        for field, value in (("component", "NoSuchComponent"), ("probe", "no_such_probe")):
            modified = copy.deepcopy(data)
            modified["recipes"][1]["context_audit"][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "context audit"):
                self.load_modified(modified)

    def test_component_only_assay_does_not_build_candidate_root_or_probes(self):
        data, recipe = self.coupled_recipe()
        components = sorted({check["component"] for check in recipe["component_checks"]})
        with tempfile.TemporaryDirectory() as directory:
            def fake_compile(args, *, cwd, **kwargs):
                text = (Path(cwd) / "experiment.foma").read_text(encoding="utf-8")
                self.assertNotIn("define AFContextRoot", text)
                self.assertNotIn("define AFT00", text)
                self.assertNotIn("define AFS00", text)
                self.assertIn("define AFK001", text)
                for number in range(len(components)):
                    (Path(cwd) / f"af_component_{number:02d}.bin").write_bytes(b"test")
                return experiments.subprocess.CompletedProcess(args, 0, "", "")
            with patch.object(experiments.subprocess, "run", side_effect=fake_compile):
                bins = experiments.compile_isolated(
                    layout().germanic_fst, recipe, data["probes"], Path(directory), components_only=True,
                )
            self.assertEqual(set(bins), {f"component:{component}" for component in components})

    def test_alphabet_extension_is_private_and_does_not_make_mark_a_segment(self):
        data, recipe = self.coupled_recipe()
        source = layout().germanic_fst.read_text(encoding="utf-8")
        extended = experiments.context_source_text(source, recipe)
        self.assertEqual(extended.count("define EnglishStarAlphabet [\n    {*ᶜ} |"), 1)
        self.assertEqual(experiments.context_source_text(source, data["recipes"][0]), source)
        self.assertEqual(layout().germanic_fst.read_text(encoding="utf-8"), source)
        for text in ("", source + source):
            with self.subTest(text_length=len(text)), self.assertRaisesRegex(ValueError, "alphabet anchor"):
                experiments.context_source_text(text, recipe)

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
