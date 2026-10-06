# Citation locator claim-isolation 01 report

## Summary

- broad citations before: **387**
- broad citations after: **370**
- `claim_not_isolated` before: **173**
- `claim_not_isolated` after: **153**
- rows inspected in this pass: **86**
- locators added in this pass: **17**
- sentences split in this pass: **10**
- rows reclassified in this pass: **3**
- rows left broad after direct inspection: **66**
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

Newly reclassified inspected rows:

| status | rows |
| :--- | ---: |
| `page_markers_unreliable` | 2 |
| `headword_not_found` | 1 |

This pass met the narrow goal of working down the `claim_not_isolated` bucket by splitting only where a directly verified locator could be attached without changing the analysis.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed in place from the master-manifest-04 baseline:

1. all **17** rows that received verified locators were removed from the remaining-broad manifest;
2. **3** inspected rows were reclassified more precisely after direct source inspection;
3. all other inspected rows that still needed broad citations were left in the manifest with their unresolved status intact;
4. the manifest now reflects a remaining-broad queue of **370** rows with **153** still in `claim_not_isolated`.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 153 |
| `page_markers_unreliable` | 82 |
| `headword_not_found` | 55 |
| `general_background` | 55 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `source_preparation_needed` | 2 |

The localized rows also appear in the regenerated `lexical_volume_regular_compact_alpha_01.md`, so the remaining-manifest and the current reader-facing Markdown are aligned.

## Primary-source verification

Every new locator added in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows added for:

- `CLMM01-0260` — `Kroonen2013, 267`
- `CLMM01-0262` — `RingeTaylor2014, 130`
- `CLMM01-0278` — `RingeTaylor2014, 141`
- `CLMM01-0309`, `CLMM01-0310` — `RingeTaylor2014, 93`
- `CLMM01-0313` — `Campbell1959, §762`
- `CLMM01-0324`, `CLMM01-0327` — `RingeTaylor2014, 364`
- `CLMM01-0328` — `Campbell1959, §762`
- `CLMM01-0371` — `Campbell1959, §159`
- `CLMM01-0372` — `RingeTaylor2014, 191`
- `CLMM01-0401`, `CLMM01-0410`, `CLMM01-0423` — `Campbell1959, §356.4`
- `CLMM01-0402`, `CLMM01-0411`, `CLMM01-0424` — `RingeTaylor2014, 80`

All 17 were checked directly in the cited local source files before being added to prose.

## Sources worked through

The focused tranche was the previously selected **86-row** cluster across 15 files. Source distribution within that tranche:

| source | inspected | locators added | main unresolved outcome(s) |
| :--- | ---: | ---: | :--- |
| `RingeTaylor2014` | 32 | 10 | remaining failures were mostly multi-step development or paradigm-choice sentences |
| `Campbell1959` | 32 | 7 | mix of remaining `claim_not_isolated`, `page_markers_unreliable`, and one `headword_not_found` |
| `SieversBrunner1965` | 12 | 0 | mostly broader handbook discussion that still did not isolate cleanly in the current prose |
| `BosworthToller1898` | 2 | 0 | both remained dictionary-page problems rather than split-friendly claim-isolation cases |
| `Kroonen2013` | 2 | 1 | one clean dictionary-headword win, one broader comparative sentence still merged |
| `Orel2003` | 2 | 0 | exact entry found, but page anchoring still unreliable in the available local text |
| `Bulbring1902` | 1 | 0 | remained discussion-level background |
| `ClarkHall1960` | 1 | 0 | dictionary evidence remained page-anchor-limited |
| `Fulk2018` | 1 | 0 | remained broader paradigm background |
| `HoggPhonology1992` | 1 | 0 | remained broader phonological background |

## Successful split-and-localize fixes

