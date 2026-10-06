#!/usr/bin/env python3
"""Guardrails for the inventory authority architecture (2026 repair).

Governing principle:

    Human-authored sources contain human judgements.
    Machine facts are generated from their actual authority.

The failure this file exists to prevent is concrete and had already happened.
Before the repair, `sc_inventory_annotations.tsv` was hand-edited and held
copies of facts that live somewhere else:

  * 90 of its 100 `rule_source_anchor` line numbers were wrong, because
    editing anything above a definition silently invalidates them;
  * 22 of its `foma_definition_raw` values no longer matched the rule that
    germanic.txt actually defines;
  * 21 of its firing counts disagreed with the coverage census.

None of that was noticed, because nothing checked. The fix is not to correct
the numbers but to remove the possibility of maintaining them by hand.

Authority map:

  executable truth   Germanic/fsts/germanic.txt   via tools/executable_facts.py
                     (definition text, where a rule is written, current line)
  order truth        cascade_baseline/executable_model.tsv, cascade_order_manifest.tsv
  corpus truth       the canonical trace -> cascade_baseline/rule_coverage_census.tsv
                     (whether a rule fires, how often, on which lexemes)
  scholarly truth    registry/sc_registry.tsv, registry/sc_inventory_notes.tsv,
                     registry/chronology_edges.tsv  (human, and only human)

Run: cd Germanic/tests && python3 -m unittest test_inventory_authority
"""
from __future__ import annotations

import csv
import importlib.util
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
TOOLS = GERMANIC / "tools"
FST = GERMANIC / "fsts" / "germanic.txt"
SC_DIR = GERMANIC / "docs" / "sound_changes"
REGISTRY_DIR = SC_DIR / "registry"

SC_REGISTRY = REGISTRY_DIR / "sc_registry.tsv"
NOTES = REGISTRY_DIR / "sc_inventory_notes.tsv"
ANNOTATIONS = REGISTRY_DIR / "sc_inventory_annotations.tsv"
EDGES = REGISTRY_DIR / "chronology_edges.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
CENSUS = SC_DIR / "cascade_baseline" / "rule_coverage_census.tsv"
BASELINE = SC_DIR / "cascade_baseline" / "cascade_baseline_outputs.tsv"

GENERATED_FILES = (ANNOTATIONS, INVENTORY,
                   SC_DIR / "sound_change_historical_staging_map.tsv")
HUMAN_SOURCES = (SC_REGISTRY, NOTES, EDGES)


def load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _tsv_rows(path: Path):
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


class ExecutableFactsTests(unittest.TestCase):
    """germanic.txt is the only authority for what a rule is and where it is."""

    @classmethod
    def setUpClass(cls):
        cls.ef = load_module("executable_facts")
        cls.facts = cls.ef.define_facts()

    def test_definitions_are_parsed_at_bracket_depth_zero(self):
        fact = self.facts["EAFNasalizedLowRounding"]
        self.assertEqual(fact.definition_raw,
                         "define EAFNasalizedLowRounding [ {*ã} -> {*ō} ];")
        self.assertEqual(fact.stable_anchor, "define EAFNasalizedLowRounding")

    def test_a_semicolon_inside_a_comment_cannot_truncate_a_definition(self):
        """The bug that broke the SC097 controls: a naive 'up to the first
        semicolon' scan stops inside a comment and silently empties the rule."""
        text = ("define Foo [\n"
                "    {*a} |\n"
                "    # Campbell p. 44; Fulk p. 55\n"
                "    {*b}\n"
                "];\n")
        facts = self.ef.parse_defines(text)
        self.assertIn("{*b}", facts["Foo"].body)
        self.assertNotIn("Campbell", facts["Foo"].body)

    def test_line_numbers_are_computed_not_stored(self):
        """Inserting lines above a definition changes only the computed line."""
        text = FST.read_text(encoding="utf-8")
        target = self.facts["EAFNasalizedLowRounding"]
        shifted = "\n" * 10 + text
        after = self.ef.parse_defines(shifted)["EAFNasalizedLowRounding"]
        self.assertEqual(after.line, target.line + 10)
        self.assertEqual(after.definition_raw, target.definition_raw)
        self.assertEqual(after.stable_anchor, target.stable_anchor)

    def test_every_registry_rule_resolves_to_a_real_define(self):
        missing = [r["sc_id"] for r in _tsv_rows(SC_REGISTRY)
                   if r["lifecycle_status"] == "active"
                   and (r["fst_identifier"] or "").strip() not in self.facts]
        self.assertEqual(missing, [],
                         f"registry identifiers with no define: {missing}")


