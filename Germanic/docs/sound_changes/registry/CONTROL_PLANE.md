# Germanic control plane — SOURCE / GENERATED / ARCHIVE map

Classification of every file that encodes machine-relevant sound-change
state. Rule: for each fact there is exactly one editable SOURCE; everything
else is GENERATED from it or ARCHIVE. Never hand-edit a GENERATED file;
never treat an ARCHIVE file as current authority.

## SOURCE (hand-edited, authoritative)

Three kinds: **machine-state** (structured facts), **scientific-reasoning**
(adjudication memos), **publication-prose** (reader-facing text). All others
are GENERATED or ARCHIVE.

| File | Kind | Owns |
|---|---|---|
| `registry/sc_registry.tsv` | machine-state | SC identity, lifecycle status, executable identifier, display names, historical stage/scope, confidence, adjudication status/verdict, memo path, document pointers (evidence dossiers, chronology card, reader-facing chapter). It carries NO order-valued columns: executable positions are derived at read time from the executable model (`tools/oe_pipeline.py`) and published in the generated `registry/current_sc_state.tsv`; the legacy inventory/staging order spaces are frozen in `registry/archival_orders.tsv` (ARCHIVE) |
| `registry/chronology_edges.tsv` | machine-state | Chronology relations: relation type, evidence basis (stage-entailed vs independently demonstrated), witnesses, witness roles |
| `registry/adjudication_programme.json` | machine-state | Explicit administrative programme start (`start_sc`). `adjudicate.py --next` selects the first active, unadjudicated non-support entry at or above it in SC-ID order. Scoped verdicts never skip pending earlier work. This is neither historical chronology nor executable order; earlier cases and support stages remain explicitly addressable |
| `registry/reader_chapters.tsv` | machine-state | Reader book chapters: chapter id, title, intro file. Chapter order is the chapter id |
| `registry/reader_files.tsv` | machine-state | Reader file -> chapter assignment (one row per reader-facing chapter file; no order column — book order is derived from cascade position) |
| `registry/sc_inventory_notes.tsv` | source | HUMAN JUDGEMENTS ONLY: plain-language draft descriptions, order-sensitivity classification, editorial `illustrative_lexemes`, notes, review flags |
| `registry/sc_inventory_annotations.tsv` | GENERATED | Projection joining the two human sources with `germanic.txt` (definition text, stable anchor) and the coverage census (`firing_count`, `firing_lexemes`). Never hand-edit |
| `Germanic/fsts/germanic.txt` | machine-state | Executable rule semantics and cascade composition |
| `audits/*.md` adjudication memos | scientific-reasoning | Per-SC scientific reasoning; each carries a machine-readable `Registry-verdict:` line that must agree with the registry |
| `reader_facing/*.md`, `book_dossiers/*.md` | publication-prose | Reader-facing chapters and grouped book dossiers; `adjudicate.py SCNNN --prepare` lists the ones relevant to a given SC |
| `cascade_baseline/cascade_baseline_summary.json` | machine-state | Frozen fingerprints (change only via the explicit adjudication/refreeze procedure) |
| `cascade_baseline/approved_input_migrations.tsv` | machine-state | Exact approved old/new selected input, counterpart and output by stable OE row ID and concept, with adjudication pointer. Gift changes input only; knee changes its selected paradigm cell. All undeclared output/multiplicity drift and archival rewrites remain forbidden |
| `Germanic/data/entry_context_metadata.tsv` | machine-state | Separately sourced selected sentence stress/finality at SC098; never changes PROTO/PROTOFORM or infers stress from accent |
| `backend/oe_input_context.py` | executable source | Shared context validation/assembly and annotation-free, selected-context API projections |
| `cascade_baseline/approved_context_migration.json` | machine-state | Exact approved evaluator-input delta and independent evaluator/lexical/legacy fingerprints. Applied only by `adjudicate.py SC098 --adopt-context-baseline`, never routine refresh |
| `cascade_baseline/approved_cell_migration.json` | machine-state | Exact approved before/after fields for a selected paradigm-cell transition. `adjudicate.py SC033 --adopt-cell-baseline` preserves the pre-transition baseline and verifies every record, summary projection and legacy archive; routine refresh never adopts it |
| `Germanic/docs/CURRENT_STATE.md` | publication-prose | Current phase and standard commands (the next SC is derived: `adjudicate.py --next`) |
| `Germanic/docs/README.md`, `sound_changes/README.md` | publication-prose | Navigation |
| `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md`, `audits/ADJUDICATION_TEMPLATE.md` | publication-prose | Method |

