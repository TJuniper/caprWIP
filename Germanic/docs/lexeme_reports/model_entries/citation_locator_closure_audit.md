# Citation-locator closure audit

## Summary

- Total model entries scanned: **147**
- Citation syntax / bibliography-key defects found: **1**
- Citation syntax / bibliography-key defects fixed: **1**
- Forbidden locators found: **0**
- Forbidden locators fixed: **0**
- `KlugeSeebold2011` locator status: **all 14 occurrences remain broad; no page locators are present**
- Remaining broad citations counted: **625** broad source occurrences across **595** citation spans
- Citation layer ready for LaTeX/PDF assembly? **Yes**

This closure pass was an audit and cleanup pass, not a new locator-enrichment pass. No new page locators were added. The only live defect corrected was a stale bibliography key in `2293-will-willa.model.md` and its paired support files: `@Kluge2002` was normalized to the in-bibliography key `@KlugeSeebold2011`.

## Citation syntax audit

- No malformed citation brackets, broken semicolon chains, duplicate-comma locators, doubled numeric locators, or malformed page ranges were found in the current `.model.md` corpus.
- No accidental Markdown formatting inside citation keys was found.
- One bibliography-key defect was found and fixed:

| File | Before | After | Note |
| :--- | :--- | :--- | :--- |
| `2293-will-willa.model.md` | `[@Kroonen2013; @Orel2003; @Kluge2002]` | `[@Kroonen2013; @Orel2003; @KlugeSeebold2011]` | `docs/refs.bib` contains `KlugeSeebold2011`, not `Kluge2002`. |

The matching provenance package for row `2293` was updated as well:

- `2293-will-willa.source_ledger.md`
- `2293-will-willa.reviewer_checklist.md`
- `2293-will-willa.model_implementation_report.md`

## Forbidden locator audit

- No OCR line numbers were found inside final prose citation brackets.
- No source-file line numbers, file offsets, search-result positions, or `docs/references/...:1234`-style locators were found inside final prose citation brackets.
- No `line N` / `l. N` locators were found in final prose citations.
- No `KlugeSeebold2011` page locators were found.

`KlugeSeebold2011` therefore remains in the intended quarantined state for assembly: cited broadly where needed, but never given an unverified page locator.

## Remaining broad citations

The live corpus still contains **625** broad source occurrences. Most are deliberate carry-forwards rather than defects. The table below gives the closure classification needed for assembly.

| Category | Count | Main sources / note |
| :--- | ---: | :--- |
| acceptable broad handbook/background citation | 58 | Untargeted background sources such as `SieversBrunner1965`, `HoggPhonology1992`, `Lloyd1966`, `Ringe2006`, `Bulbring1902`, `Bammesberger1997`, `Mayrhofer1992`, `Streitberg1896`, `Sweet1953`, and similar one-off background citations |
| unresolved because source passage is multi-page or discussion-level | 144 | Known carry-forwards from `Campbell1959`, `Luick1914`, `RingeTaylor2014`, and `Fulk2018` |
| unresolved because local Bosworth-Toller supplement lacks base-dictionary evidence | 33 | `BosworthToller1898` broad citations left broad intentionally after the conditional pass |
| unresolved because page marker unavailable or unreliable | 14 | all remaining `KlugeSeebold2011` broad citations |
| unresolved because human review or source preparation is required | 66 | conditional-source page/claim-pairing failures plus high-confidence-source cases that still need manual headword/passage checking |
| broad citation not yet explained by prior locator reports | 310 | additional broad occurrences from already-cleared high-confidence sources, mostly `ClarkHall1960`, `Kroonen2013`, `RingeTaylor2014`, `Orel2003`, and `BrightCassidyRingler1971`, not exhaustively itemized in earlier reports |

Top live broad-source counts after the cleanup fix:

| Source | Broad occurrences |
| :--- | ---: |
| `RingeTaylor2014` | 128 |
| `ClarkHall1960` | 112 |
| `Kroonen2013` | 95 |
| `Campbell1959` | 93 |
| `Orel2003` | 52 |
| `BosworthToller1898` | 33 |
| `SieversBrunner1965` | 32 |
| `BrightCassidyRingler1971` | 23 |
| `KlugeSeebold2011` | 14 |
| `Fulk2018` | 13 |

The key closure finding is that the remaining broad citations are overwhelmingly either:

1. deliberately broad citations from untargeted background sources,
2. known conditional / quarantined carry-forwards, or
3. additional broad high-confidence-source citations that are syntactically fine but were not exhaustively catalogued in the earlier locator reports.

## Report consistency check

- `citation_locator_conditional_sources_report.md` is consistent with the live corpus for the conditional sources:
  - the entry-by-entry change table contains **45** changed model entries,
  - the commit file set for `6d51dceb` contains **45** changed `.model.md` files and **135** changed support files,
  - the unresolved-count summary (**128** broad conditional-source occurrences) matches the occurrence-level TSV exactly.
- `citation_locator_full_corpus_high_confidence_report.md` is internally consistent for the work it records:
  - the changed-entry list contains **40** model entries,
  - the commit file set for `296c46f5` contains **40** changed `.model.md` files and **120** changed support files,
  - the unresolved table sums to the stated **115** report-tracked unresolved occurrences.
- However, the high-confidence report's unresolved table is **not** an exhaustive inventory of all currently remaining broad citations to the high-confidence sources. The live corpus still contains many additional broad high-confidence-source occurrences beyond that table. This does **not** create a Pandoc-syntax or assembly blocker, but the earlier `115` figure should be read as pass-accounting for the tracked unresolved subset, not as the total remaining broad high-confidence inventory.
- The source-treatment boundaries remain consistent:
  - `KlugeSeebold2011` remains quarantined.
  - `Campbell1959`, `BosworthToller1898`, and `Luick1914` remain claim-by-claim sources, not bulk-safe sources.
  - No high-confidence source was converted into a forbidden conditional/quarantined source by later edits.

## Assembly recommendation

**Decision: A. Citation layer is ready for LaTeX/PDF assembly; remaining broad citations can be carried forward.**

Reasoning:

1. The live model-entry corpus is mechanically clean for Pandoc citation processing.
2. No forbidden locators remain.
3. `KlugeSeebold2011` remains broad, as required.
4. The one broken bibliography key found in the audit has been corrected.
5. The remaining broad citations are honest broad citations, not malformed or misleading pseudo-locators.

The only caution for the next phase is documentary rather than mechanical: use this closure audit, not the earlier high-confidence unresolved table, as the broad-citation inventory baseline for assembly notes.

## Scope confirmation

- No TSV source data, FST files, `report_manifest.tsv`, packets, dev-note slices, research memos, bibliography files, derivation traces, writing-skill files, or local OCR/reference files were edited.
- The only repository files changed in this closure pass were:
  - `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.model.md`
  - `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.source_ledger.md`
  - `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.reviewer_checklist.md`
  - `Germanic/docs/lexeme_reports/model_entries/2293-will-willa.model_implementation_report.md`
  - `Germanic/docs/lexeme_reports/model_entries/citation_locator_closure_audit.md`
