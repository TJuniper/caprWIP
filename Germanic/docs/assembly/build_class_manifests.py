#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ASSEMBLY_DIR = Path(__file__).resolve().parent
REPO_ROOT = ASSEMBLY_DIR.parents[2]
MODEL_DIR = REPO_ROOT / "Germanic/docs/lexeme_reports/model_entries"
TRACE_REPORT = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
# Historical-stage sidecar for reconstructed selected inputs, keyed by row_id.
# Lives with the corpus data (upstream of assembly) because it encodes scholarly
# historical judgments, not assembly output.
#
# CAPR project convention (author decision): PROTO is the Proto-Germanic
# lexeme-level reconstruction, so proto_stage is always pgmc. When PROTOFORM ==
# PROTO the selected input IS that PGmc reconstruction, so protoform_stage = pgmc
# automatically. The sidecar therefore records ONLY the exceptional rows where
# PROTOFORM != PROTO, whose stage is a separate historical question. A PROTOFORM
# != PROTO row with no sidecar entry fails closed (it is never silently pgmc).
STAGE_METADATA_PATH = REPO_ROOT / "Germanic/data/entry_stage_metadata.tsv"


def load_stage_metadata() -> dict[str, dict[str, str]]:
    """row_id -> {protoform_stage, protoform_variety} for the PROTOFORM != PROTO exception rows."""
    with STAGE_METADATA_PATH.open(encoding="utf-8") as handle:
        return {
            row["row_id"].strip(): {
                "protoform_stage": (row.get("protoform_stage") or "").strip(),
                "protoform_variety": (row.get("protoform_variety") or "").strip(),
            }
            for row in csv.DictReader(handle, delimiter="\t")
        }


def resolve_stages(row_id: str, proto: str, protoform: str, sidecar: dict[str, dict[str, str]]) -> tuple[str, str, str, list[str]]:
    """Resolve (proto_stage, protoform_stage, protoform_variety) under the CAPR convention.

    proto_stage is always pgmc (PROTO is the PGmc lexeme reconstruction). When
    PROTOFORM == PROTO, protoform_stage is pgmc by convention. When they differ,
    protoform_stage must come from an explicit sidecar decision; a missing entry
    is reported (fail closed), never defaulted to pgmc. protoform_variety is a
    separate orthogonal axis (e.g. 'transponent') and is blank unless the sidecar
    declares one; equality rows never carry a variety.
    """
    notes: list[str] = []
    proto_stage = "pgmc"
    if (proto or "").strip() and (proto or "").strip() == (protoform or "").strip():
        return proto_stage, "pgmc", "", notes
    entry = sidecar.get(str(row_id))
    if entry and entry.get("protoform_stage"):
        return proto_stage, entry["protoform_stage"], entry.get("protoform_variety", ""), notes
    notes.append("PROTOFORM != PROTO but no explicit stage decision (unresolved)")
    return proto_stage, "", "", notes


