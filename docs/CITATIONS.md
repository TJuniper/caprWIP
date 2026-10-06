# Citations and bibliography

The single source of truth for bibliographic data is **`docs/refs.bib`**
(top-level). All Markdown prose written from the presentation phase
forward should cite using **pandoc-style citation keys**, which convert
cleanly to LaTeX (`biblatex` with `\autocite`) when we compile the PDF.

## Citation syntax (Markdown that round-trips to LaTeX)

| Markdown                              | Renders as (typical author–year style)            | LaTeX (biblatex)                          |
|---------------------------------------|---------------------------------------------------|-------------------------------------------|
| `[@HoggGrammar1992]`                   | (Hogg 1992)                                       | `\autocite{HoggGrammar1992}`             |
| `[@HoggGrammar1992, §4.11]`                    | (Hogg 1992, §4.11)                                | `\autocite[\S\,4.11]{HoggGrammar1992}`           |
| `[@HoggPhonology1992, pp. 112--113]`           | (Hogg 1992, pp. 111–13)                           | `\autocite[pp.\,111--13]{HoggPhonology1992}`      |
| `[-@Ringe2006]`                       | (2006)  *(suppress author)*                       | `\autocite[][]{Ringe2006}` (year only)    |
| `@Campbell1959 [§740]`                | Campbell (1959, §740)                             | `\textcite[\S\,740]{Campbell1959}`        |
| `[@HoggGrammar1992; @RingeTaylor2014]`  | (Hogg 1992; Ringe & Taylor 2014)                 | `\autocites{HoggGrammar1992}{RingeTaylor2014}`  |
| `[see @Bammesberger1992, p. 39]`      | (see Bammesberger 1992, p. 39)                    | `\autocite[see][p.\,39]{Bammesberger1992}` |

Keep the citation **inside** the punctuation, e.g. `…lautgesetzlich
[@Campbell1959, §740].`

## Citekey scheme

`<FirstAuthorSurname><Year>[<disambig>]`

Examples already in `refs.bib`:

* `HoggPhonology1992`, `HoggGrammar1992`, `Campbell1959`, `Ringe2006`, `RingeTaylor2014`
* `KlugeSeebold2011`, `LloydSpringer1988` (joint authors → concatenate)
* `Stiles1986a`, `Stiles1986b` (multiple in same year → suffix)
* `SieversBrunner1965` (work originally by Sievers, ed. Brunner —
  cite by the edition we actually consult)

When introducing a new key, make sure it is unique and follow the
same shape.

## Adding new entries

1. Add the BibTeX entry to `docs/refs.bib` under the appropriate
   section heading.
2. If the source has a local PDF/text in `docs/references/`, include
   a `file = {docs/references/<stem>.<ext>}` field so editors can
   resolve it.
3. If you cannot verify a field (volume, pages, exact title) from a
   source you trust, set the value you have and add a `% TODO:`
   comment on the next line. The entry is still usable for drafting;
   we will sweep the TODOs before publication.
4. Update `Germanic/docs/REFERENCES.md` (the human-readable index) if
   the new source is project-relevant beyond a single dossier.

## Compiling Markdown to LaTeX/PDF (preview)

The intended pipeline is:

```bash
pandoc <input>.md \
  --from=markdown+citations \
  --citeproc \
  --bibliography=docs/refs.bib \
  --csl=<style>.csl \
  -o <output>.pdf
```

…or, for full LaTeX with `biblatex`:

```bash
pandoc <input>.md \
  --from=markdown+citations \
  --to=latex \
  --biblatex \
  --bibliography=docs/refs.bib \
  -o <output>.tex
```

We will pin a CSL style (e.g. *Unified style sheet for linguistics*)
when the presentation phase chooses one.

## Migration policy for existing prose

Existing dossiers and `DEV_NOTES.md` were written in the research
phase using informal citations such as "Campbell §740" or
"R&T vol. 2 p. 188". **Do not bulk-rewrite them.** They are a
research log; rewriting risks introducing errors and obscuring the
historical record.

Instead:

* **New prose** (presentation-phase write-ups, paper drafts, new
  sections) uses pandoc citation keys exclusively.
* **Existing prose** is converted opportunistically when it is being
  edited for substantive reasons. A drive-by citation conversion
  inside an unrelated edit is fine; a sweep purely to convert
  citations is not.
* Quotations of source text already embedded in dossiers stay as-is.

## Things that go in `refs.bib` vs things that don't

* **In `refs.bib`:** anything that might appear in a footnote or
  reference list of the eventual paper / monograph — handbooks,
  articles, dictionaries, dissertations, drafts, manuscripts cited
  by name, personal communications.
* **Not in `refs.bib`:** internal project artefacts (DEV_NOTES,
  dossiers, debug snapshots, the cogset TSV, FST source). Refer to
  these in prose by relative path or section number.
