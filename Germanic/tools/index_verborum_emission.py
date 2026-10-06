#!/usr/bin/env python3
"""Central Index Verborum occurrence/emission planner.

Owns:
  * deterministic source-locator occurrence IDs
  * book-inclusion classification
  * canonical index-command generation
  * occurrence->emission collapsing policy
  * canonical TSV view generation:
      - index_verborum_emission_table.tsv
      - index_verborum_book_occurrences.tsv
      - index_verborum_book_emissions.tsv
      - index_verborum_book_main.tsv (compatibility alias of book_emissions)
      - index_verborum_book_print_unique.tsv
"""
from __future__ import annotations

import csv
import hashlib
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))

import index_verborum_render as ivr
from build_full_lexical_volume import normalize_print_text as npt

BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"
MANIFEST_PATH = ASSEMBLY_DIR / "manifest_all_by_class.tsv"
PRINT_MAIN_PATH = BOOK_DIR / "index_verborum_print_main.tsv"
BOOK_MAIN_PATH = BOOK_DIR / "index_verborum_book_main.tsv"
BOOK_OCCURRENCES_PATH = BOOK_DIR / "index_verborum_book_occurrences.tsv"
BOOK_EMISSIONS_PATH = BOOK_DIR / "index_verborum_book_emissions.tsv"
BOOK_PRINT_UNIQUE_PATH = BOOK_DIR / "index_verborum_book_print_unique.tsv"
EMISSION_TABLE_PATH = BOOK_DIR / "index_verborum_emission_table.tsv"
INTRO_PATH = ASSEMBLY_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = (
    REPO_ROOT
    / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_20.md"
)

_LINE_INJ_SCOPES = frozenset(
    {"table_semantic_auto", "table_semantic_decision", "broad_prose_decision"}
)
_NON_EXPLICIT_COLLAPSE_PATHS = frozenset({"heading_injection", "line_injection"})
_SOURCE_SCOPE_PREFIX = {
    "lexical_heading": "heading",
    "lexical_protoform": "lexical-protoform",
    "lexical_proto": "lexical-proto",
    "trace_proto_input": "trace",
    "table_semantic_auto": "table-auto",
    "table_semantic_decision": "table-decision",
    "broad_prose_decision": "broad-prose",
    "override": "override",
}

_LANG_META: dict | None = None
_VAR_REG: object | None = None


def _lang_meta() -> dict:
    global _LANG_META
    if _LANG_META is None:
        _LANG_META = ivr.load_language_registry()
    return _LANG_META


def _var_reg() -> object:
    global _VAR_REG
    if _VAR_REG is None:
        _VAR_REG = ivr.load_variety_registry()
    return _VAR_REG


def make_index_command(row: dict[str, str]) -> str:
    return ivr.index_command(
        row.get("language", ""),
        row.get("sort_key", ""),
        npt(row.get("display", "")),
        (row.get("variety") or "").strip(),
        lang_meta=_lang_meta(),
        var_registry=_var_reg(),
    )


def make_non_explicit_occurrence_id(row: dict[str, str]) -> str:
    scope = (row.get("source_scope") or "").strip() or "structured"
    ref = (row.get("source_ref") or "").strip()
    language = (row.get("language") or "").strip()
    variety = (row.get("variety") or "").strip()
    form = (row.get("form") or "").strip()
    display = (row.get("display") or "").strip()
    role = (row.get("form_role") or "").strip()
    sort_key = (row.get("sort_key") or "").strip()
    payload = "\x1f".join([scope, ref, language, variety, form, display, role, sort_key])
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:14]
    prefix = _SOURCE_SCOPE_PREFIX.get(scope, re.sub(r"[^a-z0-9]+", "-", scope.lower()).strip("-") or "structured")
    return f"{prefix}:{digest}"


def ensure_occurrence_id(row: dict[str, str]) -> str:
    scope = (row.get("source_scope") or "").strip()
    occ_id = (row.get("occurrence_id") or "").strip()
    if scope == "explicit_tag":
        if not occ_id:
            raise ValueError(f"explicit_tag row has blank occurrence_id: {row}")
        return occ_id
    return occ_id or make_non_explicit_occurrence_id(row)


