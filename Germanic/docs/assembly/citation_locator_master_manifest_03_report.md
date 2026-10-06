# Citation locator master manifest 03 report

## Summary

- broad citations before: **410**
- broad citations after: **397**
- rows inspected in this pass: **120**
- non-regular rows inspected in this pass: **68**
- locators added: **13**
- new evidence rows added: **13**
- rows newly classified this pass: **107**
- newly classified as `headword_not_found`: **44**
- newly classified as `page_markers_unreliable`: **29**
- newly classified as `claim_not_isolated`: **29**
- newly classified as `general_background`: **5**
- compact alpha regenerated: **yes**

This pass worked directly from `citation_locator_remaining_master.tsv`, starting
with the live `not_yet_inspected` P1/P2 tranche for `RingeTaylor2014`,
`Campbell1959`, `Kroonen2013`, `ClarkHall1960`, `Orel2003`, and
`BosworthToller1898`. The strongest gains came from page-marked dictionary
evidence in Orel and Kroonen, while a large non-regular tail was reclassified
more honestly as `claim_not_isolated`, `page_markers_unreliable`, or
`headword_not_found`.

## Manifest update

`citation_locator_remaining_master.tsv` was refreshed against the current live
source layer after the new regular and non-regular locator additions. Resolved
rows were removed, surviving rows were remapped to the current citation spans in
their live source files, and the selected 120-row pass tranche was reclassified
in place.

The refreshed manifest remains synchronized with the rebuilt compact Markdown:

- remaining manifest rows: **397**
- remaining broad source occurrences in regenerated
  `lexical_volume_regular_compact_alpha_01.md`: **397**

### Remaining queue by status

- `not_yet_inspected`: **132**
- `claim_not_isolated`: **105**
- `page_markers_unreliable`: **48**
- `headword_not_found`: **46**
- `general_background`: **44**
- `source_quarantined`: **14**
- `multi_page_discussion`: **6**
- `source_preparation_needed`: **2**

### Remaining queue by priority

- `P1`: **196**
- `P2`: **175**
- `P3`: **12**
- `Q`: **14**

## Primary-source verification

Every added locator in this pass was rechecked directly in the cited local
source file before being inserted into the prose. `citation_locator_primary_source_evidence.tsv`
now contains **13** new pass-03 rows, covering:

- regular prose additions for `bake`, `forlorn`, `lid`, `net`, `sheep`,
  `summer`, and `thorn`
- non-regular model-entry additions for `buck`, `heaven`, `live`, and `man`

Primary files checked in this pass included:

- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- `docs/references/orel_handbook_germanic_etymology.vision.txt`
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- `docs/references/campbell_old_english_grammar.txt`

Candidate locators were rejected after direct inspection when the exact headword
could not be recovered in the available local text, when the local witness did
not preserve a stable printed page anchor, or when the current sentence still
bundled several analytical claims into one broad citation.

## Source-by-source results

