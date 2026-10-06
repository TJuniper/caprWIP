#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from reader_facing_check_utils import normalize_whitespace


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "reader_facing_chronology_evidence_check_01.md"
DEFAULT_SKIP = {
    "README.md",
    "style_guide.md",
    "source_note.md",
    "source_note_pilot_02.md",
    "ai_style_audit_checklist.md",
    "reader_facing_pilot_01.md",
    "reader_facing_pilot_02.md",
    "reader_facing_pilot_02_report.md",
    "reader_facing_local_section_01.md",
    "reader_facing_local_section_01_report.md",
    "reader_facing_local_section_02.md",
    "reader_facing_local_section_02_report.md",
    "reader_facing_local_section_03.md",
    "reader_facing_local_section_03_report.md",
    "reader_facing_local_section_04.md",
    "reader_facing_local_section_04_report.md",
    "reader_facing_local_section_05.md",
    "reader_facing_local_section_05_report.md",
    "reader_facing_local_section_06.md",
    "reader_facing_local_section_06_report.md",
    "reader_facing_local_section_07.md",
    "reader_facing_local_section_07_report.md",
    "reader_facing_local_section_08.md",
    "reader_facing_local_section_08_report.md",
    "reader_facing_local_section_09.md",
    "reader_facing_local_section_09_report.md",
    "reader_facing_local_section_10.md",
    "reader_facing_local_section_10_report.md",
    "reader_facing_local_section_11.md",
    "reader_facing_local_section_11_report.md",
    "reader_facing_local_section_12.md",
    "reader_facing_local_section_12_report.md",
    "reader_facing_local_section_13.md",
    "reader_facing_local_section_13_report.md",
    "reader_facing_local_section_14.md",
    "reader_facing_local_section_14_report.md",
    "reader_facing_manifest_coverage_01.md",
    "reader_facing_local_section_15.md",
    "reader_facing_local_section_15_report.md",
    "reader_facing_manifest_coverage_03.md",
    "reader_facing_local_section_16.md",
    "reader_facing_local_section_16_report.md",
    "reader_facing_manifest_coverage_04.md",
    "reader_facing_local_section_17.md",
    "reader_facing_local_section_17_report.md",
    "reader_facing_manifest_coverage_05.md",
    "reader_facing_local_section_18.md",
    "reader_facing_local_section_18_report.md",
    "reader_facing_manifest_coverage_06.md",
    "reader_facing_remaining_gap_audit_01.md",
    "reader_facing_local_section_19.md",
    "reader_facing_manifest_coverage_07.md",
    "reader_facing_local_section_20.md",
    "reader_facing_manifest_coverage_08.md",
    "reader_facing_sc005_009_012_inclusion_01_report.md",
    "reader_facing_source_based_chronology_rationales_01.md",
    "reader_facing_chronology_rationale_grounding_01.md",
    "reader_facing_broad_window_chronology_review_01.md",
    "reader_facing_one_direction_chronology_review_01.md",
    "reader_facing_chronology_confidence_audit_01.md",
    "reader_facing_local_section_19_editorial_review_01.md",
    "reader_facing_chronology_evidence_audit_01.md",
    "reader_facing_chronology_evidence_qc_01_report.md",
    "reader_facing_citation_check_01.md",
    "reader_facing_foma_width_check_01.md",
    "reader_facing_pdf_qc_02_report.md",
    "reader_facing_crossref_check_01.md",
    "reader_facing_crossref_qc_01_report.md",
    "reader_facing_generated_prose_check_01.md",
    "reader_facing_grouping_language_qc_01_report.md",
    "reader_facing_local_section_06_report.md",
    "reader_facing_local_section_07_report.md",
    "reader_facing_local_section_08_report.md",
    "reader_facing_local_section_09_report.md",
    "reader_facing_local_section_10_report.md",
    "reader_facing_local_section_11_report.md",
    "reader_facing_local_section_12_report.md",
    "reader_facing_local_section_13_report.md",
    "reader_facing_local_section_14_report.md",
    "reader_facing_manifest_coverage_01.md",
    "reader_facing_local_section_15_report.md",
    "reader_facing_manifest_coverage_03.md",
    "reader_facing_local_section_16_report.md",
    "reader_facing_manifest_coverage_04.md",
    "reader_facing_local_section_17_report.md",
    "reader_facing_manifest_coverage_05.md",
}

RULE_HEADING_RE = re.compile(r"^##\s+(SC\d{3}\.[^\n]+)$", re.M)
CODE_BLOCK_RE = re.compile(r"(?ms)^```.*?^```[ \t]*\n?")
SYMBOLIC_RELATION_RE = re.compile(r"SC\d{3}\s*<\s*SC\d{3}")
SC_RULE_REF_RE = re.compile(r"SC\d{3}\s+[A-Z][A-Za-z0-9]+")

MOVE_PATTERNS = [
    re.compile(r"if [^.]*moved", re.I),
    re.compile(r"when [^.]*moved", re.I),
    re.compile(r"if [^.]*delayed", re.I),
    re.compile(r"if [^.]*applied", re.I),
    re.compile(r"\bmoving\b[^.]{0,240}\b(?:before|after|earlier|later)\b", re.I),
    re.compile(r"\bdelaying\b[^.]{0,240}\b(?:until|past|before|after)\b", re.I),
    re.compile(r"\bwith\b[^.]{0,160}\b(?:before|after)\b", re.I),
]
BOUNDARY_PATTERNS = [
    re.compile(r"must\s+(?:\w+\s+){0,4}come\s+before", re.I),
    re.compile(r"comes\s+before", re.I),
    re.compile(r"must\s+apply\s+before", re.I),
    re.compile(r"places?[\s\S]{0,160}\bbefore\b", re.I),
    re.compile(r"must\s+follow", re.I),
    re.compile(r"must\s+(?:\w+\s+){0,4}come\s+after", re.I),
    re.compile(r"comes\s+after", re.I),
    re.compile(r"must\s+apply\s+after", re.I),
    re.compile(r"places?[\s\S]{0,160}\bafter\b", re.I),
    re.compile(r"\brequires?[\s\S]{0,240}\bto\s+(?:precede|follow)\b", re.I),
    re.compile(r"\btake[\s\S]{0,240}\bto\s+(?:precede|follow)\b", re.I),
    re.compile(r"\brequires?[\s\S]{0,160}\b(?:before|after)\b", re.I),
    re.compile(r"\bmust\b[^.]{0,160}\b(?:before|after)\b", re.I),
    re.compile(r"\bSC\d{3}\b[^.]{0,120}\b(?:precedes|follows)\b", re.I),
    # Accept natural scholarly formulations indicating relative order
    re.compile(r"\bprecede(?:d|s)?\b", re.I),
    re.compile(r"\bfollow(?:ed|s)?\b", re.I),
]
OUTPUT_PATTERNS = [
    re.compile(r"\byields?\b", re.I),
    re.compile(r"\bproduces?\b", re.I),
    re.compile(r"\bno output\b", re.I),
]
LIMITATION_PATTERNS = [
    re.compile(r"no exact wrong", re.I),
    re.compile(r"no single .* wrong form", re.I),
    re.compile(r"no comparably sharp", re.I),
    re.compile(r"no explicit .* boundary", re.I),
    re.compile(r"no positive .* boundary", re.I),
    re.compile(r"boundary-limited", re.I),
    re.compile(r"one-sided", re.I),
    re.compile(r"no decisive wrong form", re.I),
    # natural formulations indicating lack of ordering or neutral results
    re.compile(r"leav(?:es|e)\s+[\s\S]{0,120}\sunchanged", re.I),
    re.compile(r"remains?\s+unchanged", re.I),
    re.compile(r"does not determine", re.I),
    re.compile(r"does not establish", re.I),
    re.compile(r"no\s+ordering(\s|$)", re.I),
]