class HumanSourcePurityTests(unittest.TestCase):
    """A hand-edited file may contain only human judgements."""

    @classmethod
    def setUpClass(cls):
        cls.notes = _tsv_rows(NOTES)
        cls.grv = load_module("generate_registry_views")

    def test_notes_columns_are_all_human_owned(self):
        self.assertEqual(
            list(self.notes[0]),
            ["change_id", "plain_description_draft", "order_sensitivity_status",
             "illustrative_lexemes", "notes", "review_note", "needs_human_review"])

    def test_no_foma_definitions_are_hand_maintained(self):
        for column in ("foma_definition_raw", "rule_source_anchor",
                       "rule_source_path"):
            self.assertNotIn(column, self.notes[0])
        for n in self.notes:
            for column, value in n.items():
                if column in ("notes", "review_note"):
                    continue
                self.assertNotRegex(
                    value or "", r"^define\s",
                    f"{n['change_id']}: {column} holds a copied Foma definition")

    def test_no_source_line_numbers_are_hand_maintained(self):
        for n in self.notes:
            for column, value in n.items():
                if column in ("notes", "review_note", "plain_description_draft"):
                    continue
                self.assertIsNone(
                    self.grv.executable_facts.LINE_REF_RE.search(value or ""),
                    f"{n['change_id']}: {column} holds a Foma source line number")

    def test_no_executable_positions_or_firing_counts_are_hand_maintained(self):
        for column in ("cascade_position", "exec_index", "firing_count",
                       "firing_lexemes", "trace_occurrence_count",
                       "appears_in_compact_trace", "example_lexemes"):
            self.assertNotIn(column, self.notes[0])

    def test_the_validator_rejects_a_machine_column(self):
        bad = [dict(self.notes[0], foma_definition_raw="define X [];")]
        errors = self.grv.validate_human_sources(bad)
        self.assertTrue(any("foma_definition_raw" in e for e in errors))

    def test_the_validator_rejects_a_hand_written_line_number(self):
        bad = [dict(self.notes[0], illustrative_lexemes="see line 2158")]
        errors = self.grv.validate_human_sources(bad)
        self.assertTrue(any("line number" in e for e in errors))

    def test_illustrative_lexemes_are_not_a_firing_claim(self):
        """The column is named so its editorial semantics are explicit; it must
        never be read as the current corpus firing population."""
        self.assertIn("illustrative_lexemes", self.notes[0])
        banner = NOTES.read_text(encoding="utf-8")
        self.assertIn("EDITORIAL", banner)


class GeneratedProjectionTests(unittest.TestCase):
    """Generated files must be reproducible from their real authorities."""

    @classmethod
    def setUpClass(cls):
        cls.ann = {r["change_id"]: r for r in _tsv_rows(ANNOTATIONS)}
        cls.inv = {r["change_id"]: r for r in _tsv_rows(INVENTORY)}
        cls.reg = {r["sc_id"]: r for r in _tsv_rows(SC_REGISTRY)}
        cls.census = {r["sc_id"]: r for r in _tsv_rows(CENSUS)}
        cls.facts = load_module("executable_facts").define_facts()

    def test_generated_files_are_marked(self):
        for path in GENERATED_FILES:
            self.assertIn("GENERATED FILE — DO NOT EDIT",
                          path.read_text(encoding="utf-8")[:400],
                          f"{path.name} must warn that it is generated")

    def test_human_sources_are_not_marked_generated(self):
        for path in HUMAN_SOURCES:
            head = path.read_text(encoding="utf-8")[:400]
            self.assertIn("hand-edited", head, path.name)
            self.assertNotIn("GENERATED FILE", head, path.name)

    def test_generated_definitions_equal_germanic_txt(self):
        for sc, row in self.ann.items():
            ident = (self.reg[sc]["fst_identifier"] or "").strip()
            if not ident:
                continue
            with self.subTest(sc=sc):
                self.assertEqual(row["foma_definition_raw"],
                                 self.facts[ident].definition_raw)
                self.assertEqual(row["rule_source_anchor"],
                                 self.facts[ident].stable_anchor)

    def test_generated_anchors_carry_no_line_numbers(self):
        line_ref = re.compile(r"\(\s*line\s+\d+\s*\)")
        for sc, row in self.ann.items():
            self.assertIsNone(line_ref.search(row["rule_source_anchor"]), sc)

    def test_generated_firing_counts_equal_the_census(self):
        for sc, c in self.census.items():
            with self.subTest(sc=sc):
                self.assertEqual(self.ann[sc]["firing_count"],
                                 c["corpus_firing_count"])
                self.assertEqual(self.ann[sc]["firing_lexemes"],
                                 c["lexical_witnesses"])

    def test_inventory_agrees_with_the_annotation_projection(self):
        for sc, row in self.inv.items():
            with self.subTest(sc=sc):
                self.assertEqual(row["foma_definition_raw"],
                                 self.ann[sc]["foma_definition_raw"])
                self.assertEqual(row["firing_count"],
                                 self.ann[sc]["firing_count"])

    def test_check_mode_detects_a_stale_projection(self):
        original = ANNOTATIONS.read_text(encoding="utf-8")
        try:
            ANNOTATIONS.write_text(original + "SC999\tx\n", encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(TOOLS / "generate_registry_views.py"), "--check"],
                capture_output=True, text=True)
            self.assertNotEqual(proc.returncode, 0,
                                "--check must fail on a stale projection")
        finally:
            ANNOTATIONS.write_text(original, encoding="utf-8")

    def test_projections_are_clean(self):
        proc = subprocess.run(
            [sys.executable, str(TOOLS / "generate_registry_views.py"), "--check"],
            capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0,
                         f"stale generated views:\n{proc.stdout}{proc.stderr}")

    def test_finalize_regenerates_the_projections(self):
        # finalize drives the ONE artifact graph, whose registry_views node
        # renders every generate_registry_views projection
        src = (TOOLS / "adjudicate.py").read_text(encoding="utf-8")
        self.assertIn("artifact_graph.refresh", src,
                      "--finalize must run the control-plane refresh")
        graph_src = (TOOLS / "artifact_graph.py").read_text(encoding="utf-8")
        self.assertIn("generate_registry_views.build_all", graph_src,
                      "the graph must own the registry projections")