| entry | source | locator | source file checked | note |
| :--- | :--- | :--- | :--- | :--- |
| `whine / hwīnan` | `Kroonen2013` | `267` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | isolated the strong-verb headword sentence from the broader family-comparison sentence |
| `whine / hwīnan` | `RingeTaylor2014` | `130` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | localized the Northwest Germanic `hvina / hwinan` linkage after splitting the family-identification clause |
| `youth / ġeoguþ` | `RingeTaylor2014` | `141` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | localized the `*jugunþi > *juguþ > OE geoguþ ~ iuguþ` staging line |
| `have / hæfeþ` | `RingeTaylor2014` | `93` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | localized both the class-III weak-paradigm sentence and the `*-ja-` vs `*-ē-` finite-stem contrast |
| `have / hæfeþ` | `Campbell1959` | `§762` | `docs/references/campbell_old_english_grammar.txt` | localized the unsyncopated `hæfed`-type finite-form evidence |
| `live / lifeþ` | `RingeTaylor2014` | `364` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | localized the `lifed` archaism sentence and the finite-form comparison sentence |
| `live / lifeþ` | `Campbell1959` | `§762` | `docs/references/campbell_old_english_grammar.txt` | localized the attested `lifed` evidence behind normalized `lifeþ` |
| `make (iptv.2sg) / maca` | `Campbell1959` | `§159` | `docs/references/campbell_old_english_grammar.txt` | isolated the restored-`a` class-II background sentence |
| `make (iptv.2sg) / maca` | `RingeTaylor2014` | `191` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | localized the West Germanic class-II comparison sentence |
| `lick (iptv.2sg) / licca` | `Campbell1959` | `§356.4` | `docs/references/campbell_old_english_grammar.txt` | isolated Campbell’s class-II finite-ending statement |
| `lick (iptv.2sg) / licca` | `RingeTaylor2014` | `80` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | localized the stable-`a` finite-cell statement |
| `lick (3sg) / liccaþ` | `Campbell1959` | `§356.4` | `docs/references/campbell_old_english_grammar.txt` | same Campbell finite-ending statement reused for the 3sg companion row |
| `lick (3sg) / liccaþ` | `RingeTaylor2014` | `80` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | same stable-`a` discussion reused for the 3sg companion row |
| `show (3sg) / sċēawaþ` | `Campbell1959` | `§356.4` | `docs/references/campbell_old_english_grammar.txt` | localized the class-II ending sentence after a minimal split |
| `show (3sg) / sċēawaþ` | `RingeTaylor2014` | `80` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | localized the stable-`a` 3sg claim after the same split |

## Rows deliberately left broad after direct inspection

| entry | source | final status | reason |
| :--- | :--- | :--- | :--- |
| `whine / hwīnan` | `Orel2003` | `page_markers_unreliable` | the exact comparative split was recoverable, but the available local Orel text still did not expose a stable printed page anchor |
| `youth / ġeoguþ` | `Campbell1959` | `headword_not_found` | the available Campbell text did not yield a clean directly recoverable `geoguþ` passage sufficient for a safe locator |
| `have / hæfeþ` | `BosworthToller1898` | `page_markers_unreliable` | after sentence-splitting, the remaining unresolved issue was dictionary page recovery rather than claim isolation |
| `live / lifeþ` | `BosworthToller1898` | `page_markers_unreliable` | the headword sentence is now isolated, but Bosworth-Toller still lacks a safe local page anchor |
| `have / hæfeþ` | `RingeTaylor2014` + `Campbell1959` | `claim_not_isolated` | the derivation sentence still compresses several phonological steps and was not rewritten beyond the minimal safe split |
| `lick (iptv.2sg) / licca` | `Campbell1959` + `RingeTaylor2014` | `claim_not_isolated` | the development sentence still merges shortening, segmental history, and consonantism into one compact claim |
| `show (3sg) / sċēawaþ` | `Campbell1959` | `claim_not_isolated` | the development paragraph still combines multiple rule applications and was left broad rather than over-split |

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No locators were copied from prior reports without direct rechecking in the local source file.
- No invented page ranges were introduced.

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- TeX still contains the citeproc bibliography block: **yes**
- PDF still contains annotation objects / URI links: **yes** (`971` annotations; `6` URI actions detected by PDF parsing)

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- Generated TeX/PDF were regenerated, not hand-edited.

