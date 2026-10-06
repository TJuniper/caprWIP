# Citation locator source-preparation audit 06 report

## Summary

- generated broad citations before: **25**
- generated broad citations after: **19**
- regular book-prose broad citations before: **5**
- regular book-prose broad citations after: **4**
- non-regular model-entry broad citations before: **334**
- non-regular model-entry broad citations after: **329**
- upstream-only broad citations before: **314**
- upstream-only broad citations after: **314**
- rows inspected: **25**
- locators added: **6**
- citations removed: **0**
- citations restored: **0**
- source-witness rows resolved: **6**
- source-witness rows still blocked: **7**
- outputs regenerated or not: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed citation spans, including multiline citation spans.
- generated Markdown count before edits: **25**
- regular book-prose count before edits: **5**
- non-regular model-entry count before edits: **334**
- upstream-only broad count before edits: **314**
- manifest matched generated Markdown before edits: **yes**
- generated Markdown count after edits: **19**
- regular book-prose count after edits: **4**
- non-regular model-entry count after edits: **329**
- upstream-only broad count after edits: **314**
- manifest matched generated Markdown after edits: **yes**

Every broad citation still present in `lexical_volume_regular_compact_alpha_01.md` is now represented in `citation_locator_remaining_master.tsv`.

## Audit 05 spot-check

- `lap / lappa — SieversBrunner1965, §10`: **safe**
- `man / mannes — Campbell1959, §621`: **safe**
- corrections made: **none**

The local witnesses still show `lappa (laeppa; Pl. leappan)` in Brunner `§10` and `mann, man / mannes / menn` in Campbell `§621`, and the current prose does not overstate either section.

## Source-preparation results

### KlugeSeebold2011

- entries searched: `still / stillan` (`still`, `stillen`; `stille`, `stillan`), `knight / cniht` (`*knehta-`, `cniht`), `neck / hnecca` (`hnecca`, `Nacken`), `sieve / sife` (`*sibi-`, `sife`), `world / weorold` (`*wira-aldō`, `*wera-`)
- witnesses checked: `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`; `docs/refs.bib`
- paginated witness found or not: **not found**
- locators added or not: **0**
- rows still witness-blocked: **6**

The local Kluge OCR still confirms the relevant entries, but it remains unpaginated. `docs/refs.bib` also confirms that `KlugeSeebold2011` is a separate source from `Seebold1970`, so page-labeled material for the latter was not used to localize Kluge citations by proxy.

### Orel2003

- entries searched: `loam / lām`, `neck / hnecca`, `world / weorold`
- witnesses checked: `docs/references/orel_handbook_germanic_etymology.vision.txt`
- page-safe article recovery successes/failures: **3 successes / 0 failures**
- locators added or not: **3**
- rows still source-preparation-needed: **0**

Recovered locators:

- `loam / lām` -> `Orel2003, 272`
- `neck / hnecca` -> `Orel2003, 218`
- `world / weorold` -> `Orel2003, 501`

Each recovery was tied to a printed page marker in the local vision witness and logged in `citation_locator_primary_source_evidence.tsv`.

### BosworthToller1898

- headwords searched: `þencan`, `geþencan`, `lām`
- witnesses checked: `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`; `docs/references/bosworth_toller_anglo_saxon_dictionary.txt`
- page-safe recovery successes/failures: **1 success / 1 failure**
- locators added or not: **1**
- rows still source-preparation-needed: **1**

Recovered locator:

- `think / þenċan` -> `BosworthToller1898, 442`

Unresolved row:

- `loam / lām`: the local vision witness recovers `clām` on printed p. 139 ("mortar, mud, clay, paste"), but not a page-safe `lām` headword. That is useful search evidence, but not a safe locator for the current `lām` sentence.

### Kroonen2013