| Source | Remaining broad at start | Inspected this pass | Locators added | Left broad after | Reason for unresolved cases |
| :--- | ---: | ---: | ---: | ---: | :--- |
| `RingeTaylor2014` | 78 | 16 | 0 | 78 | The surviving Ringe-Taylor rows in this tranche are still mostly multi-step phonological or paradigm-commentary claims that need sentence splitting before a safe locator can be assigned. |
| `Campbell1959` | 56 | 14 | 0 | 56 | Campbell remains useful, but the pass-03 tranche mainly exposed clause-combination problems rather than single rule/example statements ready for localization. |
| `SieversBrunner1965` | 27 | 0 | 0 | 27 | Brunner was not a focus source in this tranche; remaining rows still stand where earlier passes left them. |
| `Fulk2018` | 8 | 0 | 0 | 8 | Fulk was not a focus source in this tranche; the remaining citations continue to function mainly as broader historical background. |
| `HoggPhonology1992` | 4 | 0 | 0 | 4 | Hogg was not a focus source in this tranche; the surviving rows remain broad background citations. |
| `Kroonen2013` | 65 | 30 | 5 | 60 | Kroonen localized cleanly where the local file preserved a page-marked headword (`summer`, `buck`, `heaven`, `live`, `man`), but many remaining rows are either broader comparative framing or exact-headword failures in the available text. |
| `Orel2003` | 44 | 20 | 7 | 37 | Orel remained the highest-yield source in the regular dictionary layer, but the unresolved tail is now mostly page-marker trouble or exact-headword failure rather than unworked backlog. |
| `ClarkHall1960` | 61 | 23 | 0 | 61 | Clark Hall frequently yielded the lexical item itself, but the available local witness still often failed to preserve a sufficiently reliable printed page anchor. |
| `BrightCassidyRingler1971` | 6 | 0 | 0 | 6 | Bright was not a focus source in this tranche; the remaining rows stay broad supportive glossary citations. |
| `BosworthToller1898` | 31 | 17 | 1 | 30 | Bosworth-Toller localized once more for `forlorn`, but the remaining inspected rows were mostly blocked by absent or unrecoverable exact headwords in the available local text. |
| `KlugeSeebold2011` | 14 | 0 | 0 | 14 | Kluge-Seebold remained quarantined throughout this pass. |

## Entry examples

### Successful locator additions

| Entry | Source | Source file checked | Locator added | Sentence splitting used |
| :--- | :--- | :--- | :--- | :--- |
| `bake / bacan` | `Orel2003` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | `33` | no |
| `forlorn / lēosan` | `BosworthToller1898` | `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` | `248` | no |
| `summer / sumer` | `Kroonen2013` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | `492` | no |
| `buck / bucc` | `Kroonen2013` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | `121` | no |
| `heaven / heofon` | `Kroonen2013` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | `220` | no |
| `live / lifeþ` | `Kroonen2013` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | `336` | no |

### Deliberately left broad after source inspection

| Entry | Source | Source file checked | Locator added or reason left broad | Sentence splitting used |
| :--- | :--- | :--- | :--- | :--- |
| `breeches / brēċ` | `Kroonen2013` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | left broad: `headword_not_found` | no |
| `hair / hǣr` | `Kroonen2013` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | left broad: `page_markers_unreliable` | no |
| `forlorn / lēosan` | `RingeTaylor2014` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | left broad: `claim_not_isolated` | no |
| `fright / fyrhte` | `Orel2003` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | left broad: `page_markers_unreliable` | no |
| `hammer / hameres` | `BosworthToller1898` | `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` | left broad: `headword_not_found` | no |
| `heaven / heofon` | `ClarkHall1960` | `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | left broad: `page_markers_unreliable` | no |

## Safety checks

- no OCR line numbers were used
- no file offsets were used
- no search-result positions were used
- no unverified PDF page indexes were used
- every added locator has a matching primary-source evidence row
- no invented page ranges were used
- no `KlugeSeebold2011` page locators were introduced
- no `p.` / `pp.` ordinary page syntax remains in the regenerated compact
  Markdown or the evidence log

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- citation links still work: **yes** (`967` PDF link annotations detected)
- bibliography still appears: **yes** (`CSLReferences` block present in the
  regenerated TeX)

## Recommendation

**A. Continue with another manifest-driven citation pass.**

The next pass should keep working from the refreshed `not_yet_inspected` tail.
The biggest remaining sources are still `RingeTaylor2014`, `ClarkHall1960`,
`Kroonen2013`, and `Campbell1959`, but pass 03 materially shrank the true
unknown backlog and made the dictionary tail more honest about where the block is
headword recovery versus page-anchor reliability.

## Scope confirmation

- no TSV source data were edited
- no FST files were edited
- no compact trace source was edited
- no bibliography files were edited
- no generated TeX/PDF were hand-edited