REQUIRED_METADATA = ("PROTO", "PROTOFORM", "COUNTERPART", "DERIVATION_CLASS")
CLASS_CONFIG = {
    "regular": ("regular", "Regular derivations", 1),
    "attested_variant": ("attested_variant", "Attested variants and selected comparison forms", 2),
    "early_analogy": ("early_analogy", "Early analogy and pre-Old-English input selection", 3),
    "late_analogy": ("late_analogy", "Late analogy and paradigm-cell selection", 4),
    "reconstructed_oe": ("reconstructed_oe", "Reconstructed Old English comparators", 5),
    "known_unmodelled": ("known_unmodelled", "Known but unmodelled remodellings", 6),
    "unexplained_unmodelled": (
        "unexplained_unmodelled",
        "Unexplained or deliberately unmodelled exceptions",
        7,
    ),
}
MANIFEST_COLUMNS = [
    "global_order",
    "class_order",
    "row_id",
    "lexical_item",
    "counterpart",
    "proto",
    "proto_stage",
    "protoform",
    "protoform_stage",
    "protoform_variety",
    "derivation_class",
    "class_bucket",
    "section_title",
    "model_entry_path",
    "trace_match_status",
    "trace_match_basis",
    "notes",
]
CLASS_MANIFESTS = {
    "regular": ASSEMBLY_DIR / "manifest_regular.tsv",
    "attested_variant": ASSEMBLY_DIR / "manifest_attested_variant.tsv",
    "early_analogy": ASSEMBLY_DIR / "manifest_early_analogy.tsv",
    "late_analogy": ASSEMBLY_DIR / "manifest_late_analogy.tsv",
    "reconstructed_oe": ASSEMBLY_DIR / "manifest_reconstructed_oe.tsv",
    "known_unmodelled": ASSEMBLY_DIR / "manifest_known_unmodelled.tsv",
    "unexplained_unmodelled": ASSEMBLY_DIR / "manifest_unexplained.tsv",
}


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
        entries.append(
            {
                "title": re.search(r"^# (.+)$", block, re.M).group(1).strip(),
                "proto": re.search(r"^PROTO:\s*(.*)$", block, re.M).group(1).strip(),
                "expected": re.search(r"^EXPECTED:\s*(.*)$", block, re.M).group(1).strip(),
                "outputs": re.search(r"^OUTPUTS:\s*(.*)$", block, re.M).group(1).strip(),
                "proto_input": re.search(r"^(?:English )?Proto Input:\s*(.*)$", block, re.M).group(1).strip(),
                "outcome": re.search(r"^Outcome:\s*(.*)$", block, re.M).group(1).strip(),
            }
        )
    return entries


def parse_model_entry(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise ValueError(f"empty model entry: {path}")

    title_line = next((line.strip() for line in lines if line.strip()), "")
    if not title_line.startswith("# "):
        raise ValueError(f"missing heading in model entry: {path}")

    metadata: dict[str, str] = {}
    title_index = lines.index(title_line)
    i = title_index + 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    while i < len(lines):
        match = re.match(r"^([A-Z_]+):\s*(.*)$", lines[i].strip())
        if not match:
            break
        metadata[match.group(1)] = match.group(2).strip()
        i += 1

    title = title_line[2:].strip()
    if " — OE " in title:
        lexical_item, title_counterpart = title.split(" — OE ", 1)
    else:
        lexical_item, title_counterpart = title, ""

    filename_match = re.match(r"^(\d+)-(.+)\.model\.md$", path.name)
    row_id = int(filename_match.group(1)) if filename_match else None

    missing = [field for field in REQUIRED_METADATA if not metadata.get(field)]
    raw_class = metadata.get("DERIVATION_CLASS", "")
    if raw_class in CLASS_CONFIG:
        class_bucket, section_title, class_rank = CLASS_CONFIG[raw_class]
    else:
        class_bucket = "review_unknown"
        section_title = "Unknown derivation class review bucket"
        class_rank = 99

    notes: list[str] = []
    if missing:
        notes.append("missing metadata: " + ", ".join(missing))
    if filename_match is None:
        notes.append("filename row ID does not parse cleanly")
    if raw_class not in CLASS_CONFIG:
        notes.append(f"unknown derivation class: {raw_class or '[blank]'}")
    if title_counterpart and metadata.get("COUNTERPART") and title_counterpart != metadata["COUNTERPART"]:
        notes.append("title counterpart differs from metadata COUNTERPART")

    return {
        "path": path,
        "row_id": row_id,
        "title": title,
        "lexical_item": lexical_item.strip(),
        "title_counterpart": title_counterpart.strip(),
        "metadata": metadata,
        "missing_metadata": missing,
        "class_bucket": class_bucket,
        "section_title": section_title,
        "class_rank": class_rank,
        "notes": notes,
    }


def match_trace_entry(model: dict[str, object], trace_entries: list[dict[str, str]]) -> tuple[str, str]:
    metadata = model["metadata"]
    lexical_item = model["lexical_item"]
    proto = metadata.get("PROTO", "")
    protoform = metadata.get("PROTOFORM", "")
    counterpart = metadata.get("COUNTERPART", "")

    candidates = [entry for entry in trace_entries if entry["title"] == lexical_item]
    if not candidates:
        return "no_lexical_match", "no lexical-item match"

    scored: list[tuple[int, dict[str, str], list[str]]] = []
    for entry in candidates:
        score = 0
        basis: list[str] = ["lexical item"]
        if entry["proto"] == protoform and protoform:
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

    scored.sort(key=lambda item: item[0], reverse=True)
    top_score, _, basis = scored[0]
    confident = top_score >= 16 and (len(scored) == 1 or top_score > scored[1][0])
    if confident:
        return "confident", " + ".join(basis)
    if top_score > 0:
        return "ambiguous", " + ".join(basis)
    return "low_confidence", "lexical item only"


def relative_repo_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def write_manifest(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in MANIFEST_COLUMNS})