@dataclass
class SectionCheck:
    file_name: str
    heading: str
    has_move: bool
    has_expected: bool
    has_output: bool
    has_sc_rule_ref: bool
    has_boundary: bool
    has_limitation: bool
    has_symbolic_relation: bool
    warnings: list[str]


def iter_target_files() -> list[Path]:
    return [path for path in sorted(ROOT.glob("*.md")) if path.name not in DEFAULT_SKIP]


def split_sections(text: str) -> list[tuple[str, str]]:
    matches = list(RULE_HEADING_RE.finditer(text))
    sections: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end]
        sections.append((heading, body))
    return sections


def strip_code(text: str) -> str:
    return CODE_BLOCK_RE.sub("", text)


def check_section(file_name: str, heading: str, body: str) -> SectionCheck:
    prose = strip_code(body)
    has_move = any(pattern.search(prose) for pattern in MOVE_PATTERNS)
    has_expected = "expected" in prose.lower()
    has_output = any(pattern.search(prose) for pattern in OUTPUT_PATTERNS)
    has_sc_rule_ref = bool(SC_RULE_REF_RE.search(prose))
    has_boundary = any(pattern.search(prose) for pattern in BOUNDARY_PATTERNS)
    has_limitation = any(pattern.search(prose) for pattern in LIMITATION_PATTERNS)
    has_symbolic_relation = bool(SYMBOLIC_RELATION_RE.search(prose))

    warnings: list[str] = []
    if has_symbolic_relation:
        warnings.append("symbolic chronology notation found")
    if not has_move:
        warnings.append("missing move-condition wording")
    if not has_output and not has_limitation:
        warnings.append("missing explicit wrong-output/result wording")
    if not has_expected and not has_limitation:
        warnings.append("missing expected-form wording")
    if not has_boundary and not has_limitation:
        warnings.append("missing explicit verbal boundary conclusion")
    if has_boundary and not has_sc_rule_ref and not has_limitation:
        warnings.append("missing SC-plus-rule reference in chronology prose")

    return SectionCheck(
        file_name=file_name,
        heading=heading,
        has_move=has_move,
        has_expected=has_expected,
        has_output=has_output,
        has_sc_rule_ref=has_sc_rule_ref,
        has_boundary=has_boundary,
        has_limitation=has_limitation,
        has_symbolic_relation=has_symbolic_relation,
        warnings=warnings,
    )


def render_report(results: list[SectionCheck]) -> str:
    warning_count = sum(1 for result in results if result.warnings)
    lines = [
        "# Reader-facing chronology evidence check 01",
        "",
        "_Generated from the current SC-numbered rule sections in the reader-facing chapter files._",
        "",
        "## Summary",
        "",
        f"- Sections checked: {len(results)}.",
        f"- Sections with warnings: {warning_count}.",
        "",
        "| File | Rule section | Move wording | Expected form | Wrong output/result | SC-plus-rule ref | Verbal boundary wording | Limitation wording | Symbolic `<` notation | Warnings |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for result in results:
        lines.append(
            "| "
            + " | ".join(
                [
                    result.file_name,
                    result.heading,
                    "yes" if result.has_move else "no",
                    "yes" if result.has_expected else "no",
                    "yes" if result.has_output else "no",
                    "yes" if result.has_sc_rule_ref else "no",
                    "yes" if result.has_boundary else "no",
                    "yes" if result.has_limitation else "no",
                    "yes" if result.has_symbolic_relation else "no",
                    normalize_whitespace("; ".join(result.warnings)) if result.warnings else "—",
                ]
            )
            + " |"
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    results: list[SectionCheck] = []
    for path in iter_target_files():
        text = path.read_text(encoding="utf-8")
        for heading, body in split_sections(text):
            results.append(check_section(path.name, heading, body))

    OUTPUT_PATH.write_text(render_report(results), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    warning_count = sum(1 for result in results if result.warnings)
    print(f"Sections checked: {len(results)}; warnings: {warning_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
