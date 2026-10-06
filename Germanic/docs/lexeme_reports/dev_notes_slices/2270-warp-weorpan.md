---
row_id: 2270
concept: warp
counterpart: weorpan
proto: *wérpaną
protoform: *wérpaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2270-warp-weorpan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md
linked_dossier_or_analysis_files: [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md, Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md]
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2270 warp / weorpan

## Current row state

- CONCEPT: `warp`; COUNTERPART: `weorpan`; PROTO: `*wérpaną`; PROTOFORM: `*wérpaną`; DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1318-1318].
- The live TSV note is already doing row-separation work, but its arrow is only heuristic: `OE target: wearp→weorpan (inf. of str.v. class III; noun/past 'wearp' in *warpą row)` [Germanic/data/germanic-aligned-final.tsv:1318-1318]. This should not be read as saying that row 2270 derives from row 2269's form.
- The neighboring row 2269 remains distinct and must stay distinct: `2269 ... counterpart wearp ... PROTO *wárpą`, whereas row 2270 is the infinitive/citation-form row `*wérpaną > weorpan` [Germanic/data/germanic-aligned-final.tsv:1316-1318].
- `PROTO` and `PROTOFORM` coincide here, but they still need to be kept conceptually separate from `COUNTERPART`. In this row, both proto columns name the comparative verbal input `*wérpaną`; `COUNTERPART` names the Old English output selected for the row, namely infinitive `weorpan`, not noun/preterite `wearp` [Germanic/data/germanic-aligned-final.tsv:1318-1318; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:53-67].
- Existing row-specific support files already exist and agree on the main point: the packet preserves the live trace `*wérpaną -> weorpan`, and the memo treats the real problem as lexeme overlap with row 2269 rather than any unresolved sound-law failure [Germanic/docs/lexeme_reports/packets/2270-warp-weorpan.md:17-41; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:13-21,87-99].
- Coverage infrastructure marks row 2270 as one of the note-bearing rows requiring report treatment, but no pilot/final lexeme report was located; the packet and memo are therefore the only row-local support files to inherit directly [Germanic/docs/lexeme_reports/coverage_audit.md:160-160; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:46-51].

## Development-note summary

The surviving DEV_NOTES support for row 2270 is real but thin, shared, and easy to overread. The packet explicitly reports no direct authoritative DEV_NOTES hit for the row, and only preserves supporting/background material: one cluster where `weorpan` is used as a canonical example of OE breaking before `r + C`, and one much earlier note where late West Saxon `weorpan -> wurpan` is listed among `w`-conditioned later developments [Germanic/docs/lexeme_reports/packets/2270-warp-weorpan.md:48-94]. That means this slice should not pretend that DEV_NOTES contains a dedicated row-2270 dossier. It does not. What exists is enough to justify the row conservatively, but not enough to turn it into a high-confidence indexed exception narrative.

The main durable point is that row 2270 is the **verbal infinitive** row. Both the packet and the memo insist that the English gloss `warp` is lexically misleading here, because Old English `wearp` can denote both the noun `'warp,' threads stretched lengthwise in a loom` and the 3sg preterite of `weorpan`, while the dataset's intended target for row 2270 is the citation infinitive `weorpan` [Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:71-85; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47433-47435,47874-47879]. Clark Hall is especially useful because it keeps the split explicit: `wearp` is listed as both noun and preterite, while `weorpan` is the strong verb headword; Bright likewise gives the paradigm `weorpan, wearp, wurpon, worpen`, which is exactly the distinction this row needs to preserve [docs/references/bright_anglo_saxon_reader.txt:2506-2507,26825-26826].

