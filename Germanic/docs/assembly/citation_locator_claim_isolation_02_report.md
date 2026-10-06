# Citation locator claim-isolation 02 report

## Summary

- broad citations before: **370**
- broad citations after: **316**
- `claim_not_isolated` before: **153**
- `claim_not_isolated` after: **95**
- rows inspected in this pass: **90**
- locators added in this pass: **53**
- sentences split in this pass: **12**
- rows reclassified in this pass: **4**
- unsupported broad citations removed from prose after direct inspection: **1** (`CLMM01-0280`)
- compact alpha regenerated: **yes** (`.md`, `.tex`, `.pdf`)

This pass continued the claim-isolation method from pass 01, but concentrated on a wider finite-cell cluster: `night`, `navel`, `needle`, `youth`, `heaven`, `deed`, `learn`, `lick`, `make`, `bore`, and `show`. The result was a substantial reduction of the blocker bucket without widening scope beyond directly verifiable primary-source claims.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed from the claim-isolation-01 baseline:

1. **53** rows that received verified locators were removed from the remaining-broad manifest.
2. **4** inspected rows were reclassified from `claim_not_isolated` to `general_background`.
3. **1** inspected broad citation was removed from prose after direct inspection because the claimed Campbell support could not be isolated safely (`CLMM01-0280` for `youth / ġeoguþ`).
4. all other inspected rows that still required broad citations were left in the manifest with their unresolved status intact.

Current remaining-status distribution:

| status | rows |
| :--- | ---: |
| `claim_not_isolated` | 95 |
| `page_markers_unreliable` | 82 |
| `general_background` | 59 |
| `headword_not_found` | 55 |
| `source_quarantined` | 14 |
| `multi_page_discussion` | 9 |
| `source_preparation_needed` | 2 |

The localized rows also appear in the regenerated `lexical_volume_regular_compact_alpha_01.md`, so the remaining-manifest and the current reader-facing Markdown are synchronized.

## Primary-source verification

Every new locator added in this pass has a matching row in `citation_locator_primary_source_evidence.tsv`.

New evidence rows added for:

- `CLMM01-0013`, `CLMM01-0015` — `SieversBrunner1965, §98`
- `CLMM01-0205`, `CLMM01-0212` — `RingeTaylor2014, 270`
- `CLMM01-0210` — `RingeTaylor2014, 336`
- `CLMM01-0211` — `Campbell1959, §159`
- `CLMM01-0217`, `CLMM01-0224` — `RingeTaylor2014, 329`
- `CLMM01-0222`, `CLMM01-0225` — `Campbell1959, §367`
- `CLMM01-0281`, `CLMM01-0282` — `RingeTaylor2014, 141`
- `CLMM01-0283` — `Campbell1959, §374`
- `CLMM01-0284` — `SieversBrunner1965, §150.3`
- `CLMM01-0317` — `Campbell1959, §210.1`
- `CLMM01-0318` — `RingeTaylor2014, 324`
- `CLMM01-0320` — `Campbell1959, §381`
- `CLMM01-0349`, `CLMM01-0353` — `RingeTaylor2014, 240`
- `CLMM01-0350` — `RingeTaylor2014, 380`
- `CLMM01-0352`, `CLMM01-0354` — `Campbell1959, §628.3`
- `CLMM01-0355` — `SieversBrunner1965, §284`
- `CLMM01-0373`, `CLMM01-0376`, `CLMM01-0382`, `CLMM01-0384`, `CLMM01-0418` — `RingeTaylor2014, 314`
- `CLMM01-0375` — `Campbell1959, §159`
- `CLMM01-0378` — `RingeTaylor2014, 191`
- `CLMM01-0380`, `CLMM01-0386`, `CLMM01-0388`, `CLMM01-0422`, `CLMM01-0428` — `RingeTaylor2014, 80`
- `CLMM01-0389` — `RingeTaylor2014, 38`
- `CLMM01-0392`, `CLMM01-0397` — `SieversBrunner1965, §417 Anm. 10`
- `CLMM01-0393`, `CLMM01-0398` — `RingeTaylor2014, 247`
- `CLMM01-0404`, `CLMM01-0413` — `Campbell1959, §398.1`
- `CLMM01-0405`, `CLMM01-0414` — `SieversBrunner1965, §45 Anm. 3`
- `CLMM01-0406`, `CLMM01-0415`, `CLMM01-0427` — `Campbell1959, §356.4`
- `CLMM01-0407`, `CLMM01-0416`, `CLMM01-0395` — `RingeTaylor2014, 80`
- `CLMM01-0420`, `CLMM01-0426` — `Campbell1959, §120`

All 53 were checked directly in the cited local source files before being added to prose.

## Sources worked through

The inspected tranche in this pass covered **90** manifest rows across 16 entries. Source distribution within that inspected set:

