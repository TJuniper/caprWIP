# Citation locator post-exhaustion audit 05 report

## Summary

- generated broad citations before: **30**
- generated broad citations after: **25**
- regular book-prose broad citations before: **5**
- regular book-prose broad citations after: **5**
- non-regular model-entry broad citations before: **339**
- non-regular model-entry broad citations after: **334**
- upstream-only broad citations before: **314**
- upstream-only broad citations after: **314**
- rows inspected: **30**
- locators added: **2**
- citations removed: **0**
- citations restored: **0**
- prose softened or revised for undercitation: **3**
- outputs regenerated: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed spans, including first-source detection in mixed citation spans.
- generated Markdown count before edits: **30**
- regular book-prose count before edits: **5**
- non-regular model-entry count before edits: **339**
- upstream-only broad count before edits: **314**
- manifest matched generated Markdown at pass start: **yes** — audit 04 ended with the manifest synchronized to the 30-row generated queue.
- generated Markdown count after edits: **25**
- regular book-prose count after edits: **5**
- non-regular model-entry count after edits: **334**
- upstream-only broad count after edits: **314**
- manifest matched generated Markdown at pass end: **yes** — rebuilt to the current 25-row generated queue.

## Audit 04 spot-check

The following audit-04 rows were spot-checked directly against the local witnesses and live prose:

- `three / þrīe` — `Kroonen2013, 586` — safe
- `have / hæfeþ` — `Kroonen2013, 237` — safe
- `meed / meorde` — corrected `RingeTaylor2014, 99` — safe

Audit 04 evidence discipline held up in all three cases. No correction or reversion was needed in this audit.

## Generated broad-row work

| Source | Rows inspected | Locators added | Prose softened | Witness/prep blockers | Broad retained | Notes |
| :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| Kroonen2013 | 2 | 0 | 0 | 2 | 0 | Both remaining Kroonen rows are now explicitly marked as source-preparation-needed; the audit-04 `three` and `have` locators were spot-checked and held. |
| Orel2003 | 3 | 0 | 0 | 3 | 0 | All three remaining Orel rows remain page-recovery problems rather than evidentiary failures. |
| BosworthToller1898 | 2 | 0 | 0 | 2 | 0 | Both remaining Bosworth-Toller rows are now explicitly classed as source-preparation-needed because the multi-column OCR is still not page-safe. |
| KlugeSeebold2011 | 6 | 0 | 0 | 6 | 0 | All six remaining Kluge rows remain blocked by the absence of a paginated local witness. |
| Campbell1959 | 3 | 1 | 1 | 0 | 1 | Localized `man / mannes` to `§621`, softened the Campbell derivational sentence in `fright / fyrhte`, and retained `ban / bannes` broad. |
| RingeTaylor2014 | 7 | 0 | 1 | 0 | 6 | Softened the analogical `fast / festan` sentence to project framing and retained the other class-history rows broad where no single safer page was recovered. |
| HoggPhonology1992 | 2 | 0 | 0 | 0 | 2 | Both Hogg rows remain honestly broad cluster-history citations. |
| Fulk2018 | 1 | 0 | 0 | 0 | 1 | The single Fulk row remains broad because the exact learn-family page is still unverified. |
| SieversBrunner1965 | 4 | 1 | 1 | 0 | 2 | Localized `lap / lappa` to `§10`, softened the `wolf / wulf` control sentence to project framing, and retained the distributed paradigm/background rows broad. |
| other sources | 0 | 0 | 0 | 0 | 0 | No other source families were reopened in the generated queue during audit 05. |

## Claim-isolation results

- Localized **`lap / lappa`** from broad `SieversBrunner1965` to **`§10`**.
- Localized **`man / mannes`** from broad `Campbell1959` to **`§621`** and recast the sound-change chain as project framing.
- Softened the analogical sentence in **`fast / festan`** to project framing, removing one unsupported broad Ringe-Taylor attribution while retaining the class-history citation.
- Softened the Campbell derivational sentence in **`fright / fyrhte`** to project framing because the exact section for the `-e < -i < -in` formula was still not safely isolated.
- Softened the high-vowel control sentence in **`wolf / wulf`** to project framing and relied on the already localized `SieversBrunner1965, §160` evidence elsewhere in the entry.
- Retained the remaining claim-isolation rows broad where the source support is real but still distributed across class-history, paradigm, or background discussion.

## Source-witness results

- **KlugeSeebold2011:** six remaining generated rows (`still` x2, `knight`, `neck`, `sieve`, `world`) are now explicitly marked **source_witness_needed**. The OCR evidence is real, but every local Kluge witness remains unpaginated.
- **Orel2003:** three rows (`loam`, `neck`, `world`) are now explicitly marked **source_preparation_needed**. The entries are present in local vision text, but the offsets are not safe printed pages.
- **BosworthToller1898:** two rows (`think`, `loam`) are now explicitly marked **source_preparation_needed** because the multi-column OCR still does not bind the headwords to safe printed pages.
- **Kroonen2013:** two rows (`fast`, `wolf`) are now explicitly marked **source_preparation_needed** because the local vision witness confirms the entries but not safe printed pages.