def parse_occurrence_id(occ_id: str) -> tuple[str, int]:
    last_colon = occ_id.rfind(":")
    if last_colon < 0:
        return occ_id, 1
    suffix = occ_id[last_colon + 1 :]
    if suffix.isdigit():
        return occ_id[:last_colon], int(suffix)
    return occ_id, 1


def load_model_entry_headings() -> dict[str, str]:
    headings: dict[str, str] = {}
    with MANIFEST_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            mp = (row.get("model_entry_path") or "").strip()
            li = (row.get("lexical_item") or "").strip()
            ct = (row.get("counterpart") or "").strip()
            dc = (row.get("derivation_class") or "").strip()
            if mp and li:
                headings[mp] = f"{li} — OE {'*' + ct if dc == 'reconstructed_oe' else ct}"
    return headings


class EmissionClassification(NamedTuple):
    emission_path: str
    site: str
    index_command: str
    in_book: bool


def classify_emission(
    row: dict[str, str],
    model_entry_headings: dict[str, str],
) -> EmissionClassification:
    scope = (row.get("source_scope") or "").strip()
    ref = (row.get("source_ref") or "").strip()
    cmd = make_index_command(row)
    manifest_heading_set = set(model_entry_headings.values())
    book_paths = {
        INTRO_PATH.relative_to(REPO_ROOT).as_posix(),
        CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix(),
        *model_entry_headings.keys(),
    }

    if scope == "explicit_tag":
        path_part = ref.rsplit(":", 1)[0] if ":" in ref else ref
        return EmissionClassification("explicit_tag", ref, cmd, path_part in book_paths)

    if not ref:
        return EmissionClassification("source_not_in_book", ref, cmd, False)

    if ".md:" in ref:
        path_part, line_part = ref.rsplit(":", 1)
        if scope in _LINE_INJ_SCOPES and line_part.isdigit() and path_part not in model_entry_headings:
            in_book = path_part in {
                INTRO_PATH.relative_to(REPO_ROOT).as_posix(),
                CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix(),
            }
            return EmissionClassification("line_injection", f"{path_part}:{line_part}", cmd, in_book)
        if path_part in model_entry_headings:
            return EmissionClassification("heading_injection", model_entry_headings[path_part], cmd, True)
        if line_part.isdigit():
            return EmissionClassification("line_injection", f"{path_part}:{line_part}", cmd, path_part in book_paths)
        return EmissionClassification("source_not_in_book", ref, cmd, False)

    in_book = ref in manifest_heading_set
    if in_book:
        return EmissionClassification("heading_injection", ref, cmd, True)
    return EmissionClassification("source_not_in_book", ref, cmd, False)


def load_print_main(path: Path = PRINT_MAIN_PATH) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))


_EMISSION_TABLE_FIELDS = [
    "occurrence_id",
    "emission_id",
    "source_ref",
    "source_scope",
    "emission_path",
    "site",
    "in_book",
    "collapsed_into",
    "language",
    "variety",
    "form",
    "display",
    "sort_key",
    "form_role",
    "index_command",
]


def _emission_id(path: str, site: str, cmd: str) -> str:
    payload = "\x1f".join([path, site, cmd])
    return f"emit:{hashlib.sha1(payload.encode('utf-8')).hexdigest()[:14]}"


def build_emission_table(
    main_rows: list[dict[str, str]],
    model_entry_headings: dict[str, str],
) -> list[dict[str, str]]:
    enriched: list[dict[str, str]] = []
    for row in main_rows:
        occ_id = ensure_occurrence_id(row)
        ec = classify_emission(row, model_entry_headings)
        emission_id = occ_id if ec.emission_path == "explicit_tag" else _emission_id(ec.emission_path, ec.site, ec.index_command)
        enriched.append(
            {
                "occurrence_id": occ_id,
                "emission_id": emission_id,
                "source_ref": (row.get("source_ref") or "").strip(),
                "source_scope": (row.get("source_scope") or "").strip(),
                "emission_path": ec.emission_path,
                "site": ec.site,
                "in_book": "1" if ec.in_book else "0",
                "collapsed_into": "",
                "language": row.get("language", ""),
                "variety": row.get("variety", ""),
                "form": row.get("form", ""),
                "display": row.get("display", ""),
                "sort_key": row.get("sort_key", ""),
                "form_role": row.get("form_role", ""),
                "index_command": ec.index_command,
            }
        )

    first_by_key: dict[str, str] = {}
    for rec in enriched:
        key = f"{rec['emission_path']}\t{rec['site']}\t{rec['index_command']}"
        path = rec["emission_path"]
        if path in _NON_EXPLICIT_COLLAPSE_PATHS and rec["in_book"] == "1":
            if key not in first_by_key:
                first_by_key[key] = rec["emission_id"]
                rec["collapsed_into"] = ""
            else:
                rec["collapsed_into"] = first_by_key[key]
                rec["emission_id"] = first_by_key[key]
    return enriched


