# Citation locator post-exhaustion audit 03 report

## Summary

- generated broad citations before: **49**
- generated broad citations after: **32**
- regular book-prose broad citations before: **8**
- regular book-prose broad citations after: **5**
- non-regular model-entry broad citations before: **355**
- non-regular model-entry broad citations after: **341**
- upstream-only broad citations before: **314**
- upstream-only broad citations after: **314**
- rows inspected: **49** (the full fresh-scan generated queue, including 2 drift rows omitted from the audit-02 manifest)
- locators added: **9**
- citations removed: **7**
- citations restored: **0**
- prose softened or revised for undercitation: **yes** — notably `have / hæfeþ` and `rust / rust`, plus source-matching revisions in `navel / nafola` and `dill / dile`
- outputs regenerated: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed spans, including first-source detection in mixed citation spans.
- generated Markdown count before edits: **49**
- regular book-prose count before edits: **8**
- non-regular model-entry count before edits: **355**
- upstream-only broad count before edits: **314**
- manifest matched generated Markdown at pass start: **no** — the fresh scan found **49** generated broad rows, while `citation_locator_remaining_master.tsv` still listed **47**. The missing rows were `breast / brēost` (`Kroonen2013`) and `sieve / sife` (`KlugeSeebold2011`).
- generated Markdown count after edits: **32**
- regular book-prose count after edits: **5**
- non-regular model-entry count after edits: **341**
- upstream-only broad count after edits: **314**
- manifest matched generated Markdown at pass end: **yes** — rebuilt to the current 32-row generated queue.

## Generated broad-row work

| Source | Rows inspected | Locators added | Citations removed | Broad retained | Notes |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Kroonen2013 | 9 | 2 | 2 | 5 | Added `breast / brēost` p. 114 and `navel / nafola` p. 420; removed redundant broad Kroonen rows from `dill / dile` and `lade / hladan`; retained broader staging/background rows for `three`, `fast`, `have`, and `wolf`. |
| Orel2003 | 4 | 0 | 0 | 4 | `loam`, `neck`, and `world` still need direct article recovery; no unsafe page guesses were added. |
| BosworthToller1898 | 2 | 0 | 0 | 2 | `think` and `loam` still need page-safe Bosworth-Toller headword recovery. |
| KlugeSeebold2011 | 8 | 0 | 3 | 5 | Removed redundant Kluge rows from `sap / sæp` (2) and `staff / stæf`; retained `still`, `knight`, `neck`, `sieve`, and `world` because the local witness remains unpaginated. |
| Campbell1959 | 9 | 3 | 0 | 6 | Localized `breast / brēost` to §115 and both `gall / ġealla` rows to §486; retained broader claim-bundled rows for `ban`, `fright`, and `man`. |
| RingeTaylor2014 | 10 | 3 | 0 | 7 | Localized `forlorn / lēosan` to p. 357, `smear / smierwan` to p. 263, and `meed / meorde` to p. 285; retained the more complex class-history rows for `warp`, `fast`, `fright`, `shove`, and `lick`. |
| HoggPhonology1992 | 2 | 0 | 0 | 2 | `birth / byrd` and `needle / nǣdl` remain broad background-history citations, not missing-evidence crises. |
| Fulk2018 | 3 | 1 | 1 | 2 | Localized `dill / dile` to p. 170; softened the `have / hæfeþ` sentence so the unlocalized Fulk citation could be removed; `learn / liorna` remains broad pending safer page verification. |
| SieversBrunner1965 | 7 | 1 | 0 | 6 | Localized `town / tūn` to §71; retained `lap`, `world`, `span`, and `wolf` where the grammar discussion still spans broader paradigm/background claims. |
| Other sources | 0 | 0 | 0 | 0 | No other generated broad rows were changed in this pass. |

## Citation-retention and removal discipline

