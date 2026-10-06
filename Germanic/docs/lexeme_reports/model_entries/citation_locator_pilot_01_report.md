# Citation-locator pilot 01 report

## Summary

- Pilot entries inspected: **10**
- Model entries changed: **10**
- Individual source-citation occurrences inspected: **53**
- Individual source-citation occurrences given page locators: **39**
- Left unchanged as general/background claims: **0**
- Left unchanged because page numbers could not be verified reliably: **14**

This pilot used only locally checkable source files. No page number was added
unless the local file preserved a reliable page marker, scan-page marker, or
recoverable printed page number near the cited passage. No locator was inferred
from OCR line numbers.

## Source locator inventory

| Citation key | Local file(s) checked | Source type | Reliable page markers? | Recommended locator policy | Confidence | OCR / source caution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Kroonen2013` | `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | dictionary-like | yes (`=== page N ===`) | page number available | high | Google-Vision-style text is good enough for headword-level page recovery. |
| `Orel2003` | `docs/references/orel_handbook_germanic_etymology.vision.txt` | dictionary-like | yes (`=== page N ===`) | page number available | high | OCR is noisy in places, but page markers and headword blocks are usable. |
| `Campbell1959` | `docs/references/campbell_old_english_grammar.txt` | grammar-like | conditional | page number available only after local verification | medium-high | No Vision-backed Campbell file is present locally; printed page numbers can still be recovered from the OCR text, but not mechanically for every claim. |
| `ClarkHall1960` | `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | dictionary-like | yes (`=== page N ===`) | page number available | high | Vision text is page-marked and generally easy to search for headwords. |
| `BosworthToller1898` | `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` | dictionary-like | yes (`=== page N ===`) | page number available when exact entry line is clear | medium | The file is large and noisier than Clark Hall; some headwords are easy to recover, others are not. |
| `RingeTaylor2014` | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | handbook-like | yes (`### PAGE N`) | page number available | high | Cleanest handbook source in the pilot set. |
| `Fulk2018` | `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` | handbook-like | yes (`=== page N ===`) | page number available | high | Vision text is page-marked and adequate for targeted lookup. |
| `Seebold1970` | `docs/references/seebold_vergleichendes_woerterbuch.vision.txt` | dictionary-like | yes (`=== page N ===`) | page number available | high | Vision text is page-marked and works well for verb/noun-family entries. |
| `KlugeSeebold2011` | `docs/references/kluge_seebold_etymologisches_woerterbuch.txt` | dictionary-like | no stable local page marker near the checked entry | entry/headword locator available but page number unavailable | medium | The `Distel` entry is present, but the local text file does not preserve a nearby page label that can be cited confidently. |
| `BrightCassidyRingler1971` | `docs/references/bright_anglo_saxon_reader.vision.txt` | grammar/reader-like | yes (`=== page N ===`) | page number available | high | Vision text is page-marked and the paradigm lines are easy to isolate. |
| `Luick1914` | `docs/references/luick_historische_grammatik.txt` | grammar-like | yes (`--- PAGE N ---`) | page number unavailable for now; use no locator until passage is isolated | medium | Page markers are present, but the pilot lookup did not isolate the `fugol` discussion securely enough to support a final locator. |

`HoggPhonology1992` did not occur in the 10 pilot entries, so it was not part of this
pass.

## Entry-by-entry results

### 1933 adder / nǣdre

- Citations inspected: `Kroonen2013`, `Orel2003`, `ClarkHall1960`, `Fulk2018`
- Citations updated: `Kroonen2013, 426`; `Orel2003, 325`; `ClarkHall1960, 225`; `Fulk2018, 149`
- Citations left unchanged: none
- Source files consulted: Kroonen Vision text, Orel Vision text, Clark Hall Vision text, Fulk Vision text
- OCR caution: none beyond ordinary OCR noise; page markers were explicit

### 1959 bottom / botm