def build_book_occurrences_rows(emission_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [r for r in emission_rows if r["in_book"] == "1"]


def build_book_emissions_rows(emission_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in emission_rows:
        if row["in_book"] == "1":
            grouped[row["emission_id"]].append(row)
    out: list[dict[str, str]] = []
    for emission_id, items in grouped.items():
        # The representative is the unique row with blank collapsed_into.
        # For explicit emissions there is exactly one member with blank collapsed_into.
        # For shared non-explicit groups the first-processed row carries blank collapsed_into.
        representatives = [
            r for r in items
            if not (r.get("collapsed_into") or "").strip()
        ]
        assert len(representatives) == 1, (
            f"Emission {emission_id} must have exactly one representative "
            f"(blank collapsed_into); got {len(representatives)}"
        )
        representative = representatives[0]
        out.append(
            {
                "emission_id": emission_id,
                "representative_occurrence_id": representative["occurrence_id"],
                "emission_path": representative["emission_path"],
                "site": representative["site"],
                "index_command": representative["index_command"],
                "language": representative["language"],
                "variety": representative["variety"],
                "display": representative["display"],
                "sort_key": representative["sort_key"],
                "form_role": representative["form_role"],
                "source_scope": representative["source_scope"],
                "source_ref": representative["source_ref"],
                "source_occurrence_count": str(len(items)),
                "source_occurrence_ids": "|".join(
                    r["occurrence_id"] for r in sorted(items, key=lambda r: r["occurrence_id"])
                ),
            }
        )
    out.sort(key=lambda r: (r["emission_path"], r["site"], r["sort_key"], r["display"], r["emission_id"]))
    return out


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_emission_views(
    main_rows: list[dict[str, str]] | None = None,
    model_entry_headings: dict[str, str] | None = None,
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    if main_rows is None:
        main_rows = load_print_main()
    if model_entry_headings is None:
        model_entry_headings = load_model_entry_headings()

    emission_rows = build_emission_table(main_rows, model_entry_headings)
    book_occ_rows = build_book_occurrences_rows(emission_rows)
    book_em_rows = build_book_emissions_rows(emission_rows)

    fields = list(main_rows[0].keys()) if main_rows else []
    by_occ_id = {r["occurrence_id"]: r for r in main_rows}
    book_occ_print_rows = [by_occ_id[r["occurrence_id"]] for r in book_occ_rows if r["occurrence_id"] in by_occ_id]

    write_tsv(EMISSION_TABLE_PATH, emission_rows, _EMISSION_TABLE_FIELDS)
    write_tsv(BOOK_OCCURRENCES_PATH, book_occ_print_rows, fields)
    write_tsv(
        BOOK_EMISSIONS_PATH,
        book_em_rows,
        [
            "emission_id",
            "representative_occurrence_id",
            "emission_path",
            "site",
            "index_command",
            "language",
            "variety",
            "display",
            "sort_key",
            "form_role",
            "source_scope",
            "source_ref",
            "source_occurrence_count",
            "source_occurrence_ids",
        ],
    )
    write_tsv(
        BOOK_MAIN_PATH,
        book_em_rows,
        [
            "emission_id",
            "representative_occurrence_id",
            "emission_path",
            "site",
            "index_command",
            "language",
            "variety",
            "display",
            "sort_key",
            "form_role",
            "source_scope",
            "source_ref",
            "source_occurrence_count",
            "source_occurrence_ids",
        ],
    )
    write_tsv(
        BOOK_PRINT_UNIQUE_PATH,
        build_print_unique_rows(book_occ_print_rows),
        [
            "language",
            "display",
            "sort_key",
            "printed_variety",
            "source_varieties",
            "occurrence_count",
            "roles",
            "source_scopes",
            "sample_sources",
        ],
    )

    return emission_rows, book_occ_rows, book_em_rows


def build_print_unique_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[tuple[str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        variety = (row.get("variety") or "").strip()
        printed_variety = _var_reg().printed_label(variety) if variety else ""
        key = (
            (row.get("language") or "").strip(),
            (row.get("display") or "").strip(),
            (row.get("sort_key") or "").strip(),
            printed_variety,
        )
        grouped[key].append(row)
    out: list[dict[str, str]] = []
    for (language, display, sort_key, printed_variety), items in grouped.items():
        out.append(
            {
                "language": language,
                "display": display,
                "sort_key": sort_key,
                "printed_variety": printed_variety,
                "source_varieties": "; ".join(
                    sorted({(r.get("variety") or "").strip() for r in items if (r.get("variety") or "").strip()})
                ),
                "occurrence_count": str(len(items)),
                "roles": "; ".join(sorted({(r.get("form_role") or "").strip() for r in items if (r.get("form_role") or "").strip()})),
                "source_scopes": "; ".join(sorted({(r.get("source_scope") or "").strip() for r in items if (r.get("source_scope") or "").strip()})),
                "sample_sources": "; ".join(sorted({(r.get("source_ref") or "").strip() for r in items if (r.get("source_ref") or "").strip()})[:3]),
            }
        )
    out.sort(key=lambda r: (r["language"], r["sort_key"], r["display"], r["printed_variety"]))
    return out


def load_emission_table(path: Path = EMISSION_TABLE_PATH) -> list[dict[str, str]]:
    return list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))


def check_no_occurrence_id_collisions(rows: list[dict[str, str]]) -> None:
    counts = Counter(r["occurrence_id"] for r in rows)
    dupes = {k: v for k, v in counts.items() if v > 1}
    assert not dupes, (
        f"duplicate occurrence_id values in emission table ({len(dupes)}):\n"
        + "\n".join(f"  {k}: {v}" for k, v in sorted(dupes.items())[:5])
    )


def check_emission_table_assertions(
    main_rows: list[dict[str, str]],
    emission_rows: list[dict[str, str]],
) -> None:
    expected_occ = Counter(ensure_occurrence_id(r) for r in main_rows)
    actual_occ = Counter(r["occurrence_id"] for r in emission_rows)
    assert expected_occ == actual_occ, "print_main occurrence IDs != emission-table occurrence IDs"

    rows_by_occ = defaultdict(list)
    for row in emission_rows:
        rows_by_occ[row["occurrence_id"]].append(row)
    bad_occ = [occ for occ, vals in rows_by_occ.items() if len(vals) != 1]
    assert not bad_occ, f"occurrence IDs with !=1 emission-table row: {bad_occ[:5]}"

    in_book_rows = [r for r in emission_rows if r["in_book"] == "1"]
    source_not_in_book_to_book = [
        r for r in in_book_rows if r["emission_path"] == "source_not_in_book"
    ]
    assert not source_not_in_book_to_book, (
        "source_not_in_book occurrences cannot map to book emissions"
    )

    emission_to_occ: defaultdict[str, list[str]] = defaultdict(list)
    for row in in_book_rows:
        emission_to_occ[row["emission_id"]].append(row["occurrence_id"])
    empty = [eid for eid, occs in emission_to_occ.items() if not occs]
    assert not empty, f"book emission IDs without source occurrences: {empty[:5]}"


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-views", action="store_true", help="Write emission/book occurrence/emission TSVs")
    parser.add_argument("--check", action="store_true", help="Run planner assertions")
    args = parser.parse_args()

    main_rows = load_print_main()
    headings = load_model_entry_headings()
    emission_rows = build_emission_table(main_rows, headings)

    if args.write_views:
        emission_rows, book_occ_rows, book_em_rows = write_emission_views(main_rows, headings)
        print(f"Wrote {len(emission_rows)} rows to {EMISSION_TABLE_PATH}")
        print(f"Wrote {len(book_occ_rows)} rows to {BOOK_OCCURRENCES_PATH}")
        print(f"Wrote {len(book_em_rows)} rows to {BOOK_EMISSIONS_PATH}")

    if args.check:
        check_no_occurrence_id_collisions(emission_rows)
        check_emission_table_assertions(main_rows, emission_rows)
        print("Emission planner checks passed.")


if __name__ == "__main__":
    main()
