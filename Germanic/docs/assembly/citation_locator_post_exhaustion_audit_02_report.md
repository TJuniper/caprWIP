# Citation locator post-exhaustion audit 02 report

## Summary

- generated broad citations before: **64**
- generated broad citations after: **47**
- upstream-only broad citations before: **201**
- upstream-only broad citations after: **213**
- rows inspected: **64** (the full 64-row generated queue inherited from audit 01)
- locators added: **11**
- citations removed: **6**
- citations restored: **0**
- prose softened or revised for undercitation: **yes** — notably `find / fundene`, plus sentence-level rewrites in `shilling`, `fright`, `hammer`, and `span`.
- outputs regenerated: **yes**

## Fresh scan

- scan method: bracketed Pandoc citation parser with per-source detection inside mixed spans, matching the audit 01 method.
- generated Markdown count: **47**
- regular book-prose count: **8**
- non-regular model-entry count: **256**
- manifest matched generated Markdown at pass start: **yes** (64 generated rows from audit 01).
- manifest matched generated Markdown at pass end: **yes** (rebuilt to 47 current generated rows).

## Generated broad-row work

| Source | Rows inspected | Locators added | Citations removed | Broad retained | Notes |
| :--- | ---: | ---: | ---: | ---: | :--- |
| Kroonen2013 | 10 | 3 | 0 | 7 | Two shilling rows and the youth row were localized; several comparative-headword rows remain broad and need either page recovery or project-framing softening. |
| Orel2003 | 5 | 1 | 1 | 3 | Gang was localized to p. 164; span’s Orel row was removed as redundant; loam/neck/world still need direct article recovery. |
| BosworthToller1898 | 6 | 2 | 2 | 2 | Fright and hammer gained locators; the fly row and one duplicate hammer dictionary half were removed as redundant; think and loam remain broad. |
| ClarkHall1960 | 5 | 3 | 2 | 0 | Fright, meed, and span gained locators; swan and ban no longer need a broad Clark Hall duplicate. |
| KlugeSeebold2011 | 9 | 0 | 1 | 8 | All remaining Kluge rows were re-verified in the OCR witness; none can yet be paginated safely. |
| Campbell1959 | 6 | 0 | 0 | 6 | Remaining rows are claim-complex handbook prose, not dictionary headwords; they need sentence splitting or section isolation. |
| RingeTaylor2014 | 11 | 0 | 0 | 11 | Remaining rows are mostly class-history or analogical-background sentences and were left for a future claim-isolation pass. |
| HoggPhonology1992 | 2 | 0 | 0 | 2 | Both remaining Hogg rows are broad background-form-note support, not missing-evidence crises. |
| Fulk2018 | 3 | 0 | 0 | 3 | Remaining Fulk rows support handbook-style formation claims and were not isolated further in this pass. |
| SieversBrunner1965 | 5 | 0 | 0 | 5 | Remaining Sievers-Brunner rows are paradigm/background claims that still need targeted section recovery. |
| BrightCassidyRingler1971 | 1 | 1 | 0 | 0 | The reopened show (3sg) row was localized to p. 383. |
| Kroonen2011 | 1 | 1 | 0 | 0 | The reopened knob row was localized to p. 297. |

## Undercitation audit

The watchlist review is recorded in `citation_locator_undercitation_watchlist_02.md`. The broad-citation work in this pass did **not** justify removing support merely to lower the count. Most watchlist entries remained adequately cited; where a surviving sentence still sounded too source-backed, the prose was softened rather than propped up with a guessed locator.

### `find / fundene`

`find / fundene` remains adequately cited after audit 02. The entry now rests on `RingeTaylor2014, 344` for the inherited verb line, `BosworthToller1898, 219` for attested `fundene`, and `ClarkHall1960, 124` for the participial stem background. Audit 02 further softened the phrase “not the cleanest inherited comparison” to make the cell choice explicitly project framing rather than an uncited scholarly claim, and Luick/Brunner were **not** restored.

## Successful recoveries