- broad citations retained rather than removed because they still support useful claims: **32** current generated rows remain broad after this pass.
- citations removed: **7**
  1. `dill / dile` — broad `Kroonen2013` removed after the comparative contrast was recast around localized `Fulk2018, 170` plus localized OE dictionaries.
  2. `lade / hladan` — broad `Kroonen2013` removed because localized `RingeTaylor2014, 248` already supports the direct OE strong-verb line and the wider weak-verb family claim was demoted to project framing.
  3. `sap / sæp` — two broad `KlugeSeebold2011` rows removed because localized `Kroonen2013, 420`, `Orel2003, 319`, and `ClarkHall1960, 247` already cover the comparative and OE claims.
  4. `staff / stæf` — broad `KlugeSeebold2011` removed because localized `Kroonen2013, 471` and `Orel2003, 368` fully cover the stem-class disagreement.
  5. `have / hæfeþ` — broad `Fulk2018` removed after the finite-cell sentence was softened to explicit project framing.
  6. `rust / rust` — broad `RingeTaylor2014` removed after the lowering claim was recast around localized `Campbell1959, §115` plus explicit project analysis.
- citations restored: **0**
- no citation was removed solely to reduce the broad-citation count; every removal either depended on localized replacement support or on a prose revision that removed the source-backed claim itself.

## Undercitation audit

The current watchlist is recorded in `citation_locator_undercitation_watchlist_03.md`.

### `find / fundene`

`find / fundene` remains adequately cited. The entry still rests on `RingeTaylor2014, 344` for the inherited verb line, `BosworthToller1898, 219` for attested `fundene`, and `ClarkHall1960, 124` for participial background. Audit 03 confirmed that no Luick/Brunner-style analogical-leveling claim has crept back into the prose; the selected-cell comparison remains explicit project framing based on cited forms and trace output.

### Other watchlist entries

- `still / stillan`: still adequately cited; the surviving broad Kluge support is openly retained because the witness remains unpaginated.
- `navel / nafola`: improved; the broad Kroonen staging clause was replaced with localized `Kroonen2013, 420` and the prose now matches the actual entry content.
- `meed / meorde`: improved; the last broad Ringe-Taylor development sentence is now localized to p. 285.
- `think / þenċan`, `man / mannes`: still adequately cited, but one broad dictionary/grammar row remains in each because the exact page-safe witness was not yet recovered.
- `heaven / heofon`, `light / līehtan`, `coat / rocc`, `will / willa`, `yarn / ġearn`, `wind / windan`, `thistle / þistles`: no undercitation problem was reopened in this pass.

## Remaining broad citations

