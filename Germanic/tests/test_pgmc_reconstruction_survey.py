from __future__ import annotations

import copy
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
        checks = survey.coverage_rows(self.corpus, self.sources, self.reviews)
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
        self.assertTrue(survey.incomplete(self.sources, self.reviews))

    def test_unknown_or_outside_library_holding_fails(self):
        self.sources[0]["holding_paths"] = "../outside.txt"
        with self.assertRaisesRegex(survey.SurveyError, "out-of-library"):
            self.validate()


class LiveSurveyTests(unittest.TestCase):
    def test_complete_population_includes_six_nonrunnable_rows(self):
        corpus, sources, forms, reviews = survey.load()
        self.assertEqual(len(corpus), 393)
        self.assertEqual({row["row_id"] for row in corpus if row["runnable"] == "0"},
                         {"1935", "1947", "1948", "1994", "2156", "2218"})
        self.assertEqual(sum(row["stage_basis"] == "explicit_sidecar" for row in corpus), 81)
        self.assertTrue(survey.incomplete(
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
        self.assertEqual(evidence["cud-orel-formation"]["diplomatic_form"], "*kwedwō(n)")
        self.assertEqual(evidence["cud-ringe-taylor-wgmc"]["printed_pages"], "323")
        self.assertEqual(evidence["cud-ringe-taylor-wgmc"]["asserted_stage"], "PWGmc")
        self.assertEqual(evidence["cud-clark-hall-variants"]["printed_pages"], "69")

    def test_correct_kluge_edition_is_the_active_searchable_holding(self):
        _, sources, _, _ = survey.load()
        source = next(row for row in sources if row["source_key"] == "KlugeSeebold2011")
        self.assertIn("kluge_seebold_2011_25th.txt", source["holding_paths"])
        self.assertNotIn("kluge_seebold_etymologisches_woerterbuch.txt",
                         source["holding_paths"])

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

    def test_luehr_article_is_not_omitted_or_merged_with_the_ewa_entry(self):
        _, sources, _, _ = survey.load()
        source = next(row for row in sources if row["source_key"] == "Luehr1993")
        self.assertEqual(source["role"], "reconstruction")
        self.assertIn("docs/references/luehr_article.pdf", source["holding_paths"])
        self.assertEqual(source["conventions_status"], "unreviewed")

    def test_wrong_edition_and_author_aliases_are_excluded_not_surveyed(self):
        _, sources, _, _ = survey.load()
        by_key = {row["source_key"]: row for row in sources}
        for old, actual in (
            ("Kaluza1906", "Kaluza1900"),
            ("Wright1925", "WrightWuelcker1884"),
            ("BrightCassidyRingler1971", "Bright1917"),
        ):
            with self.subTest(old=old):
                self.assertEqual(by_key[old]["role"], "excluded")
                self.assertNotEqual(by_key[actual]["role"], "excluded")
                self.assertEqual(by_key[actual]["edition_status"], "verified")
                self.assertIn(actual, by_key[old]["notes"])

    def test_graph_declares_research_outputs_not_canonical_owners(self):
        import artifact_graph
        declared = artifact_graph.declared_outputs()["pgmc_reconstruction_survey"]
        self.assertEqual({path.name for path in declared}, {
            "corpus_inventory.tsv", "source_coverage.tsv",
            "reconstruction_ledger.md", "survey_provenance.json",
        })
        self.assertFalse(any(path in artifact_graph.ARCHIVE_PATHS for path in declared))


if __name__ == "__main__":
    unittest.main()
