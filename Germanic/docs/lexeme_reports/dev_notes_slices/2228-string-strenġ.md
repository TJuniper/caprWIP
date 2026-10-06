---
row_id: 2228
concept: string
counterpart: strenġ
proto: *strángiz
protoform: *strángiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/dossier-ing-lowering-2026.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2228 string / strenġ

## Current row state

- The live OE row is `2228`, `CONCEPT string`, `COUNTERPART strenġ`, `PROTO *strángiz`, `PROTOFORM *strángiz`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1157-1157].
- `PROTO` and `PROTOFORM` are currently the same row input. Neither should be collapsed into the OE `COUNTERPART`: the comparative/model input is `*strángiz`, while the OE target output is `strenġ` [Germanic/data/germanic-aligned-final.tsv:1157-1157].
- `oe_known_problems.tsv` has no row-local entry for row `2228`, for `strenġ`, or for `*strángiz`; this row is not currently tracked as an exception or wontfix item [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still lists row `2228` as `regular` with no packet, no research memo, no linked slice history, and issue status `none`, which is exactly why the replacement working note has to be conservative about how much row-specific support actually survives [Germanic/docs/lexeme_reports/coverage_audit.md:379-379].

## Detailed development-note summary

The surviving DEV_NOTES support for row `2228` is thin but still usable. It is not a dedicated lexeme dossier about OE `strenġ`; instead, the row survives as a **negative control** inside the 2026 `*-ing-*` / unstressed-`*i` repair. That project context matters, because the note is not trying to prove from scratch that `strenġ` is the OE target. It is trying to prove that the newly added restoration before `*ng` does **not** overgenerate into ordinary palatalized `*Nġ` outcomes such as `*strángiz -> strenġ` [Germanic/docs/DEV_NOTES.md:38257-38299,38371-38387].

The controlling closure note rewrites `OEMedUnstressedILowering` as a composition: first general lowering `{*ĭ} -> {*e}`, then a repair `{*e} -> {*i} || _ {*n} {*g}` for the derivational `*-ing-/*-ung-` class [Germanic/docs/DEV_NOTES.md:38264-38272]. For row `2228`, the crucial part is not the restoration itself but the safety argument immediately following it. DEV_NOTES says that by the time this rule fires, “velar palatalisation has already converted *g → *ġ in palatalising contexts,” and therefore “All other *e + *Ng forms have already become *e + *Nġ” [Germanic/docs/DEV_NOTES.md:38281-38289]. That is the row-specific takeaway: `*strángiz` belongs on the **non-restored** side of the split because its OE output has palatalized `ġ`, not the retained velar `g` that diagnoses the protected `*-ing-/*-ung-` suffix environment.

This means the row has to be described contrastively, not vaguely. `*strángiz` is **not** one of the items for which the project now preserves unstressed `i`; those are the derivational suffix cases, supported in the same DEV_NOTES cluster by the standard handbook formulation that unstressed front vowels normally merge to `e`, while preserved `i` is exceptional in suffixes such as `-ig, -ing, -isc` [Germanic/docs/DEV_NOTES.md:6636-6657; @HoggPhonology1992, pp. 119--20; @Campbell1959, §§369, 380; @RingeTaylor2014, §6.9.6]. Row `2228` is useful precisely because it shows the opposite pattern: a form with historical `*ng` input that has already moved into the palatalized `*Nġ` domain and therefore must stay outside the `*_ng` restoration window [Germanic/docs/DEV_NOTES.md:38281-38299].

DEV_NOTES then makes the comparator function explicit in two tables. In the closure regression table, the row appears as ``*strángiz`` → `strenġ` with the status `✓ no change (palatalised *ġ)` [Germanic/docs/DEV_NOTES.md:38292-38299]. In the later sentinel set for the `*ĭ` cleanup pass, it appears again with the note `*e + *ng + palatal (no restoration)` [Germanic/docs/DEV_NOTES.md:38371-38387]. The wording of that later note should be read as project shorthand, not as a literal claim that the form still contains unchanged surface `*ng` at the point of restoration; the closure note itself is clearer and should control interpretation: relevant non-suffixal contexts have already become `*Nġ`, which is exactly why the `*_ng` restoration does not touch them [Germanic/docs/DEV_NOTES.md:38281-38289].

There is no substantial DEV_NOTES material here about lexical attestation, source disagreement, or a competing OE target. The row's value in current project history is narrower: it is one of the best compact proofs that the 2026 `*_ng` fix was not overbroad. That is enough for a replacement working note, but it also means the row should be treated conservatively for indexing. The surviving support is shared implementation history plus a handbook-backed contrastive generalization, not a rich independent lexeme memo.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-38257-38299

- Source heading: `§17.35.10 Closure (2026-04-27)`
- Source line or section hint: `lines 38257-38299`
- Fragment type: `shared_implementation_closure_with_row_specific_negative_control`
- Status: `current`
- Issue tags: `oe_med_unstressed_i_lowering`; `ng_restoration`; `palatalised_g`; `negative_control`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2057`, `2181`

This is the controlling fragment for row `2228`. It preserves both the implementation and the interpretive rule that later writers would otherwise have to reconstruct manually:

> `# Restore *e → *i before the *ng cluster (Campbell §380, R/T vol.2 §6.9.6,`
> `# Hogg 1992 p.120). Phonetic blocking, not morpho-lexical: *ng is the`
> `# diagnostic for *-ing-/*-ung- derivational suffixes at this stage.` [Germanic/docs/DEV_NOTES.md:38268-38270]

and then, even more importantly for this row:

> `All other *e + *Ng forms have already become *e + *Nġ.` [Germanic/docs/DEV_NOTES.md:38284-38289]

The regression table immediately applies that rule to the row itself:

> `| \`*strángiz\`        | \`strenġ\`    | ✓ no change (palatalised *ġ) |` [Germanic/docs/DEV_NOTES.md:38292-38299]

For row `2228`, this fragment should be read as the authoritative current explanation of why the form stays regular while the new `*_ng` restoration is added elsewhere. The handbook support named inside the note matches the standard generalization about unstressed-vowel merger and suffixal `-ing` preservation [@Campbell1959, §380; @RingeTaylor2014, §6.9.6; @HoggPhonology1992, pp. 119--20].

### DEV_NOTES:line-38371-38387

- Source heading: `§17.36 *ĭ (i-breve) cleanup — sentinel test set`
- Source line or section hint: `lines 38371-38387`
- Fragment type: `shared_regression_verification`
- Status: `current`
- Issue tags: `sentinel_table`; `no_regression`; `palatal_context`; `row_2228`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2057`, `2181`

This later table matters because it shows that row `2228` remained a live comparator after the first closure, not just during one ad hoc rebuild. The row is carried forward as:

> `| \`*strángiz\`      | \`strenġ\`   | *e + *ng + palatal (no restoration) |` [Germanic/docs/DEV_NOTES.md:38381-38381]

The phrase `*e + *ng + palatal` is useful as a mnemonic label, but the earlier closure prose should still control the technical reading: by the relevant point in the cascade, the palatalized row is outside the retained-velar `*_ng` restoration environment [Germanic/docs/DEV_NOTES.md:38281-38289]. For later report work, the value of this fragment is verification history: it confirms that `*strángiz -> strenġ` stayed stable through the subsequent `*ĭ` cleanup.

### DEV_NOTES:line-6636-6657

- Source heading: `Late OE unstressed front-vowel merger (general handbook digest)`
- Source line or section hint: `lines 6636-6657`
- Fragment type: `shared_handbook_context_for_contrast`
- Status: `current`
- Issue tags: `unstressed_front_vowel_merger`; `suffixal_i_preservation`; `contrastive_background`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2057`, `2181`

This fragment is not row-specific, but it is the best preserved source digest explaining why row `2228` is a **negative control** rather than a restoration target. DEV_NOTES quotes Hogg:

> `by about 700 all unstressed front vowels had become /e/. The only exception is that [i] was preserved in derivational suffixes such as -ig, -ing, -isc` [Germanic/docs/DEV_NOTES.md:6636-6645; @HoggPhonology1992, pp. 119--20]

and then quotes Campbell and Ringe–Taylor for the same merger/exemption background [Germanic/docs/DEV_NOTES.md:6647-6657; @Campbell1959, §369; @RingeTaylor2014, §6.9.6]. For row `2228`, this shared fragment should only be used contrastively: it explains the class that **does** keep `i`, so that `*strángiz -> strenġ` can be kept separate from that class.

## Superseded or diagnostic material

- There is no surviving DEV_NOTES evidence that `strenġ` itself was ever under row-specific target dispute. The row enters the notes only as a comparator in shared implementation work, so later prose should not invent a richer lexeme controversy than the sources actually preserve [Germanic/docs/DEV_NOTES.md:38257-38299,38371-38387].
- The sentinel wording `*e + *ng + palatal (no restoration)` is diagnostically useful, but the closure prose is the more precise statement of current policy. If later work cites the sentinel line alone, it risks obscuring the real point that non-suffixal palatal contexts have already become `*Nġ` before the `*_ng` restoration is evaluated [Germanic/docs/DEV_NOTES.md:38281-38289,38381-38381].
- `Germanic/docs/dossier-ing-lowering-2026.md` is useful supporting infrastructure for the general `*-ing-*` repair, especially its handbook digest on preserved suffixal `i`, but it does not add a separate row-local `strenġ` discussion. For this row it should remain supporting background, not be mistaken for a dedicated memo [Germanic/docs/dossier-ing-lowering-2026.md:144-237].
- Coverage infrastructure still says `none` for row `2228`, and that remains the correct practical reading. This slice replaces repeated returns to DEV_NOTES, but it does not by itself create packet-level evidence or a row-specific philological audit [Germanic/docs/lexeme_reports/coverage_audit.md:379-379].

## Open questions for later work

- If row `2228` is ever to become comfortably indexable, add a genuinely row-specific memo or packet with direct lexicographic / etymological support for `strenġ`; the current surviving note set is mostly shared implementation history.
- If a later central report on the `*_ng` restoration is written, keep row `2228` explicitly on the **non-restored** side of the contrast: retained-velar derivational `*-ing-/*-ung-` versus palatalized non-suffixal `*Nġ` outcomes [Germanic/docs/DEV_NOTES.md:38281-38299; @Campbell1959, §380; @RingeTaylor2014, §6.9.6].
- If future work revisits the chronology of palatalization versus unstressed-vowel lowering, preserve the current closure wording that makes the row usable as a diagnostic: the key claim is not just that `strenġ` survived unchanged, but why it survived unchanged.
