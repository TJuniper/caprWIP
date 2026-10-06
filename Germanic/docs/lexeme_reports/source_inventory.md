# Old English lexeme-report source inventory

## Scope

This inventory covers the sources needed for the next-generation Old English
derivation report infrastructure. It records which files are authoritative for
which kind of evidence, where bibliography keys live, and which source classes
need extra care when transformed into generated Markdown.

It also records the **selective-report policy**: not every Old English row
needs a generated `### Lexeme report`.

## Citation system

- **Bibliography database:** `docs/refs.bib`
- **Bibliography-key convention:** the header of `docs/refs.bib` is explicit
  that project Markdown should use **pandoc-style citations** such as
  `[@HoggGrammar1992]`, `[@Kroonen2013, p. 82]`, and `[-@Ringe2006]`.
- **Decision for lexeme reports:** use **pandoc-style `[@key]` citations** in
  Markdown. This is the only citation convention explicitly documented in the
  repository, and it is LaTeX-friendly via pandoc/biblatex conversion.
- **Reference index:** `Germanic/docs/REFERENCES.md` is the human-readable index
  of the local source library in `docs/references/`.

## Authoritative sources by evidence type

| Evidence type | Primary source(s) | Notes |
|:---|:---|:---|
| Per-row OE target, FST input, derivation class | `Germanic/data/germanic-aligned-final.tsv` | **Primary row authority.** `COUNTERPART`, `PROTOFORM`, `PROTO`, `DERIVATION_CLASS`, `NOTE`, and `HISTORY` all live here. `NOTE` and `HISTORY` are source material, not final prose. |
| Documented unresolved / intentionally unmodelled cases | `Germanic/data/oe_known_problems.tsv` | **Primary authority** for known exceptions and whether a mismatch is intentionally left unresolved. |
| Generated derivation traces | `Germanic/docs/debug_snapshots/oe_full_trace_report.txt`, `oe_derivation_class_trace_report.txt`, `oe_derivation_class_trace_report.compact.md` | Generated outputs; useful for checking stage behavior and current presentation, but not philological authority. |
| Current trace-generation logic | `Germanic/tools/oe_full_trace_report.py`, `oe_derivation_class_trace_report.py`, `compact_trace_report.py` | Authority for how reports are currently generated. |
| Current mismatch logic / known-problems integration | `Germanic/tools/oe_mismatch_report.py`, `oe_known_problems_report.py` | Authority for current bucketing, mismatch diagnostics, and ledger integration. |
| FST stage chronology and actual derivation rules | `Germanic/fsts/germanic.txt`, `Germanic/fsts/old_english_sandbox.txt` | **Primary authority** for what the deterministic pipeline actually does. |
| Internal project reasoning / prior decisions | `Germanic/docs/DEV_NOTES.md` | **Primary internal rationale source.** Section anchors in DEV_NOTES are often the best route into the repo’s reasoning history. |
| Focused lexical / phonological dossiers | `Germanic/docs/analysis/`, `Germanic/docs/dossiers/`, top-level `Germanic/docs/dossier-*.md` | Secondary internal authority for individual problems, source canvasses, and philological arguments. |
| OE lexical lookup and spelling snapshots | `Germanic/data/old_english_wiktionary.tsv` | Supplementary only. Useful as a local lookup table, but often reflects Wiktionary headword/template extraction and must not outrank better local sources. |
| OE Swadesh lookup | `Germanic/data/old_english_swadesh.tsv` | Low-authority lexical reference. Useful for normalized forms/IPA, not for full philological argument. |
| Local reference texts | `docs/references/` plus `Germanic/docs/REFERENCES.md` | **Primary external evidence base** for citations and source dossier extraction. |

## Data profile

For Old English rows with a real `COUNTERPART`:

- total OE rows: **380**
- non-empty `NOTE`: **137**
- non-empty `HISTORY`: **289**
- non-empty `DERIVATION_CLASS`: **380**

`DERIVATION_CLASS` distribution:

- `regular`: 303
- `early_analogy`: 35
- `late_analogy`: 28
- `unexplained_unmodelled`: 5
- `attested_variant`: 4
- `reconstructed_oe`: 3
- `known_unmodelled`: 2

Under the selective-report policy, a generated `### Lexeme report` is required
only when:

1. the row has a non-empty TSV `NOTE`;
2. `DERIVATION_CLASS` is not `regular`;
3. or a manual pilot/full report already exists for that row under
   `Germanic/docs/lexeme_reports/`.

