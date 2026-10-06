"""Evidence-linked analytical comparisons; no canonical reconstruction authority."""
from __future__ import annotations

import csv
import html
import io
import json
import sqlite3
from collections import Counter
from contextlib import closing

ANALYSIS_COLUMNS = (
    "analysis_id", "row_id", "evidence_id", "status", "relation_to_row",
    "attribution_status", "comparison_unit", "stage_interpretation", "stage_basis",
    "stage_evidence_ids", "analytical_form", "normalization_basis",
    "normalization_evidence_ids", "features", "feature_evidence_ids", "notes",
)
COMPARISON_COLUMNS = (
    "comparison_id", "row_ids", "analysis_ids", "scope", "question",
    "comparison_unit", "type_tags", "comparability", "status",
    "explanation_status", "conclusion", "premises", "rationale_ids", "notes",
    "alignment_status", "alignment_basis", "alignment_evidence_ids", "alignment_limits",
)
RATIONALE_COLUMNS = (
    "rationale_id", "analysis_ids", "comparison_ids", "basis_type",
    "support_mode", "evidence_ids", "statement", "premises", "counterarguments",
    "reason_target", "conditioning_tags",
)
TABLES = {
    "analyses": ANALYSIS_COLUMNS,
    "comparisons": COMPARISON_COLUMNS,
    "rationales": RATIONALE_COLUMNS,
}
RELATIONS = {
    "selected_cell", "same_etymon_citation", "same_etymon_other_cell",
    "same_family", "compound_component", "comparandum", "process", "unresolved",
}
ATTRIBUTIONS = {"endorsed", "conditional", "reported", "rejected", "illustrative", "unclear"}
UNITS = {
    "source_citation", "root_vocalism", "stem_formation", "selected_cell",
    "historical_endpoint", "segment_interpretation", "lexical_identity",
    "morpheme_segmentation", "process", "printed_representation",
}
STAGES = {
    "unspecified", "pgmc", "wgmc", "pwgmc", "northwest_germanic",
    "north_germanic", "pre_germanic", "pie", "oe", "proto_norse", "other", "mixed",
}
STAGE_BASES = {"explicit_statement", "source_convention", "analyst_inference", "dictionary_context", "unknown"}
FEATURES = {
    "vocalism", "quantity", "ablaut", "segments", "stem_class", "suffix",
    "ending", "cell", "segmentation", "stress", "gender",
}
TYPES = {
    "notation", "transcription_error", "phonemic_inventory", "vocalism",
    "quantity", "ablaut", "stem_class", "suffix", "ending", "inflection",
    "segmentation", "chronological_stage", "pgmc_membership",
    "lexical_identity", "cognate_grouping", "historical_analysis", "consonantism", "gender",
}
COMPARABILITIES = {
    "equivalent", "premised_equivalence", "substantive_difference",
    "different_units", "insufficient_evidence", "undetermined",
}
BASIS_TYPES = {
    "notation_convention", "reflex_set", "sound_law", "analogy",
    "chronology", "dialect_subgrouping", "pie_reconstruction",
    "loan_hypothesis", "morphological_argument", "lexical_identification", "method",
}
ALIGNMENT_STATUSES = {"unreviewed", "feature_aligned", "bounded_limit"}
REASON_TARGETS = {"position_support", "descriptive_bridge", "divergence_explanation"}
CONDITIONING_TAGS = {
    "following_i", "following_j", "coda_nasal", "following_u",
    "sentence_unstressed", "eu_iu", "lowering_nonhigh",
    "trigger_loss", "trigger_change", "counterexample",
}


class AnalysisError(ValueError):
    pass


def ids(value):
    return value.split(";") if value else []


def indexed(rows, column):
    result = {}
    for row in rows:
        key = row[column]
        if not key or key in result:
            raise AnalysisError(f"{column}: empty or duplicate identity {key}")
        result[key] = row
    return result


def links(value, available, label, required=False):
    linked = ids(value)
    if (required and not linked) or len(linked) != len(set(linked)) or not set(linked) <= set(available):
        raise AnalysisError(f"{label}: missing, duplicate or unknown links")
    return linked


