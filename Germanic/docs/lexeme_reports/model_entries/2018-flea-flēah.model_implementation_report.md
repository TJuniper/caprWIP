# Model entry implementation report — 2018 flea / flēah

## Files inspected

- `Germanic/data/germanic-aligned-final.tsv` (row 2018)
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
- local reference files for Orel, Kroonen, and Ringe & Taylor

## Files created

- `Germanic/docs/lexeme_reports/model_entries/2018-flea-flēah.source_ledger.md`
- `Germanic/docs/lexeme_reports/model_entries/2018-flea-flēah.model.md`
- `Germanic/docs/lexeme_reports/model_entries/2018-flea-flēah.reviewer_checklist.md`
- `Germanic/docs/lexeme_reports/model_entries/2018-flea-flēah.model_implementation_report.md`
- `Germanic/docs/assembly/book_prose/regular_all_01/2018-flea-flēah.book.md`

## Notes on this pass

- Drafted the entry around the genuine stem-class dispute: Orel's root noun
  `*flauxz` versus Kroonen's ō-stem `*flauhō-`. Unlike 'book' and 'goose',
  this is not a notation difference but a disagreement about inflectional
  class, and the entry presents it as such without adjudicating it.
- The entry explains that the selected input follows Orel's analysis alongside
  the other root nouns, and that on that analysis the nominative marker was
  lost early, before the diphthong developments that yield `flēah`.
- Page citations were verified directly against the local reference texts; the
  ledger records line-level locators.

## Citation-key check

Checked against `docs/refs.bib`:

- `Orel2003`
- `Kroonen2013`
- `RingeTaylor2014`

## Unresolved points

- The root-noun versus ō-stem class question is genuinely open in the sources.
  If a later pass adopts Kroonen's analysis, the selected input would need
  author-level reconsideration; this is recorded in the reviewer checklist.

## Scope confirmation

- No TSV, FST, manifest, packet, dev-note slice, research memo, bibliography
  file, derivation trace, existing model entry, writing-skill file, or existing
  batch report was changed.
