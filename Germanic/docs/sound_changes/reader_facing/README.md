# Reader-facing sound-change pilot

This directory is a **new book-facing layer** for the sound-change half. The
existing reports, dossiers, chronology cards, and FOMA definitions remain the
source material; the files here test how that material can be rewritten for a
historical-linguistic reader who does not need the internal workflow.

The present pilot contains three deliberately different cases:

1. `052-velar-palatalization.md` — a major consonantal change with rich
   scholarship and clear local chronology.
2. `055-056-i-umlaut-core.md` — a grouped chapter with one major central change
   and one narrower right-edge follower.
3. `058-nasal-dissimilation.md` — a residual change with thin source support and
   boundary-limited chronology.

An expanded local batch now also exists for a separate pilot-02 build:

1. `049-050-b-allophony-and-sievers-law-syncope.md`
2. `051-sk-palatalization.md`
3. `053-054-pre-umlaut-bridge-and-w-loss.md`
4. `057-j-cluster-coalescence.md`

## Current scope

These files do **not** replace the existing sound-change reports. They are a
controlled pilot for tone, structure, quotation practice, code presentation,
and chronology explanation.

## Pilot PDF build

To assemble the three pilot chapters into one reviewable PDF, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_docker.sh
```

This writes:

- `reader_facing_pilot_01.md`
- `reader_facing_pilot_01.pdf`

To build the expanded batch without altering the original pilot target, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_02_docker.sh
```

This writes:

- `reader_facing_pilot_02.md`
- `reader_facing_pilot_02.pdf`

To build the ordered seven-chapter local section without altering the preserved
pilot outputs, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_01_docker.sh
```

This writes:

- `reader_facing_local_section_01.md`
- `reader_facing_local_section_01.pdf`

To extend that ordered section rightward through back mutation and the two short
weak-tail notes, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_02_docker.sh
```

This writes:

- `reader_facing_local_section_02.md`
- `reader_facing_local_section_02.pdf`

To extend the same ordered section through high-vowel apocope and the next late
weak-tail batch, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_03_docker.sh
```

This writes:

- `reader_facing_local_section_03.md`
- `reader_facing_local_section_03.pdf`

To extend that ordered section through unstressed long-vowel shortening and the
unstressed ae-merger core, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_04_docker.sh
```

This writes:

- `reader_facing_local_section_04.md`
- `reader_facing_local_section_04.pdf`

To extend the same ordered section through medial unstressed-i lowering,
prefix-vowel reduction, and weak-tail reduction, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_05_docker.sh
```

This writes:

- `reader_facing_local_section_05.md`
- `reader_facing_local_section_05.pdf`

To extend the same ordered section through final-j loss, contraction, and
r-metathesis, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_06_docker.sh
```

This writes:

- `reader_facing_local_section_06.md`
- `reader_facing_local_section_06.pdf`

To extend the same ordered section leftward through surviving bimoric
o-unrounding, Anglo-Frisian brightening, breaking, and restoration, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_07_docker.sh
```

This writes:

- `reader_facing_local_section_07.md`
- `reader_facing_local_section_07.pdf`

To extend the same ordered section further leftward through prefix and
compound adjustments, medial unstressed vowel changes, and final bare-a
loss, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_08_docker.sh
```

This writes:

- `reader_facing_local_section_08.md`
- `reader_facing_local_section_08.pdf`

To extend the same ordered section further leftward through the West Saxon
diphthong sequence, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_09_docker.sh
```

This writes:

- `reader_facing_local_section_09.md`
- `reader_facing_local_section_09.pdf`

To extend the same ordered section further leftward through preconsonantal
x-loss, awj glide formation, and au-fronting, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_10_docker.sh
```

This writes:

- `reader_facing_local_section_10.md`
- `reader_facing_local_section_10.pdf`

To extend the same ordered section further leftward through nasal spirant
changes, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_11_docker.sh
```

This writes:

- `reader_facing_local_section_11.md`
- `reader_facing_local_section_11.pdf`

To extend the same ordered section further leftward through the early
unstressed-vowel and boundary notes from SC021 to SC025, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_12_docker.sh
```

This writes:

- `reader_facing_local_section_12.md`
- `reader_facing_local_section_12.pdf`

To extend the same ordered section further leftward through the early vocalic
and final changes from SC016 to SC020, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_13_docker.sh
```

This writes:

- `reader_facing_local_section_13.md`
- `reader_facing_local_section_13.pdf`

To extend the same ordered section further leftward through the earliest
unstressed vowel changes, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_14_docker.sh
```

This writes:

- `reader_facing_local_section_14.md`
- `reader_facing_local_section_14.pdf`

To extend the same ordered section farther leftward by adding West Germanic
rhotacism ahead of the existing opening pair, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_15_docker.sh
```

This writes:

- `reader_facing_local_section_15.md`
- `reader_facing_local_section_15.pdf`

To extend the same ordered section farther leftward by adding Proto-West-Germanic
ai-monophthongization and early i-apocope while leaving SC005 outside the
reader-facing span, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_16_docker.sh
```

This writes:

- `reader_facing_local_section_16.md`
- `reader_facing_local_section_16.pdf`

To extend the same ordered section farther leftward by adding final *ō-lowering
before *r and coronal-w assimilation while still leaving SC005 and SC009 outside
the reader-facing span, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_17_docker.sh
```

This writes:

- `reader_facing_local_section_17.md`
- `reader_facing_local_section_17.pdf`

To extend the same ordered section farther leftward by adding West Germanic
j-gemination, syllabic j after final-vowel loss, and dental hardening while
still leaving SC005, SC009, and SC012 outside the reader-facing span, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_18_docker.sh
```

This writes:

- `reader_facing_local_section_18.md`
- `reader_facing_local_section_18.pdf`

To extend the same ordered section farther leftward by adding unstressed
\emph{*a}-raising before final \emph{*m}, \emph{ij}-contraction in the `friend`
family, and \emph{lþ}-voicing, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_19_docker.sh
```

This writes:

- `reader_facing_local_section_19.md`
- `reader_facing_local_section_19.pdf`

The current book section is assembled from the generated
`registry/reader_manifest.tsv` (chapters and file order derived from
`registry/reader_chapters.tsv`, `registry/reader_files.tsv`, the SC registry,
and the executable cascade — no hand-typed file list). To run the checkers,
rebuild the assembled Markdown with `Germanic/tools/build_reader_book.py`,
and render the PDF, use:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_20_docker.sh
```

This writes:

- `reader_facing_local_section_20.md`
- `reader_facing_local_section_20.pdf`

## Style audit workflow

After drafting or revising any reader-facing chapter, run:

```bash
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
```

Inspect the warnings manually. If the pilot PDF is being rebuilt, run the
checker before:

```bash
bash Germanic/docs/sound_changes/reader_facing/build_reader_facing_pilot_docker.sh
```

## Numbering note

The current sound-change assembly wrappers do **not** request numbered section
headings. `Germanic/docs/assembly/build_sound_change_volume.sh` passes Markdown
through Pandoc, but it does not add `--number-sections`, and
`full_volume_metadata.yaml` does not currently override that. A later
reader-facing assembly should enable numbering there rather than hard-coding
numbers in prose.
