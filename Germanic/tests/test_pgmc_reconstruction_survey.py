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
        self.assertEqual(result, "scheduled_rows\tactual_reviews\n393\t191\n")
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
        self.assertEqual(sum(row["source_key"] == "Fulk2018" for row in reviews), 135)

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
        self.assertEqual(len(reviews), 1376)
        self.assertEqual(sum(row["source_key"] == "RingeTaylor2014" for row in reviews), 255)
        self.assertEqual(sum(row["alignment_status"] == "bounded_limit"
                             for row in tables["comparisons"] if row["scope"] == "core_triage"), 17)
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
