from __future__ import annotations

import copy
import json
import sqlite3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import pgmc_reconstruction_analysis as analytical
import pgmc_reconstruction_survey as survey


class AnalyticalValidationTests(unittest.TestCase):
    def setUp(self):
        self.corpus = [{"row_id": "1"}, {"row_id": "2"}]
        self.forms = [
            {"evidence_id": key, "row_ids": "1", "source_key": source,
             "diplomatic_form": form, "form_kind": "word", "printed_pages": "12",
             "confidence": "low"}
            for key, source, form in (
                ("e1", "Orel2003", "*a"), ("e2", "Kroonen2013", "*ā"))
        ]
        self.positions = []
        for form in self.forms:
            pos = dict.fromkeys(analytical.ANALYSIS_COLUMNS, "")
            pos.update(
                analysis_id="a" + form["evidence_id"], row_id="1",
                evidence_id=form["evidence_id"], status="reviewed",
                relation_to_row="same_etymon_citation", attribution_status="endorsed",
                comparison_unit="source_citation", stage_interpretation="unspecified",
                stage_basis="dictionary_context", analytical_form=form["diplomatic_form"],
                normalization_basis="identity", features="{}", notes="stage is not established",
            )
            self.positions.append(pos)
        case = dict.fromkeys(analytical.COMPARISON_COLUMNS, "")
        case.update(
            comparison_id="c1", row_ids="1", analysis_ids="ae1;ae2",
            scope="core_triage", question="What differs?", comparison_unit="source_citation",
            type_tags="quantity;inflection", comparability="undetermined",
            status="reviewed", explanation_status="unestablished",
            conclusion="quantity and cell need independent alignment", premises="no endpoint inferred",
            alignment_status="unreviewed",
        )
        self.cases = [case]
        self.reasons = []

    def validate(self):
        analytical.validate(self.corpus, self.forms, self.positions, self.cases, self.reasons)

    def add_reason(self, mode="analyst_inference"):
        reason = dict.fromkeys(analytical.RATIONALE_COLUMNS, "")
        reason.update(
            rationale_id="r1", analysis_ids="ae1;ae2", comparison_ids="c1",
            basis_type="morphological_argument", support_mode=mode, evidence_ids="e1;e2",
            statement="distinct cells may explain presentation", premises="alignment needed",
            counterarguments="does not settle endpoint",
            reason_target="divergence_explanation",
        )
        self.reasons.append(reason)
        self.cases[0].update(rationale_ids="r1", explanation_status=mode)

    def test_uncertain_citation_units_are_valid_without_invented_cause(self):
        before = copy.deepcopy(self.forms)
        self.validate()
        self.assertEqual(before, self.forms)

    def test_citation_review_does_not_complete_feature_alignment(self):
        with self.assertRaisesRegex(analytical.AnalysisError, "nonempty corpus"):
            analytical.require_alignment_complete([], [])
        analytical.require_complete(self.corpus[:1], self.cases)
        with self.assertRaisesRegex(analytical.AnalysisError, "feature alignment INCOMPLETE"):
            analytical.require_alignment_complete(self.corpus[:1], self.cases)

        self.cases[0].update(alignment_status="feature_aligned",
                             alignment_basis="Compared the word forms",
                             alignment_evidence_ids="e1;e2")
        with self.assertRaisesRegex(analytical.AnalysisError, "citation-cell inventory"):
            self.validate()
        for position in self.positions:
            position.update(features='{"quantity":"short"}',
                            feature_evidence_ids=position["evidence_id"])
        self.validate()
        analytical.require_alignment_complete(self.corpus[:1], self.cases)

    def test_alignment_gate_rejects_missing_or_partially_reviewed_core_cases(self):
        with self.assertRaisesRegex(analytical.AnalysisError, "feature alignment INCOMPLETE"):
            analytical.require_alignment_complete(self.corpus, [])
        first = self.cases[0]
        first.update(alignment_status="bounded_limit", alignment_basis="Cited comparison",
                     alignment_evidence_ids="e1;e2",
                     alignment_limits="The source does not date this alternative formation.")
        second = dict(first, comparison_id="c2", alignment_status="unreviewed",
                      alignment_basis="", alignment_evidence_ids="", alignment_limits="")
        with self.assertRaisesRegex(analytical.AnalysisError, "feature alignment INCOMPLETE"):
            analytical.require_alignment_complete(self.corpus[:1], [first, second])

    def test_bounded_alignment_requires_exact_cited_remaining_premise(self):
        self.cases[0].update(alignment_status="bounded_limit",
                            alignment_basis="Root quantity compared; endpoint not asserted",
                            alignment_evidence_ids="e1;e2")
        with self.assertRaisesRegex(analytical.AnalysisError, "exact remaining premise"):
            self.validate()
        self.cases[0]["alignment_limits"] = "Neither passage specifies whether this stem predates the shared raising."
        self.validate()
        analytical.require_alignment_complete(self.corpus[:1], self.cases)
        self.cases[0]["alignment_evidence_ids"] = "e1"
        with self.assertRaisesRegex(analytical.AnalysisError, "omits member evidence"):
            self.validate()

    def test_position_support_does_not_certify_divergence(self):
        self.add_reason("source_explicit")
        self.reasons[0]["reason_target"] = "position_support"
        with self.assertRaisesRegex(analytical.AnalysisError, "position support does not explain"):
            self.validate()
        self.cases[0]["explanation_status"] = "unestablished"
        self.validate()
        self.reasons[0]["reason_target"] = "divergence_explanation"
        self.reasons[0]["analysis_ids"] = "ae1"
        with self.assertRaisesRegex(analytical.AnalysisError, "at least two sources"):
            self.validate()

    def test_conditioning_tags_are_cited_classifications_not_string_matches(self):
        self.add_reason()
        self.reasons[0]["conditioning_tags"] = "following_j;trigger_loss"
        self.validate()
        tables = {
            "forms": (tuple(self.forms[0]), self.forms),
            "analyses": (analytical.ANALYSIS_COLUMNS, self.positions),
            "comparisons": (analytical.COMPARISON_COLUMNS, self.cases),
            "rationales": (analytical.RATIONALE_COLUMNS, self.reasons),
        }
        self.assertEqual(analytical.query(tables,
            "SELECT condition FROM rationale_conditions ORDER BY condition"),
            "condition\nfollowing_j\ntrigger_loss\n")
        self.reasons[0]["conditioning_tags"] = "regex_e_before_j"
        with self.assertRaisesRegex(analytical.AnalysisError, "conditioning tags"):
            self.validate()

    def test_unknown_reference_or_row_link_fails(self):
        for field, value in (("row_id", "2"), ("evidence_id", "absent")):
            with self.subTest(field=field):
                saved = copy.deepcopy(self.positions)
                self.positions[0][field] = value
                with self.assertRaises(analytical.AnalysisError):
                    self.validate()
                self.positions = saved

    def test_unknown_or_dictionary_context_cannot_date_endpoint(self):
        for basis in ("unknown", "dictionary_context"):
            with self.subTest(basis=basis):
                self.positions[0].update(stage_basis=basis, stage_interpretation="pgmc")
                with self.assertRaisesRegex(analytical.AnalysisError, "dated label|date a historical"):
                    self.validate()

    def test_low_confidence_explicit_later_stage_remains_later(self):
        self.positions[0].update(stage_interpretation="pwgmc", stage_basis="explicit_statement",
                                 stage_evidence_ids="e1")
        self.validate()
        self.forms[0]["confidence"] = "high"
        self.validate()
        self.assertEqual(self.positions[0]["stage_interpretation"], "pwgmc")

    def test_process_cannot_supply_word(self):
        self.forms[0].update(form_kind="process", diplomatic_form="")
        with self.assertRaisesRegex(analytical.AnalysisError, "not a reconstructed word"):
            self.validate()
        self.positions[0].update(
            analytical_form="", relation_to_row="process", comparison_unit="process")
        self.validate()

    def test_normalization_and_features_need_evidence(self):
        self.positions[0]["analytical_form"] = "*a-normalized"
        with self.assertRaisesRegex(analytical.AnalysisError, "normalization"):
            self.validate()
        self.positions[0]["normalization_evidence_ids"] = "e1"
        self.positions[0]["features"] = '{"quantity":"short"}'
        with self.assertRaisesRegex(analytical.AnalysisError, "features"):
            self.validate()
        self.positions[0]["feature_evidence_ids"] = "e1"
        self.validate()

    def test_unsupported_feature_or_tag_fails(self):
        self.positions[0]["features"] = '{"output_fit":"best"}'
        with self.assertRaisesRegex(analytical.AnalysisError, "feature claim"):
            self.validate()
        self.positions[0]["features"] = "{}"
        self.cases[0]["type_tags"] = "author_vote"
        with self.assertRaisesRegex(analytical.AnalysisError, "types"):
            self.validate()

    def test_core_review_cannot_omit_a_source_or_an_alternative(self):
        self.cases[0]["analysis_ids"] = "ae1"
        with self.assertRaisesRegex(analytical.AnalysisError, "core-source"):
            self.validate()
        self.cases[0]["analysis_ids"] = "ae1;ae2"
        self.forms.append(dict(self.forms[0], evidence_id="e3", diplomatic_form="*b"))
        with self.assertRaisesRegex(analytical.AnalysisError, "alternatives"):
            self.validate()

    def test_reviewed_case_cannot_hide_unreviewed_position(self):
        self.positions[0]["status"] = "unreviewed"
        with self.assertRaisesRegex(analytical.AnalysisError, "unreviewed positions"):
            self.validate()

    def test_explicit_explanation_requires_reciprocal_cited_reason(self):
        self.cases[0]["explanation_status"] = "source_explicit"
        with self.assertRaisesRegex(analytical.AnalysisError, "requires evidence"):
            self.validate()
        self.add_reason("source_explicit")
        self.validate()
        self.reasons[0]["comparison_ids"] = ""
        with self.assertRaisesRegex(analytical.AnalysisError, "reciprocal"):
            self.validate()

    def test_inference_cannot_be_laundered_as_author_statement(self):
        self.add_reason()
        self.cases[0]["explanation_status"] = "source_explicit"
        with self.assertRaisesRegex(analytical.AnalysisError, "author's explicit"):
            self.validate()

    def test_equivalence_requires_unit_stage_and_features(self):
        self.cases[0]["comparability"] = "equivalent"
        with self.assertRaisesRegex(analytical.AnalysisError, "different forms"):
            self.validate()
        self.positions[1].update(analytical_form="*a", normalization_basis="explained sign mapping",
                                 normalization_evidence_ids="e2")
        with self.assertRaisesRegex(analytical.AnalysisError, "uncertain stages"):
            self.validate()
        self.cases[0]["comparison_unit"] = "printed_representation"
        for pos in self.positions:
            pos["comparison_unit"] = "printed_representation"
        self.validate()
        self.positions[0]["comparison_unit"] = "selected_cell"
        with self.assertRaisesRegex(analytical.AnalysisError, "incompatible"):
            self.validate()

    def test_json_key_order_does_not_create_false_difference(self):
        self.cases[0].update(comparability="equivalent", comparison_unit="printed_representation")
        for pos in self.positions:
            pos.update(comparison_unit="printed_representation", analytical_form="*a",
                       normalization_evidence_ids=pos["evidence_id"],
                       feature_evidence_ids=pos["evidence_id"])
        self.positions[0]["features"] = '{"quantity":"short","cell":"citation"}'
        self.positions[1]["features"] = '{"cell":"citation","quantity":"short"}'
        self.validate()

    def test_full_equivalence_needs_endorsed_feature_complete_positions(self):
        self.cases[0].update(comparability="equivalent", comparison_unit="root_vocalism")
        for pos in self.positions:
            pos.update(comparison_unit="root_vocalism", analytical_form="*a",
                       normalization_evidence_ids=pos["evidence_id"],
                       stage_interpretation="pgmc", stage_basis="explicit_statement",
                       stage_evidence_ids=pos["evidence_id"])
        with self.assertRaisesRegex(analytical.AnalysisError, "essential unit features"):
            self.validate()
        for pos in self.positions:
            pos.update(features='{"vocalism":"a","quantity":"short"}',
                       feature_evidence_ids=pos["evidence_id"])
        self.validate()
        self.positions[1]["attribution_status"] = "rejected"
        with self.assertRaisesRegex(analytical.AnalysisError, "cannot prove full equivalence"):
            self.validate()

    def test_premised_equivalence_requires_reason_not_transitive_closure(self):
        self.cases[0]["comparability"] = "premised_equivalence"
        with self.assertRaisesRegex(analytical.AnalysisError, "cited reasoning"):
            self.validate()
        self.add_reason()
        self.validate()
        self.assertEqual(analytical.coverage(self.corpus, self.cases)[1]["status"], "unreviewed")
        with self.assertRaisesRegex(analytical.AnalysisError, "1 unreviewed"):
            analytical.require_complete(self.corpus, self.cases)

    def test_readonly_query_bridges_and_deterministic_atlas(self):
        self.add_reason()
        self.validate()
        tables = {
            "forms": (tuple(self.forms[0]), self.forms),
            "analyses": (analytical.ANALYSIS_COLUMNS, self.positions),
            "comparisons": (analytical.COMPARISON_COLUMNS, self.cases),
            "rationales": (analytical.RATIONALE_COLUMNS, self.reasons),
        }
        self.assertEqual(
            analytical.query(tables, "SELECT row_id FROM comparison_rows ORDER BY row_id"),
            "row_id\n1\n")
        self.assertEqual(
            analytical.query(tables, "SELECT type FROM comparison_types ORDER BY type"),
            "type\ninflection\nquantity\n")
        for sql in ("DELETE FROM forms", "PRAGMA user_version", "ATTACH ':memory:' AS extra"):
            with self.subTest(sql=sql), self.assertRaises(sqlite3.DatabaseError):
                analytical.query(tables, sql)
        first = analytical.atlas(self.forms, self.positions, self.cases, self.reasons)
        self.assertEqual(first, analytical.atlas(self.forms, self.positions, self.cases, self.reasons))
        self.assertIn("Orel2003 pp.12", first)


class LiveAnalyticalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.corpus, cls.sources, cls.forms, cls.reviews = survey.load()
        cls.tables = survey.load_analysis(survey.ROOT, cls.corpus, cls.forms)
        cls.positions = {pos["analysis_id"]: pos for pos in cls.tables["analyses"]}
        cls.cases = {case["comparison_id"]: case for case in cls.tables["comparisons"]}
        cls.evidence = {form["evidence_id"]: form for form in cls.forms}

    def test_all393_core_citation_units_retain_every_alternative(self):
        analytical.require_complete(self.corpus, self.tables["comparisons"])
        core = [case for case in self.cases.values() if case["scope"] == "core_triage"]
        self.assertEqual(len(core), 393)
        self.assertEqual({case["row_ids"] for case in core},
                         {row["row_id"] for row in self.corpus})

    def test_source_silence_is_not_agreement(self):
        negative_rows = {review["row_id"] for review in self.reviews
                         if review["source_key"] == "Kroonen2013" and review["status"] == "no_form_found"}
        self.assertEqual(len(negative_rows), 33)
        for row_id in negative_rows:
            self.assertEqual(self.cases[f"core-{row_id}"]["comparability"], "insufficient_evidence")

    def test_calibration_preserves_cells_components_and_rejected_positions(self):
        for row_id in ("1983", "1996", "2040", "2085", "2119", "2254", "2302"):
            self.assertEqual(self.cases[f"core-{row_id}"]["comparability"], "different_units")
        man = self.positions["a-2119-kroonen-core-2119-1"]
        self.assertEqual(man["attribution_status"], "rejected")
        self.assertEqual(self.positions["a-2302-kroonen-core-2302-1"]["relation_to_row"],
                         "compound_component")
        self.assertEqual(self.positions["a-2332-kroonen-core-2332-1"]["relation_to_row"], "same_family")
        self.assertEqual(self.positions["a-1983-cud-ringe-taylor-wgmc"]["stage_interpretation"], "pwgmc")
        self.assertEqual(self.positions["a-2272-orel-core-2272-1"]["attribution_status"], "conditional")
        self.assertEqual(self.positions["a-2040-gift-orel-headword"]["relation_to_row"],
                         "same_etymon_citation")
        self.assertEqual(self.positions["a-2040-kroonen-core-2040-1"]["relation_to_row"],
                         "same_family")
        self.assertEqual(self.positions["a-1934-orel-core-1934-02"]["relation_to_row"],
                         "same_etymon_other_cell")

    def test_dictionary_context_never_becomes_dated_pgmc_endpoint(self):
        contextual = [pos for pos in self.positions.values()
                      if pos["stage_basis"] == "dictionary_context"]
        self.assertTrue(contextual)
        self.assertTrue(all(pos["stage_interpretation"] == "unspecified" for pos in contextual))
        self.assertEqual(self.positions["a-2108-kroonen-core-2108-4"]["stage_interpretation"], "proto_norse")
        self.assertEqual(self.positions["a-1935-kroonen-core-1935-4"]["stage_interpretation"], "north_germanic")

    def test_representational_equivalence_does_not_erase_vocalism(self):
        self.assertEqual(self.cases["notation-gift-velar"]["comparability"], "equivalent")
        self.assertNotEqual(self.cases["core-2040"]["comparability"], "equivalent")
        self.assertEqual(self.evidence["gift-orel-headword"]["diplomatic_form"], "*ʒeftiz")
        self.assertEqual(self.positions["a-2040-gift-orel-headword"]["analytical_form"], "*geftiz")
        self.assertEqual(self.evidence["orel-core-2282-1"]["diplomatic_form"], "*westanē̆")
        self.assertEqual(self.cases["stem-spare-premised"]["comparability"], "premised_equivalence")
        self.assertNotEqual(self.cases["core-2205"]["comparability"], "equivalent")

    def test_query_separates_vowel_features_inventory_and_positional_reasons(self):
        tables = {
            "forms": (survey.FORM_COLUMNS, self.forms),
            **{name: (analytical.TABLES[name], rows) for name, rows in self.tables.items()},
        }
        result = analytical.query(tables, """
            SELECT f.source_key, af.value
            FROM analyses a JOIN forms f USING(evidence_id)
            JOIN analysis_features af USING(analysis_id)
            WHERE a.row_id='2011' AND af.feature='vocalism'
            ORDER BY f.source_key,a.analysis_id
        """)
        self.assertEqual(result, "source_key\tvalue\nKroonen2013\ti\nOrel2003\te\n"
                                "Ringe2017\ti/a/u/u\nRinge2017\ti\nRinge2017\tu\n")
        result = analytical.query(tables, """
            SELECT DISTINCT cr.comparison_id
            FROM comparison_rationales cr JOIN rationales r USING(rationale_id)
            WHERE r.basis_type='loan_hypothesis' ORDER BY cr.comparison_id
        """)
        self.assertEqual(result, "comparison_id\nbuck-borrowing-direction\ncore-2272\n")
        # Explicit reasons for a position need not explain the disagreement.
        self.assertTrue(self.cases["core-1975"]["rationale_ids"])
        self.assertEqual(self.cases["core-1975"]["explanation_status"], "unestablished")

    def test_seventh_tranche_queries_scoped_causes_without_promoting_whole_rows(self):
        tables = {"forms": (survey.FORM_COLUMNS, self.forms),
                  **{name: (analytical.TABLES[name], rows)
                     for name, rows in self.tables.items()}}
        sql = """
            SELECT c.comparison_id,c.explanation_status,
                   count(DISTINCT f.source_key) AS sources
            FROM comparisons c JOIN comparison_analyses ca USING(comparison_id)
            JOIN analyses p USING(analysis_id) JOIN forms f USING(evidence_id)
            WHERE c.comparison_id IN ('cud-e-cognate-admissibility','deal-root-derivation')
            GROUP BY c.comparison_id,c.explanation_status ORDER BY c.comparison_id
        """
        expected = ("comparison_id\texplanation_status\tsources\n"
                    "cud-e-cognate-admissibility\tanalyst_inference\t2\n"
                    "deal-root-derivation\tanalyst_inference\t2\n")
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, sql), expected)
        for row_id in map(str, range(1982, 1990)):
            self.assertEqual(self.cases["core-" + row_id]["explanation_status"], "unestablished")
        self.assertEqual(analytical.query(tables, """
            SELECT count(*) AS positions,count(DISTINCT evidence_id) AS evidence
            FROM analyses WHERE CAST(row_id AS INTEGER) BETWEEN 1982 AND 1989
        """), "positions\tevidence\n153\t149\n")

    def test_eighth_tranche_queries_direct_and_inferred_explanations_separately(self):
        tables = {"forms": (survey.FORM_COLUMNS, self.forms),
                  **{name: (analytical.TABLES[name], rows) for name, rows in self.tables.items()}}
        sql = """
            SELECT c.comparison_id,c.explanation_status,
                   count(DISTINCT f.source_key) AS sources
            FROM comparisons c JOIN comparison_analyses ca USING(comparison_id)
            JOIN analyses p USING(analysis_id) JOIN forms f USING(evidence_id)
            WHERE c.comparison_id IN ('do-present-metrical-history','dream-root-derivation')
            GROUP BY c.comparison_id,c.explanation_status ORDER BY c.comparison_id
        """
        expected = ("comparison_id\texplanation_status\tsources\n"
                    "do-present-metrical-history\tsource_explicit\t2\n"
                    "dream-root-derivation\tanalyst_inference\t2\n")
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, """
            SELECT count(*) AS positions,count(DISTINCT evidence_id) AS evidence
            FROM analyses WHERE CAST(row_id AS INTEGER) BETWEEN 1990 AND 1997
        """), "positions\tevidence\n138\t133\n")
        for row_id in map(str, range(1990, 1998)):
            self.assertEqual(self.cases["core-" + row_id]["explanation_status"], "unestablished")

    def test_ninth_tranche_queries_scoped_inference_without_promoting_core_causes(self):
        tables = {"forms": (survey.FORM_COLUMNS, self.forms),
                  **{name: (analytical.TABLES[name], rows) for name, rows in self.tables.items()}}
        sql = """
            SELECT c.comparison_id,c.explanation_status,count(DISTINCT f.source_key) AS sources
            FROM comparisons c JOIN comparison_analyses ca USING(comparison_id)
            JOIN analyses p USING(analysis_id) JOIN forms f USING(evidence_id)
            WHERE c.comparison_id IN ('drive-cognate-admissibility','fall-segmentation-gemination')
            GROUP BY c.comparison_id,c.explanation_status ORDER BY c.comparison_id
        """
        expected = ("comparison_id\texplanation_status\tsources\n"
                    "drive-cognate-admissibility\tanalyst_inference\t2\n"
                    "fall-segmentation-gemination\tanalyst_inference\t2\n")
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, """
            SELECT count(*) AS positions,count(DISTINCT evidence_id) AS evidence
            FROM analyses WHERE CAST(row_id AS INTEGER) BETWEEN 1998 AND 2005
        """), "positions\tevidence\n176\t172\n")
        for row_id in map(str, range(1998, 2006)):
            self.assertEqual(self.cases["core-" + row_id]["explanation_status"], "unestablished")

    def test_tenth_tranche_explanations_are_scoped_and_queries_deterministic(self):
        tables = {"forms": (survey.FORM_COLUMNS, self.forms),
                  **{name: (analytical.TABLES[name], rows) for name, rows in self.tables.items()}}
        sql = """
            SELECT c.comparison_id,c.explanation_status,count(DISTINCT f.source_key) AS sources
            FROM comparisons c JOIN comparison_analyses ca USING(comparison_id)
            JOIN analyses p USING(analysis_id) JOIN forms f USING(evidence_id)
            WHERE c.comparison_id IN ('field-formation-pathway','fire-collective-preform',
                                     'fire-front-vowel-formation')
            GROUP BY c.comparison_id,c.explanation_status ORDER BY c.comparison_id
        """
        expected = ("comparison_id\texplanation_status\tsources\n"
                    "field-formation-pathway\tanalyst_inference\t2\n"
                    "fire-collective-preform\tanalyst_inference\t2\n"
                    "fire-front-vowel-formation\tanalyst_inference\t2\n")
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, """
            SELECT count(*) AS positions,count(DISTINCT evidence_id) AS evidence
            FROM analyses WHERE CAST(row_id AS INTEGER) BETWEEN 2006 AND 2013
        """), "positions\tevidence\n149\t143\n")
        for row_id in map(str, range(2006, 2014)):
            self.assertEqual(self.cases["core-" + row_id]["explanation_status"], "unestablished")

    def test_eleventh_tranche_scoped_causes_and_deterministic_queries(self):
        tables = {"forms": (survey.FORM_COLUMNS, self.forms),
                  **{name: (analytical.TABLES[name], rows) for name, rows in self.tables.items()}}
        sql = """
            SELECT c.comparison_id,c.explanation_status,count(DISTINCT f.source_key) AS sources
            FROM comparisons c JOIN comparison_analyses ca USING(comparison_id)
            JOIN analyses p USING(analysis_id) JOIN forms f USING(evidence_id)
            WHERE c.comparison_id IN ('flee-fly-lexical-connection','flee-initial-cluster-history',
                                     'flea-citation-formation')
            GROUP BY c.comparison_id,c.explanation_status ORDER BY c.comparison_id
        """
        expected = ("comparison_id\texplanation_status\tsources\n"
                    "flea-citation-formation\tunestablished\t2\n"
                    "flee-fly-lexical-connection\tanalyst_inference\t2\n"
                    "flee-initial-cluster-history\tanalyst_inference\t2\n")
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, sql), expected)
        self.assertEqual(analytical.query(tables, """
            SELECT count(*) AS positions,count(DISTINCT evidence_id) AS evidence
            FROM analyses WHERE CAST(row_id AS INTEGER) BETWEEN 2014 AND 2021
        """), "positions\tevidence\n105\t99\n")
        self.assertEqual(analytical.query(tables, """
            SELECT p.evidence_id,p.relation_to_row,p.stage_interpretation
            FROM analyses p WHERE p.row_id='2015' AND p.evidence_id IN
                ('fulk-complete-index-fist','fulk-complete-index-fist-nasal')
            ORDER BY p.evidence_id
        """), "evidence_id\trelation_to_row\tstage_interpretation\n"
              "fulk-complete-index-fist\tcomparandum\tunspecified\n"
              "fulk-complete-index-fist-nasal\tcomparandum\tunspecified\n")
        for row_id in map(str, range(2014, 2022)):
            self.assertEqual(self.cases["core-" + row_id]["explanation_status"], "unestablished")

    def test_core_reading_population_and_supplements(self):
        survey.require_core_complete(self.corpus, self.sources, self.reviews)
        self.assertEqual(sum(form["source_key"] in survey.CORE_SOURCES
                             for form in self.forms), 1437)
        self.assertEqual(sum(review["source_key"] in survey.CORE_SOURCES
                             for review in self.reviews), 786)
        self.assertEqual(set(survey.ids(self.evidence["orel-core-1956-01"]["row_ids"])),
                         {"1956", "2311", "2312"})
        self.assertEqual(set(survey.ids(self.evidence["orel-core-1963-01"]["row_ids"])),
                         {"1963", "2148"})
        self.assertIn("Supplemented whole-entry", self.evidence["hind-orel-headword"]["argument"])
        for row_id in ("2080", "2086"):
            self.assertEqual(self.evidence[f"orel-core-{row_id}-1"]["asserted_stage"], "wgmc_explicit")
        spare = self.evidence["kroonen-core-2205-1"]
        self.assertIn("weak spare/save verb", spare["cell"])
        self.assertEqual(spare["printed_pages"], "465")
        self.assertNotIn("stem_class", self.cases["core-2205"]["type_tags"])

    def test_ringe_positions_do_not_manufacture_endpoint_or_core_resolution(self):
        def position(row_id, key):
            return self.positions[f"a-{row_id}-ringe-system-{key}"]

        self.assertEqual(position("1950", "bind-underlying")["attribution_status"], "conditional")
        self.assertEqual(position("1950", "bind-1")["analytical_form"], "*bindaną")
        self.assertEqual(position("1950", "bind-2")["relation_to_row"], "same_etymon_other_cell")
        self.assertEqual(position("2193", "sit-root")["stage_interpretation"], "unspecified")
        self.assertEqual(position("2193", "sit-root")["stage_basis"], "unknown")
        self.assertEqual(position("2193", "sit")["stage_interpretation"], "pgmc")
        self.assertEqual(position("2010", "fight-wg")["stage_interpretation"], "pwgmc")
        self.assertEqual(position("2233", "sup")["attribution_status"], "conditional")
        self.assertEqual(analytical.feature_values(position("1972", "brook"))["stem_class"], "weak")
        self.assertEqual(position("2313", "learn-no")["relation_to_row"], "same_etymon_citation")
        self.assertIn("Neither is an authored imperative", self.evidence["ringe-system-learn-no"]["argument"])
        self.assertEqual(self.cases["core-2193"]["explanation_status"], "unestablished")
        self.assertEqual(self.cases["core-1950"]["explanation_status"], "unestablished")


if __name__ == "__main__":
    unittest.main()
