# Citation locator claim-isolation audit 08 report

## Summary

- generated broad citations before: **12**
- generated broad citations after: **6**
- regular book-prose broad citations before: **2**
- regular book-prose broad citations after: **1**
- non-regular model-entry broad citations before: **324**
- non-regular model-entry broad citations after: **319**
- upstream-only broad citations before: **314**
- upstream-only broad citations after: **314**
- rows inspected: **19**
- locators added: **6**
- citations removed: **0**
- citations restored: **0**
- prose softened or revised for undercitation: **6**
- outputs regenerated or not: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed citation spans, including multiline citation spans.
- generated Markdown count before edits: **12**
- regular book-prose count before edits: **2**
- non-regular model-entry count before edits: **324**
- upstream-only broad count before edits: **314**
- manifest matched generated Markdown before edits: **yes**
- generated Markdown count after edits: **6**
- regular book-prose count after edits: **1**
- non-regular model-entry count after edits: **319**
- upstream-only broad count after edits: **314**
- manifest matched generated Markdown after edits: **yes**

## Audit 07 spot-check

All seven audit-07 locators remained safe and required no correction:

- `KlugeSeebold2011, 885` — **safe**
- `KlugeSeebold2011, 886` — **safe**
- `KlugeSeebold2011, 506` — **safe**
- `BosworthToller1898, 604` — **safe**
- `KlugeSeebold2011, 347` — **safe**
- `KlugeSeebold2011, 847` — **safe**
- `KlugeSeebold2011, 981` — **safe**

The printed page markers remain visible in the local witnesses, the cited forms are present, the prose still stays within what those witnesses show, and the existing evidence rows remain accurate.

## Kluge PDF / refs.bib provenance audit

This subtask was deferred by user instruction in audit 08. No provenance-based edits or reversions were made.

See `Germanic/docs/assembly/citation_locator_reference_witness_provenance_08.md`.

## Claim-isolation results

| Entry | Source | Current claim | Searches attempted | Locator added or retained broad | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `birth / byrd` | `HoggPhonology1992` | Hogg provides the broader deverbal-feminine setting for the lexical family. | searched `byrd`, deverbal feminine, nearby noun-cluster discussion in `hogg_vol1.txt` | retained broad | Hogg still treats `byrd` in a broader derivational cluster rather than in one page-localizable clause. |
| `warp / weorpan` | `RingeTaylor2014` | preterite `*warp` contrasted with infinitive `*werpana` behind the selected verbal input | searched `warp`, `werpana`, `weorpan` in `ringe_taylor_linguistic_history_vol2.txt` | locator added: `195`, `197` | The sentence could be split cleanly into one clause for the preterite and one for the infinitive. |
| `fast / festan` | `RingeTaylor2014` | OE 'to fast' treated as originally class I and only later associated with the wider family | searched `fastai`, `fastija`, `feestan`, class-I wording in `ringe_taylor_linguistic_history_vol2.txt` | locator added: `110` | The class-history sentence could be narrowed to the directly witnessed wording on p. 110. |
| `needle / nǣdl` | `HoggPhonology1992` | `nidi / nǣdl` included in the broader cluster history | searched `nidi`, `nǣdl`, `nædl` in `hogg_vol1.txt` | retained broad | The discussion remains embedded in a broader phonological cluster rather than an isolatable handbook clause. |
| `world / weorold` | `SieversBrunner1965` | broader OE variant cluster including `world` and `wurold` | searched `weorold`, `worold`, `woruld`, `world`, `wurold` in `brunner_1965_altenglische_grammatik.txt` | locator added: `§113` | A stable section supports the exact variant-cluster claim, so the broad citation could be localized safely. |
| `ban / bannes` | `Campbell1959` | nominative `ban` from citation `*bánną` by final-vowel loss and geminate simplification | searched `ban`, `bannes`, apocope, geminate discussion in `campbell_old_english_grammar.txt` | retained broad | The nominative simplification claim remains bundled too broadly for one safe Campbell locator. |
| `fright / fyrhte` | `RingeTaylor2014` | later nominatives remodeled, oblique in-stem forms more conservative | searched `furxt`, `fyrhte`, noun-family discussion in `ringe_taylor_linguistic_history_vol2.txt` | retained broad | The contrast still behaves like distributed handbook synthesis rather than a single recoverable clause. |
| `shove / sċēaf` | `RingeTaylor2014` | English present system belongs to a wider class-II split not identical with the preterite grade | searched `skeuban`, `skūban`, class-II present/preterite discussion in `ringe_taylor_linguistic_history_vol2.txt` | retained broad | The remaining class-history sentence still compresses a broader argument than one safe page allows. |
| `span / spanne` | `SieversBrunner1965` | selected form is a dative singular cell, not a rival headword | searched `spanne`, `spann`, `spannen`, paradigm discussion in `brunner_1965_altenglische_grammatik.txt` | retained broad | The dative-singular paradigm background still depends on a broader discussion rather than one clean section-locatable clause. |
| `learn (iptv.2sg) / liorna` | `Fulk2018` | learn-family background from `*liznō-` | searched `liornian`, `leornian`, `*liznō-` in `fulk_comparative_grammar_early_germanic.vision.txt` | locator added: `127` | Fulk gives a clean, page-safe learn-family clause. |
| `lick (iptv.2sg) / licca` | `RingeTaylor2014` | lexeme-level lick-family line continued by OE `liccian` | searched `*li/ekkōn`, `liccian`, `likkon`, `lecchon` in `ringe_taylor_linguistic_history_vol2.txt` | locator added: `50` | The broad class-II paraphrase could be narrowed to the directly witnessed comparative line. |
| `lick (3sg) / liccaþ` | `RingeTaylor2014` | lexeme-level lick-family line continued by OE `liccian` | searched `*li/ekkōn`, `liccian`, `likkon`, `lecchon` in `ringe_taylor_linguistic_history_vol2.txt` | locator added: `50` | The same narrowing worked for the companion 3sg row. |

