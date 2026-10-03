#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
from index_verborum_emission import build_emission_table, load_model_entry_headings, load_print_main
INTRO_PATH = SCRIPT_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_20.md"
LEXICAL_PATH = SCRIPT_DIR / "lexical_volume_alpha_01.md"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
MANIFEST_PATH = SCRIPT_DIR / "manifest_all_by_class.tsv"
OUTPUT_PATH = SCRIPT_DIR / "capr_book_draft_alpha_01.md"
NESTED_RECON_IV_RE = re.compile(r"\[\[(?P<form>[^\]]+)\]\{\.recon\}(?P<tail>.*?)\]\{(?P<attrs>[^}]*)\}")
EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{(?P<attrs>[^}]*)\}")


def has_tag_class(raw_attrs: str, cls: str) -> bool:
    return re.search(rf"(^|\s)\.{re.escape(cls)}(?=\s|$)", raw_attrs) is not None


def load_language_order() -> list[str]:
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as handle:
        return [row["code"] for row in csv.DictReader(handle, delimiter="\t") if (row.get("active") or "").strip() == "1"]


LANGUAGE_ORDER = load_language_order()

def oe_target_display(counterpart: str, derivation_class: str) -> str:
    return f"*{counterpart}" if derivation_class == "reconstructed_oe" else counterpart


def heading_ref(lexical_item: str, counterpart: str, derivation_class: str = "") -> str:
    return f"{lexical_item} — OE {oe_target_display(counterpart, derivation_class)}"


def load_production_rows() -> tuple[dict[str, list[str]], dict[str, dict[int, list[str]]], list[str]]:
    commands_by_heading_ref: dict[str, list[str]] = defaultdict(list)
    commands_by_line_ref: dict[str, dict[int, list[str]]] = defaultdict(lambda: defaultdict(list))
    main_rows = load_print_main()
    emission_rows = build_emission_table(main_rows, load_model_entry_headings())
    seen_emission_ids: set[str] = set()
    for row in emission_rows:
        if row.get("in_book") != "1":
            continue
        emission_id = row.get("emission_id", "")
        if emission_id in seen_emission_ids:
            continue
        seen_emission_ids.add(emission_id)
        path = row.get("emission_path", "")
        if path == "explicit_tag":
            continue
        cmd = row.get("index_command", "")
        site = row.get("site", "")
        if path == "heading_injection":
            if cmd not in commands_by_heading_ref[site]:
                commands_by_heading_ref[site].append(cmd)
        elif path == "line_injection":
            if ".md:" not in site:
                continue
            path_part, line_part = site.rsplit(":", 1)
            if not line_part.isdigit():
                continue
            line_no = int(line_part)
            if cmd not in commands_by_line_ref[path_part][line_no]:
                commands_by_line_ref[path_part][line_no].append(cmd)
    return commands_by_heading_ref, commands_by_line_ref, []


