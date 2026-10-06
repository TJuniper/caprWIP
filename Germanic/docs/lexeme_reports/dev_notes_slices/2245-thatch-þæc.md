---
row_id: 2245
concept: thatch
counterpart: þæc
proto: *θáką
protoform: *θáką
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2245 thatch / þæc

## Current row state

- CONCEPT: `thatch`
- COUNTERPART: `þæc`
- PROTO: `*θáką`
- PROTOFORM: `*θáką`
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1221-1221]
- The live TSV row carries only source boilerplate (`Source: Wiktionary etymology ...` twice) and no row-specific derivational note beyond the regular classification, so the slice has to reconstruct working policy from shared DEV_NOTES phonology rather than from a dedicated lexeme discussion [Germanic/data/germanic-aligned-final.tsv:1221-1221].

## Detailed development-note summary

No surviving DEV_NOTES passage appears to discuss `þæc`, `thatch`, or `*θáką` directly. The replacement note for row 2245 therefore has to be conservative: the live TSV state is accepted as current, and the supporting argument comes from shared chronology and sound-change notes rather than from a lexeme-specific memorandum. That thinness is important to preserve explicitly, because it means the row is currently **regular by shared rule support**, not by a dedicated row-level DEV_NOTES adjudication.

The main shared chronology note is the Ringe-Taylor passage copied into DEV_NOTES on loss of final short low vowels. DEV_NOTES says that R/T treat the loss of word-final `*-a` and `*-ą` as a **PWGmc** change and quotes the sequence `PGmc *stabaz ... > PWGmc *stab ... > OE stæf` and `PGmc *paþaz ... > PWGmc *paþ ... > OE pæþ` [@RingeTaylor2014, vol. 2, pp. 45-46, 307; Germanic/docs/DEV_NOTES.md:22099-22120]. For row 2245, that chronology strongly favors reading `*θáką` at the Anglo-Frisian Brightening stage as effectively monosyllabic `*þak`, not as a form that still keeps a following back-vocalic tail. Once the final short vowel is gone, there is no surviving back-vowel trigger for A-restoration, so fronting of stressed monosyllabic `*á` to `æ` is the expected direction rather than something to retract [@RingeTaylor2014, vol. 2, pp. 45-46; Germanic/docs/DEV_NOTES.md:22111-22120,22151-22155].

The second shared point is the palatalization chronology. DEV_NOTES' Hogg summary states that "`First fronting` (= fronting of `*a → *æ`, Anglo-Frisian Brightening) precedes palatalization" [@HoggPhonology1992, §§7.30-7.36; Germanic/docs/DEV_NOTES.md:34401-34410]. That ordering matters directly for `*θáką`: if fronting yields `*þæk` before velar palatalization applies, then the `*æ` counts as a primary front vowel in precisely the environment that licenses palatalization/affrication of `*k` [Germanic/docs/DEV_NOTES.md:34402-34404,34407-34417]. On that shared chronology, `*θáką > *þæk > þæc` is not a special repair but the regular interaction of fronting and palatalization.

The clearest in-repo control case is the `makô` diagnostic. DEV_NOTES says that before the Class II weak-verb fix, ``makô → mæċa`` was wrong because a missing A-restoration trigger let fronting survive where it should have been retracted: “The `*æ` then triggered palatalization of `*k → *ʧ (→ ċ)`” [@RingeTaylor2014, vol. 2, p. 205; Germanic/docs/DEV_NOTES.md:2921-2934]. After the fix, the expected result is `maca`, because a following back vowel `*ô` really should trigger restoration and block the front-vowel environment [Germanic/docs/DEV_NOTES.md:2923-2934]. That note is diagnostic, not lexeme-specific, but it is still useful for row 2245 because it shows the inverse configuration. `þæc` is **not** a `maca`-type case with a preserved following back vowel; it is the kind of apocopated monosyllable where no restoration trigger remains, so fronting and then palatalization are exactly what should happen.

The current row policy should therefore stay simple and distinct at all three levels. `PROTO` remains `*θáką` as the cognate-set headword; `PROTOFORM` also remains `*θáką`, because the row does not need a surrogate paradigm cell or alternate OE-facing input; and `COUNTERPART` remains `þæc`, because the shared chronology notes support it as the regular OE outcome [Germanic/data/germanic-aligned-final.tsv:1221-1221; @RingeTaylor2014, vol. 2, pp. 45-46, 307; @HoggPhonology1992, §§7.30-7.36]. What is thin here is not the regularity claim itself, but the lexeme-specific DEV_NOTES paper trail. The row currently has general phonological support, not a dedicated `þæc` dossier.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:no-exact-hit-for-2245-thatch-þæc