That philological split matches the comparative reconstruction. The row's `PROTO` and `PROTOFORM` are both `*wérpaną`, i.e. the verbal infinitive/citation-form input. The related short-form ablaut row 2269 instead uses `*wárpą`, which corresponds to the `wearp` side of the paradigm [Germanic/data/germanic-aligned-final.tsv:1316-1318; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:55-67]. Ringe-Taylor's sound-history examples support exactly this separation: they derive `PGmc *warp 'threw' > OE wearp`, but separately `PGmc *werpana 'to throw' > OE weorpan` [@RingeTaylor2014, pp. 180-182; docs/references/ringe_taylor_linguistic_history_vol2.txt:10451-10555,10568-10574]. For row 2270, that is the decisive distinction among row levels: the proto verbal headword and the row-level protoform coincide as `*wérpaną`, while the OE counterpart is the infinitive `weorpan`; row 2269 handles the different ablaut grade and different paradigm cell.

DEV_NOTES then matters chiefly because it explains why `weorpan` is the expected OE verbal outcome. The strongest shared anchor is the later breaking discussion: DEV_NOTES, quoting Hogg and Campbell, treats `weorpan` as a canonical example of front-vowel breaking before `r + C` and states that breaking applies before heterosyllabic `/r/ + C`, with `*weorpan 'throw'` among the standard examples [Germanic/docs/DEV_NOTES.md:33889-33899; @HoggPhonology1992, §5.85ff.; @Campbell1959, §§128-141]. Campbell's handbook text aligns with that generalization by listing `weorpan throw` among the regular breaking examples and then separately noting Northumbrian `worpa`-type retraction forms [@Campbell1959, §§146-147; docs/references/campbell_old_english_grammar.txt:4530-4541]. So the row's regular status is not a special repair: the live derivation `*wérpaną -> weorpan` is exactly the sort of breaking outcome the project's own DEV_NOTES treats as canonical [Germanic/docs/lexeme_reports/packets/2270-warp-weorpan.md:17-41].

The late-West-Saxon and dialectal material must be kept, but only with labels attached. DEV_NOTES also preserves the separate note `weo → wo → wu (§§265-268): late WS weorpan → wurpan, sweord → swurd` [Germanic/docs/DEV_NOTES.md:216-219]. Campbell likewise notes W-S spellings such as `wurpan throw` and related `wur-` forms [@Campbell1959, §321; docs/references/campbell_old_english_grammar.txt:8987-9000], and Hogg observes that in classical Old English `weorpan` normally further developed to `wurpan` [docs/references/hogg_vol1.txt:7391-7394]. But those facts are **background about later or dialectal OE**, not reasons to retarget row 2270 away from normalized `weorpan`. The packet and memo are correct to keep `wurpan` as later-stage background only [Germanic/docs/lexeme_reports/packets/2270-warp-weorpan.md:58-70; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:25-36,80-85].

Two diagnostic hazards also need to stay visible. First, the analysis file on Northumbrian/Anglian variation cites `uarp warp` from the Franks Casket/Bewcastle context, but that evidence belongs with `wearp`-type past/root-vowel forms, not with the citation infinitive of row 2270 [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:751-751; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:28-35]. Second, the final-vowel apocope investigation's `*warpą → wearpa (exp. wearp)` is about the short-form row, again not the infinitive row [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:298-298]. Both are worth preserving precisely because they show how easily row 2269 and row 2270 can be collapsed if the paradigm distinction is left implicit.

The practical conclusion is conservative. Row 2270 looks stable and regular as currently encoded, and the live derivation plus handbook/dictionary evidence are enough to maintain `weorpan` confidently. But the DEV_NOTES support remains shared phenomenon material rather than row-specific policy text. The file should therefore preserve the row split, preserve the direct quotations that justify `weorpan` as the canonical breaking example, and explicitly warn that the note's `wearp→weorpan` arrow is mnemonic rather than a literal derivational claim [Germanic/data/germanic-aligned-final.tsv:1318-1318; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:116-126].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-33889-33899