| Entry | Before | After | Action |
| :--- | :--- | :--- | :--- |
| fly / flēogan | [@BosworthToller1898] | Removed the redundant broad Bosworth-Toller support and left the localized Clark Hall and Bright citations in place. | citation_removed_as_redundant |
| gang / gang | [@Orel2003] | Localized the comparative noun citation to `[@Orel2003, 164]`. | locator_added |
| shilling / sċilling | [@Kroonen2013; @Orel2003, 377] | Rewrote the sentence to retain only the page-supported `*skeld-linga-` analysis and localized it to `[@Kroonen2013, 482]`. | sentence_split_and_locator_added |
| shilling / sċilling | [@Kroonen2013] | Localized the form note to `[@Kroonen2013, 482]`. | locator_added |
| swan / swanes | [@ClarkHall1960] | Removed the redundant broad Clark Hall citation and kept the localized Bright evidence. | citation_removed_as_redundant |
| withy / wīþiġ | [@KlugeSeebold2011; @Orel2003, 503] | Removed the broad Kluge-Seebold duplicate from the comparative-evidence sentence. | citation_removed_as_redundant |
| youth / ġeoguþ | [@Kroonen2013] | Localized the earlier etymological headword citation to `[@Kroonen2013, 316]`. | locator_added |
| ban / bannes | [@ClarkHall1960; @BosworthToller1898, 303] | Removed the redundant broad Clark Hall citation from the Old English evidence sentence. | citation_removed_as_redundant |
| fright / fyrhte | [@BosworthToller1898] | Localized the attested oblique form to `[@BosworthToller1898, 160]`. | locator_added |
| fright / fyrhte | [@ClarkHall1960] | Localized the adjective/verb distinction to `[@ClarkHall1960, 141]`. | locator_added |
| hammer / hameres | [@BosworthToller1898] | Localized the genitival `hameres` citation to `[@BosworthToller1898, 78]`. | locator_added |
| hammer / hameres | [@BosworthToller1898; @ClarkHall1960, 160] | Dropped the redundant broad Bosworth-Toller half from the mixed dictionary sentence. | citation_removed_as_redundant |
| meed / meorde | [@ClarkHall1960; @BosworthToller1898, 647] | Localized the competing `mēd` doublet citation to `[@ClarkHall1960, 214]`. | locator_added |
| span / spanne | [@Orel2003; @Seebold1970, 450] | Removed the redundant broad Orel citation from the reconstruction sentence. | citation_removed_as_redundant |
| span / spanne | [@ClarkHall1960] | Localized the citation noun support to `[@ClarkHall1960, 286]`. | locator_added |
| show (3sg) / sċēawaþ | [@BrightCassidyRingler1971] | Localized the finite-cell evidence to `[@BrightCassidyRingler1971, 383]`. | locator_added |
| knob / cnobba | [@Kroonen2011] | Localized the knob-family comparative citation to `[@Kroonen2011, 297]`. | locator_added |

## Remaining broad citations

