---
row_id: 2085
concept: knee
counterpart: cnēow
proto: '*knéwą'
protoform: '*knéwą'
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/analysis/notable_findings.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: superseded_by_model_entry
needs_literature_agent: yes
---

# DEV_NOTES material — 2085 knee / cnēow

This slice preserves the pre-SC033 nominative state. Its references
to the "current" row and successful long-output trace below are historical,
not descriptions of the adopted dative *knéwai → cneowe. The current
scientific account and detailed paradigm comparison are owned by
`model_entries/2085-knee-cneowe.model.md` and
`sound_changes/audits/sc033-adjudication.md`; the older evidence is
retained here without retroactively changing its observations.

## Current row state

- The live OE row is `2085`, with `CONCEPT = knee`, `COUNTERPART = cnēow`, `PROTO = *knéwą`, `PROTOFORM = *knéwą`, and `DERIVATION_CLASS = regular`. `PROTO` and `PROTOFORM` are identical in the current TSV; the attested/target OE form is `cnēow`, not the shorter comparative shape `cnēo` that appears in one shared DEV_NOTES example [Germanic/data/germanic-aligned-final.tsv:601-601].
- The row has no surviving row-local packet, memo, or manifest entry. Coverage still reads `| 2085 | knee | cnēow | regular | no | - | - | - | none |`, and `report_manifest.tsv` still contains only pilot/report rows unrelated to `2085` [Germanic/docs/lexeme_reports/coverage_audit.md:285-285; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- `oe_known_problems.tsv` does not list `*knéwą`, `cnēow`, or row `2085`, so current repo policy is that this row is not parked as an OE exception item [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation snapshot is an exact match and gives the only row-specific stage path now in repo documentation: `PROTO: *knéwą`, `EXPECTED: cnēow`, `OUTPUTS: cnēow`, with `OE Ew Long Diphthong: *knēową` followed by `OE Heavy Syllable Nasal Apocope: *knēow` and surface `Outcome: cnēow` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2599-2618].

## Development-note summary

No row-specific DEV_NOTES block for `knee / cnēow` survives. The only live DEV_NOTES material that names the lexeme is a shared rule note under `PWGmcIjContraction`, where `knee` appears only as a parallel comparator beside `friend` and `few`, not as the subject of its own row dossier [Germanic/docs/DEV_NOTES.md:1385-1410]. This slice therefore has to be built conservatively from (i) that shared-background-only DEV_NOTES fragment, (ii) the current row metadata, and (iii) the current derivation trace.

The key distinction to preserve is that the live row stores `PROTO = PROTOFORM = *knéwą` and targets attested OE `cnēow`, whereas DEV_NOTES' shared example gives an internal comparative sequence `*knewu → *kneu → OE cnēo ('knee')` [Germanic/data/germanic-aligned-final.tsv:601-601; Germanic/docs/DEV_NOTES.md:1395-1397]. That DEV_NOTES sequence is useful evidence for a historical `*Vwu → *Vu` reduction/compression, but it is not itself the row's stored metadata and it does not by itself settle the final OE `-w` seen in `cnēow`. The row-specific closing step now comes from the published trace, which keeps final `w` after `OE Heavy Syllable Nasal Apocope` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2612-2618].

The other point that must remain explicit is evidentiary thinness. DEV_NOTES does not present `knee` as a settled standalone sound-law case; instead it preserves Ringe–Taylor's caution around the neighboring `friend` change and then asks, as an open expert question, whether the `knee/few` pattern is “the same mechanism” [Germanic/docs/DEV_NOTES.md:1387-1391,1401-1410]. So the row is operationally current and regular in the live cascade, but its surviving DEV_NOTES support is shared-background-only plus an unresolved comparative question, not a bespoke lexeme memorandum.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1372-1383

- Source heading: `### 1. PWGmcSyllabicJ: *ja/*ją → *i (after light syllable, word-finally)`
- Source line hint: `lines 1372-1383`
- Fragment type: `shared_background_boundary_note`
- Status: `current_but_not_row_specific`
- Issue tags: `adjacent_w_material`; `light_syllable_only`; `do_not_overapply`
- Recommended next use: `cite_only_to_mark_the_boundary_of_what_DEV_NOTES_is_and_is_not_claiming_for_row_2085`
- Shared-with rows if relevant: `1946; 1943; 2138`

This adjacent fragment matters mainly as a warning against overreading. DEV_NOTES quotes Ringe–Taylor: “Upon the loss of unstressed `*a` and `*ą`, preceding postconsonantal `*j` and `*w` became syllabic `*i` and `*u` respectively,” but the project immediately narrows the conditioning to “After a light syllable (short vowel + single consonant), word-finally,” and the examples are `*bazją → *bazi → berġes`, `*harjaz → *hari → here`, and `*natją → *nati → net` [Germanic/docs/DEV_NOTES.md:1374-1383]. For row `2085`, this is shared-background-only boundary evidence, not direct support: the note does mention postconsonantal `*w`, but it does not identify `knee`, does not use the row's `*knéwą` input, and does not present a heavy-syllable `*ēo(w)` outcome.

### DEV_NOTES:line-1385-1399

- Source heading: `### 2. PWGmcIjContraction: *ijō → *iu (before consonant)`
- Source line hint: `lines 1385-1399`
- Fragment type: `shared_background_only`
- Status: `current_but_shared`
- Issue tags: `parallel_vwu_to_vu`; `knee_example`; `not_row_local`; `comparative_preforms`
- Recommended next use: `primary_DEV_NOTES_citation_for_the_surviving_knee_material`
- Shared-with rows if relevant: `2033`

