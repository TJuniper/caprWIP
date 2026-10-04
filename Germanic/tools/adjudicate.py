#!/usr/bin/env python3
"""Narrow adjudication interface for one SC.

    python3 Germanic/tools/adjudicate.py --next
        Report the next SC to adjudicate, derived from the canonical
        registry and explicit programme start (first pending historical
        change in the programme, excluding technical support stages).

    python3 Germanic/tools/adjudicate.py SC024 --prepare
        Assemble a compact packet from canonical sources: registry row, rule
        text and executable position, chronology relations and witnesses,
        an explicit registry-driven reading list (required sources, existing
        adjudication, chronology evidence, publication prose, historical
        support), frozen fingerprints, and the standard commands.

    python3 Germanic/tools/adjudicate.py --refresh
        Control-plane refresh: bring EVERY generated artifact up to date
        from its authority via the unified artifact graph
        (Germanic/tools/artifact_graph.py) — executable-order projections,
        generated sandbox, registry views, coverage census, reader book,
        book draft, index verborum, and (only when their recorded input
        provenance shows them stale) the runtime evidence: stage bins,
        canonical full trace, interaction matrix. Ends with
        'CONTROL PLANE CLEAN' or one actionable authority-tied error.
        This is the ONE command to run after any SOURCE edit, including
        rule moves. May also be invoked as 'SCNNN --refresh'.

    python3 Germanic/tools/adjudicate.py SC024 --evidence
        Deterministically gather the executable (runtime) evidence: run the
        control-plane refresh with an unconditional stage-bin rebuild
        (fsts/old_english_sandbox.txt inside the backend container, build
        manifest, production-vs-sandbox semantic equivalence, canonical
        full trace when stale), then print the complete live firing census
        for the SC's executable rule (lexeme, protoform, form immediately
        before the rule, form immediately after), plus before/after lines
        for the SC's chronology witnesses. No manual foma/flookup work is
        ever needed.

    python3 Germanic/tools/adjudicate.py SC024 --finalize
        Control-plane refresh plus the SC-specific propagation checks.
        Never fabricates runtime evidence (the census fails closed on stale
        trace evidence) and never rewrites ARCHIVE/FROZEN snapshots. Run
        after editing SOURCE files.

    python3 Germanic/tools/adjudicate.py SC024 --check
        Validate propagation consistency only (no regeneration): SC
        metadata checks plus a non-mutating freshness check of every
        artifact-graph node.

    python3 Germanic/tools/adjudicate.py SC033 --adopt-cell-baseline
        Evaluate fresh container runtime bins and apply only the exact
        approved_cell_migration.json transition. Preserve the previous
        baseline bytes and immutable legacy identities; reject all
        undeclared record, output, multiplicity and context drift.
        Routine refresh/finalize never adopts a baseline.

Canonical sources read: registry/sc_registry.tsv, registry/chronology_edges.tsv,
registry/sc_inventory_notes.tsv, Germanic/fsts/germanic.txt,
cascade_baseline/cascade_order_manifest.tsv,
cascade_baseline/cascade_baseline_summary.json. Archives are not current
scientific authority; explicit baseline adoption reads and protects them.
"""

from __future__ import annotations

import json
import re
import shlex
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic/tools"))

from generate_registry_views import (  # noqa: E402
    ANNOTATIONS,
    EDGE_REGISTRY,
    SC_REGISTRY,
    VERDICT_VOCABULARY,
    read_tsv,
)

import artifact_graph  # noqa: E402
from capr_runtime import run_in_runner  # noqa: E402
import cascade_baseline  # noqa: E402

SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
FST = REPO_ROOT / "Germanic/fsts/germanic.txt"
SANDBOX_FST = REPO_ROOT / "Germanic/fsts/old_english_sandbox.txt"
# Runtime layout (authoritative bin dir, runner) comes from capr_runtime.
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
BASELINE_SUMMARY = SC_DIR / "cascade_baseline/cascade_baseline_summary.json"
TEMPLATE = SC_DIR / "audits/ADJUDICATION_TEMPLATE.md"
PROTOCOL = REPO_ROOT / "Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md"
PROGRAMME = SC_DIR / "registry/adjudication_programme.json"
# ONE artifact graph (Germanic/tools/artifact_graph.py) owns every generated
# artifact: its authority, freshness check and builder. There are no other
# builder lists. ARCHIVE/FROZEN artifacts (historical_audit_table.tsv,
# rename_migration_manifest.tsv) are deliberately NOT in the graph: frozen
# snapshots are never rewritten.

