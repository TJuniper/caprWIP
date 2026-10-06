# Canonical state freeze report

## Files inspected

- `README.md`
- `Germanic/README.md`
- `Germanic/docs/README.md`
- `Germanic/docs/WORKFLOW.md`
- `Germanic/docs/DEV_NOTES.md`
- `Germanic/docs/germanic_transducer_report.md`
- `Germanic/docs/lexeme_reports/report_schema.md`
- `Germanic/docs/lexeme_reports/report_manifest.tsv`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/tools/oe_lexeme_report_coverage.py`
- `Germanic/tools/oe_derivation_report_with_lexeme_reports.py`
- `Germanic/tools/oe_lexeme_report_packet.py`

## Files changed

- `README.md`
- `Germanic/README.md`
- `Germanic/docs/README.md`
- `Germanic/docs/WORKFLOW.md`
- `Germanic/docs/germanic_transducer_report.md`
- `Germanic/docs/CANONICAL_STATE.md`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/docs/canonical_state_freeze_report.md`

## Stale claims found

### Claims presented as current and updated

- Root `README.md` still said `25 mismatches out of ~386 OE lexemes (94% accuracy)`.
- `Germanic/README.md` correctly carried the 7-of-386 closure, but still presented mismatch-debugging workflow without saying that the active phase is now lexical write-up.
- `Germanic/docs/README.md` listed `germanic_transducer_report.md` as a generic coverage summary without warning that it is historical.
- `Germanic/docs/WORKFLOW.md` still presented sound-change debugging as the default resume path.

### Historical claims found and left in place

- `Germanic/docs/germanic_transducer_report.md` contains historical counts such as `282 mismatches / 88 matches (370 total OE rows)`.
- `Germanic/docs/DEV_NOTES.md` and many packets/slices preserve older mismatch totals as part of dated research history.
- Historical dossier material such as `Germanic/docs/dossier-spar-apocope-2025.md` still mentions older counts (for example `~25 mismatches`) in clearly historical context.

These historical figures were not rewritten. They remain as traceability records.

## Claims updated

- Root `README.md` now points to the 7-of-386 closure and explicitly directs readers to `Germanic/README.md` and `Germanic/docs/CANONICAL_STATE.md`.
- `Germanic/README.md` now states that the active phase is lexical write-up/publication preparation and that `docs/CANONICAL_STATE.md` defines the writing-phase source hierarchy.
- `Germanic/docs/README.md` now lists `CANONICAL_STATE.md` as primary documentation and labels `germanic_transducer_report.md` as historical.
- `Germanic/docs/WORKFLOW.md` now says that the current default phase is write-up and that the file mainly documents how to reopen sound-change work later.
- `Germanic/docs/germanic_transducer_report.md` now has a top-of-file historical-status warning.
- `Germanic/docs/CANONICAL_STATE.md` now freezes the authoritative project state and source hierarchy for the writing phase.

## Terminology addendum after freeze

After the initial freeze pass, the coverage-audit terminology was refined so that non-manifest files are no longer described as reports.

- **Manifest-backed production reports** remain the only production-report layer.
- Packets, dev-note slices, research memos, and similar non-manifest files are now described as **source material available**.
- Rows with neither a manifest-backed production report nor matched supporting files are now described as **no source material found**.

This change was terminology-only. It did not promote any row into `report_manifest.tsv`, create new production reports, or change any research conclusions.

## Scripts run successfully

### Coverage audit regeneration

```bash
python3 Germanic/tools/oe_lexeme_report_coverage.py --output Germanic/docs/lexeme_reports/coverage_audit.md
```

This succeeded and rewrote `Germanic/docs/lexeme_reports/coverage_audit.md`.

### Count checks

Local count checks were run against `Germanic/data/germanic-aligned-final.tsv` and `Germanic/data/oe_known_problems.tsv` to confirm:

- 386 total OE rows in the TSV
- 380 OE rows with a real `COUNTERPART`
- 6 OE rows excluded from report coverage because `COUNTERPART = -`
- 7 rows in `oe_known_problems.tsv`

## Scripts not run

- `python3 Germanic/tools/oe_derivation_report_with_lexeme_reports.py`
  - Not run because this freeze pass did not need to regenerate the assembled derivation report; the task was to freeze documentation hierarchy and status claims.
- `python3 Germanic/tools/oe_lexeme_report_packet.py`
  - Not run because this pass did not create or revise packets.

## Remaining uncertainties

1. The repository still uses two different denominators for two different purposes:
   - **386 OE lexemes/rows** for pipeline-status reporting
   - **380 OE rows with real counterpart** for lexeme-report coverage
2. The regenerated coverage audit now treats many non-manifest files as **source material available** rather than production reports. This is consistent with the current tool’s policy, but it means the real production backlog should be read as:
   - rows with **no source material found**, plus
   - rows with **source material available** but no manifest-backed production report.
3. `Germanic/docs/DEV_NOTES.md` contains the authoritative April 2026 closure note, but it also retains many older status totals by design. Future agents should rely on `CANONICAL_STATE.md` before treating any status line as current.

## Next recommended production step

Use the regenerated coverage audit as the lexeme-report backlog:

```bash
python3 Germanic/tools/oe_lexeme_report_coverage.py --output Germanic/docs/lexeme_reports/coverage_audit.md
```

Then work down:

1. `Required rows with no source material found`
2. `Required rows with source material available but no manifest-backed production report`
3. rows that already have packets/dev-note slices but no manifest-backed production report