| source | inspected | locators added | main unresolved outcome(s) |
| :--- | ---: | ---: | :--- |
| `RingeTaylor2014` | 31 | 29 | residual broadness is now mostly general background or already-isolated but still page-anchored elsewhere |
| `Campbell1959` | 21 | 16 | remaining unresolved Campbell rows are mostly broader handbook synthesis or page-sensitive dictionary/interface sentences |
| `SieversBrunner1965` | 9 | 8 | the remaining Brunner broad case was reclassified to `general_background` |
| `ClarkHall1960` | 9 | 0 | all remaining issues are page-anchor problems in the local dictionary witness |
| `Kroonen2013` | 6 | 0 | retained as general comparative background where the exact claim no longer required a tighter locator |
| `Fulk2018` | 3 | 0 | left broad as paradigm or handbook background |
| `Orel2003` | 2 | 0 | unchanged where already exact or not part of the present blocker |
| `Ringe2006` | 2 | 0 | broader comparative background only |
| `BosworthToller1898` | 2 | 0 | both remain page-recovery problems rather than claim-isolation problems |
| `BrightCassidyRingler1971` | 2 | 0 | direct glossary evidence confirmed, but current local witness still remains unsuitable for safe page locators |
| `Streitberg1896` | 1 | 0 | broader comparative background only |
| `Mayrhofer1992` | 1 | 0 | broader comparative background only |
| `HoggPhonology1992` | 1 | 0 | broader phonological background only |

## Successful split-and-localize fixes

| entry | source | locator | source file checked | note |
| :--- | :--- | :--- | :--- | :--- |
| `night / niht` | `RingeTaylor2014` | `240`, `380` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | isolated the dative-singular paradigm-cell derivation and the later analogy sentence |
| `heaven / heofon` | `RingeTaylor2014`; `Campbell1959` | `324`; `§210.1`, `§381` | `docs/references/ringe_taylor_linguistic_history_vol2.txt`; `docs/references/campbell_old_english_grammar.txt` | split the oblique-stem versus dialect sentence and separated the `hefzen` clause |
| `learn (3sg) / liornaþ` | `RingeTaylor2014`; `SieversBrunner1965` | `38`, `80`, `247`; `§417 Anm. 10` | `docs/references/ringe_taylor_linguistic_history_vol2.txt`; `docs/references/brunner_1965_altenglische_grammatik.vision.txt` | localized both the learn-family base and the Northumbrian finite-form evidence |
| `make (iptv.2sg) / maca` | `RingeTaylor2014`; `Campbell1959` | `314`; `§159` | `docs/references/ringe_taylor_linguistic_history_vol2.txt`; `docs/references/campbell_old_english_grammar.txt` | isolated the finite imperative-cell rationale from the restored-`a` stem clause |
| `show (3sg) / sċēawaþ` | `Campbell1959`; `RingeTaylor2014` | `§120`, `§356.4`; `80` | `docs/references/campbell_old_english_grammar.txt`; `docs/references/ringe_taylor_linguistic_history_vol2.txt` | split the show-family `scēaw-` development from the class-II `-aþ` ending claim |

## Rows deliberately left broad after direct inspection

| entry | source | final status | reason |
| :--- | :--- | :--- | :--- |
| `deed / dǣd` | `Campbell1959` | `claim_not_isolated` | the West-Saxon lowering claim is still compressed with several historical steps and was not safely isolated in this pass |
| `heaven / heofon` | `Fulk2018` | `general_background` | the source remains useful for broad handbook staging, but not for a tighter locator-safe sentence as currently written |
| `needle / nǣdl` | `HoggPhonology1992` | `general_background` | the local Hogg witness supports the broader cluster history, not a tighter sentence-level locator |
| `navel / nafola` | `SieversBrunner1965` | `general_background` | the older-medial-`u` dispute remains comparative background rather than a locator-safe sentence in the current prose |
| `show (iptv.2sg) / sċēawa` | `BrightCassidyRingler1971` | `page_markers_unreliable` | the glossary gives `scēawa` directly, but the current local witness still does not provide a safe page-style locator |
| `show (3sg) / sċēawaþ` | `BrightCassidyRingler1971` | `page_markers_unreliable` | the `-sceawað` evidence is real, but still tied to glossary entry locations rather than a safe printed-page locator |
| `youth / ġeoguþ` | `Campbell1959` | citation removed | the previously broad Campbell claim about direct `geoguþ` spellings could not be recovered safely, so the unsupported broad citation was dropped rather than guessed tighter |

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
- TeX still contains the citeproc bibliography block: **yes**

## Scope confirmation

- No TSV source data were edited.
- No FST files were edited.
- No compact trace source was edited.
- No bibliography files were edited.
- Generated TeX/PDF were regenerated, not hand-edited.