def feature_values(row):
    try:
        features = json.loads(row["features"])
    except json.JSONDecodeError as exc:
        raise AnalysisError(f"{row['analysis_id']}: invalid feature JSON") from exc
    if (not isinstance(features, dict) or not set(features) <= FEATURES
            or any(not isinstance(value, str) or not value for value in features.values())):
        raise AnalysisError(f"{row['analysis_id']}: unsupported or empty feature claim")
    return features


def validate(corpus, forms, analyses, comparisons, rationales):
    rows = {row["row_id"] for row in corpus}
    evidence = indexed(forms, "evidence_id")
    positions = indexed(analyses, "analysis_id")
    cases = indexed(comparisons, "comparison_id")
    reasons = indexed(rationales, "rationale_id")
    for position in analyses:
        key = position["analysis_id"]
        if position["row_id"] not in rows or position["evidence_id"] not in evidence:
            raise AnalysisError(f"{key}: unknown row or evidence")
        form = evidence[position["evidence_id"]]
        if position["row_id"] not in ids(form["row_ids"]):
            raise AnalysisError(f"{key}: evidence does not support this row")
        if form["form_kind"] == "process":
            if position["analytical_form"] or position["relation_to_row"] != "process":
                raise AnalysisError(f"{key}: process evidence is not a reconstructed word")
        for field, allowed in (
            ("status", {"reviewed", "unreviewed"}),
            ("relation_to_row", RELATIONS), ("attribution_status", ATTRIBUTIONS),
            ("comparison_unit", UNITS), ("stage_interpretation", STAGES),
            ("stage_basis", STAGE_BASES),
        ):
            if position[field] not in allowed:
                raise AnalysisError(f"{key}: invalid {field}")
        if not position["normalization_basis"] or not position["notes"]:
            raise AnalysisError(f"{key}: normalization and scope notes are required")
        if position["stage_basis"] == "unknown" and position["stage_interpretation"] != "unspecified":
            raise AnalysisError(f"{key}: unknown stage cannot acquire a dated label")
        if position["stage_basis"] == "dictionary_context" and position["stage_interpretation"] != "unspecified":
            raise AnalysisError(f"{key}: dictionary context cannot date a historical endpoint")
        links(position["stage_evidence_ids"], evidence, f"{key} stage",
              position["stage_basis"] not in {"unknown", "dictionary_context"})
        links(position["normalization_evidence_ids"], evidence, f"{key} normalization",
              position["analytical_form"] != form["diplomatic_form"])
        features = feature_values(position)
        links(position["feature_evidence_ids"], evidence, f"{key} features", bool(features))
        if form["form_kind"] != "process" and not position["analytical_form"]:
            raise AnalysisError(f"{key}: non-process analytical form must be explicit")
    for case in comparisons:
        key = case["comparison_id"]
        affected = links(case["row_ids"], rows, f"{key} rows", True)
        members = links(case["analysis_ids"], positions, f"{key} analyses")
        links(case["type_tags"], TYPES, f"{key} types")
        linked_reasons = links(case["rationale_ids"], reasons, f"{key} rationales")
        alignment_evidence = links(case["alignment_evidence_ids"], evidence,
                                   f"{key} alignment evidence")
        if case["alignment_status"] not in ALIGNMENT_STATUSES:
            raise AnalysisError(f"{key}: invalid alignment status")
        if case["alignment_status"] != "unreviewed":
            if case["status"] != "reviewed" or not case["alignment_basis"] or not alignment_evidence:
                raise AnalysisError(f"{key}: alignment needs reviewed positions and a cited basis")
            member_evidence = {positions[member]["evidence_id"] for member in members}
            if not member_evidence <= set(alignment_evidence):
                raise AnalysisError(f"{key}: alignment omits member evidence")
            if case["alignment_status"] == "bounded_limit" and not case["alignment_limits"]:
                raise AnalysisError(f"{key}: bounded alignment needs its exact remaining premise")
            if case["alignment_status"] == "feature_aligned":
                if len(members) < 2 or not all(
                        set(feature_values(positions[member])) - {"cell"} for member in members):
                    raise AnalysisError(f"{key}: citation-cell inventory is not feature alignment")
        if (case["scope"] not in {"core_triage", "focused_case"}
                or case["comparison_unit"] not in UNITS
                or case["comparability"] not in COMPARABILITIES
                or case["status"] not in {"reviewed", "unreviewed"}
                or case["explanation_status"] not in
                {"source_explicit", "analyst_inference", "mixed", "unestablished", "not_applicable"}):
            raise AnalysisError(f"{key}: invalid comparison classification")
        if not case["question"] or not case["conclusion"] or not case["premises"]:
            raise AnalysisError(f"{key}: question, conclusion and premises are required")
        if any(positions[member]["row_id"] not in affected for member in members):
            raise AnalysisError(f"{key}: analysis belongs to another row")
        if case["status"] == "reviewed" and any(positions[member]["status"] != "reviewed" for member in members):
            raise AnalysisError(f"{key}: reviewed case hides unreviewed positions")
        if case["comparability"] in {"equivalent", "premised_equivalence", "substantive_difference"}:
            if len(members) < 2:
                raise AnalysisError(f"{key}: comparison requires at least two positions")
            if any(positions[member]["comparison_unit"] != case["comparison_unit"] for member in members):
                raise AnalysisError(f"{key}: incompatible comparison units")
        if case["comparability"] == "equivalent":
            values = {(positions[member]["analytical_form"],
                       positions[member]["stage_interpretation"],
                       tuple(sorted(feature_values(positions[member]).items()))) for member in members}
            if len(values) != 1:
                raise AnalysisError(f"{key}: claimed equivalence has different forms/stages/features")
            if case["comparison_unit"] != "printed_representation" and any(
                    positions[member]["stage_basis"] in {"unknown", "dictionary_context"}
                    or positions[member]["attribution_status"] != "endorsed"
                    or positions[member]["relation_to_row"] in
                    {"same_family", "compound_component", "comparandum", "unresolved"}
                    for member in members):
                raise AnalysisError(f"{key}: uncertain stages/family links cannot prove full equivalence")
            essential = {
                "root_vocalism": {"vocalism", "quantity"},
                "stem_formation": {"stem_class", "suffix"},
                "selected_cell": {"cell", "stem_class", "ending"},
                "historical_endpoint": {"vocalism", "quantity", "segments", "cell"},
                "segment_interpretation": {"segments"},
                "morpheme_segmentation": {"segmentation"},
                "source_citation": {"cell"},
            }.get(case["comparison_unit"], set())
            if any(not essential <= feature_values(positions[member]).keys() for member in members):
                raise AnalysisError(f"{key}: equivalence omits essential unit features")
        if case["comparability"] == "premised_equivalence" and not linked_reasons:
            raise AnalysisError(f"{key}: premised equivalence needs cited reasoning")
        if case["explanation_status"] in {"source_explicit", "analyst_inference", "mixed"} and not linked_reasons:
            raise AnalysisError(f"{key}: an explanation requires evidence-linked reasoning")
        if case["explanation_status"] in {"source_explicit", "analyst_inference", "mixed"}:
            targets = {reasons[reason]["reason_target"] for reason in linked_reasons}
            required = ({"descriptive_bridge", "divergence_explanation"}
                        if case["comparability"] in {"equivalent", "premised_equivalence"}
                        else {"divergence_explanation"})
            if not targets & required:
                raise AnalysisError(f"{key}: position support does not explain inter-author divergence")
        if case["scope"] == "core_triage" and case["status"] == "reviewed":
            for row_id in affected:
                linked_sources = {
                    evidence[positions[member]["evidence_id"]]["source_key"]
                    for member in members if positions[member]["row_id"] == row_id
                }
                available_sources = {
                    form["source_key"] for form in forms
                    if row_id in ids(form["row_ids"])
                    and form["source_key"] in {"Orel2003", "Kroonen2013"}
                }
                if not available_sources <= linked_sources:
                    raise AnalysisError(f"{key}: core triage omits available core-source evidence")
                available_evidence = {
                    form["evidence_id"] for form in forms
                    if row_id in ids(form["row_ids"])
                    and form["source_key"] in {"Orel2003", "Kroonen2013"}
                }
                linked_evidence = {
                    positions[member]["evidence_id"] for member in members
                    if positions[member]["row_id"] == row_id
                }
                if not available_evidence <= linked_evidence:
                    raise AnalysisError(f"{key}: core triage omits available alternatives")
        for reason_id in linked_reasons:
            if key not in ids(reasons[reason_id]["comparison_ids"]):
                raise AnalysisError(f"{key}: missing reciprocal rationale link")
    for reason in rationales:
        key = reason["rationale_id"]
        linked_positions = links(reason["analysis_ids"], positions, f"{key} analyses", True)
        linked_cases = links(reason["comparison_ids"], cases, f"{key} comparisons", True)
        links(reason["evidence_ids"], evidence, f"{key} supporting evidence", True)
        if reason["basis_type"] not in BASIS_TYPES or reason["support_mode"] not in {"source_explicit", "analyst_inference"}:
            raise AnalysisError(f"{key}: invalid reasoning basis or attribution")
        if reason["reason_target"] not in REASON_TARGETS:
            raise AnalysisError(f"{key}: invalid reason target")
        links(reason["conditioning_tags"], CONDITIONING_TAGS, f"{key} conditioning tags")
        if reason["reason_target"] == "divergence_explanation":
            sources = {evidence[positions[position]["evidence_id"]]["source_key"]
                       for position in linked_positions}
            if len(sources) < 2:
                raise AnalysisError(f"{key}: divergence needs positions from at least two sources")
        if any(not reason[field] for field in ("statement", "premises", "counterarguments")):
            raise AnalysisError(f"{key}: reasoning and its limits must be explicit")
        for case_id in linked_cases:
            case = cases[case_id]
            if key not in ids(case["rationale_ids"]) or not set(linked_positions) <= set(ids(case["analysis_ids"])):
                raise AnalysisError(f"{key}: missing reciprocal or compatible case link")
        for case_id in linked_cases:
            if reason["support_mode"] == "analyst_inference" and cases[case_id]["explanation_status"] == "source_explicit":
                raise AnalysisError(f"{key}: analyst inference cannot become an author's explicit explanation")


