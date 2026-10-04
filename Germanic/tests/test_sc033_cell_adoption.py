import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import cascade_baseline as baseline

BASE = ROOT / "Germanic/docs/sound_changes/cascade_baseline"


class CellAdoptionTests(unittest.TestCase):
    def setUp(self):
        self.approval = json.loads((BASE / "approved_cell_migration.json").read_text())
        self.previous = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc033.tsv",
            BASE / "cascade_baseline_summary_pre_sc033.json",
        )
        self.current = baseline.read_baseline(
            BASE / "cascade_baseline_outputs_pre_sc033_hue.tsv",
            BASE / "cascade_baseline_summary_pre_sc033_hue.json",
        )

    def test_exact_knee_cell_transition(self):
        baseline.validate_cell_transition(self.previous, self.current, self.approval)
        old = {row["row_id"]: row for row in self.previous["records"]}
        new = {row["row_id"]: row for row in self.current["records"]}
        self.assertEqual([identifier for identifier in old if old[identifier] != new[identifier]],
                         ["2085"])
        self.assertEqual(new["2085"]["proto"], "*knéwai")
        self.assertEqual(new["2085"]["counterpart"], "cneowe")
        self.assertEqual(new["2085"]["outputs"], "cneowe")
        self.assertEqual(self.current["summary"]["total_lexemes"], 387)
        self.assertEqual(self.current["summary"]["matched"], 380)
        self.assertEqual(self.current["summary"]["mismatched"], 7)
        self.assertEqual(self.current["summary"]["ambiguous_outputs"], 0)

    def test_rejects_undeclared_record_identity_and_summary_drift(self):
        for field, value in (
            ("proto", "*knéwą"), ("counterpart", "cnēow"), ("outputs", "cneow"),
            ("fst_input", "knéwą"), ("word_stress", "unstressed"),
            ("output_count", "2"), ("match", "0"), ("concept", "changed"),
        ):
            changed = copy.deepcopy(self.current)
            next(row for row in changed["records"] if row["row_id"] == "2085")[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, changed, self.approval)
        for kind in ("duplicate", "missing", "other_output", "fingerprint", "count"):
            changed = copy.deepcopy(self.current)
            if kind == "duplicate":
                changed["records"].append(copy.deepcopy(changed["records"][0]))
            elif kind == "missing":
                changed["records"].pop()
            elif kind == "other_output":
                changed["records"][0]["outputs"] = "changed"
            elif kind == "fingerprint":
                changed["summary"]["outputs_sha256"] = "0" * 64
            else:
                changed["summary"]["matched"] += 1
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, changed, self.approval)

    def test_rejects_incomplete_malformed_and_inconsistent_approval(self):
        for kind in ("missing_hash", "bad_hash", "adjudication", "memo", "duplicate",
                     "unknown", "before", "after", "multiplicity", "context"):
            approval = copy.deepcopy(self.approval)
            changed = copy.deepcopy(self.current)
            if kind == "missing_hash":
                approval["previous_summary"].pop("outputs_sha256")
            elif kind == "bad_hash":
                approval["legacy_archive_sha256"] = "bad"
            elif kind == "adjudication":
                approval["adjudication"] = "../unsafe"
            elif kind == "memo":
                approval["adjudication_memo"] = "wrong.md"
            elif kind == "duplicate":
                approval["changes"].append(copy.deepcopy(approval["changes"][0]))
            elif kind == "unknown":
                approval["changes"][0]["row_id"] = "missing"
            elif kind == "before":
                approval["changes"][0]["before"]["outputs"] = "wrong"
            elif kind == "after":
                approval["changes"][0]["after"]["outputs"] = "wrong"
            else:
                field, value = ("outputs", "cneowe|other") if kind == "multiplicity" else (
                    "fst_input", "ᵘknéwai")
                approval["changes"][0]["after"][field] = value
                next(row for row in changed["records"] if row["row_id"] == "2085")[field] = value
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                baseline.validate_cell_transition(self.previous, changed, approval)

    def test_adoption_preserves_archive_bytes_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for source, destination in (
                ("cascade_baseline_outputs_pre_sc033.tsv", "cascade_baseline_outputs.tsv"),
                ("cascade_baseline_summary_pre_sc033.json", "cascade_baseline_summary.json"),
                ("cascade_baseline_outputs_legacy380.tsv", "cascade_baseline_outputs_legacy380.tsv"),
                ("approved_input_migrations.tsv", "approved_input_migrations.tsv"),
            ):
                (target / destination).write_bytes((BASE / source).read_bytes())
            old = (target / "cascade_baseline_outputs.tsv").read_bytes()
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual((target / "cascade_baseline_outputs_pre_sc033.tsv").read_bytes(), old)
            before = {path.name: path.read_bytes() for path in target.iterdir()}
            baseline.adopt_cell_baseline(self.current, target, self.approval)
            self.assertEqual({path.name: path.read_bytes() for path in target.iterdir()}, before)
            (target / "cascade_baseline_summary_pre_sc033.json").unlink()
            with self.assertRaisesRegex(ValueError, "incomplete"):
                baseline.adopt_cell_baseline(self.current, target, self.approval)


if __name__ == "__main__":
    unittest.main()
