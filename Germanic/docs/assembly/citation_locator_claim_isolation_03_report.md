# Citation locator claim-isolation 03 report

## Summary

- broad citations before: **316**
- broad citations after: **295**
- `claim_not_isolated` before: **95**
- `claim_not_isolated` after: **74**
- rows inspected in this pass: **60**
- locators added in this pass: **21**
- sentences split in this pass: **7**
- rows reclassified in this pass: **0**
- unsupported broad citations removed after direct inspection: **0**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass focused on the easiest remaining handbook cases and avoided over-splitting. The productive cluster was `deed`, `berry`, `flask`, `knight`, `lade`, `have`, `live`, `nose`, and `timber`; several harder rows (`wolf`, `fright`, `spare`, and parts of `man`) were reinspected directly and left broad for now because the surviving prose still compresses broader historical argument or mixed comparative background.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed in place from the claim-isolation-02 baseline:

1. **21** verified locator rows were removed from the remaining-broad manifest.
2. Two still-broad companion rows were refreshed so their `current_citation_span` and `surrounding_sentence` match the live prose after sentence splitting:
   - `CLMM01-0174` (`knight / cniht`, `KlugeSeebold2011`)
   - `CLMM01-0180` (`lade / hladan`, `Kroonen2013`)
3. All other directly inspected but still unresolved rows were left in place with their existing status.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `page_markers_unreliable` | 82 |
| `claim_not_isolated` | 74 |
| `general_background` | 59 |
| `headword_not_found` | 55 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `source_preparation_needed` | 2 |

The localized rows also appear in the regenerated `lexical_volume_regular_compact_alpha_01.md`, so the manifest and current reader-facing Markdown are synchronized.

## Primary-source verification

Every new locator added in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows added for:

- `CLMM01-0012`, `CLMM01-0014` — `Campbell1959, §128`
- `CLMM01-0165` — `RingeTaylor2014, 192`
- `CLMM01-0166` — `Campbell1959, §158`
- `CLMM01-0173` — `RingeTaylor2014, 142`
- `CLMM01-0176`, `CLMM01-0177` — `Campbell1959, §146`, `§305`
- `CLMM01-0178` — `SieversBrunner1965, §122`
- `CLMM01-0179`, `CLMM01-0183` — `RingeTaylor2014, 248`
- `CLMM01-0182` — `Campbell1959, §744`
- `CLMM01-0227` — `Campbell1959, 44`
- `CLMM01-0229` — `RingeTaylor2014, 385`
- `CLMM01-0252`, `CLMM01-0254` — `RingeTaylor2014, 327`
- `CLMM01-0290`, `CLMM01-0291` — `RingeTaylor2014, 181`
- `CLMM01-0314`, `CLMM01-0330` — `RingeTaylor2014, 364`
- `CLMM01-0315`, `CLMM01-0329` — `Campbell1959, §762`

All 21 were checked directly in the cited local source files before being inserted into prose.

## Sources worked through

The inspected 60-row tranche was concentrated in the handbook-heavy remainder:

- `RingeTaylor2014`
- `Campbell1959`
- `SieversBrunner1965`
- `Kroonen2013`
- `Orel2003`
- spot-check reinspection for non-wins in `Fulk2018` and `HoggPhonology1992`

Locator additions in this pass came from:

| source | locators added |
| :--- | ---: |
| `RingeTaylor2014` | 11 |
| `Campbell1959` | 9 |
| `SieversBrunner1965` | 1 |

## Successful split-and-localize fixes

| entry | source | locator | note |
| :--- | :--- | :--- | :--- |
| `deed / dǣd` | `Campbell1959`; `SieversBrunner1965` | `§128`; `§98` | isolated the West-Saxon lowering statement from Brunner's dialect contrast |
| `knight / cniht` | `RingeTaylor2014`; `Campbell1959`; `SieversBrunner1965` | `142`; `§146`, `§305`; `§122` | split comparative reconstruction, broken plural evidence, and early West-Saxon alternation into separately citable clauses |
| `lade / hladan` | `RingeTaylor2014`; `Campbell1959` | `248`; `§744` | separated the strong-verb line from Kroonen's broader weak-family background and localized the restored-`a` clause |
| `live / lifeþ` | `Campbell1959`; `RingeTaylor2014` | `§762`; `364` | tightened the archaic 3sg `lifed` sentence without expanding the entry |
| `timber / timber` | `RingeTaylor2014` | `327` | localized both the comparative derivation and the epenthetic-vowel sentence on the same page |

## Rows deliberately left broad after direct inspection

| entry | source | final status | reason |
| :--- | :--- | :--- | :--- |
| `wolf / wulf` | `Campbell1959`; `RingeTaylor2014`; `SieversBrunner1965` | `claim_not_isolated` | the exception discussion still compresses regular lowering, labial clustering, and oblique-form counterfactuals into one argument |
| `fright / fyrhte` | `RingeTaylor2014` | `claim_not_isolated` | the oblique-cell rationale and the later nominative remodeling are both real, but the current sentence still summarizes a broader paradigm discussion |
| `spare / sparian` | `Kroonen2013`; `Orel2003` | `claim_not_isolated` | the comparative headword versus English class-II reshaping still needs a cleaner sentence boundary before safe localization |
| `man / mannes` | `RingeTaylor2014` | `claim_not_isolated` | the lexeme-level reconstruction summary and the selected genitive-cell rationale are still combined too tightly for one locator-safe clause |

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No locators were copied from prior reports without direct rechecking in the local source files.
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
- Generated TeX/PDF were regenerated, not hand-edited.