## Citation-retention and removal discipline

- citations retained broad because they still support useful claims: **6**
- citations removed: **0**
- why each removal was safe: **n/a**
- citations restored: **0**
- confirmation that no citation was removed solely to reduce the broad-citation count: **yes**

This pass stayed conservative. The six localized rows were narrowed only where the sentence could be rephrased to match an exactly verified source page or section. The six remaining rows were left broad because the supporting source material still behaves like distributed handbook or paradigm discussion.

## Undercitation audit

The current watchlist is recorded in `Germanic/docs/assembly/citation_locator_undercitation_watchlist_08.md`.

### `find / fundene`

`find / fundene` remains a stable control case. The entry still rests on `RingeTaylor2014, 344`, `BosworthToller1898, 219`, `ClarkHall1960, 124`, and project trace output. No Luick/Brunner-style analogical-leveling claim has re-entered the prose.

### Other watchlist entries

- `still / stillan`: both audit-07 Kluge locators held up under audit-08 spot-check.
- `loam / lām`: the audit-07 Bosworth p. 604 locator held up under audit-08 spot-check.
- `think / þenċan`, `man / mannes`, `have / hæfeþ`, `rust / rust`, `meed / meorde`, `navel / nafola`, `heaven / heofon`, `light / līehtan`, `coat / rocc`, `will / willa`, `yarn / ġearn`, `thistle / þistles`: all remain adequately cited, and no removed citation needed restoration.

## Remaining broad citations

| Entry | Source | Exact source-specific reason it remains broad | Category | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `birth / byrd` | `HoggPhonology1992` | Hogg still treats `byrd` within a broader deverbal-feminine cluster discussion rather than in one isolated clause. | claim-isolation | yes | Further split the sentence or find a source that states the exact simplex-noun point more locally. |
| `needle / nǣdl` | `HoggPhonology1992` | Hogg's `nidi / nǣdl` discussion remains embedded in a broader phonological cluster history. | claim-isolation | yes | Recast the sentence more narrowly or replace it with a different localizable source. |
| `ban / bannes` | `Campbell1959` | The nominative-apocope and geminate-simplification claim is still bundled more broadly than one safe Campbell locator allows. | claim-isolation | yes | Recast the nominative clause around a narrower section-safe statement. |
| `fright / fyrhte` | `RingeTaylor2014` | The nominative-remodeling versus oblique-inheritance contrast still behaves like distributed handbook synthesis. | claim-isolation | yes | Recover a page-safe clause for the exact in-stem contrast or narrow the prose further. |
| `shove / sċēaf` | `RingeTaylor2014` | The remaining class-II present-versus-preterite split sentence still compresses a broader argument than one page safely supports. | claim-isolation | yes | Split the synthesis sentence again or recover a directly matching Ringe-Taylor page. |
| `span / spanne` | `SieversBrunner1965` | The dative-singular paradigm background still depends on a broader paradigm discussion rather than one clean section-locatable clause. | claim-isolation | yes | Recast the paradigm-cell sentence around narrower localized evidence. |

## Upstream-only broad citations

The upstream-only broad queue remains **314** occurrences after this pass. Audit 08 continued to work only the generated-output queue, so upstream-only broad citations were not cleaned separately.

## Safety checks

- no OCR line numbers used: **yes**
- no file offsets used: **yes**
- no search-result positions used: **yes**
- no unverified PDF page indexes used: **yes**
- no invented page ranges: **yes**
- every new locator has evidence: **yes**
- generated Markdown and manifest are synchronized: **yes**
- no citation was removed solely to reduce the broad-citation count: **yes**
- no new binary PDFs/scans were added in audit 08: **yes**

## Recommendation

**C. Do human/prose review of remaining generated broad citations.**

Audit 08 appears to have harvested the last clean generated claim-isolation wins. The surviving six rows now skew toward genuinely broad handbook synthesis or awkward-to-split paradigm framing rather than toward obviously recoverable page or section locators.
