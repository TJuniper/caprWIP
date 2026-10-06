---
row_id: 2231
concept: sun
counterpart: sunne
proto: "*súnnōn"
protoform: "*súnnōn"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/final_vowel_missing_analysis.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2231 sun / sunne

## Current row state

- The live OE row gives `CONCEPT = sun`, `COUNTERPART = sunne`, `PROTO = *súnnōn`, `PROTOFORM = *súnnōn`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1168-1168].
- `PROTO` and `PROTOFORM` are not split in the current row. The comparative headword and the row-specific derivational input are both `*súnnōn`; the distinct OE-side target is `COUNTERPART = sunne` [Germanic/data/germanic-aligned-final.tsv:1168-1168].
- The row has no project note in the TSV `NOTE` column beyond source provenance, and its `HISTORY` field is only duplicated Wiktionary sourcing rather than a project-authored lexical argument [Germanic/data/germanic-aligned-final.tsv:1168-1168].
- `oe_known_problems.tsv` has no entry for row `2231`, `*súnnōn`, or `sunne`, so this item is not currently tracked as an OE exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- No packet, research memo, or report stem already exists for row `2231`, so this slice uses the canonical row-based filename `2231-sun-sunne.md` [Germanic/docs/lexeme_reports/coverage_audit.md:381-381].

## Detailed development-note summary

This row is one of the cleaner OE items: the live row already encodes the regular weak-feminine analysis, and surviving DEV_NOTES material does not point toward any competing policy. The stable project claim is that `sunne` is the expected OE reflex of a feminine n-stem nominative singular in `*-ōn`, not an analogical repair, paradigm-cell substitute, or workaround target [Germanic/data/germanic-aligned-final.tsv:1168-1168; @HoggPhonology1992, §3.3].

The important categorical distinction is straightforward but should still be kept explicit. `PROTO = *súnnōn` names the comparative etymological item; `PROTOFORM = *súnnōn` is the row's actual OE-facing input; and `COUNTERPART = sunne` is the expected OE output of that input [Germanic/data/germanic-aligned-final.tsv:1168-1168]. Nothing in surviving DEV_NOTES suggests that the row should instead be driven from some oblique form, from a remodeled proto input, or from a different derivation class.

The most useful shared DEV_NOTES material is the repository's general account of final `*-ōn` outcomes in feminine n-stems. In the shared derivational note, DEV_NOTES states that a word-final surviving bimoric long `ō` yields OE `-e`, and gives the concrete chain `fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) → PWGmc *tunga → OE tunge` [Germanic/docs/DEV_NOTES.md:2726-2739]. A later source note then says that Ringe-Taylor treat `fem. n-stem nom.sg. tunge < PWGmc *tunga` as a regular outcome in the same breath as other regular `-e` endings [Germanic/docs/DEV_NOTES.md:23682-23690; @RingeTaylor2014, §6.8.3]. Row `2231` fits exactly that same pattern, only with `*súnnōn > sunne` instead of `*tungōn > tunge`.

The one DEV_NOTES passage that names this row's lexeme directly is only an example embedded inside the much larger `tang/tange` discussion, but it is still worth preserving because it states the right category explicitly. There DEV_NOTES contrasts strong `ō`-stem and weak `ōn`-stem outcomes and says that the weak nominative singular yields OE `-e`, "like *tunge* < *tungōn-, *sunne* < *sunnōn-" [Germanic/docs/DEV_NOTES.md:32289-32295]. That is not a dedicated sun dossier, but it does preserve the exact project assumption currently encoded in the row: `sunne` is being treated as the ordinary weak-feminine OE reflex of `*súnnōn`, not as a special exception.

The small analysis note on final vowels says the same thing even more bluntly: `Fem. n-stem nom.sg: PGmc *-ōn → OE -e (e.g., sunne 'sun', hearpe 'harp')`, followed by the explicit developmental sketch `*sunnōn → *sunnōn` (no change), then nasal loss, then reduction of final `*-ō` to OE `-e` in the feminine class [Germanic/docs/analysis/final_vowel_missing_analysis.md:41-49]. That analysis is not itself DEV_NOTES, but it matches the shared DEV_NOTES logic and is useful because row `2231` has almost no dedicated lexical prose elsewhere.

Because the surviving DEV_NOTES support is shared and schematic rather than row-specific, this slice should function as the replacement working note: regular feminine n-stem; no live evidence for a PROTO/PROTOFORM split; no exception handling in `oe_known_problems.tsv`; and no superseded row-local proposal currently needing to be fenced off. The weakness here is not phonological uncertainty but documentary thinness.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2726-2739