| Entry | Source | Exact reason it remains broad | Acceptable for now? | What would be required to resolve it |
| :--- | :--- | :--- | :--- | :--- |
| birth / byrd | HoggPhonology1992 | This surviving HoggPhonology1992 citation still supports the broader deverbal-feminine background behind simplex _byrd_ and its prefixed relatives. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| forlorn / lēosan | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Kroonen reconstructs the verb under _\*leusan-_ and cites prefixed daughters such as Gothic _fra-liusan_ and Old English _for-lēosan_; Orel likewise gives Old English _for-leósan_ [@Kroonen2013, 374; @Orel2003, 282]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| smear / smierwan | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports the West Saxon versus Anglian/Mercian dialect split within the _smierwan_ family. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| still / stillan | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| still / stillan | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| think / þenċan | BosworthToller1898 | The surviving broad dictionary citation still supports the OE headword clause, but this pass did not recover a page-safe headword witness. | yes | Keep the broad dictionary citation until a page-safe headword witness is recovered or the OE-form clause is recast around an already localized source. |
| town / tūn | SieversBrunner1965 | This surviving SieversBrunner1965 citation still supports a combined scholarly claim rather than a single isolated fact: Kroonen cites _\*tūna-_ 'fenced area', while Orel gives _\*tūnan_ ~ _\*tūnaz_ [@Kroonen2013, 566; @Orel2003, 452]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| warp / weorpan | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Ringe and Taylor distinguish preterite _\*warp_ from infinitive _\*werpana_, and the selected input here is the verbal form _\*wérpaną_ [@RingeTaylor2014]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| three / þrīe | Kroonen2013 | This surviving Kroonen2013 citation now sits only on comparative-headword or staging prose: Kroonen cites the numeral under a broader stem-style reconstruction rather than under one Old English-ready paradigm cell [@Kroonen2013]. | yes | Either recover the exact article page or soften the sentence to explicit project framing. |
| breast / brēost | Campbell1959 | This surviving Campbell1959 citation still supports a combined scholarly claim rather than a single isolated fact: From _\*bréustą_, the regular Old English development gives _brēost_, with the expected _eu_ > _ēo_ vowel history [@Campbell1959]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| dill / dile | Kroonen2013 | This surviving Kroonen2013 citation now sits only on comparative-headword or staging prose: Kroonen treats the word as preserving evidence for both an i-stem and a ja-stem formation, with Old English _dile_ on one side and continental forms such as Old Saxon _dilli_ and Old High German _tilli_ on the other [@Kroonen2013]. | yes | Either recover the exact article page or soften the sentence to explicit project framing. |
| dill / dile | Fulk2018 | This surviving Fulk2018 citation still supports a combined scholarly claim rather than a single isolated fact: That stem-class distinction matters for the Old English consonant shape. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| fast / festan | Kroonen2013 | This surviving Kroonen2013 citation now sits only on comparative-headword or staging prose: Kroonen places the verb under a comparative headword _\*fastēną_, the wider Germanic family behind meanings such as 'make firm' and, in Old English, 'fast' [@Kroonen2013]. | yes | Either recover the exact article page or soften the sentence to explicit project framing. |
| fast / festan | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Kroonen places the verb under a comparative headword _\*fastēną_, the wider Germanic family behind meanings such as 'make firm' and, in Old English, 'fast' [@Kroonen2013]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| fast / festan | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: The _æ_-forms remain relevant, but they do not control the entry. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| gall / ġealla | Campbell1959 | This surviving Campbell1959 citation still supports a combined scholarly claim rather than a single isolated fact: Campbell also notes dialectal variation, contrasting West Saxon or Kentish _gealla_ with Anglian _galla_ [@Campbell1959]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| gall / ġealla | Campbell1959 | This surviving Campbell1959 citation still supports a combined scholarly claim rather than a single isolated fact: From _\*gállô_, the weak noun develops through the expected Old English history of the suffix and the regular breaking environment before _ll_, yielding _ġealla_ [@Campbell1959]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| knight / cniht | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| lade / hladan | Kroonen2013 | This surviving Kroonen2013 citation now sits only on comparative-headword or staging prose: Ringe and Taylor cite the strong verb _hladan_ directly [@RingeTaylor2014, 248]. | yes | Either recover the exact article page or soften the sentence to explicit project framing. |
| lap / lappa | SieversBrunner1965 | This surviving SieversBrunner1965 citation still supports a combined scholarly claim rather than a single isolated fact: Campbell explicitly lists _lappa_ among the forms with restored _a_ [@Campbell1959, §158]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| loam / lām | Orel2003 | The remaining Orel citation still sits on comparative-headword background that could not be anchored safely from the present witness. | yes | Recheck Orel with a tighter headword search or rewrite the comparative-background sentence. |
| loam / lām | BosworthToller1898 | The remaining Bosworth-Toller half is dictionary background beyond the already localized Clark Hall support and was not recovered to a safe printed page. | yes | Either recover a Bosworth-Toller page-safe lemma citation or drop the duplicate dictionary support. |
| navel / nafola | Kroonen2013 | The surviving broad Kroonen citation now supports only the comparative headword/staging clause and still lacks a verified article page. | yes | Keep the comparative-headword citation broad until the exact article page is recovered or the sentence is softened to project staging. |
| neck / hnecca | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| neck / hnecca | Orel2003 | The Orel row remains broad because the exact comparative article was not safely recoverable from the current witness. | yes | Retain broad for now and revisit with a better headword recovery. |
| needle / nǣdl | HoggPhonology1992 | This surviving HoggPhonology1992 citation still supports a combined scholarly claim rather than a single isolated fact: Clark Hall records the attested citation form _nǣdl_ [@ClarkHall1960, 210]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| sap / sæp | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| sap / sæp | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| staff / stæf | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| world / weorold | Orel2003 | The Orel row remains broad because the index pointer alone is not safe enough to cite as the article locator. | yes | Recover the actual article page before narrowing the Orel citation. |
| world / weorold | KlugeSeebold2011 | Source content was verified in the local Kluge OCR witness, but the available text preserves no printable page labels or page map. | yes | Keep the broad citation openly until a paginated witness of Kluge-Seebold is available. |
| world / weorold | SieversBrunner1965 | This surviving SieversBrunner1965 citation still supports a combined scholarly claim rather than a single isolated fact: Old English does not preserve a single isolated form. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| ban / bannes | Campbell1959 | This surviving Campbell1959 citation still supports a combined scholarly claim rather than a single isolated fact: From _\*bánnas_, the geminate remains medial before the case ending and the unstressed vowel develops regularly to give _bannes_. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| fright / fyrhte | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Ringe and Taylor treat the later nominative forms with _-u_ or _-o_ as analogically remodeled, whereas the oblique in-stem forms continue the older history more directly [@RingeTaylor2014]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| fright / fyrhte | Campbell1959 | This surviving Campbell1959 citation still supports a combined scholarly claim rather than a single isolated fact: From _\*fúrxtīnaz_, the oblique in-stem develops through the loss and weakening of the final ending and the regular OE history summarized by Campbell as _-e < -i < -in_ in this class of abstracts [@Campbell1959]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| have / hæfeþ | Kroonen2013 | The surviving Kroonen citation still supports comparative verb-family background but was not page-recoverable in this pass. | yes | Leave broad until the exact comparative verb entry can be recovered safely. |
| have / hæfeþ | Fulk2018 | This surviving Fulk2018 citation still supports a combined scholarly claim rather than a single isolated fact: The selected input _\*xábēθi_ is therefore the 3sg present cell rather than a rephrasing of the infinitive. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| man / mannes | Campbell1959 | This surviving Campbell1959 citation still supports a combined scholarly claim rather than a single isolated fact: From _\*mánnas_, Anglo-Frisian brightening yields _\*mánnæs_, and the later unstressed merger gives _\*mánnes_, hence _mannes_ [@Campbell1959]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| meed / meorde | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: From _\*mízdai_, rhotacism gives _\*mírdai_. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| shove / sċēaf | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Kroonen reconstructs the strong verb as _\*skeuban-_ ~ _\*skūban-_ and cites Old English present forms _scēofan_, _scūfan_ [@Kroonen2013, 444]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| span / spanne | SieversBrunner1965 | This surviving SieversBrunner1965 citation still supports a combined scholarly claim rather than a single isolated fact: Seebold gives Old English _spann_ under this noun family [@Seebold1970, 450]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| learn (iptv.2sg) / liorna | Fulk2018 | This surviving Fulk2018 citation still supports a combined scholarly claim rather than a single isolated fact: Ringe and Taylor give Old English _liornian_ ~ _leornian_ from a learn-family base of the _\*lizn-_ type [@RingeTaylor2014, 38], and Kroonen likewise keeps the weak verb as _\*liznōn-_ [@Kroonen2013, 380]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| lick (iptv.2sg) / licca | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Ringe and Taylor place the verb among the West Germanic class-II weak verbs, with PWGmc _\*li_/_ekkōn_ continuing as Old English _liccian_, Old Saxon _likkon_, and Old High German _lecchon_ [@RingeTaylor2014]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| lick (3sg) / liccaþ | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Ringe and Taylor place the verb among the West Germanic class-II weak verbs, with PWGmc _\*li_/_ekkōn_ continuing as Old English _liccian_, Old Saxon _likkon_, and Old High German _lecchon_ [@RingeTaylor2014]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| rust / rust | RingeTaylor2014 | This surviving RingeTaylor2014 citation still supports a combined scholarly claim rather than a single isolated fact: Under Campbell's regular lowering of stressed _u_ before a following mid or low vowel, the citation-form input gives _rost_, not _rust_ [@Campbell1959, §115]. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |
| wolf / wulf | Kroonen2013 | The surviving Kroonen row remains broad because the direct wolf article was not recovered safely from the current witness. | yes | Retain broad until the direct Kroonen wolf article is recovered. |
| wolf / wulf | SieversBrunner1965 | This surviving SieversBrunner1965 citation still supports a combined scholarly claim rather than a single isolated fact: A high-vowel oblique input would behave differently. | yes | Split the sentence or isolate the exact rule/example before adding a page or section locator. |

## Upstream-only broad citations

Upstream-only broad occurrences rose from **201** to **213** because generated broad rows were reduced faster than upstream-only source prose was cleaned. The remaining upstream-only broad rows are now mostly model-entry-only or source-only analytical background that does not surface in the compact generated volume. They deserve a separate cleanup pass, but they are no longer the main blocker for trusting the generated citation state.

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF page indexes were used as locators.
- No invented page ranges were introduced.
- Every new locator added in this pass has a corresponding row in `citation_locator_primary_source_evidence.tsv`.
- Generated Markdown and `citation_locator_remaining_master.tsv` are synchronized to the final rebuilt state of this pass.

## Recommendation

**A. Continue generated broad-citation locator work.** Audit 02 materially reduced the live generated queue (64 -> 47), verified that the remaining Kluge rows are witness-limited rather than neglected, and kept the undercitation watchlist stable. The next efficient step is another generated-output pass focused on the remaining handbook rows and the unresolved Kroonen/Orel/Bosworth dictionary survivors, not an upstream-only cleanup yet.