def coverage(corpus, comparisons):
    reviewed = {}
    for case in comparisons:
        if case["scope"] == "core_triage" and case["status"] == "reviewed":
            for row_id in ids(case["row_ids"]):
                reviewed.setdefault(row_id, []).append(case["comparison_id"])
    return [{
        "row_id": row["row_id"], "status": "reviewed" if row["row_id"] in reviewed else "unreviewed",
        "comparison_ids": ";".join(sorted(reviewed.get(row["row_id"], []))),
    } for row in corpus]


def require_complete(corpus, comparisons):
    pending = [row["row_id"] for row in coverage(corpus, comparisons) if row["status"] != "reviewed"]
    if pending:
        raise AnalysisError(f"Core analysis INCOMPLETE: {len(pending)} unreviewed rows; including {', '.join(pending[:8])}")


def alignment_coverage(corpus, comparisons):
    core = [case for case in comparisons if case["scope"] == "core_triage"]
    result = []
    for row in corpus:
        cases = [case for case in core if row["row_id"] in ids(case["row_ids"])]
        reviewed = [case for case in cases if case["alignment_status"] != "unreviewed"]
        status = ("unreviewed" if not cases or len(reviewed) != len(cases) else
                  "bounded_limit" if any(case["alignment_status"] == "bounded_limit"
                                         for case in cases) else "feature_aligned")
        result.append({
            "row_id": row["row_id"], "alignment_status": status,
            "alignment_case_ids": ";".join(case["comparison_id"] for case in reviewed),
        })
    return result