Registry document pointers (`capr_evidence`, `chronology_card`,
`source_reader_facing_file`, `adjudication_memo`) are either repo-relative
paths or bare filenames resolved against the canonical document directories;
`--prepare` builds the reading list exclusively from these fields (no
filename guessing), and a test requires every pointer to resolve.

## GENERATED (never hand-edit; rebuilt by `adjudicate.py --refresh`)

ONE unified artifact graph (`tools/artifact_graph.py`) owns every generated
artifact: its authority, a non-mutating freshness check, and its builder.
`adjudicate.py --refresh` (also run by `--finalize`) drives the graph to a
clean state and prints `CONTROL PLANE CLEAN`; `--check` verifies every node
without mutating anything. No other builder list exists, and no workflow
step ever hand-picks generators. Any stale-artifact error says to run the
control-plane refresh.

The reader and lexical sources precede the combined draft. Draft/index
projections converge together because the draft injects the generated index
commands; newly assembled lexical material must not leave a stale draft after
the index is rebuilt. Order-sensitivity crossings identify newly registered
stages from the live registry even when those stages have no frozen archival
inventory ordinal; no archival positions are invented for them.

| File | Source |
|---|---|
| `registry/current_sc_state.tsv` | sc_registry + oe_pipeline (the ONLY current-position table) |
| `registry/reader_manifest.tsv` | reader_chapters + reader_files + sc_registry + oe_pipeline: staged laws plus active support stages explicitly marked include_in_volume=yes/is_reader_facing=yes, without inventing historical staging (book order = min cascade position per file; chapters must be contiguous) |
| `registry/current_chronology.tsv` | chronology_edges + sc_registry + oe_pipeline (edges projected onto current cascade positions) |
| `sound_change_historical_staging_map.tsv` | sc_registry + oe_pipeline (row order and `cascade_position`) |
| `sound_change_inventory.tsv` | sc_registry + annotations |
| `order_tests/chronology_graph/first_break_edges.{tsv,json,dot}` | chronology_edges (+ registry for node metadata) |
| `order_tests/chronology_graph/first_break_nodes.tsv` | sc_registry |
| `order_tests/chronology_graph/first_break_graph_summary.md` | both registries |
| `registry/settled_verdicts.md` | sc_registry |
| `reader_facing/reader_facing_local_section_20.md`, `reader_facing/reader_facing_manifest_coverage_08.md` | `tools/build_reader_book.py` (reader_manifest + reader_chapters + chapter files) |
| `cascade_baseline/cascade_order_manifest.tsv`, `cascade_baseline/executable_model.tsv` | `tools/cascade_order_manifest.py` (oe_pipeline projection) |
| `Germanic/fsts/old_english_sandbox.txt` | `tools/generate_oe_sandbox.py` (oe_pipeline projection) |
| `cascade_baseline/rule_coverage_census.tsv` | `tools/rule_coverage_census.py` (fails closed if the canonical trace evidence is stale — the refresh rebuilds the trace first) |
| `docs/assembly/capr_book_draft_alpha_01.md` | `docs/assembly/build_capr_book_draft.py` |
| `debug_snapshots/oe_derivation_class_trace_report.{txt,compact.md}`, `docs/assembly/manifest_*.tsv`, `manifest_summary.md`, `lexical_volume_alpha_01.md`, `lexical_source_provenance.json` | `lexical_sources` node: pure projection of the fresh canonical full trace + corpus + model entries + entry-stage sidecar, via existing compact/manifest/assembly builders. Input and output digests prevent stale lexical histories from silently entering the book |
| `docs/book/index_verborum_*` + `docs/assembly/book_draft_index_registry.tex` | `tools/build_index_verborum.py` |

Runtime evidence (container-built; the graph rebuilds these ONLY when their
recorded input provenance shows them stale, so a no-op refresh never touches
Docker):

