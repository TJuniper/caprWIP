#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "reader_facing_citation_check_01.md"
WHITELIST_PATH = ROOT / "reader_facing_citation_whitelist.tsv"
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
    "reader_facing_chronology_evidence_check_01.md",
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

CITATION_BLOCK_RE = re.compile(r"\[@([^\]]+)\]", re.S)
PAGE_RE = re.compile(r"\bpp?\.\s*\d", re.I)
KEY_RE = re.compile(r"@([A-Za-z0-9_.:-]+)")


@dataclass
class CitationIssue:
    file_name: str
    line_number: int
    key: str
    citation_text: str
    reason: str


def iter_target_files() -> list[Path]:
    return [path for path in sorted(ROOT.glob("*.md")) if path.name not in DEFAULT_SKIP]


def load_whitelist() -> set[tuple[str, str, int]]:
    if not WHITELIST_PATH.exists():
        return set()
    with WHITELIST_PATH.open(encoding="utf-8") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        return {
            ((row.get("key") or "").strip(), (row.get("file_name") or "").strip(), int((row.get("line_number") or "0").strip()))
            for row in rows
            if (row.get("key") or "").strip() and (row.get("file_name") or "").strip() and (row.get("line_number") or "").strip()
        }


def split_citations(block: str) -> list[str]:
    return [part.strip() for part in block.split(";") if part.strip()]


def scan_file(path: Path, whitelist: set[tuple[str, str, int]]) -> list[CitationIssue]:
    text = path.read_text(encoding="utf-8")
    issues: list[CitationIssue] = []
    for match in CITATION_BLOCK_RE.finditer(text):
        block = match.group(1)
        line_number = text.count("\n", 0, match.start()) + 1
        for citation in split_citations(block):
            key_match = KEY_RE.search(citation)
            if not key_match:
                continue
            key = key_match.group(1)
            if PAGE_RE.search(citation):
                continue
            if (key, path.name, line_number) in whitelist:
                continue
            issues.append(
                CitationIssue(
                    file_name=path.name,
                    line_number=line_number,
                    key=key,
                    citation_text=citation.replace("\n", " "),
                    reason="missing page number and not whitelisted",
                )
            )
    return issues


def render(issues: list[CitationIssue], checked_files: list[Path]) -> str:
    lines = [
        "# Reader-facing citation check 01",
        "",
        "_Generated from the current reader-facing chapter files and `reader_facing_citation_whitelist.tsv`._",
        "",
        "## Summary",
        "",
        f"- Files checked: {len(checked_files)}.",
        f"- Citation issues: {len(issues)}.",
        "",
        "| File | Line | Key | Citation | Issue |",
        "| --- | --- | --- | --- | --- |",
    ]
    for issue in issues:
        lines.append(
            f"| {issue.file_name} | {issue.line_number} | `{issue.key}` | `{issue.citation_text}` | {issue.reason} |"
        )
    if not issues:
        lines.append("| — | — | — | — | No citation issues found. |")
    return "\n".join(lines) + "\n"


def main() -> int:
    files = iter_target_files()
    whitelist = load_whitelist()
    issues: list[CitationIssue] = []
    for path in files:
        issues.extend(scan_file(path, whitelist))

    OUTPUT_PATH.write_text(render(issues, files), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Files checked: {len(files)}; citation issues: {len(issues)}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