# Canonical directories in which bare-filename registry pointers may live.
DOC_SEARCH_DIRS = (
    SC_DIR / "audits",
    SC_DIR / "book_dossiers",
    SC_DIR / "literature_dossiers",
    SC_DIR / "reader_facing",
    SC_DIR / "order_tests/chronology_cards",
    REPO_ROOT / "Germanic/docs",
    SC_DIR,
)

VERDICT_LINE_RE = re.compile(r"^Registry-verdict:\s*(.+)$", re.MULTILINE)


def load_registry_row(sc_id):
    for row in read_tsv(SC_REGISTRY):
        if row["sc_id"] == sc_id:
            return row
    return None


def load_annotation_row(sc_id):
    for row in read_tsv(ANNOTATIONS):
        if row["change_id"] == sc_id:
            return row
    return None


def find_rule(fst_identifier):
    if not fst_identifier:
        return None, None
    for lineno, line in enumerate(FST.read_text(encoding="utf-8").splitlines(), 1):
        if re.match(rf"\s*define\s+{re.escape(fst_identifier)}\b", line):
            return lineno, line.strip()
    return None, None


def edges_for(sc_id):
    return [
        e
        for e in read_tsv(EDGE_REGISTRY)
        if sc_id in (e["source_change_id"], e["target_change_id"])
    ]


def resolve_doc(ref):
    """Resolve one registry document pointer to a repo-relative Path.

    A pointer containing '/' is repo-relative; a bare filename is looked up
    in the canonical document directories. Returns None if unresolvable.
    """
    ref = ref.strip()
    if not ref:
        return None
    if "/" in ref:
        p = REPO_ROOT / ref
        return p.relative_to(REPO_ROOT) if p.is_file() else None
    for d in DOC_SEARCH_DIRS:
        p = d / ref
        if p.is_file():
            return p.relative_to(REPO_ROOT)
    return None


def split_refs(value):
    return [part.strip() for part in value.split(";") if part.strip()]


def reading_list(row, ann):
    """Build the registry-driven reading list for one SC.

    Returns (sections, warnings) where sections is an ordered dict of
    section title -> list of repo-relative path strings, and warnings lists
    registry pointers that failed to resolve. No filename guessing: every
    entry comes from an explicit canonical registry/annotation field.
    """
    sections = {
        "REQUIRED CURRENT SOURCES": [],
        "EXISTING ADJUDICATION": [],
        "CHRONOLOGY EVIDENCE": [],
        "PUBLICATION PROSE (inspect/update after verdict)": [],
        "OPTIONAL / HISTORICAL SUPPORT": [],
    }
    warnings = []

    def add(section, ref):
        p = resolve_doc(ref)
        if p is None:
            warnings.append(f"unresolvable registry pointer: {ref!r}")
            return
        s = str(p)
        if s not in sections[section]:
            sections[section].append(s)

    if ann and ann.get("rule_source_path"):
        anchor = ann.get("rule_source_anchor", "")
        entry = ann["rule_source_path"] + (f"  ({anchor})" if anchor else "")
        sections["REQUIRED CURRENT SOURCES"].append(entry)
    for ref in split_refs(row.get("capr_evidence", "")):
        p = resolve_doc(ref)
        if p is None:
            warnings.append(f"unresolvable registry pointer: {ref!r}")
            continue
        parent = p.parts[-2] if len(p.parts) > 1 else ""
        if parent == "literature_dossiers":
            section = "OPTIONAL / HISTORICAL SUPPORT"
        elif parent in ("book_dossiers", "reader_facing"):
            section = "PUBLICATION PROSE (inspect/update after verdict)"
            # Grouped book dossiers are also primary CAPR evidence.
            if str(p) not in sections["REQUIRED CURRENT SOURCES"]:
                sections["REQUIRED CURRENT SOURCES"].append(str(p))
        else:
            section = "REQUIRED CURRENT SOURCES"
        if str(p) not in sections[section]:
            sections[section].append(str(p))
    if row.get("adjudication_memo"):
        add("EXISTING ADJUDICATION", row["adjudication_memo"])
    if row.get("chronology_card"):
        add("CHRONOLOGY EVIDENCE", row["chronology_card"])
    if row.get("source_reader_facing_file"):
        add("PUBLICATION PROSE (inspect/update after verdict)",
            row["source_reader_facing_file"])
    return sections, warnings


def sc_num(sc_id):
    return int(sc_id[2:5])


