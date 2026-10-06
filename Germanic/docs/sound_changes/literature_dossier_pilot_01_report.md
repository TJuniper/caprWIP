# Literature dossier pilot 01 report

## Summary

The pilot dossier covers **SC043 Anglo Frisian Brightening**. I searched the local witnesses for Campbell1959, HoggPhonology1992, RingeTaylor2014, Fulk2018, SieversBrunner1965, Luick1914, Bulbring1902, Kaluza1906, BrightCassidyRingler1971, Polome1994, and Ringe1984, starting from the Google Vision OCR witnesses where they existed. Verified relevant discussion was harvested from **Campbell1959, HoggPhonology1992, Toon1992, RingeTaylor2014, and Fulk2018**.

The matrix now contains **10 verified SC043 rows**, replacing the earlier pilot stub. The dossier file was created at `literature_dossiers/043-anglo-frisian-brightening.dossier.md`, and the SC043 change-entry stub now points to it. No primary source needed to be treated as unavailable in this pass, though several older grammatical witnesses were searched without yet yielding clean dossier-ready extracts.

This dossier is an **internal research file**. Final sound-change volume prose should paraphrase most of this material and reserve direct quotation for short, selective cases only.

## Source search

Shared search terms:

1. Anglo Frisian Brightening
2. Anglo-Frisian Brightening
3. Anglo-Frisian brightening
4. first fronting
5. First Fronting
6. a-fronting
7. fronting of a
8. Germanic a to æ
9. West Germanic a
10. Old English æ
11. breaking after fronting
12. restoration of a
13. retraction
14. A-restoration
15. Campbell first fronting
16. Hogg first fronting
17. Ringe Taylor first fronting

Sources searched:

| Source | Local witness used | Result |
| --- | --- | --- |
| Campbell1959 | `docs/references/campbell_old_english_grammar.txt` | verified |
| HoggPhonology1992 | `docs/references/hogg_vol1.txt` | verified |
| Toon1992 | `docs/references/toon_1992_old_english_dialects.txt` | verified |
| RingeTaylor2014 | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | verified |
| Fulk2018 | `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` | verified |
| SieversBrunner1965 | `docs/references/brunner_1965_altenglische_grammatik.vision.txt` | searched; no clean matrix row harvested |
| Luick1914 | `docs/references/luick_historische_grammatik.txt` | searched; no clean matrix row harvested |
| Bulbring1902 | `docs/references/bulbring_altenglisches_elementarbuch.txt` | searched; chapter signal found, no clean matrix row harvested |
| Kaluza1906 | `docs/references/kaluza_historische_grammatik_englisch.txt` | searched; no clean matrix row harvested |
| BrightCassidyRingler1971 | `docs/references/bright_anglo_saxon_reader.vision.txt` | searched; reader-level witness, not used in verified dossier rows |
| Polome1994 | local Vision OCR witness | searched; peripheral relevance only |
| Ringe1984 | `docs/references/ringe_1984_germanic_e2_and_r.vision.txt` | searched; peripheral relevance only |

## Verified source discussions

1. **Campbell1959** — `§ 131; §§ 139, 157-158`: classic handbook formulation of `a > æ` outside nasal environments, plus the key argument that breaking presupposes an earlier fronted vowel and restoration is later.
2. **HoggPhonology1992** — `p. 101 (§ 3.3.3.1); p. 119`: explicit naming as "Anglo-Frisian Brightening (or First Fronting)" and support for an unstressed extension. **Toon1992** — `p. 446`: a preserved summary of the standard order fronting > breaking/retraction > restoration, drawn from chapter 6 of the same volume and now cited under its own key.
3. **RingeTaylor2014** — `§ 5.1.2, pp. 157-158; § 6.1.1, pp. 168-169; § 6.3.1, pp. 189-190`: cleanest modern explanation of the nasal exception, early chronology, dialect geography, and the explicit proof that retraction is later than fronting and breaking.
4. **Fulk2018** — `§ 4.12, p. 73; § 4.13, pp. 73-74`: compact definition of Anglo-Frisian Brightening, clear examples, and an immediately adjacent account of the breaking and retraction environments that follow it.

## Conditioning and chronology findings

The dossier confirms a stable core picture:

1. Low `a` fronts outside nasal environments.
2. The major non-fronting branch is the nasalized branch before nasals.
3. Later OE Breaking often masks the fronted vowel in `rC`, `lC`, and `h` environments.
4. Later restoration or general retraction before back-vowel environments reintroduces `a` in paradigms such as `faran` and `bacan`.

The strongest reusable order statement is:

1. fronting;
2. breaking;
3. restoration or general retraction.

That order is implied by Campbell, summarized in Hogg, and stated most explicitly by Ringe and Taylor.

## Disagreements or complications

1. The label "Anglo-Frisian Brightening" is standard, but some handbooks describe the change directly rather than foregrounding the subgroup label.
2. English and Frisian do not pattern identically in every environment; Fulk is especially useful here.
3. The geographic spread of the fronted outcomes remains open: Ringe and Taylor allow either a continental or an early-insular locus for much of the variable spread.
4. The transducer's unstressed clause is supportable from Hogg, but most handbook discussion centers the stressed-vowel change, so chapter framing will need care.

## Dossier format assessment

The dossier structure worked well for this pilot. Chronological source blocks plus a thematic synthesis were enough to keep quotations, chronology claims, and conditioning notes readable without turning the file into polished chapter prose.

The main improvement before scaling is to treat the **witness actually used** as a first-class part of the workflow. In practice that means continuing to start from Google Vision OCR when available, and probably adding an explicit `witness_used` or `locator_confidence` note to future dossiers when OCR and PDF witnesses diverge.

## Next recommended task

**A. Build a second literature dossier pilot, preferably SC063 OE High Vowel Apocope.**

The pilot format is reusable, the main handbook sources were accessible locally, and the remaining open questions are normal chapter-design questions rather than workflow blockers.
