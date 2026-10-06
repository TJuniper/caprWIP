"""Research consistency, independent of canonical executable order."""
from __future__ import annotations

import contextlib
import csv
import io
import json
import sys
import tempfile
import unittest
from dataclasses import asdict, fields, replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import anglo_frisian_chronology as af


def claim(name="c1", a="a", b="b", relation="before", **changes):
    base = af.Claim(
        name, "model", a, b, relation, "English", "unresolved", "unresolved",
        "source input > output under stated conditioner", "later input > output",
        "operative layer", "Source", "41-42", "inference",
        "explicit conditional premise", "positive and negative witness",
        "", "",
    )
    return replace(base, **changes)


class ChronologyTests(unittest.TestCase):
    def check(self, *claims):
        af.validate_claims(list(claims), {"Source"})
        return af.check_model(list(claims))

    def kinds(self, result):
        return {issue["kind"] for issue in result["issues"]}

    def test_strict_cycle_has_source_path(self):
        result = self.check(claim(), claim("c2", "b", "a"))
        self.assertIn("strict_cycle", self.kinds(result))
        issue = result["issues"][0]
        self.assertEqual(set(issue["claim_path"]), {"c1", "c2"})
        self.assertEqual(issue["event_path"][0], issue["event_path"][-1])
        self.assertTrue(all(source["pages"] == "41-42" for source in issue["sources"]))

    def test_weak_only_cycle_is_not_strict_cycle(self):
        result = self.check(claim(relation="not_after"), claim("c2", "b", "a", "not_after"))
        self.assertFalse(result["issues"])

    def test_mixed_strict_weak_cycle(self):
        self.assertIn("strict_cycle", self.kinds(self.check(claim(), claim("c2", "b", "a", "not_after"))))

    def test_identity_collapses_strict_order(self):
        self.assertIn("strict_cycle", self.kinds(self.check(claim(), claim("c2", "a", "b", "same_event"))))

    def test_transitive_identity_conflicts_with_distinctness(self):
        result = self.check(claim(relation="same_event"), claim("c2", "b", "c", "same_event"),
                            claim("c3", "a", "c", "distinct"))
        self.assertIn("identity_conflict", self.kinds(result))
        self.assertEqual(result["issues"][0]["supporting_claims"], ["c3"])

    def test_weak_coincidence_does_not_assert_event_identity(self):
        result = self.check(claim(relation="not_after"), claim("c2", "b", "a", "not_after"),
                            claim("c3", "a", "b", "distinct"))
        self.assertFalse(result["issues"])

    def test_transitive_daughter_predecessor(self):
        result = self.check(claim(event_a_scope="daughter_only"),
                            claim("c2", "b", "c", event_b_scope="common_stem"))
        issue = next(issue for issue in result["issues"] if issue["kind"] == "daughter_predecessor")
        self.assertEqual(issue["event_path"], ["a", "b", "c"])
        self.assertEqual(issue["claim_path"], ["c1", "c2"])

    def test_not_after_cannot_evade_tree_test(self):
        result = self.check(claim(relation="not_after", event_a_scope="daughter_only",
                                 event_b_scope="common_stem"))
        self.assertIn("daughter_predecessor", self.kinds(result))

    def test_identity_cannot_merge_daughter_and_stem(self):
        result = self.check(claim(relation="same_event", event_a_scope="daughter_only",
                                 event_b_scope="common_stem"))
        self.assertIn("daughter_predecessor", self.kinds(result))

    def test_scope_is_not_inferred_from_language_or_identifier(self):
        result = self.check(claim(a="EnglishOnly", b="EAFShared", language="Old English",
                                 sc_correspondence="SC004"))
        self.assertEqual(result["status"], "incomplete")
        self.assertNotIn("daughter_predecessor", self.kinds(result))

    def test_conflicting_scope_assertions(self):
        result = self.check(claim(event_a_scope="common_stem"),
                            claim("c2", "a", "c", event_a_scope="daughter_only"))
        self.assertIn("scope_conflict", self.kinds(result))

    def test_unresolved_relation_produces_limited_result(self):
        result = self.check(claim(relation="unresolved", event_a_scope="common_stem",
                                 event_b_scope="daughter_only"))
        self.assertEqual(result["status"], "incomplete")
        self.assertFalse(result["issues"])

    def test_open_conditioning_gap_is_not_success(self):
        result = self.check(claim(event_a_scope="common_stem", event_b_scope="daughter_only",
                                 open_questions="conditioner unverified"))
        self.assertEqual(result["status"], "incomplete")

    def test_disconnected_groups_are_reported(self):
        result = self.check(claim(), claim("c2", "c", "d"))
        self.assertTrue(any("disconnected" in reason for reason in result["incomplete"]))

    def test_complete_local_claims_remain_conditional(self):
        result = self.check(claim(event_a_scope="common_stem", event_b_scope="daughter_only"))
        self.assertEqual(result["status"], "consistent_under_assumptions")
        self.assertIn("not a complete history", result["coverage"])

    def test_alternatives_cannot_be_combined(self):
        with self.assertRaisesRegex(ValueError, "one nonempty"):
            af.check_model([claim(), claim("c2", "b", "a", model_id="rival")])

    def test_duplicate_and_missing_provenance_rejected(self):
        for claims, message in (
            ([claim(), claim()], "duplicate"),
            ([claim(source_key="Absent")], "unknown source"),
            ([claim(printed_pages="")], "missing printed_pages"),
            ([claim(event_a_spec="")], "missing event_a_spec"),
            ([], "no claims"),
        ):
            with self.subTest(message=message), self.assertRaisesRegex(ValueError, message):
                af.validate_claims(claims, {"Source"})

    def test_invalid_pages_and_vocabularies(self):
        for changes in ({"printed_pages": "sections 1-3"}, {"printed_pages": "42-41"},
                        {"printed_pages": "0"}, {"relation": "after"},
                        {"event_a_scope": "inferred"}, {"evidence_type": "output_fit"}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                af.validate_claims([claim(**changes)], {"Source"})

    def test_checked_in_source_tables_are_limited_and_cited(self):
        claims = af.load_claims(af.DEFAULT_TABLE, af.bibliography_keys(af.ROOT / "docs/refs.bib"))
        self.assertEqual({c.model_id for c in claims},
                         {"ringe-taylor-d", "campbell-english-conditional", "ringe-taylor-a",
                          "goblirsch-au", "hogg-initial-cutoff", "hogg-medial-trigger",
                          "ordinary-ws-pd", "conventional-english-breaking",
                          "versloot-anglian-e", "bremmer-frisian-breaking"})
        for model in {c.model_id for c in claims}:
            result = af.check_model([c for c in claims if c.model_id == model])
            self.assertEqual(result["status"], "incomplete")
            self.assertFalse(result["issues"])

    def test_ringe_taylor_ai_constraint_orders_milestones_not_whole_durations(self):
        claims = af.load_claims(af.DEFAULT_TABLE, af.bibliography_keys(af.ROOT / "docs/refs.bib"))
        milestones = [c for c in claims if c.model_id == "ringe-taylor-a"]
        self.assertEqual(len(milestones), 1)
        self.assertEqual(milestones[0].event_a, "inherited-long-fronting-well-underway")
        self.assertEqual(milestones[0].event_b, "english-ai-contraction-complete")
        self.assertEqual(milestones[0].relation, "before")
        self.assertIn("allows overlap", milestones[0].assumptions)
        self.assertEqual(milestones[0].source_key, "RingeTaylor2014")
        self.assertEqual(milestones[0].printed_pages, "170")

    def test_node_candidates_preserve_separate_premises_and_unresolved_classes(self):
        with (af.DEFAULT_TABLE.parent / "node_state_candidates.tsv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
        self.assertEqual(len({(row["candidate_id"], row["component"]) for row in rows}), len(rows))
        self.assertEqual({row["candidate_id"] for row in rows},
                         {"conservative-english", "luick-common-fronting", "goblirsch-common-au"})
        keys = af.bibliography_keys(af.ROOT / "docs/refs.bib")
        for row in rows:
            with self.subTest(candidate=row["candidate_id"], component=row["component"]):
                self.assertTrue(all(row.values()))
                self.assertIn(row["source_key"], keys)
                self.assertRegex(row["printed_pages"], r"^[1-9]\d*(?:-\d+)?(?:,[1-9]\d*(?:-\d+)?)*$")
                self.assertIn(row["status"], {"conditional_working_cut", "partial_domain_only",
                                             "alternative_not_adopted", "unresolved"})
        conservative = {row["component"]: row for row in rows
                        if row["candidate_id"] == "conservative-english"}
        self.assertEqual(len(conservative), 7)
        self.assertEqual(conservative["palatal-layers"]["status"], "unresolved")
        self.assertEqual(conservative["glide-reanalysis"]["status"], "partial_domain_only")
        self.assertIn("conditional", conservative["stressed-ai"]["premises"])

    def test_cli_is_read_only_and_preserves_alternatives(self):
        with tempfile.TemporaryDirectory() as directory:
            table = Path(directory) / "table.tsv"
            bibliography = Path(directory) / "refs.bib"
            bibliography.write_text("@book{Source, title={Example}}\n", encoding="utf-8")
            names = [field.name for field in fields(af.Claim)]
            with table.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=names, delimiter="\t")
                writer.writeheader()
                writer.writerows(asdict(c) for c in (
                    claim(event_a_scope="common_stem", event_b_scope="daughter_only"),
                    claim("c2", "b", "a", model_id="rival",
                          event_a_scope="common_stem", event_b_scope="daughter_only"),
                ))
            before = table.read_bytes(), bibliography.read_bytes()
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = af.main(["--table", str(table), "--bibliography", str(bibliography)])
            self.assertEqual(code, 0)
            self.assertEqual(len(json.loads(output.getvalue())), 2)
            self.assertEqual(before, (table.read_bytes(), bibliography.read_bytes()))
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    af.main(["--table", str(table), "--bibliography", str(bibliography), "--model", "missing"])
            self.assertEqual(error.exception.code, 2)

    def test_cli_incomplete_exit_is_distinct_from_success(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(af.main([]), 3)


if __name__ == "__main__":
    unittest.main()
