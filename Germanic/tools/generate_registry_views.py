#!/usr/bin/env python3
"""Regenerate all derived views from the canonical SC registries.

SOURCE (hand-edited; human judgements only):
    Germanic/docs/sound_changes/registry/sc_registry.tsv
    Germanic/docs/sound_changes/registry/sc_inventory_notes.tsv
    Germanic/docs/sound_changes/registry/chronology_edges.tsv

MACHINE AUTHORITIES (read, never written by a human):
    Germanic/fsts/germanic.txt              via tools/executable_facts.py
                                            and tools/oe_pipeline.py (order)
    docs/debug_snapshots/oe_full_trace_report.txt  via tools/rule_coverage_census.py

GENERATED (never hand-edited; written by this script):
    Germanic/docs/sound_changes/registry/sc_inventory_annotations.tsv
    Germanic/docs/sound_changes/registry/current_sc_state.tsv
    Germanic/docs/sound_changes/sound_change_historical_staging_map.tsv
    Germanic/docs/sound_changes/sound_change_inventory.tsv
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.tsv
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.json
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_edges.dot
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_nodes.tsv
    Germanic/docs/sound_changes/order_tests/chronology_graph/first_break_graph_summary.md
    Germanic/docs/sound_changes/registry/settled_verdicts.md

FROZEN ARCHIVES (never regenerated, never synchronized with current state):
    Germanic/docs/sound_changes/cascade_baseline/historical_audit_table.tsv
    Germanic/docs/sound_changes/cascade_baseline/rename_migration_manifest.tsv
    These are dated ARCHIVE / FROZEN snapshots of a past state. This script
    does not write them, adjudicate.py --finalize explicitly excludes them,
    and current-state propagation must never synchronize them. Their
    historical builders (tools/build_historical_audit_table.py,
    tools/build_rename_migration_manifest.py) are retained only as a record
    of how the snapshots were originally produced.

Usage:
    python3 Germanic/tools/generate_registry_views.py            # write views
    python3 Germanic/tools/generate_registry_views.py --check    # verify clean
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import executable_facts  # noqa: E402
import oe_pipeline  # noqa: E402
import rule_coverage_census  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
REGISTRY_DIR = SC_DIR / "registry"
GRAPH_DIR = SC_DIR / "order_tests/chronology_graph"
ORDER_SUMMARIES = SC_DIR / "order_tests/summaries"

SC_REGISTRY = REGISTRY_DIR / "sc_registry.tsv"
INVENTORY_NOTES = REGISTRY_DIR / "sc_inventory_notes.tsv"
EDGE_REGISTRY = REGISTRY_DIR / "chronology_edges.tsv"
READER_CHAPTERS = REGISTRY_DIR / "reader_chapters.tsv"
READER_FILES = REGISTRY_DIR / "reader_files.tsv"

# The complete list of hand-edited inputs this generator may read. Guardrail
# tests assert that no archived file can silently become a current-state input.
DECLARED_INPUTS = (SC_REGISTRY, INVENTORY_NOTES, EDGE_REGISTRY,
                   READER_CHAPTERS, READER_FILES)

ANNOTATIONS = REGISTRY_DIR / "sc_inventory_annotations.tsv"  # now GENERATED
BASELINE_OUTPUTS = SC_DIR / "cascade_baseline/cascade_baseline_outputs.tsv"

RULE_SOURCE_PATH = executable_facts.FST_REL
# literature_status is the inventory vocabulary for the registry's
# adjudication_status. It is a rendering, not an independent judgement.
LITERATURE_STATUS = {"unadjudicated": "not_started", "adjudicated": "adjudicated"}

STAGING_VIEW = SC_DIR / "sound_change_historical_staging_map.tsv"
INVENTORY_VIEW = SC_DIR / "sound_change_inventory.tsv"
CURRENT_SC_STATE = REGISTRY_DIR / "current_sc_state.tsv"
READER_MANIFEST = REGISTRY_DIR / "reader_manifest.tsv"
CURRENT_CHRONOLOGY = REGISTRY_DIR / "current_chronology.tsv"
EDGES_TSV = GRAPH_DIR / "first_break_edges.tsv"
EDGES_JSON = GRAPH_DIR / "first_break_edges.json"
EDGES_DOT = GRAPH_DIR / "first_break_edges.dot"
NODES_TSV = GRAPH_DIR / "first_break_nodes.tsv"
GRAPH_SUMMARY = GRAPH_DIR / "first_break_graph_summary.md"
SETTLED_VERDICTS = REGISTRY_DIR / "settled_verdicts.md"

CHRONOLOGY_RELATION_TYPES = {
    "broad_far_chronology",
    "near_reciprocal_chronology",
    "one_sided_chronology",
    "reciprocal_chronology",
}

VERDICT_VOCABULARY = {
    "RETAIN", "REFORMULATE", "RESTRICT", "SPLIT", "RETIRE", "REORDER", "DEFER",
}


def read_tsv(path: Path):
    header = None
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        fields = line.split("\t")
        if header is None:
            header = fields
        else:
            rows.append(dict(zip(header, fields)))
    return rows


def tsv_text(banner_lines, header, rows):
    lines = [f"# {b}" if b else "#" for b in banner_lines]
    lines.append("\t".join(header))
    for row in rows:
        lines.append("\t".join(row))
    return "\n".join(lines) + "\n"


def banner(source_desc):
    return [
        "GENERATED FILE — DO NOT EDIT.",
        f"Source: {source_desc}",
        "Generator: Germanic/tools/generate_registry_views.py (run after editing sources).",
    ]


# Columns a human source file may never contain: each names a fact that has a
# real authority elsewhere, so a hand-typed copy is a second authority.
FORBIDDEN_HUMAN_COLUMNS = {
    "foma_definition_raw": "germanic.txt (tools/executable_facts.py)",
    "rule_source_anchor": "germanic.txt (tools/executable_facts.py)",
    "rule_source_path": "germanic.txt (tools/executable_facts.py)",
    "rule_source_line": "computed for display only, never stored",
    "cascade_position": "cascade_baseline/executable_model.tsv",
    "exec_index": "cascade_baseline/executable_model.tsv",
    "appears_in_compact_trace": "cascade_baseline/rule_coverage_census.tsv",
    "trace_occurrence_count": "cascade_baseline/rule_coverage_census.tsv",
    "firing_count": "cascade_baseline/rule_coverage_census.tsv",
    "firing_lexemes": "cascade_baseline/rule_coverage_census.tsv",
    "example_lexemes": "ambiguous; use illustrative_lexemes (human) or the census",
    "trace_stage": "sc_registry.tsv pipeline_stage",
    "literature_status": "sc_registry.tsv adjudication_status",
}


def validate_human_sources(notes):
    """A hand-edited source may contain only human judgements."""
    errors = []
    if not notes:
        return ["inventory notes: file is empty"]
    for column, authority in FORBIDDEN_HUMAN_COLUMNS.items():
        if column in notes[0]:
            errors.append(
                f"inventory notes: column {column!r} is machine-derived "
                f"(authority: {authority}) and must not be hand-maintained")
    for n in notes:
        for column, value in n.items():
            if column in ("notes", "review_note", "plain_description_draft"):
                continue  # prose may legitimately mention a rule
            if executable_facts.LINE_REF_RE.search(value or ""):
                errors.append(
                    f"inventory notes: {n['change_id']} column {column!r} "
                    "contains a Foma source line number; line numbers are "
                    "computed for display and never stored")
    errors.extend(validate_human_prose("sc_inventory_notes.tsv", notes, "change_id"))
    return errors


def split_lexemes(value):
    return [x.strip() for x in re.split(r"[;,]", value or "") if x.strip()]


# Unmistakable formulations of CURRENT machine state. Human prose may describe
# scientific relations, but a volatile quantity or physical cascade offset that
# has a generated authority must not be mirrored in hand-edited metadata: the
# mirror goes stale the moment a corpus row, a firing population or the
# executable order changes. Deliberately conservative — page numbers, dates,
# section references ("Campbell 128"), SC numbers and phrases such as "one
# historical sound change" are all legitimate and must not be caught.
MACHINE_STATE_PROSE = (
    (r"\bcascade position\s+\d+", "the generated executable model"),
    (r"\bexecutable position\s+\d+", "the generated executable model"),
    (r"\bexec[_ ]index\s*=?\s*\d+", "the generated executable model"),
    (r"\bposition\s+\d+\b", "the generated executable model"),
    (r"\bpositions\s+\d+\s*[-\u2013]\s*\d+", "the generated executable model"),
    (r"\bpos\.?\s+\d+\b", "the generated executable model"),
    (r"\bmoved from position\s+\d+", "the generated executable model"),
    (r"\btrace_occurrence_count\b", "the generated firing census"),
    (r"\bwitness_count\b", "the generated firing census"),
    (r"\bfiring_count\s*=\s*\d+", "the generated firing census"),
    (r"\bfires\s+\d+\s+times\b", "generated firing_count / firing_lexemes"),
    (r"\b\d+\s+firings\b", "generated firing_count / firing_lexemes"),
    (r"\b\d+\s+corpus\s+(applications|firings|witnesses|rows)\b",
     "generated firing_count / firing_lexemes"),
    (r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s+"
     r"corpus\s+(applications|firings|witnesses|rows)\b",
     "generated firing_count / firing_lexemes"),
    (r"\ball\s+\d+\s+(firings|witnesses|applications)\b",
     "generated firing_count / firing_lexemes"),
    (r"\bsole\s+(live\s+)?(firing|witness|corpus firing)\b",
     "generated firing_count / firing_lexemes"),
    (r"\bonly\s+(live\s+)?(firing|witness)\b",
     "generated firing_count / firing_lexemes"),
)

MACHINE_STATE_PROSE_RE = tuple(
    (re.compile(pattern, re.IGNORECASE), advice)
    for pattern, advice in MACHINE_STATE_PROSE
)

# Free-text columns of the hand-edited sources. Prose here is expected to stay
# current, so it is held to the same authority rule as a structured column.
# (Dated adjudication memos under docs/sound_changes/audits/ are research
# records, not live metadata, and are deliberately NOT covered by this guard.)
HUMAN_PROSE_COLUMNS = {
    "sc_inventory_notes.tsv": ("notes", "review_note", "plain_description_draft"),
    "sc_registry.tsv": (
        "staging_notes", "chronology_summary", "chronology_problem",
        "evidence_summary", "notes", "verdict_summary",
    ),
    "chronology_edges.tsv": ("notes", "representative_forms"),
}


def find_machine_state_prose(text):
    """Return (matched_text, advice) pairs for machine-state claims in prose."""
    hits = []
    for pattern, advice in MACHINE_STATE_PROSE_RE:
        for m in pattern.finditer(text or ""):
            hits.append((m.group(0), advice))
    return hits


def validate_human_prose(filename, rows, key_column):
    """No live human metadata may mirror a current machine-state quantity."""
    errors = []
    columns = HUMAN_PROSE_COLUMNS.get(filename, ())
    for row in rows:
        key = row.get(key_column) or "?"
        for column in columns:
            if column not in row:
                continue
            for matched, advice in find_machine_state_prose(row[column]):
                errors.append(
                    f"{filename}: {key} column {column!r} states current machine "
                    f"state ({matched!r}); human prose must describe the "
                    f"scientific relation and defer to {advice}"
                )
    return errors


def load_harness_witnesses():
    """Edge -> witness lexemes actually demonstrated by the order-test harness.

    The canonical first-break/order-sensitivity summaries record, per run, the
    rule that was displaced, the rule it was crossed with, and the lexeme whose
    output changed. That is machine evidence that the two rules really do
    interact on that lexeme, as opposed to mere corpus membership.
    """
    witnesses = {}
    if not ORDER_SUMMARIES.is_dir():
        return witnesses
    for path in sorted(ORDER_SUMMARIES.glob("*_changes.tsv")):
        try:
            rows = read_tsv(path)
        except Exception:  # a malformed archive summary must not break --check
            continue
        for row in rows:
            change = row.get("change_id")
            crossed = row.get("crossed_change_id")
            lexeme = row.get("lexical_item")
            if change and crossed and lexeme:
                witnesses.setdefault((change, crossed), set()).add(lexeme)
                witnesses.setdefault((crossed, change), set()).add(lexeme)
    return witnesses


def load_corpus_concepts():
    """The selected corpus, from the cascade baseline outputs."""
    if not BASELINE_OUTPUTS.is_file():
        return None
    return {r["concept"] for r in read_tsv(BASELINE_OUTPUTS)}


# Order-valued columns that once lived in sc_registry.tsv. Executable order is
# owned by oe_pipeline (parsed from germanic.txt); the legacy inventory/staging
# order spaces are frozen in registry/archival_orders.tsv (ARCHIVE). None of
# them may reappear as a hand-maintained registry column.
REGISTRY_FORBIDDEN_COLUMNS = dict(FORBIDDEN_HUMAN_COLUMNS)
REGISTRY_FORBIDDEN_COLUMNS.update({
    "staging_order": "registry/archival_orders.tsv (ARCHIVE / FROZEN)",
    "inventory_order": "registry/archival_orders.tsv (ARCHIVE / FROZEN)",
    "current_order": "no such fact; executable order is oe_pipeline's",
    "v1_chapter": "registry/reader_files.tsv (file -> chapter) via "
                  "source_reader_facing_file",
    "v1_reader_position": "GENERATED registry/reader_manifest.tsv "
                          "(min cascade position per reader file)",
})


def validate_registry(reg, edges):
    errors = []
    for column, authority in REGISTRY_FORBIDDEN_COLUMNS.items():
        if reg and column in reg[0]:
            errors.append(
                f"registry: column {column!r} is machine-derived or archival "
                f"(authority: {authority}) and must not be hand-maintained")
    corpus = load_corpus_concepts()
    if corpus is None:
        corpus = set()
    harness = load_harness_witnesses()
    errors.extend(validate_human_prose("sc_registry.tsv", reg, "sc_id"))
    errors.extend(validate_human_prose("chronology_edges.tsv", edges, "source_change_id"))
    counts = Counter(r["sc_id"] for r in reg)
    for sc, n in counts.items():
        if n != 1:
            errors.append(f"registry: {sc} appears {n} times")
    ids = set(counts)
    model_idents = {s.foma_identifier for s in oe_pipeline.named_stages()}
    for r in reg:
        ident = (r.get("fst_identifier") or "").strip()
        if r["lifecycle_status"] == "active" and ident and ident not in model_idents:
            errors.append(
                f"registry: active {r['sc_id']} fst_identifier {ident!r} is not "
                "a stage of the executable model (oe_pipeline)")
        if r["lifecycle_status"] == "retired" and ident and ident in model_idents:
            errors.append(
                f"registry: retired {r['sc_id']} fst_identifier {ident!r} is "
                "still a stage of the executable model")
        if r["lifecycle_status"] not in ("active", "retired"):
            errors.append(f"registry: {r['sc_id']} bad lifecycle_status {r['lifecycle_status']!r}")
        if r["lifecycle_status"] == "retired":
            if r["staging_row"] == "yes":
                errors.append(f"registry: retired {r['sc_id']} marked as a staging row")
        if r["verdict"]:
            for token in r["verdict"].split("/"):
                if token not in VERDICT_VOCABULARY:
                    errors.append(f"registry: {r['sc_id']} verdict token {token!r} not in vocabulary")
            if r["adjudication_status"] != "adjudicated":
                errors.append(f"registry: {r['sc_id']} has a verdict but is not marked adjudicated")
            if not r["adjudication_memo"]:
                errors.append(f"registry: {r['sc_id']} has a verdict but no adjudication_memo")
            elif not (REPO_ROOT / r["adjudication_memo"]).is_file():
                errors.append(f"registry: {r['sc_id']} memo missing: {r['adjudication_memo']}")
    for e in edges:
        for endpoint in (e["source_change_id"], e["target_change_id"]):
            if endpoint.startswith("SC") and endpoint not in ids:
                errors.append(f"edges: unknown SC {endpoint}")
        if e["relation_type"] in CHRONOLOGY_RELATION_TYPES:
            if e["evidence_basis"] not in ("independently_demonstrated", "stage_entailed"):
                errors.append(
                    f"edges: {e['source_change_id']}->{e['target_change_id']} chronology edge "
                    f"with evidence_basis {e['evidence_basis']!r}"
                )
            if not e["witness_role"]:
                errors.append(f"edges: {e['source_change_id']}->{e['target_change_id']} missing witness_role")
            if not e["notes"]:
                errors.append(
                    f"edges: {e['source_change_id']}->{e['target_change_id']} chronology edge "
                    "without notes explaining the relation"
                )
            # A chronology edge that CLAIMS a live lexical demonstration must
            # name real corpus items. An edge whose direction follows from
            # independently established stages legitimately has no current
            # witness, and inventing one to satisfy a validator would be
            # fabricating evidence.
            if e["evidence_basis"] == "independently_demonstrated":
                if not e["representative_lexemes"] or not e["representative_forms"]:
                    errors.append(
                        f"edges: {e['source_change_id']}->{e['target_change_id']} claims an "
                        "independently demonstrated relation but names no witness "
                        "lexemes/forms (use evidence_basis=stage_entailed if the "
                        "direction follows from the stages alone)"
                    )
                for lex in split_lexemes(e["representative_lexemes"]):
                    if lex not in corpus:
                        errors.append(
                            f"edges: {e['source_change_id']}->{e['target_change_id']} names "
                            f"witness {lex!r}, which is not in the selected corpus"
                        )
                # representative_lexemes establishes CORPUS MEMBERSHIP ONLY: it
                # proves the named word is in the selected corpus, not that it
                # actually demonstrates the claimed interaction. A claimed live
                # demonstration must therefore also have a machine-checkable
                # evidence route: either the canonical order-test harness
                # recorded an output change for this rule pair on one of the
                # named lexemes, or structured metadata names a dedicated
                # regression test that checks the interaction.
                pair = (e["source_change_id"], e["target_change_id"])
                demonstrated = harness.get(pair, set())
                named = set(split_lexemes(e["representative_lexemes"]))
                ref = (e.get("machine_evidence") or "").strip()
                if not (demonstrated & named):
                    if not ref:
                        errors.append(
                            f"edges: {e['source_change_id']}->{e['target_change_id']} claims an "
                            "independently demonstrated relation, but no order-test "
                            "harness result demonstrates the interaction on a named "
                            "witness; name a dedicated regression test in "
                            "machine_evidence (test:Germanic/tests/<file>.py) or use "
                            "evidence_basis=stage_entailed"
                        )
                    elif not ref.startswith("test:"):
                        errors.append(
                            f"edges: {e['source_change_id']}->{e['target_change_id']} has "
                            f"machine_evidence {ref!r}; expected test:<path>"
                        )
                    elif not (REPO_ROOT / ref[len("test:"):]).is_file():
                        errors.append(
                            f"edges: {e['source_change_id']}->{e['target_change_id']} "
                            f"machine_evidence names a missing test: {ref[len('test:'):]}"
                        )
            retired = {r["sc_id"] for r in reg if r["lifecycle_status"] == "retired"}
            if e["source_change_id"] in retired or e["target_change_id"] in retired:
                errors.append(
                    f"edges: retired SC on chronology edge {e['source_change_id']}->{e['target_change_id']}"
                )
    return errors


def build_staging_view(reg):
    header = [
        "sc_id", "fst_identifier", "display_name", "source_reader_facing_file",
        "cascade_position", "hist_stage", "hist_scope", "confidence",
        "action_status", "capr_evidence", "chronology_problem", "notes",
    ]
    staged = [r for r in reg if r["staging_row"] == "yes"]
    position = {r["sc_id"]: oe_pipeline.cascade_position(r["fst_identifier"])
                for r in staged}
    missing = [sc for sc, pos in position.items() if pos is None]
    if missing:
        raise SystemExit(
            f"staging view: staged SCs without a numbered cascade position: {missing}")
    staged.sort(key=lambda r: position[r["sc_id"]])
    rows = [
        [
            r["sc_id"], r["fst_identifier"], r["display_name"],
            r["source_reader_facing_file"], str(position[r["sc_id"]]),
            r["hist_stage"],
            r["hist_scope"], r["confidence"],
            r["action_status"], r["capr_evidence"], r["chronology_problem"],
            r["staging_notes"],
        ]
        for r in staged
    ]
    b = banner("registry/sc_registry.tsv (rows with staging_row=yes) + "
               "oe_pipeline (cascade_position, row order)") + [
        "Canonical SC-level historical staging map view for the Version 1 CAPR book.",
        "Rows are in executable cascade order (oe_pipeline).",
        "Book chapter/file order is the GENERATED registry/reader_manifest.tsv",
        "(sources: registry/reader_chapters.tsv + reader_files.tsv + oe_pipeline).",
        "Confidence: A=secure | B=strong but analysis-dependent | C=genuinely unresolved",
    ]
    return tsv_text(b, header, rows)


def read_reader_sources():
    chapters = read_tsv(READER_CHAPTERS)
    files = read_tsv(READER_FILES)
    return chapters, files


def build_reader_manifest(reg, chapters, files):
    """The generated Version 1 book manifest: one row per reader-facing file,
    in presentation order. Chapter membership is human (reader_files.tsv);
    chapter metadata is human (reader_chapters.tsv); order inside a chapter is
    DERIVED: files sort by the minimum cascade position of the SCs they
    contain (sc_registry.tsv source_reader_facing_file + oe_pipeline)."""
    errors = []
    chapter_meta = {}
    for c in chapters:
        if c["chapter_id"] in chapter_meta:
            errors.append(f"reader_chapters: duplicate chapter_id {c['chapter_id']}")
        chapter_meta[c["chapter_id"]] = c
        if not (SC_DIR / "reader_facing" / c["intro_file"]).is_file():
            errors.append(f"reader_chapters: chapter {c['chapter_id']} intro "
                          f"file missing: {c['intro_file']}")
    file_chapter = {}
    for f in files:
        if f["reader_file"] in file_chapter:
            errors.append(f"reader_files: duplicate reader_file {f['reader_file']}")
        if f["chapter_id"] not in chapter_meta:
            errors.append(f"reader_files: {f['reader_file']} names unknown "
                          f"chapter_id {f['chapter_id']}")
        file_chapter[f["reader_file"]] = f["chapter_id"]
        if not (SC_DIR / "reader_facing" / f["reader_file"]).is_file():
            errors.append(f"reader_files: missing reader file {f['reader_file']}")

    published = [r for r in reg if r["staging_row"] == "yes"
                 or (r["lifecycle_status"] == "active"
                     and r["entry_type"] == "support_stage"
                     and r["include_in_volume"] == "yes"
                     and r["is_reader_facing"] == "yes")]
    per_file = {}
    for r in published:
        fname = (r["source_reader_facing_file"] or "").strip()
        if not fname:
            errors.append(f"reader manifest: published SC {r['sc_id']} has no "
                          "source_reader_facing_file")
            continue
        if fname not in file_chapter:
            errors.append(f"reader manifest: {r['sc_id']} names file {fname} "
                          "absent from reader_files.tsv")
            continue
        pos = oe_pipeline.cascade_position(r["fst_identifier"])
        if pos is None:
            errors.append(f"reader manifest: published SC {r['sc_id']} has no "
                          "numbered cascade position")
            continue
        per_file.setdefault(fname, []).append((pos, r["sc_id"]))
    unused = sorted(set(file_chapter) - set(per_file))
    if unused:
        errors.append(f"reader_files: files with no published SC: {unused}")

    chapter_order = [c["chapter_id"] for c in chapters]
    ordered = sorted(
        per_file.items(),
        key=lambda kv: (chapter_order.index(file_chapter[kv[0]]),
                        min(p for p, _ in kv[1])))
    # Chapters must own contiguous cascade-position intervals, so ordering by
    # (chapter, min position) is the same as ordering by min position alone.
    mins = [min(p for p, _ in scs) for _, scs in ordered]
    if mins != sorted(mins):
        errors.append("reader manifest: chapter assignment breaks cascade "
                      f"order (file min positions {mins})")
    if len(mins) != len(set(mins)):
        errors.append("reader manifest: two reader files share the same "
                      "minimum cascade position")
    prev_max = None
    for cid in chapter_order:
        pos_in_ch = [p for fname, scs in per_file.items()
                     if file_chapter[fname] == cid for p, _ in scs]
        if not pos_in_ch:
            errors.append(f"reader manifest: chapter {cid} has no positioned SCs")
            continue
        if prev_max is not None and min(pos_in_ch) <= prev_max:
            errors.append(f"reader manifest: chapter {cid} overlaps the "
                          "previous chapter's cascade positions")
        prev_max = max(pos_in_ch)
    if errors:
        for e in errors:
            print(f"READER CONFIG ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)

    header = ["reader_order", "chapter_id", "chapter_title", "reader_file",
              "sc_ids", "min_cascade_position"]
    rows = []
    for i, (fname, scs) in enumerate(ordered, start=1):
        cid = file_chapter[fname]
        sc_ids = ";".join(sc for _, sc in sorted(scs))
        rows.append([str(i), cid, chapter_meta[cid]["title"], fname,
                     sc_ids, str(min(p for p, _ in scs))])
    b = banner("registry/reader_chapters.tsv + registry/reader_files.tsv "
               "(editorial) + registry/sc_registry.tsv + oe_pipeline "
               "(cascade positions)") + [
        "Version 1 book manifest: reader-facing files in presentation order.",
        "File order inside a chapter is DERIVED from the minimum executable",
        "cascade position of the SCs each file contains; never edit order here.",
        "The book builder (Germanic/tools/build_reader_book.py) consumes this",
        "manifest and contains no file list of its own.",
    ]
    return tsv_text(b, header, rows)


def build_current_chronology(reg, edges):
    """Generated current chronology view: the scholarly edge registry joined
    with today's executable positions. Replaces the retired live position
    column of the archival chronology card index."""
    ident_of = {r["sc_id"]: (r.get("fst_identifier") or "").strip() for r in reg}

    def position(change_id):
        ident = ident_of.get(change_id, change_id)
        if not ident:
            return ""
        try:
            pos = oe_pipeline.cascade_position(ident)
        except KeyError:
            return ""
        return "" if pos is None else str(pos)

    header = ["source_change_id", "target_change_id", "relation_type",
              "direction_basis", "evidence_basis", "witness_role",
              "source_cascade_position", "target_cascade_position"]
    rows = [
        [e["source_change_id"], e["target_change_id"], e["relation_type"],
         e["direction_basis"], e["evidence_basis"], e["witness_role"],
         position(e["source_change_id"]), position(e["target_change_id"])]
        for e in edges
    ]
    b = banner("registry/chronology_edges.tsv (scholarly relations) + "
               "registry/sc_registry.tsv + oe_pipeline (current positions)") + [
        "Current chronology view. Edge semantics are owned by",
        "chronology_edges.tsv; positions are DERIVED from germanic.txt and go",
        "stale the moment the cascade changes; regenerate, never edit.",
        "Archived first-break experiments live in order_tests/chronology_cards/",
        "(frozen in their original experiment order space).",
    ]
    return tsv_text(b, header, rows)


ANNOTATION_HEADER = [
    "change_id", "trace_stage", "rule_source_path", "rule_source_anchor",
    "foma_definition_raw", "plain_description_draft", "appears_in_compact_trace",
    "firing_count", "firing_lexemes", "illustrative_lexemes", "literature_status",
    "order_sensitivity_status", "notes", "review_note", "needs_human_review",
]


def build_annotation_rows(reg, notes):
    """Join human notes with the executable and corpus authorities.

    Nothing mechanical is read from a hand-edited file. The Foma definition
    and its anchor come from germanic.txt; the firing count and firing
    lexemes come from the canonical trace/census; the stage and literature
    status are renderings of registry columns.
    """
    facts = executable_facts.define_facts()
    firing = rule_coverage_census.load_firing_summary(
        rule_coverage_census.FULL_TRACE.read_text(encoding="utf-8"))
    reg_by_id = {r["sc_id"]: r for r in reg}
    rows = []
    for n in sorted(notes, key=lambda n: n["change_id"]):
        sc = n["change_id"]
        r = reg_by_id.get(sc)
        if r is None:
            raise SystemExit(f"inventory notes: unknown SC {sc}")
        ident = (r.get("fst_identifier") or "").strip()
        fact = facts.get(ident) if ident else None
        count, lexemes = firing.get(ident, (0, [])) if ident else (0, [])
        status = r["adjudication_status"]
        if status not in LITERATURE_STATUS:
            raise SystemExit(f"{sc}: unmapped adjudication_status {status!r}")
        rows.append([
            sc,
            r["pipeline_stage"],
            RULE_SOURCE_PATH if fact else "",
            fact.stable_anchor if fact else "",
            fact.definition_raw if fact else "",
            n["plain_description_draft"],
            "yes" if count else "no",
            str(count) if ident else "",
            ", ".join(dict.fromkeys(lexemes)),
            n["illustrative_lexemes"],
            LITERATURE_STATUS[status],
            n["order_sensitivity_status"],
            n["notes"], n["review_note"], n["needs_human_review"],
        ])
    return rows


def build_annotations_view(rows):
    b = banner(
        "registry/sc_registry.tsv + registry/sc_inventory_notes.tsv (human) "
        "joined with Germanic/fsts/germanic.txt and the coverage census (machine)"
    ) + [
        "",
        "rule_source_anchor is deliberately a STABLE anchor with no line number:",
        "inserting lines above a definition must not dirty any committed file.",
        "Run tools/executable_facts.py NAME for the current line.",
        "",
        "firing_count/firing_lexemes are the CURRENT corpus firing population",
        "(machine evidence). illustrative_lexemes are examples a human chose",
        "(editorial). The two are never interchangeable.",
    ]
    return tsv_text(b, ANNOTATION_HEADER, rows)


def build_inventory_view(reg, ann_rows):
    header = [
        "change_id", "display_name", "stage", "trace_stage",
        "rule_source_path", "rule_source_anchor", "foma_definition_raw",
        "plain_description_draft", "appears_in_compact_trace", "firing_count",
        "firing_lexemes", "illustrative_lexemes", "literature_status",
        "order_sensitivity_status", "notes",
        "entry_type", "include_in_volume", "historical_stage", "pipeline_stage",
        "canonical_change_id", "duplicate_group", "is_reader_facing", "review_note",
        "needs_human_review",
    ]
    ann_by_id = {row[0]: dict(zip(ANNOTATION_HEADER, row)) for row in ann_rows}
    rows = []
    for r in sorted(reg, key=lambda r: r["sc_id"]):
        a = ann_by_id.get(r["sc_id"])
        if a is None:
            continue  # SCs without an inventory row (e.g. retired SC021)
        display = r["inventory_display_name"] or r["display_name"]
        rows.append([
            r["sc_id"], display, r["stage_label"],
            a["trace_stage"], a["rule_source_path"], a["rule_source_anchor"],
            a["foma_definition_raw"], a["plain_description_draft"],
            a["appears_in_compact_trace"], a["firing_count"],
            a["firing_lexemes"], a["illustrative_lexemes"],
            a["literature_status"], a["order_sensitivity_status"],
            a["notes"], r["entry_type"], r["include_in_volume"],
            r["historical_stage_label"], r["pipeline_stage"], r["canonical_change_id"],
            r["duplicate_group"], r["is_reader_facing"], a["review_note"],
            a["needs_human_review"],
        ])
    b = banner(
        "registry/sc_registry.tsv + registry/sc_inventory_notes.tsv + "
        "germanic.txt + rule_coverage_census"
    ) + [
        "Rows are keyed by change_id. Executable positions come from",
        "oe_pipeline / cascade_order_manifest.tsv; the archival inventory",
        "order space is frozen in registry/archival_orders.tsv.",
    ]
    return tsv_text(b, header, rows)


def build_edges_tsv(edges):
    header = [
        "source_change_id", "target_change_id", "relation_type", "direction_basis",
        "representative_lexemes", "representative_forms", "strength",
        "interpretation_category", "reciprocal_group_id", "notes",
    ]
    rows = [[e[h] for h in header] for e in edges]
    return tsv_text(banner("registry/chronology_edges.tsv"), header, rows)


def node_rows(reg):
    rows = []
    for r in sorted(reg, key=lambda r: r["sc_id"]):
        if not r["chronology_card"]:
            continue
        rows.append({
            "change_id": r["sc_id"],
            "display_name": r["display_name"],
            "lifecycle_status": r["lifecycle_status"],
            "rule_name": r["fst_identifier"],
            "card_path": r["chronology_card"],
            "card_type": r["chronology_profile"],
            "has_reciprocal_boundary": r["chronology_has_reciprocal_boundary"],
            "short_summary": r["chronology_summary"],
        })
    return rows


def build_nodes_tsv(reg):
    header = [
        "change_id", "display_name", "lifecycle_status", "rule_name", "card_path",
        "card_type", "has_reciprocal_boundary", "short_summary",
    ]
    rows = [[n[h] for h in header] for n in node_rows(reg)]
    return tsv_text(
        banner("registry/sc_registry.tsv (rows with chronology-card facts)") + [
            "Executable positions are not repeated here; they come from",
            "oe_pipeline / cascade_order_manifest.tsv (see current_sc_state.tsv).",
        ], header, rows
    )


def build_edges_json(reg, edges):
    payload = {
        "generated_by": "Germanic/tools/generate_registry_views.py — GENERATED FILE, DO NOT EDIT",
        "order_note": (
            "nodes carry no order fields; executable order comes from oe_pipeline / "
            "cascade_order_manifest.tsv (see registry/current_sc_state.tsv)"
        ),
        "sources": [
            "Germanic/docs/sound_changes/registry/sc_registry.tsv",
            "Germanic/docs/sound_changes/registry/chronology_edges.tsv",
        ],
        "nodes": node_rows(reg),
        "edges": [
            {
                "source_change_id": e["source_change_id"],
                "target_change_id": e["target_change_id"],
                "relation_type": e["relation_type"],
                "direction_basis": e["direction_basis"],
                "evidence_basis": e["evidence_basis"],
                "witness_role": e["witness_role"],
                "representative_lexemes": e["representative_lexemes"],
                "representative_forms": e["representative_forms"],
                "strength": e["strength"],
                "interpretation_category": e["interpretation_category"],
                "reciprocal_group_id": e["reciprocal_group_id"],
                "notes": e["notes"],
            }
            for e in edges
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


EDGE_COLORS = {
    "reciprocal_chronology": "#2f855a",
    "near_reciprocal_chronology": "#2f855a",
    "one_sided_chronology": "#2b6cb0",
    "broad_far_chronology": "#2b6cb0",
    "runner_limited_boundary": "#c05621",
    "no_break_search_boundary": "#c05621",
    "technical_computational": "#718096",
}


def build_edges_dot(reg, edges):
    lines = [
        "// GENERATED FILE — DO NOT EDIT.",
        "// Source: registry/sc_registry.tsv + registry/chronology_edges.tsv",
        "// Generator: Germanic/tools/generate_registry_views.py",
        "digraph first_break_chronology {",
        "  rankdir=LR;",
        '  node [shape=box, style="rounded,filled", fillcolor="#ebf8ff", fontname="Helvetica"];',
    ]
    mentioned = set()
    for e in edges:
        mentioned.add(e["source_change_id"])
        mentioned.add(e["target_change_id"])
    for n in node_rows(reg):
        style = ""
        if n["lifecycle_status"] == "retired":
            style = ', fillcolor="#71809622", color="#718096"'
        lines.append(f'  "{n["change_id"]}" [label="{n["change_id"]}\\n{n["display_name"]}"{style}];')
    for name in sorted(mentioned):
        if not name.startswith("SC"):
            lines.append(f'  "{name}" [shape=ellipse, fillcolor="#faf089"];')
    for e in edges:
        color = EDGE_COLORS.get(e["relation_type"], "#4a5568")
        dashed = ", style=dashed" if e["relation_type"] not in CHRONOLOGY_RELATION_TYPES else ""
        lines.append(
            f'  "{e["source_change_id"]}" -> "{e["target_change_id"]}" '
            f'[label="{e["relation_type"]}", color="{color}", fontcolor="{color}"{dashed}];'
        )
    lines.append("}")
    return "\n".join(lines) + "\n"


def build_graph_summary(reg, edges):
    nodes = node_rows(reg)
    node_counts = Counter(n["card_type"] for n in nodes)
    edge_counts = Counter(e["relation_type"] for e in edges)
    lines = [
        "# First-break chronology graph summary",
        "",
        "GENERATED FILE — DO NOT EDIT. Source: `registry/sc_registry.tsv` +",
        "`registry/chronology_edges.tsv`. Generator:",
        "`Germanic/tools/generate_registry_views.py`.",
        "",
        "**Ordinary chronology** means a first-break relation between modeled",
        "sound-change rules. Runner-limited boundaries, no-break search",
        "boundaries and technical markers are diagnostic observations, not",
        "chronology constraints.",
        "",
        "## Totals",
        "",
        f"- total node count: `{len(nodes)}`",
        f"- total edge count: `{len(edges)}`",
        "",
        "### Node counts by card_type",
        "",
        "| card_type | count |",
        "| --- | ---: |",
    ]
    for k in sorted(node_counts):
        lines.append(f"| `{k}` | {node_counts[k]} |")
    lines += ["", "### Edge counts by relation_type", "", "| relation_type | count |", "| --- | ---: |"]
    for k in sorted(edge_counts):
        lines.append(f"| `{k}` | {edge_counts[k]} |")
    lines += ["", "## Chronology edges", ""]
    for e in edges:
        if e["relation_type"] not in CHRONOLOGY_RELATION_TYPES:
            continue
        lines.append(
            f"1. `{e['source_change_id']} -> {e['target_change_id']}` "
            f"({e['relation_type']}; {e['evidence_basis']}; witness role: {e['witness_role']}) — "
            f"lexemes: `{e['representative_lexemes']}`; forms: {e['representative_forms']}"
        )
    lines += ["", "## Boundary and technical observations", ""]
    for e in edges:
        if e["relation_type"] in CHRONOLOGY_RELATION_TYPES:
            continue
        lines.append(
            f"1. `{e['source_change_id']} -> {e['target_change_id']}` ({e['relation_type']})"
        )
    return "\n".join(lines) + "\n"


def build_settled_verdicts(reg):
    lines = [
        "# Settled adjudication verdicts",
        "",
        "GENERATED FILE — DO NOT EDIT. Source: `registry/sc_registry.tsv`.",
        "Generator: `Germanic/tools/generate_registry_views.py`.",
        "",
        "| SC | Display name | Lifecycle | Verdict | Memo |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in sorted(reg, key=lambda r: r["sc_id"]):
        if not r["verdict"]:
            continue
        lines.append(
            f"| {r['sc_id']} | {r['display_name']} | {r['lifecycle_status']} | "
            f"{r['verdict']} | `{r['adjudication_memo']}` |"
        )
    return "\n".join(lines) + "\n"


def build_current_sc_state(reg):
    """The generated current-state table: one row per active SC, joining the
    registry's human judgements with the executable model's derived order.
    This is the projection that replaces every retired hand-maintained
    position mirror (registry cascade_position column, live audit matrix)."""
    header = [
        "sc_id", "fst_identifier", "entry_type", "pipeline_stage",
        "display_name", "hist_stage", "hist_scope", "confidence",
        "adjudication_status", "verdict", "exec_index", "cascade_position",
    ]
    rows = []
    for r in reg:
        if r["lifecycle_status"] != "active":
            continue
        ident = (r.get("fst_identifier") or "").strip()
        exec_index = cascade_pos = ""
        if ident:
            stage = oe_pipeline.stage_for(ident)
            exec_index = str(stage.exec_index)
            if stage.cascade_position is not None:
                cascade_pos = str(stage.cascade_position)
        rows.append([
            r["sc_id"], ident, r["entry_type"], r["pipeline_stage"],
            r["display_name"], r["hist_stage"], r["hist_scope"], r["confidence"],
            r["adjudication_status"], r["verdict"], exec_index, cascade_pos,
        ])
    rows.sort(key=lambda row: (row[10] == "", int(row[10] or 0), row[0]))
    b = banner("registry/sc_registry.tsv (human judgements) + oe_pipeline "
               "(exec_index/cascade_position from germanic.txt)") + [
        "Current SC state projection. Positions here are DERIVED and go stale the",
        "moment germanic.txt changes; regenerate, never edit. An empty",
        "cascade_position means the stage executes outside the numbered span",
        "(prelude or written-surface block); an empty exec_index means the SC has",
        "no executable stage.",
    ]
    return tsv_text(b, header, rows)


def build_all():
    reg = read_tsv(SC_REGISTRY)
    notes = read_tsv(INVENTORY_NOTES)
    edges = read_tsv(EDGE_REGISTRY)
    chapters, files = read_reader_sources()
    errors = validate_registry(reg, edges)
    errors += validate_human_sources(notes)
    if errors:
        for e in errors:
            print(f"REGISTRY ERROR: {e}", file=sys.stderr)
        raise SystemExit(1)
    ann_rows = build_annotation_rows(reg, notes)
    return {
        ANNOTATIONS: build_annotations_view(ann_rows),
        CURRENT_SC_STATE: build_current_sc_state(reg),
        STAGING_VIEW: build_staging_view(reg),
        READER_MANIFEST: build_reader_manifest(reg, chapters, files),
        CURRENT_CHRONOLOGY: build_current_chronology(reg, edges),
        INVENTORY_VIEW: build_inventory_view(reg, ann_rows),
        EDGES_TSV: build_edges_tsv(edges),
        EDGES_JSON: build_edges_json(reg, edges),
        EDGES_DOT: build_edges_dot(reg, edges),
        NODES_TSV: build_nodes_tsv(reg),
        GRAPH_SUMMARY: build_graph_summary(reg, edges),
        SETTLED_VERDICTS: build_settled_verdicts(reg),
    }


def main() -> int:
    check = "--check" in sys.argv[1:]
    outputs = build_all()
    dirty = []
    for path, text in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        if check:
            dirty.append(path)
        else:
            path.write_text(text, encoding="utf-8")
            print(f"wrote {path.relative_to(REPO_ROOT)}")
    if check:
        if dirty:
            for p in dirty:
                print(f"STALE VIEW: {p.relative_to(REPO_ROOT)} does not match its sources", file=sys.stderr)
            return 1
        print("all generated views are clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