class ChronologyEdgeWitnessSemanticsTests(unittest.TestCase):
    """A historically justified edge may have no live corpus witness."""

    @classmethod
    def setUpClass(cls):
        cls.edges = _tsv_rows(EDGES)
        cls.corpus = {r["concept"] for r in _tsv_rows(BASELINE)}
        cls.grv = load_module("generate_registry_views")
        cls.reg = _tsv_rows(SC_REGISTRY)

    def test_claimed_live_witnesses_really_exist_in_the_corpus(self):
        for e in self.edges:
            if e["evidence_basis"] != "independently_demonstrated":
                continue
            for lex in self.grv.split_lexemes(e["representative_lexemes"]):
                with self.subTest(edge=f"{e['source_change_id']}->{e['target_change_id']}"):
                    self.assertIn(lex, self.corpus)

    def test_a_stage_entailed_edge_needs_no_invented_witness(self):
        """The validator must not force an agent to fabricate a lexeme."""
        edge = dict(self.edges[0], relation_type="one_sided_chronology",
                    evidence_basis="stage_entailed", witness_role="none",
                    representative_lexemes="", representative_forms="",
                    notes="direction follows from the established stages")
        self.assertEqual(self.grv.validate_registry(self.reg, [edge]), [])

    def test_a_demonstrated_edge_without_a_witness_is_rejected(self):
        edge = dict(self.edges[0], relation_type="one_sided_chronology",
                    evidence_basis="independently_demonstrated",
                    witness_role="counterfeeding",
                    representative_lexemes="", representative_forms="",
                    notes="claims a demonstration")
        errors = self.grv.validate_registry(self.reg, [edge])
        self.assertTrue(any("names no witness" in e for e in errors))

    def test_a_demonstrated_edge_with_a_fake_witness_is_rejected(self):
        edge = dict(self.edges[0], relation_type="one_sided_chronology",
                    evidence_basis="independently_demonstrated",
                    witness_role="counterfeeding",
                    representative_lexemes="notaword",
                    representative_forms="*notaword",
                    notes="claims a demonstration")
        errors = self.grv.validate_registry(self.reg, [edge])
        self.assertTrue(any("not in the selected corpus" in e for e in errors))


    def test_a_demonstrated_edge_needs_a_machine_evidence_route(self):
        """Corpus membership alone does not demonstrate an interaction."""
        edge = dict(self.edges[0], source_change_id="SC001",
                    target_change_id="SC002",
                    relation_type="one_sided_chronology",
                    evidence_basis="independently_demonstrated",
                    witness_role="feeding",
                    representative_lexemes=sorted(self.corpus)[0],
                    representative_forms="*whatever",
                    machine_evidence="",
                    notes="claims a demonstration")
        errors = self.grv.validate_registry(self.reg, [edge])
        self.assertTrue(any("no order-test harness result" in e for e in errors),
                        errors)

    def test_machine_evidence_must_name_a_real_test(self):
        edge = dict(self.edges[0], source_change_id="SC001",
                    target_change_id="SC002",
                    relation_type="one_sided_chronology",
                    evidence_basis="independently_demonstrated",
                    witness_role="feeding",
                    representative_lexemes=sorted(self.corpus)[0],
                    representative_forms="*whatever",
                    machine_evidence="test:Germanic/tests/test_does_not_exist.py",
                    notes="claims a demonstration")
        errors = self.grv.validate_registry(self.reg, [edge])
        self.assertTrue(any("missing test" in e for e in errors), errors)

    def test_every_live_demonstrated_edge_has_an_evidence_route(self):
        harness = self.grv.load_harness_witnesses()
        for e in self.edges:
            if e["evidence_basis"] != "independently_demonstrated":
                continue
            pair = (e["source_change_id"], e["target_change_id"])
            named = set(self.grv.split_lexemes(e["representative_lexemes"]))
            ref = (e.get("machine_evidence") or "").strip()
            with self.subTest(edge=f"{pair[0]}->{pair[1]}"):
                if harness.get(pair, set()) & named:
                    continue
                self.assertTrue(ref.startswith("test:"), ref)
                self.assertTrue((REPO_ROOT / ref[len("test:"):]).is_file(), ref)


