# Germanic assembly pilot and lexical-volume design

This directory now contains three connected layers of work:

1. the validated **pilot assembly** used to settle entry layout, trace display,
   and citation behavior; and
2. the **book-architecture and class-manifest design** for a future full lexical
   derivation volume; and
3. the first **full lexical assembly alpha** built from the seven-class manifest.

The pilot remains deliberately small. The architecture layer defines the corpus
ordering, and the full alpha exercises that design across all 147 current model
entries.

## Pilot status

The pilot format is now stable enough to serve as the basis for a full lexical
assembly alpha:

- generated derivation summary under each headword
- boxed derivation trace
- model-entry prose below the trace
- live internal citation links in PDF output
- Unicode-safe Docker-backed PDF rendering

See `assembly_pilot_01_report.md` through `assembly_pilot_08_report.md` for the
incremental pilot passes.

## Pilot contents

The pilot includes these eight model entries, in the stable order recorded in `pilot_manifest.tsv`:

1. `1934-bake-bacan.model.md`
2. `1962-bow-bēag.model.md`
3. `1981-craft-cræft.model.md`
4. `2030-fowl-fugol.model.md`
5. `2250-thistle-þistles.model.md`
6. `2278-weapon-wǣpn.model.md`
7. `2293-will-willa.model.md`
8. `2308-youth-ġeoguþ.model.md`

## How to run the pilot

From the repository root:

```bash
bash Germanic/docs/assembly/build_pilot.sh
```

The script is path-stable and can also be run from other working directories.

If local `pandoc` / LaTeX tools are unavailable but Docker is available, use:

```bash
bash Germanic/docs/assembly/build_pilot_docker.sh
```

That wrapper regenerates `pilot_assembled.md` locally, then renders `.tex` and
`.pdf` inside a `pandoc/latex` container.

## Expected outputs

- `pilot_assembled.md` — assembled Markdown with normalized heading levels
- `pilot_assembled.tex` — LaTeX output, if `pandoc` is available
- `pilot_assembled.pdf` — PDF output, if `pandoc` and a Unicode-capable LaTeX engine (`xelatex` or `lualatex`) are available

## Current local result

In the current local host environment used for pilot 01:

- assembled Markdown generation was exercised successfully;
- `pandoc` was **not installed**, so `.tex` generation did not complete;
- no PDF engine stage was reached.

Pilot 02 adds and validates a Docker-backed render path because Docker is
available even where the host lacks local `pandoc`.

In the validated Docker-backed pilot-02 path:

- `pilot_assembled.md` regenerates on the host;
- `pilot_assembled.tex` renders successfully in `pandoc/latex`;
- `pilot_assembled.pdf` renders successfully with `xelatex`;
- `Noto Serif` / `Noto Sans Mono` are used in the container to preserve the Old
  English and reconstruction characters that the default Latin Modern fonts
  dropped.

See the pilot reports for the exact build results and the layout decisions that
landed during those passes.

## Book architecture and class manifests

The current design layer for full lexical assembly includes:

- `book_architecture.md` — proposed structure of the lexical derivation volume
- `book_architecture_01_report.md` — summary report for the architecture pass
- `full_assembly_design.md` — design note for a future full assembly script
- `section_introductions_draft.md` — placeholder section-opening prose
- `build_class_manifests.py` — helper that scans current `.model.md` entries and
  writes class-based manifests
- `manifest_regular.tsv`
- `manifest_attested_variant.tsv`
- `manifest_early_analogy.tsv`
- `manifest_late_analogy.tsv`
- `manifest_reconstructed_oe.tsv`
- `manifest_known_unmodelled.tsv`
- `manifest_unexplained.tsv`
- `manifest_all_by_class.tsv`
- `manifest_summary.md`
- `book_architecture_02_report.md`

These files define the ordering and section architecture used by the full alpha.

The standard full lexical-volume and combined-book shell wrappers first
run `python3 Germanic/tools/adjudicate.py --refresh`. This regenerates
stale canonical traces, compact lexical histories and manifests through
the shared artifact graph before rendering; failure stops the build.
Use these wrappers for publication rather than invoking individual
assembly builders against potentially stale inputs.

The class architecture now follows all **seven** current TSV
`DERIVATION_CLASS` values as first-class book sections:

1. `regular`
2. `attested_variant`
3. `early_analogy`
4. `late_analogy`
5. `reconstructed_oe`
6. `known_unmodelled`
7. `unexplained_unmodelled`

## Full lexical alpha 01

The current full-corpus alpha layer includes:

- `build_full_lexical_volume.py` — assembles the 147-entry lexical volume from
  `manifest_all_by_class.tsv`
- `build_full_lexical_volume.sh` — host wrapper for Markdown generation and
  local `pandoc` / PDF builds where available
- `build_full_lexical_volume_docker.sh` — Docker-backed render path for `.tex`
  and `.pdf`
- `full_volume_metadata.yaml` — Pandoc metadata for the full lexical volume
- `lexical_volume_alpha_01.md`
- `lexical_volume_alpha_01.tex`
- `lexical_volume_alpha_01.pdf`
- `full_lexical_assembly_alpha_01_report.md`

The full alpha uses all seven live TSV `DERIVATION_CLASS` values as first-class
sections and keeps the pilot layout: derivation summary, boxed trace, and model
prose.

## How to run the full alpha

From the repository root:

```bash
bash Germanic/docs/assembly/build_full_lexical_volume.sh
```

If local `pandoc` / LaTeX tools are unavailable but Docker is available, use:

```bash
bash Germanic/docs/assembly/build_full_lexical_volume_docker.sh
```

That wrapper regenerates `lexical_volume_alpha_01.md` locally, then renders
`.tex` and `.pdf` inside a `pandoc/latex` container with `xelatex` and Noto
fonts.

## Full-alpha outputs

- `lexical_volume_alpha_01.md` — full assembled Markdown in seven-part order
- `lexical_volume_alpha_01.tex` — Pandoc-generated LaTeX
- `lexical_volume_alpha_01.pdf` — Docker-rendered PDF with live citation links

See `full_lexical_assembly_alpha_01_report.md` for counts, output sizes, and
inspection notes.