| Entry | Source | Exact source-specific reason it remains broad | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- |
| birth / byrd | HoggPhonology1992 | This surviving HoggPhonology1992 citation still supports the broader deverbal-feminine background behind simplex _byrd_ and its prefixed relatives. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| still / stillan | KlugeSeebold2011 | Kluge still supports the wider West Germanic _still/stillen_ family here, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available or localized comparative support fully replaces it. |
| still / stillan | KlugeSeebold2011 | Kluge still supports the adjective-versus-verb family framing in this form note, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available or the family note is recast around localized sources only. |
| think / þenċan | BosworthToller1898 | The Bosworth-Toller citation still supplies distinct Old English headword support for _þenċan_, and no page-safe headword witness was recovered in this pass. | yes | Keep the broad dictionary citation until a page-safe Bosworth-Toller headword witness is recovered or the clause is recast around localized evidence. |
| warp / weorpan | RingeTaylor2014 | This Ringe-Taylor citation still carries the preterite-versus-infinitive distinction behind the selected verbal input _*wérpaną_, and that discussion was not isolated to a safer page in this pass. | yes | Retain broad for now and isolate the exact Ringe-Taylor page if the sentence is kept in its current form. |
| three / þrīe | Kroonen2013 | The Kroonen citation still marks the broader numeral headword behind the selected _*θréjez_ cell, but the exact article page was not verified safely in this pass. | yes | Recover the exact Kroonen article page or soften the sentence to explicit project staging. |
| fast / festan | Kroonen2013 | The Kroonen citation still supplies only the broader _*fastēną_ family framing rather than the direct Old English class-I verb evidence. | yes | Either recover the exact Kroonen article page or soften the comparative-family sentence further. |
| fast / festan | RingeTaylor2014 | The Ringe-Taylor citation still supports the class-history distinction between the wider _*fastēną_ family and the class-I verb reflected in Old English. | yes | Isolate the exact Ringe-Taylor page for the class-history clause if the sentence remains combined. |
| fast / festan | RingeTaylor2014 | The remaining Ringe-Taylor citation still carries the analogical _æ_-form discussion behind _fæstan_ versus inherited _festan_. | yes | Either isolate the exact analogical-leveling page or soften the sentence to explicit project framing. |
| knight / cniht | KlugeSeebold2011 | Kluge still corroborates the _*knehta-_ family behind _cniht_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| lap / lappa | SieversBrunner1965 | The Sievers-Brunner citation still carries the weak-masculine background for the selected _lappa_ outcome, but the exact supporting section was not isolated safely in this pass. | yes | Retain broad for now or recast the sentence to rely only on already localized Campbell and dictionary evidence. |
| loam / lām | Orel2003 | The remaining Orel citation still supports the comparative _*laimōn_ / _*laiman-_ family behind _lām_, but the exact article page was not recovered safely. | yes | Recheck Orel with a tighter article search or soften the comparative-family sentence. |
| loam / lām | BosworthToller1898 | The remaining Bosworth-Toller citation still provides corroborating Old English dictionary support for _lām_, but no page-safe headword witness was recovered. | yes | Either recover a Bosworth-Toller page-safe lemma citation or leave the corroborating dictionary support broad. |
| neck / hnecca | KlugeSeebold2011 | Kluge still supplies the a-grade _Nacken_ family comparison for _hnecca_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| neck / hnecca | Orel2003 | The remaining Orel citation still marks the competing a-grade comparative label for the neck family, but the exact article page was not recovered safely. | yes | Retain broad for now and revisit with a better Orel article recovery. |
| needle / nǣdl | HoggPhonology1992 | The Hogg citation still provides broader cluster-history background for _nidi_ / _nǣdl_, rather than simple dictionary attestation. | yes | Retain broad for now or split the historical background away from the localized OE attestation. |
| sieve / sife | KlugeSeebold2011 | Kluge still serves as secondary comparative support for the West Germanic _*sibi-_ line behind _sife_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| world / weorold | Orel2003 | The remaining Orel citation still marks the older _*wira-_ vocalism in the _weorold_ family, but the actual article page was not recovered beyond an unsafe index pointer. | yes | Recover the actual Orel article page or soften the clause to explicit project framing. |
| world / weorold | KlugeSeebold2011 | Kluge still preserves the _*wira-aldō_ compound line behind _weorold_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| world / weorold | SieversBrunner1965 | The remaining Sievers-Brunner citation still carries the wider _weorold / world / wurold_ form set, which was not isolated to one safer section in this pass. | yes | Retain broad for now or split the orthographic/paradigmatic background from the localized Bright evidence. |
| ban / bannes | Campbell1959 | The Campbell citation still supports the nominative _ban_ contrast against medial-geminate _bannes_, but the combined apocope-plus-simplification clause was not isolated to a safer section. | yes | Retain broad for now and isolate the exact Campbell section if the comparison sentence is kept. |
| fright / fyrhte | RingeTaylor2014 | The Ringe-Taylor citation still carries the nominative-remodeling versus oblique-inheritance contrast behind _fyrhte_. | yes | Retain broad for now and isolate the exact Ringe-Taylor page if the analogical contrast remains in prose. |
| fright / fyrhte | Campbell1959 | The Campbell citation still carries the abstract-noun _-e < -i < -in_ development behind _fyrhte_, but the exact section was not safely isolated in this pass. | yes | Retain broad for now and isolate the exact Campbell section if the derivational sentence remains combined. |
| have / hæfeþ | Kroonen2013 | The Kroonen citation still provides broader class-III weak-verb family background for _habban_ beside the localized Ringe-Taylor present-stem discussion. | yes | Leave broad until the exact Kroonen article can be recovered safely. |
| man / mannes | Campbell1959 | The Campbell citation still supports the brightening-plus-unstressed-merger path behind _mannes_, but the combined rule chain was not isolated to a safer section in this pass. | yes | Retain broad for now and isolate the exact Campbell section if the derivational sentence remains combined. |
| shove / sċēaf | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the class-II present-versus-preterite split behind the selected _sċēaf_ cell, but not on an isolated page yet. | yes | Retain broad for now and isolate the exact class-II discussion page if the sentence remains combined. |
| span / spanne | SieversBrunner1965 | The remaining Sievers-Brunner citation still supplies the dative-singular paradigm background behind _spanne_, but the exact supporting section was not isolated safely. | yes | Retain broad for now or recast the paradigm sentence around already localized Seebold and Clark Hall evidence. |
| learn (iptv.2sg) / liorna | Fulk2018 | The Fulk citation still marks the _*liznō-_ learn-family background behind _liorna_, but the exact page was not verified safely in this pass. | yes | Retain broad for now and verify the exact Fulk page before narrowing the citation. |
| lick (iptv.2sg) / licca | RingeTaylor2014 | The Ringe-Taylor citation still supplies the West Germanic class-II weak-verb background behind imperative _licca_. | yes | Retain broad for now and verify the exact Ringe-Taylor page before narrowing the citation. |
| lick (3sg) / liccaþ | RingeTaylor2014 | The Ringe-Taylor citation still supplies the West Germanic class-II weak-verb background behind 3sg _liccaþ_. | yes | Retain broad for now and verify the exact Ringe-Taylor page before narrowing the citation. |
| wolf / wulf | Kroonen2013 | The Kroonen citation still supplies wider wolf-family background beside the localized Ringe-Taylor exception discussion. | yes | Retain broad until the direct Kroonen wolf article is recovered safely. |
| wolf / wulf | SieversBrunner1965 | The remaining Sievers-Brunner citation still frames the counterfactual high-vowel oblique comparison behind _wulf_, which has not yet been rewritten into fully explicit project framing. | yes | Either isolate the exact paradigm rule or soften the counterfactual sentence further. |