- Source heading: no exact `þæc` / `thatch` / `*θáką` heading survives in `DEV_NOTES.md`
- Source line or section hint: no direct hit
- Fragment type: `unclear_needs_human_review`
- Status: `current_but_thin`
- Issue tags: `missing_row_specific_authority`; `negative_result`; `shared_phonology_only`
- Recommended next use: `check_against_literature`
- Shared with row IDs:

Direct review does not produce a row-specific DEV_NOTES fragment for this lexeme. That negative result should be preserved rather than normalized away, because it explains why the present slice relies on shared chronology notes and why the row is a poor candidate for immediate indexing.

### DEV_NOTES:line-22099-22155

- Source heading: `R/T on word-final *a`
- Source line or section hint: `lines 22099-22155`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `PWGmc_apocope`; `AFB`; `monosyllabic_fronting`; `no_restoration_trigger`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2212`

This is the main current support for treating row 2245 as a regular apocopated monosyllable. DEV_NOTES preserves R/T's chronology that word-final short `*-a` and `*-ą` are lost already in PWGmc, then explicitly illustrates the outcome with forms like `*stabaz > *stab > stæf` and `*paþaz > *paþ > pæþ` [@RingeTaylor2014, vol. 2, pp. 45-46, 307; Germanic/docs/DEV_NOTES.md:22099-22120]. The same note then stresses that stressed monosyllabic `*á` still fronts word-finally after that apocope [Germanic/docs/DEV_NOTES.md:22151-22155]. For `*θáką`, this is the shared argument for `*þak > *þæk`, with no following back vowel left to force A-restoration.

### DEV_NOTES:line-34399-34417

- Source heading: `The chronological issue: palatalization BEFORE or AFTER i-umlaut?`
- Source line or section hint: `lines 34399-34417`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `palatalization`; `AFB`; `chronology`; `primary_front_vowel`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2151`

This shared chronology note gives the missing second half of the derivation. DEV_NOTES summarizes the traditional account as: first palatalization applies before primary front vowels, and Hogg's refinement is that “First fronting” (`*a → *æ`) precedes palatalization [@HoggPhonology1992, §§7.30-7.36; Germanic/docs/DEV_NOTES.md:34401-34410]. That means the fronted vowel in pre-OE `*þæk` is already in place when the velar is evaluated. For row 2245, the fragment is useful because it explains why fronting and palatalization are mutually reinforcing here rather than competing repairs.

### DEV_NOTES:line-2921-2934

- Source heading: `A-restoration fix for {*ô}`
- Source line or section hint: `lines 2921-2934`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `a_restoration`; `palatalization`; `control_case`; `inverse_comparator`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This note is not about `þæc`, but it is the best explicit DEV_NOTES statement of the restoration/palatalization interaction that the row depends on. DEV_NOTES says the old `makô → mæċa` output was wrong because missing A-restoration left fronted `*æ` in place and “The `*æ` then triggered palatalization of `*k → *ʧ (→ ċ)`”; after adding the missing back-vowel trigger, the correct outcome becomes `maca` [@RingeTaylor2014, vol. 2, p. 205; Germanic/docs/DEV_NOTES.md:2923-2934]. For row 2245, this is useful only as an inverse comparator: where a back vowel survives, restoration blocks the `þæc`-type path; where no such trigger survives, the `þæc` path is the regular one.

## Superseded or diagnostic material

- No dedicated superseded `þæc` proposal survives in DEV_NOTES. The row's thinness comes from missing lexeme-specific note history, not from a stack of abandoned row-local analyses.
- The `makô → maca` passage should not be misread as evidence that row 2245 is unstable. Its value here is purely diagnostic: it demonstrates the reverse environment, where a following back vowel retracts `æ` and prevents the front-vowel-triggered palatalization that row 2245 actually needs [Germanic/docs/DEV_NOTES.md:2921-2934].
- Because no existing packet or research-memo stem was found for this row, the present file uses the canonical row-based filename. That filename choice does not itself imply that the row has index-ready DEV_NOTES coverage.

## Open questions for later work

- If a later lexeme report is written, add direct lexical citations for the noun itself (e.g. Orel/Kroonen/Clark Hall or comparable source extracts) so the file is not relying entirely on shared phonology for an otherwise regular row.
- If later DEV_NOTES work adds a dedicated `þæc` discussion, re-evaluate whether the row should move from no-index working-note status to indexed lexeme coverage.
- If derivational-family reporting becomes relevant, decide whether the final report should briefly cross-reference the related cover/thatch verb family (`*þakjanan`, OE `þeccan`) while still keeping the noun row's `PROTO` and `PROTOFORM` distinct from any verbal derivative.
