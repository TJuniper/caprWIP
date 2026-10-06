# Model entry implementation report — 2044 goose / gōs

## Files inspected

- `Germanic/data/germanic-aligned-final.tsv` (row 2044)
- `Germanic/docs/sound_changes/audits/sc020-dossier-a-root-noun-nominative-z.md`
- `Germanic/docs/sound_changes/audits/sc020-three-rule-adjudication.md`
- `Germanic/docs/sound_changes/audits/sc020-split-before-after-firing-table.tsv`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/docs/lexeme_reports/model_entries/2152-rest-ræste.*` (genre models)
- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/source_ledger_template.md`
- `Germanic/docs/lexeme_reports/writing_skill/reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/writing_skill/anti_patterns.md`
- `docs/refs.bib`
- local reference files for Orel, Kroonen, Kluge/Seebold, Bammesberger, Ringe & Taylor, and Fulk

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2044-goose-gōs.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2044-goose-gōs.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2044-goose-gōs.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2044-goose-gōs.model_implementation_report.md`
- `Germanic/docs/assembly/book_prose/regular_all_01/2044-goose-gōs.book.md`

## Notes on this pass

- Drafted the entry as a layered nominative history: Szemerényi's law in the
  PIE nominative (Bammesberger), the analogically rebuilt Germanic nominative,
  Orel's explicit `*ǥansz`, and Kroonen's endingless `*gans-` with oblique
  `*gunzaz` are presented as analytical layers of one paradigm.
- The entry explains the selected input's explicit `-z`, the early root-noun
  nominative loss, and the subsequent Ingvaeonic nasal-spirant development
  that yields `gōs`.
- Page citations were verified directly against the local reference texts; the
  ledger records line-level locators, including the OCR discrepancy
  (`*zansz` for `*ǥansz`).

## Citation-key check

Checked against `docs/refs.bib`:

- `Orel2003`
- `Kroonen2013`
- `KlugeSeebold2011`
- `Bammesberger1990`
- `RingeTaylor2014`
- `Fulk2018`

## Unresolved points

- Bammesberger's account of the rebuilt nominative is one analysis among
  several possible; the entry reports it as his, with its hedging preserved.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
