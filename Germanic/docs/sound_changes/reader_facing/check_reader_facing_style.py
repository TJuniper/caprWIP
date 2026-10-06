#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
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
    "reader_facing_chronology_evidence_check_01.md",
    "reader_facing_chronology_evidence_audit_01.md",
    "reader_facing_chronology_evidence_qc_01_report.md",
    "reader_facing_citation_check_01.md",
    "reader_facing_foma_width_check_01.md",
    "reader_facing_pdf_qc_02_report.md",
    "reader_facing_crossref_check_01.md",
    "reader_facing_crossref_qc_01_report.md",
    "reader_facing_generated_prose_check_01.md",
    "reader_facing_grouping_language_qc_01_report.md",
    "reader_facing_local_section_05_report.md",
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

NEGATION_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("negation:not only", re.compile(r"\bnot only\b", re.I)),
    ("negation:not merely", re.compile(r"\bnot merely\b", re.I)),
    ("negation:not just", re.compile(r"\bnot just\b", re.I)),
    ("negation:not-but", re.compile(r"\bnot\b[^.\n;:]{0,80}\bbut\b", re.I)),
    ("negation:rather than", re.compile(r"\brather than\b", re.I)),
    ("negation:instead of", re.compile(r"\binstead of\b", re.I)),
    ("negation:can and cannot", re.compile(r"\bcan—and cannot\b|\bcan and cannot\b", re.I)),
    ("negation:cannot-but", re.compile(r"\bcannot\b[^.\n;:]{0,80}\bbut\b", re.I)),
    ("negation:unlike", re.compile(r"\bunlike\b", re.I)),
    ("negation:by contrast", re.compile(r"\bby contrast\b", re.I)),
]

META_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("meta:reader-facing stance", re.compile(r"reader-facing stance", re.I)),
    ("meta:bridge", re.compile(r"\bbridge\b", re.I)),
    ("meta:chapter-sized", re.compile(r"chapter-sized", re.I)),
    ("meta:deserve section", re.compile(r"deserve(?:s|d)?[^.\n]{0,40}\bsection\b", re.I)),
    ("meta:this section should", re.compile(r"\bthis section should\b", re.I)),
    ("meta:this chapter should", re.compile(r"\bthis chapter should\b", re.I)),
    ("meta:the chapter should", re.compile(r"\bthe chapter should\b", re.I)),
    ("meta:the note should", re.compile(r"\bthe note should\b", re.I)),
    ("meta:this chapter is meant to", re.compile(r"\bthis chapter is meant to\b", re.I)),
    ("meta:keep visible", re.compile(r"\bkeeps?\b[^.\n]{0,40}\bvisible\b", re.I)),
    ("meta:larger chapter of its own", re.compile(r"larger chapter of (?:its|their) own", re.I)),
    ("meta:extension", re.compile(r"\bextension\b", re.I)),
    ("meta:local section", re.compile(r"\blocal section\b", re.I)),
    ("meta:build", re.compile(r"\bbuild(?: target| path| script| layer)?\b", re.I)),
    ("meta:project", re.compile(r"\bproject\b", re.I)),
    ("meta:workflow", re.compile(r"\bworkflow\b", re.I)),
    ("meta:source report", re.compile(r"\bsource report\b", re.I)),
    ("meta:manifest", re.compile(r"\bmanifest\b", re.I)),
    ("meta:development section", re.compile(r"Development of the discussion", re.I)),
    ("meta:remaining cautions", re.compile(r"Remaining cautions", re.I)),
    ("meta:pilot", re.compile(r"\bpilot\b", re.I)),
    ("meta:scaffold", re.compile(r"\bscaffold\b", re.I)),
    ("meta:chronology card", re.compile(r"chronology card", re.I)),
    ("meta:runner", re.compile(r"\brunner\b", re.I)),
    ("meta:left edge", re.compile(r"\bleft edge\b", re.I)),
    ("meta:right edge", re.compile(r"\bright edge\b", re.I)),
    ("meta:left-hand", re.compile(r"\bleft-hand\b", re.I)),
    ("meta:right-hand", re.compile(r"\bright-hand\b", re.I)),
    ("meta:leftward", re.compile(r"\bleftward\b", re.I)),
    ("meta:rightward", re.compile(r"\brightward\b", re.I)),
    ("meta:far right", re.compile(r"\bfar right\b", re.I)),
    ("meta:far left", re.compile(r"\bfar left\b", re.I)),
    ("meta:chapter center", re.compile(r"\bchapter center\b", re.I)),
    ("meta:cleanup", re.compile(r"\bcleanup(?: rule)?\b", re.I)),
    ("meta:corridor", re.compile(r"\bcorridor\b", re.I)),
    ("meta:file path", re.compile(r"Germanic/docs/")),
]

OE_CODE_SPAN_RE = re.compile(
    r"`(ceaster|geaf|giefan|giest|cild|dæg|weccan|licgan|lecgan|secg|ecg|wicg|brycg|streċċan|strecċan|cȳ|lungen|gylden|wyrm|hierde|ieldra|bryd|trymman|bedd|ciest|wiersa|gieldan|scield|scieppan|sceap|ġift|ġieft|sċēaþ|sċǣþ|heofon|fæstenn|enetre)`",
    re.I,
)
GLOSS_BACKTICK_RE = re.compile(r"`[A-Za-z][A-Za-z -]*'")
ITALIC_ENGLISH_RE = re.compile(r"_(stretch|cow|lung|gift|sheath|yearling)_", re.I)
RECONSTRUCTION_MARKDOWN_RE = re.compile(r"\*\\\*")
RECONSTRUCTION_HTML_RE = re.compile(r"<(?:em|i)>\*")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
SAFE_LATEX_RE = re.compile(r"\\emph\{[^}]*\}")
BARE_STAR_TOKEN_RE = re.compile(r"\*[-\wþðæǣȳċġƿȝʃʒʧʤβ]+(?:\*)?", re.UNICODE)


