#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import re
import sys
from collections import Counter
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
REPORTS_DIR = REPO_ROOT / "Germanic/docs/sound_changes/change_reports"
MANIFEST_PATH = REPORTS_DIR / "report_manifest.tsv"
SCAFFOLD_PATH = REPORTS_DIR / "sound_change_half_scaffold.tsv"
INVENTORY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/book_dossiers/sound_change_book_dossier_inventory.tsv"
CHRONOLOGY_INDEX_PATH = (
    REPO_ROOT / "Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv"
)


def env_path(name: str) -> Path | None:
    raw = os.environ.get(name)
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_absolute() else SCRIPT_DIR / path


OUTPUT_PATH = env_path("SOUND_CHANGE_VOLUME_OUTPUT_MD") or (SCRIPT_DIR / "sound_change_volume_alpha_01.md")
COVERAGE_REPORT_PATH = env_path("SOUND_CHANGE_COVERAGE_REPORT_MD") or (
    REPORTS_DIR / "sound_change_half_coverage_report.md"
)
ASSEMBLED_STATUSES = {"pilot", "full", "scaffold"}
DOCUMENTED_STATUSES = ASSEMBLED_STATUSES | {"needs_literature", "needs_human_review", "grouped_elsewhere"}
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
BOLD_SPAN_RE = re.compile(r"(?<!\*)\*\*([^*\n]+)\*\*(?!\*)")
ITALIC_SPAN_RE = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
FORM_CONNECTOR_WORDS = {"and", "or", "written", "spelled", "vs", "with"}
INLINE_CONNECTOR_WORDS = FORM_CONNECTOR_WORDS | {"from", "to", "through", "beside", "via"}
STAGE_LABELS = {
    "PGmc",
    "PWGmc",
    "WGmc",
    "NWGmc",
    "Angl",
    "Anglian",
    "OE",
    "WS",
    "West Saxon",
    "Mercian",
    "Northumbrian",
    "Kentish",
}
INLINE_SEPARATOR_CHARS = {"~", "/", ">", "<", "=", ",", ";", "(", ")", "[", "]", "{", "}"}
PRINT_LONG_I_ACUTE = "\u00ed"
PRINT_TILDE_EDGE_CHAR_CLASS = r"A-Za-z\u00C0-\u024F\u00F0\u00FE\u00DE\u00C6\u00E6\u0152\u0153\u014A\u014B" + PRINT_LONG_I_ACUTE
RECONSTRUCTED_STEM_TRAILING_STAR_RE = re.compile(
    rf"(?<=\*)([{PRINT_TILDE_EDGE_CHAR_CLASS}][{PRINT_TILDE_EDGE_CHAR_CLASS}0-9'./-]*)\*(?=(?:\s|$|[.,;:!?)]))"
)
FORM_TILDE_SPACING_RE = re.compile(rf"(?<=[{PRINT_TILDE_EDGE_CHAR_CLASS}0-9])~(?=[{PRINT_TILDE_EDGE_CHAR_CLASS}0-9])")
FENCED_CODE_BLOCK_RE = re.compile(r"(?ms)(^```[^\n]*\n.*?^```[ \t]*\n?)")


def normalize_print_text(text: str) -> str:
    text = RECONSTRUCTED_STEM_TRAILING_STAR_RE.sub(r"\1", text)
    return FORM_TILDE_SPACING_RE.sub(" ~ ", text)


def italicize_form(text: str) -> str:
    text = normalize_print_text(text)
    if not text:
        return text
    stripped = text.strip()
    if not stripped:
        return text
    leading = text[: len(text) - len(text.lstrip())]
    trailing = text[len(text.rstrip()) :]
    core = stripped
    if core.startswith("*") and len(core) > 1:
        return f"{leading}*{core[1:]}*{trailing}"
    return f"{leading}*{core}*{trailing}"