- Citations inspected: `Kroonen2013`, `Orel2003`, `ClarkHall1960`, `BosworthToller1898`
- Citations updated: `Kroonen2013, 120`; `Orel2003, 100`; `ClarkHall1960, 63`; `BosworthToller1898, 112`
- Citations left unchanged: none
- Source files consulted: Kroonen Vision text, Orel Vision text, Clark Hall Vision text, Bosworth-Toller Vision text
- OCR caution: Bosworth-Toller is noisier than Clark Hall, but the `bodan -> botm` cross-reference was clear enough

### 1962 bow / bēag

- Citations inspected: `RingeTaylor2014` (2), `Campbell1959` (2), `BosworthToller1898`, `ClarkHall1960`
- Citations updated: `RingeTaylor2014, 55` (2), `ClarkHall1960, 45`
- Citations left unchanged: `Campbell1959` (2), `BosworthToller1898`
- Why unchanged: the exact page-to-claim support for the cited strong-verb and preterite statements was not confirmed with the same confidence from the available local files
- Source files consulted: Ringe-Taylor text, Campbell OCR text, Clark Hall Vision text, Bosworth-Toller Vision text
- OCR caution: Campbell is locally usable only after passage-level page recovery

### 1981 craft / cræft

- Citations inspected: `Kroonen2013`, `Orel2003`, `ClarkHall1960`, `BosworthToller1898`
- Citations updated: `Kroonen2013, 340`; `Orel2003, 259`; `ClarkHall1960, 19`
- Citations left unchanged: `BosworthToller1898`
- Why unchanged: the exact `cræft` headword page was not isolated confidently from the local Bosworth-Toller file in this pass
- Source files consulted: Kroonen Vision text, Orel Vision text, Clark Hall Vision text, Bosworth-Toller Vision text
- OCR caution: Bosworth-Toller headword recovery remains patchier than Clark Hall

### 1983 cud / cwedu

- Citations inspected: `Kroonen2013`, `Orel2003`, `RingeTaylor2014`, `ClarkHall1960`
- Citations updated: `Kroonen2013, 355`; `Orel2003, 266`; `RingeTaylor2014, 338`; `ClarkHall1960, 84`
- Citations left unchanged: none
- Source files consulted: Kroonen Vision text, Orel Vision text, Ringe-Taylor text, Clark Hall Vision text
- OCR caution: none beyond ordinary OCR noise

### 2009 field / feld

- Citations inspected: `RingeTaylor2014` (2), `ClarkHall1960`, `Campbell1959`
- Citations updated: `RingeTaylor2014, 170` (2); `ClarkHall1960, 114`; `Campbell1959, 169`
- Citations left unchanged: none
- Source files consulted: Ringe-Taylor text, Clark Hall Vision text, Campbell OCR text
- OCR caution: Campbell passage required local page recovery from the OCR text

### 2030 fowl / fugol

- Citations inspected: `Kroonen2013`, `Orel2003`, `RingeTaylor2014` (2), `Campbell1959` (3), `BosworthToller1898`, `ClarkHall1960`, `Luick1914`
- Citations updated: `Kroonen2013, 197`; `Orel2003, 155`; `ClarkHall1960, 138`
- Citations left unchanged: `RingeTaylor2014` (2), `Campbell1959` (3), `BosworthToller1898`, `Luick1914`
- Why unchanged: the exact page-to-claim mapping for the remaining handbook and dictionary claims was not recovered securely enough from the local files
- Source files consulted: Kroonen Vision text, Orel Vision text, Ringe-Taylor text, Campbell OCR text, Bosworth-Toller Vision text, Clark Hall Vision text, Luick OCR text
- OCR caution: this was the noisiest pilot case; Luick has page markers, but the needed `fugol` passage was not isolated

### 2151 reek / rēac

- Citations inspected: `Kroonen2013` (2), `Orel2003`, `ClarkHall1960` (2), `Seebold1970`
- Citations updated: `Kroonen2013, 446` (2); `Orel2003, 338`; `ClarkHall1960, 255`; `ClarkHall1960, 254`; `Seebold1970, 380`
- Citations left unchanged: none
- Source files consulted: Kroonen Vision text, Orel Vision text, Clark Hall Vision text, Seebold Vision text
- OCR caution: none beyond ordinary OCR noise

