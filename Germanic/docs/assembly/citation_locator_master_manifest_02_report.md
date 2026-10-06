# Citation locator master manifest 02 report

## Summary

- broad citations before: **417**
- broad citations after: **410**
- number inspected in this pass: **135**
- locators added: **7**
- locators standardized from `p.` / `pp.` syntax: **44** in live source citations; **24** matching `locator_added` values in the evidence log
- rows left broad: **410**
- rows requiring source preparation or quarantine: **35**
- compact alpha regenerated: **yes**

This pass kept the master-manifest workflow from pass 01, but refreshed the
queue as a true remaining-broad manifest rather than leaving it mixed with
already-resolved rows. The result is a current 410-row queue whose status field
now distinguishes `general_background`, `claim_not_isolated`,
`multi_page_discussion`, `page_markers_unreliable`, `headword_not_found`,
`source_quarantined`, `source_preparation_needed`, and `not_yet_inspected`.

Non-regular material was materially included in this pass: **95** of the
inspected or re-triaged remaining rows came from non-regular classes.

## Locator syntax cleanup

Ordinary page locators were standardized from Pandoc forms such as
`[@RingeTaylor2014, p. 218]` and `[@RingeTaylor2014, pp. 189, 324]` to bare-page
forms such as `[@RingeTaylor2014, 218]` and `[@RingeTaylor2014, 189, 324]`.
Section locators such as `[@Campbell1959, §428]`, `[@HoggPhonology1992, §3.4.2.4]`, and
`[@Fulk2018, §6.15]` were preserved as section locators.

Counts for this cleanup:

- live source citations standardized: **44**
- evidence-log `locator_added` values standardized: **24**
- remaining live `p.` / `pp.` ordinary page locators in the checked source
  layers and regenerated compact Markdown: **0**

## Manifest update

`citation_locator_remaining_master.tsv` was regenerated from the current live
citation layer after the syntax cleanup, the new verified locator additions, and
compact-alpha regeneration. It now contains only the **remaining** broad source
occurrences, each with current citation span text, the surrounding paragraph,
source-layer routing, and the refreshed status vocabulary.

Updated remaining-queue counts:

### By status

- `not_yet_inspected`: **252**
- `claim_not_isolated`: **76**
- `general_background`: **39**
- `page_markers_unreliable`: **19**
- `source_quarantined`: **14**
- `multi_page_discussion`: **6**
- `source_preparation_needed`: **2**
- `headword_not_found`: **2**

### By priority

- `P1`: **209**
- `P2`: **175**
- `P3`: **12**
- `Q`: **14**

The regenerated manifest matches the rebuilt compact Markdown exactly: the
assembled file still contains **410** broad source occurrences, and the
refreshed manifest has **410** rows.

## Primary-source verification

`citation_locator_primary_source_evidence.tsv` was updated in two ways:

1. existing `locator_added` values from pass 01 were normalized to bare-page
   syntax where appropriate; and
2. **7** new evidence rows were added for the newly verified locators in this
   pass.

Primary-source files checked in this pass included:

- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- `docs/references/orel_handbook_germanic_etymology.vision.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`

Candidate locators were rejected after direct inspection when the source support
remained broader than a single sentence-safe claim, when the exact paradigm-cell
form was not directly found, or when local page markers remained unreliable.
The clearest rejected patterns were:

- non-contiguous handbook discussions better left broad than forced into a
  composite locator;
- dictionary support that attested the lexeme but not the exact finite or
  oblique comparison form; and
- quarantined Kluge-Seebold rows where a reliable printed page anchor was still
  not recoverable.

## Source-by-source results

