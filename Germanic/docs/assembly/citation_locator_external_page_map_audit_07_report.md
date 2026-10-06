# Citation locator external/page-map audit 07 report

## Summary

- generated broad citations before: **19**
- generated broad citations after: **12**
- regular book-prose broad citations before: **4**
- regular book-prose broad citations after: **2**
- non-regular model-entry broad citations before: **329**
- non-regular model-entry broad citations after: **324**
- upstream-only broad citations before: **314**
- upstream-only broad citations after: **314**
- rows inspected: **13**
- locators added: **7**
- citations removed: **0**
- citations restored: **0**
- Kluge rows resolved / still blocked: **6 / 0**
- Bosworth loam resolved / still blocked: **1 / 0**
- outputs regenerated or not: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed citation spans, including multiline citation spans.
- generated Markdown count before edits: **19**
- regular book-prose count before edits: **4**
- non-regular model-entry count before edits: **329**
- upstream-only broad count before edits: **314**
- manifest matched generated Markdown before edits: **yes**
- generated Markdown count after edits: **12**
- regular book-prose count after edits: **2**
- non-regular model-entry count after edits: **324**
- upstream-only broad count after edits: **314**
- manifest matched generated Markdown after edits: **yes**

Every broad citation still present in `lexical_volume_regular_compact_alpha_01.md` is now represented in `citation_locator_remaining_master.tsv`.

## Audit 06 spot-check

- `BosworthToller1898, 442`: **safe**
- `Kroonen2013, 171`: **safe**
- `Orel2003, 272`: **safe**
- `Orel2003, 218`: **safe**
- `Orel2003, 501`: **safe**
- `Kroonen2013, 638`: **safe**

The printed page markers remain visible in the local witnesses, the cited forms are present, and the current prose does not overstate those pages.

## Kluge-Seebold witness recovery

| Entry | Local witnesses checked | External witnesses checked | Entry evidence found | Page evidence found? | Locator added or retained broad | What still needs to happen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| still / stillan (`still`, `stillen`) | `docs/references/kluge_seebold_etymologisches_woerterbuch.txt`; new `docs/references/kluge_seebold_etymologisches_woerterbuch.pdf` | earlier preview/search checks only; no usable page-safe external preview | `still Adj ... ae. stille ... stilla 'stillen'` | yes — printed p. **885** | locator added | nothing |
| still / stillan (`stille`, `stillan`) | same local TXT/PDF pair | earlier preview/search checks only; no usable page-safe external preview | `stillen Vsw ... Wie ae. stillan ... abgeleitet von still` | yes — printed p. **886** | locator added | nothing |
| knight / cniht (`*knehta-`, `cniht`) | same local TXT/PDF pair | earlier preview/search checks only; no usable page-safe external preview | `Knecht ... Aus wg. *knehta- m. ... ae. cniht` | yes — printed p. **506** | locator added | nothing |
| neck / hnecca (`hnecca`, `Nacken`) | same local TXT/PDF pair | earlier preview/search checks only; no usable page-safe external preview | `Genick ... afr. hnekka m., ae. hnecca m. 'Nacken'. Dieses steht im Ablaut zu Nacken` | yes — printed p. **347** | locator added | nothing |
| sieve / sife (`*sibi-`, `sife`) | same local TXT/PDF pair | earlier preview/search checks only; no usable page-safe external preview | `Sieb ... Aus wg. *sibi- n. (o.ä.) ... ae. sife` | yes — printed p. **847** | locator added | nothing |
| world / weorold (`*wira-aldō`, `weorold`) | same local TXT/PDF pair | earlier preview/search checks only; no usable page-safe external preview | `Welt ... Aus wg. *wira-aldo ... auch in ae. weorold` | yes — printed p. **981** | locator added | nothing |

Audit 07 also copied the newly found Kluge PDF into the repo at `docs/references/kluge_seebold_etymologisches_woerterbuch.pdf`, updated the `docs/refs.bib` file pointer to that paginated witness, and recorded the exact target pages in `Germanic/docs/assembly/source_page_maps/kluge_seebold_2011_target_page_map.tsv`.

## Bosworth-Toller loam recovery

- witnesses checked: `docs/references/bosworth_toller_anglo_saxon_dictionary.pdf`; `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`; `docs/references/bosworth_toller_anglo_saxon_dictionary.txt`
- forms searched: `lām`, `lam`, `laam`, `lám`, `loam`, `clām`, `clay`, `mud`, `earth`
- whether `lām` was found with printed page evidence: **yes**
- why `clām` is not enough, if still unresolved: **n/a**
- whether locator was added or retained broad: **locator added**

The local Bosworth PDF text layer yields `lam. Add: Lim hoc argillum ... Ic eom lame` with the printed page marker **604** on the same page. That is the exact headword evidence the audit had been missing, so the broad `BosworthToller1898` citation for `loam / lām` could be localized safely.

## Claim-isolation check

No additional claim-isolation locators were added in this pass. Audit 07 prioritized the newly available Kluge and Bosworth page-safe witnesses; the remaining twelve generated broad citations still look like sentence-splitting or section-isolation problems rather than witness-preparation problems.

## Citation-retention and removal discipline

- citations retained broad because they still support useful claims: **12**
- citations removed: **0**
- why each removal was safe: **n/a**
- citations restored: **0**
- confirmation that no citation was removed solely to reduce the broad-citation count: **yes**

This pass stayed conservative. Once the page-safe Kluge and Bosworth witnesses existed, the affected citations were localized rather than removed. Earlier removed Kluge cases such as `will / willa` and `thistle / þistles` were rechecked through the undercitation watchlist and did not require restoration.