| Artifact | Provenance record |
|---|---|
| stage bins (`backend/*.bin`) + `backend/oe_build_manifest.json` | source hashes in the build manifest (`tools/capr_runtime.py`) |
| `debug_snapshots/oe_full_trace_report.txt` | PROVENANCE block checked by `oe_full_trace_report.trace_provenance_problems` |
| `cascade_baseline/cascade_interaction_matrix.tsv` | `cascade_baseline/cascade_interaction_provenance.json` — hash over harness source, the stage-derived pair list, and the executable_facts definition closure of every participating network. Pure cascade reorders do not invalidate the matrix; editing a participating rule does. The matrix is CURRENT-STATE analysis, not a frozen snapshot |

The standard reader, full lexical-volume and combined-book shell entry
points run the canonical `adjudicate.py --refresh` before their checks or
rendering. Thus direct publication also validates runtime/trace provenance
and regenerates lexical manifests, compact traces and the joint draft/index
projection. A failed refresh stops publication; a no-op refresh does not
recompile the FST. The graph's builders do not invoke these render wrappers.

## ARCHIVE / RECORD (historical; never current authority)

- `cascade_baseline/historical_partial_order.tsv` preserves the old
  Phase-3 constraint snapshot, including the superseded late ww proxy.
  Current independently supported interaction constraints come from
  `registry/chronology_edges.tsv`, not that snapshot.
- `cascade_baseline/cascade_baseline_outputs_legacy380.tsv` remains the immutable
  original 380-identity snapshot. Its archive digest is distinct from the active
  legacy-subset digest after an approved input migration.
- `cascade_baseline/cascade_baseline_{outputs,summary}_pre_sc031_sc098.*`
  preserve the selected387 baseline before the approved context transition;
  refresh and finalization protect them against mutation.
- `cascade_baseline/cascade_baseline_outputs_pre_sc056.tsv` and
  `cascade_baseline_summary_pre_sc056.json` preserve the selected387 state before
  the gift/ordinary-PD adjudication; never refreshed or repointed.
- `cascade_baseline/historical_audit_table.tsv` and
  `cascade_baseline/rename_migration_manifest.tsv` — ARCHIVE/FROZEN audit
  snapshots (banner comments in the files). NOT regenerated by `--finalize`;
  their builders (`tools/build_historical_audit_table.py`,
  `tools/build_rename_migration_manifest.py`) refuse to run without
  `--allow-archival-rewrite`. Current stage/scope/verdict authority is the
  registry; current positions come from the executable model.
  - **Position-field semantics (do not conflate).** In the frozen archive the
    `current_*` prefix means "current *at the time this snapshot was frozen*",
    not current repository state. In particular
    `historical_audit_table.tsv.current_cascade_position` MUST NOT be
    synchronized to later executable insertions, removals, or reorders: it is
    audit-time record, and it is *expected* to drift from the live cascade.
    The audit matrix `audits/sc001-sc020-chronology-audit.tsv` is likewise
    ARCHIVE/FROZEN (frozen at commit ce4fd3e5): its `cascade_position` and
    reader-placement columns are audit-time state and are never
    resynchronized. The only current-position table is the GENERATED
    `registry/current_sc_state.tsv` projection.
    `exec_index` in the executable model is the complete physical execution
    index. No further vague position synonym may be introduced.
- `registry/archival_orders.tsv` — ARCHIVE/FROZEN legacy order spaces
  (`inventory_order`: the chronology-experiment order space still used as
  archival coordinates by `tools/sound_change_order_sensitivity.py`;
  `staging_order`: the retired staging-map row sequence). Never
  resynchronized.
- `Germanic/docs/archive/` — DEV_NOTES.md, WORKFLOW.md, CANONICAL_STATE.md, HISTORICAL_CHRONOLOGY_AUDIT_PLAN.md, canonical_state_freeze_report.md (tombstones remain at old paths)
- `sound_changes/archive/next_batch_candidates.tsv` — retired candidate board; the registry owns lifecycle/candidate status
- `audits/sc001-sc020-chronology-audit.tsv` — the frozen SC001-SC020 audit matrix (see position-field semantics above)
- `order_tests/chronology_cards/*.md` and `chronology_cards/chronology_graph_nodes.tsv` — per-SC evidence records from past audits; cite but do not treat their metadata as current
- `chronology_card_index.tsv` — ARCHIVE record of the card set at experiment time (banner comment in the file; no live position column; the book pipeline reads its id set only)

