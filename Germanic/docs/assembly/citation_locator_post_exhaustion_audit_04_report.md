# Citation locator post-exhaustion audit 04 report

## Summary

- generated broad citations before: **32**
- generated broad citations after: **30**
- regular book-prose broad citations before: **5**
- regular book-prose broad citations after: **5**
- non-regular model-entry broad citations before: **341**
- non-regular model-entry broad citations after: **339**
- upstream-only broad citations before: **314**
- upstream-only broad citations after: **314**
- rows inspected: **32**
- locators added: **2**
- citations removed: **0**
- citations restored: **0**
- prose softened or revised for undercitation: **yes** — `meed / meorde` was corrected during the audit-03 spot-check so the detailed oblique-cell chain is explicit project framing while the Ringe locator now points to verified p. 99
- outputs regenerated: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed spans, including first-source detection in mixed citation spans.
- generated Markdown count before edits: **32**
- regular book-prose count before edits: **5**
- non-regular model-entry count before edits: **341**
- upstream-only broad count before edits: **314**
- manifest matched generated Markdown at pass start: **yes** — audit 03 had ended with the manifest synchronized to the 32-row generated queue.
- generated Markdown count after edits: **30**
- regular book-prose count after edits: **5**
- non-regular model-entry count after edits: **339**
- upstream-only broad count after edits: **314**
- manifest matched generated Markdown at pass end: **yes** — rebuilt to the current 30-row generated queue.

## Audit 03 spot-check

The following audit-03 locators were spot-checked directly against the local witnesses and live prose:

- `forlorn / lēosan` — `RingeTaylor2014, 357` — safe
- `smear / smierwan` — `RingeTaylor2014, 263` — safe
- `town / tūn` — `SieversBrunner1965, §71` — safe
- `breast / brēost` — `Campbell1959, §115` — safe
- `dill / dile` — `Fulk2018, 170` — safe
- `gall / ġealla` — `Campbell1959, §486` — safe
- `navel / nafola` — `Kroonen2013, 420` — safe
- `breast / brēost` — `Kroonen2013, 114` — safe
- `meed / meorde` — `RingeTaylor2014, 285` — **corrected**

Audit 03 evidence discipline held up for eight of the nine spot-checked locators. The one correction was `meed / meorde`: the direct `PGmc *mizdo > ... > OE meord ~ méd` line is on **p. 99** of the local Ringe witness, not p. 285. Audit 04 therefore changed the citation to `[@RingeTaylor2014, 99]` and narrowed the sentence so the fuller oblique-cell chain is explicit project framing rather than a claim attributed to Ringe and Taylor.

## Generated broad-row work

| Source | Rows inspected | Locators added | Citations removed | Broad retained | Notes |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Kroonen2013 | 4 | 2 | 0 | 2 | Added `three / þrīe` -> `Kroonen2013, 586` and `have / hæfeþ` -> `Kroonen2013, 237`; retained `fast / festan` and `wolf / wulf` broad because the comparative-family support is still real but not cleanly page-localized for the current prose. |
| Orel2003 | 3 | 0 | 0 | 3 | `loam`, `neck`, and `world` still need better article recovery; all three remain broad for source-specific comparative reasons. |
| BosworthToller1898 | 2 | 0 | 0 | 2 | `think` and `loam` still need a page-safe headword witness from a better Bosworth-Toller source. |
| ClarkHall1960 | 0 | 0 | 0 | 0 | No remaining generated broad rows were worked directly through Clark Hall in this pass. |
| KlugeSeebold2011 | 6 | 0 | 0 | 6 | All remaining Kluge rows still depend on an unpaginated local witness; none were removed because each still provides useful comparative framing. |
| Campbell1959 | 3 | 0 | 0 | 3 | `ban`, `fright`, and `man` remain broad because the relevant claims still bundle multiple rule steps more safely than the current witness isolates. |
| RingeTaylor2014 | 7 | 0 | 0 | 7 | `warp`, `fast` (2), `fright`, `shove`, and `lick` (2) remain broad because the class-history or analogical claims are still not cleanly isolatable to one verified page. The audit-03 `meed` locator was corrected during spot-checking. |
| HoggPhonology1992 | 2 | 0 | 0 | 2 | `birth` and `needle` remain broad background-history citations. |
| Fulk2018 | 1 | 0 | 0 | 1 | `learn (iptv.2sg) / liorna` still needs a safer page anchor if the citation is to be narrowed. |
| SieversBrunner1965 | 4 | 0 | 0 | 4 | `lap`, `world`, `span`, and `wolf` remain broad because the relevant paradigm/background claims still span more than one safely isolated section. |
| Luick1914 | 0 | 0 | 0 | 0 | No live generated broad rows required direct Luick work in this pass. |
| other sources | 0 | 0 | 0 | 0 | No other source families changed the generated broad queue in audit 04. |