- entries searched: `fast / festan`, `wolf / wulf`
- witnesses checked: `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- page-safe recovery successes/failures: **2 successes / 0 failures**
- locators added or not: **2**
- rows still source-preparation-needed: **0**

Recovered locators:

- `fast / festan` -> `Kroonen2013, 171`
- `wolf / wulf` -> `Kroonen2013, 638`

For `fast / festan`, the prose was tightened to the page-safe `*fastu-` / derived `*fasten-` wording actually shown by the witness rather than forcing the page into a stronger `*fastēną` headword claim than it visibly supports.

## Claim-isolation check

The remaining non-witness rows were all re-inspected:

- `birth / byrd — HoggPhonology1992`
- `warp / weorpan — RingeTaylor2014`
- `fast / festan — RingeTaylor2014`
- `needle / nǣdl — HoggPhonology1992`
- `world / weorold — SieversBrunner1965`
- `ban / bannes — Campbell1959`
- `fright / fyrhte — RingeTaylor2014`
- `shove / sċēaf — RingeTaylor2014`
- `span / spanne — SieversBrunner1965`
- `learn (iptv.2sg) / liorna — Fulk2018`
- `lick (iptv.2sg) / licca — RingeTaylor2014`
- `lick (3sg) / liccaþ — RingeTaylor2014`

No new safe locators were added from this subset. These rows remain broad because the supporting discussion is still distributed across class history, paradigm background, or handbook framing rather than a single page-safe clause.

## Citation-retention and removal discipline

- citations retained broad because they still support useful claims: **19**
- citations removed: **0**
- why each removal was safe: **n/a**
- citations restored: **0**
- confirmation that no citation was removed solely to reduce the broad-citation count: **yes**

This pass followed the source-preparation brief conservatively. Even the unresolved `BosworthToller1898` loam row was retained broad rather than removed, because the current result is “better witness still needed,” not “citation definitely unusable.”

## Undercitation audit

The current watchlist is recorded in `Germanic/docs/assembly/citation_locator_undercitation_watchlist_06.md`.

### `find / fundene`

`find / fundene` remains a stable control case. The entry still rests on `RingeTaylor2014, 344`, `BosworthToller1898, 219`, `ClarkHall1960, 124`, and project trace output. No Luick/Brunner-style analogical-leveling claim has re-entered the prose.

### Other watchlist entries

- `still / stillan`: adequately cited; the two remaining Kluge rows are still witness-blocked but honest.
- `think / þenċan`: better anchored than before because `BosworthToller1898` is now localized to p. 442.
- `man / mannes`: audit-05 `Campbell1959, §621` held up under spot-check.
- `have / hæfeþ`, `rust / rust`, `meed / meorde`, `navel / nafola`, `heaven / heofon`, `light / līehtan`, `coat / rocc`, `will / willa`, `yarn / ġearn`, `thistle / þistles`: all remain adequately cited, and no removed citation needed restoration.

## Remaining broad citations

| Entry | Source | Exact source-specific reason it remains broad | Category | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- | :--- |
| birth / byrd | HoggPhonology1992 | Hogg still treats _byrd_ within a broader deverbal-feminine cluster discussion rather than on one page devoted to the simplex noun alone. | claim-isolation | yes | Keep the broad handbook citation unless the sentence is split to isolate the exact deverbal-feminine point. |
| still / stillan | KlugeSeebold2011 | The local Kluge OCR confirms the wider _still/stillen_ family, but every local witness remains unpaginated. | source-witness | yes | Use a paginated Kluge-Seebold witness or another page-labeled comparative dictionary for the same entry. |
| still / stillan | KlugeSeebold2011 | The adjective-versus-verb family framing is visible in local Kluge OCR, but no local witness provides safe printed page markers. | source-witness | yes | Use a paginated Kluge-Seebold witness or recast the family note around already localized sources only. |
| warp / weorpan | RingeTaylor2014 | The Ringe-Taylor discussion still supports the preterite-versus-infinitive distinction behind the selected verbal input, but the exact page for that contrast remains distributed across the class discussion. | claim-isolation | yes | Retain broad unless the preterite/infinitive contrast is split from the rest of the derivational sentence. |
| fast / festan | RingeTaylor2014 | Ringe and Taylor still provide the comparative class-history argument distinguishing the wider _*fastēną_ family from the class-I verb reflected in Old English, but not on a single isolated page for this sentence. | claim-isolation | yes | Retain broad unless a safer page for the class-history clause is recovered. |
| knight / cniht | KlugeSeebold2011 | The local Kluge OCR confirms the _*knehta-_ family, but no paginated local witness is available. | source-witness | yes | Use a paginated Kluge-Seebold witness or another page-labeled comparative dictionary for the same family. |
| loam / lām | BosworthToller1898 | The local Bosworth search recovered page-safe _clām_ material on p. 139, but not a page-safe _lām_ headword; the current citation therefore cannot yet be localized to the attested target noun. | source-preparation | yes | Recover a page-image/base-dictionary witness that shows _lām_ with a printed page, or keep the broad corroborating citation pending better source preparation. |
| neck / hnecca | KlugeSeebold2011 | The local Kluge OCR confirms the a-grade _Nacken_ family comparison, but the witness is unpaginated. | source-witness | yes | Use a paginated Kluge-Seebold witness for the _Nacken_ entry. |
| needle / nǣdl | HoggPhonology1992 | Hogg treats _nidi_ / _nǣdl_ inside a broader cluster-history discussion rather than in a single page-localizable entry note. | claim-isolation | yes | Keep the broad handbook citation unless the historical-background sentence is split further. |
| sieve / sife | KlugeSeebold2011 | The local Kluge OCR confirms the West Germanic _*sibi-_ line, but the witness is unpaginated. | source-witness | yes | Use a paginated Kluge-Seebold witness for the sieve entry. |
| world / weorold | KlugeSeebold2011 | The local Kluge OCR confirms compound _*wira-aldō_ beside simplex _*wera-_, but the witness is unpaginated. | source-witness | yes | Use a paginated Kluge-Seebold witness for the world-family entry. |
| world / weorold | SieversBrunner1965 | The Sievers-Brunner citation still covers a distributed paradigm set (_weorold / world / wurold_) rather than one safely isolatable section. | claim-isolation | yes | Retain broad unless the variant-set sentence is split into a narrower localized clause. |
| ban / bannes | Campbell1959 | The Campbell citation still supports the nominative _ban_ versus medial-geminate _bannes_ contrast, but the apocope-plus-simplification claim remains bundled across the derivational sentence. | claim-isolation | yes | Retain broad unless a safer Campbell section for the nominative simplification clause is recovered. |
| fright / fyrhte | RingeTaylor2014 | Ringe and Taylor still support the nominative-remodeling versus oblique-inheritance contrast, but the exact page for this specialized in-stem comparison remains distributed. | claim-isolation | yes | Retain broad unless the nominative-remodeling clause can be isolated to a verified page. |
| shove / sċēaf | RingeTaylor2014 | The Ringe-Taylor discussion still supplies the wider class-II present-versus-preterite split behind the selected _sċēaf_ cell, but the supporting discussion is not isolated to one page. | claim-isolation | yes | Retain broad unless the class-II split clause is separated from the rest of the paragraph. |
| span / spanne | SieversBrunner1965 | The Sievers-Brunner citation still supplies the dative-singular paradigm background behind _spanne_, but the support is distributed across the paradigm discussion rather than one clean section. | claim-isolation | yes | Retain broad unless the paradigm-cell sentence is recast around already localized Seebold and Clark Hall evidence. |
| learn (iptv.2sg) / liorna | Fulk2018 | Fulk still provides comparative learn-family background for _*liznō-_ here, but the exact page for this clause has not yet been verified safely. | claim-isolation | yes | Retain broad until the precise Fulk page is recovered. |
| lick (iptv.2sg) / licca | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the West Germanic class-II weak-verb family background behind imperative _licca_; the finite-cell ending claim is already localized separately to p. 80. | claim-isolation | yes | Retain broad family framing unless a page-localized Ringe-Taylor discussion of the lick family is recovered. |
| lick (3sg) / liccaþ | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the West Germanic class-II weak-verb family background behind 3sg _liccaþ_; the stable-`a` ending claim is already localized separately to p. 80. | claim-isolation | yes | Retain broad family framing unless a page-localized Ringe-Taylor discussion of the lick family is recovered. |

## Source-witness needs

See `Germanic/docs/assembly/citation_locator_source_witness_needs_06.md`.

## Upstream-only broad citations

The upstream-only broad queue remains **314** occurrences after this pass. Audit 06 did not work upstream-only citations directly because the focus remained the generated-output source-preparation bottleneck. The unresolved generated queue is now split between:

1. Kluge/Bosworth witness-preparation blockers.
2. A smaller claim-isolation remainder that still looks honest but not yet page-saturated.

## Safety checks

- no OCR line numbers used: **yes**
- no file offsets used: **yes**
- no search-result positions used: **yes**
- no unverified PDF page indexes used: **yes**
- no invented page ranges: **yes**
- every new locator has evidence: **yes**
- generated Markdown and manifest are synchronized: **yes**
- no citation was removed solely to reduce the broad-citation count: **yes**

## Recommendation

**B. Do deeper external-source/page-map research for named blockers.**

Audit 06 removed the recoverable Orel, Kroonen, and Bosworth `think` blockers and brought the generated queue down from **25 -> 19**. The highest-value unresolved work is now concentrated in six `KlugeSeebold2011` rows plus the ambiguous `BosworthToller1898` `loam / lām` row, all of which need better paginated witnesses rather than more sentence-level tightening.