def require_alignment_complete(corpus, comparisons):
    if not corpus:
        raise AnalysisError("Core feature alignment requires a nonempty corpus")
    pending = [row["row_id"] for row in alignment_coverage(corpus, comparisons)
               if row["alignment_status"] == "unreviewed"]
    if pending:
        raise AnalysisError(f"Core feature alignment INCOMPLETE: {len(pending)} rows; "
                            f"including {', '.join(pending[:8])}")


def atlas(forms, analyses, comparisons, rationales):
    evidence = indexed(forms, "evidence_id")
    positions = indexed(analyses, "analysis_id")
    reasons = indexed(rationales, "rationale_id")
    lines = [
        "# PGmc disagreement map", "", "GENERATED analytical view; source forms remain separately authoritative.",
        "Reading coverage, analytical review and explanatory certainty are independent.", "",
        "Core triage compares the recorded citation units and retains every core alternative.",
        "Tags identify reviewed questions; undetermined cases are not settled historical disagreements.",
        "Unknown attribution or date is a review outcome, not source endorsement or a PGmc default.", "",
        "Citation-unit triage, feature alignment and explanations of divergence have separate accountability.",
        "Position-support reasons do not certify an explanation of inter-author disagreement.", "",
    ]
    core = [case for case in comparisons if case["scope"] == "core_triage"]
    counts = Counter(case["comparability"] for case in core)
    lines += [
        f"Core cases: {len(core)}; " + "; ".join(
            f"{state}: {counts[state]}" for state in sorted(counts)) + ".",
        "Core alignment: " + "; ".join(
            f"{status}: {count}" for status, count in sorted(
                Counter(case["alignment_status"] for case in core).items())) + ".",
        "The catalogue below covers every case. Detailed explanations follow only where reasoning is recorded;",
        "the linked source ledger retains the complete alternatives, arguments and verification limits.", "",
        "## Case catalogue", "",
        "| Case / source ledger | Question | Types | Comparability / explanation | Alignment / limits | Positions / source pages |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for case in sorted(comparisons, key=lambda row: row["comparison_id"]):
        pages = {}
        members = ids(case["analysis_ids"])
        for member in members:
            form = evidence[positions[member]["evidence_id"]]
            pages.setdefault(form["source_key"], set()).add(form["printed_pages"])
        references = "; ".join(
            f"{source} pp.{','.join(sorted(folios))}" for source, folios in sorted(pages.items()))
        links_text = ", ".join(
            f"[{row_id}](reconstruction_ledger.md#row-{row_id})" for row_id in ids(case["row_ids"]))
        values = (
            f"{case['comparison_id']} / {links_text}", case["question"],
            case["type_tags"] or "(no type assigned)", f"{case['comparability']} / {case['explanation_status']}",
            f"{case['alignment_status']}; {case['alignment_basis']}; limits: {case['alignment_limits'] or 'none recorded'}",
            f"{len(members)} / {references}",
        )
        lines.append("| " + " | ".join(value.replace("|", "\\|") for value in values) + " |")
    lines += ["", "## Recorded explanations and scoped equivalences", ""]
    for case in sorted(comparisons, key=lambda row: row["comparison_id"]):
        if not case["rationale_ids"]:
            continue
        lines += [
            f'<a id="{html.escape(case["comparison_id"], quote=True)}"></a>', "",
            f"## {case['comparison_id']}: {case['question']}", "",
            f"Rows: {case['row_ids']}; {case['status']}; {case['comparability']}; "
            f"types: {case['type_tags'] or 'not assigned'}; explanation: {case['explanation_status']}.",
            f"Unit: {case['comparison_unit']}. Premises: {case['premises']}", "",
            "| Position | Source / pages | Diplomatic form | Relation / attribution | Analytical interpretation |",
            "| --- | --- | --- | --- | --- |",
        ]
        for key in ids(case["analysis_ids"]):
            position = positions[key]
            form = evidence[position["evidence_id"]]
            values = (key, f"{form['source_key']} pp.{form['printed_pages']}",
                      form["diplomatic_form"] or "(process evidence)",
                      f"{position['relation_to_row']} / {position['attribution_status']}",
                      f"{position['stage_interpretation']} ({position['stage_basis']}); "
                      f"form: {position['analytical_form'] or '(none)'}; "
                      f"features: {position['features']}; {position['notes']}")
            lines.append("| " + " | ".join(value.replace("|", "\\|") for value in values) + " |")
        lines += ["", case["conclusion"], ""]
        for key in ids(case["rationale_ids"]):
            reason = reasons[key]
            citations = "; ".join(
                f"{evidence[item]['source_key']} pp.{evidence[item]['printed_pages']}"
                for item in ids(reason["evidence_ids"]))
            lines += [
                f"- {reason['reason_target']} / {reason['basis_type']} ({reason['support_mode']}): "
                f"{reason['statement']} [{citations}]",
                f"  Premises: {reason['premises']} Counterarguments/limits: {reason['counterarguments']}",
            ]
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def query(tables, sql):
    with closing(sqlite3.connect(":memory:")) as database:
        for name, (columns, rows) in tables.items():
            database.execute(f'CREATE TABLE "{name}" ({", ".join(f"{column} TEXT" for column in columns)})')
            database.executemany(
                f'INSERT INTO "{name}" VALUES ({", ".join("?" for _ in columns)})',
                [[row[column] for column in columns] for row in rows])
        database.execute("CREATE TABLE comparison_types (comparison_id TEXT, type TEXT)")
        database.executemany("INSERT INTO comparison_types VALUES (?, ?)", [
            (row["comparison_id"], tag) for row in tables["comparisons"][1] for tag in ids(row["type_tags"])])
        database.execute("CREATE TABLE comparison_analyses (comparison_id TEXT, analysis_id TEXT)")
        database.executemany("INSERT INTO comparison_analyses VALUES (?, ?)", [
            (row["comparison_id"], key) for row in tables["comparisons"][1] for key in ids(row["analysis_ids"])])
        for table, owner, key, linked_field, linked_key in (
            ("comparison_rows", "comparisons", "comparison_id", "row_ids", "row_id"),
            ("evidence_rows", "forms", "evidence_id", "row_ids", "row_id"),
            ("comparison_rationales", "comparisons", "comparison_id", "rationale_ids", "rationale_id"),
            ("rationale_evidence", "rationales", "rationale_id", "evidence_ids", "evidence_id"),
            ("rationale_analyses", "rationales", "rationale_id", "analysis_ids", "analysis_id"),
            ("alignment_evidence", "comparisons", "comparison_id", "alignment_evidence_ids", "evidence_id"),
            ("rationale_conditions", "rationales", "rationale_id", "conditioning_tags", "condition"),
        ):
            database.execute(f"CREATE TABLE {table} ({key} TEXT, {linked_key} TEXT)")
            database.executemany(f"INSERT INTO {table} VALUES (?, ?)", [
                (row[key], linked) for row in tables[owner][1] for linked in ids(row[linked_field])])
        database.execute("CREATE TABLE analysis_features (analysis_id TEXT, feature TEXT, value TEXT)")
        database.executemany("INSERT INTO analysis_features VALUES (?, ?, ?)", [
            (row["analysis_id"], key, value) for row in tables["analyses"][1]
            for key, value in feature_values(row).items()])
        if "reading_scopes" in tables:
            scopes = tables["reading_scopes"][1]
            database.execute("CREATE TABLE scope_rows (scope_id TEXT, row_id TEXT)")
            database.executemany("INSERT INTO scope_rows VALUES (?, ?)", [
                (scope["scope_id"], row_id) for scope in scopes
                for row_id in (
                    [row["row_id"] for row in tables["corpus"][1]]
                    if scope["population_scope"] == "all_rows" else ids(scope["row_ids"]))])
            database.execute("CREATE TABLE scope_evidence (scope_id TEXT, evidence_id TEXT)")
            database.executemany("INSERT INTO scope_evidence VALUES (?, ?)", [
                (scope["scope_id"], key) for scope in scopes for key in ids(scope["evidence_ids"])])
            database.execute("CREATE TABLE target_scopes (source_key TEXT, row_id TEXT, scope_id TEXT)")
            database.executemany("INSERT INTO target_scopes VALUES (?, ?, ?)", [
                (target["source_key"], target["row_id"], key)
                for target in tables["targets"][1] for key in ids(target["scope_ids"])])
        database.commit()
        allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_FUNCTION, sqlite3.SQLITE_RECURSIVE}
        database.set_authorizer(lambda action, *args: sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY)
        cursor = database.execute(sql)
        if cursor.description is None:
            raise AnalysisError("Query must return a read-only result.")
        output = io.StringIO()
        writer = csv.writer(output, delimiter="\t", lineterminator="\n")
        writer.writerow([item[0] for item in cursor.description])
        writer.writerows(cursor)
        return output.getvalue()
