#!/usr/bin/env python3
from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SC_DIR = ROOT.parent
READER_MANIFEST = SC_DIR / "registry" / "reader_manifest.tsv"
BUILD_READER_BOOK = ROOT.parents[3] / "Germanic/tools/build_reader_book.py"
RULE_HEADING_RE = re.compile(
    r"^##\s+(SC\d{3})\.\s+(.*?)\s+\(`([^`]+)`\)\s+\{#(rule-[^}]+)\}\s*$"
)
CODE_FENCE_RE = re.compile(r"(?ms)^```.*?^```[ \t]*\n?")


@dataclass(frozen=True)
class RuleHeading:
    file_name: str
    sc_number: str
    title: str
    rule_name: str
    anchor: str


def iter_chapter_source_paths() -> list[Path]:
    return sorted(ROOT.glob("[0-9]*.md"))


def manifest_chapter_files(manifest: Path = READER_MANIFEST) -> list[str]:
    """Reader files in presentation order, from the generated book manifest."""
    lines = [ln for ln in manifest.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    import csv
    rows = list(csv.DictReader(lines, delimiter="\t"))
    if not rows:
        raise ValueError(f"No rows found in {manifest}")
    return [row["reader_file"] for row in rows]


def parse_python_list_assignment(module_path: Path, name: str) -> list[str]:
    module = ast.parse(module_path.read_text(encoding="utf-8"))
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return list(ast.literal_eval(node.value))
        if isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name and node.value is not None:
                return list(ast.literal_eval(node.value))
    raise ValueError(f"Could not find {name} list assignment in {module_path}")


def parse_intro_parts(builder: Path = BUILD_READER_BOOK) -> list[str]:
    parts = parse_python_list_assignment(builder, "parts_front")
    # Support both legacy "## Introduction" and current "## Scope and orientation" markers
    marker = None
    for candidate in ("## Scope and orientation", "## Introduction"):
        if candidate in parts:
            marker = candidate
            break
    if marker is None:
        raise ValueError(f"Could not find ## Introduction or ## Scope and orientation marker in {builder}")
    start = parts.index(marker) + 1
    return [part for part in parts[start:] if part.strip() and not part.startswith("#")]


def iter_build_chapter_paths(manifest: Path = READER_MANIFEST) -> list[Path]:
    return [ROOT / name for name in manifest_chapter_files(manifest)]


def extract_rule_headings(path: Path) -> list[RuleHeading]:
    headings: list[RuleHeading] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = RULE_HEADING_RE.match(line.strip())
        if match:
            headings.append(
                RuleHeading(
                    file_name=path.name,
                    sc_number=match.group(1),
                    title=match.group(2),
                    rule_name=match.group(3),
                    anchor=f"#{match.group(4)}",
                )
            )
    if not headings:
        raise ValueError(f"No SC-numbered rule headings found in {path}")
    return headings


def build_rule_heading_map(manifest: Path = READER_MANIFEST) -> dict[str, RuleHeading]:
    mapping: dict[str, RuleHeading] = {}
    for path in iter_build_chapter_paths(manifest):
        for heading in extract_rule_headings(path):
            if heading.anchor in mapping:
                raise ValueError(f"Duplicate rule anchor {heading.anchor} in {path}")
            mapping[heading.anchor] = heading
    return mapping


def build_all_source_rule_heading_map() -> dict[str, RuleHeading]:
    mapping: dict[str, RuleHeading] = {}
    for path in iter_chapter_source_paths():
        for heading in extract_rule_headings(path):
            if heading.anchor in mapping:
                raise ValueError(f"Duplicate rule anchor {heading.anchor} in {path}")
            mapping[heading.anchor] = heading
    return mapping


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _mask_preserving_newlines(text: str) -> str:
    return "".join("\n" if char == "\n" else " " for char in text)


def mask_fenced_code(text: str) -> str:
    return CODE_FENCE_RE.sub(lambda match: _mask_preserving_newlines(match.group(0)), text)


def mask_spans(text: str, spans: list[tuple[int, int]]) -> str:
    if not spans:
        return text
    chars = list(text)
    for start, end in spans:
        for idx in range(start, end):
            if chars[idx] != "\n":
                chars[idx] = " "
    return "".join(chars)
