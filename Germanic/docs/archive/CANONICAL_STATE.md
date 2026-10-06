# Germanic/OE canonical state

> **FROZEN HISTORICAL CHECKPOINT (2026-05-09).** This file records the
> project state at its freeze date and is preserved unchanged as a
> historical record. It is **not** the current state: an active
> sound-change adjudication programme has since reopened individual
> rules. For current state, start with `Germanic/docs/CURRENT_STATE.md`;
> for the adjudication method, see
> `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md`.

- **Freeze date:** 2026-05-09
- **Branch used:** `update`
- **Base commit used for this freeze pass:** `37567274`

## Canonical status summary

- The Germanic → Old English **research phase is complete** as of 2026-04-30.
- The canonical high-level project status is **7 mismatches out of 388 OE lexemes** (**98.2% accuracy**), with **0 actionable phonology**.
- All 7 remaining mismatches are treated as **documented exceptions** in `Germanic/data/oe_known_problems.tsv`.
- The project is now in **lexical write-up and publication-preparation mode**, not active sound-change debugging mode.

## Important count distinction

- The **pipeline-status denominator** is now **388 OE lexemes** (the original 386 plus *who* 2322 and *you* 2326 from corpus-maturation pass 01). This is the status reported in `Germanic/README.md` and in the closing status section of `Germanic/docs/DEV_NOTES.md`. The original 380-row selected corpus is frozen as a legacy subset with invariant fingerprint `a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc` (see `cascade_baseline_outputs_legacy380.tsv`).
- The **lexeme-report coverage audit** currently counts **382 OE rows with a real `COUNTERPART`**. Six OE TSV rows have `COUNTERPART = -` and are therefore excluded from lexeme-report coverage:
  - `1935 ball`
  - `1947 bid`
  - `1948 bid`
  - `1994 dove`
  - `2156 roe`
  - `2218 stilt`
- These two counts serve different purposes and should not be conflated.

## Authoritative files for the writing phase

### A. Primary current data

Treat the following as the authoritative current source layer for lexeme-report production:

1. `Germanic/data/germanic-aligned-final.tsv`
2. `Germanic/data/oe_known_problems.tsv`
3. `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
4. `Germanic/docs/lexeme_reports/report_schema.md`
5. `Germanic/docs/lexeme_reports/report_manifest.tsv`
6. `Germanic/docs/lexeme_reports/coverage_audit.md`

Also use the relevant row packet under `Germanic/docs/lexeme_reports/packets/` when one exists.

### B. Research rationale

Use these to recover reasoning, chronology, and philological argumentation behind the current state:

1. `Germanic/docs/DEV_NOTES.md`
2. `Germanic/docs/analysis/`
3. Specific dossiers or investigations when directly relevant to a row (for example `dossier-shoulder-2026.md` and comparable row-level files)
4. The detailed `dev_notes_slices/` layer when a row-specific replacement note is needed

### C. Historical diagnostics only

These remain useful for traceability, but they are **not** authoritative current-status sources:

1. Old mismatch reports under `Germanic/docs/debug_snapshots/`
2. Old full trace reports under `Germanic/docs/debug_snapshots/`
3. `Germanic/docs/germanic_transducer_report.md`
4. Older transducer status notes embedded in historical docs
5. Outdated planning/TODO files and archived project-status entries outside the current freeze note

## Writing-phase instruction

Generate or polish lexeme reports from:

1. the live TSV row in `Germanic/data/germanic-aligned-final.tsv`;
2. the current compact derivation report `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`;
3. the relevant lexeme packet in `Germanic/docs/lexeme_reports/packets/`;
4. `Germanic/docs/lexeme_reports/report_manifest.tsv`;
5. `Germanic/docs/lexeme_reports/report_schema.md`;
6. `Germanic/docs/lexeme_reports/coverage_audit.md`.

Do **not** treat older debug snapshots as the basis for current lexeme-report prose or current mismatch counts. They may preserve useful historical diagnostics, but many contain superseded totals, superseded targets, or superseded implementation states.

Only **manifest-backed** entries in `Germanic/docs/lexeme_reports/report_manifest.tsv` with status `pilot` or `full` count as current **production lexeme reports**. Packets, dev-note slices, research memos, batch summaries, and other non-manifest matches are **supporting source material**, not production-report prose.

## Current assembled outputs

- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md` is the current assembled publish-mode derivation report.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md` is the audit-mode assembled report.

These are useful reading views, but the authoritative input for new report work remains the **compact report + TSV + packets + manifest + schema**.

## Coverage audit status in this freeze pass

- `Germanic/docs/lexeme_reports/coverage_audit.md` **was regenerated successfully** in this pass with:

  ```bash
  python3 Germanic/tools/oe_lexeme_report_coverage.py --output Germanic/docs/lexeme_reports/coverage_audit.md
  ```

- The regenerated audit currently reports:
  - 382 OE rows with real counterpart
  - 150 rows requiring lexeme reports
  - 11 manifest-backed production reports
  - 138 required rows with source material available but no manifest-backed production report
  - 1 required row with no source material found

Because the coverage tool now distinguishes **manifest-backed production reports** from **supporting source material**, the production backlog is not limited to the final row with no matched files. Treat both **“source material available but no manifest-backed production report”** and **“no source material found”** as active write-up backlog categories.

## Next production step

Use `Germanic/docs/lexeme_reports/coverage_audit.md` as the backlog for missing lexeme reports, prioritizing:

1. rows with **no source material found**;
2. rows with **source material available** but no manifest-backed production report;
3. rows already represented by packets/dev-note slices but not yet promoted into manifest-backed report files.