## Undercitation audit

The current watchlist is recorded in `Germanic/docs/assembly/citation_locator_undercitation_watchlist_07.md`.

### `find / fundene`

`find / fundene` remains a stable control case. The entry still rests on `RingeTaylor2014, 344`, `BosworthToller1898, 219`, `ClarkHall1960, 124`, and project trace output. No Luick/Brunner-style analogical-leveling claim has re-entered the prose.

### Other watchlist entries

- `still / stillan`: now localized to `KlugeSeebold2011, 885` and `886`; no restoration needed.
- `think / þenċan`: audit-06 Bosworth p. 442 held up under spot-check.
- `loam / lām`: now localized to `BosworthToller1898, 604`.
- `man / mannes`, `have / hæfeþ`, `rust / rust`, `meed / meorde`, `navel / nafola`, `heaven / heofon`, `light / līehtan`, `coat / rocc`, `will / willa`, `yarn / ġearn`, `thistle / þistles`: all remain adequately cited, and no removed citation needed restoration.

## Remaining broad citations

| Entry | Source | Exact source-specific reason it remains broad | Category | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- | :--- |
| birth / byrd | HoggPhonology1992 | Hogg still treats _byrd_ within a broader deverbal-feminine cluster discussion rather than on one page devoted to the simplex noun alone. | claim-isolation | yes | Keep the broad handbook citation unless the sentence is split to isolate the exact deverbal-feminine point. |
| warp / weorpan | RingeTaylor2014 | The Ringe-Taylor discussion still supports the preterite-versus-infinitive distinction behind the selected verbal input, but the exact page for that contrast remains distributed across the class discussion. | claim-isolation | yes | Retain broad unless the preterite/infinitive contrast is split from the rest of the derivational sentence. |
| fast / festan | RingeTaylor2014 | Ringe and Taylor still provide the comparative class-history argument distinguishing the wider _*fastēną_ family from the class-I verb reflected in Old English, but not on a single isolated page for this sentence. | claim-isolation | yes | Retain broad unless a safer page for the class-history clause is recovered. |
| needle / nǣdl | HoggPhonology1992 | Hogg treats _nidi_ / _nǣdl_ inside a broader cluster-history discussion rather than in a single page-localizable entry note. | claim-isolation | yes | Keep the broad handbook citation unless the historical-background sentence is split further. |
| world / weorold | SieversBrunner1965 | The Sievers-Brunner citation still covers a distributed paradigm set (_weorold / world / wurold_) rather than one safely isolatable section. | claim-isolation | yes | Retain broad unless the variant-set sentence is split into a narrower localized clause. |
| ban / bannes | Campbell1959 | The Campbell citation still supports the nominative _ban_ versus medial-geminate _bannes_ contrast, but the apocope-plus-simplification claim remains bundled across the derivational sentence. | claim-isolation | yes | Retain broad unless a safer Campbell section for the nominative simplification clause is recovered. |
| fright / fyrhte | RingeTaylor2014 | Ringe and Taylor still support the nominative-remodeling versus oblique-inheritance contrast, but the exact page for this specialized in-stem comparison remains distributed. | claim-isolation | yes | Retain broad unless the nominative-remodeling clause can be isolated to a verified page. |
| shove / sċēaf | RingeTaylor2014 | The Ringe-Taylor discussion still supplies the wider class-II present-versus-preterite split behind the selected _sċēaf_ cell, but the supporting discussion is not isolated to one page. | claim-isolation | yes | Retain broad unless the class-II split clause is separated from the rest of the paragraph. |
| span / spanne | SieversBrunner1965 | The Sievers-Brunner citation still supplies the dative-singular paradigm background behind _spanne_, but the support is distributed across the paradigm discussion rather than one clean section. | claim-isolation | yes | Retain broad unless the paradigm-cell sentence is recast around already localized Seebold and Clark Hall evidence. |
| learn (iptv.2sg) / liorna | Fulk2018 | Fulk still provides comparative learn-family background for _*liznō-_ here, but the exact page for this clause has not yet been verified safely. | claim-isolation | yes | Retain broad until the precise Fulk page is recovered. |
| lick (iptv.2sg) / licca | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the West Germanic class-II weak-verb family background behind imperative _licca_; the finite-cell ending claim is already localized separately to p. 80. | claim-isolation | yes | Retain broad family framing unless a page-localized Ringe-Taylor discussion of the lick family is recovered. |
| lick (3sg) / liccaþ | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the West Germanic class-II weak-verb family background behind 3sg _liccaþ_; the stable-`a` ending claim is already localized separately to p. 80. | claim-isolation | yes | Retain broad family framing unless a page-localized Ringe-Taylor discussion of the lick family is recovered. |

## Source-witness needs

See `Germanic/docs/assembly/citation_locator_source_witness_needs_07.md`.

## Upstream-only broad citations

The upstream-only broad queue remains **314** occurrences after this pass. Audit 07 did not work upstream-only citations directly because the focus remained the generated-output witness bottleneck. That bottleneck is now gone; the remaining generated queue is a claim-isolation queue.

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

**A. Continue generated broad-citation locator work.**

Audit 07 resolved the hard source-witness backlog by localizing all six `KlugeSeebold2011` rows and the `BosworthToller1898` `loam / lām` row. The remaining twelve generated broad citations are now claim-isolation rows, so the next pass should return to sentence splitting and narrower section/page recovery inside the already-known sources.
