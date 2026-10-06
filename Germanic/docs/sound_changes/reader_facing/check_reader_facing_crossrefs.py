#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from reader_facing_check_utils import (
    READER_MANIFEST,
    build_all_source_rule_heading_map,
    build_rule_heading_map,
    iter_build_chapter_paths,
    line_number,
    mask_fenced_code,
    mask_spans,
    normalize_whitespace,
)


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "reader_facing_crossref_check_01.md"
LINK_RE = re.compile(r"\[([^\]]+)\]\((#rule-[^)]+)\)", re.S)
SYMBOLIC_RELATION_RE = re.compile(r"\bSC\d{3}\s*<\s*SC\d{3}\b")
FULL_REFERENCE_RE = re.compile(r"\b(SC\d{3})\s+([A-Z][A-Za-z0-9]+)\b")
INLINE_RULE_NAME_RE = re.compile(r"`((?:PGmc|PWGmc|NWGmc|OE)[A-Z][A-Za-z0-9]+)`")
RULE_HEADING_LINE_RE = re.compile(r"^##\s+SC\d{3}\.")


@dataclass
class CrossrefIssue:
    file_name: str
    line_number: int
    issue_type: str
    detail: str


@dataclass
class ScanCounts:
    chapter_files_checked: int = 0
    sound_change_links_checked: int = 0
    symbolic_relations_found: int = 0
    bare_sc_references_found: int = 0
    rule_name_only_references_found: int = 0
    broken_internal_anchors_found: int = 0
    unlinked_current_references_found: int = 0
    incomplete_internal_link_text_found: int = 0


def scan_file(
    path: Path,
    current_rule_map: dict[str, object],
    all_rule_map: dict[str, object],
    current_pairs: set[tuple[str, str]],
) -> tuple[list[CrossrefIssue], ScanCounts]:
    text = path.read_text(encoding="utf-8")
    masked = mask_fenced_code(text)
    issues: list[CrossrefIssue] = []
    counts = ScanCounts()
    counts.chapter_files_checked = 1

    link_spans: list[tuple[int, int]] = []
    for match in LINK_RE.finditer(masked):
        visible = normalize_whitespace(match.group(1))
        target = match.group(2)
        line = line_number(masked, match.start())
        counts.sound_change_links_checked += 1
        link_spans.append((match.start(), match.end()))

        heading = current_rule_map.get(target)
        if heading is None:
            future_heading = all_rule_map.get(target)
            if future_heading is None:
                counts.broken_internal_anchors_found += 1
                issues.append(
                    CrossrefIssue(
                        file_name=path.name,
                        line_number=line,
                        issue_type="broken-internal-anchor",
                        detail=f"{visible} -> {target}",
                    )
                )
            elif future_heading.sc_number not in visible or future_heading.rule_name not in visible:
                counts.incomplete_internal_link_text_found += 1
                issues.append(
                    CrossrefIssue(
                        file_name=path.name,
                        line_number=line,
                        issue_type="incomplete-future-link-text",
                        detail=f"{visible} -> {target}",
                    )
                )
            continue

        has_expected_sc = bool(re.search(rf"\b{re.escape(heading.sc_number)}\b", visible))
        has_expected_rule = heading.rule_name in visible
        if not has_expected_sc and has_expected_rule:
            counts.rule_name_only_references_found += 1
            issues.append(
                CrossrefIssue(
                    file_name=path.name,
                    line_number=line,
                    issue_type="rule-name-only-link",
                    detail=f"{visible} -> {target}",
                )
            )
        elif not has_expected_sc or not has_expected_rule:
            counts.incomplete_internal_link_text_found += 1
            issues.append(
                CrossrefIssue(
                    file_name=path.name,
                    line_number=line,
                    issue_type="incomplete-internal-link-text",
                    detail=f"{visible} -> {target}",
                )
            )

    working = mask_spans(masked, link_spans)

    relation_spans: list[tuple[int, int]] = []
    for match in SYMBOLIC_RELATION_RE.finditer(working):
        counts.symbolic_relations_found += 1
        relation_spans.append((match.start(), match.end()))
        issues.append(
            CrossrefIssue(
                file_name=path.name,
                line_number=line_number(working, match.start()),
                issue_type="symbolic-chronology-notation",
                detail=normalize_whitespace(match.group(0)),
            )
        )
    working = mask_spans(working, relation_spans)

    full_ref_spans: list[tuple[int, int]] = []
    for match in FULL_REFERENCE_RE.finditer(working):
        sc_number, rule_name = match.groups()
        full_ref_spans.append((match.start(), match.end()))
        if (sc_number, rule_name) in current_pairs:
            counts.unlinked_current_references_found += 1
            issues.append(
                CrossrefIssue(
                    file_name=path.name,
                    line_number=line_number(working, match.start()),
                    issue_type="unlinked-current-section-reference",
                    detail=f"{sc_number} {rule_name}",
                )
            )
    working = mask_spans(working, full_ref_spans)

    rule_name_spans: list[tuple[int, int]] = []
    original_lines = text.splitlines()
    for match in INLINE_RULE_NAME_RE.finditer(working):
        line = line_number(working, match.start())
        if RULE_HEADING_LINE_RE.match(original_lines[line - 1].strip()):
            continue
        counts.rule_name_only_references_found += 1
        rule_name_spans.append((match.start(), match.end()))
        issues.append(
            CrossrefIssue(
                file_name=path.name,
                line_number=line,
                issue_type="rule-name-only-reference",
                detail=f"`{match.group(1)}`",
            )
        )
    working = mask_spans(working, rule_name_spans)

    working_lines = working.splitlines()
    for idx, line in enumerate(working_lines, start=1):
        original_line = original_lines[idx - 1]
        if RULE_HEADING_LINE_RE.match(original_line.strip()):
            continue
        for match in re.finditer(r"\bSC\d{3}\b", line):
            counts.bare_sc_references_found += 1
            issues.append(
                CrossrefIssue(
                    file_name=path.name,
                    line_number=idx,
                    issue_type="bare-sc-reference",
                    detail=normalize_whitespace(original_line),
                )
            )

    return issues, counts


