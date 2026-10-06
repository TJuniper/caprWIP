---
row_id: 2174
concept: seven
counterpart: seofon
proto: *sébun
protoform: *sébun
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2174 seven / seofon

## Current row state

- The live OE row currently reads `CONCEPT = seven`, `COUNTERPART = seofon`, `PROTO = *sébun`, `PROTOFORM = *sébun`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:945-948].
- `PROTO` and `PROTOFORM` are identical in the live TSV. This row is therefore not using a surrogate OE-facing stem, a different paradigm cell, or an analogical repair input; the same `*sébun` serves both as the comparative proto label and as the derivational input that the current OE cascade consumes [Germanic/data/germanic-aligned-final.tsv:947-947].
- `oe_known_problems.tsv` currently has no row-specific entry for row `2174`, for `seven`, for `seofon`, or for `*sébun`; the live known-problems file only lists unrelated exception buckets [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace is an exact match and shows the row's active pathway explicitly: `PROTO: *sébun`, `EXPECTED: seofon`, `OUTPUTS: seofon`, with the OE-side stages `OE Med Unstressed U Lowering: *sébon`, `PGmc B Allophony: *séβon`, `OE Back Mutation: *séoβon`, and surface `Outcome: seofon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3955-3973].
- No row-specific packet or research memo was found during slice preparation, so the YAML link fields are intentionally left blank and this slice stands as the replacement working note for the row.

## Development-note summary

Row 2174 is now a regular exact-match derivation, not a stem-selection controversy. The live TSV keeps `PROTO = PROTOFORM = *sébun`, and the published trace already derives exact `seofon` from that form with no extra repair layer [Germanic/data/germanic-aligned-final.tsv:947-947; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3955-3973]. The surviving DEV_NOTES material that matters is therefore the shared phonology that explicitly uses `seven` as evidence: medial unstressed `*u > *o` and West-Saxon back mutation `*e > *eo` before a single intervening labial or liquid plus a following back vowel [@Campbell1959, §331 fn. 3; @Campbell1959, §373; @RingeTaylor2014, p. 324; @HoggPhonology1992, §6.3] [Germanic/docs/DEV_NOTES.md:223-315,637-675,33842-33848].

The first half of the row's explanation is the weak-syllable vowel. DEV_NOTES quotes Campbell §331 fn. 3 that “in Prim. OE `*sefun` existed beside `*sifuni (§ 293)`,” then immediately spells out the consequence: the uninflected form `*sefun` has medial `*u` before no following high vowel and yields `seofon`, whereas inflected `*sifuni` preserves the high vowel before following `*i` [@Campbell1959, §331 fn. 3] [Germanic/docs/DEV_NOTES.md:240-245]. The same note then quotes Ringe-Taylor's dialect summary, “PGmc `*sebun` 'seven' ... > WS, North. OE `seofon`, Merc. `seofen`,” and explains Mercian `seofen` through a separate weak-vowel development [@RingeTaylor2014, p. 324; @Campbell1959, §385] [Germanic/docs/DEV_NOTES.md:247-260]. For row 2174 that distinction matters: the live OE target is specifically WS/Northumbrian `seofon`, not Mercian `seofen`, and nothing in current DEV_NOTES suggests changing the row's target or its proto input [Germanic/data/germanic-aligned-final.tsv:947-947].

DEV_NOTES later restates the same point in more operational form under Campbell §373. There the note defines the rule as “Unstressed medial `*u -> *o` in West Saxon and Northumbrian, but NOT after an accented `*u` in the preceding syllable,” and it lists `*sebun -> seofon` as a positive example precisely because the stressed vowel is `*e`, not `*u` [@Campbell1959, §373] [Germanic/docs/DEV_NOTES.md:637-645]. That is exactly the first OE step shown in the live trace, `*sébun -> *sébon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3961-3968]. The row-level consequence is simple but important to preserve: `PROTO` and `PROTOFORM` stay `*sébun`; the OE target differs from the proto input because ordinary OE phonology changes the unstressed medial vowel, not because the row needs a substitute stem.

The second half of the derivation is the diphthong. DEV_NOTES quotes Hogg's statement that in West Saxon “back mutation was even more restricted, for it occurred only if there was a single intervening consonant which was either a labial or a liquid,” and one of Hogg's own examples there is `*sifon > siofon 'seven'` [@HoggPhonology1992, §6.3] [Germanic/docs/DEV_NOTES.md:33842-33846]. This is directly applicable to row 2174: once medial `*u` has lowered to `o`, the environment for WS back mutation is present, and the live trace shows that explicitly as `*séβon -> *séoβon -> seofon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3967-3973]. The row should therefore be documented as a regular OE success with two chronological stages—`*u > *o`, then `*e > *eo`—rather than as a leftover numeral exception.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-223-315