class MachineStateProseTests(unittest.TestCase):
    """Live human metadata may not mirror a current machine-state quantity.

    The structured columns were cleaned by the authority repair, but a
    free-text mirror is still a mirror: it goes stale the moment a corpus row,
    a firing population or the executable order changes.
    """

    @classmethod
    def setUpClass(cls):
        cls.grv = load_module("generate_registry_views")

    def test_live_human_sources_contain_no_machine_state_prose(self):
        errors = self.grv.validate_human_sources(_tsv_rows(NOTES))
        errors += self.grv.validate_human_prose(
            "sc_registry.tsv", _tsv_rows(SC_REGISTRY), "sc_id")
        errors += self.grv.validate_human_prose(
            "chronology_edges.tsv", _tsv_rows(EDGES), "source_change_id")
        machine_state = [e for e in errors if "current machine state" in e]
        self.assertEqual(machine_state, [])

    def test_machine_state_formulations_are_detected(self):
        for text in (
            "SC103 sits at cascade position 1.",
            "SC022 has witness_count = 1.",
            "The rule fires 17 times.",
            "SC004 currently has 24 corpus applications.",
            "SC024 has 17 firings in the present corpus.",
            "moved from position 23 to position 1",
            "trace_occurrence_count is 3",
            "executable position 22 is a holding zone",
        ):
            with self.subTest(text=text):
                self.assertTrue(self.grv.find_machine_state_prose(text), text)

    def test_legitimate_scholarly_prose_is_not_flagged(self):
        for text in (
            "Campbell §128 n. 1 p. 50 unifies the three feeders.",
            "Ringe vol. 1 §3.2.7(ii) pp. 149-150.",
            "This is one historical sound change, not three.",
            "SC103 feeds SC028 in `fist`.",
            "Early Runic makija, later 2nd c. AD (Gronvik 1998: 87).",
            "Diagnostic witnesses include `fist` and `thought`.",
            "See the generated firing census for the current population.",
            "Fulk 2018 §4.6 pp. 60-61 reconstructs a retained low front vowel.",
        ):
            with self.subTest(text=text):
                self.assertEqual(self.grv.find_machine_state_prose(text), [], text)

    def test_dated_adjudication_memos_are_not_covered(self):
        """A memo is a research record, not live metadata."""
        self.assertNotIn("audits", str(self.grv.HUMAN_PROSE_COLUMNS))
        for name in self.grv.HUMAN_PROSE_COLUMNS:
            self.assertTrue(name.endswith(".tsv"), name)


class NoOtherHandMaintainedMirrorsTests(unittest.TestCase):
    """Search the human sources for other copies of the same machine facts."""

    def test_no_human_source_holds_a_foma_definition_column(self):
        for path in HUMAN_SOURCES:
            rows = _tsv_rows(path)
            self.assertNotIn("foma_definition_raw", rows[0], path.name)

    def test_no_human_source_holds_a_foma_source_line_number(self):
        line_ref = re.compile(r"\(\s*line\s+\d+\s*\)")
        for path in HUMAN_SOURCES:
            for row in _tsv_rows(path):
                for column, value in row.items():
                    if column.endswith("notes") or column in ("notes", "review_note"):
                        continue
                    with self.subTest(path=path.name, column=column):
                        self.assertIsNone(line_ref.search(value or ""))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
