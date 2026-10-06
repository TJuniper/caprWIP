#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_PATH = ROOT / "reader_facing_foma_width_check_01.md"
THRESHOLD = 90
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


@dataclass
class BlockCheck:
    file_name: str
    start_line: int
    heading: str
    longest_line: int
    overflow_lines: list[str]


def iter_target_files() -> list[Path]:
    return [path for path in sorted(ROOT.glob("*.md")) if path.name not in DEFAULT_SKIP]


def scan_foma_blocks(path: Path) -> list[BlockCheck]:
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[BlockCheck] = []
    current_heading = ""
    inside = False
    block_lines: list[str] = []
    start_line = 0

    for idx, line in enumerate(lines, start=1):
        if line.startswith("## "):
            current_heading = line[3:].strip()
        if line.strip() == "```foma":
            inside = True
            block_lines = []
            start_line = idx
            continue
        if inside and line.strip() == "```":
            longest = max((len(item) for item in block_lines), default=0)
            overflow = [item for item in block_lines if len(item) > THRESHOLD]
            blocks.append(
                BlockCheck(
                    file_name=path.name,
                    start_line=start_line,
                    heading=current_heading,
                    longest_line=longest,
                    overflow_lines=overflow,
                )
            )
            inside = False
            continue
        if inside:
            block_lines.append(line)
    return blocks


def render(blocks: list[BlockCheck]) -> str:
    overflowing = [block for block in blocks if block.overflow_lines]
    lines = [
        "# Reader-facing foma width check 01",
        "",
        "_Generated from the current fenced `foma` blocks in the reader-facing chapter files._",
        "",
        "## Summary",
        "",
        f"- Foma blocks checked: {len(blocks)}.",
        f"- Blocks over the conservative {THRESHOLD}-character threshold: {len(overflowing)}.",
        "- Width-safe rendering protocol: `ReaderFacingFoma` uses `fvextra`/`Verbatim` with `breaklines=true`, `breakanywhere=true`, and `fontsize=\\small` in the Docker XeLaTeX build.",
        "",
        "| File | Rule section | Start line | Longest line | Over threshold under old rendering |",
        "| --- | --- | --- | --- | --- |",
    ]
    for block in blocks:
        lines.append(
            f"| {block.file_name} | {block.heading or '—'} | {block.start_line} | {block.longest_line} | {'yes' if block.overflow_lines else 'no'} |"
        )

    if overflowing:
        lines.extend(["", "## Lines that would have overflowed under the old rendering", ""])
        for block in overflowing:
            lines.append(f"### {block.file_name}:{block.start_line} — {block.heading or 'Unnamed block'}")
            lines.append("")
            for line in block.overflow_lines:
                lines.append(f"- `{len(line)}` chars — `{line}`")
            lines.append("")

    lines.extend(
        [
            "## Interpretation",
            "",
            "The conservative character threshold identifies blocks that were likely to overflow under the previous unwrapped PDF rendering. The current build-side `ReaderFacingFoma` environment wraps these lines, so the presence of long source lines no longer implies right-margin loss in the final PDF.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    blocks: list[BlockCheck] = []
    for path in iter_target_files():
        blocks.extend(scan_foma_blocks(path))
    OUTPUT_PATH.write_text(render(blocks), encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH}")
    print(f"Foma blocks checked: {len(blocks)}; blocks over threshold: {sum(1 for block in blocks if block.overflow_lines)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