### 2250 thistle / þistles

- Citations inspected: `Orel2003`, `KlugeSeebold2011`, `ClarkHall1960`, `Campbell1959`
- Citations updated: `Orel2003, 458`; `ClarkHall1960, 326`; `Campbell1959, 151`
- Citations left unchanged: `KlugeSeebold2011`
- Why unchanged: the local Kluge-Seebold text preserves the `Distel` entry but not a reliable nearby page marker
- Source files consulted: Orel Vision text, Kluge-Seebold text, Clark Hall Vision text, Campbell OCR text
- OCR caution: Kluge entry recovery is good at the headword level, not at the page level

### 2278 weapon / wǣpn

- Citations inspected: `Kroonen2013`, `Campbell1959` (2), `BrightCassidyRingler1971` (2), `ClarkHall1960` (2)
- Citations updated: `Kroonen2013, 617`; `BrightCassidyRingler1971, 29` (2); `ClarkHall1960, 355` (2)
- Citations left unchanged: `Campbell1959` (2)
- Why unchanged: the local Campbell file supports the cluster-noun behavior more confidently than the exact nominative/oblique wording cited in the model entry
- Source files consulted: Kroonen Vision text, Campbell OCR text, Bright Vision text, Clark Hall Vision text
- OCR caution: Campbell remains usable only after passage-level checking

## Examples of successful locator updates

- `1933-adder-nǣdre.model.md`: `[@Kroonen2013]` -> `[@Kroonen2013, 426]`
- `1983-cud-cwedu.model.md`: `[@RingeTaylor2014; @ClarkHall1960]` -> `[@RingeTaylor2014, 338; @ClarkHall1960, 84]`
- `2250-thistle-þistles.model.md`: `[@Orel2003; @KlugeSeebold2011]` -> `[@Orel2003, 458; @KlugeSeebold2011]`

The last example is intentional: the Orel page was recoverable, but the local
Kluge-Seebold file did not support a page locator confidently, so the citation
was only partially localized.

## Cases not updated

- `1962-bow-bēag.model.md`: `Campbell1959` and `BosworthToller1898`
- `1981-craft-cræft.model.md`: `BosworthToller1898`
- `2030-fowl-fugol.model.md`: `RingeTaylor2014`, `Campbell1959`, `BosworthToller1898`, `Luick1914`
- `2250-thistle-þistles.model.md`: `KlugeSeebold2011`
- `2278-weapon-wǣpn.model.md`: `Campbell1959`

These are the cases where a page locator would be desirable, but the available
local files did not let the pilot recover one reliably.

## Recommendation for full-corpus pass

A full-corpus locator pass is **feasible only as a phased pass**, not as a
single bulk rewrite.

Recommended sequence:

1. **Pass A: high-confidence page-marked sources**
   - `Kroonen2013`
   - `Orel2003`
   - `ClarkHall1960`
   - `RingeTaylor2014`
   - `Fulk2018`
   - `Seebold1970`
   - `BrightCassidyRingler1971`

2. **Pass B: conditionally recoverable OCR sources**
   - `Campbell1959`
   - `Luick1914`
   - `BosworthToller1898`

   These should be handled only claim by claim, with page recovery demonstrated
   from the local file each time.

3. **Pass C: unresolved / source-preparation cases**
   - `KlugeSeebold2011`
   - any remaining Bosworth/Campbell/Luick cases where the passage can be found
     but the page cannot be cited confidently

   These need either better local source preparation or explicit human review.

The pilot shows that the high-confidence subset is worth doing, but it also
shows that broad OCR-driven replacement would introduce a real risk of guessed
or misassigned locators.

## Scope confirmation

- Changed files were limited to the 10 pilot `.model.md` files and their
  matching `.source_ledger.md`, `.reviewer_checklist.md`, and
  `.model_implementation_report.md` files, plus this report.
- `docs/refs.bib` was read but not edited.
- No TSV source data, FST files, `report_manifest.tsv`, pilot reports, packets,
  dev-note slices, research memos, bibliography data, derivation traces, or
  model entries outside the 10 pilot files were changed.
