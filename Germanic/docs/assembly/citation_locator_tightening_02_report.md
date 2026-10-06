# Citation locator tightening 02 report

## Summary

- broad citations before: **475**
- broad citations after: **422**
- broad citations inspected: **153**
- locators added: **53**
- locators added by source: `ClarkHall1960` 26, `Kroonen2013` 15, `BrightCassidyRingler1971` 10, `Orel2003` 2
- files changed: **40**
- model entries were edited: **yes**
- compact alpha was regenerated: **yes**

## Method

This pass went beyond tightening 01 by sweeping all current broad Clark Hall and Bright occurrences, plus the regular-overlay Kroonen and Orel occurrences, against the rebuilt compact-alpha baseline. Regular prose was tightened upstream in `book_prose/regular_all_01/`; non-regular fixes were made in the relevant `.model.md` files and paired support files.

Page locators were added only where the local page-marked OCR showed the exact headword, paradigm form, or comparative headword cleanly enough to support the reader-facing sentence. No OCR line numbers, file offsets, search-result positions, image-page guesses, or inferred page ranges were used.

## Source-by-source results

### Kroonen2013
- broad occurrences before: **76**
- inspected: **36**
- locators added: **15**
- left broad: **61**
- reason for remaining broad cases: Regular-overlay dictionary cases were inspected source-by-source. Remaining broad cases are mostly non-regular occurrences not inspected here, plus regular claims where the headword page did not isolate the exact sentence cleanly.

### Orel2003
- broad occurrences before: **47**
- inspected: **18**
- locators added: **2**
- left broad: **45**
- reason for remaining broad cases: This pass inspected the regular-overlay Orel cases only. Remaining broad Orel occurrences are mostly outside the regular overlay, with a smaller regular remainder where the headword page did not isolate the exact claim cleanly.

### ClarkHall1960
- broad occurrences before: **83**
- inspected: **83**
- locators added: **26**
- left broad: **57**
- reason for remaining broad cases: Clark Hall was swept across all current broad occurrences; most survivors are exact-headword misses or cases where the page was found but the sentence-level claim remained too loose to tighten safely.

### BrightCassidyRingler1971
- broad occurrences before: **16**
- inspected: **16**
- locators added: **10**
- left broad: **6**
- reason for remaining broad cases: Bright was swept across all current broad occurrences; the remaining broad cases are the few entries where a safe page anchor was not isolated tightly enough for the exact reader-facing claim.

### RingeTaylor2014
- broad occurrences before: **93**
- inspected: **0**
- locators added: **0**
- left broad: **93**
- reason for remaining broad cases: Broad Ringe & Taylor citations remain largely handbook-style rule or discussion citations and were not the bulk-localization target of this pass.

### Campbell1959
- broad occurrences before: **66**
- inspected: **0**
- locators added: **0**
- left broad: **66**
- reason for remaining broad cases: Broad Campbell citations remain largely grammar-rule or discussion citations and were not the bulk-localization target of this pass.

### Fulk2018
- broad occurrences before: **9**
- inspected: **0**
- locators added: **0**
- left broad: **9**
- reason for remaining broad cases: Only a few Fulk claims are tightly anchorable; the remaining broad cases stay discussion-level.

### SieversBrunner1965
- broad occurrences before: **24**
- inspected: **0**
- locators added: **0**
- left broad: **24**
- reason for remaining broad cases: Remaining Brunner cases are mostly grammar-level references rather than single-page headword citations.

### BosworthToller1898
- broad occurrences before: **31**
- inspected: **0**
- locators added: **0**
- left broad: **31**
- reason for remaining broad cases: Bosworth-Toller remains mixed because of base/supplement complications; untouched cases remain broad unless a page-safe local witness is explicit.

### HoggPhonology1992
- broad occurrences before: **5**
- inspected: **0**
- locators added: **0**
- left broad: **5**
- reason for remaining broad cases: The surviving Hogg citations are discussion-level and were not retightened in this pass.

### Luick1914
- broad occurrences before: **1**
- inspected: **0**
- locators added: **0**
- left broad: **1**
- reason for remaining broad cases: The Luick tail was not revisited in this pass.

### KlugeSeebold2011
- broad occurrences before: **12**
- inspected: **0**
- locators added: **0**
- left broad: **12**
- reason for remaining broad cases: Kluge-Seebold remains page-quarantined in this pass.

## Entry examples

- **calf — OE ċealf**: `[@Kroonen2013]` -> `[@Kroonen2013, 318]`
- **calf — OE ċealf**: `[@ClarkHall1960]` -> `[@ClarkHall1960, 73]`
- **corn — OE corn**: `[@Kroonen2013]` -> `[@Kroonen2013, 352]`
- **door — OE dor**: `[@ClarkHall1960]` -> `[@ClarkHall1960, 92]`
- **fern — OE fearn**: `[@ClarkHall1960]` -> `[@ClarkHall1960, 114]`
- **fly — OE flēogan**: `[@BrightCassidyRingler1971]` -> `[@BrightCassidyRingler1971, 363]`
- **horn — OE horn**: `[@ClarkHall1960]` -> `[@ClarkHall1960, 179]`
- **span — OE spannan**: `[@Kroonen2013]` -> `[@Kroonen2013, 505]`
- **water — OE wæter**: `[@BrightCassidyRingler1971]` -> `[@BrightCassidyRingler1971, 29]`
- **swan — OE swanes**: `[@BrightCassidyRingler1971]` -> `[@BrightCassidyRingler1971, 441]`

## Left broad inventory

- whole-book/general background: **0**
- multi-page discussion: **0**
- page markers unavailable: **0**
- source OCR unreliable: **0**
- headword not found: **53**
- page found but claim not isolated: **47**
- source quarantined: **12**
- not inspected: **310**

## Safety checks

- no OCR line numbers were used as locators
- no file offsets were used
- no search-result positions were used
- no unverified PDF image-page numbers were used
- no invented page ranges were used
- no forbidden `KlugeSeebold2011` locators were introduced

## Output inspection

- Markdown regenerated: **yes**
- TeX regenerated: **yes**
- PDF regenerated: **yes**
- citation links still work: **yes** (`963` PDF link annotations found)
- bibliography still appears: **yes** (`CSLReferences` block in TeX; bibliography text visible on PDF p. 110)

## Recommendation

**A. Locator tightening 02 was successful; continue with another source-specific pass.**

## Scope confirmation

- no TSV source data were edited
- no FST files were edited
- no compact trace source was edited
- no generated TeX/PDF was hand-edited
- bibliography files were not edited
