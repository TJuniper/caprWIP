from __future__ import annotations

import hashlib
import json
import re
import unittest

from test_sc043_component_split import SC, SOURCE, definition, rows
import oe_pipeline


def compact(text, name):
    return re.sub(r"\s+", "", definition(text, name))


class PalatalClassSplitTests(unittest.TestCase):
    def test_current_controls_are_distinct_from_historical_recipes(self):
        directory = SC / "literature_dossiers/anglo_frisian"
        current = json.loads((directory / "oe_adopted_palatal_controls.json").read_text())
        historical = json.loads((directory / "oe_palatal_class_recipes.json").read_text())
        self.assertEqual(current["baseline_fst_sha256"],
                         "38213e869276ef5887316553a20bf3f018ee5eace66819dee6bfb4b817ba7cc7")
        knee = json.loads((directory / "oe_post_sc033_controls.json").read_text())
        self.assertEqual(knee["baseline_fst_sha256"],
                         "235fb9cf07cf40d0e00181c2959b7ada5c2852c85d231b6c1caa3dccad3074f9")
        active = json.loads((directory / "oe_post_hue_controls.json").read_text())
        self.assertEqual(active["baseline_fst_sha256"],
                         hashlib.sha256(SOURCE.read_bytes()).hexdigest())
        self.assertEqual(historical["baseline_fst_sha256"],
                         "c51b8e4077194f4cc6f65e54a0c8a899366b5570152c6415cba117907d1a225c")
        recipe = current["recipes"][1]
        self.assertEqual(len(recipe["component_checks"]), 31)
        self.assertEqual(len(recipe["staged_checks"]), 7)
        for field in ("component_checks", "staged_checks"):
            self.assertTrue(all(check in active["recipes"][1][field] for check in recipe[field]))

    def test_production_matches_the_executed_coupled_components(self):
        data = json.loads((SC / "literature_dossiers/anglo_frisian/"
                           "oe_palatal_class_recipes.json").read_text())
        recipe = next(row for row in data["recipes"] if row["id"] == "p-coupled")
        source = SOURCE.read_text()
        for current, private in (
            ("OEWsPalatalDiphthongization", "AFOrd"),
            ("OELatePalatalDiphthong", "AFLate"),
            ("OEPalatalFricativeMerger", "AFMerge"),
            ("OEIntervocalicJVocalization", "AFJV"),
        ):
            self.assertEqual(compact(source, current),
                             compact(recipe["definitions"], private), current)
        private = compact(recipe["definitions"], "AFPal")
        self.assertEqual(private[1:-1].removesuffix(".o.OEVelarPalatalization"),
                         compact(source, "OEGFricativePalatal"))
        self.assertEqual(compact(recipe["definitions"], "AFSuffix")[1:-1],
                         compact(source, "OELateUnstressedAgSuffix"))
        self.assertEqual(compact(source, "OEVelarPalatalization"),
                         "[OEGFricativePalatal.o.OEVelarPalatalizationStops]")

    def test_real_fricative_class_and_separate_merger_order(self):
        source = SOURCE.read_text()
        self.assertIn("{*ʝ}", definition(source, "EnglishPalatalConsonant"))
        self.assertNotIn("{*ʝ}", definition(source, "EnglishIUmlautTrigger"))
        names = [stage.foma_identifier for stage in oe_pipeline.stages()]
        self.assertLess(names.index("OEIUmlaut"),
                        names.index("OEPalatalFricativeMerger"))
        self.assertEqual(names.index("OEPalatalFricativeMerger"),
                         names.index("OELateUnstressedAgSuffix") + 1)
        self.assertEqual(names.index("OECjCleanup"),
                         names.index("OEPalatalFricativeMerger") + 1)
        self.assertNotIn("{*ɣ}", definition(source, "OEVelarFricativePalatalization"))
        self.assertEqual(len("ʝ"), 1)

    def test_historical_and_technical_metadata_are_independent(self):
        registry = {row["sc_id"]: row for row in rows(SC / "registry/sc_registry.tsv")}
        self.assertEqual(registry["SC052"]["hist_stage"], "preoe")
        self.assertEqual(registry["SC052"]["verdict"], "REFORMULATE/SPLIT")
        for identifier in ("SC045", "SC082", "SC089"):
            self.assertEqual(registry[identifier]["adjudication_status"], "adjudicated")
        support = registry["SC109"]
        self.assertEqual(support["entry_type"], "support_stage")
        for field in ("hist_stage", "hist_scope", "confidence", "verdict"):
            self.assertEqual(support[field], "", field)
        self.assertEqual(registry["SC089"]["source_reader_facing_file"],
                         "089-late-unstressed-ag-suffix.md")

    def test_changed_reader_bodies_match_production(self):
        files = {
            "044-045-breaking-and-velar-fricative-palatalization.md":
                {"OEVelarFricativePalatalization"},
            "052-velar-palatalization.md": {
                "OEGFricativePalatal", "OEVelarPalatalizationKFront",
                "OEVelarPalatalizationStops", "OEVelarPalatalization",
                "OEPalatalFricativeMerger",
            },
            "055-056-i-umlaut-core.md":
                {"OEWsPalatalDiphthongization", "OELatePalatalDiphthong"},
            "081-083-j-strengthening-vocalization-and-ei-contraction.md":
                {"OEIntervocalicJVocalization"},
            "089-late-unstressed-ag-suffix.md": {"OELateUnstressedAgSuffix"},
        }
        source = SOURCE.read_text()
        for filename, expected in files.items():
            reader = (SC / "reader_facing" / filename).read_text()
            found = set()
            for block in re.findall(r"```foma\n([\s\S]*?)```", reader):
                names = re.findall(r"\bdefine (\w+)", block)
                self.assertEqual(len(names), 1, filename)
                name = names[0]
                if name in expected:
                    found.add(name)
                    self.assertEqual(compact(block, name), compact(source, name), name)
            self.assertEqual(found, expected, filename)


if __name__ == "__main__":
    unittest.main()