- Source heading: `final long ō outcomes; shared feminine n-stem derivation note`
- Source line or section hint: `lines 2726-2739`
- Fragment type: `shared_sound_change_support`
- Status: `current_but_shared`
- Issue tags: `feminine_n_stem`; `final_ōn`; `shared_example`
- Recommended next use: `use_for_row_support_not_as_row_specific_dossier`
- Shared with row IDs: `2138`; `2231`; other weak feminine rows in `*-ōn`

DEV_NOTES explains the general category used by this row: surviving word-final bimoric long `ō` gives OE `-e`, and the feminine n-stem example is quoted directly as `fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) → PWGmc *tunga → OE tunge` [Germanic/docs/DEV_NOTES.md:2730-2737]. The note then says that the FST models the feminine n-stem case separately: `For fem. n-stems, modelled by NWGmcNStemNLoss: {*ō}{*n} → {*ǭ} word-finally, then {*ǭ} → {*æ} → OE -e` [Germanic/docs/DEV_NOTES.md:2736-2739]. Row `2231` is not named here, but the same rule is exactly the one needed for `*súnnōn > sunne`.

### DEV_NOTES:line-23682-23690

- Source heading: `Ringe-Taylor on regular -e outcomes`
- Source line or section hint: `lines 23682-23690`
- Fragment type: `shared_source_claim`
- Status: `current_but_shared`
- Issue tags: `RingeTaylor`; `lautgesetzlich`; `feminine_n_stem`
- Recommended next use: `use_as_handbook_support`
- Shared with row IDs: `2138`; `2231`; other rows using the same final-vowel account

This source note matters because it treats the feminine n-stem nominative singular as regular rather than analogical. DEV_NOTES quotes Ringe-Taylor's derivational paragraph and then summarizes that it is presented `in the same paragraph that derives a-stem dat.sg. -e < PWGmc *-ē and fem. n-stem nom.sg. tunge < PWGmc *tunga`. DEV_NOTES concludes: `R/T treat all three as lautgesetzlich outcomes` [Germanic/docs/DEV_NOTES.md:23685-23690; @RingeTaylor2014, §6.8.3]. For row `2231`, the relevance is categorical rather than lexical: `sunne` belongs to the same regular ending type.

### DEV_NOTES:line-32289-32295

- Source heading: `tang/tange discussion; weak ōn-stem comparison`
- Source line or section hint: `lines 32289-32295`
- Fragment type: `direct_lexeme_mention_in_shared_note`
- Status: `current_but_incidental`
- Issue tags: `sunne_example`; `weak_ōn_stem`; `contrast_with_strong_ō_stem`
- Recommended next use: `keep_as_row_specific_hook`
- Shared with row IDs: `2231`; `2138`

This is the only surviving DEV_NOTES passage that names the lexeme directly. In contrasting strong `ō`-stem and weak `ōn`-stem outcomes, the note says that the target `tange` could reflect `the NomSg of a weak ōn-stem variant (PGmc *tangōn-, fem., yielding OE -e like *tunge* < *tungōn-, *sunne* < *sunnōn-)` [Germanic/docs/DEV_NOTES.md:32289-32295]. The sun material here is incidental, but it is still a useful direct statement that DEV_NOTES understands `sunne` as the regular OE `-e` reflex of `*sunnōn-`.

## Superseded or diagnostic material

- No row-specific superseded DEV_NOTES proposal was found for `sun` / `sunne`. The documentary problem is scarcity, not a visible trail of abandoned protoforms or rival counterparts.
- The only direct DEV_NOTES hit is embedded in another lexeme's argument (`tang/tange`), so it should not be over-read as a dedicated sun dossier. It is best treated as a correct but shared comparator passage [Germanic/docs/DEV_NOTES.md:32289-32295].
- `coverage_audit.md` still lists row `2231` with `packet no`, `memo -`, `report -`, and `links none`, which confirms that the row had no prior lexeme-report infrastructure to reuse before this slice was written [Germanic/docs/lexeme_reports/coverage_audit.md:381-381].

## Open questions for later work

- If a later lexeme report is written, add direct dictionary citations for the OE lemma and paradigm so the row does not rely almost entirely on shared weak-noun discussions.
- If more feminine `*-ōn` rows are sliced, consider whether the shared DEV_NOTES material on `*tungōn > tunge` and `*sunnōn > sunne` should be indexed once for a cluster of weak feminine rows rather than treated as strong row-local evidence.
- If `index.tsv` is updated later, keep the row conservative unless a dedicated sun note or memo is added; the present attachment is real but mostly shared infrastructure rather than a substantive sun-specific dossier.