def annotate_explicit_tags_in_line(line: str, rel_path: str, line_no: int) -> str:
    source_ref = f'{rel_path}:{line_no}'
    span_counter = [0]  # mutable for closure; counts ALL .iv/.pred spans on this line

    def _make_attrs_with_provenance(existing_attrs: str) -> str | None:
        """Return augmented attrs string or None if span already has source_ref."""
        if re.search(r'(^|\s)source_ref=', existing_attrs):
            return None  # already annotated by upstream (model-entry builder)
        span_counter[0] += 1
        occ_id = f'{source_ref}:{span_counter[0]}'
        body = existing_attrs.strip()
        new_attrs = f'source_ref="{source_ref}" occ_id="{occ_id}"'
        return f'{body} {new_attrs}' if body else new_attrs

    def repl_nested(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if not (has_tag_class(attrs, "iv") or has_tag_class(attrs, "pred")):
            return match.group(0)
        new_attrs = _make_attrs_with_provenance(attrs)
        if new_attrs is None:
            return match.group(0)
        return f"[[{match.group('form')}]{{.recon}}{match.group('tail')}]{{{new_attrs}}}"

    def repl(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if not (has_tag_class(attrs, "iv") or has_tag_class(attrs, "pred")):
            return match.group(0)
        new_attrs = _make_attrs_with_provenance(attrs)
        if new_attrs is None:
            return match.group(0)
        return f"[{match.group('content')}]{{{new_attrs}}}"

    line = NESTED_RECON_IV_RE.sub(repl_nested, line)
    return EXPLICIT_TAG_RE.sub(repl, line)


def annotate_explicit_tags_with_source_ref(path: Path, text: str) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    return "\n".join(
        annotate_explicit_tags_in_line(line, rel, line_no)
        for line_no, line in enumerate(text.splitlines(), start=1)
    )


def inject_line_commands(path: Path, line_commands: dict[str, dict[int, list[str]]]) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    commands = line_commands.get(rel, {})
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    for idx, line in enumerate(lines, start=1):
        out.append(annotate_explicit_tags_in_line(line, rel, idx))
        if idx in commands:
            out.extend(commands[idx])
    return "\n".join(out).rstrip()


def strip_title_block(text: str) -> str:
    lines = text.rstrip().splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines).rstrip()


def strip_references(text: str) -> str:
    marker = "\n# References\n"
    return text.split(marker, 1)[0].rstrip() if marker in text else text.rstrip()


def strip_lexical_terminal_references(text: str) -> str:
    """Remove trailing \clearpage + ## References that terminates the standalone lexical volume."""
    text = re.sub(r'\s*\\clearpage\s*\n\s*## References.*$', '', text, flags=re.DOTALL)
    return text


_HIST_CHAPTER_RE = re.compile(r"^# Chapter \d+\. (.+)$")


def transform_chronology(text: str) -> str:
    """Emit the reader-facing chronology at correct heading levels for the book.

    The preamble before the first historical chapter (Scope and orientation,
    Numbering note) becomes an unnumbered chapter so it consumes no chapter
    number.  Its sections become unnumbered sections.

    Each ``# Chapter N. TITLE`` heading in the source becomes a real numbered
    book chapter at ``#`` level (``# TITLE``, dropping the ``Chapter N.`` prefix).

    Individual sound-change entries (``# Name``) are demoted to ``##`` sections
    within their historical chapter.

    Headings that appear directly under a historical chapter introduction
    (``## ...``) stay at ``##`` level.  Headings that appear inside a
    sound-change entry (``## Historical discussion``, ``## SC049. ...``) are
    demoted to ``###`` subsections.  This is tracked via the ``in_intro`` flag
    which is True after a ``# Chapter N.`` heading and False after the first
    plain ``# SoundChange`` heading within a chapter.

    ``###`` headings in chapter introductions (e.g. ``### West Germanic rhotacism
    (SC003)`` in the Chapter 3 intro) stay at ``###``.
    """
    out: list[str] = []
    preamble: list[str] = []
    seen_chapter = False
    in_intro = False          # True = inside historical chapter intro
                              # False = inside a sound-change entry

    for line in strip_title_block(strip_references(text)).splitlines():
        m = _HIST_CHAPTER_RE.match(line)
        if m:
            # Historical chapter heading
            if not seen_chapter and preamble:
                # Emit accumulated preamble as an unnumbered chapter so it
                # sits visibly between the \part heading and the first historical chapter
                # without consuming a chapter counter number.
                out.append("# Sound-change overview {.unnumbered}")
                for p in preamble:
                    if p.startswith("## ") and not p.rstrip().endswith("{.unnumbered}"):
                        out.append(p.rstrip() + " {.unnumbered}")
                    else:
                        out.append(p)
                preamble = []
                out.append("")
            seen_chapter = True
            in_intro = True
            out.append("# " + m.group(1))
        elif not seen_chapter:
            # Still accumulating preamble
            preamble.append(line)
        elif line.startswith("# "):
            # Sound-change entry (not a historical chapter heading)
            in_intro = False
            out.append("## " + line[2:])
        elif line.startswith("## "):
            if in_intro:
                # Chapter-introduction section → stays at ## (section in chapter)
                out.append(line)
            else:
                # Sound-change subsection → ### (subsection of sound-change section)
                out.append("### " + line[3:])
        elif line.startswith("### "):
            if in_intro:
                # Chapter-introduction sub-section (e.g. SC list in chap3 intro)
                out.append(line)
            else:
                # Deeper nesting inside a sound-change entry → ####
                out.append("#### " + line[4:])
        else:
            out.append(line)

    return "\n".join(out).rstrip()


_PART_HEADING_RE = re.compile(r"^## Part [IVX]+\.\s+(.+)$")


def transform_lexical(text: str, commands_by_ref: dict[str, list[str]]) -> str:
    """Emit lexical material at correct heading levels for the book.

    Front matter (Introduction, Data and sources, Transducer and derivation
    method, Derivation classes) becomes an unnumbered ``# Word-by-word
    derivations {.unnumbered}`` chapter so it consumes no chapter number,
    analogous to the Part I Sound-change overview.

    Each ``## Part N. TITLE`` heading becomes a real book chapter (``# TITLE``).
    Lexical entries (``### word — OE form``) become sections (``## word — OE form``).
    Entry subsections (``#### Derivation trace`` etc.) become subsections (``###``).
    """
    out: list[str] = []
    preamble: list[str] = []
    seen_part = False

    lines = strip_title_block(text).splitlines()
    if lines and lines[0].startswith("_Alpha 01"):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]

    for line in lines:
        m_part = _PART_HEADING_RE.match(line)
        if m_part:
            if not seen_part and preamble:
                # Emit front matter as unnumbered chapter with unnumbered sections
                out.append("# Word-by-word derivations {.unnumbered}")
                for p in preamble:
                    if p.startswith("## ") and not p.rstrip().endswith("{.unnumbered}"):
                        out.append(p.rstrip() + " {.unnumbered}")
                    else:
                        out.append(p)
                preamble = []
                out.append("")
            seen_part = True
            out.append("# " + m_part.group(1))
        elif not seen_part:
            preamble.append(line)
        elif line.startswith("### "):
            # Lexical entry heading: demote to ## (section within derivation-class chapter)
            entry_text = line[3:]  # keep the leading space from "### "
            out.append("##" + entry_text)
            # Inject index commands after each entry heading
            ref = line[4:].strip()
            if " — OE _" in ref and ref.endswith("_"):
                lexical_item, target = ref.split(" — OE ", 1)
                cleaned_target = target[1:-1].replace('\\*', '*')
                ref = f"{lexical_item} — OE {cleaned_target}"
            commands = commands_by_ref.get(ref, [])
            if commands:
                out.append("")
                out.extend(commands)
        elif line.startswith("#### "):
            # Entry subsection (Derivation trace, Reconstruction...) → ###
            out.append("###" + line[4:])
        elif line.startswith("##### "):
            out.append("####" + line[5:])
        else:
            out.append(line)

    return "\n".join(out).rstrip()


def build_book_markdown() -> str:
    commands_by_ref, line_commands, nonempty_languages = load_production_rows()
    intro = inject_line_commands(INTRO_PATH, line_commands)
    chronology = transform_chronology(inject_line_commands(CHRONOLOGY_PATH, line_commands))
    lexical_text = annotate_explicit_tags_with_source_ref(LEXICAL_PATH, LEXICAL_PATH.read_text(encoding="utf-8"))
    lexical = transform_lexical(
        strip_lexical_terminal_references(lexical_text),
        commands_by_ref,
    )
    index_parts = [r"\printindex[iv]"]
    parts = [
        r"\mainmatter",
        intro,
        r"\part{Sound changes, formalization, and relative chronology}",
        chronology,
        r"\part{Lexical derivations}",
        lexical,
        r"\backmatter",
        "# References",
        "",
        "::: {#refs}",
        ":::",
        "",
        r"\part*{Index verborum}",
        r"\addcontentsline{toc}{part}{Index verborum}",
        *index_parts,
    ]
    return "\n\n".join(parts) + "\n"


def main() -> None:
    OUTPUT_PATH.write_text(build_book_markdown(), encoding="utf-8")
    print(f"Generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
