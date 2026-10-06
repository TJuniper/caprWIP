import csv
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import anglo_frisian_experiments as experiments
import cascade_baseline

DIRECTORY = ROOT / "Germanic/docs/sound_changes/literature_dossiers/anglo_frisian"


class HueSourceResearchTests(unittest.TestCase):
    def test_research_preserves_its_historical_pins_and_adopted_input_is_explicit(self):
        data = experiments.load_recipes(DIRECTORY / "oe_hue_recipes.json")
        self.assertEqual(
            data["baseline_fst_sha256"],
            "235fb9cf07cf40d0e00181c2959b7ada5c2852c85d231b6c1caa3dccad3074f9",
        )
        self.assertEqual(
            data["baseline_corpus_sha256"],
            "0c3646e37e872bb0f386bf988b1ef032f2104546ad3dde8d43113ec87201bc89",
        )
        hue = next(
            row for row in experiments.corpus_rows(experiments.layout().corpus_tsv)
            if row["id"] == "2332"
        )
        self.assertEqual(hue["proto"], "*xíwją")
        self.assertEqual(hue["counterpart"], "hīew")

    def test_persisted_reports_prove_input_and_intermediate_changes_not_final_drift(self):
        data = experiments.load_recipes(DIRECTORY / "oe_hue_recipes.json")
        recipes = {recipe["id"]: recipe for recipe in data["recipes"]}
        with (DIRECTORY / data["fixture_file"]).open() as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        for name in ("inherited_i", "source_chain"):
            with self.subTest(report=name):
                report = json.loads((DIRECTORY / f"oe_hue_{name}_result.json").read_text())
                self.assertEqual(report["recipe"], recipes[report["recipe"]["id"]])
                self.assertTrue(report["identity_equal"])
                self.assertTrue(report["canonical_artifacts_unchanged"])
                self.assertEqual(report["selected_rows"], 387)
                self.assertEqual(len(report["rows"]), 387)
                self.assertEqual(
                    {row["id"] for row in report["rows"]},
                    {row["id"] for row in experiments.corpus_rows(
                        experiments.layout().corpus_tsv
                    )},
                )
                self.assertEqual(report["input_changed_ids"], ["2332"])
                for field in ("changed_ids", "missing_output_ids", "ambiguous_output_ids"):
                    self.assertEqual(report[field], [])
                self.assertEqual(report["baseline_mismatch_ids"], report["variant_mismatch_ids"])
                self.assertEqual(
                    report["baseline_mismatch_ids"],
                    ["1973", "2013", "2030", "2162", "2240", "2298", "2300"],
                )
                self.assertEqual(
                    experiments.check_fixture_predictions(report, fixtures),
                    report["checked_fixture_ids"],
                )
                for row in report["rows"]:
                    self.assertEqual(row["baseline_outputs"], row["variant_outputs"])
                    self.assertEqual(
                        set(row["intermediates"]),
                        {probe["id"] for probe in data["probes"]},
                    )
                    if row["id"] != "2332":
                        for probe, states in row["intermediates"].items():
                            self.assertEqual(
                                states["baseline"], states["variant"],
                                f"{row['id']} changed at {probe}",
                            )
                hue = next(row for row in report["rows"] if row["id"] == "2332")
                self.assertEqual(hue["variant_proto"], "*xíwją")
                self.assertEqual(hue["variant_outputs"], ["hīew"])
                if name == "source_chain":
                    self.assertEqual(
                        hue["intermediates"]["after_sc033"]["variant"], ["*x*íu*w*j*ą"]
                    )
                    self.assertEqual(
                        hue["intermediates"]["after_realization"]["variant"],
                        ["*x*īo*w*j*ą"],
                    )
                    self.assertEqual(
                        hue["intermediates"]["after_mutation"]["variant"], ["*ç*īe*w*j"]
                    )
                    self.assertEqual(len(report["checked_component_fixtures"]), 19)
                    self.assertEqual(len(report["checked_staged_fixtures"]), 4)

    def test_proposed_input_projection_preserves_original380_without_adopting_it(self):
        report = json.loads((DIRECTORY / "oe_hue_source_chain_result.json").read_text())
        candidate = [
            dict(
                row, proto=row["variant_proto"], proto_norm=row["variant_proto_norm"],
                fst_input=row["variant_fst_input"], outputs="|".join(row["variant_outputs"]),
                accepted="1" if row["variant_outputs"] else "0",
                output_count=str(len(row["variant_outputs"])),
                match="1" if row["variant_match"] else "0",
            )
            for row in report["rows"]
        ]
        self.assertEqual(
            cascade_baseline.projection_sha256(candidate, "fst_input"),
            "47a901e9e4a7cd663b8eb574b87fe737382e8fc1b4f1bc8afc38701af0c96872",
        )
        self.assertEqual(
            cascade_baseline.projection_sha256(candidate, "proto_norm"),
            "90789094b8d8889bb478dd6077de75e1d8e1cb66b7b6d347b63e73a83d039c47",
        )
        baseline = ROOT / "Germanic/docs/sound_changes/cascade_baseline"
        with (baseline / "cascade_baseline_outputs_legacy380.tsv").open() as handle:
            legacy = list(csv.DictReader(handle, delimiter="\t"))
        with (baseline / "approved_input_migrations.tsv").open() as handle:
            migrations = list(csv.DictReader(handle, delimiter="\t"))
        self.assertFalse(any(row["concept"] == "hue" for row in legacy))
        self.assertEqual(
            cascade_baseline.projection_sha256(
                cascade_baseline.legacy_subset(candidate, legacy, migrations), "proto_norm",
            ),
            "70bdaba537d8f6b6bb7d872d00eefbef75127d2d77689af7ba01b35a79ebce39",
        )
        summary = json.loads((baseline / "cascade_baseline_summary_pre_sc033_hue.json").read_text())
        self.assertEqual(
            summary["outputs_sha256"],
            "ffad47aefc01423953fc57784fe6a6f6cef31dcca9bbdbb7b36b06a63dc552bc",
        )

    def test_source_coverage_preserves_dictionary_alternatives_and_fulk_objection(self):
        data = experiments.load_recipes(DIRECTORY / "oe_hue_recipes.json")
        candidate = next(recipe for recipe in data["recipes"]
                         if recipe["id"] == "hue-source-chain")
        sources = {source["key"]: source["pages"] for source in candidate["sources"]}
        self.assertEqual(sources["Orel2003"], "171-172")
        self.assertEqual(sources["Kroonen2013"], "224")
        self.assertIn("250", sources["RingeTaylor2014"])
        self.assertIn("71-72", sources["Fulk2018"])
        self.assertIn("phonemic", candidate["assumptions"])
        self.assertIn("disputes", candidate["limitations"])


if __name__ == "__main__":
    unittest.main()