The generated queue is now smaller because the remaining easy claim-isolation fixes were taken in source prose, while the unresolved dictionary rows are documented as explicit witness/preparation blockers instead of being left under vague “acceptable for now” language.

## Citation-retention and removal discipline

- citations retained broad because they still support useful claims: **25**
- citations removed: **0**
- citations restored: **0**
- three generated broad rows disappeared because the prose was softened to explicit project framing, not because support was deleted as redundant.
- two generated broad rows disappeared because verified locators were added (`lap / lappa`, `man / mannes`).
- no citation was removed solely to reduce the broad-citation count.

## Undercitation audit

The current watchlist is recorded in `citation_locator_undercitation_watchlist_05.md`.

### `find / fundene`

`find / fundene` remains a stable control case. The entry still rests on `RingeTaylor2014, 344`, `BosworthToller1898, 219`, and `ClarkHall1960, 124`, and the selected-cell comparison remains explicit project framing based on cited forms and trace output. No Luick/Brunner-style analogical-leveling claim has re-entered the prose.

### Other watchlist entries

- `still / stillan`: still adequately cited; the remaining broad Kluge rows are now explicitly documented as witness-blocked rather than merely deferred.
- `navel / nafola`, `have / hæfeþ`, `meed / meorde`: all remain adequately cited, and the audit-04 locators/correction held up under spot-checking.
- `think / þenċan`: still adequately cited, with the remaining Bosworth-Toller support now explicitly marked as source-preparation-needed.
- `man / mannes`: now better supported because `Campbell1959` has been localized to `§621` and the sound-change chain is explicit project framing.
- `rust / rust`, `heaven / heofon`, `light / līehtan`, `coat / rocc`, `will / willa`, `yarn / ġearn`, `thistle / þistles`: no removed citation needs restoration and no undercitation problem reopened in this pass.

## Remaining broad citations

