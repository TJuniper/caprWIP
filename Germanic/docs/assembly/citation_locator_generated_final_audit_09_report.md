# Citation locator generated-final audit 09 report

## Summary

- generated broad citations before: **6**
- generated broad citations after: **2**
- regular book-prose broad citations before: **1**
- regular book-prose broad citations after: **0**
- non-regular model-entry broad citations before: **319**
- non-regular model-entry broad citations after: **316**
- upstream-only broad citations before: **314**
- upstream-only broad citations after: **314**
- rows inspected: **12**
- locators added: **4**
- citations removed: **0**
- citations restored: **0**
- prose softened or revised for undercitation: **2**
- outputs regenerated or not: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed citation spans, counting an individual citation as broad only when its `@Source` item carries no locator suffix.
- generated Markdown count before edits: **6**
- regular book-prose count before edits: **1**
- non-regular model-entry count before edits: **319**
- upstream-only broad count before edits: **314**
- manifest matched generated Markdown before edits: **yes**
- generated Markdown count after edits: **2**
- regular book-prose count after edits: **0**
- non-regular model-entry count after edits: **316**
- upstream-only broad count after edits: **314**
- manifest matched generated Markdown after edits: **yes**

## Audit 08 spot-check

All six audit-08 locators remained safe and required no correction:

- `warp / weorpan` — `RingeTaylor2014, 195` and `197`
- `fast / festan` — `RingeTaylor2014, 110`
- `world / weorold` — `SieversBrunner1965, §113`
- `learn (iptv.2sg) / liorna` — `Fulk2018, 127`
- `lick (iptv.2sg) / licca` — `RingeTaylor2014, 50`
- `lick (3sg) / liccaþ` — `RingeTaylor2014, 50`

The page or section markers remain visible, the cited forms or rules are present,
the prose does not overstate the sources, and the evidence rows remain accurate.

## Final six review

| Entry | Source | Current claim | Searches attempted | Locator added or retained broad | Final reason |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `birth / byrd` | `HoggPhonology1992` | Hogg supplies the deverbal-feminine setting for `byrd`. | `byrd`, `deverbal`, `birth`, `burden` | localized: `357` | Printed p. 357 directly lists `byrd 'birth, burden'` inside a deverbal-noun grouping, so the broad citation could be narrowed safely. |
| `needle / nǣdl` | `HoggPhonology1992` | Hogg includes `nidi / nǣdl` in the broader cluster history. | `nidi`, `needle`, `syllabic`, `epenthetic` | localized: `95` | Printed p. 95 directly lists `nidi 'needle'` in the syllabic-sonorant discussion, so the background clause is now page-safe. |
| `ban / bannes` | `Campbell1959` | The nominative comparison `*bánną > ban` depends on final-vowel loss plus final-geminate simplification. | `ban`, `bannes`, `geminate`, `final unstressed`, `§345`, `§457` | retained broad | Campbell still supports the sentence only through distributed rule discussion, not one page-bound nominative clause. |
| `fright / fyrhte` | `RingeTaylor2014` | Later nominatives in `-u/-o` are analogically remodeled relative to the older in-stem history. | `fyrhte`, `fyrhtu`, `in-stem`, `analogical`, `abstract` | localized: `395-396` | The nominative-remodeling claim is explicit on pp. 395-396 once the oblique-conservative point is marked as project framing rather than as a direct source claim. |
| `shove / sċēaf` | `RingeTaylor2014` | The English present system belongs to a wider class-II split not identical with the preterite grade. | `skeuban`, `skūban`, `scēaf`, `scufan`, `class II`, `preterite`, `present` | retained broad | The current sentence still compresses distributed handbook discussion rather than one recoverable page-bound clause. |
| `span / spanne` | `SieversBrunner1965` | `*spánnai` is a selected dative-singular cell, not a rival headword. | `ō-stems`, `Dat. Sg.`, `obliquen Kasus`, `syncope`, `§252`, `§255` | localized: `§252; §255.2` | Recasting the sentence as grammar background allowed safe localization to the ō-stem paradigm and oblique-syncope sections. |

## Citation-retention and removal discipline

- citations retained broad because they still support useful claims: **2**
- citations removed: **0**
- why each removal was safe: **n/a**
- citations restored: **0**
- confirmation that no citation was removed solely to reduce the broad-citation count: **yes**

This pass stayed conservative. `birth`, `needle`, `fright`, and `span` were
localized only after a visible page or stable section could be tied to a
narrowed sentence. `ban` and `shove` remain broad because they still carry real
scholarly support that could not be turned into one locator without either
inventing a page-safe clause or stripping the prose down too far.

## Undercitation audit

The current watchlist is recorded in
`Germanic/docs/assembly/citation_locator_undercitation_watchlist_09.md`.

### `find / fundene`

`find / fundene` remains a stable control case. The entry still rests on
`RingeTaylor2014, 344`, `BosworthToller1898, 219`, `ClarkHall1960, 124`, and
project trace output. No Luick/Brunner-style analogical-leveling claim has
re-entered the prose.

### Other watchlist entries

- `birth / byrd`, `needle / nǣdl`, `fright / fyrhte`, and `span / spanne` are now adequately localized.
- `ban / bannes` and `shove / sċēaf` remain adequately cited, but intentionally broad.
- `still / stillan`, `loam / lām`, `think / þenċan`, `meed / meorde`, `have / hæfeþ`, and `rust / rust` remain adequately cited and required no restoration.

## Remaining generated broad citations

Two generated broad citations remain:

| Entry | Source | Exact source-specific reason it remains broad | Category | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `ban / bannes` | `Campbell1959` | The nominative comparison still relies on multiple Campbell rule discussions rather than one page-bound statement of `*bánną > ban`. | project-framing | yes | Rewrite the sentence around separately localized rule clauses or find a source that states the nominative outcome directly. |
| `shove / sċēaf` | `RingeTaylor2014` | The class-II present-versus-preterite background is still distributed across the handbook's broader verb-history discussion. | distributed-source-discussion | yes | Rewrite the sentence more radically or find a source that isolates the class split for this verb family. |

See `Germanic/docs/assembly/citation_locator_final_generated_broad_citations_09.md`.

## Upstream-only broad citations

The upstream-only broad queue remains **314** occurrences after this pass. Audit
09 continued to work only the generated-output queue, so upstream-only broad
citations were not cleaned separately.

## Safety checks

- no OCR line numbers used: **yes**
- no file offsets used: **yes**
- no search-result positions used: **yes**
- no unverified PDF page indexes used: **yes**
- no invented page ranges: **yes**
- every new locator has evidence: **yes**
- generated Markdown and manifest are synchronized: **yes**
- no citation was removed solely to reduce the broad-citation count: **yes**
- no new binary PDFs/scans were added: **yes**

## Recommendation

**D. Stop generated citation locator work because any remaining broad citations are explicitly justified.**

Audit 09 appears to have harvested the last clean generated-output wins. The
remaining `ban` and `shove` rows are now documented as justified broad
citations, with the unresolved issue being prose judgment rather than locator
recovery.