def next_sc():
    """First pending historical change at or after the explicit programme start.

    Scoped verdicts cannot advance past earlier pending work. Programme
    order is an administrative SC-ID sequence, not executable or historical order.
    """
    rows = read_tsv(SC_REGISTRY)
    policy = json.loads(PROGRAMME.read_text(encoding="utf-8"))
    if (not isinstance(policy, dict) or set(policy) != {"start_sc"}
            or not isinstance(policy["start_sc"], str)
            or not re.fullmatch(r"SC\d{3}", policy["start_sc"])):
        raise ValueError(f"{PROGRAMME}: expected exactly one start_sc (SCNNN)")
    start = policy["start_sc"]
    if not any(r["sc_id"] == start for r in rows):
        raise ValueError(f"{PROGRAMME}: programme start {start} is not registered")
    pending = sorted(
        (sc_num(r["sc_id"]), r["sc_id"])
        for r in rows
        if r["lifecycle_status"] == "active"
        and r["adjudication_status"] != "adjudicated"
        and r["entry_type"] != "support_stage"
        and sc_num(r["sc_id"]) >= sc_num(start)
    )
    return pending[0][1] if pending else None


def refresh() -> int:
    """Control-plane refresh: drive the ONE artifact graph to a clean state."""
    print("== control-plane refresh (artifact graph) ==")
    try:
        artifact_graph.refresh()
    except artifact_graph.GraphError as exc:
        print(f"REFRESH FAILED: {exc}", file=sys.stderr)
        return 1
    problems = artifact_graph.verify_all()
    if problems:
        for p in problems:
            print(f"STALE AFTER REFRESH: {p}", file=sys.stderr)
        return 1
    print("CONTROL PLANE CLEAN")
    return 0


