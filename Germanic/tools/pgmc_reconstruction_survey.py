#!/usr/bin/env python3
"""Validate research evidence and project the complete OE survey population.

Generated outputs belong to the artifact graph. This command only validates;
--require-complete additionally refuses unfinished source/row reviews.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

from check_bibliography_sanity import parse_entries
from oe_pipeline import load_rows as load_selected_rows

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/docs/assembly"))
from build_class_manifests import resolve_stages

DIRECTORY = Path("Germanic/docs/lexeme_reports/pgmc_reconstructions")
SOURCE_COLUMNS = (
    "source_key", "role", "holding_paths", "scope", "edition_status",
    "conventions_status", "notes",
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


def coverage_rows(corpus, sources, reviews):
    reviewed = {(row["row_id"], row["source_key"]): row for row in reviews}
    return [{
        "row_id": row["row_id"], "source_key": source["source_key"],
        **reviewed.get((row["row_id"], source["source_key"]), {
            "status": "unchecked", "evidence_ids": "", "search_basis": "", "assessment": "",
        }),
    } for row in corpus for source in sorted(sources, key=lambda item: item["source_key"])
        if source["role"] != "excluded"]


def incomplete(sources, coverage) -> bool:
    return (any(row["status"] == "unchecked" for row in coverage)
            or any(source["edition_status"] == "unreviewed"
                   or source["conventions_status"] == "unreviewed"
                   for source in sources if source["role"] != "excluded"))


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
    state = "INCOMPLETE" if incomplete(sources, coverage) else "REVIEWED WITH DECLARED LIMITS"
    lines = [
        "# PGmc reconstruction survey: comprehensive population ledger",
        "",
        "GENERATED from research SOURCE tables and the live corpus. Never hand-edit.",
        "",
        f"Survey status: **{state}**. Schema validity is not scientific completion.",
        f"Population: {len(corpus)} OE rows; {sum(row['runnable'] == '1' for row in corpus)} runnable.",
        f"Source/row checks: {len(coverage)}; unchecked: {counts['unchecked']}; "
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
    coverage = coverage_rows(corpus, sources, reviews)
    directory = root / DIRECTORY
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
    }
    inputs.update(root / form["basis"] for form in forms)
    for source in sources:
        if source["role"] == "excluded":
            continue
        for relative in ids(source["holding_paths"]):
            holding = root / relative
            inputs.update(holding.rglob("*.txt") if holding.is_dir() else [holding])
    provenance = {
        str(path.relative_to(root if path.is_relative_to(root) else ROOT)):
        hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(inputs)
    }
    return {
        directory / "corpus_inventory.tsv": table_text(corpus, tuple(corpus[0])),
        directory / "source_coverage.tsv": table_text(coverage, REVIEW_COLUMNS),
        directory / "reconstruction_ledger.md": ledger_text(corpus, sources, forms, coverage),
        directory / "survey_provenance.json": json.dumps({
            "inputs": provenance,
            "population": len(corpus),
            "source_row_checks": len(coverage),
            "status": "incomplete" if incomplete(sources, coverage) else "reviewed_with_declared_limits",
        }, indent=2, sort_keys=True) + "\n",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-complete", action="store_true")
    args = parser.parse_args()
    try:
        corpus, sources, forms, reviews = load()
    except (SurveyError, OSError) as exc:
        parser.exit(1, f"Reconstruction survey error: {exc}\n")
    coverage = coverage_rows(corpus, sources, reviews)
    pending = incomplete(sources, coverage)
    print(f"Valid evidence tables: {len(corpus)} OE rows, {len(forms)} evidence records.")
    print(f"Survey {'INCOMPLETE' if pending else 'REVIEWED WITH DECLARED LIMITS'}: "
          f"{Counter(row['status'] for row in coverage)['unchecked']} unchecked source/row pairs.")
    return 2 if args.require_complete and pending else 0


if __name__ == "__main__":
    raise SystemExit(main())
