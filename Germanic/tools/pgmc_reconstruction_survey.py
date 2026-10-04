#!/usr/bin/env python3
"""Validate research evidence and project the complete OE survey population.

Generated outputs belong to the artifact graph. This command only validates;
--require-complete additionally refuses unfinished reading targets or core analysis.
--require-core-complete checks the Orel/Kroonen reading population only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

from check_bibliography_sanity import parse_entries
from oe_pipeline import load_rows as load_selected_rows
import pgmc_reconstruction_analysis as analytical

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/docs/assembly"))
from build_class_manifests import resolve_stages

DIRECTORY = Path("Germanic/docs/lexeme_reports/pgmc_reconstructions")
CORE_SOURCES = ("Orel2003", "Kroonen2013")
SOURCE_COLUMNS = (
    "source_key", "role", "holding_paths", "scope", "edition_status",
    "conventions_status", "notes", "consultation_mode", "priority", "payoff",
)
TARGET_COLUMNS = ("source_key", "row_id", "selection_basis", "scope_ids")
READING_SOURCES = ("Ringe2017", "Fulk2018", "RingeTaylor2014")
SCOPE_COLUMNS = (
    "scope_id", "source_key", "scope_kind", "population_scope", "row_ids",
    "printed_pages", "locator", "selection_basis", "status", "evidence_ids",
    "search_basis", "assessment", "verification", "verification_limits",
)
CONSULTATION_MODES = {
    "core_dictionary", "systematic_relevant", "case_triggered",
    "opportunistic", "excluded",
}
PROJECTION_FILES = (
    "corpus_inventory.tsv", "source_coverage.tsv", "reconstruction_ledger.md",
    "survey_provenance.json", "comparison_map.md", "analytical_coverage.tsv",
    "source_priorities.tsv",
    "reading_progress.md",
)
FORM_COLUMNS = (
    "evidence_id", "row_ids", "source_key", "printed_pages", "locator",
    "diplomatic_form", "asserted_stage", "form_kind", "cell",
    "comparison_form", "normalization_basis", "argument", "verification",
    "confidence", "quoted_author", "basis", "notes",
)
REVIEW_COLUMNS = (
    "row_id", "source_key", "status", "evidence_ids", "search_basis", "assessment",
)
REVIEW_STATUSES = {
    "evidence_found", "discussion_only", "no_form_found",
    "not_applicable", "verification_gap",
}
ROLES = {"reconstruction", "context", "excluded"}
FORM_KINDS = {"word", "stem", "root", "attestation", "process"}
VERIFICATIONS = {"page_image_checked", "text_checked", "verified_ledger"}
PAGES = re.compile(r"(?:[0-9]+|[ivxlcdm]+)(?:-(?:[0-9]+|[ivxlcdm]+))?"
                   r"(?:,(?:[0-9]+|[ivxlcdm]+)(?:-(?:[0-9]+|[ivxlcdm]+))?)*$")


class SurveyError(ValueError):
    pass


def read_table(path: Path, columns: tuple[str, ...] | None = None) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if columns is not None and tuple(reader.fieldnames or ()) != columns:
            raise SurveyError(f"{path}: expected columns {columns}")
        rows = list(reader)
    for number, row in enumerate(rows, 2):
        if columns is not None and (None in row or any(value is None for value in row.values())):
            raise SurveyError(f"{path}:{number}: wrong number of fields")
    return rows


def unique(rows: list[dict[str, str]], fields: tuple[str, ...], label: str) -> dict:
    result = {}
    for row in rows:
        key = tuple(row[field] for field in fields)
        if any(not value for value in key) or key in result:
            raise SurveyError(f"{label}: empty or duplicate identity {key}")
        result[key] = row
    return result


def ids(value: str) -> list[str]:
    return value.split(";") if value else []


def inventory(root: Path = ROOT) -> list[dict[str, str]]:
    corpus = root / "Germanic/data/germanic-aligned-final.tsv"
    selected = {row["row_id"]: row for row in load_selected_rows(corpus)}
    sidecar = {
        row["row_id"]: row
        for row in read_table(corpus.with_name("entry_stage_metadata.tsv"))
    }
    rows = []
    for raw in read_table(corpus):
        if raw["DOCULECT"] != "Old_English":
            continue
        row_id = raw["ID"]
        proto, protoform = raw["PROTO"].strip(), raw["PROTOFORM"].strip()
        proto_stage, input_stage, variety, problems = resolve_stages(
            row_id, proto, protoform, sidecar)
        if problems:
            raise SurveyError(f"row {row_id}: {'; '.join(problems)}")
        context = selected.get(row_id)
        rows.append({
            "row_id": row_id, "concept": raw["CONCEPT"],
            "target": raw["COUNTERPART"], "proto": proto, "proto_stage": proto_stage,
            "protoform": protoform, "input_stage": input_stage, "input_variety": variety,
            "stage_basis": "equality_convention" if proto == protoform else "explicit_sidecar",
            "derivation_class": raw["DERIVATION_CLASS"],
            "runnable": "1" if context else "0",
            "word_stress": context["word_stress"] if context else "not_evaluated",
            "phonological_finality": (
                context["phonological_finality"] if context else "not_evaluated"),
        })
    unique(rows, ("row_id",), "corpus")
    return sorted(rows, key=lambda row: int(row["row_id"]))


def validate(sources, forms, reviews, corpus, bibliography: set[str], root: Path) -> None:
    source_map = {key[0]: row for key, row in unique(
        sources, ("source_key",), "sources").items()}
    evidence_map = {key[0]: row for key, row in unique(
        forms, ("evidence_id",), "forms").items()}
    review_map = unique(reviews, ("row_id", "source_key"), "reviews")
    row_ids = {row["row_id"] for row in corpus}
    if not row_ids or not any(source["role"] != "excluded" for source in sources):
        raise SurveyError("survey requires a nonempty corpus and included source universe")
    references = (root / "docs/references").resolve()
    for source in sources:
        key = source["source_key"]
        if key not in bibliography or source["role"] not in ROLES:
            raise SurveyError(f"source {key}: unknown bibliography key or role")
        if source["consultation_mode"] not in CONSULTATION_MODES:
            raise SurveyError(f"source {key}: explicit consultation mode is required")
        if ((source["role"] == "excluded") !=
                (source["consultation_mode"] == "excluded")):
            raise SurveyError(f"source {key}: exclusion role and mode disagree")
        if source["priority"] not in {"0", "1", "2", "3", "4", "5"} or not source["payoff"]:
            raise SurveyError(f"source {key}: explicit priority and payoff are required")
        if key in CORE_SOURCES and source["role"] != "excluded":
            if source["consultation_mode"] != "core_dictionary":
                raise SurveyError(f"source {key}: core obligations cannot be demoted")
        if source["consultation_mode"] == "core_dictionary" and key not in CORE_SOURCES:
            raise SurveyError(f"source {key}: undeclared core dictionary")
        if not source["scope"] or not source["notes"] or not source["holding_paths"]:
            raise SurveyError(f"source {key}: holding, scope and notes are required")
        for field in ("edition_status", "conventions_status"):
            if source[field] not in {"verified", "unreviewed", "verification_gap"}:
                raise SurveyError(f"source {key}: invalid {field}")
        for relative in ids(source["holding_paths"]):
            path = (root / relative).resolve()
            if not path.is_relative_to(references) or not path.exists():
                raise SurveyError(f"source {key}: missing or out-of-library holding {relative}")
    for form in forms:
        evidence_id, key = form["evidence_id"], form["source_key"]
        linked = ids(form["row_ids"])
        if not linked or len(linked) != len(set(linked)) or not set(linked) <= row_ids:
            raise SurveyError(f"{evidence_id}: missing, duplicate or unknown row links")
        if key not in source_map or source_map[key]["role"] == "excluded":
            raise SurveyError(f"{evidence_id}: unknown or excluded source")
        if not PAGES.fullmatch(form["printed_pages"]):
            raise SurveyError(f"{evidence_id}: printed pages are required, not sheet labels")
        if form["form_kind"] not in FORM_KINDS or form["verification"] not in VERIFICATIONS:
            raise SurveyError(f"{evidence_id}: invalid kind or verification")
        for field in ("asserted_stage", "cell", "argument", "basis", "locator"):
            if not form[field]:
                raise SurveyError(f"{evidence_id}: {field} must be explicit")
        basis = (root / form["basis"]).resolve()
        if not basis.is_relative_to(root.resolve()) or not basis.is_file():
            raise SurveyError(f"{evidence_id}: missing or out-of-repository verification basis")
        if form["form_kind"] != "process" and not form["diplomatic_form"]:
            raise SurveyError(f"{evidence_id}: authored form is required")
        if form["form_kind"] == "process" and form["diplomatic_form"]:
            raise SurveyError(f"{evidence_id}: process evidence is not a quoted form")
        if form["comparison_form"] and not form["normalization_basis"]:
            raise SurveyError(f"{evidence_id}: explain comparison normalization")
        for row_id in linked:
            review = review_map.get((row_id, key))
            if review is None or evidence_id not in ids(review["evidence_ids"]):
                raise SurveyError(f"{evidence_id}: missing reciprocal review link for {row_id}")
    for review in reviews:
        row_id, key, status = review["row_id"], review["source_key"], review["status"]
        if row_id not in row_ids or key not in source_map or source_map[key]["role"] == "excluded":
            raise SurveyError(f"review {row_id}/{key}: unknown row or unknown/excluded source")
        if status not in REVIEW_STATUSES or not review["search_basis"] or not review["assessment"]:
            raise SurveyError(f"review {row_id}/{key}: explicit status/search/assessment required")
        linked = ids(review["evidence_ids"])
        if len(linked) != len(set(linked)):
            raise SurveyError(f"review {row_id}/{key}: duplicate evidence links")
        if status in {"evidence_found", "discussion_only"} and not linked:
            raise SurveyError(f"review {row_id}/{key}: evidence is required")
        if status in {"no_form_found", "not_applicable"} and linked:
            raise SurveyError(f"review {row_id}/{key}: negative disposition cannot hide evidence")
        for evidence_id in linked:
            form = evidence_map.get(evidence_id)
            if form is None or form["source_key"] != key or row_id not in ids(form["row_ids"]):
                raise SurveyError(f"review {row_id}/{key}: invalid evidence link {evidence_id}")
            if status == "discussion_only" and form["form_kind"] not in {"process", "attestation"}:
                raise SurveyError(f"review {row_id}/{key}: discussion-only hides a reconstruction")


def load(root: Path = ROOT):
    directory = root / DIRECTORY
    corpus = inventory(root)
    sources = read_table(directory / "sources.tsv", SOURCE_COLUMNS)
    forms = read_table(directory / "forms.tsv", FORM_COLUMNS)
    reviews = read_table(directory / "coverage.tsv", REVIEW_COLUMNS)
    bibliography = {entry.key for entry in parse_entries((root / "docs/refs.bib").read_text())}
    validate(sources, forms, reviews, corpus, bibliography, root)
    return corpus, sources, forms, reviews


def load_analysis(root, corpus, forms):
    directory = root / DIRECTORY
    tables = {
        name: read_table(directory / f"{name}.tsv", columns)
        for name, columns in analytical.TABLES.items()
    }
    analytical.validate(corpus, forms, **tables)
    return tables


def validate_targets(targets, corpus, sources):
    unique(targets, ("source_key", "row_id"), "review targets")
    source_map = {row["source_key"]: row for row in sources}
    row_ids = {row["row_id"] for row in corpus}
    for target in targets:
        source = source_map.get(target["source_key"])
        if (source is None or source["consultation_mode"] in
                {"excluded", "opportunistic", "core_dictionary"}):
            raise SurveyError(f"target {target}: invalid non-core consultation scope")
        if target["row_id"] not in row_ids or not target["selection_basis"]:
            raise SurveyError(f"target {target}: row and selection basis are required")


def scope_rows(scope, corpus):
    if scope["population_scope"] == "all_rows":
        return {row["row_id"] for row in corpus}
    return set(ids(scope["row_ids"]))


def validate_scopes(scopes, corpus, sources, forms, targets):
    scope_map = {key[0]: row for key, row in unique(
        scopes, ("scope_id",), "reading scopes").items()}
    source_map = {row["source_key"]: row for row in sources}
    evidence = {row["evidence_id"]: row for row in forms}
    population = {row["row_id"] for row in corpus}
    validate_targets(targets, corpus, sources)
    for scope in scopes:
        key = scope["scope_id"]
        source = source_map.get(scope["source_key"])
        if source is None or source["consultation_mode"] in {"excluded", "core_dictionary"}:
            raise SurveyError(f"{key}: invalid reading-scope source")
        if scope["scope_kind"] not in {"screen", "method", "passage"}:
            raise SurveyError(f"{key}: invalid scope kind")
        if scope["population_scope"] not in {"all_rows", "named_rows", "source_general"}:
            raise SurveyError(f"{key}: invalid population scope")
        linked_rows = ids(scope["row_ids"])
        if (len(linked_rows) != len(set(linked_rows))
                or not set(linked_rows) <= population
                or (scope["population_scope"] == "named_rows" and not linked_rows)
                or (scope["population_scope"] != "named_rows" and linked_rows)):
            raise SurveyError(f"{key}: inconsistent population/row links")
        if scope["scope_kind"] == "screen" and scope["population_scope"] == "source_general":
            raise SurveyError(f"{key}: applicability screen requires a corpus population")
        if not scope["locator"] or not scope["selection_basis"]:
            raise SurveyError(f"{key}: locator and selection basis are required")
        if scope["printed_pages"] and not PAGES.fullmatch(scope["printed_pages"]):
            raise SurveyError(f"{key}: use printed pages, not sheet markers")
        if scope["status"] not in {"pending", "reviewed", "verification_gap"}:
            raise SurveyError(f"{key}: invalid reading status")
        if scope["verification"] not in VERIFICATIONS | {"unreviewed"}:
            raise SurveyError(f"{key}: invalid scope verification")
        if scope["status"] == "pending":
            if scope["verification"] != "unreviewed" or scope["evidence_ids"]:
                raise SurveyError(f"{key}: pending scope cannot claim verified extraction")
        else:
            if not scope["search_basis"] or not scope["assessment"]:
                raise SurveyError(f"{key}: actual reading/search assessment is required")
            if scope["status"] == "reviewed" and (
                    not scope["printed_pages"] or scope["verification"] == "unreviewed"):
                raise SurveyError(f"{key}: reviewed scope needs printed pages and verification")
            if scope["status"] == "verification_gap" and not scope["verification_limits"]:
                raise SurveyError(f"{key}: specify the verification limit")
        linked_evidence = ids(scope["evidence_ids"])
        if len(linked_evidence) != len(set(linked_evidence)):
            raise SurveyError(f"{key}: duplicate scope evidence")
        for evidence_id in linked_evidence:
            form = evidence.get(evidence_id)
            if form is None or form["source_key"] != scope["source_key"]:
                raise SurveyError(f"{key}: unknown or cross-source evidence")
            if (scope["population_scope"] == "named_rows"
                    and not set(ids(form["row_ids"])) & scope_rows(scope, corpus)):
                raise SurveyError(f"{key}: evidence does not support the named scope")
    for target in targets:
        linked = ids(target.get("scope_ids", ""))
        if target["source_key"] in READING_SOURCES and not linked:
            raise SurveyError(f"{target['source_key']}/{target['row_id']}: scope link is required")
        if len(linked) != len(set(linked)):
            raise SurveyError(f"{target['source_key']}/{target['row_id']}: duplicate target scopes")
        for key in linked:
            scope = scope_map.get(key)
            if (scope is None or scope["source_key"] != target["source_key"]
                    or scope["population_scope"] == "source_general"
                    or target["row_id"] not in scope_rows(scope, corpus)):
                raise SurveyError(f"{target['source_key']}/{target['row_id']}: incompatible target scope")


def load_scopes(root, corpus, sources, forms, targets):
    scopes = read_table(root / DIRECTORY / "reading_scopes.tsv", SCOPE_COLUMNS)
    validate_scopes(scopes, corpus, sources, forms, targets)
    return scopes


def require_reading_complete(corpus, sources, scopes, forms, targets, reviews):
    validate_scopes(scopes, corpus, sources, forms, targets)
    source_map = {row["source_key"]: row for row in sources}
    population = {row["row_id"] for row in corpus}
    problems = []
    if not population:
        raise SurveyError("Relevant three-source reading requires a nonempty corpus")
    for key in READING_SOURCES:
        source = source_map.get(key)
        scheduled = [scope for scope in scopes if scope["source_key"] == key]
        if source is None or source["consultation_mode"] != "systematic_relevant":
            problems.append(f"{key}: missing systematic source")
            continue
        if source["edition_status"] != "verified" or source["conventions_status"] != "verified":
            problems.append(f"{key}: identity/conventions not verified")
        for kind in ("screen", "method", "passage"):
            if not any(scope["scope_kind"] == kind for scope in scheduled):
                problems.append(f"{key}: no {kind} scope")
        screened = set().union(*(scope_rows(scope, corpus) for scope in scheduled
                                if scope["scope_kind"] == "screen"
                                and scope["status"] == "reviewed"))
        if screened != population:
            problems.append(f"{key}: {len(population - screened)} rows not applicability-screened")
        for scope in scheduled:
            if scope["status"] != "reviewed":
                problems.append(f"{scope['scope_id']}: {scope['status']}")
        required = [row for row in coverage_rows(corpus, [source], reviews, [
            target for target in targets if target["source_key"] == key])
                    if row["review_required"] == "1"
                    and row["status"] in {"unchecked", "verification_gap"}]
        problems.extend(f"{key}/{row['row_id']}: {row['status']}" for row in required)
    if problems:
        raise SurveyError("Relevant three-source reading INCOMPLETE: " + "; ".join(problems))


def reading_progress(corpus, sources, scopes, forms, targets, reviews):
    try:
        require_reading_complete(corpus, sources, scopes, forms, targets, reviews)
    except SurveyError as exc:
        state = str(exc)
    else:
        state = "Relevant three-source reading reviewed; analytical closeout is separate."
    lines = [
        "# Relevant three-source reading progress", "",
        "GENERATED from reading scopes, actual consultations and the live corpus.", "",
        state, "",
        "Pending page fields are navigation addresses, not completed passage citations.",
        "Applicability screening is not a lexical review or a claim of source absence.",
        "Source-general method readings do not create arbitrary corpus consultations.", "",
        "| Scope | Source / printed pages | Population | Status / verification | Reading basis / assessment / limits |",
        "| --- | --- | --- | --- | --- |",
    ]
    for scope in scopes:
        values = (
            scope["scope_id"], f"{scope['source_key']} / {scope['printed_pages'] or '(folio unresolved)'}",
            f"{scope['population_scope']} ({len(scope_rows(scope, corpus))} rows)",
            f"{scope['status']} / {scope['verification']}",
            f"{scope['locator']}; {scope['selection_basis']}; {scope['assessment']}; "
            f"limits: {scope['verification_limits'] or 'none recorded'}",
        )
        lines.append("| " + " | ".join(md(value) for value in values) + " |")
    return "\n".join(lines).rstrip() + "\n"


def coverage_rows(corpus, sources, reviews, targets=()):
    validate_targets(targets, corpus, sources)
    included = {source["source_key"] for source in sources if source["role"] != "excluded"}
    required = {
        (row["row_id"], source["source_key"]): "complete core population"
        for row in corpus for source in sources
        if source["consultation_mode"] == "core_dictionary"
        and source["role"] != "excluded"
    }
    required.update({
        (target["row_id"], target["source_key"]): target["selection_basis"]
        for target in targets
    })
    reviewed = {(row["row_id"], row["source_key"]): row for row in reviews}
    keys = set(required) | {key for key in reviewed if key[1] in included}
    return [{
        "row_id": row_id, "source_key": source_key,
        **reviewed.get((row_id, source_key), {
            "status": "unchecked", "evidence_ids": "", "search_basis": "", "assessment": "",
        }),
        "review_required": "1" if (row_id, source_key) in required else "0",
        "target_basis": required.get((row_id, source_key), "retained actual consultation"),
    } for row_id, source_key in sorted(keys, key=lambda key: (int(key[0]), key[1]))]


def incomplete(sources, coverage) -> bool:
    required_sources = {row["source_key"] for row in coverage
                        if row["review_required"] == "1"}
    return (any(row["status"] == "unchecked" for row in coverage
                if row["review_required"] == "1")
            or any(source["edition_status"] == "unreviewed"
                   or source["conventions_status"] == "unreviewed"
                   for source in sources if source["source_key"] in required_sources))


def require_core_complete(corpus, sources, reviews) -> None:
    included = {row["source_key"]: row for row in sources
                if row["role"] != "excluded"}
    missing_sources = set(CORE_SOURCES) - included.keys()
    if missing_sources:
        raise SurveyError(f"missing included sources: {', '.join(sorted(missing_sources))}")
    core = [included[key] for key in CORE_SOURCES]
    if any(source["consultation_mode"] != "core_dictionary" for source in core):
        raise SurveyError("core dictionary obligations cannot be demoted")
    coverage = coverage_rows(corpus, core, reviews)
    unchecked = [row for row in coverage if row["status"] == "unchecked"]
    if unchecked:
        examples = ", ".join(f"{row['source_key']}/{row['row_id']}"
                             for row in unchecked[:8])
        raise SurveyError(f"{len(unchecked)} unchecked pairs, including {examples}")
    if incomplete(core, coverage):
        raise SurveyError("core source identity or reconstruction conventions remain unreviewed")


def table_text(rows, columns) -> str:
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=columns, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def ledger_text(corpus, sources, forms, coverage) -> str:
    counts = Counter(row["status"] for row in coverage)
    state = "INCOMPLETE" if incomplete(sources, coverage) else "READING TARGETS REVIEWED WITH DECLARED LIMITS"
    lines = [
        "# PGmc reconstruction survey: source-faithful population ledger",
        "",
        "GENERATED from research SOURCE tables and the live corpus. Never hand-edit.",
        "",
        f"Row-target status: **{state}**. Row coverage is not passage or analytical completion.",
        "The separately generated [reading progress](reading_progress.md) tracks the three-source passages and applicability screens.",
        f"Population: {len(corpus)} OE rows; {sum(row['runnable'] == '1' for row in corpus)} runnable.",
        f"Required source/row targets: {sum(row['review_required'] == '1' for row in coverage)}; "
        f"retained actual consultations: {sum(row['review_required'] == '0' for row in coverage)}; "
        f"unchecked targets: {counts['unchecked']}; "
        f"declared verification gaps: {counts['verification_gap']}.",
        "",
        "Current CAPR fields below are observations, not new endorsements or approvals.",
        "A PGmc equality stage is the encoding convention, not independent author evidence.",
        "Author alternatives are not merged; discussion-only evidence is not a whole-word reconstruction.",
        "",
    ]
    for row in corpus:
        row_id = row["row_id"]
        lines.extend([
            f'<a id="row-{row_id}"></a>', "",
            f"## {row_id}: {md(row['concept'])} / {md(row['target'])}", "",
            f"Current citation: {md(row['proto'])} ({row['proto_stage']}); "
            f"selected input: {md(row['protoform'])} ({row['input_stage']}; "
            f"variety: {row['input_variety'] or 'none'}; {row['stage_basis']}).",
            f"Runnable: {row['runnable']}; derivation class: {row['derivation_class']}.",
            "",
            "| Evidence | Source / printed pages | Diplomatic form | Asserted stage / kind / cell | Comparison and argument | Verification |",
            "| --- | --- | --- | --- | --- | --- |",
        ])
        for form in forms:
            if row_id in ids(form["row_ids"]):
                values = [
                    form["evidence_id"], f"{form['source_key']} pp.{form['printed_pages']}",
                    form["diplomatic_form"] or "(process discussion, no quoted form)",
                    f"{form['asserted_stage']} / {form['form_kind']} / {form['cell']}",
                    f"{form['comparison_form']} {form['normalization_basis']} {form['argument']}",
                    form["verification"],
                ]
                lines.append("| " + " | ".join(md(value) for value in values) + " |")
        row_checks = [check for check in coverage if check["row_id"] == row_id]
        row_counts = Counter(check["status"] for check in row_checks)
        lines.extend(["", f"Coverage: {len(row_checks)} checks; "
                      f"{row_counts['unchecked']} unchecked; "
                      f"{row_counts['verification_gap']} verification gaps.", ""])
    return "\n".join(lines).rstrip("\n") + "\n"


def render(root: Path = ROOT) -> dict[Path, str]:
    corpus, sources, forms, reviews = load(root)
    directory = root / DIRECTORY
    targets = read_table(directory / "review_targets.tsv", TARGET_COLUMNS)
    scopes = load_scopes(root, corpus, sources, forms, targets)
    coverage = coverage_rows(corpus, sources, reviews, targets)
    analysis = load_analysis(root, corpus, forms)
    analytical_coverage = analytical.coverage(corpus, analysis["comparisons"])
    alignment_coverage = analytical.alignment_coverage(corpus, analysis["comparisons"])
    for row, alignment in zip(analytical_coverage, alignment_coverage):
        row.update(alignment)
    inputs = {
        root / "docs/refs.bib",
        root / "Germanic/data/germanic-aligned-final.tsv",
        root / "Germanic/data/entry_stage_metadata.tsv",
        root / "Germanic/data/entry_context_metadata.tsv",
        ROOT / "Germanic/tools/pgmc_reconstruction_survey.py",
        ROOT / "Germanic/tools/oe_pipeline.py",
        ROOT / "Germanic/docs/assembly/build_class_manifests.py",
        directory / "sources.tsv", directory / "forms.tsv", directory / "coverage.tsv",
        directory / "commentary.md",
        directory / "review_targets.tsv",
        directory / "reading_scopes.tsv",
        ROOT / "Germanic/tools/pgmc_reconstruction_analysis.py",
    }
    inputs.update(directory / f"{name}.tsv" for name in analytical.TABLES)
    inputs.update((directory / "reading_accountability").glob("*.tsv"))
    inputs.update(root / form["basis"] for form in forms)
    consulted_sources = ({row["source_key"] for row in coverage}
                         | {scope["source_key"] for scope in scopes})
    for source in sources:
        if source["source_key"] not in consulted_sources:
            continue
        for relative in ids(source["holding_paths"]):
            holding = root / relative
            inputs.update(holding.rglob("*.txt") if holding.is_dir() else [holding])
    provenance = {
        str(path.relative_to(root if path.is_relative_to(root) else ROOT)):
        hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(inputs)
    }
    try:
        require_reading_complete(corpus, sources, scopes, forms, targets, reviews)
    except SurveyError:
        reading_pending = True
    else:
        reading_pending = False
    return {
        directory / "corpus_inventory.tsv": table_text(corpus, tuple(corpus[0])),
        directory / "source_coverage.tsv": table_text(
            coverage, REVIEW_COLUMNS + ("review_required", "target_basis")),
        directory / "reconstruction_ledger.md": ledger_text(corpus, sources, forms, coverage),
        directory / "source_priorities.tsv": table_text(sources, SOURCE_COLUMNS),
        directory / "comparison_map.md": analytical.atlas(forms, **analysis),
        directory / "analytical_coverage.tsv": table_text(
            analytical_coverage, ("row_id", "status", "comparison_ids",
                                  "alignment_status", "alignment_case_ids")),
        directory / "reading_progress.md": reading_progress(
            corpus, sources, scopes, forms, targets, reviews),
        directory / "survey_provenance.json": json.dumps({
            "inputs": provenance,
            "population": len(corpus),
            "source_row_checks": len(coverage),
            "required_reading_targets": sum(row["review_required"] == "1" for row in coverage),
            "unreviewed_analytical_rows": sum(row["status"] != "reviewed" for row in analytical_coverage),
            "alignment_statuses": dict(Counter(row["alignment_status"] for row in analytical_coverage)),
            "reason_targets": dict(Counter(reason["reason_target"]
                                           for reason in analysis["rationales"])),
            "three_source_reading_pending": reading_pending,
            "reading_scope_statuses": dict(Counter(scope["status"] for scope in scopes)),
            "status": "incomplete" if reading_pending or incomplete(sources, coverage) or any(
                row["status"] != "reviewed" or row["alignment_status"] == "unreviewed"
                for row in analytical_coverage) else "reviewed_with_declared_limits",
        }, indent=2, sort_keys=True) + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--require-core-complete", action="store_true")
    parser.add_argument("--require-analysis-complete", action="store_true")
    parser.add_argument("--require-three-source-complete", action="store_true")
    parser.add_argument("--require-feature-alignment-complete", action="store_true")
    parser.add_argument("--query", metavar="SQL", help="Read-only SQL over validated evidence and analysis tables.")
    args = parser.parse_args()
    try:
        corpus, sources, forms, reviews = load()
        targets = read_table(ROOT / DIRECTORY / "review_targets.tsv", TARGET_COLUMNS)
        scopes = load_scopes(ROOT, corpus, sources, forms, targets)
        coverage = coverage_rows(corpus, sources, reviews, targets)
        analysis = load_analysis(ROOT, corpus, forms)
    except (SurveyError, analytical.AnalysisError, OSError) as exc:
        parser.exit(1, f"Reconstruction survey error: {exc}\n")
    reading_error = None
    try:
        require_reading_complete(corpus, sources, scopes, forms, targets, reviews)
    except SurveyError as exc:
        reading_error = str(exc)
    row_pending = incomplete(sources, coverage)
    pending = row_pending or reading_error is not None
    analytical_pending = [row for row in analytical.coverage(corpus, analysis["comparisons"])
                          if row["status"] != "reviewed"]
    if args.query:
        tables = {
            "corpus": (tuple(corpus[0]), corpus),
            "sources": (SOURCE_COLUMNS, sources), "forms": (FORM_COLUMNS, forms),
            "reviews": (REVIEW_COLUMNS, reviews), "targets": (TARGET_COLUMNS, targets),
            "reading_scopes": (SCOPE_COLUMNS, scopes),
            **{name: (analytical.TABLES[name], rows) for name, rows in analysis.items()},
        }
        try:
            print(analytical.query(tables, args.query), end="")
        except (analytical.AnalysisError, sqlite3.Error) as exc:
            parser.exit(1, f"Read-only query error: {exc}\n")
        return 0
    print(f"Valid evidence tables: {len(corpus)} OE rows, {len(forms)} evidence records.")
    print(f"Row targets {'INCOMPLETE' if row_pending else 'REVIEWED WITH DECLARED LIMITS'}: "
          f"{Counter(row['status'] for row in coverage)['unchecked']} unchecked targets.")
    print(f"Core citation-unit triage: {len(analytical_pending)} unreviewed rows.")
    print(reading_error or "Relevant three-source reading reviewed.")
    if (args.require_three_source_complete or args.require_feature_alignment_complete) and reading_error:
        parser.exit(2, f"{reading_error}\n")
    if (args.require_core_complete or args.require_analysis_complete
            or args.require_feature_alignment_complete or args.require_complete):
        try:
            require_core_complete(corpus, sources, reviews)
        except SurveyError as exc:
            parser.exit(2, f"Core dictionaries INCOMPLETE: {exc}\n")
        print(f"Core dictionaries reviewed: {len(corpus) * len(CORE_SOURCES)} pairs; "
              "recorded verification limits remain explicit.")
    if args.require_analysis_complete:
        try:
            analytical.require_complete(corpus, analysis["comparisons"])
        except analytical.AnalysisError as exc:
            parser.exit(2, f"{exc}\n")
    if args.require_feature_alignment_complete or args.require_complete:
        try:
            analytical.require_alignment_complete(corpus, analysis["comparisons"])
        except analytical.AnalysisError as exc:
            parser.exit(2, f"{exc}\n")
    return 2 if args.require_complete and (pending or analytical_pending) else 0


if __name__ == "__main__":
    raise SystemExit(main())