def is_ignorable_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith(("```", "#", ">", "|", "- ", "* ")):
        return True
    if re.match(r"\d+\.\s", stripped):
        return True
    return False


def colon_list_match(line: str) -> bool:
    stripped = line.strip()
    if is_ignorable_line(stripped):
        return False
    if "http://" in stripped or "https://" in stripped:
        return False
    return bool(re.search(r":[^.\n]{0,160},[^.\n]{0,160},", stripped))


def iter_target_files(include_all: bool) -> list[Path]:
    files = sorted(ROOT.glob("*.md"))
    if include_all:
        return files
    return [
        path for path in files
        if path.name not in DEFAULT_SKIP
        # Chapter introduction files are not individual sound-change sections;
        # skip them from the sound-change style checks.
        and not path.name.startswith("chap") and not path.name.endswith("-intro.md")
    ]


def bare_star_matches(line: str) -> list[str]:
    masked = INLINE_CODE_RE.sub("", line)
    masked = SAFE_LATEX_RE.sub("", masked)
    masked = masked.replace(r"\*", "")
    matches: list[str] = []
    for match in BARE_STAR_TOKEN_RE.finditer(masked):
        token = match.group(0)
        if token.endswith("*"):
            inner = token[1:-1]
            if inner and re.fullmatch(r"[\wþðæǣȳċġƿȝʃʒʧʤβ]+", inner, re.UNICODE):
                continue
        matches.append(token)
    return matches


def define_warnings(path: Path) -> list[tuple[Path, int, str, str]]:
    warnings: list[tuple[Path, int, str, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    inside_foma = False
    block_start = 0
    define_count = 0
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```foma"):
            inside_foma = True
            block_start = idx
            define_count = 0
            continue
        if inside_foma and stripped.startswith("```"):
            if define_count > 1:
                warnings.append((path, block_start, "foma:multiple-define", f"{define_count} define statements in one foma block"))
            inside_foma = False
            continue
        if inside_foma and re.match(r"define\s+\w+", stripped):
            define_count += 1
    return warnings


def grouped_history_warnings(path: Path) -> list[tuple[Path, int, str, str]]:
    warnings: list[tuple[Path, int, str, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    unique_sc_numbers = {
        match.group(1)
        for line in lines
        if (match := re.match(r"##\s+SC(\d{3})\.\s", line.strip()))
    }
    if len(unique_sc_numbers) <= 1:
        return warnings
    generic_lines = [idx for idx, line in enumerate(lines, start=1) if line.strip() == "## Historical discussion"]
    explicit_lines = [
        idx
        for idx, line in enumerate(lines, start=1)
        if re.match(r"## Historical discussion of .+", line.strip())
    ]
    if len(generic_lines) == 1 and not explicit_lines:
        warnings.append(
            (
                path,
                generic_lines[0],
                "grouped:single-generic-historical-discussion",
                lines[generic_lines[0] - 1],
            )
        )
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check reader-facing sound-change prose for style and formatting patterns.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if warnings are found.")
    parser.add_argument("--all", action="store_true", help="Scan all Markdown files in the directory, including notes and generated pilot Markdown.")
    args = parser.parse_args()

    warnings: list[tuple[Path, int, str, str]] = []

    for path in iter_target_files(args.all):
        warnings.extend(define_warnings(path))
        warnings.extend(grouped_history_warnings(path))
        inside_fence = False
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("```"):
                inside_fence = not inside_fence
                continue
            if inside_fence:
                continue
            if "—" in line and not is_ignorable_line(line):
                warnings.append((path, line_number, "emdash", line.rstrip()))
            if stripped.startswith("## "):
                if re.match(r"## Historical discussion(?: of .+)?$", stripped):
                    pass
                elif not re.match(r"## SC\d{3}\.\s", stripped):
                    warnings.append((path, line_number, "heading:missing-sc-number", line.rstrip()))
            if colon_list_match(line):
                warnings.append((path, line_number, "colon-list", line.rstrip()))
            if GLOSS_BACKTICK_RE.search(line):
                warnings.append((path, line_number, "gloss:backtick-quote", line.rstrip()))
            if ITALIC_ENGLISH_RE.search(line):
                warnings.append((path, line_number, "gloss:italic-english", line.rstrip()))
            if RECONSTRUCTION_MARKDOWN_RE.search(line):
                warnings.append((path, line_number, "reconstruction:markdown-asterisk", line.rstrip()))
            if RECONSTRUCTION_HTML_RE.search(line):
                warnings.append((path, line_number, "reconstruction:html-emphasis", line.rstrip()))
            if bare_star_matches(line):
                warnings.append((path, line_number, "reconstruction:bare-star-form", line.rstrip()))
            if not is_ignorable_line(line) and OE_CODE_SPAN_RE.search(line):
                warnings.append((path, line_number, "oe-form:code-span", line.rstrip()))
            for label, pattern in NEGATION_PATTERNS:
                if pattern.search(line):
                    if label in {"negation:rather than", "negation:instead of"} and ("expected" in line or "yields" in line or "produces" in line):
                        continue
                    warnings.append((path, line_number, label, line.rstrip()))
            for label, pattern in META_PATTERNS:
                if pattern.search(line):
                    if label == "meta:bridge" and re.search(r"[‘']bridge[’']", line):
                        continue
                    warnings.append((path, line_number, label, line.rstrip()))

    if warnings:
        for path, line_number, label, line in warnings:
            print(f"{path}:{line_number}:{label}:{line}")
        return 1 if args.strict else 0

    print("No reader-facing style warnings found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