def evidence(sc_id) -> int:
    """Deterministically gather the executable evidence for one SC.

    Fails loudly at every step; never falls back to stale artifacts.
    """
    row = load_registry_row(sc_id)
    if row is None:
        print(f"{sc_id} not found in {SC_REGISTRY.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    ident = row["fst_identifier"]
    if not ident:
        print(f"EVIDENCE FAILED: {sc_id} has no executable fst_identifier in the "
              f"registry (lifecycle: {row['lifecycle_status']}); there is no live "
              "rule to census.", file=sys.stderr)
        return 1
    edges = edges_for(sc_id)
    witnesses = "; ".join(
        w for e in edges for w in split_refs(e["representative_lexemes"]))

    print(f"# Executable evidence: {sc_id} ({ident})")
    print("\n## Chronology relations and witnesses (canonical edge registry)")
    if not edges:
        print("- none recorded")
    for e in edges:
        print(f"- {e['source_change_id']} -> {e['target_change_id']} "
              f"[{e['relation_type']}; {e['evidence_basis']}; "
              f"role: {e['witness_role'] or '-'}]")
        if e["representative_lexemes"]:
            print(f"  witnesses: {e['representative_lexemes']}")
        if e["representative_forms"]:
            print(f"  forms: {e['representative_forms']}")

    if not SANDBOX_FST.is_file():
        print(f"EVIDENCE FAILED: missing {SANDBOX_FST}", file=sys.stderr)
        return 1
    try:
        clock = run_in_runner("date +%s", capture_output=True, text=True)
    except RuntimeError as exc:
        print(f"EVIDENCE FAILED: {exc}", file=sys.stderr)
        return 1
    if clock.returncode != 0:
        print(clock.stderr, file=sys.stderr)
        print("EVIDENCE FAILED: backend container is not reachable "
              "(is `docker compose up -d` running?)", file=sys.stderr)
        return 1
    min_mtime = int(clock.stdout.strip())

    # Control-plane refresh with an unconditional stage-bin rebuild: the
    # graph regenerates the mechanical projections, rebuilds the full OE
    # cascade + stage bins in the container (writing the build manifest and
    # proving production/sandbox equivalence), regenerates the canonical
    # full trace only when its recorded provenance is stale, and brings
    # every downstream projection up to date.
    print("\n## Control-plane refresh (forced stage-bin rebuild) ...")
    sys.stdout.flush()
    try:
        artifact_graph.refresh(force=frozenset({"runtime_bins"}))
    except artifact_graph.GraphError as exc:
        print(f"EVIDENCE FAILED: {exc}", file=sys.stderr)
        return 1
    stale = artifact_graph.verify_all()
    if stale:
        for s in stale:
            print(f"EVIDENCE FAILED (stale after refresh): {s}", file=sys.stderr)
        return 1

    print("\n## Firing census (fresh stage bins only)")
    sys.stdout.flush()
    inner = f"python3 tools/sc_evidence.py {shlex.quote(ident)} --min-mtime {min_mtime}"
    if witnesses:
        inner += f" --witnesses {shlex.quote(witnesses)}"
    census = run_in_runner(inner)
    if census.returncode != 0:
        print(f"EVIDENCE FAILED: census exited {census.returncode}", file=sys.stderr)
        return 1
    return 0


def prepare(sc_id) -> int:
    row = load_registry_row(sc_id)
    if row is None:
        print(f"{sc_id} not found in {SC_REGISTRY.relative_to(REPO_ROOT)}", file=sys.stderr)
        return 1
    print(f"# Adjudication packet: {sc_id}")
    print(f"\n## Protocol\nFollow {PROTOCOL.relative_to(REPO_ROOT)} and fill "
          f"{TEMPLATE.relative_to(REPO_ROOT)} (copy to "
          f"Germanic/docs/sound_changes/audits/{sc_id.lower()}-adjudication.md).")
    print("\n## Registry row (canonical metadata)")
    for key, value in row.items():
        if value:
            print(f"- {key}: {value}")
    print("\n## Executable rule")
    lineno, text = find_rule(row["fst_identifier"])
    if lineno:
        print(f"- {row['fst_identifier']} at Germanic/fsts/germanic.txt line {lineno}:")
        print(f"  {text}")
        manifest = {r["foma_identifier"]: r["position"] for r in read_tsv(ORDER_MANIFEST)}
        pos = manifest.get(row["fst_identifier"])
        if pos:
            print(f"- executable cascade position (order manifest): {pos}")
    else:
        print(f"- no live `define {row['fst_identifier'] or '?'}` in germanic.txt "
              f"(lifecycle: {row['lifecycle_status']})")
    print("\n## Chronology relations (canonical edge registry)")
    edges = edges_for(sc_id)
    if not edges:
        print("- none recorded")
    for e in edges:
        print(f"- {e['source_change_id']} -> {e['target_change_id']} "
              f"[{e['relation_type']}; {e['evidence_basis']}; role: {e['witness_role'] or '-'}] "
              f"lexemes: {e['representative_lexemes'] or '-'}")
    print("\n## Reading list (registry-driven; no repository searching needed)")
    sections, warnings = reading_list(row, load_annotation_row(sc_id))
    for title, entries in sections.items():
        print(f"\n### {title}")
        if not entries:
            print("- (none recorded)")
        for entry in entries:
            print(f"- {entry}")
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    print("\n## Frozen fingerprints (observations, not goals)")
    summary = json.loads(BASELINE_SUMMARY.read_text(encoding="utf-8"))
    print(f"- expanded-{summary['total_lexemes']}: {summary['outputs_sha256']}")
    print(f"- legacy-{summary['legacy_subset_count']}: {summary['legacy_subset_sha256']}")
    print("\n## Standard commands")
    print(f"- executable evidence (rebuild + firing census): "
          f"python3 Germanic/tools/adjudicate.py {sc_id} --evidence")
    print(f"- finalize after SOURCE edits: python3 Germanic/tools/adjudicate.py {sc_id} --finalize")
    print("- full suite: cd Germanic/tests && python3 -m pytest -q")
    print("All container FST work (rebuild, freshness checks, firing census, "
          "witness pre/post) is encapsulated by --evidence; never compile or "
          "probe transducers by hand.")
    return 0


def finalize(sc_id) -> int:
    """Control-plane refresh plus SC-specific propagation checks.

    The agent never decides which builders to run: the artifact graph owns
    every generated artifact and regenerates whatever is stale. Runtime
    evidence is never fabricated here — runtime nodes rebuild only when
    their recorded input provenance shows them stale, and the coverage
    census fails closed on stale trace evidence. ARCHIVE/FROZEN snapshots
    are never rewritten.
    """
    rc = refresh()
    if rc:
        return rc
    print("== propagation checks ==")
    return check(sc_id)


def check(sc_id) -> int:
    errors = []
    row = load_registry_row(sc_id)
    if row is None:
        print(f"{sc_id} not found in registry", file=sys.stderr)
        return 1
    if row["adjudication_status"] != "adjudicated":
        errors.append(f"registry adjudication_status is {row['adjudication_status']!r}, not 'adjudicated'")
    verdict = row["verdict"]
    if not verdict:
        errors.append("registry verdict is empty")
    else:
        for token in verdict.split("/"):
            if token not in VERDICT_VOCABULARY:
                errors.append(f"verdict token {token!r} not in controlled vocabulary")
    memo_rel = row["adjudication_memo"]
    if not memo_rel:
        errors.append("registry adjudication_memo is empty")
    else:
        memo_path = REPO_ROOT / memo_rel
        if not memo_path.is_file():
            errors.append(f"memo missing: {memo_rel}")
        else:
            text = memo_path.read_text(encoding="utf-8")
            match = VERDICT_LINE_RE.search(text)
            if not match:
                errors.append(f"memo {memo_rel} has no 'Registry-verdict:' line")
            else:
                declared = dict(
                    part.split("=", 1)
                    for part in (p.strip() for p in match.group(1).split(";"))
                    if "=" in part
                )
                if declared.get(sc_id) != verdict:
                    errors.append(
                        f"memo Registry-verdict {declared.get(sc_id)!r} != registry verdict {verdict!r}"
                    )
    if "RETIRE" in (verdict or ""):
        if row["lifecycle_status"] != "retired":
            errors.append("verdict RETIRE but lifecycle_status is not 'retired'")
    if row["lifecycle_status"] == "retired":
        lineno, _ = find_rule(row["fst_identifier"])
        if lineno:
            errors.append(
                f"retired SC still has a live define {row['fst_identifier']} "
                f"at germanic.txt line {lineno}"
            )
    # the registry never stores positions; the executable model owns them,
    # and stale projections are caught by the artifact-graph check below
    # every generated artifact must be fresh (non-mutating graph check)
    errors.extend(artifact_graph.verify_all())
    if errors:
        for e in errors:
            print(f"CHECK FAILED: {e}", file=sys.stderr)
        return 1
    print(f"{sc_id}: propagation checks passed. Remember: cd Germanic/tests && python3 -m pytest -q")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if len(args) == 2 and args[1] in {"--adopt-context-baseline", "--adopt-cell-baseline"}:
        cell_migration = args[1] == "--adopt-cell-baseline"
        approval_path = BASELINE_SUMMARY.with_name(
            "approved_cell_migration.json" if cell_migration else "approved_context_migration.json"
        )
        approval = json.loads(approval_path.read_text(encoding="utf-8"))
        if args[0] != approval["adjudication"]:
            print("BASELINE FAILED: command does not name the approved adjudication", file=sys.stderr)
            return 2
        code = (
            "import sys,json;sys.path.insert(0,'tools');"
            "from pathlib import Path;"
            "from capr_runtime import layout,check_build_manifest;"
            "from cascade_baseline import build_baseline;"
            "import oe_pipeline;"
            "rt=layout();"
            "errors=check_build_manifest(oe_pipeline.expected_snapshot_bins()+['old_english.bin'],rt);\n"
            "if errors: raise RuntimeError('; '.join(errors))\n"
            "print(json.dumps(build_baseline(rt.corpus_tsv,rt.bin_dir/'old_english.bin')))"
        )
        result = run_in_runner("python3 -c " + shlex.quote(code),
                               capture_output=True, text=True)
        if result.returncode:
            print("BASELINE FAILED: " + result.stderr.strip(), file=sys.stderr)
            return 1
        try:
            adopter = (
                cascade_baseline.adopt_cell_baseline if cell_migration
                else cascade_baseline.adopt_context_baseline
            )
            adopter(
                json.loads(result.stdout), BASELINE_SUMMARY.parent, approval,
            )
        except (OSError, ValueError, KeyError) as exc:
            print("BASELINE FAILED: " + str(exc), file=sys.stderr)
            return 1
        print("Approved paradigm-cell baseline adopted; archived identities remain protected."
              if cell_migration else
              "Approved context baseline adopted; lexical finals and both legacy protections unchanged.")
        return 0
    if args == ["--next"]:
        try:
            nxt = next_sc()
        except (OSError, ValueError) as exc:
            print(f"QUEUE FAILED: {exc}", file=sys.stderr)
            return 2
        if nxt is None:
            print("no pending active historical change remains in the adjudication programme")
            return 1
        print(nxt)
        return 0
    if args == ["--refresh"]:
        return refresh()
    if (len(args) != 2
            or args[1] not in ("--prepare", "--check", "--finalize",
                               "--evidence", "--refresh")
            or not re.fullmatch(r"SC\d{3}", args[0])):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    sc_id, mode = args
    if mode == "--prepare":
        return prepare(sc_id)
    if mode == "--evidence":
        return evidence(sc_id)
    if mode == "--finalize":
        return finalize(sc_id)
    if mode == "--refresh":
        return refresh()
    return check(sc_id)


if __name__ == "__main__":
    raise SystemExit(main())
