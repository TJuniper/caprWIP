import copy
import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import cascade_baseline as baseline
import oe_pipeline
from rule_coverage_census import load_firing_summary

BASE = ROOT / "Germanic/docs/sound_changes/cascade_baseline"


class ContextAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.approval = json.loads((BASE / "approved_context_migration.json").read_text())
        self.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc031_sc098.tsv",
            BASE / "cascade_baseline_summary_pre_sc031_sc098.json",
        )
        self.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc033.tsv",
            BASE / "cascade_baseline_summary_pre_sc033.json",
        )

    def test_exact_approved_delta_preserves_lexical_and_output_records(self):
        baseline.validate_context_transition(self.previous, self.current, self.approval)
        self.assertEqual(self.current["summary"]["total_lexemes"], 387)
        self.assertEqual(self.current["summary"]["mismatched"], 7)
        self.assertEqual(self.current["summary"]["ambiguous_outputs"], 0)
        self.assertEqual(self.current["summary"]["outputs_sha256"],
                         "fe55aa8b39467e318b3a9997c2c48009c057dfbfc2bf877bf7be49b9f89a510e")

    def test_transition_rejects_output_lexical_context_and_identity_drift(self):
        for field, value in (
            ("outputs", "changed"), ("proto", "*changed"), ("proto_norm", "changed"),
            ("counterpart", "changed"), ("output_count", "2"),
            ("word_stress", "unstressed"), ("fst_input", "ᵘchanged"),
        ):
            changed = copy.deepcopy(self.current)
            changed["records"][0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                baseline.validate_context_transition(self.previous, changed, self.approval)
        for mutation in ("duplicate", "missing"):
            changed = copy.deepcopy(self.current)
            if mutation == "duplicate":
                changed["records"].append(changed["records"][0])
            else:
                changed["records"].pop()
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                baseline.validate_context_transition(self.previous, changed, self.approval)

    def test_adoption_preserves_previous_bytes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            pairs = (
                ("cascade_baseline_outputs_pre_sc031_sc098.tsv", "cascade_baseline_outputs.tsv"),
                ("cascade_baseline_summary_pre_sc031_sc098.json", "cascade_baseline_summary.json"),
                ("cascade_baseline_outputs_legacy380.tsv", "cascade_baseline_outputs_legacy380.tsv"),
            )
            for source, dest in pairs:
                (target / dest).write_bytes((BASE / source).read_bytes())
            old = (target / "cascade_baseline_outputs.tsv").read_bytes()
            baseline.adopt_context_baseline(self.current, target, self.approval)
            self.assertEqual((target / "cascade_baseline_outputs_pre_sc031_sc098.tsv").read_bytes(), old)
            before = {p.name: p.read_bytes() for p in target.iterdir()}
            baseline.adopt_context_baseline(self.current, target, self.approval)
            self.assertEqual({p.name: p.read_bytes() for p in target.iterdir()}, before)

    def test_fresh_canonical_census_and_source_supported_feeders(self):
        text = (ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt").read_text()
        summary = load_firing_summary(text)
        self.assertEqual(summary["OEWWSimplification"], (5, ["chew", "dew", "four", "hew", "you"]))
        self.assertEqual(summary["OEEwLongDiphthong"], (1, ["hue"]))
        self.assertEqual(summary.get("OEJWWSimplification", (0, [])), (0, []))
        self.assertEqual(summary["OEJGlideIO"], (1, ["hue"]))
        self.assertEqual(summary["OEDiphthongLeveling"][0], 32)
        self.assertEqual(summary["OEAwLongDiphthong"][0], 4)
        for concept in ("four", "you"):
            block = text.split(f"--- {concept} ---\n", 1)[1].split("\n--- ", 1)[0]
            self.assertRegex(block, r"(?m)^PWGmcCoronalWAssimilation: .*")
            self.assertRegex(block, r"(?m)^OEWWSimplification: .*")
            self.assertNotRegex(block, r"[ᵘᶜ]")
        order = [stage.foma_identifier for stage in oe_pipeline.stages()]
        self.assertLess(order.index("PWGmcCoronalWAssimilation"), order.index("OEWWSimplification"))
        self.assertLess(order.index("OEWWSimplification"), order.index("PWGmcJGemination"))


if __name__ == "__main__":
    unittest.main()