This is the only surviving DEV_NOTES fragment that names `knee`, but it does so only as a parallel example inside a note whose main topic is `friend`. DEV_NOTES first quotes Ringe–Taylor on `friend`: “A roughly similar change of `*ijo` to `*iu` appears to have occurred in the word 'friend' in PWGmc,” while also preserving the caveat that “the uniqueness of the sequence `*ijo` (with stressed `*i`) makes it inadvisable to attempt any generalizations based on the history of this word” [Germanic/docs/DEV_NOTES.md:1387-1391]. It then adds the row-relevant comparator: “R/T also mentions a parallel `*Vwu → *Vu` change (§3.1.5): `*knewu → *kneu → OE cnēo ('knee')`; `*fawu → *fau → OE fēa ('few')`” [Germanic/docs/DEV_NOTES.md:1395-1397].

For row `2085`, the substance is real but limited. The fragment preserves the project's only live DEV_NOTES acknowledgment that the `knee` etymon belongs with a semivowel-loss/contraction pattern of the shape `*Vwu → *Vu`. But it is shared-background-only because the quoted sequence uses comparative preforms `*knewu` and `*kneu`, not the row's stored `PROTO/PROTOFORM = *knéwą`, and because the endpoint quoted in DEV_NOTES is `cnēo`, not the current row target `cnēow` [Germanic/data/germanic-aligned-final.tsv:601-601; Germanic/docs/DEV_NOTES.md:1395-1397]. The fragment should therefore be used for mechanism/history, not as a replacement for the row's actual metadata or present trace.

### DEV_NOTES:line-1401-1410

- Source heading: `### Relationship between the two` / `### Questions for experts`
- Source line hint: `lines 1401-1410`
- Fragment type: `shared_open_question`
- Status: `current_open_issue`
- Issue tags: `unresolved_mechanism`; `knee_vs_friend`; `literature_gap`
- Recommended next use: `preserve_as_reason_for_literature_follow_up`
- Shared-with rows if relevant: `2033`

This fragment is crucial because it states the surviving uncertainty explicitly instead of letting later notes flatten it into a settled rule. DEV_NOTES says the `friend` and `knee/few` developments “cannot plausibly be reduced to a single phonological rule,” then asks: “Is the parallel `*Vwu → *Vu` change (knee, few) the same mechanism?” [Germanic/docs/DEV_NOTES.md:1401-1410]. For row `2085`, that means the project preserved `knee` not as a closed lexeme-local solution in DEV_NOTES, but as an example attached to an unresolved comparative-mechanism question. That is why this slice marks the DEV_NOTES support as thin/shared even though the live derivation now succeeds.

## Superseded or diagnostic material

- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` preserves an older failure signature: `*knewą → cnēowa (exp. cnēow)` inside the `Proto *-ą cases` list [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:275-289]. This is diagnostic only. It records that the row once belonged to the extra-final-vowel problem set, but it is superseded by the current published trace, which now reaches `cnēow` directly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2599-2618].
- The sandbox JSON files under `Germanic/tmp/` are also diagnostic/stale rather than authoritative for current row state. One current tmp dump still shows unaccented `*knewą` with `outputs: []`, and the staged dump for the same unaccented form still ends at surface `cnowa` with `first_failing_stage: ProtoRhoticFronting` [Germanic/tmp/old_english_sandbox_results_current.json:1475-1480; Germanic/tmp/old_english_sandbox_results_with_stages.json:21995-22134]. Those files illuminate older or alternate instrumentation, but they should not override the live TSV plus published trace for row `2085`.
- `analysis/notable_findings.md` restates the same shared comparison and modelling dilemma — `*knewu → *kneu → OE cnēo ('knee')`, `*fawu → *fau → OE fēa ('few')`, and the warning that the `friend` and `knee/few` developments “cannot plausibly be reduced to a single phonological rule” [Germanic/docs/analysis/notable_findings.md:506-523]. Useful, but still diagnostic/shared-background rather than row-specific DEV_NOTES authority.
- The published derivation trace is row-specific and current, but it is not a DEV_NOTES fragment. Its role in this slice is to supply the row's present successful implementation path where DEV_NOTES itself preserves only shared mechanism notes [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2599-2618].

## Open questions for later work

- If a literature pass is commissioned, answer the exact DEV_NOTES question rather than replacing it with vague prose: is the `knee/few` `*Vwu → *Vu` pattern really the same mechanism as `friend`'s `*ijō → *iu`, or only an analogy/parallel noticed in the handbooks? [Germanic/docs/DEV_NOTES.md:1407-1410].
- If a later report quotes the DEV_NOTES comparator chain, keep the three layers separate: live row metadata `*knéwą`, DEV_NOTES comparative preforms `*knewu`/`*kneu`, and the attested OE target `cnēow`. Do not silently normalize the row to `cnēo` just because that is the form written in the shared DEV_NOTES example [Germanic/data/germanic-aligned-final.tsv:601-601; Germanic/docs/DEV_NOTES.md:1395-1397].
- If sandbox artefacts are reused in later documentation, regenerate them or label them clearly as stale instrumentation. As currently checked into the repo, the tmp JSON files still contradict the published trace for this row [Germanic/tmp/old_english_sandbox_results_current.json:1475-1480; Germanic/tmp/old_english_sandbox_results_with_stages.json:21995-22134; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2599-2618].
