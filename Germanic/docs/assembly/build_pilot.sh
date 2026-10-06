#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../.." && pwd)"

manifest="${script_dir}/pilot_manifest.tsv"
metadata="${script_dir}/pilot_metadata.yaml"
assembled_md="${script_dir}/pilot_assembled.md"
assembled_tex="${script_dir}/pilot_assembled.tex"
assembled_pdf="${script_dir}/pilot_assembled.pdf"
refs_bib="${repo_root}/docs/refs.bib"

python3 - "${repo_root}" "${manifest}" "${assembled_md}" <<'PY'
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

repo_root = Path(sys.argv[1])
manifest_path = Path(sys.argv[2])
output_path = Path(sys.argv[3])
trace_report_path = repo_root / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"


def normalize_headings(text: str) -> str:
    lines = []
    for line in text.splitlines():
        match = re.match(r'^(#{1,6})\s+(.*)$', line)
        if not match:
            lines.append(line)
            continue
        level = len(match.group(1))
        title = match.group(2)
        if level == 1:
            new_level = 2
        elif level == 2:
            new_level = 3
        elif level == 3:
            new_level = 3
        else:
            new_level = level
        lines.append(f'{"#" * new_level} {title}')
    return "\n".join(lines).strip()


def parse_trace_entries(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    chunks: list[list[str]] = []
    current: list[str] = []

    for line in text.splitlines():
        if line.startswith("# "):
            if current:
                chunks.append(current)
            current = [line]
        elif current:
            current.append(line)
    if current:
        chunks.append(current)

    for chunk in chunks:
        block = "\n".join(chunk).strip()
        lines = block.splitlines()
        table_lines: list[str] = []
        in_table = False
        for line in lines:
            if line.startswith("| Earlier Germanic developments | Old English developments |"):
                in_table = True
            if in_table and line.startswith("|"):
                table_lines.append(line)
                continue
            if in_table and not line.startswith("|"):
                break

        entries.append(
            {
                "title": lines[0][2:].strip(),
                "proto": re.search(r"^PROTO:\s*(.*)$", block, re.M).group(1).strip(),
                "expected": re.search(r"^EXPECTED:\s*(.*)$", block, re.M).group(1).strip(),
                "outputs": re.search(r"^OUTPUTS:\s*(.*)$", block, re.M).group(1).strip(),
                "proto_input": re.search(r"^(?:English )?Proto Input:\s*(.*)$", block, re.M).group(1).strip(),
                "outcome": re.search(r"^Outcome:\s*(.*)$", block, re.M).group(1).strip(),
                "table": "\n".join(table_lines).strip(),
            }
        )

    return entries


def italicize_form(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace("*", r"\*").replace("|", r"\|")
    return f"_{escaped}_"


def keep_as_code(text: str) -> bool:
    return bool(
        re.search(r"(?:\.md\b|\.txt\b|\.pdf\b|\.py\b|\.sh\b|\.tsv\b|^@|^https?://|docs/|Germanic/|--\w)", text)
    )


def convert_inline_code(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        return match.group(0) if keep_as_code(inner) else italicize_form(inner)

    return re.sub(r"`([^`]+)`", repl, text)


def demote_bold_forms(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if "\n" in inner:
            return match.group(0)
        if len(inner.split()) <= 3 and not re.search(r"[.!?;:]", inner):
            return inner if "`" in inner else italicize_form(inner)
        return inner

    return re.sub(r"\*\*([^*]+)\*\*", repl, text)


def tidy_prose(text: str) -> str:
    return convert_inline_code(demote_bold_forms(text))


def display_stage_name(stage: str) -> str:
    if stage == "Proto-West Germanic":
        return "West Germanic"
    return stage


def parse_trace_cell(cell: str) -> list[tuple[str, list[tuple[str, str]]]]:
    pieces = [piece.strip() for piece in re.split(r"<br\s*/?>", cell) if piece.strip()]
    if not pieces:
        return []

    stages: list[tuple[str, list[str]]] = []
    current_stage = ""
    current_items: list[str] = []

    for piece in pieces:
        stage_match = re.fullmatch(r"\*\*([^*]+)\*\*", piece)
        if stage_match:
            if current_stage or current_items:
                stages.append((current_stage, current_items))
            current_stage = stage_match.group(1).strip()
            current_items = []
            continue
        current_items.append(piece)

    if current_stage or current_items:
        stages.append((current_stage, current_items))

    parsed_stages: list[tuple[str, list[tuple[str, str]]]] = []
    for stage, items in stages:
        parsed_items: list[tuple[str, str]] = []

        for item in items:
            if item == "[no change]":
                parsed_items.append((item, ""))
                continue

            if ":" in item:
                change, form = item.split(":", 1)
                change = change.strip()
                form = form.strip()
            else:
                change = item.strip()
                form = ""

            parsed_items.append((change, form))

        parsed_stages.append((display_stage_name(stage), parsed_items))

    return parsed_stages


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def latex_form(text: str) -> str:
    return rf"\emph{{{latex_escape(text)}}}"


def humanize_derivation_class(label: str) -> str:
    mapping = {
        "regular": "regular",
        "early_analogy": "early analogy",
        "late_analogy": "late analogy",
        "unexplained_unmodelled": "unexplained exception",
    }
    return mapping.get(label, label.replace("_", " "))


def derivation_summary(model: dict[str, object], trace_entry: dict[str, str] | None) -> str:
    metadata = model["metadata"]
    citation = metadata.get("PROTO", "")
    selected = metadata.get("PROTOFORM", "")
    target = metadata.get("COUNTERPART", "")
    label = humanize_derivation_class(metadata.get("DERIVATION_CLASS", ""))
    arrow = r"$\rightarrow$"

    if trace_entry is None:
        return (
            f"Derivation: selected input {italicize_form(selected)} and target {italicize_form(target)}; "
            "no compact trace was confidently matched in this assembly pass."
        )

    output = trace_entry["outcome"]
    if citation == selected and output == target:
        return f"Derivation: {italicize_form(selected)} {arrow} {italicize_form(target)} ({label})."
    if citation != selected and output == target:
        return (
            f"Derivation: citation reconstruction {italicize_form(citation)}; "
            f"selected input {italicize_form(selected)} {arrow} {italicize_form(target)} ({label})."
        )
    if citation == selected and output != target:
        return (
            f"Derivation: {italicize_form(selected)} yields regular {italicize_form(output)}; "
            f"the selected target is {italicize_form(target)} ({label})."
        )
    return (
        f"Derivation: citation reconstruction {italicize_form(citation)}; "
        f"selected input {italicize_form(selected)} yields {italicize_form(output)}; "
        f"the selected target is {italicize_form(target)} ({label})."
    )


def render_trace_panel(
    stage_blocks: list[tuple[str, list[tuple[str, str]]]],
    *,
    suppress_old_english_stage: bool = False,
) -> list[str]:
    lines = [r"\raggedright"]

    for index, (stage, items) in enumerate(stage_blocks):
        show_stage_header = not (suppress_old_english_stage and stage == "Old English")
        if index:
            lines.append(r"\vspace{0.6em}")

        if show_stage_header:
            lines.extend(
                [
                    rf"\centering\textbf{{{latex_escape(stage)}}}\par",
                    r"\raggedright",
                    r"\vspace{0.2em}",
                ]
            )

        if not items:
            lines.append(r"\raggedright [no change]\par")
            continue

        if all(change == "[no change]" and not form for change, form in items):
            lines.append(r"\raggedright [no change]\par")
            continue

        lines.append(
            r"\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}"
        )
        for change, form in items:
            if change == "[no change]" and not form:
                lines.append(r"\multicolumn{2}{@{}l@{}}{[no change]} \\")
            elif form:
                lines.append(rf"{latex_escape(change)} & {latex_form(form)} \\")
            else:
                lines.append(rf"\multicolumn{{2}}{{@{{}}l@{{}}}}{{{latex_escape(change)}}} \\")
        lines.append(r"\end{tabularx}")

    return lines


def render_trace_table(trace_entry: dict[str, str]) -> list[str]:
    table_lines = trace_entry["table"].splitlines()
    if len(table_lines) < 3:
        return [trace_entry["table"]]

    row_parts = [part.strip() for part in table_lines[2].strip().strip("|").split("|")]
    if len(row_parts) != 2:
        return [trace_entry["table"]]

    left_panel = render_trace_panel(parse_trace_cell(row_parts[0]))
    right_panel = render_trace_panel(parse_trace_cell(row_parts[1]), suppress_old_english_stage=True)

    return [
        r"\begingroup",
        r"\setlength{\fboxsep}{6pt}",
        r"\noindent\fbox{%",
        r"\begin{minipage}{0.97\linewidth}",
        r"\small",
        r"\begin{minipage}[t]{0.485\linewidth}",
        r"\centering\textbf{Earlier Germanic changes}\par",
        r"\vspace{0.35em}",
        *left_panel,
        r"\end{minipage}\hfill",
        r"\begin{minipage}[t]{0.485\linewidth}",
        r"\centering\textbf{Old English changes}\par",
        r"\vspace{0.35em}",
        *right_panel,
        r"\end{minipage}",
        r"\end{minipage}%",
        r"}",
        r"\endgroup",
    ]


def parse_model_entry(path: Path) -> dict[str, object]:
    lines = normalize_headings(path.read_text(encoding="utf-8")).splitlines()
    if not lines:
        raise ValueError(f"empty model entry: {path}")

    title = lines[0].strip()
    i = 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    metadata: dict[str, str] = {}
    while i < len(lines):
        match = re.match(r"^([A-Z_]+):\s*(.*)$", lines[i])
        if not match:
            break
        metadata[match.group(1)] = match.group(2).strip()
        i += 1

    sections: list[tuple[str, str]] = []
    current_heading: str | None = None
    current_lines: list[str] = []
    for line in lines[i:]:
        if line.startswith("### "):
            if current_heading is not None:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            current_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_lines).strip()))

    lexical_item = title.removeprefix("## ").split(" — OE ", 1)[0].strip()
    return {
        "title": title,
        "lexical_item": lexical_item,
        "metadata": metadata,
        "sections": sections,
    }


def match_trace_entry(model: dict[str, object], trace_entries: list[dict[str, str]]) -> tuple[dict[str, str] | None, str, bool]:
    metadata = model["metadata"]
    lexical_item = model["lexical_item"]
    proto = metadata.get("PROTO", "")
    protoform = metadata.get("PROTOFORM", "")
    counterpart = metadata.get("COUNTERPART", "")

    candidates = [entry for entry in trace_entries if entry["title"] == lexical_item]
    scored: list[tuple[int, dict[str, str], list[str]]] = []
    for entry in candidates:
        score = 0
        basis: list[str] = ["lexical item"]
        if entry["proto"] == protoform:
            score += 10
            basis.append("PROTOFORM")
        if entry["proto"] == proto and proto:
            score += 4
            basis.append("PROTO")
        if entry["expected"] == counterpart and counterpart:
            score += 6
            basis.append("EXPECTED")
        if entry["outputs"] == counterpart and counterpart:
            score += 6
            basis.append("OUTPUTS")
        scored.append((score, entry, basis))

    if not scored:
        return None, "no lexical-item match", False

    scored.sort(key=lambda item: item[0], reverse=True)
    top_score, top_entry, basis = scored[0]
    confident = top_score >= 16 and (len(scored) == 1 or top_score > scored[1][0])
    return top_entry, " + ".join(basis), confident


def rewrite_entry(model: dict[str, object], trace_entry: dict[str, str] | None) -> str:
    out: list[str] = [model["title"], "", derivation_summary(model, trace_entry)]

    if trace_entry is not None:
        out.extend(
            [
                "",
                "### Derivation trace",
                "",
                f"Proto input: {italicize_form(trace_entry['proto_input'])}",
                "",
                *render_trace_table(trace_entry),
                "",
            ]
        )
        if trace_entry["outcome"] == model["metadata"].get("COUNTERPART", ""):
            out.append(f"Outcome: {italicize_form(trace_entry['outcome'])}")
        else:
            out.append(f"Transducer outcome: {italicize_form(trace_entry['outcome'])}")
            out.append("")
            out.append(f"Selected target: {italicize_form(model['metadata'].get('COUNTERPART', ''))}")

    for heading, body in model["sections"]:
        if heading == "### Transducer input and output":
            continue
        cleaned_body = tidy_prose(body)
        out.extend(["", heading, ""])
        if cleaned_body:
            out.append(cleaned_body)

    return "\n".join(out).strip()


rows = []
with manifest_path.open(encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle, delimiter="\t")
    rows = list(reader)

trace_entries = parse_trace_entries(trace_report_path.read_text(encoding="utf-8"))

parts = [
    "This pilot assembles a small representative subset of the current Germanic model entries for publication-format testing. Each entry combines the compact transducer trace with the current lexeme-report prose, while leaving the source `.model.md` files unchanged.",
    "",
    "The included entries are listed in `pilot_manifest.tsv` and appear here in stable manifest order. Compact trace blocks come from `oe_derivation_class_trace_report.compact.md`; philological and literature discussion comes from the current model-entry prose. Implementation reports, reviewer checklists, source ledgers, packets, and research notes are intentionally excluded from the assembled body.",
]

for row in rows:
    entry_path = repo_root / row["entry_path"]
    model = parse_model_entry(entry_path)
    trace_entry, basis, confident = match_trace_entry(model, trace_entries)
    if trace_entry is None or not confident:
        print(f"WARNING: trace match unresolved for {entry_path.name} ({basis})", file=sys.stderr)
        trace_entry = None
    else:
        print(
            f"Matched {entry_path.name} -> {trace_entry['title']} / {trace_entry['proto']} / {trace_entry['outputs']} ({basis})",
            file=sys.stderr,
        )
    parts.extend(["", rewrite_entry(model, trace_entry)])

output_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
print(f"Generated {output_path}")
PY

if ! command -v pandoc >/dev/null 2>&1; then
  echo "pandoc not found; regenerated ${assembled_md##*/} only. Skipping ${assembled_tex##*/} and ${assembled_pdf##*/}." >&2
  exit 0
fi

pandoc "${assembled_md}" \
  --standalone \
  --from=markdown+raw_tex+citations \
  --to=latex \
  --metadata-file="${metadata}" \
  --bibliography="${refs_bib}" \
  --citeproc \
  -o "${assembled_tex}"

echo "Generated ${assembled_tex}"

pdf_engine=""
if command -v xelatex >/dev/null 2>&1; then
  pdf_engine="xelatex"
elif command -v lualatex >/dev/null 2>&1; then
  pdf_engine="lualatex"
fi

if [[ -n "${pdf_engine}" ]]; then
  pandoc "${assembled_md}" \
    --standalone \
    --from=markdown+raw_tex+citations \
    --metadata-file="${metadata}" \
    --bibliography="${refs_bib}" \
    --citeproc \
    --pdf-engine="${pdf_engine}" \
    -o "${assembled_pdf}"
  echo "Generated ${assembled_pdf}"
else
  echo "No Unicode-capable PDF engine found (xelatex/lualatex); skipping PDF generation." >&2
fi
