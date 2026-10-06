# Infrastructure authority architecture (internal engineering note)

> HISTORICAL NOTE (control-plane pass, 2026): this note records passes 1–2
> as implemented at the time. The 2026 control-plane pass has since removed
> the registry's derived order columns entirely (no `cascade_position` /
> `staging_order` / `inventory_order` in `sc_registry.tsv`; no
> `sync_registry_cascade_positions.py`). Current positions live only in the
> generated `registry/current_sc_state.tsv`; legacy order spaces are frozen
> in `registry/archival_orders.tsv`. For the current authority map see
> `registry/CONTROL_PLANE.md`. The tables below are kept as a record of the
> earlier architecture.

Internal engineering documentation for the 2026 infrastructure-consistency
passes ("one logical authority for each fact"). Not reader-facing.
Pass 1: authority consolidation. Pass 2: derived cascade positions,
freshness chain, order-sensitivity refactor, archive/current separation.

## Authorities

| Fact | Single authority | Access point |
|---|---|---|
| Executable OE rule definitions and order | `Germanic/fsts/germanic.txt` (production composition rooted at `regex OldEnglish`) | parsed by `Germanic/tools/oe_pipeline.py` |
| Executable stage model (stage names, exec indices, cascade positions, snapshot-bin names, bundle expansion) | `oe_pipeline.py` (derived, in-memory) | `stages()`, `named_stages()`, `cascade_position()`, `rules_between()`, `expected_snapshot_bins()`, `sandbox_text()` |
| SC ↔ Foma identifier mapping; SC lifecycle; verdicts | `Germanic/docs/sound_changes/registry/sc_registry.tsv` | `generate_registry_views.py` |
| Historical/semantic SC metadata | `sc_registry.tsv` + `sc_inventory_annotations.tsv` + `chronology_edges.tsv` | `generate_registry_views.build_all()` |
| Runtime locations (bin dir, fsts dir, data dir; host vs container) | `Germanic/tools/capr_runtime.py` `layout()` | all active tools |
| Compiled-artifact freshness | `oe_build_manifest.json` in the runtime bin dir (source sha256s + expected bin set), written by the rebuild entry points | `capr_runtime.write_build_manifest()` / `check_build_manifest()`; checked by `oe_bin_sync_check.py` |
| Corpus | `Germanic/data/germanic-aligned-final.tsv` | `oe_pipeline.load_rows()` |

Structural bundles in `germanic.txt` (defines whose bodies are pure
composition of other rules) are marked with a trailing `# capr:bundle`
comment; `oe_pipeline` expands them recursively. A define without the
marker is a leaf stage even if its body is compositional.

## Generated projections (never hand-edited)

| File | Generator | Semantics |
|---|---|---|
| `cascade_baseline/cascade_order_manifest.tsv` | `cascade_order_manifest.py` | legacy-compatible view (cascade positions 1–95) |
| `cascade_baseline/executable_model.tsv` | `cascade_order_manifest.py` | complete view: exec_index 1–98 ↔ cascade_position, origin block, snapshot bin, SC id |
| `Germanic/fsts/old_english_sandbox.txt` | `generate_oe_sandbox.py` | stage-by-stage snapshot compile (98 checkpoints); sources `germanic.txt` |
| `sc_registry.tsv` `cascade_position` column | `sync_registry_cascade_positions.py` | DERIVED column inside an otherwise hand-edited SOURCE file: rewritten from registry `fst_identifier` + `oe_pipeline.cascade_position()`; never typed by hand |
| `chronology_card_index.tsv` `cascade_position` column | `sync_chronology_card_positions.py` | derived from registry `fst_identifier` + `oe_pipeline` (retired → `retired`); does NOT read the registry's cached column |
| `cascade_baseline/rule_coverage_census.tsv` | `rule_coverage_census.py` | joins committed trace-report firing counts to model positions; fails closed if the committed trace is stale or noncanonical |
| `cascade_baseline/oe_equivalence_report.json` | `check_production_sandbox_equivalence.py` | production `old_english.bin` vs final generated-sandbox checkpoint: identical output multisets over all selected corpus rows |
| registry views (8 files) | `generate_registry_views.py` + chained builders | see `adjudicate.py CHAINED_BUILDERS`; the `current_order` field in inventory/nodes views is the ARCHIVAL inventory order, not executable position |

Each generator has a `--check` mode (or equivalent) and is run by
`adjudicate.py --finalize`; `adjudicate.py --check` and the guard tests
fail if any projection is stale.

## Consumers (no independent copies)

- `oe_full_trace_report.py`: `STAGES`/headers derived from `oe_pipeline`;
  labels are canonical Foma identifiers.
- `sc_evidence.py`: stage lookup from `oe_pipeline`; no alias table;
  fail-closed bin validation (`--min-mtime`, `MIN_BIN_BYTES`).
- `rule_coverage_census.py`: positions from `oe_pipeline`; no
  `STAGE_ALIASES`.
- `sc004_interaction_analysis.py`: crossed-rule sets derived via
  `oe_pipeline.rules_between()` (previously hand-coded and stale).
- `sound_change_order_sensitivity.py`: production chain, bundle
  components, prelude/tail and variant construction all derived from
  `oe_pipeline` (`composition_members_of()`, `production_parent_chain()`);
  no private regex parser, no hand-maintained `POST_EPENTHESIS_RULES` or
  `PWGMC_COMPONENT_RULES`; paths from `layout()`; canonical bin gated on
  `check_build_manifest()` (`--allow-stale-bin` to bypass with warning).
  Order spaces are explicit: EXECUTABLE (from the model) vs INVENTORY
  (`inventory_order`, archival) vs CHRONOLOGY-EXPERIMENT (archival TSV
  coordinates).
