# Citation locator claim-isolation 05 report

## Summary

- broad citations before: **262**
- broad citations after: **246**
- `claim_not_isolated` before: **82**
- `claim_not_isolated` after: **66**
- rows inspected in this pass: **55**
- locators added in this pass: **16**
- sentences split in this pass: **4**
- rows reclassified in this pass: **0**
- unsupported broad citations removed after direct inspection: **0**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass stayed narrow and only took the cleanest remaining easy wins. The productive tranche came from non-regular entries whose current prose could be safely narrowed or split around already-verified dictionary and handbook evidence; the harder argumentative remainder was left broad rather than forced into misleadingly precise citation clauses.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed in place from the claim-isolation-04 baseline:

1. **16** verified locator rows were removed from the remaining-broad manifest.
2. No rows were reclassified in this pass.
3. All other inspected but still unresolved rows were left in place with their existing status.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `headword_not_found` | 75 |
| `claim_not_isolated` | 66 |
| `general_background` | 59 |
| `source_preparation_needed` | 15 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `page_markers_unreliable` | 8 |

The localized rows also appear in the regenerated `lexical_volume_regular_compact_alpha_01.md`, so the manifest and current reader-facing Markdown are synchronized.

## Primary-source verification

Every new locator added in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows added for:

- `CLMM01-0168`, `CLMM01-0169` — `ClarkHall1960, 125`; `BosworthToller1898, 275`
- `CLMM01-0187`, `CLMM01-0188` — `Campbell1959, §158`; `SieversBrunner1965, §10`
- `CLMM01-0194`, `CLMM01-0195`, `CLMM01-0196` — `BosworthToller1898, 551`; `ClarkHall1960, 160-161`; `BrightCassidyRingler1971, 315`
- `CLMM01-0242` — `ClarkHall1960, 263`
- `CLMM01-0256` — `ClarkHall1960, 338`
- `CLMM01-0292` — `ClarkHall1960, 67`
- `CLMM01-0333` — `Campbell1959, §621`
- `CLMM01-0351` — `ClarkHall1960, 215`
- `CLMM01-0448`, `CLMM01-0449`, `CLMM01-0450`, `CLMM01-0451` — `Campbell1959, §115`; `Bulbring1902, §116`; `Campbell1959, §115`; `SieversBrunner1965, §160`

All 16 were checked directly in the cited local source files before being inserted into prose.

## Sources worked through

The inspected tranche concentrated on the easiest surviving source types and a smaller verification sweep through the harder remainder:

- direct localization work:
  - `ClarkHall1960`
  - `BosworthToller1898`
  - `BrightCassidyRingler1971`
  - `Campbell1959`
  - `SieversBrunner1965`
  - `Bulbring1902`
- inspected remainder triage:
  - `RingeTaylor2014`
  - `Kroonen2013`
  - `Orel2003`
  - `Fulk2018`
  - `HoggPhonology1992`

Locator additions in this pass came from:

| source | locators added |
| :--- | ---: |
| `ClarkHall1960` | 6 |
| `Campbell1959` | 4 |
| `BosworthToller1898` | 2 |
| `SieversBrunner1965` | 2 |
| `BrightCassidyRingler1971` | 1 |
| `Bulbring1902` | 1 |

## Successful split-and-localize fixes

| entry | source | locator | note |
| :--- | :--- | :--- | :--- |
| `follow / fylġan` | `ClarkHall1960`; `BosworthToller1898` | `125`; `275` | narrowed the OE evidence to the conservative class-I dictionary headwords instead of the mixed `folgian`/`fylgan` sentence |
| `lap / lappa` | `Campbell1959`; `SieversBrunner1965` | `§158`; `§10` | split restored-`a` evidence from the separate variant-form note |
| `laugh / hliehhan` | `BosworthToller1898`; `ClarkHall1960`; `BrightCassidyRingler1971` | `551`; `160-161`; `315` | separated three source-specific dictionary/glossary claims that had previously shared one broad citation span |
| `cow / cȳ` | `ClarkHall1960` | `67` | isolated the Clark Hall paradigm line from the already narrower Ringe-Taylor historical summary |
| `wolf / wulf` | `Campbell1959`; `Bulbring1902`; `SieversBrunner1965` | `§115`; `§116`; `§160` | localized the recoverable handbook clauses while leaving the broader explanatory debate broad |

## Rows deliberately left broad

| entry | source | final status | reason |
| :--- | :--- | :--- | :--- |
| `man / mannes` | `RingeTaylor2014` | `claim_not_isolated` | the paradigm-cell choice still sits inside a wider reconstruction summary rather than a cleanly isolatable source claim |
| `wolf / wulf` | `Kroonen2013`; `RingeTaylor2014`; `Luick1914` | `claim_not_isolated` | the remaining prose still compresses inherited reconstruction, exception handling, and explanatory debate into one argument |
| inspected easy-looking remainder | mixed handbook and comparative sources | `claim_not_isolated` | the final easy-win pass stopped once further splitting would have produced awkward or misleadingly atomized prose |

## Support-package updates

All nine changed non-regular model entries had their paired support files updated:

- `.source_ledger.md`
- `.reviewer_checklist.md`
- `.model_implementation_report.md`

Each received a short claim-isolation-05 note recording that the citation locator was tightened against a directly checked source.

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No locators were copied from earlier reports without direct rechecking in the local source files.
- Every newly added locator has a matching primary-source evidence row.

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- No generated TeX/PDF files were hand-edited.

## Recommendation

**B. switch to `headword_not_found` audit.**

This pass appears to have harvested the last clean claim-isolation easy wins. The remaining `claim_not_isolated` rows are now smaller than the `headword_not_found` bucket and skew more strongly toward genuinely broad argument, mixed-source compression, or prose that would become awkward if split further.
