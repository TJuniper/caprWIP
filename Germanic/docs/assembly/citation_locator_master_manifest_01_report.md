# Citation locator master manifest 01 report

## Summary

- total broad source occurrences inventoried from the pass-start compact Markdown: **455**
- remaining broad source occurrences after this pass and regeneration: **417**
- inspected or triaged this pass: **93**
- locators added: **38**
- left broad after this pass: **417**
- requiring source preparation or quarantine: **14**
- compact alpha regenerated: **yes**

Priority distribution in the master manifest:

- **P1**: 210
- **P2**: 219
- **P3**: 12
- **Q**: 14
- **G**: 0

A corrected parser was necessary here. Earlier ad hoc scans were dropping the first source in mixed citation spans, which is why they undercounted the broad queue badly. The master manifest generator used for this pass counts every broad source occurrence in each citation span, not just later semicolon-separated ones.

## Master manifest

`citation_locator_remaining_master.tsv` was created from the pass-start `Germanic/docs/assembly/lexical_volume_regular_compact_alpha_01.md` as the queue baseline for this pass. Each broad source occurrence received a stable `manifest_id`, source-layer routing, priority, and current status.

The manifest is now the source of truth for remaining citation work. Rows marked `inspected_locator_added` were successfully tightened in this pass; rows still broad remain queued with explicit reasons or next actions.

## Primary-source verification

`citation_locator_primary_source_evidence.tsv` was created only for locators that were actually added in this pass. Each evidence row points back to a manifest row and records the exact page or section seen in the local primary source file.

Primary-source evidence in this pass means a printed page marker or a stable section number visible in the local source text itself. Previous reports, source ledgers, and analogous citations were used only to suggest candidates; none were accepted as sole evidence, and several candidate handbook locators were rejected because the sentence-level claim was still broader than the safely isolatable passage.

## Source-by-source results

### RingeTaylor2014
- total broad occurrences in master manifest: **102**
- inspected or triaged this pass: **37**
- locators added: **24**
- left broad after this pass: **78**
- reason for unresolved cases: Ringe-Taylor supports the paradigm-cell distinction, but the exact finite-cell sentence remains too broad for a safe locator.
### Campbell1959
- total broad occurrences in master manifest: **73**
- inspected or triaged this pass: **16**
- locators added: **11**
- left broad after this pass: **62**
- reason for unresolved cases: Campbell supports the breaking environment in general, but the exact entry-level sentence is broader than a single safely isolatable rule citation.
### SieversBrunner1965
- total broad occurrences in master manifest: **27**
- inspected or triaged this pass: **8**
- locators added: **0**
- left broad after this pass: **27**
- reason for unresolved cases: Brunner contributes to the oblique-form background, but the exact sentence remains too broad for a safe locator.
### Fulk2018
- total broad occurrences in master manifest: **9**
- inspected or triaged this pass: **3**
- locators added: **1**
- left broad after this pass: **8**
- reason for unresolved cases: Fulk supports the etymological background, but not a locator-safe sentence for the exact OE-facing claim as currently written.
### HoggPhonology1992
- total broad occurrences in master manifest: **6**
- inspected or triaged this pass: **5**
- locators added: **2**
- left broad after this pass: **4**
- reason for unresolved cases: Hogg is cited here for wider derivational background rather than a locator-safe sentence about the selected OE form.
### Kroonen2013
- total broad occurrences in master manifest: **65**
- inspected or triaged this pass: **1**
- locators added: **0**
- left broad after this pass: **65**
- reason for unresolved cases: Kroonen identifies the weak noun family, but the full OE-specific argument is broader than a single headword locator.
### Orel2003
- total broad occurrences in master manifest: **45**
- inspected or triaged this pass: **2**
- locators added: **0**
- left broad after this pass: **45**
- reason for unresolved cases: Orel provides comparative headword background, but not a page-safe anchor for the full alternant argument.
### ClarkHall1960
- total broad occurrences in master manifest: **61**
- inspected or triaged this pass: **2**
- locators added: **0**
- left broad after this pass: **61**
- reason for unresolved cases: Clark Hall attests the neighboring cnopp/cnoppa branch, not the reconstructed cnobba claim itself.
### BrightCassidyRingler1971
- total broad occurrences in master manifest: **6**
- inspected or triaged this pass: **0**
- locators added: **0**
- left broad after this pass: **6**
- reason for unresolved cases: Mostly not yet inspected in this pass.
### BosworthToller1898
- total broad occurrences in master manifest: **31**
- inspected or triaged this pass: **0**
- locators added: **0**
- left broad after this pass: **31**
- reason for unresolved cases: Mostly not yet inspected in this pass.
### KlugeSeebold2011
- total broad occurrences in master manifest: **14**
- inspected or triaged this pass: **14**
- locators added: **0**
- left broad after this pass: **14**
- reason for unresolved cases: Kluge-Seebold remains page-quarantined in the available local text; no safe printed-page anchor was recovered in this pass.
## Entry examples

