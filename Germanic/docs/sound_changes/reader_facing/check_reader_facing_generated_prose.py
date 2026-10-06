#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from reader_facing_check_utils import BUILD_READER_BOOK, parse_intro_parts


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "reader_facing_generated_prose_check_01.md"
DISALLOWED_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("extension", re.compile(r"\bextension\b", re.I)),
    ("rollout", re.compile(r"\brollout\b", re.I)),
    ("inserted", re.compile(r"\binsert(?:ed|s|ing)?\b", re.I)),
    ("batch", re.compile(r"\bbatch\b", re.I)),
    ("current section", re.compile(r"\bcurrent section\b", re.I)),
    ("local-section", re.compile(r"\blocal[- ]section\b", re.I)),
    ("reader-facing", re.compile(r"\breader-facing\b", re.I)),
    ("workflow", re.compile(r"\bworkflow\b", re.I)),
    ("project", re.compile(r"\bproject\b", re.I)),
    ("build target", re.compile(r"\bbuild target\b", re.I)),
    ("generated", re.compile(r"\bgenerated\b", re.I)),
    ("pilot", re.compile(r"\bpilot\b", re.I)),
    ("scaffold", re.compile(r"\bscaffold\b", re.I)),
    ("manifest", re.compile(r"\bmanifest\b", re.I)),
    ("no new earlier material", re.compile(r"\bno new earlier material\b", re.I)),
    ("attempted here", re.compile(r"\battempted here\b", re.I)),
]


@dataclass
class GeneratedProseIssue:
    paragraph_number: int
    label: str
    paragraph: str


def scan_intro(builder: Path) -> tuple[list[str], list[GeneratedProseIssue]]:
    paragraphs = parse_intro_parts(builder)
    issues: list[GeneratedProseIssue] = []
    for idx, paragraph in enumerate(paragraphs, start=1):
        for label, pattern in DISALLOWED_PATTERNS:
            if pattern.search(paragraph):
                issues.append(
                    GeneratedProseIssue(
                        paragraph_number=idx,
                        label=label,
                        paragraph=paragraph,
                    )
                )
    return paragraphs, issues


def render(builder: Path, paragraphs: list[str], issues: list[GeneratedProseIssue]) -> str:
    lines = [
        "# Reader-facing generated prose check 01",
        "",
        "_Generated from the introduction prose owned by the reader-facing book builder._",
        "",
        "## Summary",
        "",
        f"- Book builder: `{builder}`.",
        f"- Introduction paragraphs checked: {len(paragraphs)}.",
        f"- Issues found: {len(issues)}.",
        "",
        "## Introduction paragraphs",
        "",
    ]
    for idx, paragraph in enumerate(paragraphs, start=1):
        lines.append(f"{idx}. {paragraph}")
    lines.extend(["", "## Issues", "", "| Paragraph | Issue | Text |", "| --- | --- | --- |"])
    if issues:
        for issue in issues:
            safe_par = issue.paragraph.replace('|', '\\|')
            lines.append(
                f"| {issue.paragraph_number} | {issue.label} | {safe_par} |"
            )
    else:
        lines.append("| — | — | No generated-prose issues found. |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check generated reader-facing introduction prose for project-facing language.")
    parser.add_argument(
        "--builder",
        type=Path,
        default=BUILD_READER_BOOK,
        help="Book builder module whose front-matter prose should be checked.",
    )
    args = parser.parse_args()

    builder = args.builder.resolve()
    paragraphs, issues = scan_intro(builder)
    OUTPUT_PATH.write_text(render(builder, paragraphs, issues), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Paragraphs checked: {len(paragraphs)}; issues: {len(issues)}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
