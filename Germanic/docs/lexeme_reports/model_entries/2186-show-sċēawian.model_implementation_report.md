# Model entry implementation report — 2186 show / sċēawian

## Files inspected

- `Germanic/docs/lexeme_reports/packets/2186-show-sċēawian.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2186-show-sċēawian.md`
- `Germanic/docs/lexeme_reports/research_memos/2186-show-sċēawian.md`
- `Germanic/data/germanic-aligned-final.tsv`
- local reference files for Orel, Kroonen, Bright, Brunner, Campbell, and Hogg
- `docs/refs.bib`

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2186-show-sċēawian.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2186-show-sċēawian.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2186-show-sċēawian.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2186-show-sċēawian.model_implementation_report.md`

## Notes on this pass

- Kept the entry on the infinitive lemma row and did not fold in the separate imperative and 3sg companion rows.
- Treated the current note as a normalization issue, not as a live phonological mismatch.
- Used Bright for the OE lemma and Campbell/Hogg for the `<sc>` versus normalized `sċ` distinction.

## Citation-key check

Checked against `docs/refs.bib`:

- `BrightCassidyRingler1971`
- `Campbell1959`
- `HoggPhonology1992`
- `Kroonen2013`
- `Orel2003`
- `SieversBrunner1965`

## Unresolved points

- Later review should preserve the distinction between source spelling `scēawian` and normalized target `sċēawian`.

## OCR and source-transcription checks

- Existing local reference files were sufficient; no extra Google Vision fallback beyond those files was needed.
- Campbell's palatal-`sc` discussion is OCR-noisy in places, so Bright and Hogg were used as control witnesses rather than reproducing the corrupted symbols.
- No unresolved OCR or encoding issue was reproduced in final prose.

## Scope confirmation

- No TSV, FST, manifest, packet, memo, bibliography file, derivation trace, writing-skill file, or existing model entry was changed.

## Citation-locator full-corpus high-confidence pass

- Added page-specific locators for `Kroonen2013, 482`.
- This pass was limited to high-confidence sources (`Kroonen2013`, `Orel2003`, `ClarkHall1960`, `RingeTaylor2014`, `Fulk2018`, `Seebold1970`, `BrightCassidyRingler1971`).
- Existing citations to conditional or unresolved locator sources were left unchanged.
