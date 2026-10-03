import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "Germanic/tools"))
import oe_derivation_class_trace_report as report


class LexicalProjectionTests(unittest.TestCase):
    def setUp(self):
        self.row = {"concept": "gift", "proto": "*gíftiz", "counterpart": "ġift",
                    "derivation_class": "regular", "note": "Source-backed input."}
        self.text = ("=== MATCHES ===\n--- gift ---\nPROTO: *gíftiz\n"
                     "EXPECTED: ġift\nOUTPUTS: ġift\n\n"
                     "OEWsPalatalDiphthongization [no-change]: *ʤ*í*f*t*i\n\n"
                     "=== STAGE FIRING SUMMARY ===\nOEWsPalatalDiphthongization: 7\n")

    def project(self, text, rows=None):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trace.txt"
            path.write_text(text)
            with patch.object(report, "trace_provenance_problems", return_value=[]), \
                    patch.object(report, "apply_down", side_effect=AssertionError("must reuse evidence")), \
                    patch.object(report, "trace_lexeme", side_effect=AssertionError("must reuse evidence")):
                return report.project_full_trace(rows or [self.row], path)

    def test_regroups_exact_fresh_evidence_without_lookup(self):
        result = self.project(self.text)
        self.assertIn("=== DERIVATION_CLASS: regular (1) ===", result)
        self.assertIn("NOTE: Source-backed input.", result)
        self.assertIn("OEWsPalatalDiphthongization [no-change]: *ʤ*í*f*t*i", result)
        self.assertNotIn("STAGE FIRING SUMMARY", result)

    def test_stale_duplicate_and_wrong_identity_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trace.txt"
            path.write_text(self.text)
            with patch.object(report, "trace_provenance_problems", return_value=["stale"]):
                with self.assertRaisesRegex(ValueError, "stale"):
                    report.project_full_trace([self.row], path)
        for text in (self.text + self.text, self.text.replace("*gíftiz", "*géftiz")):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.project(text)

    def test_duplicate_corpus_rows_cannot_hide_omitted_evidence(self):
        other = self.text.replace("--- gift ---", "--- other ---")
        with self.assertRaisesRegex(ValueError, "duplicate corpus identity"):
            self.project(self.text + other, [self.row, self.row])


if __name__ == "__main__":
    unittest.main()
