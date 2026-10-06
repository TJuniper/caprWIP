"""Regression coverage for the SC021 adjudication and its successor rules."""

from __future__ import annotations

import csv
import importlib.util
import io
import re
import shutil
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
MANIFEST = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
            / "cascade_order_manifest.tsv")
HISTORICAL_AUDIT = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
                    / "historical_audit_table.tsv")
RENAME_MANIFEST = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
                   / "rename_migration_manifest.tsv")
BOOK_DOSSIER = (GERMANIC / "docs" / "sound_changes" / "book_dossiers"
                / "018-025-early-nwgmc-unstressed-and-boundary-limited-zone.book-dossier.md")
CHRONOLOGY_GRAPH_NODES = (GERMANIC / "docs" / "sound_changes" / "order_tests"
                          / "chronology_cards" / "chronology_graph_nodes.tsv")
SC_REGISTRY = (GERMANIC / "docs" / "sound_changes" / "registry"
               / "sc_registry.tsv")
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"


# Live-probe availability: these adjudication files mix committed-evidence
# assertions (always run) with live flookup probes against the untracked
# sandbox bins built by `adjudicate --evidence`. The probes are skipped when
# the local runtime build is absent (e.g. clean CI checkout).
RUNTIME_BUILT = ((BIN_DIR / "old_english.bin").is_file()
                 and shutil.which("flookup") is not None)
requires_runtime = unittest.skipUnless(
    RUNTIME_BUILT,
    "live runtime probe: needs local sandbox bins (adjudicate --evidence) "
    "and flookup on PATH")


def load_trace_tool():
    spec = importlib.util.spec_from_file_location("oe_full_trace_report", TRACE_TOOL)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class SC021AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)#.*$", "", cls.text)
        with MANIFEST.open(encoding="utf-8") as handle:
            cls.positions = {
                row["foma_identifier"]: int(row["position"])
                for row in csv.DictReader(handle, delimiter="\t")
            }
        cls.trace = load_trace_tool()

    def stage(self, name, form):
        return self.trace.run_stage(
            BIN_DIR, f"old_english_sandbox_after_{name}.bin", form
        )

    def test_sc021_is_retired_not_silently_repurposed(self):
        self.assertNotRegex(
            self.uncommented, r"define\s+PNWGmcUnstressedORaising\b"
        )
        self.assertNotIn("PNWGmcUnstressedORaising", self.positions)

    def test_sc021_is_not_a_current_promotion_or_migration_candidate(self):
        def rows(path):
            lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
                     if not ln.startswith("#")]
            return {row["sc_id"]: row
                    for row in csv.DictReader(lines, delimiter="\t")}

        audit = rows(HISTORICAL_AUDIT)["SC021"]
        rename = rows(RENAME_MANIFEST)["SC021"]
        dossier = BOOK_DOSSIER.read_text(encoding="utf-8")

        self.assertEqual(audit["required_action"], "retired")
        self.assertEqual(audit["proposed_hist_stage"], "retired")
        self.assertEqual(rename["migration_status"], "retired")
        self.assertEqual(rename["canonical_foma_identifier"], "")
        self.assertNotRegex(dossier, r"singleton candidates?:[^\n]*SC021")
        self.assertIn("SC021 is retired", dossier)

        with CHRONOLOGY_GRAPH_NODES.open(encoding="utf-8") as handle:
            graph = {
                row["change_id"]: row for row in csv.DictReader(handle, delimiter="\t")
            }["SC021"]
        reg_lines = [ln for ln in SC_REGISTRY.read_text(encoding="utf-8").splitlines()
                     if not ln.startswith("#")]
        registry = {
            row["sc_id"]: row
            for row in csv.DictReader(io.StringIO("\n".join(reg_lines)), delimiter="\t")
        }["SC021"]
        # chronology_graph_nodes.tsv is the archival card-area record; its
        # experiment-time current_order column recorded the retirement.
        self.assertEqual(graph["current_order"], "retired")
        self.assertEqual(graph["in_contextual_edges"], "no")
        self.assertEqual(registry["lifecycle_status"], "retired")
        self.assertEqual(registry["verdict"], "RETIRE")
        self.assertEqual(registry["staging_row"], "no")

    def test_successors_follow_shortening_and_precede_sc040(self):
        self.assertLess(
            self.positions["OELateOShortening"],
            self.positions["OEMedUnstressedORaising"],
        )
        self.assertLess(
            self.positions["OEMedUnstressedORaising"],
            self.positions["OEFinalUnstressedOLowering"],
        )
        self.assertLess(
            self.positions["OEFinalUnstressedOLowering"],
            self.positions["OEMedUnstressedULowering"],
        )

    @requires_runtime
    def test_wundude_has_the_source_backed_medial_path(self):
        form = "wúndōdē"
        self.assertEqual(
            self.stage("oe_late_o_shortening", form), ["*w*ú*n*d*o*d*ē"]
        )
        self.assertEqual(
            self.stage("oe_med_unstressed_o_raising", form), ["*w*ú*n*d*u*d*ē"]
        )
        self.assertEqual(
            self.stage("oe_final_unstressed_o_lowering", form), ["*w*ú*n*d*u*d*ē"]
        )
        self.assertEqual(
            self.stage("old_english_surface", form), ["wundude"]
        )

    @requires_runtime
    def test_final_shortened_o_does_not_use_the_medial_rule(self):
        form = "mḗnōθz"
        self.assertEqual(
            self.stage("oe_late_o_shortening", form), ["*m*ō*n*o*θ"]
        )
        self.assertEqual(
            self.stage("oe_med_unstressed_o_raising", form), ["*m*ō*n*o*θ"]
        )
        self.assertEqual(
            self.stage("oe_final_unstressed_o_lowering", form), ["*m*ō*n*a*θ"]
        )
        self.assertEqual(
            self.stage("old_english_surface", form), ["mōnaþ"]
        )

    @requires_runtime
    def test_late_sc040_remains_distinct_from_the_new_chain(self):
        form = "xébun"
        self.assertEqual(
            self.stage("oe_final_unstressed_o_lowering", form), ["*ç*éo*β*u*n"]
        )
        self.assertEqual(
            self.stage("oe_med_unstressed_u_lowering", form), ["*ç*éo*β*o*n"]
        )
        self.assertEqual(
            self.stage("old_english_surface", form), ["heofon"]
        )


if __name__ == "__main__":
    unittest.main()