def render_report(
    issues: list[CrossrefIssue],
    totals: ScanCounts,
    manifest: Path,
    rule_count: int,
) -> str:
    lines = [
        "# Reader-facing cross-reference check 01",
        "",
        "_Generated from the generated reader manifest's chapter files and their SC-numbered rule headings._",
        "",
        "## Summary",
        "",
        f"- Reader manifest: `{manifest}`.",
        f"- Chapter files checked: {totals.chapter_files_checked}.",
        f"- Rule headings mapped from current chapter files: {rule_count}.",
        f"- Sound-change links checked: {totals.sound_change_links_checked}.",
        f"- Symbolic `<` relations found: {totals.symbolic_relations_found}.",
        f"- Bare SC references found: {totals.bare_sc_references_found}.",
        f"- Rule-name-only references found: {totals.rule_name_only_references_found}.",
        f"- Broken internal anchors found: {totals.broken_internal_anchors_found}.",
        f"- Unlinked current-section references found: {totals.unlinked_current_references_found}.",
        f"- Incomplete internal link text found: {totals.incomplete_internal_link_text_found}.",
        "",
        "| File | Line | Issue | Detail |",
        "| --- | --- | --- | --- |",
    ]
    if issues:
        for issue in issues:
            safe_detail = issue.detail.replace('|', '\\|')
            lines.append(
                f"| {issue.file_name} | {issue.line_number} | {issue.issue_type} | {safe_detail} |"
            )
    else:
        lines.append("| — | — | — | No cross-reference issues found. |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check reader-facing sound-change cross-references and chronology notation.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=READER_MANIFEST,
        help="Generated reader manifest whose rows define the current assembled reader-facing section.",
    )
    args = parser.parse_args()

    manifest = args.manifest.resolve()
    current_rule_map = build_rule_heading_map(manifest)
    all_rule_map = build_all_source_rule_heading_map()
    current_pairs = {(heading.sc_number, heading.rule_name) for heading in current_rule_map.values()}

    all_issues: list[CrossrefIssue] = []
    totals = ScanCounts()
    for path in iter_build_chapter_paths(manifest):
        issues, counts = scan_file(path, current_rule_map, all_rule_map, current_pairs)
        all_issues.extend(issues)
        totals.chapter_files_checked += counts.chapter_files_checked
        totals.sound_change_links_checked += counts.sound_change_links_checked
        totals.symbolic_relations_found += counts.symbolic_relations_found
        totals.bare_sc_references_found += counts.bare_sc_references_found
        totals.rule_name_only_references_found += counts.rule_name_only_references_found
        totals.broken_internal_anchors_found += counts.broken_internal_anchors_found
        totals.unlinked_current_references_found += counts.unlinked_current_references_found
        totals.incomplete_internal_link_text_found += counts.incomplete_internal_link_text_found

    OUTPUT_PATH.write_text(
        render_report(all_issues, totals, manifest, len(current_rule_map)),
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT_PATH}")
    print(
        "Files checked: "
        f"{totals.chapter_files_checked}; links: {totals.sound_change_links_checked}; "
        f"issues: {len(all_issues)}"
    )
    return 1 if all_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