## Citation-retention and removal discipline

- citations retained broad rather than removed because they still support useful claims: **30**
- citations removed: **0**
- citations restored: **0**
- the two broad rows that disappeared (`three / þrīe` and `have / hæfeþ`, both `Kroonen2013`) were resolved by adding verified locators, not by dropping support.
- no citation was removed solely to reduce the broad-citation count.

## Undercitation audit

The current watchlist is recorded in `citation_locator_undercitation_watchlist_04.md`.

### `find / fundene`

`find / fundene` remains a stable control case. The entry still rests on `RingeTaylor2014, 344`, `BosworthToller1898, 219`, and `ClarkHall1960, 124`, and the selected-cell comparison remains explicit project framing based on cited forms and trace output. No Luick/Brunner-style analogical-leveling claim has re-entered the prose.

### Other watchlist entries

- `still / stillan`: still adequately cited; the remaining broad Kluge rows are genuinely necessary pending a paginated witness.
- `navel / nafola`: still adequately cited; audit-04 spot-check confirmed the Kroonen p. 420 locator and revised wording.
- `meed / meorde`: still adequately cited after the audit-04 correction from `RingeTaylor2014, 285` to `99` and the shift to explicit project framing for the detailed chain.
- `think / þenċan`, `man / mannes`: still adequately cited, but each still carries one broad row because the page-safe Bosworth/Campbell witness has not yet been isolated.
- `rust / rust`, `have / hæfeþ`: still adequately cited; no removed citation needs restoration.
- `heaven / heofon`, `light / līehtan`, `coat / rocc`, `will / willa`, `yarn / ġearn`, `wind / windan`, `thistle / þistles`: no undercitation problem was reopened in this pass.

## Source-witness needs

The current witness blockers are collected in `citation_locator_source_witness_needs_04.md`.

- **KlugeSeebold2011** remains the main structural blocker: `still`, `knight`, `neck`, `sieve`, and `world` all still rely on an unpaginated local witness.
- **Orel2003** still needs better article recovery for `loam`, `neck`, and `world`.
- **BosworthToller1898** still needs a page-safe headword witness for `think` and `loam`.

These are now documented separately rather than hidden inside broad-citation reasons, which should make a later source-preparation pass easier to scope.

## Remaining broad citations

