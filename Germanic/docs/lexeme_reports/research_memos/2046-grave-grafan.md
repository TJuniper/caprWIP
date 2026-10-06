# Research memo — 2046 grave / grafan

## Starting point

- **ID:** 2046
- **CONCEPT:** grave
- **COUNTERPART:** `grafan`
- **PROTO:** `*grábaną`
- **PROTOFORM:** `*grábaną`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `OE target: græf→græfan (inf. of str.v. class VI 'to dig, grave') | OE target: grafan (not græfan); Hogg §5.3.1, Hall s.v. grafan. Proto encoding: -aną for A-restoration; R/T §6.3.1`

The live row already points to the correct OE target `grafan`, but its note still preserves an older and misleading `græf→græfan` formulation. The immediate task is therefore not to discover an unmodelled form, but to separate current evidence for the attested infinitive from stale project history and from the separate noun `græf` “grave.”

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the compact derivation trace showing output `grafan`; the packet's direct quotations from Campbell on A-restoration and the exact DEV_NOTES entry stating that row 2046 is a single-`b` case where A-restoration fires correctly [@Campbell1959; @RingeTaylor2014].
- **Useful background:** the packet's excerpts from `arestoration_r_l_research.md` and `notable_findings.md`, which reinforce that `grafan` is a textbook A-restoration infinitive and that back-vowel suffixes are the crucial conditioning environment [@Campbell1959; @Luick1914; @Kaluza1906].
- **Stale or superseded:** DEV_NOTES passages with temporary inputs `*grabăną` and `*grafaną`, and older debug outputs such as `græfen`/`grafen`; these are diagnostic traces from earlier modelling attempts, not current lexical evidence for the row.
- **Irrelevant or misleading:** `old_english_wiktionary.tsv` gives `grave → græf`, but that is the noun “grave, trench,” not the verbal counterpart represented by row 2046. The note's initial `græf→græfan` clause likewise conflates noun and verb material.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` around the March 2026 A-restoration experiments and the later row-level inventory.
- `Germanic/docs/analysis/arestoration_r_l_research.md`.
- `Germanic/docs/analysis/notable_findings.md`.
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/hogg_vol1.txt`.
- `Germanic/docs/lexeme_reports/coverage_audit.md` and `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.missing_reports.md`.

No separate full dossier for this lexeme was named in the packet or TSV note. The coverage files show that row 2046 requires a memo/report because of its non-empty `NOTE`, and no pilot/full lexeme report already exists.

## Reconstruction and early-stage forms

The row's **cognate-set proto** and current **project input form** are both `*grábaną`; there is no present need to split TSV `PROTO` from TSV `PROTOFORM`.

That input form should still be distinguished from intermediate OE stages inferred inside the derivation. The packet's own trace implies a sequence of roughly:

`*grábaną` (project input) → pre-restoration `*græbaną` after Anglo-Frisian brightening → restored `*grabaną` before the back-vocalic infinitive tail → surface `grafan`.

The experimental DEV_NOTES spellings `*grabăną` and `*grafaną` belong to earlier attempts to encode the infinitive tail more explicitly in the pipeline; they are useful for project chronology, but they are not the live row and should not be promoted over the current TSV form.

## Old English philology

For Old English, the relevant target is the **attested infinitive verb** `grafan` “to dig, grave,” not a reconstructed-only form [@ClarkHall1960]. Clark Hall separately lists:

- `græf` as a noun “cave, grave, trench”;
- `grafan` as the verb “to dig, dig up; grave”;
- `græfð` as present 3 sg. of `grafan`;
- `græfen` as the past participle of `grafan` [@ClarkHall1960].

That lexical split matters here. The English gloss **grave** can point either to the noun `græf` or the verb `grafan`, but row 2046 is clearly the verb row, since its Germanic cognate set is verbal and the live counterpart is the infinitive `grafan`. Kastovsky's discussion of `/æ/ ~ /a/` alternation also treats `grafan` alongside derived `græf-` material, which supports the alternation but does not change the citation form of the verb [@Kastovsky1992, p. 361].

## Project problem and solution

The project problem was not that OE lacked a clear target, but that earlier modelling and note text temporarily drifted toward the wrong shape: first by preserving `græf→græfan` language, and elsewhere by producing non-target infinitival outputs such as `græfen` or by experimenting with alternate encoded inputs.

The current solution is sound:

- keep the row as a **regular** OE strong-verb infinitive row;
- keep the counterpart as `grafan`;
- treat `grafan` as the expected A-restoration outcome under a back-vowel infinitive tail [@Campbell1959; @RingeTaylor2014];
- treat noun `græf` and verbal non-citation forms such as `græfð`/`græfen` as philological background, not as the row target.

## Paradigm probe

No paradigm probe is required for this memo. The row's issue is a citation-form and note-cleanup problem, not an unresolved paradigm-level analogy problem, and the repo-local handbook/dictionary evidence already settles the target infinitive as `grafan`.

If extra QA is ever desired, it would be optional rather than required, and should compare the infinitive `grafan` against at least present 3 sg. `græfð` and past participle `græfen` so the report can show that the front-vowel forms belong to other cells, not to the infinitive lemma.

## Recommended final report

Recommend a short final report stating that row 2046 represents the attested OE strong-verb infinitive `grafan` < project input `*grábaną`, with regular A-restoration before the back-vowel infinitive ending; it should explicitly note that older `græf→græfan` wording is stale because `græf` is a separate noun and forms like `græfð`/`græfen` belong to other paradigm cells.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended.
- **TSV `DERIVATION_CLASS`:** no change recommended.
- **TSV `NOTE`:** **change recommended.** Remove the stale `græf→græfan` clause and replace it with a note that directly identifies `grafan` as the attested infinitive, while mentioning `græf` only as a separate noun if needed. A cleaner note would also say plainly that `-aną` is the live project encoding used to obtain the expected A-restoration outcome.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no mandatory change recommended. The historical `*grabăną` / `*grafaną` experiments are acceptable as archived diagnostics, though they should continue to be read as superseded project history rather than live lexical authority.