| Source | Remaining broad at start | Inspected this pass | Locators added | Left broad after | Reason for unresolved cases |
| :--- | ---: | ---: | ---: | ---: | :--- |
| `RingeTaylor2014` | 78 | 25 | 0 | 78 | Remaining Ringe-Taylor rows are mostly discussion-level phonology or paradigm commentary that still needs sentence splitting before a safe locator can be assigned. |
| `Campbell1959` | 62 | 30 | 6 | 56 | Campbell localized well where the prose named a compact rule/example pairing, but many remaining rows still combine several steps or contrastive claims in one sentence. |
| `SieversBrunner1965` | 27 | 10 | 0 | 27 | Brunner remains useful as support, but the surviving citations are still broader than a single safely isolatable rule or form note. |
| `Fulk2018` | 8 | 4 | 0 | 8 | The remaining Fulk citations mostly serve broader historical or analogical framing rather than a single locator-safe clause. |
| `HoggPhonology1992` | 4 | 2 | 0 | 4 | The surviving Hogg citations function mainly as broader background rather than sentence-level anchors. |
| `Kroonen2013` | 65 | 19 | 0 | 65 | Kroonen often supplies the comparative headword or family background, but the current prose usually makes a broader OE-facing claim than one headword locator would honestly support. |
| `Orel2003` | 45 | 8 | 1 | 44 | Orel localized cleanly for `mare`, but most other Orel rows remain comparative-background citations rather than single-claim anchors. |
| `ClarkHall1960` | 61 | 18 | 0 | 61 | Clark Hall still has a large tail where the needed lexical material is present but the available local text did not yield a safe printed page anchor in this pass. |
| `BrightCassidyRingler1971` | 6 | 2 | 0 | 6 | The remaining Bright citations are supportive glossary material rather than the sole basis for the full entry claim. |
| `BosworthToller1898` | 31 | 9 | 0 | 31 | The remaining Bosworth-Toller rows mostly need either a more reliable page-labeled witness or a narrower claim than the current sentence. |
| `KlugeSeebold2011` | 14 | 2 | 0 | 14 | Kluge-Seebold remains quarantined; no forbidden page locators were introduced. |

## Entry examples

### Successful locator additions

| Entry | Source | Source file checked | Locator added | Sentence splitting used |
| :--- | :--- | :--- | :--- | :--- |
| `gold / gold` | `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | `§414` | no |
| `milk / meoloc` | `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | `§574.5` | no |
| `nightmare / mare` | `Orel2003` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | `262` | no |
| `swallow / swealwe` | `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | `§365` | no |
| `token / tācn` | `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | `§574` | yes |
| `wade / wadan` | `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | `§744` | no |

### Deliberately left broad after source inspection

| Entry | Source | Source file checked | Locator added or reason left broad | Sentence splitting used |
| :--- | :--- | :--- | :--- | :--- |
| `deed / dǣd` | `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | left broad: `claim_not_isolated` | no |
| `begin / beġinnan` | `ClarkHall1960` | `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | left broad: `page_markers_unreliable` | no |
| `brand / brandes` | `ClarkHall1960` | `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | left broad: `headword_not_found` | no |
| `smear / smierwan` | `RingeTaylor2014` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | left broad: `multi_page_discussion` | no |
| `knight / cniht` | `KlugeSeebold2011` | `docs/references/kluge_seebold_etymologisches_woerterbuch.txt` | left broad: `source_quarantined` | no |
| `have / hæfeþ` | `RingeTaylor2014` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | left broad: `claim_not_isolated` | no |

## Safety checks

- no OCR line numbers were used
- no file offsets were used
- no search-result positions were used
- no unverified PDF page indexes were used
- no locators were copied from previous reports without direct primary-source
  rechecking
- no invented page ranges were used
- no forbidden Kluge-Seebold locators were introduced

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- citation links still work: **yes** (`966` link annotations detected in the
  regenerated PDF)
- bibliography still appears: **yes** (`CSLReferences` block present in the
  regenerated TeX)

## Recommendation

**A. Continue with another manifest-driven citation pass.**

The next pass should stay source-led rather than entry-random: the biggest
remaining handbook targets are still `RingeTaylor2014` and `Campbell1959`, but
the queue is now honest about which rows are genuine sentence-splitting problems
and which rows are blocked by source preparation or quarantined material.

## Scope confirmation

- no TSV source data were edited
- no FST files were edited
- no compact trace source was edited
- no bibliography files were edited unless explicitly justified
- no generated TeX/PDF were hand-edited