def keep_as_code(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if "/" in stripped or "\\" in stripped or stripped.startswith("--") or "::" in stripped:
        return True
    if re.search(r"[A-Za-z0-9_-]+\.[A-Za-z0-9._-]+", stripped):
        return True
    if re.search(r"[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+/[A-Za-z0-9_.\-/]+", stripped):
        return True
    if re.search(r"\b(?:SC|GO|RU)\d{2,4}\b", stripped):
        return True
    if re.search(r"(?:\[\{.*?\}\s*->|->\s*0\b.*\|\||\|\||\.\#\.)", stripped):
        return True
    return False


def normalize_inline_code_content(text: str) -> str:
    return normalize_print_text(text.replace("\\_", "_"))


def is_token_boundary(text: str, index: int) -> bool:
    return index <= 0 or index >= len(text) or not text[index].isalnum()


def tokenize_linguistic_span(text: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    current = []
    mode = None

    def flush() -> None:
        nonlocal current, mode
        if current:
            tokens.append((mode or "sep", "".join(current)))
            current = []
            mode = None

    for char in text:
        char_mode = "word" if (char.isalnum() or char in {"*", "-", "'", ".", PRINT_LONG_I_ACUTE}) else "sep"
        if char_mode != mode:
            flush()
            mode = char_mode
        current.append(char)
    flush()
    return tokens


def next_non_whitespace_token(tokens: list[tuple[str, str]], start: int, step: int) -> tuple[str, str] | None:
    idx = start + step
    while 0 <= idx < len(tokens):
        if tokens[idx][1].strip():
            return tokens[idx]
        idx += step
    return None


def is_form_token(
    token: str,
    previous: tuple[str, str] | None = None,
    following: tuple[str, str] | None = None,
) -> bool:
    stripped = token.strip()
    if not stripped:
        return False
    lowered = stripped.lower()
    if lowered in INLINE_CONNECTOR_WORDS:
        return False
    if stripped in STAGE_LABELS:
        return False
    if stripped.startswith("*"):
        return True
    if any(char in stripped for char in ("þ", "ð", "æ", "ǣ", "œ", "ȳ", "á", "é", "í", "ó", "ú", "ā", "ē", "ī", "ō", "ū")):
        return True
    if previous and previous[0] == "sep" and any(ch in previous[1] for ch in INLINE_SEPARATOR_CHARS):
        return True
    if following and following[0] == "sep" and any(ch in following[1] for ch in INLINE_SEPARATOR_CHARS):
        return True
    if stripped.islower() and len(stripped) >= 2:
        return True
    return False


def format_linguistic_inline_code(text: str) -> str:
    normalized = normalize_inline_code_content(text)
    if keep_as_code(normalized):
        return f"`{normalized}`"
    tokens = tokenize_linguistic_span(normalized)
    if not tokens:
        return italicize_form(normalized)

    rendered: list[str] = []
    saw_form = False
    for idx, (kind, token) in enumerate(tokens):
        if kind != "word":
            rendered.append(token)
            continue
        previous = next_non_whitespace_token(tokens, idx, -1)
        following = next_non_whitespace_token(tokens, idx, 1)
        if is_form_token(token, previous=previous, following=following):
            rendered.append(italicize_form(token))
            saw_form = True
        else:
            rendered.append(token)
    if saw_form:
        return "".join(rendered)
    return italicize_form(normalized)


def convert_inline_code(text: str) -> str:
    return INLINE_CODE_RE.sub(lambda match: format_linguistic_inline_code(match.group(1)), text)


def has_linguistic_inline_code(text: str) -> bool:
    for match in INLINE_CODE_RE.finditer(text):
        if not keep_as_code(normalize_inline_code_content(match.group(1))):
            return True
    return False


def looks_like_linguistic_markup(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if keep_as_code(stripped):
        return False
    if any(char in stripped for char in ("*", "~", ">", "<", "/", "þ", "ð", "æ", "ǣ", "œ", "ȳ", "á", "é", "í", "ó", "ú", "ā", "ē", "ī", "ō", "ū")):
        return True
    if stripped in STAGE_LABELS:
        return True
    if re.search(r"\b(?:OE|PGmc|PWGmc|WGmc|NWGmc)\b", stripped):
        return True
    if stripped.islower() and len(stripped) >= 3:
        return True
    return False


def demote_bold_forms(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if not looks_like_linguistic_markup(inner):
            return match.group(0)
        inner = normalize_print_text(inner)
        return italicize_form(inner)

    return BOLD_SPAN_RE.sub(repl, text)


def unwrap_bolded_linguistic_markup(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if not looks_like_linguistic_markup(inner):
            return match.group(0)
        return normalize_print_text(inner)

    return ITALIC_SPAN_RE.sub(repl, text)


def tidy_prose(text: str) -> str:
    text = normalize_print_text(text)
    text = convert_inline_code(text)
    text = demote_bold_forms(text)
    text = unwrap_bolded_linguistic_markup(text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r" +", " ", text)
    return text


def tidy_markdown_prose(text: str) -> str:
    parts = FENCED_CODE_BLOCK_RE.split(text)
    cleaned_parts: list[str] = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            cleaned_parts.append(part)
        else:
            cleaned_parts.append(tidy_prose(part))
    return "".join(cleaned_parts)


def split_semicolon_field(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip() and part.strip().lower() != "none"]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        lines = [line for line in handle if not line.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def load_manifest_rows() -> list[dict[str, str]]:
    rows = read_tsv(MANIFEST_PATH)
    if not rows:
        raise ValueError(f"No rows found in {MANIFEST_PATH}")
    normalized: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for row in rows:
        row_id = (row.get("ID") or "").strip()
        status = (row.get("STATUS") or "").strip()
        row["change_ids"] = split_semicolon_field(row.get("CHANGE_IDS") or "")
        if not row_id:
            raise ValueError(f"Manifest row is missing ID: {row}")
        if row_id in seen_ids:
            raise ValueError(f"Duplicate manifest ID: {row_id}")
        if status not in DOCUMENTED_STATUSES:
            raise ValueError(f"Unsupported manifest STATUS {status!r} in {MANIFEST_PATH}")
        seen_ids.add(row_id)
        normalized.append(row)
    assembled = [row for row in normalized if (row.get("STATUS") or "").strip() in ASSEMBLED_STATUSES]
    if not assembled:
        raise ValueError(f"No assembled rows found in {MANIFEST_PATH}")
    return normalized


def load_scaffold_rows() -> list[dict[str, str]]:
    rows = read_tsv(SCAFFOLD_PATH)
    if not rows:
        raise ValueError(f"No rows found in {SCAFFOLD_PATH}")
    normalized: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for row in rows:
        unit_id = (row.get("UNIT_ID") or "").strip()
        if not unit_id:
            raise ValueError(f"Scaffold row is missing UNIT_ID: {row}")
        if unit_id in seen_ids:
            raise ValueError(f"Duplicate scaffold UNIT_ID: {unit_id}")
        row["change_ids"] = split_semicolon_field(row.get("CHANGE_IDS") or "")
        if not row["change_ids"]:
            raise ValueError(f"Scaffold row {unit_id} is missing CHANGE_IDS")
        seen_ids.add(unit_id)
        normalized.append(row)
    return normalized


def load_inventory_rows() -> dict[str, dict[str, str]]:
    rows = read_tsv(INVENTORY_PATH)
    if not rows:
        raise ValueError(f"No rows found in {INVENTORY_PATH}")
    return {(row.get("change_id") or "").strip(): row for row in rows}


def load_chronology_ids() -> list[str]:
    rows = read_tsv(CHRONOLOGY_INDEX_PATH)
    chronology_ids = [(row.get("change_id") or "").strip() for row in rows if (row.get("change_id") or "").strip()]
    if not chronology_ids:
        raise ValueError(f"No chronology rows found in {CHRONOLOGY_INDEX_PATH}")
    return chronology_ids


def validate_scaffold_coverage(
    scaffold_rows: list[dict[str, str]],
    chronology_ids: list[str],
    inventory_rows: dict[str, dict[str, str]],
) -> None:
    chronology_set = set(chronology_ids)
    represented: list[str] = []
    duplicates: set[str] = set()
    for row in scaffold_rows:
        for change_id in row["change_ids"]:
            if change_id not in chronology_set:
                raise ValueError(f"Unknown chronology change ID {change_id} in scaffold row {row['UNIT_ID']}")
            if change_id not in inventory_rows:
                raise ValueError(f"Unknown inventory change ID {change_id} in scaffold row {row['UNIT_ID']}")
            if change_id in represented:
                duplicates.add(change_id)
            represented.append(change_id)
    if duplicates:
        raise ValueError(f"Duplicate scaffold coverage for {', '.join(sorted(duplicates))}")
    missing = sorted(chronology_set - set(represented))
    if missing:
        raise ValueError(f"Missing scaffold coverage for {', '.join(missing)}")


def validate_manifest_alignment(manifest_rows: list[dict[str, str]], scaffold_rows: list[dict[str, str]]) -> None:
    assembled_manifest_rows = [row for row in manifest_rows if (row.get("STATUS") or "").strip() in ASSEMBLED_STATUSES]
    manifest_ids = {(row.get("ID") or "").strip() for row in assembled_manifest_rows}
    scaffold_ids = {(row.get("UNIT_ID") or "").strip() for row in scaffold_rows}
    if manifest_ids != scaffold_ids:
        missing_from_manifest = sorted(scaffold_ids - manifest_ids)
        missing_from_scaffold = sorted(manifest_ids - scaffold_ids)
        raise ValueError(
            "Manifest/scaffold mismatch: "
            f"missing from manifest={missing_from_manifest}, missing from scaffold={missing_from_scaffold}"
        )
    for row in assembled_manifest_rows:
        report_path = (row.get("REPORT_PATH") or "").strip()
        if not report_path:
            raise ValueError(f"Manifest row is missing REPORT_PATH: {row}")
        source_path = REPORTS_DIR / report_path
        if not source_path.exists():
            raise FileNotFoundError(f"Report file not found: {source_path}")


def compute_coverage_stats(
    scaffold_rows: list[dict[str, str]],
    inventory_rows: dict[str, dict[str, str]],
    chronology_ids: list[str],
) -> dict[str, object]:
    pilot_full_changes = {
        change_id
        for row in scaffold_rows
        if (row.get("STATUS") or "").strip() in {"pilot", "full"}
        for change_id in row["change_ids"]
    }
    scaffold_changes = {
        change_id
        for row in scaffold_rows
        if (row.get("STATUS") or "").strip() == "scaffold"
        for change_id in row["change_ids"]
    }
    grouped_changes = {change_id for row in scaffold_rows if len(row["change_ids"]) > 1 for change_id in row["change_ids"]}
    needs_literature = {
        change_id for change_id, row in inventory_rows.items() if (row.get("literature_status") or "").strip() == "not_found"
    }
    negative_boundary_only = {
        change_id
        for change_id, row in inventory_rows.items()
        if (row.get("chronology_evidence_status") or "").strip() == "negative_boundary_only"
    }
    broad_far_contextual = {
        change_id
        for change_id, row in inventory_rows.items()
        if (row.get("chronology_evidence_status") or "").strip()
        in {"broad_far_constraint", "contextual_or_one_sided", "mixed"}
    }
    return {
        "total_changes": len(chronology_ids),
        "pilot_full_changes": len(pilot_full_changes),
        "scaffold_changes": len(scaffold_changes),
        "grouped_changes": len(grouped_changes),
        "multi_change_units": sum(1 for row in scaffold_rows if len(row["change_ids"]) > 1),
        "singleton_units": sum(1 for row in scaffold_rows if len(row["change_ids"]) == 1),
        "needs_literature": len(needs_literature),
        "needs_human_review": len(scaffold_changes),
        "negative_boundary_only": len(negative_boundary_only),
        "broad_far_contextual": len(broad_far_contextual),
        "all_represented": True,
    }


def build_unit_register(rows: list[dict[str, str]], id_key: str, treatment_heading: str = "Recommended treatment") -> str:
    header = [
        f"| Unit | Change IDs | Status | Chronology status | Literature status | {treatment_heading} |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    body = [
        "| "
        + " | ".join(
            [
                (row.get(id_key) or "").strip(),
                "; ".join(row["change_ids"]),
                (row.get("STATUS") or "").strip(),
                (row.get("CHRONOLOGY_STATUS") or "").strip(),
                (row.get("LITERATURE_STATUS") or "").strip(),
                (row.get("RECOMMENDED_TREATMENT") or "").strip(),
            ]
        )
        + " |"
        for row in rows
    ]
    return "\n".join(header + body)


def normalize_entry_markdown(title: str, text: str) -> str:
    stripped = text.lstrip()
    lines = stripped.splitlines()
    if lines and lines[0].startswith("# "):
        body = "\n".join(lines[1:]).lstrip()
        return f"## {title}\n\n{body}".rstrip()
    return f"## {title}\n\n{stripped}".rstrip()


def build_volume_text(
    manifest_rows: list[dict[str, str]],
    scaffold_rows: list[dict[str, str]],
    stats: dict[str, object],
) -> str:
    treatment_heading = "Final treatment" if stats["scaffold_changes"] == 0 else "Recommended treatment"
    if stats["scaffold_changes"] == 0:
        intro = (
            "_Generated from `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` and "
            "`Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`. "
            "All 70 ordinary sound changes now have pilot/full production prose in the assembled half._"
        )
    else:
        intro = (
            "_Generated from `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` and "
            "`Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`. "
            "Pilot/full rows preserve finished production prose where it exists; scaffold rows keep the rest of the "
            "70-change half visible and buildable without pretending that the prose is complete._"
        )
    parts: list[str] = [
        "# Sound-change half, alpha 01",
        "",
        intro,
        "",
        "## Coverage summary",
        "",
        f"- Ordinary chronology-card sound changes represented: {stats['total_changes']}/{stats['total_changes']}.",
        f"- Covered by pilot/full production reports: {stats['pilot_full_changes']}.",
        f"- Covered by scaffold placeholders: {stats['scaffold_changes']}.",
        f"- Grouped into multi-change units: {stats['grouped_changes']} changes across {stats['multi_change_units']} units.",
        f"- Still needing literature dossiers: {stats['needs_literature']}.",
        f"- Still needing human judgement or promotion decisions: {stats['needs_human_review']}.",
        f"- Negative/boundary-only chronology cards: {stats['negative_boundary_only']}.",
        f"- Broad/far/contextual chronology cards: {stats['broad_far_contextual']}.",
        "",
        "## Unit register",
        "",
        build_unit_register(scaffold_rows, "UNIT_ID", treatment_heading),
        "",
    ]

    assembled_manifest_rows = [row for row in manifest_rows if (row.get("STATUS") or "").strip() in ASSEMBLED_STATUSES]
    for row in assembled_manifest_rows:
        title = (row.get("TITLE") or "").strip()
        report_path = (row.get("REPORT_PATH") or "").strip()
        if not title:
            raise ValueError(f"Manifest row is missing TITLE: {row}")
        if not report_path:
            raise ValueError(f"Manifest row is missing REPORT_PATH: {row}")

        source_path = REPORTS_DIR / report_path
        if not source_path.exists():
            raise FileNotFoundError(f"Report file not found: {source_path}")

        entry_text = tidy_markdown_prose(source_path.read_text(encoding="utf-8"))
        parts.append(normalize_entry_markdown(title, entry_text))
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def build_coverage_report_text(scaffold_rows: list[dict[str, str]], stats: dict[str, object]) -> str:
    treatment_heading = "Final treatment" if stats["scaffold_changes"] == 0 else "Recommended treatment"
    if stats["scaffold_changes"] == 0:
        recommended_next_work = (
            "10. Recommended next work: final quality control of the assembled sound-change half."
        )
    else:
        recommended_next_work = (
            "10. Recommended next work: human review of the full scaffold structure, then choose the next cluster to "
            "promote from scaffold to production prose."
        )
    parts = [
        "# Sound-change half coverage report",
        "",
        "_Generated from `sound_change_half_scaffold.tsv`, `report_manifest.tsv`, and the chronology-card inventory._",
        "",
        f"1. Total ordinary sound changes covered: {stats['total_changes']}.",
        f"2. Number covered by pilot/full production reports: {stats['pilot_full_changes']}.",
        f"3. Number covered by scaffold placeholders: {stats['scaffold_changes']}.",
        f"4. Number grouped into multi-change units: {stats['grouped_changes']}.",
        f"5. Number needing literature dossiers: {stats['needs_literature']}.",
        f"6. Number needing human judgement: {stats['needs_human_review']}.",
        f"7. Number negative/boundary-only: {stats['negative_boundary_only']}.",
        f"8. Number broad/far/contextual: {stats['broad_far_contextual']}.",
        "9. Every ordinary `SC*.md` chronology card is represented somewhere in the assembled sound-change half: yes.",
        recommended_next_work,
        "",
        "## Unit register",
        "",
        build_unit_register(scaffold_rows, "UNIT_ID", treatment_heading),
        "",
    ]
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    manifest_rows = load_manifest_rows()
    scaffold_rows = load_scaffold_rows()
    inventory_rows = load_inventory_rows()
    chronology_ids = load_chronology_ids()
    validate_scaffold_coverage(scaffold_rows, chronology_ids, inventory_rows)
    validate_manifest_alignment(manifest_rows, scaffold_rows)
    stats = compute_coverage_stats(scaffold_rows, inventory_rows, chronology_ids)
    output_text = build_volume_text(manifest_rows, scaffold_rows, stats)
    coverage_text = build_coverage_report_text(scaffold_rows, stats)
    OUTPUT_PATH.write_text(output_text, encoding="utf-8")
    COVERAGE_REPORT_PATH.write_text(coverage_text, encoding="utf-8")
    assembled_count = sum(1 for row in manifest_rows if (row.get("STATUS") or "").strip() in ASSEMBLED_STATUSES)
    print(
        f"Wrote {OUTPUT_PATH} with {assembled_count} assembled sound-change unit(s), "
        f"and {COVERAGE_REPORT_PATH}."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise
