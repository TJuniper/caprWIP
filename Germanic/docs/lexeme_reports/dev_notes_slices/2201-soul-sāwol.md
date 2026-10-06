---
row_id: 2201
concept: soul
counterpart: sāwol
proto: *sáiwalō
protoform: *sáiwalō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2201 soul / sāwol

## Current row state

- CONCEPT: `soul` [Germanic/data/germanic-aligned-final.tsv:1051-1051]
- COUNTERPART: `sāwol` [Germanic/data/germanic-aligned-final.tsv:1051-1051]
- PROTO: `*sáiwalō` [Germanic/data/germanic-aligned-final.tsv:1051-1051]
- PROTOFORM: `*sáiwalō` [Germanic/data/germanic-aligned-final.tsv:1051-1051]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1051-1051]
- `oe_known_problems.tsv` currently has no entry for `*sáiwalō`, `sāwol`, or `soul`, so the row is not being managed as a live unresolved exception there [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage/report infrastructure still shows row `2201 | soul | sāwol | regular | no | - | - | - | none`, i.e. no packet, research memo, or report stem to reuse; this slice therefore has to serve as the row's replacement working note on its own [Germanic/docs/lexeme_reports/coverage_audit.md:361-361].
- The obvious linked analysis file treats the row as already correct and outside the A-restoration problem-space: `sáiwalō    sāwol         # OK — *aiwal-: multi-segment intervening, no relevance` and later `intervening *iwal is multi-segment; restoration not triggered for first *a* (already covered by other rules)` [Germanic/docs/analysis/arestoration_r_l_research.md:521-522,718-718].

## Development-note summary

The live row is straightforward in its current policy but not in its project history. Row 2201 now keeps `PROTO = *sáiwalō`, `PROTOFORM = *sáiwalō`, `COUNTERPART = sāwol`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1051-1051]. That means there is no current row-level distinction between cognate-set headword and OE-directed input here, but the distinction still matters conceptually: `PROTO` and `PROTOFORM` are both the inherited Germanic form, while `COUNTERPART` is the OE outcome that the notes are trying to justify, not another proto-level label.

The most reusable current linguistic point appears surprisingly early in DEV_NOTES, in the general syncope summary. There the notes list `*saiwalō -> *sawlu -> sāwol 'soul'` as an example of non-high-vowel syncope after a stressed syllable [@RingeTaylor2014, §6.7.3; @Campbell1959, §§388-392; @HoggPhonology1992, pp. 225-232; Germanic/docs/DEV_NOTES.md:700-716]. For this row, that compact chain is still valuable because it captures the first indispensable step: medial `-a-` is expected to syncopate, so the row is not supposed to preserve a trisyllabic pre-surface shape all the way into OE.

The later row-specific mismatch dossier preserves the fuller OE-side issue. Under older row numbering, DEV_NOTES records residual mismatch table entry `1051 | *sáiwalō | sāwul | sāwol | vowel_quality__u_o_alternation`, so later readers must not be confused when the same lexeme appears as row 1051 in those sections but row 2201 in the live TSV [Germanic/docs/DEV_NOTES.md:22550-22553]. The important philological result of that dossier is not the old mismatch itself but the source consensus it assembled: Campbell §362 says, “Normal OE forms are fugol, tungol, cumbol, **sāwol**, nagel …”; Campbell §373 says that unaccented `u` may be preserved in early or dialectal material but very often becomes `o`; and Campbell §589.5 says explicitly that `Sāwol soul ... had syncopation of medial a in all cases (§341), but parasiting subsequently arose in nom. sg., though saul, sæwl also occur` [@Campbell1959, §§362, 373, 589.5; Germanic/docs/DEV_NOTES.md:22637-22657]. Ringe & Taylor add the oblique comparator `sāwle 'for a soul' < sawle < *sawele < PWGmc *saiwalē < PGmc *saiwaldai`, which confirms that the lexeme really does belong to a `sawl-/sāwl-` family and was not invented ad hoc to rescue one surface form [@RingeTaylor2014, §6.8.3; Germanic/docs/DEV_NOTES.md:22655-22657].

The upshot of those quotations is precise. West Saxon `sāwol` is the canonical current target; `sāwul` is the early/dialectal-looking variant that the pipeline was producing during the residual-regression phase; and the lexeme's history involves both syncope and later parasite-vowel behavior [@Campbell1959, §§362, 373, 589.5; Germanic/docs/DEV_NOTES.md:22659-22666]. This is why the row can remain `regular` even though DEV_NOTES once treated it as a mismatch: the problem was not a disputed OE target or a disputed proto input, but a chronology bug in how the transducer reached the already agreed target.

DEV_NOTES also preserves an important false start that later writers would otherwise repeat. The first implementation proposal tried to add an `OEWLInsertion` rule, directly paralleling `OEGLInsertion`, on the assumption that the derivation reached `*sāwl` and merely lacked word-final `w+l` parasiting [Germanic/docs/DEV_NOTES.md:22676-22701,23281-23320]. That proposal quoted the right sources but attached them to the wrong structural diagnosis. A later stage-by-stage trace showed that the assumed `*sāwl` stage never appeared in the live pipeline: the actual chain was `*sāwalō -> *sāwalu -> *sāwulu -> *sāwul`, so by the time epenthesis ran, `w` and `l` were no longer adjacent [Germanic/docs/DEV_NOTES.md:23343-23375]. For replacement-note purposes, this matters because the scholarly evidence remained sound while the first FST repair plan became superseded.

The decisive current note is the subsequent chronology correction. DEV_NOTES rechecked the literature and concluded that inter-stress raising belongs to an earlier Pre-OE / early-OE layer, while medial unstressed `u > o` belongs to a later OE layer; therefore raising should feed lowering, not follow it [@RingeTaylor2014, §6.3.3; @Campbell1959, §§49, 373-374; @HoggPhonology1992, §3.3.3.2; Germanic/docs/DEV_NOTES.md:23423-23449]. After moving `OEMedUnstressedULowering` after `OEInterStressRaising`, the probe result was `40 mismatches` at baseline versus `38` after the reorder, with `*sáiwalō -> sāwol` and `*wír-aldu -> weorold` both fixed and “new regressions: none” [Germanic/docs/DEV_NOTES.md:23451-23485]. That is the present project authority for row 2201: the row is now regular because the chronology bug was fixed, not because the row was reclassified or manually papered over.

The linked A-restoration analysis is useful mainly as a guardrail. It confirms twice that `*sáiwalō` is not an A-restoration case: the first `a` is not in the relevant `a + single r/l + back-vowel trigger` environment, because `*iwal` is multi-segment, and the probe already gave `sāwol` before and after that line of work [Germanic/docs/analysis/arestoration_r_l_research.md:521-522,718-718,758-758]. That means later writers should keep the row attached to the syncope / parasite-vowel / unstressed-`u` chronology story, not fold it into unrelated restoration debates merely because `-wal-` contains an `l`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-700-716

- Source heading: `Summary of OE syncope rules (scholarly consensus)`
- Source line or section hint: `lines 700-716`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `medial_syncope`; `shared_sound_change`; `soul_example`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This shared syncope summary is still the cleanest short statement of the lexeme's first crucial step. DEV_NOTES gives `*saiwalō -> *sawlu -> sāwol 'soul'` as an example of non-high-vowel syncope in a stressed environment [@RingeTaylor2014, §6.7.3; @Campbell1959, §§388-392; @HoggPhonology1992, pp. 225-232; Germanic/docs/DEV_NOTES.md:700-716]. For row 2201, the value of the fragment is not that it solves every later OE detail, but that it locks in the expected loss of medial `-a-` and shows that `sāwol` was already being treated as a regular historical endpoint in the project's general sound-change notes.

### DEV_NOTES:line-22550-22553

- Source heading: `Phase 1d-β post-Option-X: source-verified research on the four residual regressions`
- Source line or section hint: `lines 22550-22553`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_row_number`; `residual_mismatch`; `u_o_alternation`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This short inventory line is purely diagnostic now, but it is important because it explains why later DEV_NOTES prose talks about row `1051` instead of live row `2201`. The notes record the old state as `*sáiwalō -> sāwul` with expected `sāwol`, bucketed under `vowel_quality__u_o_alternation` [Germanic/docs/DEV_NOTES.md:22550-22553]. Later reporting should preserve this as project chronology only, not as live row status.

### DEV_NOTES:line-22635-22664

- Source heading: `Case 2 — *sáiwalō → sāwul (expected sāwol)`
- Source line or section hint: `lines 22635-22664`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `literature_consensus`; `parasite_vowel`; `dialectal_u_vs_ws_o`; `medial_syncope`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current source fragment for the row's philology. It preserves the exact quotations that justify the target: Campbell's list of normal WS parasite-vowel forms with `sāwol`, Campbell's note that protected unstressed `u` may survive in early or dialectal materials but commonly appears as `o`, Campbell's explicit statement that `sāwol` had syncope of medial `a` and later parasiting in the nominative singular, and Ringe & Taylor's oblique form `sāwle` [@Campbell1959, §§362, 373, 589.5; @RingeTaylor2014, §6.8.3; Germanic/docs/DEV_NOTES.md:22635-22664]. Even if later implementation prose changes, this source block remains the durable authority for why OE `sāwol` is the right endpoint.

### DEV_NOTES:line-22665-22701

- Source heading: `What our pipeline does` / `Revised proposal`
- Source line or section hint: `lines 22665-22701`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `first_fix_attempt`; `oewlinsertion`; `misdiagnosed_structure`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment preserves the first serious repair attempt and should be kept only as superseded history. DEV_NOTES correctly noticed that the pipeline was producing `sāwul` instead of `sāwol`, but it initially proposed a new `OEWLInsertion` rule on the assumption that the relevant structure was bare word-final `*wl` [Germanic/docs/DEV_NOTES.md:22665-22701]. That diagnosis turned out to be incomplete, so later work should mine this fragment for chronology and rationale, not for current implementation advice.

### DEV_NOTES:line-23249-23320

- Source heading: `Case 2 implementation write-up`
- Source line or section hint: `lines 23249-23320`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `oewlinsertion`; `audit`; `inert_fix`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This write-up is worth retaining because it records the exact first implementation theory, including the audit that `sāwol` was the only tracked OE row with the relevant `w + l` word-final cluster [Germanic/docs/DEV_NOTES.md:23267-23299]. But its central claim — that direct `OEWLInsertion` would yield `*sāwol` — is no longer current. Later trace work disproved that pathway, so this section now functions as careful but superseded project history [Germanic/docs/DEV_NOTES.md:23301-23320].

### DEV_NOTES:line-23334-23416

- Source heading: `Case 2 revised: OEWLInsertion does not fire; actual pathway differs`
- Source line or section hint: `lines 23334-23416`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `stage_trace`; `actual_pathway`; `repair_options`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This is the key diagnostic bridge between the stale `OEWLInsertion` idea and the final solution. DEV_NOTES traces the actual path `*sāwalō -> *sāwalu -> *sāwulu -> *sāwul`, showing that no `*sāwl` stage ever appears and therefore no `w+l` insertion rule can fire [Germanic/docs/DEV_NOTES.md:23343-23375]. It then lays out three possible repairs and explicitly identifies the real defect as rule ordering, not missing parasiting [Germanic/docs/DEV_NOTES.md:23377-23416]. The fragment is no longer current in its menu of options, but it remains the best diagnostic explanation of why the first proposal failed.

### DEV_NOTES:line-23418-23485

- Source heading: `Case 2 implementation via R3 (probe + scholarship)`
- Source line or section hint: `lines 23418-23485`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `chronology_reorder`; `current_fix`; `probe_result`; `resolved_mismatch`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current implementation fragment for row 2201. DEV_NOTES rechecks the chronology in Ringe & Taylor, Campbell, Hogg, and Luick, concludes that inter-stress raising must precede medial unstressed `u > o`, applies that reorder, and records the successful probe: baseline `40` mismatches, reordered `38`, with `*sáiwalō -> sāwol` fixed and no new regressions [@RingeTaylor2014, §6.3.3; @Campbell1959, §§49, 373-374; @HoggPhonology1992, §3.3.3.2; Germanic/docs/DEV_NOTES.md:23418-23485]. For current row policy, this fragment matters more than the earlier mismatch write-up because it explains why the row is now regular rather than merely why it once failed.

## Superseded or diagnostic material

- The residual-regression inventory and all prose that treats this lexeme as mismatch row `1051` are obsolete as row status, though still useful for project chronology [Germanic/docs/DEV_NOTES.md:22550-22553].
- The `OEWLInsertion` proposal should be preserved only as superseded analysis. It had a sensible source motivation but depended on a structural stage (`*sāwl`) that the trace later showed never occurs in the actual derivation [Germanic/docs/DEV_NOTES.md:22676-22701,23281-23320,23343-23375].
- The important live distinction here is not between competing proto inputs but between outdated and current implementation diagnoses. `PROTO` and `PROTOFORM` both remain `*sáiwalō`; the stale part of DEV_NOTES is the repair plan, not the lexeme's etymon or OE target [Germanic/data/germanic-aligned-final.tsv:1051-1051; Germanic/docs/DEV_NOTES.md:22635-22664,23418-23485].
- The A-restoration analysis file should not be overread. It is valuable because it confirms that row 2201 was unaffected by that separate repair campaign, but it is not the main authority for `sāwol` itself [Germanic/docs/analysis/arestoration_r_l_research.md:521-522,718-718].

## Open questions for later work

- If this row ever receives a full lexeme report, decide whether the report should foreground Campbell's nominal-sg. parasiting account (`sāwol ... had syncopation of medial a in all cases ... parasiting subsequently arose in nom. sg.`) or the transducer-oriented chronology fix. Both matter, but the former is the cleaner philological statement of the outcome [@Campbell1959, §589.5; Germanic/docs/DEV_NOTES.md:22650-22653,23418-23485].
- If `dev_notes_slices/index.tsv` is updated later, the safest current anchors are `DEV_NOTES:line-22635-22664` for the philology and `DEV_NOTES:line-23418-23485` for the current implementation resolution. `DEV_NOTES:line-22550-22553`, `DEV_NOTES:line-22665-22701`, `DEV_NOTES:line-23249-23320`, and `DEV_NOTES:line-23334-23416` belong in index metadata only as diagnostic or superseded history [Germanic/docs/DEV_NOTES.md:22550-23485].
- If future cleanup revisits shared sound-change prose, keep row 2201 attached to the syncope and unstressed-`u/o` chronology cluster rather than to A-restoration. The live analysis record already says the restoration environment is irrelevant here [Germanic/docs/analysis/arestoration_r_l_research.md:521-522,718-718].