- `oe_full_trace_report.py`: canonical runs (default bins) are gated
  fail-closed on `check_build_manifest()`; provenance records build
  identity (manifest source hashes, built_at, runner, foma version,
  expected-bin count) alongside live source hashes;
  `trace_provenance_problems()` lets downstream consumers verify
  freshness. Explicit bin overrides require `--debug-bins` and are
  stamped NONCANONICAL.
- `adjudicate.py`: `--evidence` owns everything requiring Foma/runtime
  (sandbox+production compile, build manifest, production↔sandbox
  equivalence, canonical trace regeneration when stale, census evidence);
  `--finalize` owns host-side deterministic projections (derived-column
  syncs first, then views, manifest, sandbox, card positions, census),
  and fails with "run --evidence first" if runtime-derived upstream
  evidence is stale. Archive builders are NOT in the finalize chain.

## Retired duplication

- `EnglishAfter*` instrumentation chain in `germanic.txt` (28 defines +
  27 regex/save blocks + tracked bins): deleted — zero consumers; the
  generated sandbox is the only instrumentation, and it is derived from
  the production composition itself.
- `trace_old_english_sandbox.py`, `annotate_old_english_sandbox_results.py`,
  `run_old_english_sandbox_workflow.sh`: deleted — hard-coded stale stage
  universe, stale `server/` layout, no consumers.
- Tracked `.bin` files under `backend/` and `Germanic/fsts/`: untracked —
  bins are runtime artifacts rebuilt into the single authoritative bin
  directory (host `backend/` ≡ container `/usr/app`); freshness is the
  build manifest, not git or mtimes.
- mtime-skew heuristics in `oe_bin_sync_check.py`: replaced by the build
  manifest (mtime survives only as `sc_evidence.py --min-mtime`, which
  proves bins were rebuilt during the current evidence run).
- `sound_change_order_sensitivity.py`'s hand-maintained
  `POST_EPENTHESIS_RULES` / `PWGMC_COMPONENT_RULES` lists and private
  regex parsers: deleted (pass 2) — production chain and bundle
  membership now come from `oe_pipeline`; the stale hand list had
  already drifted (10 vs 11 `EarlyEnglishLineChanges` components after
  the SC024 move).
- Hand-edited registry `cascade_position`: retired as a human authority
  (pass 2) — the column physically remains for compatibility but is
  rewritten by `sync_registry_cascade_positions.py` (run in
  `adjudicate.py --finalize`), checked by `--check` and guard tests.
- `build_historical_audit_table.py` / `build_rename_migration_manifest.py`
  and their TSVs: reclassified ARCHIVE/FROZEN (pass 2) — banners added,
  removed from the finalize chain, regeneration requires
  `--allow-archival-rewrite`. Their campaign-time statements (SC004
  "split pending", SC024 position 12, SC025 position 26) are historical
  snapshots, not current facts.

## Deliberately left duplicated

- `cascade_order_manifest.tsv` remains byte-compatible with the legacy
  format (many committed tools/tests read it); `executable_model.tsv`
  carries the complete truth. Both are generated from the same model, so
  they cannot drift from each other.
- The card index's `earliest_safe_order` / `latest_safe_order` /
  `*_boundary_order` columns are ARCHIVAL first-break experiment results
  in the original chronology-test order space; only `cascade_position`
  is synchronized to the current model.
- Registry `staging_order` / `inventory_order` / `v1_reader_position`
  are distinct, hand-curated order spaces (not executable order) and are
  unaffected.
- `Germanic/tests` intentionally pin literal positions, bin names and
  firing counts: tests are supposed to break when the model changes.

## File genres (pass 2)

Every infrastructure file is exactly one of:

**SOURCE** (current human-authored authority): `germanic.txt`,
`sc_registry.tsv` (except the derived `cascade_position` column),
`sc_inventory_annotations.tsv`, `chronology_edges.tsv`, the corpus TSV,
the hand-authored experiment definitions in
`sound_change_order_sensitivity.py` (focal SC, movement direction,
profiles, probes), chronology-card prose.

**GENERATED** (current projection of current authorities): registry
views, `cascade_order_manifest.tsv`, `executable_model.tsv`,
`old_english_sandbox.txt`, card-index `cascade_position`, registry
`cascade_position` column, `rule_coverage_census.tsv`,
`oe_full_trace_report.md`, `oe_build_manifest.json`,
`oe_equivalence_report.json`.

**ARCHIVE/FROZEN** (historical snapshot; never rewritten by current
workflows): `historical_audit_table.tsv`,
`rename_migration_manifest.tsv`, first-break experiment manifests and
their `current_order`-style coordinates, next-batch candidate archives.

## Freshness chain (pass 2)

```
germanic.txt + corpus  ── rebuild (–-evidence) ──►  runtime bins + oe_build_manifest.json
oe_build_manifest.json ── gate ──►  canonical oe_full_trace_report (records build identity)
committed trace (canonical, fresh) ── gate ──►  rule_coverage_census.tsv
runtime bins (manifest-fresh) ── gate ──►  production↔sandbox equivalence report
```

`--finalize` never fabricates runtime-derived evidence: if the trace or
manifest is stale it fails with an instruction to run `--evidence` first.

## Known future work (out of scope for this pass)

- `EarlyEnglishLineChanges` mixes historical stages (PNWGmc/PWGmc/EAF/OE)
  in one structural block.
- The larger cascade-generation refactor (generating `germanic.txt`
  block order itself) has not been started.