| Entry | Source | Exact source-specific reason it remains broad | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- |
| birth / byrd | HoggPhonology1992 | Hogg still treats _byrd_ within a broader deverbal-feminine cluster discussion rather than on one page devoted to the simplex noun alone. | yes | Keep the broad handbook citation unless the sentence is split to isolate the exact deverbal-feminine point. |
| still / stillan | KlugeSeebold2011 | The local Kluge OCR confirms the wider _still/stillen_ family, but every local witness remains unpaginated. | yes | Use a paginated Kluge-Seebold witness or another page-labeled comparative dictionary for the same entry. |
| still / stillan | KlugeSeebold2011 | The adjective-versus-verb family framing is visible in local Kluge OCR, but no local witness provides safe printed page markers. | yes | Use a paginated Kluge-Seebold witness or recast the family note around already localized sources only. |
| think / þenċan | BosworthToller1898 | The Bosworth-Toller headword support for _þencan_/_geþencan_ is real, but the current multi-column OCR still does not bind the entry to a safe printed page. | yes | Recover a page-safe Bosworth-Toller page map or another paginated witness for the headword. |
| warp / weorpan | RingeTaylor2014 | The Ringe-Taylor discussion still supports the preterite-versus-infinitive distinction behind the selected verbal input, but the exact page for that contrast remains distributed across the class discussion. | yes | Retain broad unless the preterite/infinitive contrast is split from the rest of the derivational sentence. |
| fast / festan | Kroonen2013 | The local Kroonen witness confirms the _*fastu- / *fasten-_ family, but the available vision-text offsets are not page-safe for a printed locator. | yes | Recover the printed Kroonen page from a PDF/page image or keep the broad family framing. |
| fast / festan | RingeTaylor2014 | Ringe and Taylor still provide the comparative class-history argument distinguishing the wider _*fastēną_ family from the class-I verb reflected in Old English, but not on a single isolated page for this sentence. | yes | Retain broad unless a safer page for the class-history clause is recovered. |
| knight / cniht | KlugeSeebold2011 | The local Kluge OCR confirms the _*knehta-_ family, but no paginated local witness is available. | yes | Use a paginated Kluge-Seebold witness or another page-labeled comparative dictionary for the same family. |
| loam / lām | Orel2003 | Orel still supports the _*laimōn_ / _*laiman-_ loam family, but the current local witness does not yield a safe printed page for the entry. | yes | Recover the exact Orel page from a PDF/page image or keep the comparative-family citation broad. |
| loam / lām | BosworthToller1898 | The Bosworth-Toller headword support for _lām_ is present, but the multi-column OCR still does not bind the dictionary entry to a safe printed page. | yes | Recover a page-safe Bosworth-Toller witness or keep the broad corroborating dictionary citation. |
| neck / hnecca | KlugeSeebold2011 | The local Kluge OCR confirms the a-grade _Nacken_ family comparison, but the witness is unpaginated. | yes | Use a paginated Kluge-Seebold witness for the _Nacken_ entry. |
| neck / hnecca | Orel2003 | Orel still preserves the competing a-grade neck-family label, but the available local witness does not safely recover the printed article page. | yes | Recover the exact Orel page from a PDF/page image or keep the comparative label broad. |
| needle / nǣdl | HoggPhonology1992 | Hogg treats _nidi_ / _nǣdl_ inside a broader cluster-history discussion rather than in a single page-localizable entry note. | yes | Keep the broad handbook citation unless the historical-background sentence is split further. |
| sieve / sife | KlugeSeebold2011 | The local Kluge OCR confirms the West Germanic _*sibi-_ line, but the witness is unpaginated. | yes | Use a paginated Kluge-Seebold witness for the sieve entry. |
| world / weorold | Orel2003 | Orel still preserves the older _*wira-_ vocalism tradition, but the local witness does not safely recover the printed page for the world-family article. | yes | Recover the exact Orel page from a PDF/page image or keep the comparative vocalism citation broad. |
| world / weorold | KlugeSeebold2011 | The local Kluge OCR confirms compound _*wira-aldō_ beside simplex _*wera-_, but the witness is unpaginated. | yes | Use a paginated Kluge-Seebold witness for the world-family entry. |
| world / weorold | SieversBrunner1965 | The Sievers-Brunner citation still covers a distributed paradigm set (_weorold / world / wurold_) rather than one safely isolatable section. | yes | Retain broad unless the variant-set sentence is split into a narrower localized clause. |
| ban / bannes | Campbell1959 | The Campbell citation still supports the nominative _ban_ versus medial-geminate _bannes_ contrast, but the apocope-plus-simplification claim remains bundled across the derivational sentence. | yes | Retain broad unless a safer Campbell section for the nominative simplification clause is recovered. |
| fright / fyrhte | RingeTaylor2014 | Ringe and Taylor still support the nominative-remodeling versus oblique-inheritance contrast, but the exact page for this specialized in-stem comparison remains distributed. | yes | Retain broad unless the nominative-remodeling clause can be isolated to a verified page. |
| shove / sċēaf | RingeTaylor2014 | The Ringe-Taylor discussion still supplies the wider class-II present-versus-preterite split behind the selected _sċēaf_ cell, but the supporting discussion is not isolated to one page. | yes | Retain broad unless the class-II split clause is separated from the rest of the paragraph. |
| span / spanne | SieversBrunner1965 | The Sievers-Brunner citation still supplies the dative-singular paradigm background behind _spanne_, but the support is distributed across the paradigm discussion rather than one clean section. | yes | Retain broad unless the paradigm-cell sentence is recast around already localized Seebold and Clark Hall evidence. |
| learn (iptv.2sg) / liorna | Fulk2018 | Fulk still provides comparative learn-family background for _*liznō-_ here, but the exact page for this clause has not yet been verified safely. | yes | Retain broad until the precise Fulk page is recovered. |
| lick (iptv.2sg) / licca | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the West Germanic class-II weak-verb family background behind imperative _licca_; the finite-cell ending claim is already localized separately to p. 80. | yes | Retain broad family framing unless a page-localized Ringe-Taylor discussion of the lick family is recovered. |
| lick (3sg) / liccaþ | RingeTaylor2014 | The remaining Ringe-Taylor citation still supplies the West Germanic class-II weak-verb family background behind 3sg _liccaþ_; the stable-`a` ending claim is already localized separately to p. 80. | yes | Retain broad family framing unless a page-localized Ringe-Taylor discussion of the lick family is recovered. |
| wolf / wulf | Kroonen2013 | The local Kroonen witness confirms _*wulfa-_ as the inherited wolf-family headword, but the current witness does not safely recover the printed page. | yes | Recover the exact Kroonen page from a PDF/page image or keep the comparative-family citation broad. |

## Upstream-only broad citations

The upstream-only broad queue remains **314** occurrences after this pass. Audit 05 did not work upstream-only citations directly because the focus remained the generated-output bottleneck; however, the queue is now even more clearly split between (a) claim-isolation work largely exhausted in generated output and (b) source-preparation work still needed for Kluge/Orel/Bosworth/Kroonen.

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

**B. Do a source-preparation pass for Kluge/Orel/Bosworth.**

Audit 05 took the easy remaining claim-isolation fixes and reduced the generated queue from **30 -> 25**. The stubborn remainder is now dominated by explicit witness/preparation blockers rather than fuzzy review debt, so the next highest-value pass is to recover paginated witnesses or page-safe PDF anchors for Kluge-Seebold, Orel, Bosworth-Toller, and the remaining Kroonen entries before moving on to upstream-only cleanup.