def format_count_table(counts: Counter[str]) -> list[str]:
    rows = [
        ("regular", "Regular derivations"),
        ("attested_variant", "Attested variants and selected comparison forms"),
        ("early_analogy", "Early analogy and pre-Old-English input selection"),
        ("late_analogy", "Late analogy and paradigm-cell selection"),
        ("reconstructed_oe", "Reconstructed Old English comparators"),
        ("known_unmodelled", "Known but unmodelled remodellings"),
        ("unexplained_unmodelled", "Unexplained or deliberately unmodelled exceptions"),
    ]
    lines = ["| Derivation class | Count |", "| :--- | ---: |"]
    for key, label in rows:
        lines.append(f"| `{key}` ({label}) | {counts.get(key, 0)} |")
    return lines


def main() -> None:
    trace_entries = parse_trace_entries(TRACE_REPORT.read_text(encoding="utf-8"))
    models = [parse_model_entry(path) for path in sorted(MODEL_DIR.glob("*.model.md"))]
    stage_map = load_stage_metadata()

    models.sort(
        key=lambda model: (
            model["class_rank"],
            model["row_id"] if model["row_id"] is not None else 999999,
            model["path"].name,
        )
    )

    by_bucket: dict[str, list[dict[str, object]]] = defaultdict(list)
    count_by_raw_class: Counter[str] = Counter()
    trace_status_counts: Counter[str] = Counter()

    global_order = 0
    class_orders: Counter[str] = Counter()
    manifest_rows: list[dict[str, object]] = []
    for model in models:
        raw_class = model["metadata"].get("DERIVATION_CLASS", "")
        count_by_raw_class[raw_class or "[blank]"] += 1

        bucket = model["class_bucket"]
        if bucket != "review_unknown":
            global_order += 1
            class_orders[bucket] += 1
            global_value = global_order
            class_value = class_orders[bucket]
        else:
            global_value = ""
            class_value = ""

        trace_status, trace_basis = match_trace_entry(model, trace_entries)
        trace_status_counts[trace_status] += 1

        notes = list(model["notes"])
        if trace_status != "confident":
            notes.append(f"trace match {trace_status}")

        proto_stage, protoform_stage, protoform_variety, stage_notes = resolve_stages(
            str(model["row_id"]),
            model["metadata"].get("PROTO", ""),
            model["metadata"].get("PROTOFORM", ""),
            stage_map,
        )
        notes.extend(stage_notes)

        row = {
            "global_order": global_value,
            "class_order": class_value,
            "row_id": model["row_id"] if model["row_id"] is not None else "",
            "lexical_item": model["lexical_item"],
            "counterpart": model["metadata"].get("COUNTERPART", ""),
            "proto": model["metadata"].get("PROTO", ""),
            "proto_stage": proto_stage,
            "protoform": model["metadata"].get("PROTOFORM", ""),
            "protoform_stage": protoform_stage,
            "protoform_variety": protoform_variety,
            "derivation_class": raw_class,
            "class_bucket": bucket,
            "section_title": model["section_title"],
            "model_entry_path": relative_repo_path(model["path"]),
            "trace_match_status": trace_status,
            "trace_match_basis": trace_basis,
            "notes": "; ".join(notes),
        }
        manifest_rows.append(row)
        by_bucket[bucket].append(row)

    write_manifest(ASSEMBLY_DIR / "manifest_all_by_class.tsv", manifest_rows)
    for bucket, path in CLASS_MANIFESTS.items():
        write_manifest(path, by_bucket.get(bucket, []))

    unknown_classes = [row for row in manifest_rows if row["class_bucket"] == "review_unknown"]
    incomplete_metadata = [row for row in manifest_rows if "missing metadata" in row["notes"]]
    bad_row_ids = [row for row in manifest_rows if not row["row_id"]]
    special_handling = [
        row
        for row in manifest_rows
        if row["trace_match_status"] != "confident" or row["class_bucket"] == "review_unknown" or row["notes"]
    ]

    lines: list[str] = [
        "# Manifest summary",
        "",
        "## Corpus scan summary",
        "",
        f"- Total current model entries found: **{len(manifest_rows)}**",
        f"- Confident trace matches: **{trace_status_counts.get('confident', 0)}**",
        f"- Non-confident trace matches: **{len(manifest_rows) - trace_status_counts.get('confident', 0)}**",
        "",
        "## Counts by derivation class",
        "",
        *format_count_table(count_by_raw_class),
        "",
        "## Trace-match status",
        "",
        "| Trace-match status | Count |",
        "| :--- | ---: |",
    ]
    for key in ("confident", "ambiguous", "low_confidence", "no_lexical_match"):
        lines.append(f"| `{key}` | {trace_status_counts.get(key, 0)} |")

    lines.extend(["", "## Unknown or unexpected derivation classes", ""])
    if unknown_classes:
        lines.extend(
            [
                "| Row ID | File | Raw class | Notes |",
                "| :--- | :--- | :--- | :--- |",
                *[
                    f"| {row['row_id'] or '—'} | `{Path(row['model_entry_path']).name}` | `{row['derivation_class'] or '[blank]'}` | {row['notes'] or '—'} |"
                    for row in unknown_classes
                ],
            ]
        )
    else:
        lines.append("- None.")

    lines.extend(["", "## Incomplete metadata", ""])
    if incomplete_metadata:
        lines.extend(
            [
                "| Row ID | File | Missing fields |",
                "| :--- | :--- | :--- |",
                *[
                    f"| {row['row_id'] or '—'} | `{Path(row['model_entry_path']).name}` | {row['notes']} |"
                    for row in incomplete_metadata
                ],
            ]
        )
    else:
        lines.append("- None.")

    lines.extend(["", "## Filename row-ID parse issues", ""])
    if bad_row_ids:
        lines.extend(
            [
                "| File | Notes |",
                "| :--- | :--- |",
                *[f"| `{Path(row['model_entry_path']).name}` | {row['notes'] or '—'} |" for row in bad_row_ids],
            ]
        )
    else:
        lines.append("- None.")

    lines.extend(["", "## Entries needing special handling before full assembly", ""])
    if special_handling:
        lines.extend(
            [
                "| Row ID | File | Trigger |",
                "| :--- | :--- | :--- |",
                *[
                    f"| {row['row_id'] or '—'} | `{Path(row['model_entry_path']).name}` | {row['notes'] or row['trace_match_status']} |"
                    for row in special_handling
                ],
            ]
        )
    else:
        lines.append("- None.")

    (ASSEMBLY_DIR / "manifest_summary.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
