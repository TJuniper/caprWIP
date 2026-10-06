#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MARKDOWN_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_20.md"
LONG_HEADING_THRESHOLD = 65
TARGET_RULE_NAME = "PNWGmcStressedMonosyllableORaising"
TARGET_ANCHOR = "rule-PNWGmcStressedMonosyllableORaising"

LEGACY_HEADING_RE = re.compile(
    r"^(#{2,3})\s+(SC\d{3})\.\s+(.*?)\s+\(`([^`]+)`\)\s+\{#(rule-[^}]+)\}\s*$"
)
WRAPPED_HEADING_RE = re.compile(
    r"^(#{2,3})\s+\\CAPRRuleHeading\{(SC\d{3})\.\s+(.+)\}\{([^{}]+)\}\s+\{#(rule-[^}]+)\}\s*$"
)


@dataclass(frozen=True)
class RuleHeading:
    line_no: int
    level: int
    sc_number: str
    title: str
    rule_name: str
    anchor: str
    wrapped: bool
    raw: str


def normalize_title_for_length(title: str) -> str:
    normalized = title
    prev = None
    while prev != normalized:
        prev = normalized
        normalized = re.sub(r"\\[A-Za-z]+\{([^{}]*)\}", r"\1", normalized)
    normalized = normalized.replace("{", "").replace("}", "")
    normalized = normalized.replace("`", "")
    normalized = re.sub(r"\\[A-Za-z]+", "", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def visible_heading_length(heading: RuleHeading) -> int:
    title = normalize_title_for_length(heading.title)
    return len(f"{heading.sc_number}. {title} ({heading.rule_name})")


def parse_headings(markdown_path: Path) -> list[RuleHeading]:
    headings: list[RuleHeading] = []
    for idx, raw_line in enumerate(markdown_path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.strip()
        wrapped_match = WRAPPED_HEADING_RE.match(line)
        if wrapped_match:
            hashes, sc_number, title, rule_name, anchor = wrapped_match.groups()
            headings.append(
                RuleHeading(
                    line_no=idx,
                    level=len(hashes),
                    sc_number=sc_number,
                    title=title,
                    rule_name=rule_name,
                    anchor=anchor,
                    wrapped=True,
                    raw=raw_line,
                )
            )
            continue
        legacy_match = LEGACY_HEADING_RE.match(line)
        if legacy_match:
            hashes, sc_number, title, rule_name, anchor = legacy_match.groups()
            headings.append(
                RuleHeading(
                    line_no=idx,
                    level=len(hashes),
                    sc_number=sc_number,
                    title=title,
                    rule_name=rule_name,
                    anchor=anchor,
                    wrapped=False,
                    raw=raw_line,
                )
            )
    if not headings:
        raise AssertionError(f"No SC rule headings found in {markdown_path}")
    return headings


def check_markdown(markdown_path: Path) -> list[RuleHeading]:
    headings = parse_headings(markdown_path)
    anchor_counts: dict[str, int] = {}
    for heading in headings:
        anchor_counts[heading.anchor] = anchor_counts.get(heading.anchor, 0) + 1
    duplicate_anchors = sorted(anchor for anchor, count in anchor_counts.items() if count > 1)
    if duplicate_anchors:
        raise AssertionError(f"Duplicate rule anchors found: {', '.join(duplicate_anchors)}")

    long_unwrapped = [
        heading
        for heading in headings
        if visible_heading_length(heading) > LONG_HEADING_THRESHOLD and not heading.wrapped
    ]
    if long_unwrapped:
        details = ", ".join(
            f"{heading.sc_number}/{heading.rule_name} (line {heading.line_no}, len {visible_heading_length(heading)})"
            for heading in long_unwrapped
        )
        raise AssertionError(f"Long SC headings are not wrapped: {details}")

    target = [heading for heading in headings if heading.anchor == TARGET_ANCHOR]
    if len(target) != 1:
        raise AssertionError(f"Expected exactly one {TARGET_ANCHOR} heading; found {len(target)}")
    target_heading = target[0]
    if not target_heading.wrapped:
        raise AssertionError("SC018 heading is not routed through \\CAPRRuleHeading.")
    if target_heading.rule_name != TARGET_RULE_NAME:
        raise AssertionError(
            f"SC018 heading rule mismatch: expected {TARGET_RULE_NAME}, found {target_heading.rule_name}"
        )
    if TARGET_RULE_NAME not in target_heading.raw:
        raise AssertionError("SC018 heading no longer contains the plain implementation label.")

    return headings


def check_tex(tex_path: Path, wrapped_headings: list[RuleHeading]) -> None:
    tex_text = tex_path.read_text(encoding="utf-8")
    for heading in wrapped_headings:
        if visible_heading_length(heading) <= LONG_HEADING_THRESHOLD:
            continue
        macro_marker = rf"\CAPRRuleHeading{{{heading.sc_number}."
        if macro_marker not in tex_text:
            raise AssertionError(
                f"TeX is missing wrapped heading macro for {heading.sc_number} (expected marker: {macro_marker})"
            )
        rule_marker = "{" + heading.rule_name + "}"
        if rule_marker not in tex_text:
            raise AssertionError(f"TeX is missing implementation label for {heading.rule_name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--markdown-path", type=Path, default=DEFAULT_MARKDOWN_PATH)
    parser.add_argument("--tex-path", type=Path, default=None)
    args = parser.parse_args()

    markdown_path = args.markdown_path.expanduser().resolve()
    if not markdown_path.exists():
        raise AssertionError(f"Markdown file not found: {markdown_path}")

    headings = check_markdown(markdown_path)
    wrapped = [heading for heading in headings if heading.wrapped]

    if args.tex_path is not None:
        tex_path = args.tex_path.expanduser().resolve()
        if not tex_path.exists():
            raise AssertionError(f"TeX file not found: {tex_path}")
        check_tex(tex_path, wrapped)

    long_count = sum(1 for heading in headings if visible_heading_length(heading) > LONG_HEADING_THRESHOLD)
    wrapped_long_count = sum(
        1
        for heading in headings
        if visible_heading_length(heading) > LONG_HEADING_THRESHOLD and heading.wrapped
    )
    print(
        "sound-change heading wrapping checks passed "
        f"(headings: {len(headings)}, long: {long_count}, wrapped long: {wrapped_long_count})"
    )


if __name__ == "__main__":
    main()
