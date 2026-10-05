from __future__ import annotations

import copy
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import pgmc_reconstruction_survey as survey


class SurveyValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        holding = self.root / "docs/references/source.txt"
        holding.parent.mkdir(parents=True)
        holding.write_text("local held source", encoding="utf-8")
        self.sources = [{
            "source_key": "Source", "role": "reconstruction",
            "holding_paths": "docs/references/source.txt",
            "scope": "PGmc word reconstructions", "edition_status": "verified",
            "conventions_status": "verified", "notes": "actual held edition",
            "consultation_mode": "systematic_relevant", "priority": "1",
            "payoff": "addresses a specific reconstructed formation",
        }]
        self.corpus = [{"row_id": "1"}, {"row_id": "2"}]
        self.forms = [{
            "evidence_id": "form1", "row_ids": "1", "source_key": "Source",
            "printed_pages": "12-13", "locator": "s.v. source form",
            "diplomatic_form": "*éą", "asserted_stage": "unspecified_by_source",
            "form_kind": "word", "cell": "not specified",
            "comparison_form": "*éą", "normalization_basis": "identity",
            "argument": "actual source argument", "verification": "text_checked",
            "confidence": "low", "quoted_author": "",
            "basis": "docs/references/source.txt", "notes": "",
        }]
        self.reviews = [{
            "row_id": "1", "source_key": "Source", "status": "evidence_found",
            "evidence_ids": "form1", "search_basis": "full relevant source entry",
            "assessment": "source stage is not specified",
        }]

    def validate(self):
        survey.validate(self.sources, self.forms, self.reviews, self.corpus,
                        {"Source"}, self.root)

    def test_missing_review_is_unchecked_not_absent(self):
        self.validate()
        checks = survey.coverage_rows(self.corpus, self.sources, self.reviews, [{
            "source_key": "Source", "row_id": "2", "selection_basis": "specific formation question",
        }])
        self.assertEqual([row["status"] for row in checks], ["evidence_found", "unchecked"])
        self.assertTrue(survey.incomplete(self.sources, checks))

    def test_scoped_negative_needs_explicit_basis(self):
        self.reviews.append({
            "row_id": "2", "source_key": "Source", "status": "not_applicable",
            "evidence_ids": "", "search_basis": "", "assessment": "scope exclusion",
        })
        with self.assertRaisesRegex(survey.SurveyError, "search/assessment"):
            self.validate()
        self.reviews[-1]["search_basis"] = "source treats another formation exclusively"
        self.validate()
        self.assertFalse(survey.incomplete(
            self.sources, survey.coverage_rows(self.corpus, self.sources, self.reviews)))

    def test_duplicate_or_unknown_rows_fail(self):
        for links in ("1;1", "999"):
            with self.subTest(links=links):
                self.forms[0]["row_ids"] = links
                with self.assertRaisesRegex(survey.SurveyError, "row links"):
                    self.validate()

    def test_source_attribution_cannot_cross_review(self):
        self.reviews[0]["evidence_ids"] = "missing"
        with self.assertRaisesRegex(survey.SurveyError, "reciprocal"):
            self.validate()

    def test_process_evidence_is_not_a_whole_word(self):
        self.forms[0]["form_kind"] = "process"
        with self.assertRaisesRegex(survey.SurveyError, "not a quoted form"):
            self.validate()
        self.forms[0]["diplomatic_form"] = ""
        self.reviews[0]["status"] = "discussion_only"
        self.validate()

    def test_discussion_only_cannot_hide_authored_reconstruction(self):
        self.reviews[0]["status"] = "discussion_only"
        with self.assertRaisesRegex(survey.SurveyError, "hides a reconstruction"):
            self.validate()

    def test_printed_pages_and_normalization_are_required(self):
        for field, value, message in (
            ("printed_pages", "PAGE338", "printed pages"),
            ("normalization_basis", "", "normalization"),
            ("asserted_stage", "", "asserted_stage"),
            ("basis", "absent.txt", "verification basis"),
        ):
            with self.subTest(field=field):
                saved = copy.deepcopy(self.forms)
                self.forms[0][field] = value
                with self.assertRaisesRegex(survey.SurveyError, message):
                    self.validate()
                self.forms = saved

    def test_confidence_never_changes_source_stage_or_diplomatic_form(self):
        before = copy.deepcopy(self.forms)
        self.validate()
        self.forms[0]["confidence"] = "high"
        self.validate()
        self.assertEqual(self.forms[0]["asserted_stage"], before[0]["asserted_stage"])
        self.assertEqual(self.forms[0]["diplomatic_form"], "*éą")

    def test_unreviewed_source_convention_prevents_completion(self):
        self.sources[0]["conventions_status"] = "unreviewed"
        checks = survey.coverage_rows(self.corpus, self.sources, self.reviews, [{
            "source_key": "Source", "row_id": "1", "selection_basis": "selected formation",
        }])
        self.assertTrue(survey.incomplete(self.sources, checks))

    def test_opportunistic_evidence_is_retained_without_blanket_targets(self):
        self.sources[0]["consultation_mode"] = "opportunistic"
        self.validate()
        checks = survey.coverage_rows(self.corpus, self.sources, self.reviews)
        self.assertEqual(len(checks), 1)
        self.assertEqual(checks[0]["review_required"], "0")
        self.assertEqual(checks[0]["status"], "evidence_found")
        self.assertFalse(survey.incomplete(self.sources, checks))
        with self.assertRaisesRegex(survey.SurveyError, "consultation scope"):
            survey.coverage_rows(self.corpus, self.sources, self.reviews, [{
                "source_key": "Source", "row_id": "2", "selection_basis": "unjustified blanket obligation",
            }])

    def test_noncore_target_requires_known_row_and_explicit_selection(self):
        for row_id, basis in (("999", "specific case"), ("2", "")):
            with self.subTest(row_id=row_id):
                with self.assertRaisesRegex(survey.SurveyError, "selection basis"):
                    survey.validate_targets([{
                        "source_key": "Source", "row_id": row_id, "selection_basis": basis,
                    }], self.corpus, self.sources)

    def test_unknown_or_outside_library_holding_fails(self):
        self.sources[0]["holding_paths"] = "../outside.txt"
        with self.assertRaisesRegex(survey.SurveyError, "out-of-library"):
            self.validate()