### Successful locator additions

- **begin / beġinnan** — **RingeTaylor2014**; reason: Palatalization rule and bi- > be- were both directly verified in the primary text.; source file checked: `docs/references/ringe_taylor_linguistic_history_vol2.txt`; locator added: **p. 218; p. 350**
- **fly / flēogan** — **RingeTaylor2014**; reason: The derivation and the WS/Anglian form contrast were both directly visible with printed page markers.; source file checked: `docs/references/ringe_taylor_linguistic_history_vol2.txt`; locator added: **pp. 189, 324**
- **give / ġiefan** — **Campbell1959**; reason: Campbell directly gives gefan (W-S giefan) and the palatal-diphthongization examples.; source file checked: `docs/references/campbell_old_english_grammar.txt`; locator added: **§428; §185**
- **hold / healdan** — **Campbell1959; RingeTaylor2014**; reason: Both handbooks directly contrast WS healdan with Anglian/Mercian haldan.; source file checked: `docs/references/campbell_old_english_grammar.txt; docs/references/ringe_taylor_linguistic_history_vol2.txt`; locator added: **§144; p. 199**
- **net / nett** — **Fulk2018; Campbell1959**; reason: Fulk gives the gemination section and Campbell gives the graphic simplification point.; source file checked: `docs/references/fulk_comparative_grammar_early_germanic.vision.txt; docs/references/campbell_old_english_grammar.txt`; locator added: **§6.15; §66**

### Deliberately left broad after review

- **birth / byrd** — **HoggPhonology1992**; reason: Kept broad as general derivational background rather than an entry-specific locator target.; source file checked: `Germanic/docs/assembly/book_prose/regular_all_01/1951-birth-byrd.book.md`; left broad: **general background**
- **knight / cniht** — **KlugeSeebold2011**; reason: Kept broad because Kluge-Seebold remains page-quarantined in the available local text.; source file checked: `Germanic/docs/lexeme_reports/model_entries/2086-knight-cniht.model.md`; left broad: **quarantined source**
- **lap / lappa** — **SieversBrunner1965**; reason: Kept broad because the attestation and A-restoration claims are broader than one safe handbook anchor.; source file checked: `Germanic/docs/lexeme_reports/model_entries/2090-lap-lappa.model.md`; left broad: **claim not isolated**
- **knob / cnobba** — **ClarkHall1960**; reason: Kept broad because Clark Hall attests cnopp/cnoppa, not the reconstructed-OE cnobba claim itself.; source file checked: `Germanic/docs/lexeme_reports/model_entries/2087-knob-cnobba.model.md`; left broad: **claim not isolated**
- **wolf / wulf** — **RingeTaylor2014**; reason: Kept broad because the exception analysis spans a broader discussion than one safe locator.; source file checked: `Germanic/docs/lexeme_reports/model_entries/2298-wolf-wulf.model.md`; left broad: **claim not isolated**

## Safety checks

- no OCR line numbers were used
- no file offsets were used
- no search-result positions were used
- no unverified PDF image-page numbers were used
- no locators were copied from previous reports without primary-source rechecking
- no invented page ranges were used

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- citation links still work: **yes**
- bibliography still appears: **yes**

## Recommendation

**A. Manifest and verification workflow are sound; continue with the next source-specific tranche.**

## Scope confirmation

- no TSV source data were edited
- no FST files were edited
- no compact trace source was edited
- no bibliography files were edited unless explicitly justified
- no generated TeX/PDF were hand-edited