- Source heading: `OE Medial unstressed *u → *o: Conditioning environment (2026-03-20)`
- Source line or section hint: `lines 223-315`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `medial_unstressed_u`; `dialect_split`; `sefun_vs_sifuni`; `protoform_vs_target`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2068`

This is the strongest current DEV_NOTES fragment for row 2174 because it preserves the actual evidence chain rather than just the rule label. DEV_NOTES quotes Campbell §331 fn. 3: “in Prim. OE `*sefun` existed beside `*sifuni (§ 293)`,” and then explains that uninflected `*sefun` yields `seofon` whereas inflected `*sifuni` preserves the high vowel before following `*i` [@Campbell1959, §331 fn. 3] [Germanic/docs/DEV_NOTES.md:240-245]. The same fragment also quotes Ringe-Taylor's explicit dialect statement, “PGmc `*sebun` 'seven' ... > WS, North. OE `seofon`, Merc. `seofen`,” and uses Campbell §385 to explain Mercian `e` as a different weak-vowel outcome [@RingeTaylor2014, p. 324; @Campbell1959, §385] [Germanic/docs/DEV_NOTES.md:247-260].

What this establishes for row 2174 is concrete. First, it shows why the live counterpart is the WS/Northumbrian form `seofon`, not Mercian `seofen` [Germanic/data/germanic-aligned-final.tsv:947-947]. Second, it shows that the row does **not** need a revised `PROTOFORM`: the live `*sébun` is acceptable because the decisive work is being done by OE medial-vowel history, not by substituting a different lexical stem [Germanic/data/germanic-aligned-final.tsv:947-947; Germanic/docs/DEV_NOTES.md:240-260].

### DEV_NOTES:line-637-675

- Source heading: `OE Medial Unstressed *u → *o (Campbell §373)`
- Source line or section hint: `lines 637-675`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `campbell_373`; `medial_u_lowering`; `conditioning`; `shared_row_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2068`

This later restatement is valuable because it turns the earlier comparative discussion into an explicit conditioning statement. DEV_NOTES defines the change as “Unstressed medial `*u → *o` in West Saxon and Northumbrian, but NOT after an accented `*u` in the preceding syllable,” and it lists `*sebun → seofon` among the examples where the change applies because the accented vowel is `*e`, not `*u` [@Campbell1959, §373] [Germanic/docs/DEV_NOTES.md:637-645]. It then contrasts blocked forms such as `sunu` and `wudu`, preserving Campbell's own formulation that “u is always well preserved after accented u” [@Campbell1959, §373] [Germanic/docs/DEV_NOTES.md:647-675].

For row 2174, this fragment establishes the exact conditioning behind the trace's first OE step `*sébun -> *sébon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3961-3968]. It is therefore the best short-form citation when later review wants to explain why `seofon` is regular without replaying the full widow-related investigation that originally surfaced the rule.

### DEV_NOTES:line-33842-33848

- Source heading: `§17.21.10.1 The environmental specifications for back mutation (velar umlaut) in the OE dialects`
- Source line or section hint: `lines 33842-33848`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `back_mutation`; `west_saxon`; `labial_conditioning`; `eo_outcome`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2068`

This fragment supplies the best current DEV_NOTES authority for the second half of the row's derivation. DEV_NOTES quotes Hogg directly: “In West Saxon back mutation was even more restricted, for it occurred only if there was a single intervening consonant which was either a labial or a liquid,” and immediately gives `*sifon > siofon 'seven'` as one of Hogg's model examples [@HoggPhonology1992, §6.3] [Germanic/docs/DEV_NOTES.md:33842-33846]. That is exactly the environment row 2174 needs once medial `*u` has lowered to `o`: front `e`, one intervening labial (`f` / `β`), then a back vowel.

For the row, the fragment does more than provide general background. It explains the trace stage `*séβon -> *séoβon`, which is the immediate precursor of surface `seofon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3967-3973]. It also keeps the chronology explicit: `*u > *o` supplies the back-vowel trigger, and then WS back mutation supplies `eo` [Germanic/docs/DEV_NOTES.md:637-645,33842-33846].

## Superseded or diagnostic material

The main diagnostic material worth preserving is the January 2026 mismatch history. DEV_NOTES records a “HIGH PRIORITY: PGmc final `*-un` behavior” note in which `*sebun` was still producing model output `sobun`, expected `seofon`, alongside the parallel failures `*texun -> teoun` and `*newun -> nēowun` [Germanic/docs/DEV_NOTES.md:2647-2662]. The note attributes this to `OldEnglishWeakTailReduction` not touching `*u`, so `*-un` never received the weak-tail treatment it needed [Germanic/docs/DEV_NOTES.md:2656-2662]. That material remains useful as project history because it explains why `seven` once appeared inside a broader numeral-tail bug cluster, but it is no longer current row authority now that the published derivation trace shows exact `seofon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3955-3973].

An even earlier sanity-check note from 2026-01-26 says the same thing in more implementation-facing language: `*u` in weak tails such as `*tehun, *sebun, *newun` “stays `{*u}` at `EnglishAfterProtoToOEWeakTail`,” so a newly added `{*u}->{*o}` line was inert and a dedicated `*-un -> -on` rule might be necessary [Germanic/docs/DEV_NOTES.md:1735-1739]. Later writers should use this only to explain why the row once misfired as `sobun`; it should not be cited as evidence that row 2174 is still an open exception bucket item.

## Open questions for later work

- If a later final lexeme report wants fuller dialect coverage, decide whether to include a compact contrast note `WS/North. seofon` versus `Merc. seofen`; the live row only needs the former, but DEV_NOTES preserves both outcomes and their different weak-vowel explanations [@RingeTaylor2014, p. 324; @Campbell1959, §385] [Germanic/docs/DEV_NOTES.md:247-260].
- If later review wants a shorter row summary for central indexing, the strongest securely attachable current anchors are the medial-`u` dossier (`223-315`), the Campbell §373 rule restatement (`637-675`), and the Hogg back-mutation quotation (`33842-33848`); the `sobun` mismatch note (`2647-2662`) should be indexed only as diagnostic project history.
- If a packet or memo is created later, keep the derivational chronology explicit rather than collapsing everything into “back mutation”: live `*sébun` first gives `*sébon` by medial unstressed `u > o`, then `*séoβon` by WS back mutation, then surface `seofon` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3961-3973].