## Standard workflow for one SC adjudication

1. `python3 Germanic/tools/adjudicate.py --next` (derived next SC)
2. `python3 Germanic/tools/adjudicate.py SCNNN --prepare`
3. `python3 Germanic/tools/adjudicate.py SCNNN --evidence` (container rebuild of the full cascade and stage bins, freshness-checked live firing census, witness pre/post — never run foma/flookup or trace scripts by hand)
4. Investigate per `RESEARCH_ADJUDICATION_PROTOCOL.md`; write the memo from `audits/ADJUDICATION_TEMPLATE.md` including a `Registry-verdict:` line.
5. Edit SOURCE files only: `sc_registry.tsv`, `chronology_edges.tsv`, memo, `germanic.txt` if the verdict requires, and the publication prose listed by `--prepare`.
6. `python3 Germanic/tools/adjudicate.py SCNNN --finalize` (control-plane refresh of every derived artifact via the artifact graph, then propagation checks — never choose generators by hand)
7. `cd Germanic/tests && python3 -m pytest -q`

## Moving a rule (or any other SOURCE-only edit)

1. Edit the real authority (`tools/oe_pipeline.py` / `Germanic/fsts/germanic.txt` for order; a registry TSV for metadata; a reader file for prose).
2. `python3 Germanic/tools/adjudicate.py --refresh` (rebuilds every stale projection; rebuilds bins/trace/matrix only if their recorded provenance is invalidated).
3. `cd Germanic/tests && python3 -m pytest -q`

No hand synchronization, no builder selection, no position editing anywhere else.

## Control-plane acceptance tests (executed 2026-02; rerun after any control-plane change)

These experiments define what "one authority + one refresh" means. Each was
run against the live tree and reverted; rerun them whenever the artifact
graph, adjudicate front-end, or projection renderers change materially.

1. **Move-a-rule.** Swap two adjacent commuting same-stage rules
   (`OEPrefixAReduction`/`OEInterStressRaising`, no chronology edge, disjoint
   witnesses) in `fsts/germanic.txt` — the ONLY manual edit — then run
   `adjudicate.py --refresh` and the suite. Result: the single refresh
   rebuilt order manifest, executable model, sandbox FST, stage bins
   (+ production/sandbox equivalence, 386 rows identical), full trace,
   registry views, and census; the interaction matrix correctly stayed fresh
   (move-invariant provenance); the suite passed with zero test edits; no
   SOURCE TSV, audit TSV, chronology card, or reader list needed touching.
   Revert = `git checkout` of the moved sources and generated files + one
   refresh (only the bins rebuild; the committed trace matches the restored
   sources), leaving a byte-clean tree.
2. **Add-a-valid-witness.** Append one corpus TSV row in an already-derived
   domain (a duplicate final-`*-z` protoform under a temporary concept),
   `--refresh`, suite. Result: trace and census update automatically; firing
   counts/lists absorb the new witness with no test edits; only the explicit
   corpus-identity guard (386-row equivalence count) flags the change, which
   is its job — a real corpus addition updates the baseline via
   `tools/cascade_baseline.py` as part of the adjudicated change.
3. **Idempotence.** From a clean tree, `--refresh` twice: zero file changes
   both times (~6.5 s each, no container work).
4. **Missing-runtime recovery.** Delete the bin build manifest (or clone
   without bins): `--check` names exactly what is stale and the refresh
   command to run; one `--refresh` restores runtime evidence without tribal
   knowledge.

## Known remaining duplications (accepted, machine-checked where possible)

- `tools/build_historical_audit_table.py` internally hard-codes the SC021 archival prose block; the table is now ARCHIVE/FROZEN, so the hard-coding is frozen historical record rather than a live duplication.
- `book_dossiers/sound_change_book_dossier_inventory.tsv` and book-entry planning files repeat display names/stages for the publication pipeline; the registry is authoritative and divergence would be a bug.
- Archived audit layers preserve legacy stage-label vocabulary (e.g. wgmc/ingvaeonic vs eaf/pwgmc) as historical record; do not normalize.