class ReadingScopeTests(unittest.TestCase):
    def setUp(self):
        self.corpus = [{"row_id": "1"}, {"row_id": "2"}]
        self.sources = [{
            "source_key": key, "role": "reconstruction",
            "consultation_mode": "systematic_relevant",
            "edition_status": "verified", "conventions_status": "verified",
        } for key in survey.READING_SOURCES]
        self.scopes = []
        for key in survey.READING_SOURCES:
            for kind in ("screen", "method", "passage"):
                scope = dict.fromkeys(survey.SCOPE_COLUMNS, "")
                scope.update(
                    scope_id=f"{key}-{kind}", source_key=key, scope_kind=kind,
                    population_scope="source_general" if kind == "method" else "all_rows",
                    printed_pages="11-12", locator="actual relevant section",
                    selection_basis="named reconstruction question",
                    status="reviewed", search_basis="complete argument and index/alias screen",
                    assessment="bounded actual reading; no lexical absence inferred",
                    verification="text_checked",
                )
                self.scopes.append(scope)
        self.forms = []
        self.targets = []
        self.reviews = []

    def validate(self):
        survey.validate_scopes(
            self.scopes, self.corpus, self.sources, self.forms, self.targets)

    def require_complete(self):
        survey.require_reading_complete(
            self.corpus, self.sources, self.scopes, self.forms, self.targets, self.reviews)

    def test_actual_scoped_reading_does_not_manufacture_lexical_reviews(self):
        self.require_complete()
        self.assertEqual(survey.coverage_rows(
            self.corpus, self.sources, self.reviews, self.targets), [])
        self.assertEqual(len(self.reviews), 0)

    def test_empty_or_deleted_schedule_cannot_complete_named_programme(self):
        self.scopes = []
        with self.assertRaisesRegex(survey.SurveyError, "no screen scope"):
            self.require_complete()
        self.sources = []
        with self.assertRaisesRegex(survey.SurveyError, "missing systematic source"):
            self.require_complete()

    def test_empty_population_cannot_complete_programme(self):
        self.corpus = []
        with self.assertRaisesRegex(survey.SurveyError, "nonempty corpus"):
            self.require_complete()

    def test_pending_screen_does_not_certify_population_review(self):
        scope = self.scopes[0]
        scope.update(status="pending", verification="unreviewed")
        self.validate()
        with self.assertRaisesRegex(survey.SurveyError, "2 rows not applicability-screened"):
            self.require_complete()

    def test_grouped_screens_must_cover_the_exact_population(self):
        self.scopes[0].update(population_scope="named_rows", row_ids="1")
        with self.assertRaisesRegex(survey.SurveyError, "1 rows not applicability-screened"):
            self.require_complete()
        second = dict(self.scopes[0], scope_id="second-screen", row_ids="2")
        self.scopes.append(second)
        self.require_complete()

    def test_completed_pass_needs_methods_and_passage_reading(self):
        self.scopes = [scope for scope in self.scopes if scope["scope_kind"] != "passage"]
        with self.assertRaisesRegex(survey.SurveyError, "no passage scope"):
            self.require_complete()

    def test_unverified_source_conventions_prevent_complete_reading(self):
        self.sources[0]["conventions_status"] = "unreviewed"
        with self.assertRaisesRegex(survey.SurveyError, "conventions not verified"):
            self.require_complete()

    def test_reviewed_scope_needs_actual_printed_pages_and_assessment(self):
        for field, value, message in (
            ("printed_pages", "PAGE338", "printed pages"),
            ("printed_pages", "", "printed pages"),
            ("search_basis", "", "assessment"),
            ("assessment", "", "assessment"),
            ("verification", "unreviewed", "verification"),
        ):
            with self.subTest(field=field, value=value):
                saved = copy.deepcopy(self.scopes)
                self.scopes[0][field] = value
                with self.assertRaisesRegex(survey.SurveyError, message):
                    self.validate()
                self.scopes = saved

    def test_pending_scope_cannot_claim_verified_extraction(self):
        self.scopes[0]["status"] = "pending"
        with self.assertRaisesRegex(survey.SurveyError, "pending scope"):
            self.validate()

    def test_declared_gap_remains_visible_and_blocks_full_verification(self):
        self.scopes[0].update(status="verification_gap", verification="unreviewed",
                              printed_pages="", verification_limits="held excerpt lacks the index")
        self.validate()
        with self.assertRaisesRegex(survey.SurveyError, "verification_gap"):
            self.require_complete()
        progress = survey.reading_progress(
            self.corpus, self.sources, self.scopes, self.forms, self.targets, self.reviews)
        self.assertIn("held excerpt lacks the index", progress)
        self.scopes[0]["verification_limits"] = ""
        with self.assertRaisesRegex(survey.SurveyError, "verification limit"):
            self.validate()

    def test_target_needs_compatible_named_scope_and_actual_review(self):
        key = survey.READING_SOURCES[0]
        self.targets = [{"source_key": key, "row_id": "1",
                         "selection_basis": "actual formation", "scope_ids": ""}]
        with self.assertRaisesRegex(survey.SurveyError, "scope link"):
            self.validate()
        self.targets[0]["scope_ids"] = f"{key}-method"
        with self.assertRaisesRegex(survey.SurveyError, "incompatible target scope"):
            self.validate()
        self.targets[0]["scope_ids"] = f"{key}-passage"
        self.validate()
        with self.assertRaisesRegex(survey.SurveyError, "Ringe2017/1: unchecked"):
            self.require_complete()
        self.reviews = [{"source_key": key, "row_id": "1", "status": "verification_gap"}]
        with self.assertRaisesRegex(survey.SurveyError, "Ringe2017/1: verification_gap"):
            self.require_complete()
        self.reviews[0]["status"] = "discussion_only"
        self.require_complete()

    def test_source_and_row_links_cannot_be_crossed(self):
        self.scopes[0].update(population_scope="named_rows", row_ids="999")
        with self.assertRaisesRegex(survey.SurveyError, "population/row"):
            self.validate()
        self.scopes[0].update(population_scope="named_rows", row_ids="1")
        self.forms = [{"evidence_id": "e", "source_key": survey.READING_SOURCES[1],
                       "row_ids": "1"}]
        self.scopes[0]["evidence_ids"] = "e"
        with self.assertRaisesRegex(survey.SurveyError, "cross-source"):
            self.validate()
        self.forms[0]["source_key"] = survey.READING_SOURCES[0]
        self.forms[0]["row_ids"] = "2"
        with self.assertRaisesRegex(survey.SurveyError, "named scope"):
            self.validate()

    def test_live_dispatch_is_valid_but_not_completed_research(self):
        corpus, sources, forms, reviews = survey.load()
        targets = survey.read_table(
            survey.ROOT / survey.DIRECTORY / "review_targets.tsv", survey.TARGET_COLUMNS)
        scopes = survey.load_scopes(survey.ROOT, corpus, sources, forms, targets)
        for source, expected in (("Ringe2017", 6), ("Fulk2018", 8)):
            completed = [scope for scope in scopes if scope["source_key"] == source]
            self.assertEqual(len(completed), expected)
            self.assertTrue(all(scope["status"] == "reviewed" for scope in completed))
        self.assertEqual({scope["source_key"] for scope in scopes
                          if scope["status"] != "reviewed"}, {"RingeTaylor2014"})
        rt_scopes = [scope for scope in scopes if scope["source_key"] == "RingeTaylor2014"]
        self.assertEqual(len(rt_scopes), 6)
        self.assertEqual([scope["scope_id"] for scope in rt_scopes
                          if scope["status"] != "reviewed"], ["rt-conventions"])
        self.assertEqual(next(scope for scope in rt_scopes
                              if scope["scope_id"] == "rt-conventions")["status"],
                         "verification_gap")
        self.assertEqual({scope["source_key"] for scope in scopes}, set(survey.READING_SOURCES))
        with self.assertRaisesRegex(survey.SurveyError, "INCOMPLETE"):
            survey.require_reading_complete(corpus, sources, scopes, forms, targets, reviews)
        self.assertEqual(sum(review["source_key"] in survey.CORE_SOURCES
                             for review in reviews), 786)

    def test_scope_query_separates_scheduling_from_actual_consultations(self):
        corpus, sources, forms, reviews = survey.load()
        targets = survey.read_table(
            survey.ROOT / survey.DIRECTORY / "review_targets.tsv", survey.TARGET_COLUMNS)
        scopes = survey.load_scopes(survey.ROOT, corpus, sources, forms, targets)
        analysis = survey.load_analysis(survey.ROOT, corpus, forms)
        tables = {
            "corpus": (tuple(corpus[0]), corpus),
            "sources": (survey.SOURCE_COLUMNS, sources),
            "forms": (survey.FORM_COLUMNS, forms),
            "reviews": (survey.REVIEW_COLUMNS, reviews),
            "targets": (survey.TARGET_COLUMNS, targets),
            "reading_scopes": (survey.SCOPE_COLUMNS, scopes),
            **{name: (survey.analytical.TABLES[name], rows) for name, rows in analysis.items()},
        }
        result = survey.analytical.query(tables, """
            SELECT (SELECT count(*) FROM scope_rows
                    WHERE scope_id='ringe-corpus-screen') AS scheduled_rows,
                   (SELECT count(*) FROM reviews
                    WHERE source_key='Ringe2017') AS actual_reviews
        """)
        self.assertEqual(result, "scheduled_rows\tactual_reviews\n393\t192\n")
        result = survey.analytical.query(tables, """
            SELECT count(*) AS pending_evidence FROM scope_evidence se
            JOIN reading_scopes rs USING(scope_id)
            WHERE rs.status='pending'
        """)
        self.assertEqual(result, "pending_evidence\n0\n")

    def test_completed_readings_preserve_local_dates_quantity_and_cell_variants(self):
        _, _, forms, reviews = survey.load()
        evidence = {form["evidence_id"]: form for form in forms}
        for key, page in (("ringe-complete-fight-pgmc", "108"),
                          ("ringe-complete-fight-paradigm", "271")):
            self.assertEqual(evidence[key]["diplomatic_form"], "*fehtaną")
            self.assertEqual(evidence[key]["printed_pages"], page)
            self.assertEqual(evidence[key]["asserted_stage"], "PGmc")
        self.assertEqual(evidence["ringe-system-fight-wg"]["asserted_stage"], "pwgmc")
        for cell in ("nom", "acc"):
            name = evidence[f"ringe-complete-name-{cell}-image"]
            self.assertEqual(name["diplomatic_form"], "namō\u0304")
            self.assertEqual(name["printed_pages"], "312")
            self.assertEqual(name["verification"], "page_image_checked")
        sit = evidence["fulk-complete-sit-p43"]
        alternative = evidence["fulk-complete-sit-e-citation"]
        self.assertEqual((sit["diplomatic_form"], sit["asserted_stage"]),
                         ("*sit-j-anaⁿ", "pgmc"))
        self.assertEqual((alternative["diplomatic_form"], alternative["asserted_stage"]),
                         ("*setjanaⁿ", "not_explicitly_dated"))
        self.assertEqual(sum(row["source_key"] == "Fulk2018" for row in reviews), 137)

    def test_actual_applicability_manifests_preserve_the_full_population(self):
        corpus, _, _, reviews = survey.load()
        population = {row["row_id"] for row in corpus}
        directory = survey.ROOT / survey.DIRECTORY / "reading_accountability"
        for source, filename, field, consulted in (
            ("Ringe2017", "ringe-applicability.tsv", "disposition", "relevant_consulted"),
            ("Fulk2018", "fulk-applicability.tsv", "screen_disposition",
             "screened_actual_lexical_or_family_consultation"),
            ("RingeTaylor2014", "rt-applicability.tsv", "disposition",
             "consulted_applicable"),
        ):
            rows = survey.read_table(directory / filename)
            self.assertEqual(len(rows), 393)
            self.assertEqual({row["row_id"] for row in rows}, population)
            actual = {row["row_id"] for row in reviews if row["source_key"] == source}
            self.assertEqual({row["row_id"] for row in rows if row[field] == consulted}, actual)
            self.assertNotEqual(actual, population)

    def test_rt_occurrence_audit_removes_overlap_without_merging_repeated_positions(self):
        _, _, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        self.assertNotIn("rt-complete-1934-002", evidence)
        self.assertNotIn("rt-complete-1934-009", evidence)
        first, later = (evidence[f"rt-complete-1934-{suffix}"] for suffix in ("004", "006"))
        self.assertEqual(first["diplomatic_form"], later["diplomatic_form"])
        self.assertEqual(first["asserted_stage"], "pwgmc")
        self.assertEqual(later["asserted_stage"], "unspecified_local_endpoint")
        directory = survey.ROOT / survey.DIRECTORY / "reading_accountability"
        remap = survey.read_table(directory / "rt-dedup_remap.tsv")
        self.assertEqual(len(remap), 31)
        occurrences = survey.read_table(directory / "rt-occurrence_accountability.tsv")
        retained = [row for row in occurrences
                    if row["evidence_id"] == "rt-complete-1934-006"
                    and row["disposition"] == "actual_source_occurrence_retained"]
        self.assertEqual({(row["start_char"], row["end_char"]) for row in retained},
                         {("66", "72"), ("85", "91")})
        self.assertEqual(sum(row["source_key"] == "RingeTaylor2014" for row in reviews), 255)
        self.assertTrue(all(row["verification"] == "text_checked"
                            for row in forms if row["evidence_id"].startswith("rt-complete-")))

    def test_source_explicit_ask_reason_does_not_certify_interauthor_explanation(self):
        corpus, _, forms, _ = survey.load()
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        reason = next(row for row in analytical["rationales"]
                      if row["rationale_id"] == "r-1948-ringe-j-raising")
        self.assertEqual((reason["reason_target"], reason["support_mode"],
                          reason["conditioning_tags"]),
                         ("position_support", "source_explicit", "following_j"))
        argument = next(row for row in forms if row["evidence_id"] == "ringe-ask-raising-argument")
        self.assertEqual(argument["printed_pages"], "151-152,273")
        case = next(row for row in analytical["comparisons"]
                    if row["comparison_id"] == "core-1948")
        self.assertEqual(case["explanation_status"], "unestablished")
        self.assertEqual(case["alignment_status"], "bounded_limit")

    def test_ask_full_source_alignment_preserves_exact_limits_and_representations(self):
        corpus, _, forms, _ = survey.load()
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["analysis_id"]: row for row in analytical["analyses"]}
        case = next(row for row in analytical["comparisons"]
                    if row["comparison_id"] == "core-1948")
        members = survey.analytical.ids(case["analysis_ids"])
        self.assertEqual(len(members), 20)
        self.assertEqual(set(members), {key for key, row in positions.items()
                                      if row["row_id"] == "1948"})
        self.assertEqual(set(survey.analytical.ids(case["alignment_evidence_ids"])),
                         {positions[key]["evidence_id"] for key in members})
        for premise in ("Kroonen", "wait etymon", "quantity", "target is absent"):
            self.assertIn(premise, case["alignment_limits"])
        self.assertEqual(case["explanation_status"], "unestablished")
        by_evidence = {row["evidence_id"]: row for row in positions.values()
                       if row["row_id"] == "1948"}
        underlying = by_evidence["rt-complete-1948-003"]
        self.assertEqual(underlying["analytical_form"], "*/bidjan/")
        self.assertEqual(underlying["attribution_status"], "endorsed")
        self.assertEqual(underlying["stage_interpretation"], "unspecified")
        self.assertEqual(by_evidence["rt-complete-1948-011"]["attribution_status"], "endorsed")
        for suffix in ("004", "005", "006", "007", "008", "009", "010"):
            position = by_evidence[f"rt-complete-1948-{suffix}"]
            self.assertEqual(position["attribution_status"], "illustrative")
            self.assertEqual(position["relation_to_row"], "same_etymon_other_cell")
        self.assertTrue(any(row["alignment_status"] == "unreviewed"
                            for row in analytical["comparisons"]
                            if row["scope"] == "core_triage"))

    def test_fulk_cow_annotation_matches_the_selected_dative_not_a_surface_guess(self):
        corpus, _, forms, _ = survey.load()
        cow = next(row for row in corpus if row["row_id"] == "1980")
        self.assertEqual((cow["protoform"], cow["target"]), ("*kūi", "cȳ"))
        sidecar = survey.read_table(
            survey.ROOT / "Germanic/data/entry_stage_metadata.tsv")
        selected = next(row for row in sidecar if row["row_id"] == "1980")
        self.assertIn("dat.sg. cȳ < *kūi", selected["evidence"])
        evidence = {form["evidence_id"]: form for form in forms}
        self.assertIn("DAT.SG", evidence["fulk-complete-index-cow-stem"]["cell"])
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["analysis_id"]: row for row in analytical["analyses"]}
        for key in ("a-1958-fulk-complete-both-cow",
                    "a-1980-fulk-complete-both-cow",
                    "a-1980-fulk-complete-index-cow-stem"):
            self.assertIn("DAT.SG", survey.analytical.feature_values(positions[key])["cell"])
        guards = survey.read_table(
            survey.ROOT / survey.DIRECTORY /
            "reading_accountability/fulk-selected_cell_guard_provenance.tsv")
        guard = next(row for row in guards if row["row_id"] == "1980")
        self.assertIn("Unsupported surface-form inference", guard["original_basis"])
        self.assertIn("DAT.SG", guard["current_guard"])

    def test_ask_bid_alignment_retains_rejection_and_derivational_quantity(self):
        corpus, _, forms, _ = survey.load()
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in analytical["analyses"]
                     if row["row_id"] == "1948"}
        self.assertEqual(positions["kroonen-core-1948-1"]["attribution_status"], "endorsed")
        self.assertEqual(positions["kroonen-core-1948-2"]["attribution_status"], "rejected")
        self.assertEqual(positions["orel-core-1948-02"]["relation_to_row"], "same_family")
        antecedent = survey.analytical.feature_values(positions["orel-core-1948-02"])
        self.assertEqual(antecedent["quantity"], "long root ī")
        self.assertEqual(positions["orel-core-1948-02"]["analytical_form"], "*bīđanan")
        for key in ("orel-core-1948-01", "kroonen-core-1948-1"):
            self.assertEqual(positions[key]["stage_interpretation"], "unspecified")
        self.assertEqual(positions["ringe-system-bid-ask"]["stage_interpretation"], "pgmc")

    def test_rt_token_boundary_repairs_do_not_restore_native_corruption(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        directory = survey.ROOT / survey.DIRECTORY / "reading_accountability"
        receipt = survey.read_table(directory / "rt-token_boundary_review.tsv")
        repairs = [row for row in receipt if row["outcome"] == "proved extractor clip repaired"]
        self.assertEqual(len(repairs), 8)
        for row in receipt:
            self.assertEqual(evidence[row["evidence_id"]]["diplomatic_form"],
                             row["current_native_reading"])
            self.assertEqual(evidence[row["evidence_id"]]["printed_pages"], row["printed_pages"])
            self.assertEqual(evidence[row["evidence_id"]]["verification"], "text_checked")
        beard = evidence["rt-complete-1940-001"]
        self.assertEqual((beard["diplomatic_form"], beard["form_kind"]), ("*bar(z)da-", "stem"))
        occurrence = next(row for row in survey.read_table(
            directory / "rt-occurrence_accountability.tsv")
                          if row["evidence_id"] == "rt-complete-1940-001")
        self.assertEqual((occurrence["start_char"], occurrence["end_char"]), ("5", "11"))
        self.assertEqual((occurrence["retained_start_char"], occurrence["retained_end_char"]),
                         ("5", "15"))
        self.assertEqual(evidence["rt-complete-1948-002"]["diplomatic_form"], "*(bididan]")
        self.assertEqual(evidence["rt-complete-2254-004"]["diplomatic_form"], "priG)u")

    def test_initial_lexical_block_alignments_include_all_available_positions(self):
        corpus, _, forms, _ = survey.load()
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["analysis_id"]: row for row in analytical["analyses"]}
        cases = {row["comparison_id"]: row for row in analytical["comparisons"]}
        for row_id in map(str, range(1933, 1941)):
            case = cases[f"core-{row_id}"]
            self.assertEqual(case["alignment_status"], "bounded_limit")
            members = set(survey.analytical.ids(case["analysis_ids"]))
            self.assertEqual(members, {key for key, row in positions.items()
                                       if row["row_id"] == row_id})
            self.assertEqual(set(survey.analytical.ids(case["alignment_evidence_ids"])),
                             {positions[key]["evidence_id"] for key in members})
        self.assertIn("shortening does not by itself turn ē into a",
                      cases["core-1933"]["alignment_limits"])
        self.assertIn("nominal genitive", cases["core-1936"]["alignment_limits"])
        self.assertIn("label/-az tension", cases["core-1938"]["alignment_limits"])
        self.assertIn("loan direction", cases["core-1940"]["alignment_limits"])

    def test_bake_supplement_retains_finite_cell_and_conditional_etymology(self):
        corpus, _, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in analytical["analyses"]
                     if row["row_id"] == "1934"}
        finite = evidence["rt-alignment-bake-second-singular"]
        self.assertEqual((finite["diplomatic_form"], finite["printed_pages"],
                          finite["form_kind"], finite["asserted_stage"]),
                         ("becst", "233", "attestation", "oe"))
        self.assertEqual(positions[finite["evidence_id"]]["relation_to_row"],
                         "same_etymon_other_cell")
        self.assertEqual(positions["ringe-complete-bake-stem"]["attribution_status"], "endorsed")
        self.assertIn("etymological premise remains conditional",
                      positions["ringe-complete-bake-stem"]["notes"])
        review = next(row for row in reviews if row["row_id"] == "1934"
                      and row["source_key"] == "RingeTaylor2014")
        self.assertIn(finite["evidence_id"], survey.analytical.ids(review["evidence_ids"]))
        self.assertEqual(sum(row["source_key"] == "RingeTaylor2014" for row in reviews), 255)

    def test_second_tranche_alignments_include_every_position_without_duplicate_evidence(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        cases = {row["comparison_id"]: row for row in tables["comparisons"]}
        for row_id in ("1941", "1942", "1943", "1944", "1945", "1946", "1947", "1949"):
            with self.subTest(row_id=row_id):
                members = [row for row in tables["analyses"] if row["row_id"] == row_id]
                case = cases["core-" + row_id]
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(set(survey.ids(case["analysis_ids"])),
                                 {row["analysis_id"] for row in members})
                linked = survey.ids(case["alignment_evidence_ids"])
                self.assertEqual(len(linked), len(set(linked)))
                self.assertEqual(set(linked), {row["evidence_id"] for row in members})
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertTrue(case["alignment_limits"])
        self.assertEqual(len({(row["row_id"], row["source_key"]) for row in reviews}),
                         len(reviews))
        self.assertEqual(sum(row["source_key"] == "RingeTaylor2014" for row in reviews), 255)
        self.assertEqual(sum(row["alignment_status"] == "bounded_limit"
                             for row in tables["comparisons"]
                             if row["scope"] == "core_triage"
                             and row["row_ids"] in {str(i) for i in range(1933, 1950)}), 17)
        with self.assertRaises(survey.analytical.AnalysisError):
            survey.analytical.require_alignment_complete(corpus, tables["comparisons"])

    def test_tranche_source_repairs_preserve_local_stages_and_starred_comparison(self):
        corpus, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] in {"1945", "1949"}}
        self.assertEqual(evidence["orel-core-1949-01"]["asserted_stage"], "WGmc")
        self.assertEqual(positions["orel-core-1949-01"]["stage_interpretation"], "wgmc")
        gothic = evidence["rt-complete-1945-015"]
        self.assertEqual((gothic["diplomatic_form"], gothic["form_kind"]), ("*balgs", "word"))
        self.assertEqual(positions[gothic["evidence_id"]]["stage_interpretation"], "other")
        self.assertEqual(positions[gothic["evidence_id"]]["relation_to_row"], "comparandum")
        self.assertEqual(gothic["verification"], "text_checked")

    def test_fulk_beaver_body_quote_does_not_backdate_index_or_oe_mutation(self):
        corpus, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1941" and row["comparison_unit"] != "lexical_identity"}
        self.assertEqual(evidence["fulk-alignment-beaver-pgmc"]["diplomatic_form"], "*bebruz")
        self.assertEqual(positions["fulk-alignment-beaver-pgmc"]["stage_interpretation"], "pgmc")
        self.assertEqual(evidence["fulk-complete-index-beaver"]["diplomatic_form"], "bebruz")
        self.assertEqual(positions["fulk-complete-index-beaver"]["stage_interpretation"], "unspecified")
        self.assertEqual(evidence["fulk-alignment-beaver-oe"]["diplomatic_form"], "beofor")
        self.assertEqual(positions["fulk-complete-beaver-stem"]["stage_interpretation"], "oe")
        reason = next(row for row in tables["rationales"]
                      if row["rationale_id"] == "r-1941-fulk-oe-back-mutation")
        self.assertEqual(reason["conditioning_tags"], "following_u")
        self.assertIn("not a claim of PGmc u-raising", reason["premises"])

    def test_beaver_direction_explanation_is_inferred_and_not_whole_case_resolution(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        cases = {row["comparison_id"]: row for row in tables["comparisons"]}
        focus = cases["beaver-colour-direction"]
        self.assertEqual(focus["comparability"], "substantive_difference")
        self.assertEqual(focus["explanation_status"], "analyst_inference")
        self.assertEqual(focus["alignment_status"], "bounded_limit")
        self.assertIn("Orel's independent grounds", focus["alignment_limits"])
        self.assertEqual(cases["core-1941"]["explanation_status"], "unestablished")
        reason = next(row for row in tables["rationales"]
                      if row["rationale_id"] == "r-1941-beaver-direction")
        self.assertEqual((reason["support_mode"], reason["reason_target"]),
                         ("analyst_inference", "divergence_explanation"))
        self.assertIn("no direct rebuttal of Orel", reason["premises"])

    def test_tranche_endpoints_preserve_dialects_compounds_and_late_finite_cells(self):
        corpus, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] in {"1944", "1945", "1947"}}
        self.assertEqual(evidence["rt-alignment-believe-ws"]["diplomatic_form"], "geliefan")
        for page in ("243", "287"):
            record = evidence["rt-alignment-belly-ws-" + page]
            self.assertEqual((record["diplomatic_form"], record["printed_pages"]), ("bielg", page))
        for key in ("rt-complete-1945-007", "rt-complete-1945-013"):
            self.assertEqual(positions[key]["relation_to_row"], "compound_component")
        for literal in ("bebytst", "bebiet"):
            record = evidence["rt-alignment-offer-" + literal]
            self.assertEqual((record["diplomatic_form"], record["row_ids"]), (literal, "1947"))
        self.assertIn("second singular, explicitly late", evidence["rt-alignment-offer-bebytst"]["cell"])
        self.assertIn("third singular", evidence["rt-alignment-offer-bebiet"]["cell"])
        self.assertEqual(evidence["rt-complete-1947-001"]["asserted_stage"], "OE")
        self.assertEqual(positions["rt-complete-1947-002"]["attribution_status"], "endorsed")

    def test_tranche_supplement_receipts_point_to_exact_held_occurrences(self):
        import hashlib
        corpus, sources, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        receipts = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                    "reading_accountability/alignment-1941-1949-occurrences.tsv")
        self.assertEqual(len(receipts), 7)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                sheet = int(receipt["holding_sheet"])
                marker = (rf"### PAGE {sheet}\s*\n" if receipt["source_key"] == "RingeTaylor2014"
                          else rf"=== page {sheet:03d} ===\s*\n")
                block = re.split(marker, text, maxsplit=1)[1]
                block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                paragraphs = [part.strip() for part in re.split(r"\n\s*\n", block) if part.strip()]
                paragraph = paragraphs[int(receipt["paragraph"]) - 1]
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(),
                                 receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
                self.assertTrue(any(record["evidence_id"] in survey.ids(row["evidence_ids"])
                                    and row["source_key"] == record["source_key"]
                                    and row["row_id"] == record["row_ids"] for row in reviews))

    def test_tranche_reasons_do_not_turn_family_grade_or_accent_into_selected_cells(self):
        corpus, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] in {"1942", "1943", "1944", "1946"}}
        self.assertEqual(positions["kroonen-core-1942-3"]["attribution_status"], "rejected")
        self.assertEqual(positions["kroonen-core-1944-3"]["attribution_status"], "conditional")
        for key in ("kroonen-core-1946-3", "kroonen-core-1946-4"):
            self.assertEqual(positions[key]["attribution_status"], "conditional")
            self.assertEqual(positions[key]["relation_to_row"], "same_etymon_other_cell")
        self.assertIn("no accented reconstructed cells", evidence["kroonen-core-1946-1"]["argument"])
        reasons = {row["rationale_id"]: row for row in tables["rationales"]}
        for key, tags in (
            ("r-1944-rt-dialect-mutation", "following_j"),
            ("r-1945-rt-dialect-and-trigger", "following_i;trigger_loss"),
            ("r-1947-rt-finite-history", "following_i;trigger_loss"),
        ):
            self.assertEqual(reasons[key]["reason_target"], "position_support")
            self.assertEqual(reasons[key]["conditioning_tags"], tags)
        self.assertFalse(any("1943" in row["rationale_id"] and row["conditioning_tags"] == "coda_nasal"
                             for row in tables["rationales"]))

    def test_new_position_and_descriptive_reasons_are_not_divergence_explanations(self):
        corpus, _, forms, _ = survey.load()
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        reasons = {row["rationale_id"]: row for row in analytical["rationales"]}
        self.assertEqual(reasons["r-1934-rt-paradigm-position"]["reason_target"], "position_support")
        self.assertEqual(reasons["r-1934-rt-paradigm-position"]["conditioning_tags"],
                         "following_i;trigger_loss")
        self.assertEqual(reasons["r-1935-kroonen-secondary-u"]["reason_target"], "position_support")
        self.assertEqual(reasons["r-1940-rt-dated-optional-z"]["reason_target"], "descriptive_bridge")
        positions = {row["evidence_id"]: row for row in analytical["analyses"]
                     if row["row_id"] == "1935"}
        self.assertEqual(positions["kroonen-core-1935-4"]["stage_interpretation"], "north_germanic")
        self.assertEqual(positions["kroonen-core-1935-5"]["relation_to_row"],
                         "same_etymon_other_cell")

    def test_third_tranche_aligns_every_position_and_keeps_exact_limits(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        cases = {row["comparison_id"]: row for row in tables["comparisons"]}
        for row_id in map(str, range(1950, 1958)):
            with self.subTest(row_id=row_id):
                members = [row for row in tables["analyses"] if row["row_id"] == row_id]
                case = cases["core-" + row_id]
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(set(survey.ids(case["analysis_ids"])),
                                 {row["analysis_id"] for row in members})
                linked = survey.ids(case["alignment_evidence_ids"])
                self.assertEqual(len(linked), len(set(linked)))
                self.assertEqual(set(linked), {row["evidence_id"] for row in members})
                self.assertTrue(all(survey.analytical.feature_values(row) for row in members))
                self.assertTrue(all(row["attribution_status"] != "unclear" for row in members))
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertTrue(case["alignment_limits"])
        self.assertEqual(len({(row["row_id"], row["source_key"]) for row in reviews}),
                         len(reviews))
        with self.assertRaises(survey.analytical.AnalysisError):
            survey.analytical.require_alignment_complete(corpus, tables["comparisons"])

    def test_bind_root_representation_does_not_absorb_endings_or_gothic_comparator(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1950"}
        reasons = {row["rationale_id"]: row for row in tables["rationales"]}
        self.assertEqual(positions["rt-complete-1950-006"]["analytical_form"], "*bindands")
        self.assertEqual(positions["rt-complete-1950-006"]["stage_interpretation"], "other")
        self.assertEqual(positions["rt-complete-1950-006"]["relation_to_row"], "comparandum")
        self.assertEqual(positions["ringe-system-bind-underlying"]["attribution_status"], "conditional")
        self.assertEqual(reasons["r-1950-coda-nasal-positions"]["conditioning_tags"], "coda_nasal")
        bridge = reasons["r-1950-representation-bridge"]
        self.assertEqual((bridge["reason_target"], bridge["support_mode"]),
                         ("descriptive_bridge", "analyst_inference"))
        self.assertIn("Orel's bind e", bridge["premises"])
        self.assertIn("unstressed a", next(row for row in forms
                                          if row["evidence_id"] == "rt-complete-1950-010")["argument"])

    def test_birth_finite_family_and_blood_datives_are_not_selected_nouns(self):
        corpus, _, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] in {"1951", "1952"}}
        self.assertEqual(evidence["rt-alignment-birth-verbal-endpoint"]["diplomatic_form"],
                         "(ge)byrede")
        self.assertEqual(positions["rt-alignment-birth-verbal-endpoint"]["relation_to_row"],
                         "same_family")
        self.assertIn("light root syllables", evidence["rt-complete-1951-003"]["argument"])
        for suffix in ("005", "007", "009", "011"):
            self.assertEqual(positions["rt-complete-1952-" + suffix]["relation_to_row"],
                             "same_etymon_other_cell")
        for suffix in ("004", "006", "008", "010"):
            self.assertEqual(positions["rt-complete-1952-" + suffix]["relation_to_row"],
                             "comparandum")
        self.assertEqual(positions["rt-complete-1952-003"]["stage_interpretation"], "pgmc")
        self.assertEqual(positions["rt-complete-1952-010"]["stage_interpretation"], "pgmc")
        self.assertEqual(positions["rt-complete-1952-011"]["stage_interpretation"], "oe")
        self.assertEqual(evidence["rt-complete-1952-007"]["diplomatic_form"], "*blédé")
        self.assertEqual(evidence["ringe-alignment-blood-lexicon"]["diplomatic_form"], "*blōþą")
        review = next(row for row in reviews if row["row_id"] == "1954"
                      and row["source_key"] == "Ringe2017")
        self.assertEqual(review["status"], "evidence_found")
        self.assertIn("ringe-alignment-bone-lexicon", survey.ids(review["evidence_ids"]))

    def test_board_diagnostic_and_bone_origin_do_not_manufacture_rebuttal(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {row["evidence_id"]: row for row in forms}
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1953"}
        self.assertEqual(evidence["kroonen-alignment-board-secondary-zero"]["diplomatic_form"],
                         "*bruzda-")
        self.assertEqual(positions["kroonen-alignment-board-secondary-zero"]["relation_to_row"],
                         "same_family")
        focus = next(row for row in tables["comparisons"]
                     if row["comparison_id"] == "bone-origin-premises")
        self.assertEqual((focus["comparability"], focus["explanation_status"]),
                         ("substantive_difference", "analyst_inference"))
        self.assertIn("Do not equate", focus["premises"])
        reason = next(row for row in tables["rationales"]
                      if row["rationale_id"] == "r-1954-bone-origin-premises")
        self.assertEqual(reason["reason_target"], "divergence_explanation")
        self.assertEqual(len(survey.ids(reason["analysis_ids"])), 2)

    def test_book_plural_dates_borrowed_suffix_and_native_corruption_stay_separate(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1955"}
        for suffix in ("005", "007", "009"):
            self.assertEqual(positions["rt-complete-1955-" + suffix]["stage_interpretation"],
                             "northwest_germanic")
            self.assertEqual(positions["rt-complete-1955-" + suffix]["relation_to_row"],
                             "same_etymon_other_cell")
        self.assertEqual(positions["rt-complete-1955-010"]["stage_interpretation"], "pwgmc")
        self.assertEqual(positions["rt-complete-1955-001"]["attribution_status"], "endorsed")
        self.assertEqual(positions["rt-complete-1955-001"]["stage_interpretation"], "pwgmc")
        for suffix in ("002", "003"):
            self.assertEqual(positions["rt-complete-1955-" + suffix]["relation_to_row"], "comparandum")
        self.assertEqual(positions["rt-complete-1955-004"]["relation_to_row"], "same_family")
        self.assertEqual(positions["rt-alignment-book-227-ws"]["analytical_form"], "béé")
        self.assertEqual(positions["fulk-alignment-book-nominative"]["analytical_form"], "bōc")
        self.assertEqual(positions["fulk-alignment-book-nominative"]["relation_to_row"], "selected_cell")
        self.assertEqual(positions["fulk-complete-book-plural-p64"]["stage_interpretation"], "pgmc")

    def test_shared_book_and_bore_links_survive_individual_alignment(self):
        _, _, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for key, rows in (("orel-core-1942-01", {"1942", "1955"}),
                          ("orel-core-1942-04", {"1942", "1955"}),
                          ("orel-core-1956-01", {"1956", "2311", "2312"}),
                          ("kroonen-core-1956-1", {"1956", "2311", "2312"})):
            with self.subTest(evidence_id=key):
                self.assertTrue(rows <= set(survey.ids(evidence[key]["row_ids"])))
                for row_id in rows:
                    review = next(row for row in reviews if row["row_id"] == row_id
                                  and row["source_key"] == evidence[key]["source_key"])
                    self.assertIn(key, survey.ids(review["evidence_ids"]))

    def test_bosom_ownership_membership_compound_and_late_epenthesis_are_independent(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1957"}
        self.assertEqual(positions["kroonen-core-1957-1"]["attribution_status"], "endorsed")
        self.assertIn("conditional", survey.analytical.feature_values(
            positions["kroonen-core-1957-1"])["suffix"])
        self.assertEqual(positions["fulk-complete-bosom-stem-p114"]["attribution_status"], "illustrative")
        self.assertEqual(positions["fulk-complete-bosom-stem-p114"]["stage_interpretation"], "unspecified")
        self.assertEqual(positions["fulk-complete-bosom-counterexample"]["attribution_status"], "endorsed")
        self.assertEqual(positions["rt-complete-1957-004"]["relation_to_row"], "compound_component")
        self.assertEqual(positions["rt-complete-1957-001"]["analytical_form"], "*bésm")
        reason = next(row for row in tables["rationales"]
                      if row["rationale_id"] == "r-1957-fulk-sm-counterexample")
        self.assertEqual((reason["reason_target"], reason["conditioning_tags"]),
                         ("position_support", "counterexample"))

    def test_third_tranche_receipts_reproduce_literal_held_occurrences(self):
        import hashlib
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        receipts = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                    "reading_accountability/alignment-1950-1957-occurrences.tsv")
        self.assertEqual(len(receipts), 13)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                if receipt["holding_sheet"]:
                    sheet = int(receipt["holding_sheet"])
                    marker = (rf"### PAGE {sheet}\s*\n"
                              if receipt["source_key"] == "RingeTaylor2014"
                              else rf"=== page {sheet:03d} ===\s*\n")
                    block = re.split(marker, text, maxsplit=1)[1]
                    block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", block) if part.strip()]
                    paragraph = paragraphs[int(receipt["paragraph"]) - 1]
                else:
                    start = text.index("words of doubtful or unknown")
                    paragraph = text[start:text.index("Much more interesting", start)]
                self.assertEqual(paragraph, receipt["paragraph_text"])
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(),
                                 receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
        amendments = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                      "reading_accountability/alignment-1950-1957-amendments.tsv")
        for amendment in amendments:
            self.assertEqual(evidence[amendment["evidence_id"]][amendment["field"]],
                             amendment["new_value"])

    def test_fourth_tranche_reconciles_all_inherited_and_added_units(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        cases = {row["comparison_id"]: row for row in tables["comparisons"]}
        for row_id in map(str, range(1958, 1966)):
            members = [row for row in tables["analyses"] if row["row_id"] == row_id]
            case = cases["core-" + row_id]
            with self.subTest(row_id=row_id):
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(set(survey.ids(case["analysis_ids"])),
                                 {row["analysis_id"] for row in members})
                self.assertEqual(set(survey.ids(case["alignment_evidence_ids"])),
                                 {row["evidence_id"] for row in members})
                self.assertEqual(len(survey.ids(case["alignment_evidence_ids"])),
                                 len({row["evidence_id"] for row in members}))
                self.assertTrue(all(row["attribution_status"] != "unclear" for row in members))
                self.assertTrue(all(survey.analytical.feature_values(row) for row in members))
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertTrue(case["alignment_limits"])
        self.assertEqual(sum(row["scope"] == "core_triage" and
                             row["alignment_status"] == "bounded_limit"
                             for row in tables["comparisons"]), 73)
        self.assertEqual(len(reviews), 1379)
        with self.assertRaisesRegex(survey.analytical.AnalysisError, "320"):
            survey.analytical.require_alignment_complete(corpus, tables["comparisons"])

    def test_both_neuter_does_not_absorb_other_genders_three_or_two(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1958"}
        self.assertEqual(positions["kroonen-core-1958-2"]["relation_to_row"], "selected_cell")
        for suffix in ("3", "4", "5", "6", "7"):
            self.assertEqual(positions["kroonen-core-1958-" + suffix]["relation_to_row"],
                             "same_etymon_other_cell")
        self.assertEqual(positions["rt-complete-1958-006"]["stage_interpretation"], "pwgmc")
        self.assertEqual(positions["rt-complete-1958-006"]["relation_to_row"], "comparandum")
        self.assertEqual(positions["fulk-complete-both-compound"]["attribution_status"], "reported")
        self.assertEqual(positions["fulk-complete-both-cow"]["attribution_status"], "conditional")
        argument = next(row for row in forms if row["evidence_id"] == "rt-complete-1958-007")["argument"]
        self.assertIn("cannot be attributed to both", argument)

    def test_bottom_genitive_missing_m_and_cluster_attestations_stay_distinct(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1959"}
        self.assertEqual(positions["kroonen-core-1959-4"]["analytical_form"], "*buttaz")
        self.assertIn("genitive", survey.analytical.feature_values(
            positions["kroonen-core-1959-4"])["cell"])
        self.assertEqual(positions["kroonen-core-1959-4"]["relation_to_row"],
                         "same_etymon_other_cell")
        for suffix in ("003", "006"):
            self.assertEqual(positions["rt-complete-1959-" + suffix]["stage_interpretation"], "oe")
        for suffix in ("004", "005"):
            self.assertEqual(positions["rt-complete-1959-" + suffix]["relation_to_row"], "process")

    def test_strong_preterite_is_not_ring_or_weak_past_and_fulk_review_is_real(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1962" and row["comparison_unit"] != "lexical_identity"}
        for eid in ("orel-core-1962-01", "ringe-complete-bow-ring", "rt-complete-1962-001",
                    "rt-complete-1962-002", "rt-complete-1962-003", "rt-complete-1962-004"):
            self.assertEqual(positions[eid]["relation_to_row"], "same_family")
        for eid in ("kroonen-core-1962-1", "kroonen-core-1962-2",
                    "fulk-alignment-strong-bend-present"):
            self.assertEqual(positions[eid]["relation_to_row"], "same_etymon_other_cell")
        self.assertEqual(positions["kroonen-core-1962-2"]["analytical_form"], "*būgan-")
        review = next(row for row in reviews if row["row_id"] == "1962"
                      and row["source_key"] == "Fulk2018")
        self.assertIn("fulk-alignment-strong-bend-present", survey.ids(review["evidence_ids"]))
        self.assertEqual(review["status"], "discussion_only")
        ring = next(row for row in forms if row["evidence_id"] == "ringe-complete-bow-ring")
        self.assertIn("singular verbal preterite", ring["argument"])
        case = next(row for row in tables["comparisons"] if row["comparison_id"] == "core-1962")
        self.assertIn("RT55", case["alignment_limits"])
        self.assertTrue(all(row["row_id"] == "1961" for row in tables["analyses"]
                            if row["evidence_id"].startswith("rt-alignment-causative-past")))

    def test_weak_finite_cells_keep_stages_and_native_signs_without_restoration(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] == "1961"}
        for eid, form, stage in (
            ("rt-alignment-causative-present-nwg-3", "*baugipi", "northwest_germanic"),
            ("rt-alignment-causative-present-wg-3", "*baugibi", "pwgmc"),
            ("rt-alignment-causative-present-ws-3", "biegp", "oe"),
            ("rt-alignment-causative-present-kent-3", "ge-bégp", "oe"),
        ):
            self.assertEqual(positions[eid]["analytical_form"], form)
            self.assertEqual(positions[eid]["stage_interpretation"], stage)
            self.assertEqual(positions[eid]["relation_to_row"], "same_etymon_other_cell")
        self.assertEqual(positions["ringe-complete-bend"]["relation_to_row"], "same_family")

    def test_external_cognate_case_is_bounded_inference_not_direct_rebuttal(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        case = next(row for row in tables["comparisons"]
                    if row["comparison_id"] == "bend-external-cognates")
        reason = next(row for row in tables["rationales"]
                      if row["rationale_id"] == "r-bend-external-comparisons")
        self.assertEqual((case["comparability"], case["explanation_status"]),
                         ("substantive_difference", "analyst_inference"))
        self.assertEqual((reason["reason_target"], reason["support_mode"]),
                         ("divergence_explanation", "analyst_inference"))
        self.assertEqual(len(survey.ids(case["analysis_ids"])), 2)
        self.assertIn("not a direct rebuttal", case["conclusion"])
        self.assertIn("reason for rejection", reason["counterarguments"])

    def test_noun_bow_bower_gender_brand_homonyms_and_shared_links_are_preserved(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {row["evidence_id"]: row for row in forms}
        positions = {row["evidence_id"]: row for row in tables["analyses"]
                     if row["row_id"] in {"1963", "1964", "1965"}}
        self.assertEqual(positions["rt-complete-1963-003"]["stage_interpretation"], "oe")
        self.assertEqual(positions["ringe-complete-bow-noun-family"]["relation_to_row"], "same_family")
        self.assertIn("n-stem noun", survey.analytical.feature_values(
            positions["kroonen-core-1963-1"])["stem_class"])
        self.assertIn("dwell", evidence["orel-core-1964-01"]["argument"])
        self.assertIn("neuter reconstruction", survey.analytical.feature_values(
            positions["kroonen-core-1964-1"])["gender"])
        self.assertEqual(evidence["orel-core-1965-01"]["diplomatic_form"],
                         evidence["orel-core-1965-02"]["diplomatic_form"])
        self.assertNotEqual(positions["orel-core-1965-01"]["relation_to_row"],
                            positions["orel-core-1965-02"]["relation_to_row"])
        self.assertEqual(positions["kroonen-core-1965-1"]["relation_to_row"], "same_family")
        for row_id in ("1963", "2148"):
            self.assertIn(row_id, survey.ids(evidence["orel-core-1963-01"]["row_ids"]))
            review = next(row for row in reviews if row["row_id"] == row_id
                          and row["source_key"] == "Orel2003")
            self.assertIn("orel-core-1963-01", survey.ids(review["evidence_ids"]))

    def test_fourth_tranche_receipts_reproduce_original_occurrences_and_amendments(self):
        import hashlib
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        receipts = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                    "reading_accountability/alignment-1958-1965-occurrences.tsv")
        self.assertEqual(len(receipts), 20)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                if receipt["holding_sheet"]:
                    sheet = int(receipt["holding_sheet"])
                    marker = (rf"### PAGE {sheet}\s*\n"
                              if receipt["source_key"] == "RingeTaylor2014"
                              else rf"=== page {sheet:03d} ===\s*\n")
                    block = re.split(marker, text, maxsplit=1)[1]
                    block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                    paragraph = [part.strip() for part in re.split(r"\n\s*\n", block)
                                 if part.strip()][int(receipt["paragraph"]) - 1]
                else:
                    start = text.index(receipt["begin_anchor"])
                    paragraph = text[start:text.index(receipt["end_anchor"], start)]
                self.assertEqual(paragraph, receipt["paragraph_text"])
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(),
                                 receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
        amendments = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                      "reading_accountability/alignment-1958-1965-amendments.tsv")
        self.assertEqual(len(amendments), 7)
        for amendment in amendments:
            self.assertEqual(evidence[amendment["evidence_id"]][amendment["field"]],
                             amendment["new_value"])

    def test_fifth_tranche_aligns_every_position_without_new_consultations(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        cases = {row["comparison_id"]: row for row in tables["comparisons"]}
        for row_id in map(str, range(1966, 1974)):
            members = [p for p in tables["analyses"] if p["row_id"] == row_id]
            case = cases["core-" + row_id]
            with self.subTest(row_id=row_id):
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(set(survey.ids(case["analysis_ids"])),
                                 {p["analysis_id"] for p in members})
                self.assertEqual(set(survey.ids(case["alignment_evidence_ids"])),
                                 {p["evidence_id"] for p in members})
                self.assertTrue(all(p["attribution_status"] != "unclear" for p in members))
                self.assertTrue(all(survey.analytical.feature_values(p) for p in members))
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertTrue(case["alignment_limits"])
        self.assertEqual(len(reviews), 1379)

    def test_break_expected_antecedent_is_not_an_author_opposition(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {f["evidence_id"]: f for f in forms}
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1967"}
        self.assertEqual((evidence["alignment-break-expected-ur"]["diplomatic_form"],
                          evidence["alignment-break-expected-ur"]["printed_pages"]),
                         ("*burkanaz", "290"))
        self.assertIn("explicitly agrees", evidence["alignment-break-expected-ur"]["argument"])
        self.assertEqual(positions["alignment-break-possible-inaz"]["attribution_status"],
                         "conditional")
        for eid in ("alignment-break-past-sg", "alignment-break-past-pl",
                    "alignment-break-expected-ur", "rt-complete-1967-002"):
            self.assertEqual(positions[eid]["relation_to_row"], "same_etymon_other_cell")
        self.assertEqual(positions["rt-complete-1967-002"]["stage_interpretation"], "pgmc")
        self.assertEqual(positions["rt-complete-1967-003"]["relation_to_row"], "comparandum")
        self.assertEqual(evidence["rt-complete-1967-003"]["asserted_stage"], "Gothic")
        reason = next(r for r in tables["rationales"] if r["rationale_id"] == "r-1967-ur-ru-bridge")
        self.assertEqual(reason["reason_target"], "descriptive_bridge")
        self.assertFalse(any(c["scope"] == "focused_case" and c["row_ids"] == "1967"
                             and c["comparability"] == "substantive_difference"
                             for c in tables["comparisons"]))

    def test_breast_preferred_accounts_are_qualified_and_stage_scoped(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {f["evidence_id"]: f for f in forms}
        case = next(c for c in tables["comparisons"]
                    if c["comparison_id"] == "breast-paradigm-derivation")
        self.assertEqual(case["explanation_status"], "analyst_inference")
        self.assertIn("both", case["alignment_limits"])
        self.assertEqual(evidence["rt-complete-1968-001"]["asserted_stage"], "PNWGmc")
        self.assertEqual(evidence["alignment-breast-root"]["diplomatic_form"], "*brust-")
        position = next(p for p in tables["analyses"]
                        if p["evidence_id"] == "alignment-breast-derivation"
                        and p["comparison_unit"] == "process")
        self.assertEqual(position["attribution_status"], "conditional")
        breast = next(r for r in corpus if r["row_id"] == "1968")
        self.assertEqual((breast["proto"], breast["protoform"]), ("*brústz", "*bréustą"))

    def test_breeches_plural_does_not_date_a_pgmc_whole_word(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1969"}
        for eid in ("rt-complete-1969-001", "rt-complete-1969-004"):
            self.assertEqual(positions[eid]["stage_interpretation"], "northwest_germanic")
            self.assertEqual(positions[eid]["relation_to_row"], "selected_cell")
        self.assertEqual(positions["orel-core-1969-01"]["relation_to_row"],
                         "same_etymon_other_cell")
        self.assertEqual(positions["kroonen-core-1969-1"]["relation_to_row"],
                         "same_etymon_citation")
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "core-1969")
        self.assertIn("PGmc date", case["alignment_limits"])

    def test_bride_citation_origin_and_native_corruptions_stay_separate(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {f["evidence_id"]: f for f in forms}
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1970"}
        self.assertEqual(evidence["alignment-bride-gothic"]["diplomatic_form"], "*brūþiz")
        self.assertEqual(evidence["alignment-bride-gothic"]["asserted_stage"], "Gothic")
        self.assertEqual(evidence["rt-complete-1970-001"]["diplomatic_form"], "*bridiz")
        self.assertEqual(positions["orel-core-1970-01"]["attribution_status"], "endorsed")
        self.assertEqual(positions["kroonen-core-1970-1"]["attribution_status"], "endorsed")
        self.assertEqual(positions["alignment-bride-pgmc"]["stage_interpretation"], "pgmc")
        self.assertEqual(positions["rt-complete-1970-003"]["relation_to_row"], "selected_cell")

    def test_bring_comparanda_and_heavy_stem_endings_are_not_selected_inputs(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {f["evidence_id"]: f for f in forms}
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1971"}
        for eid in ("rt-complete-1971-002", "rt-complete-1971-003", "rt-complete-1971-004"):
            self.assertEqual(positions[eid]["relation_to_row"], "comparandum")
        self.assertEqual(evidence["rt-complete-1971-002"]["asserted_stage"], "pre-OE")
        self.assertEqual(positions["kroonen-core-1971-2"]["attribution_status"], "conditional")
        self.assertIn("HEAVY-STEM", evidence["rt-complete-1971-007"]["argument"])
        self.assertEqual(evidence["alignment-bring-oe-3sg"]["diplomatic_form"], "bringd")
        self.assertEqual(evidence["alignment-bring-north"]["diplomatic_form"], "tobringed")
        self.assertEqual(evidence["alignment-bring-heavy-stems"]["printed_pages"], "349-350")

    def test_brook_weak_history_and_optional_finite_cell_preserve_negative(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {f["evidence_id"]: f for f in forms}
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1972"}
        self.assertEqual(evidence["alignment-brook-pgmc-3sg"]["diplomatic_form"], "*brūki(j)iþ(i)")
        self.assertEqual(positions["alignment-brook-pgmc-3sg"]["relation_to_row"],
                         "same_etymon_other_cell")
        self.assertEqual(evidence["rt-complete-1972-002"]["asserted_stage"], "PGmc")
        self.assertEqual(positions["rt-complete-1972-002"]["relation_to_row"], "comparandum")
        review = next(r for r in reviews if r["row_id"] == "1972"
                      and r["source_key"] == "Kroonen2013")
        self.assertEqual((review["status"], review["evidence_ids"]), ("no_form_found", ""))
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "core-1972")
        self.assertEqual(case["explanation_status"], "unestablished")

    def test_buck_direction_is_inferred_without_merging_genitive_or_stage(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] == "1973" and p["comparison_unit"] == "source_citation"}
        case = next(c for c in tables["comparisons"]
                    if c["comparison_id"] == "buck-borrowing-direction")
        self.assertEqual(case["comparability"], "substantive_difference")
        self.assertEqual(case["explanation_status"], "analyst_inference")
        self.assertEqual(positions["kroonen-core-1973-4"]["attribution_status"], "conditional")
        self.assertEqual(positions["kroonen-core-1973-4"]["relation_to_row"],
                         "same_etymon_other_cell")
        self.assertEqual(positions["ringe-complete-buck"]["stage_interpretation"],
                         "northwest_germanic")
        self.assertEqual(positions["alignment-buck-oe"]["relation_to_row"], "selected_cell")
        self.assertEqual(positions["alignment-buck-bucca"]["relation_to_row"],
                         "same_etymon_other_cell")

    def test_fifth_tranche_receipts_reproduce_literals_and_amendments(self):
        import hashlib
        _, _, forms, _ = survey.load()
        evidence = {f["evidence_id"]: f for f in forms}
        receipts = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                    "reading_accountability/alignment-1966-1973-occurrences.tsv")
        self.assertEqual(len(receipts), 24)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                if receipt["holding_sheet"]:
                    sheet = int(receipt["holding_sheet"])
                    marker = (rf"### PAGE {sheet}\s*\n"
                              if receipt["source_key"] == "RingeTaylor2014"
                              else rf"=== page {sheet:03d} ===\s*\n")
                    block = re.split(marker, text, maxsplit=1)[1]
                    block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                    paragraph = [p.strip() for p in re.split(r"\n\s*\n", block)
                                 if p.strip()][int(receipt["paragraph"]) - 1]
                else:
                    start = text.index(receipt["begin_anchor"])
                    end = text.index(receipt["end_anchor"], start) + len(receipt["end_anchor"])
                    paragraph = text[start:end]
                self.assertEqual(paragraph, receipt["paragraph_text"])
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(),
                                 receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
                self.assertEqual(record["verification"], "text_checked")
        amendments = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                      "reading_accountability/alignment-1966-1973-amendments.tsv")
        self.assertEqual(len(amendments), 9)
        for amendment in amendments:
            self.assertEqual(evidence[amendment["evidence_id"]][amendment["field"]],
                             amendment["new_value"])

    def test_sixth_tranche_aligns_all_positions_and_preserves_actual_reviews(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        cases = {c["comparison_id"]: c for c in tables["comparisons"]}
        members = [p for p in tables["analyses"] if p["row_id"] in set(map(str, range(1974, 1982)))]
        self.assertEqual(len(members), 131)
        self.assertEqual(len(reviews), 1379)
        for row_id in map(str, range(1974, 1982)):
            positions = [p for p in members if p["row_id"] == row_id]
            case = cases["core-" + row_id]
            with self.subTest(row_id=row_id):
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertEqual(set(survey.ids(case["analysis_ids"])),
                                 {p["analysis_id"] for p in positions})
                self.assertEqual(set(survey.ids(case["alignment_evidence_ids"])),
                                 {p["evidence_id"] for p in positions})
                self.assertTrue(all(p["status"] == "reviewed"
                                    and p["attribution_status"] != "unclear" for p in positions))
                self.assertTrue(case["alignment_limits"])

    def test_calf_az_singular_does_not_infer_masculine_a_stem(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1975"}
        for eid in ("kroonen-core-1975-2", "ringe-complete-calf-a", "rt-complete-1975-001"):
            self.assertEqual(positions[eid]["relation_to_row"], "selected_cell")
            self.assertEqual(survey.analytical.feature_values(positions[eid])["gender"], "neuter")
            self.assertEqual(positions[eid]["analytical_form"], "*kalbaz")
        self.assertEqual(positions["kroonen-core-1975-3"]["relation_to_row"],
                         "same_etymon_other_cell")
        self.assertEqual(positions["rt-complete-1975-023"]["attribution_status"], "rejected")
        self.assertEqual(positions["rt-complete-1975-024"]["attribution_status"], "conditional")
        self.assertEqual(positions["rt-complete-1975-025"]["attribution_status"], "conditional")
        self.assertEqual(positions["rt-complete-1975-020"]["relation_to_row"], "comparandum")
        self.assertIn("egg", survey.analytical.feature_values(positions["rt-complete-1975-020"])["cell"])

    def test_identical_calf_genitive_plural_forms_keep_distinct_cells_and_occurrences(self):
        _, _, forms, _ = survey.load()
        evidence = {f["evidence_id"]: f for f in forms}
        for genitive, plural in (
            ("alignment-calf-merc-genitive", "alignment-calf-merc-plural-note"),
            ("alignment-calf-rt-genitive", "alignment-calf-rt-plural"),
        ):
            self.assertEqual(evidence[genitive]["diplomatic_form"], "calfur")
            self.assertEqual(evidence[plural]["diplomatic_form"], "calfur")
            self.assertIn("GEN.SG", evidence[genitive]["cell"])
            self.assertIn("NOM.-ACC.PL", evidence[plural]["cell"])
        receipts = {r["evidence_id"]: r for r in survey.read_table(
            survey.ROOT / survey.DIRECTORY / "reading_accountability/alignment-1974-1981-occurrences.tsv")}
        genitive = receipts["alignment-calf-rt-genitive"]
        plural = receipts["alignment-calf-rt-plural"]
        self.assertEqual(genitive["paragraph_sha256"], plural["paragraph_sha256"])
        self.assertNotEqual(genitive["start_char"], plural["start_char"])
        self.assertEqual((receipts["alignment-calf-merc-genitive"]["printed_pages"],
                          receipts["alignment-calf-merc-plural-note"]["printed_pages"]),
                         ("177", "178"))

    def test_calf_cognate_opposition_is_bounded_and_counterfactual_not_adopted(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        case = next(c for c in tables["comparisons"]
                    if c["comparison_id"] == "calf-greek-cognate-admissibility")
        reason = next(r for r in tables["rationales"] if r["rationale_id"] == "r-calf-greek-premises")
        self.assertEqual((case["comparability"], case["explanation_status"]),
                         ("substantive_difference", "analyst_inference"))
        self.assertEqual((reason["basis_type"], reason["reason_target"], reason["support_mode"]),
                         ("reflex_set", "divergence_explanation", "analyst_inference"))
        self.assertIn("not a direct rebuttal", case["conclusion"])
        self.assertFalse(any(f["diplomatic_form"] == "**kwalbiz-" for f in forms))
        process = next(f for f in forms if f["evidence_id"] == "alignment-calf-greek-rejection")
        self.assertEqual(process["printed_pages"], "278")
        self.assertIn("counterfactual **kwalbiz-", process["argument"])
        self.assertIn("probably PIE d", process["argument"])
        self.assertIn("before o", process["argument"])

    def test_chew_principal_parts_and_native_quantity_are_not_collapsed(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {f["evidence_id"]: f for f in forms}
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1976"}
        for eid, literal in (
            ("alignment-chew-pgmc-inf", "*kewwaną"),
            ("alignment-chew-pgmc-past-sg", "*kaww"),
            ("alignment-chew-pgmc-past-pl", "*ku(w)un"),
            ("alignment-chew-pgmc-ptc", "*kuwanaz"),
        ):
            self.assertEqual((evidence[eid]["diplomatic_form"], evidence[eid]["printed_pages"]),
                             (literal, "268"))
            self.assertEqual(positions[eid]["stage_interpretation"], "pgmc")
        self.assertEqual(positions["orel-core-1976-2"]["attribution_status"], "conditional")
        self.assertEqual(positions["alignment-chew-oe-inf"]["relation_to_row"], "selected_cell")
        self.assertEqual(positions["rt-complete-1976-001"]["analytical_form"], "*kewwang")
        self.assertEqual(positions["rt-complete-1976-004"]["analytical_form"], "céowan")
        self.assertEqual(positions["rt-complete-1976-002"]["stage_interpretation"], "pwgmc")

    def test_climb_reported_proposal_and_explicit_membership_limit_are_independent(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        evidence = {f["evidence_id"]: f for f in forms}
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1977"}
        self.assertEqual(evidence["orel-core-1977-3"]["quoted_author"], "Onions")
        self.assertEqual(positions["orel-core-1977-3"]["attribution_status"], "reported")
        self.assertEqual(positions["kroonen-core-1977-2"]["analytical_form"], "*klimb/pan-")
        self.assertEqual(positions["rt-complete-1977-001"]["stage_interpretation"], "pwgmc")
        self.assertEqual(positions["rt-complete-1977-002"]["stage_interpretation"], "oe")
        method = next(r for r in tables["rationales"] if r["rationale_id"] == "r-1977-pwgmc-method")
        self.assertEqual(method["basis_type"], "method")
        self.assertIn("possible accidental Gothic/Norse gaps", method["statement"])

    def test_comb_derivatives_burst_table_label_and_corn_consultations_stay_scoped(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] in {"1974", "1978"}}
        self.assertEqual(positions["rt-complete-1974-002"]["analytical_form"], "*Ih")
        self.assertEqual(positions["rt-complete-1974-002"]["relation_to_row"], "comparandum")
        for eid in ("rt-complete-1978-004", "rt-complete-1978-006",
                    "alignment-comb-factitive", "fulk-complete-index-comb-verb"):
            self.assertEqual(positions[eid]["relation_to_row"], "same_family")
        self.assertEqual(positions["rt-complete-1978-005"]["stage_interpretation"], "pgmc")
        self.assertEqual(positions["rt-complete-1978-006"]["stage_interpretation"], "other")
        preform = next(f for f in forms if f["evidence_id"] == "rt-complete-1978-006")
        self.assertEqual(preform["asserted_stage"], "pre-OE")
        self.assertEqual({r["source_key"] for r in reviews if r["row_id"] == "1979"},
                         {"Orel2003", "Kroonen2013", "Ringe2017"})

    def test_cow_selected_dative_dual_source_cell_and_origin_limits_are_preserved(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        cow = next(r for r in corpus if r["row_id"] == "1980")
        self.assertEqual((cow["proto"], cow["protoform"], cow["target"], cow["derivation_class"]),
                         ("*kōz", "*kūi", "cȳ", "late_analogy"))
        evidence = {f["evidence_id"]: f for f in forms}
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1980"}
        for eid in ("rt-complete-1980-007", "alignment-cow-rt-dative"):
            self.assertEqual(positions[eid]["relation_to_row"], "selected_cell")
            cell = survey.analytical.feature_values(positions[eid])["cell"]
            self.assertIn("DAT.SG", cell)
            self.assertIn("NOM.-ACC.PL", cell)
        self.assertEqual(positions["rt-complete-1980-003"]["relation_to_row"],
                         "same_etymon_other_cell")
        for eid in ("rt-complete-1980-005", "rt-complete-1980-006"):
            self.assertEqual(positions[eid]["relation_to_row"], "comparandum")
        for eid in ("rt-complete-1980-001", "rt-complete-1980-002", "rt-complete-1980-009"):
            self.assertEqual(positions[eid]["attribution_status"], "conditional")
        self.assertEqual(positions["ringe-complete-cow-u"]["stage_interpretation"], "unspecified")
        for eid in ("kroonen-core-1980-1", "kroonen-core-1980-3"):
            self.assertIn("DAT.SG", evidence[eid]["argument"])
            self.assertNotIn("selected OE plural is", evidence[eid]["argument"])
            self.assertNotIn("selected mutated plural is still", evidence[eid]["argument"])
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "cow-original-formation")
        self.assertEqual(case["explanation_status"], "analyst_inference")
        self.assertEqual(set(survey.ids(evidence["fulk-complete-both-cow"]["row_ids"])),
                         {"1958", "1980"})

    def test_craft_dictionary_stems_do_not_supply_selected_input_or_normalized_verb(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        craft = next(r for r in corpus if r["row_id"] == "1981")
        self.assertEqual((craft["proto"], craft["protoform"], craft["input_stage"], craft["derivation_class"]),
                         ("*kráftiz", "*kráftaz", "pgmc", "early_analogy"))
        positions = {p["evidence_id"]: p for p in tables["analyses"] if p["row_id"] == "1981"}
        self.assertEqual(positions["alignment-craft-demand-stative"]["analytical_form"], "*krabēn-")
        self.assertEqual(positions["orel-core-1981-3"]["analytical_form"], "*krafjanan")
        self.assertEqual(positions["alignment-craft-demand-stative"]["relation_to_row"], "same_family")
        self.assertFalse(any(p["relation_to_row"] == "selected_cell" for p in positions.values()))
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "core-1981")
        self.assertIn("stage", case["alignment_limits"])
        self.assertIn("kraftaz", case["alignment_limits"])

    def test_sixth_tranche_receipts_reproduce_literal_occurrences_and_annotations(self):
        import hashlib
        _, _, forms, _ = survey.load()
        evidence = {f["evidence_id"]: f for f in forms}
        receipts = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                    "reading_accountability/alignment-1974-1981-occurrences.tsv")
        self.assertEqual(len(receipts), 24)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                if receipt["holding_sheet"]:
                    sheet = int(receipt["holding_sheet"])
                    marker = (rf"### PAGE {sheet}\s*\n"
                              if receipt["source_key"] == "RingeTaylor2014"
                              else rf"=== page {sheet:03d} ===\s*\n")
                    block = re.split(marker, text, maxsplit=1)[1]
                    block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                    paragraph = [p.strip() for p in re.split(r"\n\s*\n", block)
                                 if p.strip()][int(receipt["paragraph"]) - 1]
                else:
                    start = text.index(receipt["begin_anchor"])
                    end = text.index(receipt["end_anchor"], start) + len(receipt["end_anchor"])
                    paragraph = text[start:end]
                self.assertEqual(paragraph, receipt["paragraph_text"])
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(),
                                 receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
                self.assertEqual(record["verification"], "text_checked")
        amendments = survey.read_table(survey.ROOT / survey.DIRECTORY /
                                      "reading_accountability/alignment-1974-1981-amendments.tsv")
        self.assertEqual(len(amendments), 12)
        for amendment in amendments:
            self.assertEqual(evidence[amendment["evidence_id"]][amendment["field"]],
                             amendment["new_value"])

    def test_seventh_tranche_aligns_every_position_without_settling_core_causes(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        members = [p for p in tables["analyses"]
                   if p["row_id"] in set(map(str, range(1982, 1990)))]
        self.assertEqual(len(members), 153)
        self.assertEqual(len({p["evidence_id"] for p in members}), 149)
        cases = {c["comparison_id"]: c for c in tables["comparisons"]}
        for row_id in map(str, range(1982, 1990)):
            positions = [p for p in members if p["row_id"] == row_id]
            case = cases["core-" + row_id]
            with self.subTest(row_id=row_id):
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertTrue(case["alignment_limits"])
                self.assertEqual(set(survey.ids(case["analysis_ids"])),
                                 {p["analysis_id"] for p in positions})
                self.assertEqual(set(survey.ids(case["alignment_evidence_ids"])),
                                 {p["evidence_id"] for p in positions})
                self.assertTrue(all(p["status"] == "reviewed"
                                    and p["attribution_status"] != "unclear" for p in positions))
        self.assertEqual(sum(r["source_key"] == "Ringe2017" for r in reviews), 192)
        self.assertEqual(sum(r["source_key"] == "Fulk2018" for r in reviews), 137)
        self.assertEqual(sum(r["source_key"] == "RingeTaylor2014" for r in reviews), 255)

    def test_cud_cognate_opposition_preserves_fulks_qualification_and_later_stage(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] == "1983" and p["comparison_unit"] != "lexical_identity"}
        case = next(c for c in tables["comparisons"]
                    if c["comparison_id"] == "cud-e-cognate-admissibility")
        self.assertEqual(case["explanation_status"], "analyst_inference")
        self.assertEqual(positions["alignment-cud-fulk-u-limit"]["attribution_status"],
                         "conditional")
        self.assertEqual(positions["alignment-cud-fulk-pie"]["stage_interpretation"], "pie")
        self.assertEqual(positions["rt-complete-1983-001"]["stage_interpretation"], "pwgmc")
        self.assertEqual(positions["kroonen-core-1983-4"]["relation_to_row"], "process")
        for eid in ("rt-complete-1983-003", "rt-complete-1983-004",
                    "alignment-cud-fulk-epinal", "alignment-cud-fulk-rounded"):
            self.assertEqual(positions[eid]["relation_to_row"], "compound_component")
        reason = next(r for r in tables["rationales"]
                      if r["rationale_id"] == "r-cud-e-admission-premises")
        self.assertEqual(reason["reason_target"], "divergence_explanation")
        self.assertEqual(reason["support_mode"], "analyst_inference")
        self.assertIn("following_u", survey.ids(reason["conditioning_tags"]))
        self.assertIn("not a PGmc i noun", next(c for c in tables["comparisons"]
                                               if c["comparison_id"] == "core-1983")["conclusion"])

    def test_deal_competing_roots_do_not_merge_thematic_noun_or_verb(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] == "1986" and p["comparison_unit"] != "stem_formation"}
        self.assertEqual(positions["kroonen-core-1986-1"]["relation_to_row"], "same_etymon_citation")
        for eid in ("alignment-deal-thematic", "alignment-deal-divide-verb",
                    "ringe-complete-deal-verb"):
            self.assertEqual(positions[eid]["relation_to_row"], "same_family")
        self.assertEqual(positions["ringe-complete-deal-noun"]["stage_interpretation"], "unspecified")
        self.assertEqual(positions["alignment-deal-fulk-explicit"]["stage_interpretation"], "pgmc")
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "deal-root-derivation")
        self.assertEqual((case["comparability"], case["explanation_status"]),
                         ("substantive_difference", "analyst_inference"))
        self.assertIn("lacks direct IE", case["conclusion"])

    def test_day_and_deed_paradigm_cells_uncertainty_and_source_dates_are_independent(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        for eid in ("rt-complete-1985-019", "rt-complete-1985-020",
                    "rt-complete-1987-034", "fulk-complete-index-day-plural"):
            self.assertEqual(positions[eid]["attribution_status"], "conditional")
        for eid in ("rt-complete-1985-005", "rt-complete-1985-006"):
            self.assertEqual(positions[eid]["stage_interpretation"], "pgmc")
            self.assertEqual(positions[eid]["relation_to_row"], "same_etymon_other_cell")
        self.assertEqual(positions["fulk-complete-day-s-proposal"]["attribution_status"], "reported")
        self.assertEqual(positions["fulk-complete-deed-accented-stem"]["analytical_form"], "*dē-ðí-")
        self.assertEqual(positions["rt-complete-1987-019"]["analytical_form"], "*dé&di")
        self.assertEqual(positions["rt-complete-1987-019"]["stage_interpretation"], "oe")
        gen, plural = (positions[eid] for eid in
                       ("alignment-deed-ringe-genitive", "alignment-deed-ringe-plural"))
        self.assertEqual(gen["analytical_form"], plural["analytical_form"])
        self.assertNotEqual(survey.analytical.feature_values(gen)["cell"],
                            survey.analytical.feature_values(plural)["cell"])

    def test_deed_does_not_adopt_seed_or_conditional_do_as_its_selected_noun(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        for suffix in ("012", "013", "016"):
            self.assertEqual(positions["rt-complete-1987-" + suffix]["relation_to_row"], "comparandum")
        self.assertEqual(positions["rt-complete-1987-012"]["stage_interpretation"], "northwest_germanic")
        for suffix in ("023", "024", "025"):
            self.assertEqual(positions["rt-complete-1987-" + suffix]["attribution_status"], "conditional")
            self.assertEqual(positions["rt-complete-1987-" + suffix]["relation_to_row"], "same_family")
        self.assertEqual(positions["rt-complete-1987-027"]["attribution_status"], "endorsed")
        self.assertEqual(positions["rt-complete-1987-027"]["relation_to_row"], "same_etymon_citation")

    def test_deer_retains_fulks_two_actual_animal_claims_and_ringes_adjective(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        for eid in ("alignment-deer-fulk-loan", "alignment-deer-fulk-retained-i"):
            self.assertEqual(positions[eid]["analytical_form"], "*diuriz")
            self.assertEqual(positions[eid]["stage_interpretation"], "pgmc")
            self.assertEqual(positions[eid]["relation_to_row"], "same_etymon_citation")
        self.assertEqual(positions["fulk-complete-index-deer-finnish-comparandum"]["relation_to_row"],
                         "same_etymon_citation")
        self.assertEqual(survey.analytical.feature_values(positions["alignment-deer-fulk-eu"])["vocalism"], "eu")
        self.assertEqual(positions["alignment-deer-ringe-dear-adjective"]["relation_to_row"], "comparandum")
        self.assertIn("adjective", survey.analytical.feature_values(
            positions["alignment-deer-ringe-dear-adjective"])["stem_class"])
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "core-1988")
        self.assertIn("compatibility", case["alignment_limits"])
        self.assertEqual(case["explanation_status"], "unestablished")

    def test_crop_membership_dale_gender_and_dew_component_do_not_become_equivalence(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        self.assertEqual(positions["ringe-complete-crop"]["stage_interpretation"], "northwest_germanic")
        self.assertEqual(survey.analytical.feature_values(positions["ringe-complete-crop"])["vocalism"], "o")
        self.assertEqual(positions["orel-core-1982-2"]["relation_to_row"], "same_family")
        self.assertEqual(positions["alignment-crop-iterative"]["relation_to_row"], "same_family")
        self.assertNotEqual(survey.analytical.feature_values(positions["orel-core-1984-1"])["gender"],
                            survey.analytical.feature_values(positions["orel-core-1984-2"])["gender"])
        self.assertEqual(positions["kroonen-core-1989-1"]["analytical_form"], "*dawwa/ō-")
        self.assertEqual(positions["ringe-complete-dew-honey-component"]["relation_to_row"],
                         "compound_component")

    def test_seventh_tranche_receipts_preserve_occurrences_and_amended_screen_history(self):
        import hashlib
        _, _, forms, _ = survey.load()
        evidence = {f["evidence_id"]: f for f in forms}
        directory = survey.ROOT / survey.DIRECTORY / "reading_accountability"
        receipts = survey.read_table(directory / "alignment-1982-1989-occurrences.tsv")
        self.assertEqual(len(receipts), 21)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                if receipt["holding_sheet"]:
                    sheet = int(receipt["holding_sheet"])
                    marker = (rf"### PAGE {sheet}\s*\n" if receipt["source_key"] == "RingeTaylor2014"
                              else rf"=== page {sheet:03d} ===\s*\n")
                    block = re.split(marker, text, maxsplit=1)[1]
                    block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                    paragraph = [p.strip() for p in re.split(r"\n\s*\n", block)
                                 if p.strip()][int(receipt["paragraph"]) - 1]
                else:
                    start = text.index(receipt["begin_anchor"])
                    end = text.index(receipt["end_anchor"], start) + len(receipt["end_anchor"])
                    paragraph = text[start:end]
                self.assertEqual(paragraph, receipt["paragraph_text"])
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(), receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
                self.assertEqual(record["verification"], "text_checked")
        amendments = survey.read_table(directory / "alignment-1982-1989-amendments.tsv")
        self.assertEqual(len(amendments), 18)
        manifests = {
            "Fulk2018/1983 applicability": next(r for r in survey.read_table(
                directory / "fulk-applicability.tsv") if r["row_id"] == "1983"),
            "Ringe2017/1988 applicability": next(r for r in survey.read_table(
                directory / "ringe-applicability.tsv") if r["row_id"] == "1988"),
        }
        for amendment in amendments:
            record = manifests.get(amendment["evidence_id"], evidence.get(amendment["evidence_id"]))
            self.assertEqual(record[amendment["field"]], amendment["new_value"])
        self.assertIn("Historical initial extraction limit", manifests["Fulk2018/1983 applicability"]["limits"])
        self.assertIn("Historical initial screen", manifests["Ringe2017/1988 applicability"]["scope_assessment"])

    def test_ninth_tranche_retains_all_members_and_bounded_whole_row_causes(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        members = [p for p in tables["analyses"]
                   if 1998 <= int(p["row_id"]) <= 2005]
        self.assertEqual((len(members), len({p["evidence_id"] for p in members})), (176, 172))
        for row_id in map(str, range(1998, 2006)):
            case = next(c for c in tables["comparisons"] if c["comparison_id"] == "core-" + row_id)
            positions = [p for p in members if p["row_id"] == row_id]
            with self.subTest(row_id=row_id):
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertTrue(case["alignment_limits"])
                self.assertEqual(set(survey.ids(case["analysis_ids"])), {p["analysis_id"] for p in positions})
                self.assertEqual(set(survey.ids(case["alignment_evidence_ids"])), {p["evidence_id"] for p in positions})
                self.assertTrue(all(p["status"] == "reviewed" and p["attribution_status"] != "unclear"
                                    for p in positions))
        self.assertEqual(len(reviews), 1379)
        self.assertEqual(next(c for c in tables["comparisons"]
                             if c["comparison_id"] == "core-2004")["comparability"], "different_units")

    def test_drive_intensive_is_not_causative_and_finite_cells_are_not_infinitives(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] == "1998" and p["comparison_unit"] != "lexical_identity"}
        derived = positions["ringe-complete-drive-causative"]
        self.assertEqual(derived["stage_interpretation"], "unspecified")
        self.assertEqual(derived["relation_to_row"], "same_family")
        self.assertIn("intensive/iterative", survey.analytical.feature_values(derived)["cell"])
        evidence = {f["evidence_id"]: f for f in forms}
        self.assertEqual(evidence["ringe-complete-drive-causative"]["cell"], "intensive/iterative infinitive")
        self.assertIn("intensive/iterative", evidence["ringe-complete-drive"]["argument"])
        self.assertEqual(positions["ringe-complete-drive"]["stage_interpretation"], "pgmc")
        for eid in ("alignment-drive-rt-2sg", "alignment-drive-rt-3sg"):
            self.assertEqual(positions[eid]["relation_to_row"], "same_etymon_other_cell")
            self.assertEqual(positions[eid]["stage_interpretation"], "oe")
        self.assertIn("not offer", survey.analytical.feature_values(positions["rt-complete-1998-012"])["cell"])

    def test_earth_coordinated_stage_does_not_date_dictionary_or_selected_accusative(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        self.assertEqual(positions["rt-complete-1999-004"]["stage_interpretation"], "pwgmc")
        self.assertEqual(positions["kroonen-core-1999-1"]["stage_interpretation"], "unspecified")
        self.assertEqual(positions["ringe-complete-earth-material"]["relation_to_row"], "same_family")
        self.assertEqual(positions["alignment-earth-fulk-accusative"]["relation_to_row"], "same_etymon_other_cell")
        self.assertIn("galgu", next(f for f in forms
                                   if f["evidence_id"] == "alignment-earth-fulk-accusative")["argument"])

    def test_eat_long_preterite_and_eel_awl_do_not_become_selected_present_ancestors(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        past = positions["alignment-eat-fulk-preterite"]
        self.assertEqual((past["stage_interpretation"], past["relation_to_row"]),
                         ("pgmc", "same_etymon_other_cell"))
        self.assertEqual(survey.analytical.feature_values(positions["fulk-complete-eat-infinitive"])["quantity"],
                         "short")
        self.assertIn("not feed/grow", survey.analytical.feature_values(positions["kroonen-core-2001-1"])["cell"])
        eel = next(f for f in forms if f["evidence_id"] == "alignment-eel-kroonen-awl-crossreferences")
        self.assertEqual(eel["form_kind"], "process")
        self.assertEqual(eel["printed_pages"], "19,116-117")
        self.assertIn("problematic", eel["argument"])

    def test_fall_gemination_explanation_is_inferred_not_direct_rebuttal(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "fall-segmentation-gemination")
        self.assertEqual(case["explanation_status"], "analyst_inference")
        self.assertIn("not evidence that Orel explicitly denies", case["conclusion"])
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        self.assertEqual(positions["rt-complete-2002-005"]["relation_to_row"], "comparandum")
        self.assertEqual(positions["rt-complete-2002-005"]["stage_interpretation"], "unspecified")
        self.assertEqual(positions["rt-complete-2002-005"]["comparison_unit"], "printed_representation")
        self.assertIn("metalinguistic", survey.analytical.feature_values(positions["rt-complete-2002-005"])["cell"])
        evidence = {f["evidence_id"]: f for f in forms}
        self.assertEqual(evidence["rt-complete-2002-005"]["form_kind"], "attestation")
        self.assertEqual(evidence["alignment-fall-kroonen-nasal-preform"]["diplomatic_form"], "*pehзl-né-")
        self.assertEqual(evidence["alignment-fall-fulk-preterite"]["diplomatic_form"], "feol(1)")

    def test_fare_expected_cells_gothic_and_metalinguistic_forms_remain_separate(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        for number in range(1, 7):
            self.assertEqual(positions[f"rt-complete-2003-{number:03d}"]["attribution_status"], "conditional")
        for number in (24, 25, 26):
            p = positions[f"rt-complete-2003-{number:03d}"]
            self.assertEqual((p["relation_to_row"], p["stage_interpretation"]), ("comparandum", "other"))
            self.assertIn("Gothic", survey.analytical.feature_values(p)["cell"])
        self.assertEqual(positions["orel-core-2003-2"]["attribution_status"], "reported")
        self.assertEqual(positions["rt-complete-2003-008"]["relation_to_row"], "process")
        self.assertEqual(positions["rt-complete-2003-008"]["comparison_unit"], "printed_representation")
        self.assertEqual(positions["rt-complete-2003-034"]["relation_to_row"], "comparandum")
        self.assertIn("groan", survey.analytical.feature_values(positions["rt-complete-2003-034"])["cell"])
        self.assertEqual(positions["rt-complete-2003-043"]["attribution_status"], "conditional")

    def test_fasting_and_calf_suffixes_do_not_quote_fastening_or_father_cells(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        fast = positions["ringe-complete-fast"]
        self.assertEqual((fast["relation_to_row"], fast["stage_interpretation"]), ("same_family", "pgmc"))
        self.assertIn("stative", survey.analytical.feature_values(fast)["stem_class"])
        self.assertEqual(positions["rt-complete-2004-005"]["relation_to_row"], "selected_cell")
        self.assertEqual(positions["rt-complete-2004-003"]["attribution_status"], "conditional")
        self.assertIn("uncertainty independent", survey.analytical.feature_values(positions["rt-complete-2004-003"])["cell"])
        for number in range(9, 13):
            p = positions[f"rt-complete-2005-{number:03d}"]
            self.assertEqual(p["relation_to_row"], "comparandum")
            self.assertIn("calf", survey.analytical.feature_values(p)["cell"])
        self.assertEqual(positions["rt-complete-2005-011"]["attribution_status"], "rejected")
        self.assertEqual(positions["rt-complete-2005-012"]["attribution_status"], "rejected")
        self.assertIn("GEN.SG", survey.analytical.feature_values(positions["alignment-father-fulk-anglian-genitive"])["cell"])
        self.assertEqual(positions["alignment-father-rt-donor"]["stage_interpretation"], "oe")
        self.assertIn("mechanism unexplained", next(f for f in forms
                        if f["evidence_id"] == "alignment-father-rt-donor")["argument"])

    def test_ninth_tranche_literal_receipts_and_annotation_amendments(self):
        import hashlib
        _, _, forms, _ = survey.load()
        evidence = {f["evidence_id"]: f for f in forms}
        directory = survey.ROOT / survey.DIRECTORY / "reading_accountability"
        receipts = survey.read_table(directory / "alignment-1998-2005-occurrences.tsv")
        self.assertEqual(len(receipts), 23)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                sheet = int(receipt["holding_sheet"])
                marker = (rf"### PAGE {sheet}\s*\n" if receipt["source_key"] == "RingeTaylor2014"
                          else rf"=== page {sheet:03d} ===\s*\n")
                block = re.split(marker, text, maxsplit=1)[1]
                block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                paragraph = [p.strip() for p in re.split(r"\n\s*\n", block)
                             if p.strip()][int(receipt["paragraph"]) - 1]
                self.assertEqual(paragraph, receipt["paragraph_text"])
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(), receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["verification"], "text_checked")
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
        amendments = survey.read_table(directory / "alignment-1998-2005-amendments.tsv")
        self.assertEqual(len(amendments), 20)
        for amendment in amendments:
            self.assertEqual(evidence[amendment["evidence_id"]][amendment["field"]], amendment["new_value"])
            self.assertTrue(amendment["source_basis"])
            self.assertNotEqual(amendment["old_value"], amendment["new_value"])

    def test_eighth_tranche_has_all_individual_positions_and_bounded_core_causes(self):
        corpus, _, forms, reviews = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        members = [p for p in tables["analyses"]
                   if p["row_id"] in set(map(str, range(1990, 1998)))]
        self.assertEqual((len(members), len({p["evidence_id"] for p in members})),
                         (138, 133))
        for row_id in map(str, range(1990, 1998)):
            case = next(c for c in tables["comparisons"]
                        if c["comparison_id"] == "core-" + row_id)
            positions = [p for p in members if p["row_id"] == row_id]
            with self.subTest(row_id=row_id):
                self.assertEqual(case["alignment_status"], "bounded_limit")
                self.assertEqual(case["explanation_status"], "unestablished")
                self.assertTrue(case["alignment_limits"])
                self.assertEqual(set(survey.ids(case["analysis_ids"])),
                                 {p["analysis_id"] for p in positions})
                self.assertEqual(set(survey.ids(case["alignment_evidence_ids"])),
                                 {p["evidence_id"] for p in positions})
                self.assertTrue(all(p["status"] == "reviewed"
                                    and p["attribution_status"] != "unclear" for p in positions))
        self.assertEqual(len(reviews), 1379)

    def test_do_direct_rebuttal_is_later_present_history_not_pgmc_root_verdict(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        case = next(c for c in tables["comparisons"]
                    if c["comparison_id"] == "do-present-metrical-history")
        reason = next(r for r in tables["rationales"]
                      if r["rationale_id"] == "r-do-direct-metrical-rebuttal")
        self.assertEqual((case["comparability"], case["explanation_status"]),
                         ("substantive_difference", "source_explicit"))
        self.assertEqual((reason["reason_target"], reason["support_mode"]),
                         ("divergence_explanation", "source_explicit"))
        self.assertIn("metrical", reason["statement"])
        self.assertIn("not a resolved PGmc root", case["conclusion"])
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] == "1991" and p["comparison_unit"] != "process"}
        self.assertEqual(positions["alignment-do-fulk-thematic-2sg"]["stage_interpretation"], "other")
        self.assertEqual(positions["alignment-do-fulk-thematic-2sg"]["attribution_status"], "conditional")
        self.assertEqual(positions["alignment-do-fulk-past-du"]["stage_interpretation"], "unspecified")
        evidence = {f["evidence_id"]: f for f in forms}
        self.assertEqual(evidence["alignment-do-fulk-thematic-2sg"]["asserted_stage"], "pre-OE")
        self.assertEqual(evidence["alignment-do-fulk-explicit-infinitive"]["diplomatic_form"],
                         '*dō-ana"')
        self.assertEqual(evidence["fulk-complete-index-do-infinitive"]["diplomatic_form"], "dō-anaⁿ")

    def test_do_edition_cells_homonyms_and_rejected_proposals_are_separate(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] == "1991"}
        evidence = {f["evidence_id"]: f for f in forms}
        table = positions["rt-complete-1991-001"]
        self.assertEqual((table["stage_interpretation"], table["attribution_status"]),
                         ("pwgmc", "endorsed"))
        self.assertIn("subjunctive3PL", survey.analytical.feature_values(table)["cell"])
        self.assertEqual(evidence["rt-complete-1991-001"]["form_kind"], "attestation")
        self.assertIn("Original extractor", evidence["rt-complete-1991-001"]["argument"])
        self.assertEqual(positions["rt-complete-1991-015"]["relation_to_row"], "comparandum")
        self.assertIn("DEEM", survey.analytical.feature_values(positions["rt-complete-1991-015"])["cell"])
        for number in (14, 20, 21, 42, 43, 44):
            self.assertEqual(positions[f"rt-complete-1991-{number:03d}"]["attribution_status"], "rejected")
        for number in (29, 30):
            p = positions[f"rt-complete-1991-{number:03d}"]
            self.assertEqual(p["attribution_status"], "reported")
            self.assertIn("not 2017", survey.analytical.feature_values(p)["cell"])
        self.assertEqual(positions["rt-complete-1991-028"]["attribution_status"], "endorsed")
        self.assertEqual(positions["alignment-do-ringe-done-preferred"]["analytical_form"], "*dēnaz")
        self.assertEqual(positions["alignment-do-ringe-segmented"]["analytical_form"], "*dō- ną?")
        self.assertEqual(positions["alignment-do-ringe-present-participle-rival"]["analytical_form"], "*dōnþ-??")
        self.assertEqual(positions["alignment-do-ringe-done-less-likely"]["attribution_status"], "conditional")
        self.assertNotEqual(survey.analytical.feature_values(positions["rt-complete-1991-036"])["cell"],
                            survey.analytical.feature_values(positions["rt-complete-1991-038"])["cell"])

    def test_dream_roots_and_reported_g_rival_are_not_one_notational_difference(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]
                     if p["row_id"] == "1995"}
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "dream-root-derivation")
        self.assertEqual(case["explanation_status"], "analyst_inference")
        for eid in ("orel-core-1995-3", "orel-core-1995-4"):
            self.assertEqual(positions[eid]["attribution_status"], "reported")
        self.assertEqual(positions["orel-core-1995-2"]["attribution_status"], "endorsed")
        self.assertEqual(positions["alignment-dream-kroonen-verb"]["analytical_form"], "*dreugan-")
        self.assertIn("not specified", survey.analytical.feature_values(
            positions["alignment-dream-kroonen-verb"])["cell"])
        self.assertNotIn("notation", survey.ids(case["type_tags"]))

    def test_drink_family_keeps_selected_noun_finite_cells_and_cluster_labels_separate(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {(p["row_id"], p["evidence_id"]): p for p in tables["analyses"]}
        self.assertEqual(positions["1996", "kroonen-core-1997-1"]["relation_to_row"], "same_family")
        self.assertEqual(positions["1997", "kroonen-core-1997-1"]["relation_to_row"], "same_etymon_citation")
        causal = positions["1996", "ringe-complete-drench-causative"]
        self.assertEqual((causal["stage_interpretation"], causal["relation_to_row"]), ("pgmc", "same_family"))
        self.assertIn("causative infinitive", survey.analytical.feature_values(causal)["cell"])
        self.assertEqual(positions["1997", "orel-core-1997-2"]["attribution_status"], "conditional")
        self.assertEqual(positions["1997", "rt-complete-1997-001"]["relation_to_row"], "process")
        self.assertEqual(positions["1997", "rt-complete-1997-008"]["relation_to_row"], "comparandum")
        self.assertIn("feolan", survey.analytical.feature_values(
            positions["1997", "rt-complete-1997-008"])["cell"])
        self.assertEqual(positions["1997", "rt-complete-1997-011"]["relation_to_row"], "selected_cell")
        self.assertEqual(positions["1997", "alignment-drink-rt-3sg"]["analytical_form"], "drincb")
        self.assertEqual(positions["1997", "alignment-drink-ringe-past-plural"]["stage_interpretation"], "pgmc")
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "core-1996")
        self.assertIn("attestation", case["alignment_limits"])

    def test_dill_door_dough_and_research_only_dove_keep_qualifications(self):
        corpus, _, forms, _ = survey.load()
        tables = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {p["evidence_id"]: p for p in tables["analyses"]}
        for eid in ("dill-kroonen-original-nominative", "dill-kroonen-original-genitive",
                    "dill-kroonen-rounded-i-stem", "dill-kroonen-rounded-ja-stem"):
            self.assertEqual(positions[eid]["attribution_status"], "conditional")
        self.assertIn("ACC.SG", survey.analytical.feature_values(positions["alignment-dill-fulk-accusative"])["cell"])
        self.assertEqual(positions["alignment-door-kroonen-i-stem"]["attribution_status"], "conditional")
        self.assertEqual(positions["alignment-door-kroonen-o-stem"]["attribution_status"], "endorsed")
        self.assertEqual(positions["rt-complete-1992-002"]["relation_to_row"], "same_family")
        self.assertNotEqual(survey.analytical.feature_values(positions["kroonen-core-1993-1"])["gender"],
                            survey.analytical.feature_values(positions["orel-core-1993-1"])["gender"])
        dove = next(r for r in corpus if r["row_id"] == "1994")
        self.assertEqual((dove["runnable"], dove["target"]), ("0", "-"))
        case = next(c for c in tables["comparisons"] if c["comparison_id"] == "core-1994")
        self.assertIn("onomatopoeia", case["alignment_limits"])
        self.assertIn("pelican", survey.analytical.feature_values(positions["orel-core-1994-1"])["cell"])

    def test_eighth_tranche_primary_occurrences_and_source_amendments(self):
        import hashlib
        _, _, forms, _ = survey.load()
        evidence = {f["evidence_id"]: f for f in forms}
        directory = survey.ROOT / survey.DIRECTORY / "reading_accountability"
        receipts = survey.read_table(directory / "alignment-1990-1997-occurrences.tsv")
        self.assertEqual(len(receipts), 27)
        for receipt in receipts:
            with self.subTest(evidence_id=receipt["evidence_id"]):
                record = evidence[receipt["evidence_id"]]
                text = (survey.ROOT / record["basis"]).read_text()
                if receipt["holding_sheet"]:
                    sheet = int(receipt["holding_sheet"])
                    marker = (rf"### PAGE {sheet}\s*\n" if receipt["source_key"] == "RingeTaylor2014"
                              else rf"=== page {sheet:03d} ===\s*\n")
                    block = re.split(marker, text, maxsplit=1)[1]
                    block = re.split(r"### PAGE \d+|=== page \d+ ===", block, maxsplit=1)[0]
                    paragraph = [p.strip() for p in re.split(r"\n\s*\n", block)
                                 if p.strip()][int(receipt["paragraph"]) - 1]
                else:
                    start = text.index(receipt["begin_anchor"])
                    end = text.index(receipt["end_anchor"], start) + len(receipt["end_anchor"])
                    paragraph = text[start:end]
                self.assertEqual(paragraph, receipt["paragraph_text"])
                self.assertEqual(hashlib.sha256(paragraph.encode()).hexdigest(), receipt["paragraph_sha256"])
                self.assertEqual(paragraph[int(receipt["start_char"]):int(receipt["end_char"])],
                                 record["diplomatic_form"])
                self.assertEqual(record["printed_pages"], receipt["printed_pages"])
                self.assertEqual(record["verification"], "text_checked")
        amendments = survey.read_table(directory / "alignment-1990-1997-amendments.tsv")
        self.assertEqual(len(amendments), 5)
        for amendment in amendments:
            self.assertEqual(evidence[amendment["evidence_id"]][amendment["field"]], amendment["new_value"])
            self.assertNotIn(amendment["field"], {"diplomatic_form", "comparison_form", "form_kind", "verification"})

    def test_family_and_conditional_belief_forms_do_not_become_selected_verbs(self):
        corpus, _, forms, _ = survey.load()
        analytical = survey.load_analysis(survey.ROOT, corpus, forms)
        positions = {row["evidence_id"]: row for row in analytical["analyses"]
                     if row["row_id"] == "1944"}
        for key in ("kroonen-core-1944-1", "kroonen-core-1944-2",
                    "kroonen-core-1944-3", "kroonen-core-1944-4",
                    "kroonen-core-1944-5"):
            self.assertEqual(positions[key]["relation_to_row"], "same_family")
        self.assertEqual(positions["kroonen-core-1944-3"]["attribution_status"], "conditional")
        self.assertEqual(positions["orel-core-1944-01"]["analytical_form"], "*laubjanan")
        self.assertEqual(positions["orel-core-1944-01"]["attribution_status"], "endorsed")

    def test_both_selected_input_annotation_does_not_substitute_a_masculine_cell(self):
        corpus, _, forms, _ = survey.load()
        both = next(row for row in corpus if row["row_id"] == "1958")
        self.assertEqual((both["proto"], both["protoform"], both["target"]),
                         ("*bō", "*bō", "bū"))
        formation = next(form for form in forms if form["evidence_id"] == "orel-core-1958-02")
        self.assertEqual((formation["diplomatic_form"], formation["printed_pages"]),
                         ("*bō-jenō", "52"))
        self.assertIn("selected neuter *bō", formation["argument"])
        self.assertNotIn("selected *báiðai", formation["argument"])

    def test_ringe_extraction_preserves_surface_underlying_and_other_cells(self):
        _, _, forms, reviews = survey.load()
        evidence = {form["evidence_id"]: form for form in forms}
        self.assertEqual(evidence["ringe-system-sit"]["diplomatic_form"], "*sitjaną")
        self.assertEqual(evidence["ringe-system-sit-root"]["diplomatic_form"], "*set-")
        self.assertEqual(evidence["ringe-system-bind-underlying"]["diplomatic_form"], "*/bend-/")
        self.assertEqual(evidence["ringe-system-bind-1"]["diplomatic_form"], "*bindaną")
        self.assertIn("possibility", evidence["ringe-system-bind-1"]["argument"])
        self.assertEqual(evidence["ringe-system-fight-wg"]["asserted_stage"], "pwgmc")
        self.assertEqual(evidence["ringe-system-fight-wg"]["diplomatic_form"], "*fehtan")
        self.assertEqual(evidence["ringe-system-sup"]["confidence"], "medium")
        self.assertIn("Perhaps", evidence["ringe-system-sup"]["argument"])
        self.assertEqual(evidence["ringe-system-wool-nom"]["diplomatic_form"], "*wullō")
        self.assertEqual(evidence["ringe-system-wool-acc"]["diplomatic_form"], "*wullǭ")
        self.assertEqual(evidence["ringe-system-do-past-pl"]["row_ids"], "1991")
        self.assertEqual(evidence["ringe-system-deed"]["row_ids"], "1987")
        self.assertEqual(evidence["ringe-system-bid-ask"]["row_ids"], "1948")
        self.assertEqual(evidence["ringe-system-learn-no"]["row_ids"], "2095;2313;2314")
        sit = next(r for r in reviews if r["row_id"] == "2193" and r["source_key"] == "Ringe2017")
        self.assertEqual(sit["status"], "evidence_found")
        self.assertIn("raising-ringe-high-front", sit["evidence_ids"])
        self.assertIn("ringe-system-sit", sit["evidence_ids"])
        self.assertIn("no whole-word PGmc sit", sit["assessment"])
        batch = [form for form in forms if form["evidence_id"].startswith("ringe-system-")]
        self.assertEqual(len(batch), 49)
        self.assertTrue(all(not set(survey.ids(form["row_ids"])) &
                            {"1947", "2122", "2161", "2292", "2293"} for form in batch))


class CoreCompletionTests(unittest.TestCase):
    def setUp(self):
        self.corpus = [{"row_id": "1"}, {"row_id": "2"}]
        self.sources = [{
            "source_key": key, "role": "reconstruction",
            "edition_status": "verified", "conventions_status": "verified",
            "consultation_mode": "core_dictionary",
        } for key in survey.CORE_SOURCES]
        self.reviews = [{
            "row_id": row["row_id"], "source_key": source["source_key"],
            "status": status,
        } for source in self.sources
          for row, status in zip(self.corpus, ("evidence_found", "no_form_found"))]

    def test_complete_dispositions_do_not_require_all_positive_evidence(self):
        survey.require_core_complete(self.corpus, self.sources, self.reviews)
        self.reviews[0]["status"] = "verification_gap"
        self.reviews[1]["status"] = "discussion_only"
        survey.require_core_complete(self.corpus, self.sources, self.reviews)

    def test_missing_review_identifies_the_actual_source_and_row(self):
        self.reviews.pop()
        with self.assertRaisesRegex(survey.SurveyError, "Kroonen2013/2"):
            survey.require_core_complete(self.corpus, self.sources, self.reviews)

    def test_deleted_or_excluded_core_source_cannot_make_completion_vacuous(self):
        self.sources[-1]["role"] = "excluded"
        with self.assertRaisesRegex(survey.SurveyError, "missing included.*Kroonen2013"):
            survey.require_core_complete(self.corpus, self.sources, self.reviews)

    def test_unreviewed_core_method_prevents_completion(self):
        self.sources[0]["conventions_status"] = "unreviewed"
        with self.assertRaisesRegex(survey.SurveyError, "conventions remain unreviewed"):
            survey.require_core_complete(self.corpus, self.sources, self.reviews)


class LiveSurveyTests(unittest.TestCase):
    def test_complete_population_includes_six_nonrunnable_rows(self):
        corpus, sources, forms, reviews = survey.load()
        self.assertEqual(len(corpus), 393)
        self.assertEqual({row["row_id"] for row in corpus if row["runnable"] == "0"},
                         {"1935", "1947", "1948", "1994", "2156", "2218"})
        self.assertEqual(sum(row["stage_basis"] == "explicit_sidecar" for row in corpus), 81)
        self.assertFalse(survey.incomplete(
            sources, survey.coverage_rows(corpus, sources, reviews)))
        ledger = survey.ledger_text(
            corpus, sources, forms, survey.coverage_rows(corpus, sources, reviews))
        self.assertTrue(ledger.endswith("\n"))
        self.assertFalse(ledger.endswith("\n\n"))

    def test_cud_folios_stage_and_morphology_are_not_harmonized(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        self.assertEqual(evidence["cud-kroonen-stem"]["printed_pages"], "315")
        self.assertEqual(evidence["cud-orel-formation"]["printed_pages"], "227")
        self.assertEqual(evidence["cud-orel-formation"]["diplomatic_form"], "*kweđwō(n)")
        self.assertEqual(evidence["cud-ringe-taylor-wgmc"]["printed_pages"], "323")
        self.assertEqual(evidence["cud-ringe-taylor-wgmc"]["asserted_stage"], "PWGmc")
        self.assertEqual(evidence["cud-clark-hall-variants"]["printed_pages"], "69")

    def test_correct_kluge_edition_is_the_active_searchable_holding(self):
        _, sources, _, _ = survey.load()
        source = next(row for row in sources if row["source_key"] == "KlugeSeebold2011")
        self.assertIn("kluge_seebold_2011_25th.txt", source["holding_paths"])
        self.assertNotIn("kluge_seebold_etymologisches_woerterbuch.txt",
                         source["holding_paths"])

    def test_older_kluge_and_appended_review_are_separate_unreviewed_sources(self):
        corpus, sources, _, reviews = survey.load()
        by_key = {row["source_key"]: row for row in sources}
        older = by_key["KlugeSeebold2002"]
        self.assertEqual(older["role"], "reconstruction")
        self.assertEqual(older["holding_paths"],
                         "docs/references/kluge_seebold_etymologisches_woerterbuch.txt")
        self.assertIn("No matching older original", older["notes"])
        review = by_key["Kuiper1991"]
        self.assertEqual(review["role"], "context")
        self.assertIn("sheets998-1013", review["notes"])
        self.assertIn("not Mayrhofer", by_key["Mayrhofer1992"]["notes"])
        checks = survey.coverage_rows(corpus, sources, reviews)
        for key in ("KlugeSeebold2002", "Kuiper1991"):
            selected = [row for row in checks if row["source_key"] == key]
            self.assertEqual(selected, [])
            self.assertEqual(by_key[key]["consultation_mode"], "opportunistic")
            self.assertEqual(by_key[key]["conventions_status"], "unreviewed")

    def test_catalogue_limits_are_not_full_source_or_convention_certificates(self):
        _, sources, _, _ = survey.load()
        by_key = {row["source_key"]: row for row in sources}
        for key in ("Pokorny1959", "Stiles1985", "Ringe1984", "NeriRingeReview"):
            self.assertEqual(by_key[key]["edition_status"], "verification_gap")
            self.assertEqual(by_key[key]["conventions_status"], "unreviewed")
        self.assertIn("688 nonempty", by_key["Pokorny1959"]["notes"])
        self.assertIn("152-155 are missing", by_key["Ringe1984"]["notes"])
        self.assertIn("Venue/year are not established", by_key["NeriRingeReview"]["notes"])
        howell = by_key["HowellSalmons1988"]
        self.assertEqual(howell["edition_status"], "verified")
        self.assertIn("1997", howell["notes"])
        self.assertIn("byte-identical", howell["notes"])
        self.assertEqual(howell["conventions_status"], "unreviewed")

    def test_source_policy_preserves_catalogue_without_cartesian_obligations(self):
        _, sources, _, _ = survey.load()
        readme = (survey.ROOT / survey.DIRECTORY / "README.md").read_text(
            encoding="utf-8")
        self.assertIn("## Prioritized consultation programme", readme)
        self.assertEqual(len(sources), 91)
        self.assertEqual(sum(row["role"] != "excluded" for row in sources), 82)
        self.assertTrue(all(row["consultation_mode"] and row["payoff"] for row in sources))
        self.assertEqual(
            {row["source_key"] for row in sources if row["consultation_mode"] == "core_dictionary"},
            set(survey.CORE_SOURCES))

    def test_orel_opening_preserves_adder_alternatives_and_explicit_wgmc_bier(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for suffix, form in (("01", "*nēđrōn"), ("02", "*nađrōn"),
                             ("03", "*nađraz")):
            record = evidence[f"orel-core-1933-{suffix}"]
            self.assertEqual(record["printed_pages"], "286")
            self.assertEqual(record["diplomatic_form"], form)
            self.assertEqual(record["comparison_form"], form)
            self.assertEqual(record["verification"], "page_image_checked")
        bier = evidence["orel-core-1949-01"]
        self.assertEqual(bier["diplomatic_form"], "*bērō")
        self.assertEqual(bier["asserted_stage"], "WGmc")
        self.assertIn("'wave'", bier["notes"])
        self.assertNotEqual(bier["diplomatic_form"],
                            evidence["orel-core-1949-02"]["diplomatic_form"])

    def test_orel_bid_bow_and_book_links_do_not_collapse_senses_or_cells(self):
        _, _, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for row_id, form in (
            ("1947", "*beuđanan"), ("1948", "*biđjanan"),
            ("1961", "*bauʒjanan"), ("1962", "*bauʒaz"), ("1963", "*buʒōn"),
        ):
            record = evidence[f"orel-core-{row_id}-01"]
            self.assertIn(row_id, survey.ids(record["row_ids"]))
            self.assertEqual(record["diplomatic_form"], form)
            self.assertTrue(any(
                review["row_id"] == row_id
                and record["evidence_id"] in survey.ids(review["evidence_ids"])
                for review in reviews))
        self.assertEqual(evidence["orel-core-1948-02"]["diplomatic_form"], "*bīđanan")
        shared = evidence["orel-core-1942-04"]
        self.assertEqual(set(survey.ids(shared["row_ids"])), {"1942", "1955"})
        self.assertIn("OE 'book'", shared["notes"])
        self.assertIn("'beech'", shared["argument"])
        self.assertEqual(evidence["orel-core-1942-02"]["row_ids"], "1942")

    def test_completed_kroonen_reviews_cover_the_exact_population(self):
        corpus, sources, forms, reviews = survey.load()
        selected = [row for row in reviews if row["source_key"] == "Kroonen2013"]
        self.assertEqual(len(selected), len(corpus))
        self.assertEqual({row["row_id"] for row in selected},
                         {row["row_id"] for row in corpus})
        by_row = {row["row_id"]: row for row in selected}
        for row_id in ("1996", "2148", "2271", "2302", "2327"):
            self.assertEqual(by_row[row_id]["status"], "evidence_found")
        for row_id in ("2217", "2218", "2250"):
            self.assertEqual(by_row[row_id]["status"], "no_form_found")
            self.assertTrue(by_row[row_id]["search_basis"])
            self.assertTrue(by_row[row_id]["assessment"])
        self.assertFalse(survey.incomplete(
            sources, survey.coverage_rows(corpus, sources, reviews)))

    def test_kroonen_family_components_do_not_invent_selected_inflections(self):
        _, _, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for key, form in (
            ("kroonen-core-1996-1", "*drankjan-"),
            ("kroonen-core-1996-2", "*drunki-"),
            ("kroonen-core-2271-1", "*warza-"),
            ("kroonen-core-2327-1", "*wunda-"),
            ("kroonen-core-2327-2", "*wundō-"),
        ):
            self.assertEqual(evidence[key]["diplomatic_form"], form)
            self.assertEqual(evidence[key]["form_kind"], "stem")
        for row_id in ("2148", "2302", "2327"):
            review = next(row for row in reviews
                          if row["source_key"] == "Kroonen2013"
                          and row["row_id"] == row_id)
            quoted = [evidence[key]["diplomatic_form"]
                      for key in survey.ids(review["evidence_ids"])]
            self.assertTrue(quoted)
            self.assertFalse(any(form in quoted for form in (
                "*regnabugan-", "*wiraldu-", "*wúndōdē")))
        self.assertIn("component", evidence["kroonen-core-2302-1"]["argument"])

    def test_kroonen_adder_folios_and_syllabic_laryngeal_are_diplomatic(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for key, form, page in (
            ("kroonen-core-1933-1", "*nēdrōn-", "386"),
            ("kroonen-core-1933-2", "*nēdra-", "386"),
            ("kroonen-core-1933-3", "*nadra-", "381"),
            ("kroonen-core-1933-4", "*nh̥₁tr-ó-", "381"),
        ):
            record = evidence[key]
            self.assertEqual(record["diplomatic_form"], form)
            self.assertEqual(record["comparison_form"], form)
            self.assertEqual(record["printed_pages"], page)
            self.assertEqual(record["verification"], "page_image_checked")
        self.assertEqual(evidence["kroonen-core-1933-2"]["asserted_stage"],
                         "germanic_reconstruction_date_unspecified")

    def test_kroonen_quantity_plural_cells_and_later_stage_stay_separate(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        hue = evidence["kroonen-core-2332-1"]
        self.assertEqual(hue["diplomatic_form"], "*hīwa-")
        self.assertEqual(hue["printed_pages"], "224")
        self.assertEqual(hue["asserted_stage"], "germanic_derivation_context")
        self.assertIn("Nordic", hue["cell"])
        liver = evidence["kroonen-core-2108-4"]
        self.assertEqual(liver["diplomatic_form"], "*leurini")
        self.assertEqual(liver["asserted_stage"], "proto_norse")
        self.assertIn("locative", liver["cell"])
        for key, form in (
            ("kroonen-core-2119-7", "*mannaniz"),
            ("kroonen-core-2119-8", "*manniz"),
        ):
            self.assertEqual(evidence[key]["diplomatic_form"], form)
            self.assertIn("plural", evidence[key]["cell"])
            self.assertNotIn("genitive", evidence[key]["cell"])

    def test_cercignani_forms_preserve_notation_cells_and_endings(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        self.assertEqual(evidence["seven-cercignani-citation"]["diplomatic_form"],
                         "*/seƀun/")
        self.assertEqual(evidence["milk-cercignani-citation"]["diplomatic_form"],
                         "*/meluks/")
        for suffix, form in (("earlier", "*/melukez/"), ("later", "*/melukiz/")):
            record = evidence[f"milk-cercignani-genitive-{suffix}"]
            self.assertEqual(record["diplomatic_form"], form)
            self.assertEqual(record["asserted_stage"], "early_germanic_unspecified")
            self.assertIn("genitive singular", record["cell"])
        self.assertEqual(evidence["horn-cercignani-citation"]["comparison_form"],
                         "*hurnan")
        self.assertEqual(evidence["nest-cercignani-citation"]["comparison_form"],
                         "*nistaz")

    def test_homonymous_glosses_do_not_supply_false_whole_word_evidence(self):
        corpus, _, forms, reviews = survey.load()
        rows = {row["row_id"]: row for row in corpus}
        self.assertEqual(rows["2294"]["target"], "windan")
        self.assertEqual(rows["2119"]["target"], "mannes")
        for row_id in ("2294", "2119"):
            linked = [form for form in forms
                      if form["source_key"] == "Cercignani1980"
                      and row_id in survey.ids(form["row_ids"])]
            self.assertTrue(linked)
            self.assertTrue(all(form["form_kind"] == "process"
                                and not form["diplomatic_form"] for form in linked))
            review = next(row for row in reviews
                          if row["row_id"] == row_id
                          and row["source_key"] == "Cercignani1980")
            self.assertEqual(review["status"], "discussion_only")

    def test_sit_and_three_keep_source_vowels_quantity_and_citation_cells(self):
        corpus, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for key, form in (
            ("sit-orel-headword", "*setjanan"),
            ("sit-kroonen-stem", "*set(j)an-"),
            ("three-orel-headword", "*þrejez"),
            ("three-kroonen-nominative", "*þrīz"),
            ("three-ringe-pgmc", "*þrīz"),
        ):
            with self.subTest(key=key):
                self.assertEqual(evidence[key]["diplomatic_form"], form)
                self.assertEqual(evidence[key]["comparison_form"], form)
        self.assertEqual(evidence["sit-kroonen-stem"]["form_kind"], "stem")
        self.assertIn("s.v. *þri-", evidence["three-kroonen-nominative"]["locator"])
        self.assertIn("added", evidence["three-ringe-pgmc"]["cell"])
        rows = {row["row_id"]: row for row in corpus}
        self.assertEqual(rows["2193"]["protoform"], "*sétjaną")
        self.assertEqual(rows["2254"]["protoform"], "*θréjez")

    def test_method_and_dating_evidence_do_not_fabricate_whole_words(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for key in (
            "orel-e-i-convention", "kroonen-e-i-inventory",
            "raising-ringe-high-front", "raising-fulk-conditioners",
            "raising-ringe-taylor-oe-boundary",
        ):
            with self.subTest(key=key):
                self.assertEqual(evidence[key]["form_kind"], "process")
                self.assertEqual(evidence[key]["diplomatic_form"], "")
        self.assertEqual(evidence["orel-e-i-convention"]["printed_pages"], "xi-xiii")
        self.assertEqual(evidence["kroonen-e-i-inventory"]["printed_pages"], "xix")
        self.assertEqual(evidence["raising-ringe-high-front"]["asserted_stage"],
                         "pgmc_probable")

    def test_candidate_cohort_keeps_alternatives_glyphs_and_actual_folios(self):
        _, _, forms, _ = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        self.assertEqual(evidence["dill-orel-headword"]["diplomatic_form"], "*đeljaz")
        self.assertEqual(evidence["hind-orel-headword"]["diplomatic_form"], "*xenđjō(n)")
        self.assertEqual(evidence["hind-kroonen-stem"]["printed_pages"], "226")
        self.assertEqual(evidence["light-orel-verb"]["printed_pages"], "243")
        for key, expected in (
            ("stilt-orel-e-form", "*steltjōn"),
            ("stilt-orel-a-form", "*staltjōn"),
            ("dill-kroonen-original-nominative", "*deliz"),
            ("dill-kroonen-original-genitive", "*duljaz"),
        ):
            self.assertEqual(evidence[key]["diplomatic_form"], expected)
        self.assertEqual(evidence["dill-kroonen-original-nominative"]["asserted_stage"],
                         "germanic_paradigm_date_unspecified")
        for author in ("orel", "kroonen"):
            self.assertEqual(evidence[f"will-{author}-verb"]["row_ids"], "2292")
            self.assertEqual(evidence[f"will-{author}-noun"]["row_ids"], "2293")
        self.assertEqual(evidence["smear-kroonen-verb-stem"]["form_kind"], "stem")
        self.assertEqual(evidence["smear-kroonen-verb-stem"]["diplomatic_form"],
                         "*smerwjan-")

    def test_luehr_article_is_not_omitted_or_merged_with_the_ewa_entry(self):
        _, sources, _, _ = survey.load()
        source = next(row for row in sources if row["source_key"] == "Luehr1993")
        self.assertEqual(source["role"], "reconstruction")
        self.assertIn("docs/references/luehr_article.pdf", source["holding_paths"])
        self.assertEqual(source["conventions_status"], "unreviewed")

    def test_nasal_controls_preserve_author_vowels_signs_and_cells(self):
        _, _, forms, reviews = survey.load()
        evidence = {row["evidence_id"]: row for row in forms}
        for key, row_id, form, page in (
            ("gift-orel-headword", "2040", "*ʒeftiz", "130"),
            ("give-orel-headword", "2041", "*ʒebanan", "130"),
            ("bind-orel-headword", "1950", "*benđanan", "41"),
            ("bind-kroonen-stem", "1950", "*bindan-", "64"),
            ("find-orel-headword", "2011", "*fenþanan", "99"),
            ("find-kroonen-stem", "2011", "*finþan-", "142"),
            ("spin-orel-headword", "2207", "*spennanan", "364"),
            ("spin-kroonen-stem", "2207", "*spinnan-", "467"),
            ("wind-orel-verb", "2294", "*wenđanan", "454"),
            ("wind-kroonen-verb-stem", "2294", "*windan-", "587"),
        ):
            with self.subTest(key=key):
                self.assertEqual(evidence[key]["row_ids"], row_id)
                self.assertEqual(evidence[key]["diplomatic_form"], form)
                self.assertEqual(evidence[key]["printed_pages"], page)
                self.assertTrue(any(key in survey.ids(review["evidence_ids"])
                                    and review["row_id"] == row_id
                                    for review in reviews))
        self.assertEqual(evidence["gift-orel-headword"]["comparison_form"], "*geftiz")
        self.assertIn("participle", evidence["find-kroonen-stem"]["cell"])
        self.assertEqual(evidence["wind-kroonen-verb-stem"]["form_kind"], "stem")
        self.assertIn("omit OE", evidence["wind-kroonen-verb-stem"]["notes"])

    def test_diagnostic_snapshot_covers_marked_high_front_and_nasal_leads(self):
        corpus, _, _, _ = survey.load()
        high_front = {
            row["row_id"] for row in corpus
            if any(re.search(r"[eé].*[iíīįj]", row[field])
                   for field in ("proto", "protoform"))
        }
        commentary = (survey.ROOT / survey.DIRECTORY / "commentary.md").read_text(
            encoding="utf-8")
        screen = commentary.split("## Whole-population diagnostic screen", 1)[1]
        screen = screen.split("\n## ", 1)[0]
        listed = set(re.findall(r"\| [a-z]+(\d+) \|", screen))
        self.assertEqual(high_front, listed)
        nasal = {
            row["row_id"] for row in corpus
            if any(re.search(r"[eé][mnŋ][^aāąáeéēiíīįoóōǫuúūųyǭâêîôû]", row[field])
                   for field in ("proto", "protoform"))
        }
        self.assertEqual(nasal, {"2075", "2208"})

    def test_wrong_edition_and_author_aliases_are_excluded_not_surveyed(self):
        _, sources, _, _ = survey.load()
        by_key = {row["source_key"]: row for row in sources}
        for old, actual in (
            ("Kaluza1906", "Kaluza1900"),
            ("Wright1925", "WrightWuelcker1884"),
            ("BrightCassidyRingler1971", "Bright1917"),
            ("Sweet1953", "Sweet1893"),
            ("BosworthToller1898", "Toller1921"),
        ):
            with self.subTest(old=old):
                self.assertEqual(by_key[old]["role"], "excluded")
                self.assertNotEqual(by_key[actual]["role"], "excluded")
                self.assertEqual(by_key[actual]["edition_status"], "verified")
                self.assertIn(actual, by_key[old]["notes"])

    def test_graph_declares_research_outputs_not_canonical_owners(self):
        import artifact_graph
        declared = artifact_graph.declared_outputs()["pgmc_reconstruction_survey"]
        self.assertEqual({path.name for path in declared}, set(survey.PROJECTION_FILES))
        self.assertFalse(any(path in artifact_graph.ARCHIVE_PATHS for path in declared))


if __name__ == "__main__":
    unittest.main()