| Entry | Source | Exact source-specific reason it remains broad | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- |
| birth / byrd | HoggPhonology1992 | This surviving HoggPhonology1992 citation still supports the broader deverbal-feminine background behind simplex _byrd_ and its prefixed relatives. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| still / stillan | KlugeSeebold2011 | Kluge still supports the wider West Germanic _still/stillen_ family here, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available or localized comparative support fully replaces it. |
| still / stillan | KlugeSeebold2011 | Kluge still supports the adjective-versus-verb family framing in this form note, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available or the family note is recast around localized sources only. |
| think / þenċan | BosworthToller1898 | Bosworth-Toller still supplies distinct Old English headword support for _þenċan_, but the local multi-column OCR witness does not bind the relevant headword to a page safely enough to localize it. | yes | Recover a page-safe Bosworth-Toller headword witness or keep the broad dictionary support as corroboration. |
| warp / weorpan | RingeTaylor2014 | This Ringe-Taylor citation still carries the preterite-versus-infinitive distinction behind the selected verbal input _*wérpaną_, and that discussion was not isolated to a safer page in this pass. | yes | Retain broad for now and isolate the exact Ringe-Taylor page if the sentence is kept in its current form. |
| fast / festan | Kroonen2013 | Kroonen treats this family through adjective _*fastu-_ and secondary derived verb _*fasten-_, not through a clean standalone entry that directly localizes the class-I Old English verb claim used here. | yes | Keep the broad Kroonen citation for family framing unless the prose is softened further or a better comparative witness is found. |
| fast / festan | RingeTaylor2014 | The Ringe-Taylor citation still supports the class-history distinction between the wider _*fastēną_ family and the class-I verb reflected in Old English. | yes | Isolate the exact Ringe-Taylor page for the class-history clause if the sentence remains combined. |
| fast / festan | RingeTaylor2014 | The remaining Ringe-Taylor citation still carries the analogical _æ_-form discussion behind _fæstan_ versus inherited _festan_. | yes | Either isolate the exact analogical-leveling page or soften the sentence to explicit project framing. |
| knight / cniht | KlugeSeebold2011 | Kluge still corroborates the _*knehta-_ family behind _cniht_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| lap / lappa | SieversBrunner1965 | The Sievers-Brunner citation still carries the weak-masculine background for the selected _lappa_ outcome, but the exact supporting section was not isolated safely in this pass. | yes | Retain broad for now or recast the sentence to rely only on already localized Campbell and dictionary evidence. |
| loam / lām | Orel2003 | Orel still provides useful comparative support for the _*laimōn_ / _*laiman-_ loam family, but this pass did not recover a page-safe article in the available witness. | yes | Recover a page-safe Orel article or leave the comparative-family citation broad. |
| loam / lām | BosworthToller1898 | Bosworth-Toller still provides corroborating Old English dictionary support for _lām_, but the available OCR witness does not tie the headword to a page safely enough to localize it. | yes | Recover a page-safe Bosworth-Toller headword witness or keep the broad corroborating dictionary citation. |
| neck / hnecca | KlugeSeebold2011 | Kluge still supplies the a-grade _Nacken_ family comparison for _hnecca_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| neck / hnecca | Orel2003 | The remaining Orel citation still marks the competing a-grade comparative label for the neck family, but the exact article page was not recovered safely. | yes | Retain broad for now and revisit with a better Orel article recovery. |
| needle / nǣdl | HoggPhonology1992 | The Hogg citation still provides broader cluster-history background for _nidi_ / _nǣdl_, rather than simple dictionary attestation. | yes | Retain broad for now or split the historical background away from the localized OE attestation. |
| sieve / sife | KlugeSeebold2011 | Kluge still serves as secondary comparative support for the West Germanic _*sibi-_ line behind _sife_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| world / weorold | Orel2003 | Orel still preserves the older _*wira-_ vocalism tradition behind _weorold_, but this pass did not recover a page-safe article in the available witness. | yes | Recover a page-safe Orel world-family article or keep the broad vocalism citation as comparative framing. |
| world / weorold | KlugeSeebold2011 | Kluge still preserves the _*wira-aldō_ compound line behind _weorold_, but the local OCR witness remains unpaginated. | yes | Keep the broad citation openly until a paginated Kluge-Seebold witness is available. |
| world / weorold | SieversBrunner1965 | The remaining Sievers-Brunner citation still carries the wider _weorold / world / wurold_ form set, which was not isolated to one safer section in this pass. | yes | Retain broad for now or split the orthographic/paradigmatic background from the localized Bright evidence. |
| ban / bannes | Campbell1959 | The Campbell citation still supports the nominative _ban_ contrast against medial-geminate _bannes_, but the combined apocope-plus-simplification clause was not isolated to a safer section. | yes | Retain broad for now and isolate the exact Campbell section if the comparison sentence is kept. |
| fright / fyrhte | RingeTaylor2014 | The Ringe-Taylor citation still carries the nominative-remodeling versus oblique-inheritance contrast behind _fyrhte_. | yes | Retain broad for now and isolate the exact Ringe-Taylor page if the analogical contrast remains in prose. |
| fright / fyrhte | Campbell1959 | The Campbell citation still carries the abstract-noun _-e < -i < -in_ development behind _fyrhte_, but the exact section was not safely isolated in this pass. | yes | Retain broad for now and isolate the exact Campbell section if the derivational sentence remains combined. |
| man / mannes | Campbell1959 | The Campbell citation still supports the brightening-plus-unstressed-merger path behind _mannes_, but the combined rule chain was not isolated to a safer section in this pass. | yes | Retain broad for now and isolate the exact Campbell section if the derivational sentence remains combined. |
| shove / sċēaf | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the class-II present-versus-preterite split behind the selected _sċēaf_ cell, but not on an isolated page yet. | yes | Retain broad for now and isolate the exact class-II discussion page if the sentence remains combined. |
| span / spanne | SieversBrunner1965 | The remaining Sievers-Brunner citation still supplies the dative-singular paradigm background behind _spanne_, but the exact supporting section was not isolated safely. | yes | Retain broad for now or recast the paradigm sentence around already localized Seebold and Clark Hall evidence. |
| learn (iptv.2sg) / liorna | Fulk2018 | The Fulk citation still marks the _*liznō-_ learn-family background behind _liorna_, but the exact page was not verified safely in this pass. | yes | Retain broad for now and verify the exact Fulk page before narrowing the citation. |
| lick (iptv.2sg) / licca | RingeTaylor2014 | The Ringe-Taylor citation still supplies the West Germanic class-II weak-verb background behind imperative _licca_. | yes | Retain broad for now and verify the exact Ringe-Taylor page before narrowing the citation. |
| lick (3sg) / liccaþ | RingeTaylor2014 | The Ringe-Taylor citation still supplies the West Germanic class-II weak-verb background behind 3sg _liccaþ_. | yes | Retain broad for now and verify the exact Ringe-Taylor page before narrowing the citation. |
| wolf / wulf | Kroonen2013 | Kroonen still supplies broader wolf-family background, but the direct _*wulfa-_ article page was not safely recovered in this pass. | yes | Recover the direct Kroonen wolf article page or keep the broad comparative-family citation. |
| wolf / wulf | SieversBrunner1965 | The remaining Sievers-Brunner citation still frames the counterfactual high-vowel oblique comparison behind _wulf_, which has not yet been rewritten into fully explicit project framing. | yes | Either isolate the exact paradigm rule or soften the counterfactual sentence further. |


## Upstream-only broad citations

The upstream-only broad queue remains substantial (**314** occurrences after this pass), but it is still outside the generated compact bottleneck for now. Audit 04 kept the focus on generated-output trustworthiness and did not work upstream-only broad citations separately.

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No invented page ranges were added.
- Every new locator added in this pass has evidence in `citation_locator_primary_source_evidence.tsv`.
- Generated Markdown and the rebuilt `citation_locator_remaining_master.tsv` are synchronized at pass end.
- No citation was removed solely to reduce the broad-citation count.

## Recommendation

**A. Continue generated broad-citation locator work.**

The generated queue is smaller again (**32 -> 30**), and audit 04 also corrected the one unsafe audit-03 locator that surfaced during spot-checking. The next pass should keep pressing on the remaining `RingeTaylor2014`, `Campbell1959`, and witness-blocked dictionary rows while treating the Kluge/Orel/Bosworth witness shortages as explicit source-preparation tasks rather than reasons to discard support.
