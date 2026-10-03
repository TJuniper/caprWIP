"""Source-order, input and publication contracts of the approved U increment."""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import oe_pipeline


class OrdinaryPDTests(unittest.TestCase):
    def test_order_and_visible_residual(self):
        names = [stage.foma_identifier for stage in oe_pipeline.stages()]
        self.assertLess(names.index("OEWLossBeforeI"), names.index("OEWsPalatalDiphthongization"))
        self.assertLess(names.index("OEWsPalatalDiphthongization"), names.index("OEIUmlaut"))
        self.assertLess(names.index("OEIUmlaut"), names.index("OELatePalatalDiphthong"))
        self.assertEqual(oe_pipeline.sc_id("OELatePalatalDiphthong"), "SC105")

    def test_gift_input_and_published_alternatives(self):
        with (ROOT / "Germanic/data/germanic-aligned-final.tsv").open() as handle:
            gift = next(row for row in csv.DictReader(handle, delimiter="\t")
                        if row["ID"] == "2040")
        self.assertEqual((gift["PROTO"], gift["PROTOFORM"], gift["COUNTERPART"]),
                         ("*gíftiz", "*gíftiz", "ġift"))
        text = (ROOT / "Germanic/docs/lexeme_reports/model_entries/2040-gift-ġift.model.md").read_text()
        for key in ("Orel2003", "KlugeSeebold2011", "Bammesberger1990",
                    "Seebold1970", "Ringe2017", "RingeTaylor2014"):
            self.assertIn("@" + key, text)
        self.assertIn("### H. Confidence", text)
        self.assertIn("not completely certain", text)
        self.assertGreater(len(text.split()), 1500)

    def test_complete_live_populations_and_intermediates(self):
        trace = (ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt").read_text()
        parts = re.split(r"(?m)^--- (.+?) ---\n", trace)
        chunks = {parts[i]: parts[i + 1] for i in range(1, len(parts), 2)}
        ordinary = []
        late = []
        for concept, chunk in chunks.items():
            if not chunk.startswith("PROTO: "):
                continue
            lines = chunk.splitlines()
            for name, population in (("OEWsPalatalDiphthongization", ordinary),
                                     ("OELatePalatalDiphthong", late)):
                changes = [line for line in lines if line.startswith(name + ":")
                           and "[no-change]" not in line]
                if changes:
                    population.append(concept)
        self.assertEqual(set(ordinary), {"give", "guest", "shaft", "shear", "sheep", "shield", "year"})
        self.assertEqual(late, ["sheath"])
        guest = chunks["guest"]
        gift = chunks["gift"]
        sheath = chunks["sheath"]
        self.assertIn("*ʤ*ea*s*t*i", guest)
        self.assertIn("*ʤ*ie*s*t*i", guest)
        self.assertIn("*ʤ*í*f*t*i", gift)
        self.assertIn("*ʃ*ǣ*θ*i", sheath)
        self.assertIn("*ʃ*ēa*θ*i", sheath)


if __name__ == "__main__":
    unittest.main()