## Suspect audit-02 reasons corrected

1. `breast / brēost` (`Kroonen2013`) — audit 02 failed to carry this live generated broad row into the manifest at all. Audit 03’s fresh scan re-opened it, localized it to `Kroonen2013, 114`, and recorded the false-zero drift explicitly.
2. `sieve / sife` (`KlugeSeebold2011`) — audit 02 likewise missed this still-live generated broad row. Audit 03 re-added it to the queue and retained it broad with an explicit witness-limitation reason instead of leaving it invisible.
3. `navel / nafola` (`Kroonen2013`) — audit 02’s broad reason treated the citation as if Kroonen directly supported a syncopated `*nablô` headword. Audit 03 checked the witness and rewrote the clause to match the actual `*nablan-` navel entry localized at p. 420.
4. `have / hæfeþ` (`Fulk2018`) and `rust / rust` (`RingeTaylor2014`) — audit 02 left these as broad source-backed sentences even though the prose was really doing project framing. Audit 03 softened both sentences and removed the broad citations rather than pretending a safe locator existed.

## Upstream-only broad citations

The upstream-only broad queue remains substantial (**314** occurrences after this pass), but it is still outside the generated compact bottleneck for now. The post-edit count stays flat because this pass reduced generated broad rows and source-layer broad rows by the same amount. A separate upstream-only cleanup pass is still warranted, but generated-output trustworthiness remains the higher priority until the 32 live generated rows are reduced further.

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No invented page ranges were added.
- Every new locator added in this pass has a row in `citation_locator_primary_source_evidence.tsv`.
- Generated Markdown and the rebuilt `citation_locator_remaining_master.tsv` are synchronized at pass end.
- No citation was removed solely to reduce the broad-citation count.

## Recommendation

**A. Continue generated broad-citation locator work.**

The queue is materially smaller (**49 -> 32**), the manifest false-zero drift has been corrected, and the remaining rows now have source-specific reasons rather than audit-02 placeholders. The next pass should keep prioritizing generated-output rows, especially the remaining `RingeTaylor2014`, `Campbell1959`, `Orel2003`, and `Kroonen2013` claims that still look isolatable without sacrificing support.
