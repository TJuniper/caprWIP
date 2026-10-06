# Model entry implementation report — 2183 shoulder / sċuldrum

## Style-and-claims tightening pass

- This pass revised the model entry lightly rather than reopening the research.
- The `Conclusion` section was removed.
- Rhetorical negation was reduced, especially in the comparative and paradigm-comparison prose.
- Project-facing language was reduced outside the metadata section.
- Paradigm-comparison certainty was tightened so that probe outputs and trace outputs are labeled as such.
- Only the model entry and this implementation report were changed in this pass.

## Files inspected

- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- `Germanic/docs/lexeme_reports/packets/2183-shoulder-sċuldrum.md`
- `Germanic/docs/lexeme_reports/dev_notes_slices/2183-shoulder-sċuldrum.md`
- `Germanic/docs/lexeme_reports/research_memos/2183-shoulder-sċuldrum.md`
- `Germanic/docs/dossier-shoulder-2026.md`
- `Germanic/docs/dossier-shoulder-paradigm-survey-2026.md`
- `Germanic/docs/DEV_NOTES.md`
- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `docs/refs.bib`
- local reference files under `docs/references/` for Bosworth-Toller, Clark Hall, Brunner, Luick, Campbell, Hogg, Orel, Kroonen, and Ringe & Taylor

## Files created or updated

- created `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.source_ledger.md`
- replaced `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`
- updated `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model_implementation_report.md`

## What changed

- A **source extraction ledger** was created first, so the rewritten entry could be built from extracted forms and source claims rather than from repository-facing prose.
- The previous model entry was **discarded as a genre failure** and rewritten from scratch. It was not repaired paragraph by paragraph.
- The rewritten model entry now follows the requested **book-entry structure**:
  - `Transducer input and output`
  - `Reconstruction and comparative evidence`
  - `Old English evidence`
  - `Development to Old English`
  - `Paradigm comparison`

## Genre corrections applied

- Repository-facing language was removed from the model entry.
- Local project files are now used only as **finding aids** and are discussed in the ledger and this implementation report, not in the lexical-entry prose.
- The new entry is about the word, the reconstructed forms, the Old English evidence, and the linguistic development, not about packets, DEV_NOTES, implementation history, or backlog status.

## Citation-key check

Citation keys used in the rewritten model entry were checked against `docs/refs.bib`:

- `BosworthToller1898`
- `Campbell1959`
- `ClarkHall1960`
- `HoggPhonology1992`
- `Kroonen2013`
- `Luick1914`
- `Orel2003`
- `RingeTaylor2014`
- `SieversBrunner1965`

The source ledger also records `Fulk2018` as locally available for the `*-o-m(i)z > -um` morphological claim, even though that key is not used in the final model-entry prose.

## Paradigm comparison status

- No automatic paradigm-generation script was run in this pass.
- The `Paradigm comparison` section in the model entry is **manual**.
- The manual comparison is based on the existing attested Old English forms and the already documented candidate inputs, especially `*skúldrō`, `*skúldru`, `*skúldramiz`, and the secondary weak-feminine `sculdra`.

## Unresolved uncertainties

- The comparative handbooks still disagree on the lexeme-level reconstruction (`*skuldr(j)ō`, `*skuldra-`, `*skuldru`), and the rewritten entry preserves that disagreement rather than trying to suppress it.
- The weak-feminine `sculdra` is real and lexicographically supported, but its exact chronological status relative to the inherited strong masculine paradigm remains secondary and analogical.
- The paradigm comparison is deliberately manual; a reusable automatic shoulder probe has still not been added.

## Scope confirmation

- No TSV rows were changed.
- No FST files were changed.
- No manifest files were changed.
- No packet, dev-note slice, research memo, bibliography file, derivation trace, or existing pilot report was changed.
- The current style-and-claims pass changed only the model entry and this implementation report.

## Citation-locator master manifest 04

- Tightened `ClarkHall1960` from a broad citation to verified page locator `257` after direct inspection of the local Clark Hall text.

## Citation locator source-preparation triage 01

- Citation locator tightened or source status reclassified after source-preparation triage; verified against `BosworthToller1898, 85 and 699`.
