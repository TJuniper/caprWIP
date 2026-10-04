# PGmc reconstruction survey

This is research evidence for all Old English data points, not a second
corpus, historical-stage registry or approved input migration. The survey
is in progress. A generated population ledger is not a completed survey.

## Ownership

- SOURCE: `sources.tsv` declares the reasonable held source universe,
  actual holdings, scope, edition/convention verification and exclusions.
- SOURCE: `forms.tsv` records diplomatic author forms or process evidence,
  exact printed pages, stages/cells, explained comparison notation, argument,
  verification and independent confidence.
- SOURCE: `coverage.tsv` records only actual row/source reviews and their
  evidence links, search basis and assessment. No row means unchecked.
- SOURCE: `commentary.md` owns the scientific synthesis and outstanding
  questions, not automatically approved corpus decisions.
- GENERATED: `corpus_inventory.tsv`, `source_coverage.tsv`,
  `reconstruction_ledger.md` and `survey_provenance.json` are projections
  through the canonical artifact graph.

All 393 OE row IDs remain in the population, including six research-only
rows. Current citation/input/stage/context/class fields are read from their
existing owners. Equality-stage resolution is an encoding convention,
not independent source agreement. Confidence does not assign a stage.
Shared evidence may link several rows, but each selected cell retains its
own review. Reconstructed stems, complete words and process statements
are not interchangeable evidence types.

Every source/row pair appears in the generated coverage grid. A negative
search needs an explicit search basis; a scoped exclusion needs a reason.
Never turn a failed string search into evidence of author silence.
Verification gaps must remain visible. An indirect quotation retains its
quoted-author attribution without claiming the original was checked.

Printed-page strings contain numerals/roman folios, comma-separated ranges
and ASCII hyphens. PDF-sheet markers belong in locator/basis notes, never
in the citation-page field. Diplomatic forms are preserved verbatim.
Comparison normalization must be explained; Foma's symbol restrictions
are not a reason to alter a printed source form.

The validator does not infer scientific agreement from normalized strings,
and does not edit corpus fields, stage metadata, FSTs or fingerprints:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-complete
python3 Germanic/tools/adjudicate.py --refresh
```

The first command reports validity and actual incompleteness. The second
fails while any row/source check or included source's edition/conventions
remain unreviewed. Declared local verification gaps are not silently erased;
a reviewed survey with such limits is not wholly image-verified evidence.
Only the last command regenerates projections. Do not run separate
generators or hand-edit outputs.

## Holding corrections and limitations

Kluge's held PDF is the 25th edition (2011), verified from its title
and edition-history pages. The older similarly named `.txt` identifies
the 24th edition, not the PDF. `kluge_seebold_2011_25th.txt` was extracted
from the held PDF using `pdftotext -layout`; it retains page breaks and
printed running heads. It requires ordinary glyph/page verification,
not an assertion that every extracted token is correct.

Hirt's held title is part I (1931), not evidence that the complete
three-part handbook is held. The Pokorny holding is a partial page
directory. Ringe-Taylor is held here as a text extract; missing local
images are explicitly distinguished from earlier dossier verification.
Generic Kylstra/Oxford filenames are aliases of identified sources.
The separately held Luehr thousand article still needs bibliography and
holding-identity resolution; it must not disappear from the eventual
source-universe review simply because its filename lacks a citation key.

No acquisition or whole-library OCR is authorized. Do not include private
correspondence as a published independent reconstruction source.