Ordinary `regular` rows with an empty `NOTE` and no manual pilot/full report do
not need generated lexeme-report prose. Exact coverage counts should be taken
from `Germanic/tools/oe_lexeme_report_coverage.py`, which audits the live TSV
and report directory state.

## How to treat key source files

### `Germanic/data/germanic-aligned-final.tsv`

Use this as the row-level control table. The report generator should trust it
for:

- `CONCEPT`
- `COUNTERPART`
- `PROTOFORM`
- `PROTO`
- `DERIVATION_CLASS`

But it should **not** treat `NOTE` as publishable prose. `NOTE` mixes:

- quick philological summaries,
- implementation rationale,
- section references,
- source snippets,
- warnings about attestation status,
- and sometimes explicit project decisions.

`HISTORY` is even less presentation-ready. In many rows it is provenance log
material (often repeated Wiktionary-template notes), not report prose.

`NOTE` also serves as one of the triggers for the selective-report policy: a
non-empty OE `NOTE` means that a lexeme report or placeholder is required even
for a `regular` row.

### `Germanic/data/oe_known_problems.tsv`

Use this as the canonical ledger for unresolved or intentionally unmodelled OE
items. Lexeme reports for `known_unmodelled` and `unexplained_unmodelled`
entries should cross-reference this ledger explicitly.

### `Germanic/data/old_english_wiktionary.tsv`

This is useful as a **local lexical lookup table**, especially for quick checks
of headwords and normalized spellings, but it is not a sufficient authority for
attestation claims on its own. In pilot reports, prefer:

1. `oe_known_problems.tsv`
2. DEV_NOTES / dossiers / analysis
3. local reference texts in `docs/references/`
4. only then `old_english_wiktionary.tsv` as supporting evidence

### `Germanic/docs/DEV_NOTES.md`

This is the most important internal prose source. It contains:

- explicit problem/solution narratives,
- section-numbered decisions,
- source canvasses,
- philological corrections,
- and links to dossier files.

It should be treated as the main bridge between TSV source material and the
more polished lexeme-report prose.

### `Germanic/docs/lexeme_reports/`

This directory now has two distinct roles:

1. **policy/infrastructure documents** at top level (`report_schema.md`,
   `source_inventory.md`, `implementation_report.md`,
   `missing_bibliography_keys.md`);
2. **manual pilot/full report files** in report subdirectories such as
   `pilot/`.

Only the manual pilot/full report files count as row-level report coverage for
the selective-report policy.

### `docs/references/` and `docs/refs.bib`

These are the authoritative local bibliography store. The bibliography keys
live in `docs/refs.bib`; the readable file index lives in
`Germanic/docs/REFERENCES.md`.

## Inconsistencies and caution points

1. **Citation markup is not yet used consistently in Germanic docs.** The
   explicit citation convention exists in `docs/refs.bib`, but the Germanic
   Markdown corpus still mainly uses prose references and section/page mentions.
2. **`NOTE` and `HISTORY` are heterogeneous.** They cannot be copied directly
   into generated reports without restructuring and source checking.
3. **`HISTORY` is often provenance-heavy and Wiktionary-heavy.** It is useful as
   an audit trail, but not itself a publishable source dossier.
4. **Generated reports are not philological authority.** They are output
   snapshots of the present pipeline, and should be cited only as project
   artifacts, not as historical evidence.
5. **`old_english_wiktionary.tsv` is convenient but low-authority.** It can help
   find a spelling quickly, but must not override better local evidence.
6. **Current generated compact report omits `DERIVATION_CLASS` metadata.** The
   next-generation schema should restore it explicitly at the entry level.

## Missing or inaccessible source classes

- No separate Germanic-specific `.bib` file exists; `docs/refs.bib` is the
  master bibliography.
- No mass coverage store exists yet; current row-level coverage is limited to
  the pilot reports under `Germanic/docs/lexeme_reports/pilot/`.
- There is no ready-made morphology generator for Proto-Germanic paradigm-cell
  probes. That must be bootstrapped from minimal hand-specified templates.

## Practical priority order for pilot reports

When building pilot lexeme reports, use evidence in this order:

1. `germanic-aligned-final.tsv`
2. `oe_known_problems.tsv` (if relevant)
3. `DEV_NOTES.md`
4. specific analysis/dossier files
5. local handbooks/dictionaries in `docs/references/`
6. `old_english_wiktionary.tsv` / `old_english_swadesh.tsv` as supplementary