- Source heading: `§17.21.10.2  Does breaking apply across /st/ + r?`
- Source line or section hint: `lines 33889-33899`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `breaking`; `heterosyllabic_rC`; `canonical_example`; `counterpart_identity`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2269; 2270`

This is the strongest DEV_NOTES anchor available for row 2270 because it names `weorpan` directly and does so in a way that still matches the live row. DEV_NOTES first summarizes Hogg: `"The canonical examples are: *feoh 'cattle', *eo 'horse', *weorpan 'throw', *weorčan 'work', *eald 'old', *feoll 'fell'. Breaking applies before /h/, /x/, /r/ + C, /l/ + C."` It then sharpens the point with Campbell: `"Breaking applies before /r/ + C when the /r/ is heterosyllabic ... Examples: *weorčan 'work', *weorpan 'throw', *earm 'arm', *sweostor 'sister'"` [Germanic/docs/DEV_NOTES.md:33889-33899]. For row 2270, this fragment is not a custom row note, but it is still the best current project-language support for keeping `*wérpaną > weorpan` as a regular breaking outcome [@HoggPhonology1992, §5.85ff.; @Campbell1959, §§128-141].

### DEV_NOTES:line-216-219

- Source heading: `Related: effects of initial labials on vowels (Bülbring §§260-274)`
- Source line or section hint: `lines 216-219`
- Fragment type: `shared_dialect_background`
- Status: `background_only`
- Issue tags: `late_west_saxon`; `weo_to_wu`; `not_row_target`
- Recommended next use: `mention_only_as_background`
- Shared with row IDs: `2269; 2270`

This short fragment is worth preserving because it is the clearest in-repo explanation for later `wurpan`-type forms, but it must stay explicitly subordinate to the live row target. DEV_NOTES says: `weo → wo → wu (§§265-268): late WS weorpan → wurpan, sweord → swurd` [Germanic/docs/DEV_NOTES.md:216-219]. That matches Campbell's and Hogg's later-stage remarks on `wurpan`, yet the packet correctly classifies the material as supporting/background rather than direct row authority [Germanic/docs/lexeme_reports/packets/2270-warp-weorpan.md:58-70]. For row 2270 the fragment should only explain why later or dialectal `wurpan` exists; it should not be used to displace normalized `COUNTERPART = weorpan`.

## Superseded or diagnostic material

- The most persistent diagnostic trap is the live TSV note's arrow `wearp→weorpan`. It is useful as a reminder that the English gloss `warp` reaches into the `wearp` side of the paradigm, but it is potentially misleading if read literally. The row's actual proto input is already verbal `*wérpaną`, not a repaired `wearp`-based surrogate [Germanic/data/germanic-aligned-final.tsv:1318-1318; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:120-125].
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:751` is diagnostic background only for this row. Its `uarp warp` evidence belongs to Northumbrian past/root-vowel discussion and is relevant chiefly because it helps explain why row 2269 and row 2270 are easy to confuse [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:751-751; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:28-35,43-45].
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:298` is likewise diagnostic-only here. The form `*warpą → wearpa (exp. wearp)` concerns the short-form `wearp` row, not the infinitive/citation-form row `*wérpaną -> weorpan` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:298-298; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:44-46].
- No superseded row-specific DEV_NOTES implementation note was located for row 2270. The row's risk is not stale rule history but stale lexeme interpretation: over-weighting `wearp`, `wurpan`, or `warp/uarp` evidence until the infinitive `weorpan` disappears from view.

## Open questions for later work

- If the live TSV note is ever rewritten, replace the mnemonic `wearp→weorpan` wording with a direct statement that row 2270 targets attested OE infinitive `weorpan`, while related noun/preterite `wearp` belongs to row 2269 / `*wárpą` [Germanic/data/germanic-aligned-final.tsv:1316-1318; Germanic/docs/lexeme_reports/research_memos/2270-warp-weorpan.md:120-125].
- If a later final lexeme report is prepared, the most useful compact paradigm reminder would be exactly the one Bright and Campbell preserve: infinitive `weorpan`, preterite singular `wearp`, preterite plural `wurpon`, past participle `worpen` [docs/references/bright_anglo_saxon_reader.txt:2506-2507,26825-26826; docs/references/campbell_old_english_grammar.txt:20857-20863].
- For indexing decisions, treat the DEV_NOTES anchors as genuine but shared. `line-33889-33899` is the only strong current anchor, and even it is a general breaking discussion rather than a row-specific instruction; `line-216-219` is weaker still because it is later-stage dialect background rather than target-setting authority.
