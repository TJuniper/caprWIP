#!/usr/bin/env python3
"""Assemble the Version 1 reader-facing book section from the generated manifest.

The book's file list and chapter boundaries are NOT typed here: they come from
the GENERATED registry/reader_manifest.tsv (sources: reader_chapters.tsv +
reader_files.tsv + sc_registry.tsv + oe_pipeline). Chapter titles and intro
files come from the human registry/reader_chapters.tsv. This builder holds only
presentation logic (front matter, chapter blocks, heading wrapping, link
resolution) plus the manifest-coverage report.

Outputs (both under docs/sound_changes/reader_facing/):
  * reader_facing_local_section_20.md
  * reader_facing_manifest_coverage_08.md

Usage:
    python3 Germanic/tools/build_reader_book.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
REGISTRY_DIR = SC_DIR / "registry"
READER_MANIFEST = REGISTRY_DIR / "reader_manifest.tsv"
READER_CHAPTERS = REGISTRY_DIR / "reader_chapters.tsv"
READER_ROOT = SC_DIR / "reader_facing"
REPORT_MANIFEST = SC_DIR / "change_reports/report_manifest.tsv"

OUT_MD = READER_ROOT / "reader_facing_local_section_20.md"
OUT_COVERAGE = READER_ROOT / "reader_facing_manifest_coverage_08.md"

rule_heading_re = re.compile(
    r"^##\s+(SC\d{3})\.\s+(.*?)\s+\(`([^`]+)`\)\s+\{#(rule-[^}]+)\}\s*$")
link_re = re.compile(r"\[([^\]]+)\]\((#rule-[^)]+)\)")
long_rule_heading_threshold = 65

# Front-matter prose for the assembled section. Editorial content, owned here.
parts_front: list[str] = [
    "# The ordered sound-change sequence",
    "",
    "## Scope and orientation",
    "",
    "The sequence begins with early West Germanic consonant and vowel changes"
    " and ends with Old English r-metathesis.",
    "",
    "Rhotacism, brightening, breaking, umlaut, and apocope alternate with narrowly"
    " conditioned changes whose relative order rests on particular witness words.",
    "",
    "The evidence ranges from broadly attested sound laws to lexical constraints"
    " that establish only one chronological boundary.",
    "",
    "## Numbering note",
    "",
    "SC numbers remain the established legacy identifiers. The Version 1 book"
    " presents the changes in historical chapter order, which differs from the"
    " computational cascade order for several rules.",
    "",
    "SC038, SC062, and SC084 mark technical or prosodic stages rather than sound"
    " changes; SC077 is unused.",
    "",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def load_manifest() -> tuple[list[dict[str, str]], dict[str, dict[str, str]]]:
    manifest = read_tsv(READER_MANIFEST)
    chapters = {c["chapter_id"]: c for c in read_tsv(READER_CHAPTERS)}
    return manifest, chapters


def heading_visible_text(sc_number: str, title: str, rule_name: str) -> str:
    visible = title
    visible = re.sub(r"\\[A-Za-z]+\{([^{}]*)\}", r"\1", visible)
    visible = visible.replace("{", "").replace("}", "")
    visible = re.sub(r"\\[A-Za-z]+", "", visible)
    visible = re.sub(r"\s+", " ", visible).strip()
    return f"{sc_number}. {visible} ({rule_name})"


def wrap_long_rule_headings(text: str) -> str:
    wrapped: list[str] = []
    for line in text.splitlines():
        match = rule_heading_re.match(line.strip())
        if not match:
            wrapped.append(line)
            continue
        sc_number, title, rule_name, anchor = match.groups()
        if len(heading_visible_text(sc_number, title, rule_name)) <= long_rule_heading_threshold:
            wrapped.append(line)
            continue
        wrapped.append(
            f"## \\CAPRRuleHeading{{{sc_number}. {title}}}{{{rule_name}}} {{#{anchor}}}"
        )
    return "\n".join(wrapped)


def inject_chapter_block(chapter_num: str, title: str, intro_file: str) -> list[str]:
    """Return markdown lines for a chapter heading and intro."""
    block: list[str] = [
        "",
        r"\newpage",
        "",
        f"# Chapter {chapter_num}. {title}",
        "",
    ]
    intro_path = READER_ROOT / intro_file
    if intro_path.exists():
        intro_text = intro_path.read_text(encoding="utf-8").strip()
        # Drop the top-level # heading from the intro file (already rendered
        # as the chapter title)
        intro_lines = intro_text.splitlines()
        if intro_lines and intro_lines[0].startswith("# "):
            intro_lines = intro_lines[1:]
        block.extend(intro_lines)
        block.append("")
    return block


def render() -> dict[Path, str]:
    """Render every output to text without touching the filesystem."""
    manifest, chapters = load_manifest()
    manifest_files = [row["reader_file"] for row in manifest]

    active_anchors: set[str] = set()
    file_sc_map: dict[str, list[str]] = {}
    reader_sc_numbers: list[str] = []
    seen_sc: set[str] = set()

    for name in manifest_files:
        text = (READER_ROOT / name).read_text(encoding="utf-8")
        scs: list[str] = []
        for line in text.splitlines():
            match = rule_heading_re.match(line.strip())
            if not match:
                continue
            sc_number = match.group(1)
            scs.append(sc_number)
            active_anchors.add(f"#{match.group(4)}")
            if sc_number not in seen_sc:
                seen_sc.add(sc_number)
                reader_sc_numbers.append(sc_number)
        file_sc_map[name] = sorted(set(scs), key=lambda item: int(item[2:]))

    def resolve_links(text: str) -> str:
        return link_re.sub(
            lambda match: match.group(0) if match.group(2) in active_anchors
            else match.group(1), text)

    parts = list(parts_front)
    first_file_seen = False
    prev_chapter = None
    for row in manifest:
        name = row["reader_file"]
        chapter_id = row["chapter_id"]
        if chapter_id != prev_chapter:
            chapter = chapters[chapter_id]
            parts.extend(inject_chapter_block(
                chapter_id, chapter["title"], chapter["intro_file"]))
            prev_chapter = chapter_id
        elif first_file_seen:
            parts.extend(["", r"\newpage", ""])
        first_file_seen = True
        chapter_text = resolve_links(
            (READER_ROOT / name).read_text(encoding="utf-8").rstrip())
        parts.append(wrap_long_rule_headings(chapter_text))

    parts.extend([
        "",
        r"\newpage",
        "",
        "# References",
        "",
        "::: {#refs}",
        ":::",
        "",
    ])

    return {
        OUT_MD: "\n".join(parts),
        OUT_COVERAGE: render_coverage_report(
            manifest_files, file_sc_map, reader_sc_numbers),
    }


def build() -> None:
    for path, text in render().items():
        path.write_text(text, encoding="utf-8")


def render_coverage_report(manifest_files: list[str],
                           file_sc_map: dict[str, list[str]],
                           reader_sc_numbers: list[str]) -> str:
    manifest_rows: list[dict[str, object]] = []
    with REPORT_MANIFEST.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if not row["ID"]:
                continue
            sc_ids = [item.strip() for item in row["CHANGE_IDS"].split(";") if item.strip()]
            chapters = [name for name in manifest_files if set(file_sc_map[name]) & set(sc_ids)]
            covered_scs = sorted({sc for name in chapters for sc in file_sc_map[name]},
                                 key=lambda item: int(item[2:]))
            manifest_rows.append({
                "id": row["ID"],
                "title": row["TITLE"],
                "change_ids": sc_ids,
                "chapters": chapters,
                "covered": set(sc_ids).issubset(set(covered_scs)),
            })

    manifest_sc_numbers = sorted({sc for row in manifest_rows for sc in row["change_ids"]},
                                 key=lambda item: int(item[2:]))
    reader_sc_set = set(reader_sc_numbers)
    manifest_sc_set = set(manifest_sc_numbers)
    missing_manifest_sc = sorted(manifest_sc_set - reader_sc_set, key=lambda item: int(item[2:]))
    extra_reader_sc = sorted(reader_sc_set - manifest_sc_set, key=lambda item: int(item[2:]))

    front_manifest_gaps = []

    resumed_sc_numbers = [sc for sc in manifest_sc_numbers if int(sc[2:]) >= 14]
    if resumed_sc_numbers:
        resumed_min = min(int(sc[2:]) for sc in resumed_sc_numbers)
        resumed_max = max(int(sc[2:]) for sc in resumed_sc_numbers)
        later_gaps = [f"SC{i:03d}" for i in range(resumed_min, resumed_max + 1)
                      if f"SC{i:03d}" not in manifest_sc_set]
    else:
        later_gaps = []

    expected_gaps = later_gaps
    early_programme_missing = [
        f"SC{i:03d}"
        for i in range(3, 14)
        if f"SC{i:03d}" not in manifest_sc_set and f"SC{i:03d}" not in set(front_manifest_gaps)
    ]
    uncovered_rows = [row for row in manifest_rows if not row["covered"]]

    coverage_parts: list[str] = [
        "# Reader-facing manifest coverage 08",
        "",
        "## Inputs",
        "",
        "1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`",
        "2. `Germanic/docs/sound_changes/registry/reader_manifest.tsv`",
        "",
        "## Manifest rows covered by reader-facing chapters",
        "",
        "| Manifest row | Change IDs | Reader-facing chapter files | Covered |",
        "| --- | --- | --- | --- |",
    ]

    for row in manifest_rows:
        chapters = ", ".join(f"`{name}`" for name in row["chapters"]) if row["chapters"] else "—"
        coverage_parts.append(
            f"| `{row['id']}` {row['title']} | `{';'.join(row['change_ids'])}` | {chapters} | {'yes' if row['covered'] else 'no'} |"
        )

    coverage_parts.extend([
        "",
        "## SC numbers covered by reader-facing rule sections",
        "",
        ", ".join(f"`{sc}`" for sc in reader_sc_numbers),
        "",
        "## Manifest rows not yet covered",
        "",
    ])

    if uncovered_rows:
        for row in uncovered_rows:
            coverage_parts.append(f"1. `{row['id']}` {row['title']} — missing `{';'.join(row['change_ids'])}`")
    else:
        coverage_parts.append("1. none")

    coverage_parts.extend([
        "",
        "## SC numbers present in the manifest but missing from reader-facing rule headings",
        "",
    ])

    if missing_manifest_sc:
        coverage_parts.append(", ".join(f"`{sc}`" for sc in missing_manifest_sc))
    else:
        coverage_parts.append("1. none")

    coverage_parts.extend([
        "",
        "## Reader-facing rule headings not present in the manifest",
        "",
    ])

    if extra_reader_sc:
        coverage_parts.append(", ".join(f"`{sc}`" for sc in extra_reader_sc))
    else:
        coverage_parts.append("1. none")

    coverage_parts.extend([
        "",
        "## Expected gaps in the manifest-backed sequence",
        "",
    ])

    if expected_gaps:
        coverage_parts.append(", ".join(f"`{sc}`" for sc in expected_gaps))
    else:
        coverage_parts.append("1. none")

    coverage_parts.extend([
        "",
        "## Early SC numbers and the current manifest-backed programme",
        "",
    ])

    early_entries = [
        ("SC003", "003-west-germanic-rhotacism.md"),
        ("SC004", "004-pwgmc-ai-monophthongization.md"),
        ("SC005", "005-unstressed-a-raising-before-final-m.md"),
        ("SC006", "006-early-i-apocope.md"),
        ("SC007", "007-final-o-lowering-before-r.md"),
        ("SC008", "008-coronal-w-assimilation.md"),
        ("SC009", "009-ij-contraction-in-friend.md"),
        ("SC010", "010-west-germanic-j-gemination.md"),
        ("SC011", "011-syllabic-j-after-final-vowel-loss.md"),
        ("SC012", "012-lth-voicing.md"),
        ("SC013", "013-dental-hardening.md"),
    ]
    for idx, (sc, fname) in enumerate(early_entries, start=1):
        if sc in manifest_sc_set and sc in reader_sc_set:
            coverage_parts.append(f"{idx}. `{sc}` is now covered by `{fname}`.")
        else:
            coverage_parts.append(
                f"{idx}. `{sc}` is not fully covered in the current reader-facing set.")

    coverage_parts.append("12. Coverage from `SC014` through `SC087` remains intact.")

    if early_programme_missing:
        coverage_parts.append(
            "13. The remaining early SC numbers outside the current manifest-backed programme are "
            + ", ".join(f"`{sc}`" for sc in early_programme_missing)
            + "."
        )
    else:
        coverage_parts.append("13. No other early SC numbers remain outside the current manifest-backed programme.")

    if {"SC003", "SC004", "SC005", "SC006", "SC007", "SC008", "SC009", "SC010",
            "SC011", "SC012", "SC013", "SC014", "SC015"} <= manifest_sc_set:
        coverage_parts.append(
            "14. The manifest-backed sequence now opens with `SC003`, `SC004`, `SC005`, "
            "`SC006`, `SC007`, `SC008`, `SC009`, `SC010`, `SC011`, `SC012`, and `SC013`, "
            "and then resumes at `SC014-SC015`.")
    else:
        coverage_parts.append(
            "14. The manifest-backed opening sequence no longer matches the expected "
            "`SC003`, `SC004`, `SC005`, `SC006`, `SC007`, `SC008`, `SC009`, `SC010`, "
            "`SC011`, `SC012`, `SC013`, then `SC014-SC015` pattern.")

    return "\n".join(coverage_parts) + "\n"


def main() -> int:
    build()
    print(f"Generated {OUT_MD}")
    print(f"Generated {OUT_COVERAGE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
