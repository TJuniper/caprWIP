---
row_id: 2260
concept: token
counterpart: tācn
proto: *táikną
protoform: *táikną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2260-token-tācn.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2260-token-tācn.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2260 token / tācn

## Current row state

- CONCEPT: `token`
- COUNTERPART: `tācn`
- PROTO: `*táikną`
- PROTOFORM: `*táikną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Proto: oblique *taiknăn→*taikną (n. a-stem nom.sg.; Kroonen)` [Germanic/data/germanic-aligned-final.tsv:1280-1280].
- Packet and memo status: both existing row-level support files agree that the live row itself is not broken, but the memo correctly warns that the packet under-represents the later DEV_NOTES resolution because it foregrounds §17.18.1-§17.18.3 more than §17.18.7 [Germanic/docs/lexeme_reports/packets/2260-token-tācn.md:15-60,66-128; Germanic/docs/lexeme_reports/research_memos/2260-token-tācn.md:15-20,62-88].
- `oe_known_problems.tsv` has no row-specific entry for `*táikną` / `tācn`, which matches the memo's assessment that this is a resolved philological-policy row rather than a currently open OE exception [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/research_memos/2260-token-tācn.md:24-37,80-89].
- No row-specific pilot, dossier, or analysis file was found under the obvious lexeme-report support directories beyond the packet and research memo.

## Development-note summary

For row 2260, the surviving DEV_NOTES material is substantial and should be treated as the controlling row policy, even though most of it lives in a shared cluster dossier rather than in a token-only note. Section 17.18 was written for the whole OE `-Cl/-Cr/-Cn/-Cm` word-final cluster problem, but `tācn` is not just an incidental string hit there: the lexeme is explicitly named in the phonological background, in the current TSV audit, in the attestation table, in the bibliography guidance, and in the final decision section [Germanic/docs/DEV_NOTES.md:29855-29880,29887-29904,29909-29946,30036-30039,30062-30083].

The central point of §17.18.1 is that the row sits inside a real OE variation class, not a one-off spelling accident. DEV_NOTES states that stem-final obstruent-plus-sonorant clusters can develop a parasite vowel in late OE, with front-vowel outcomes such as `*þistel, wǣpen, tācen, hræfen, seġel*`, while the oblique cells remain unbroken: `*þistles, tācnes, wǣpnes, hræfnes, fugles, wuldres*` [Germanic/docs/DEV_NOTES.md:29855-29868]. It also preserves the chronology/register warning that matters most for this row: “**Beowulf and other poetry**: unbroken forms (*hræfn, wǣpn, tācn*) preserved metri causa,” while late West Saxon prose regularizes the broken forms more strongly [Germanic/docs/DEV_NOTES.md:29870-29879]. That aligns with the handbook pattern usually cited for this class [@Campbell1959, §363; @HoggPhonology1992, §§6.30-6.36; @Brunner1965, §§152, 155, 160].

Section 17.18.2 then shows that the live row is internally consistent with the present FST and the present dataset policy. The TSV audit lists row 10 explicitly as `*táikną | tācn | tācn | ✓`, and DEV_NOTES immediately glosses that the system currently does **no** generalized parasiting for `-Cl/Cn/Cm#` while the TSV is correspondingly unbroken across this class except for `þistel` [Germanic/docs/DEV_NOTES.md:29881-29904]. For row 2260 this matters because it means the project did not arrive at `tācn` by accident: the unbroken target is both what the FST outputs and what the shared note recognized as the intended dataset state before the class-level policy decision was finalized.

Section 17.18.3 adds the philological nuance that later work must keep visible instead of flattening into a single dictionary-style lemma. The attestation table says `tācn` is attested unbroken (`Beowulf 141`), but `tācen` is also strongly attested and is the dominant late-WS prose spelling; meanwhile the oblique form `tācnes` remains the regular unbroken control [Germanic/docs/DEV_NOTES.md:29909-29946]. DEV_NOTES is explicit that “**The broken NomSg is the late-WS prose norm**” for almost the whole class, but also that choosing the unbroken form is a “defensible editorial choice reflecting older / poetic / Anglian usage” [Germanic/docs/DEV_NOTES.md:29937-29946]. That is the exact caution row 2260 needs: `tācn` is not the only attested OE citation form, but it is an attested one, and the dataset is deliberately selecting that register.

The decisive row authority is no longer §17.18.4-§17.18.5, which were option-building notes, but §17.18.7. There DEV_NOTES records the user ruling: “**If unbroken versions are attested in Beowulf/poetic and early/Anglian, let's stick with them. Move ONLY thistle to another paradigm cell which is lautgesetzlich and attested.**” It then names `tācn` among the ten rows retained unchanged and says the current no-parasiting behavior is “correct for these ten lemmas,” because the dataset has chosen the early / poetic / Anglian register for them [Germanic/docs/DEV_NOTES.md:30069-30083]. For row 2260, this is stronger than a general phonology note: it is the explicit project decision that `COUNTERPART = tācn` stays put and is not to be silently updated to `tācen` or shifted to oblique `tācnes`.

The distinction among `PROTO`, `PROTOFORM`, and `COUNTERPART` should still be spelled out carefully even though the live row currently uses the same string in the first two fields. `PROTO` is the row's comparative/project proto label; `PROTOFORM` is the actual derivational input fed to the OE cascade; `COUNTERPART` is the attested OE target selected for the row. Here `PROTO = PROTOFORM = *táikną` in the TSV because no row-specific analogical rewrite is currently required [Germanic/data/germanic-aligned-final.tsv:1280-1280]. But source-level headwords are not identical to that normalized project shape: Kroonen gives `*taikna- n. 'sign' ... OE täcn n. 'id.'`, Orel lists `*taiknan`, and Ringe-Taylor cite `PGmc *taikna 'sign' > PWGmc *taikn` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25907-25913; docs/references/orel_handbook_germanic_etymology.vision.txt:44219-44228; docs/references/ringe_taylor_linguistic_history_vol2.txt:3479-3484]. The row note's “oblique *taiknăn→*taikną” is therefore a source-side morphological reminder about the project input form, not an argument that the OE target should be oblique.

Local reference texts reinforce the same picture of controlled variation rather than a single obligatory output. Clark Hall normalizes the lemma as `tācen` and explicitly cross-references `tacon, tăcun = tācen`, so dictionary lookup alone will tend to point away from the dataset's chosen unbroken form [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:39850-39880]. Brunner, however, gives both the parasited and unparasited side of the paradigm, including `tācen - tācnes` and the explicit reminder that “doch kommen auch Formen mit silbischem n wie ws. bēacn, tācn, wolcn vor” [docs/references/brunner_1965_altenglische_grammatik.vision.txt:6875-6885,10172-10175]. Bülbring likewise preserves late-WS variation rather than a single mandatory form: “Alfred und das Spät-Ws. beacen, tācn tācen ...” [docs/references/bulbring_altenglisches_elementarbuch.txt:8314-8317]. Those source snapshots support the DEV_NOTES decision to retain `tācn` as an attested unbroken target while remaining explicit that `tācen` is a major competing written form [@ClarkHall1960; @Brunner1965, §§155, 160; @Bulbring1902, §445].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-29853-29880

- Source heading: `§17.18.1  The lautgesetzlich background (Campbell §§360–363; Hogg §§6.30–6.36; SB §§145–146)`
- Source line or section hint: `lines 29853-29880`
- Fragment type: `shared_phonology_with_row_specific_examples`
- Status: `current`
- Issue tags: `parasite_vowel`; `word_final_cluster`; `tācn_tācen_tācnes`; `register_variation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment establishes the problem space that row 2260 belongs to. It explicitly names `*tācn-` in the inherited cluster class, gives `tācen` as the broken NomSg-type outcome after a front vowel, gives `tācnes` among the unbroken oblique forms, and then marks unbroken `tācn` as the kind of form preserved in “Beowulf and other poetry” [Germanic/docs/DEV_NOTES.md:29855-29879]. That combination is exactly what later row-level notes need: not merely “OE sometimes has epenthesis,” but the concrete lexical contrast `tācn ~ tācen / tācnes` that explains why the row can be philologically defensible without representing the prose-majority spelling. Compare [@Campbell1959, §363; @HoggPhonology1992, §§6.30-6.36].

### DEV_NOTES:line-29881-29904

- Source heading: `§17.18.2  Current TSV state (11 candidate words)`
- Source line or section hint: `lines 29881-29904`
- Fragment type: `dataset_state_audit`
- Status: `current`
- Issue tags: `current_row_match`; `fst_behavior`; `unbroken_targets`
- Recommended next use: `cite_for_row_state`
- Shared with row IDs:

This is the strongest compact anchor for the row's live computational state. It lists `# 10 | *táikną | tācn | tācn | ✓` and immediately explains that the FST currently does no generalized parasiting for `-Cl/Cn/Cm#`, with the TSV correspondingly targeting unbroken forms across the class [Germanic/docs/DEV_NOTES.md:29887-29904]. For row 2260, this fragment is especially useful because it ties the lexical decision to the actual implementation state: the current FST output and the current TSV target already coincide, so later documentation should not describe the row as awaiting a technical fix.

### DEV_NOTES:line-29905-29946

- Source heading: `§17.18.3  Attestation findings (per agent research, sources cited at end)`
- Source line or section hint: `lines 29905-29946`
- Fragment type: `attestation_and_editorial_choice`
- Status: `current`
- Issue tags: `beowulf_attestation`; `late_ws_competitor`; `doe_lemma`; `oblique_control`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment supplies the philological calibration that the bare TSV row lacks. It records `tācn` as attested unbroken, `tācen` as strongly attested and prose-dominant, and `tācnes` as part of the uniformly unbroken oblique pattern [Germanic/docs/DEV_NOTES.md:29909-29946]. Its most important sentence for row 2260 is the explicit warning that unbroken selection is a “defensible editorial choice” but “not the prose-corpus majority spelling” [Germanic/docs/DEV_NOTES.md:29937-29941]. That is strong enough to preserve in any future lexeme report and strong enough to prevent overstated claims that `tācn` is simply the only or default OE form.

### DEV_NOTES:line-30062-30083

- Source heading: `§17.18.7  Decision and implementation plan` / `§17.18.7.1  Resolved policy`
- Source line or section hint: `lines 30062-30083`
- Fragment type: `resolved_row_policy`
- Status: `current`
- Issue tags: `final_project_decision`; `retain_tācn`; `no_parasiting_policy`; `indexable_anchor`
- Recommended next use: `primary_index_anchor`
- Shared with row IDs:

This is the fragment that settles the row. It quotes the user instruction to keep unbroken forms when they are attested in Beowulf/poetic and early/Anglian usage, then explicitly includes `tācn` among the ten rows retained unchanged [Germanic/docs/DEV_NOTES.md:30069-30083]. The section goes further than merely allowing `tācn`: it says the present FST behavior is “correct for these ten lemmas” because the dataset has chosen the early / poetic / Anglian register [Germanic/docs/DEV_NOTES.md:30075-30083]. For row 2260, this is the best single DEV_NOTES anchor for any future indexing or summary work.

### DEV_NOTES:line-30015-30032

- Source heading: `§17.18.5  Recommendation`
- Source line or section hint: `lines 30015-30032`
- Fragment type: `superseded_project_recommendation`
- Status: `superseded`
- Issue tags: `paradigm_cell_option`; `tācnes_option`; `historical_project_state`
- Recommended next use: `preserve_as_history_only`
- Shared with row IDs:

This fragment recommended the paradigm-cell strategy before the final user ruling was recorded. It argued that targeting oblique forms would be the cleanest way to avoid the parasiting question and would keep forms like `tācnes` in the alignment layer [Germanic/docs/DEV_NOTES.md:30015-30032]. For row 2260, it remains worth preserving only as project history: it explains why packet-only reading may leave the false impression that `tācnes` is still an active proposal, but §17.18.7 supersedes it as current policy.

## Superseded or diagnostic material

- The superseded material for this row is not an obsolete derivation trace but the earlier class-level recommendation that would have moved the whole cluster set to oblique forms such as `tācnes`. That recommendation was explicit in §17.18.5, but §17.18.7 later overrode it for row 2260 by retaining attested unbroken `tācn` [Germanic/docs/DEV_NOTES.md:30015-30032,30062-30083].
- Packet-only reading is somewhat diagnostic rather than sufficient, because the packet preserves the shared background and attestation material but can be read as if the `tācn ~ tācen / tācnes` issue were still open. The memo is right to treat §17.18.7 as the necessary corrective layer [Germanic/docs/lexeme_reports/packets/2260-token-tācn.md:48-128; Germanic/docs/lexeme_reports/research_memos/2260-token-tācn.md:17-20,64-88].
- Dictionary normalization toward `tācen` should also be treated as diagnostic rather than decisive for the row. Clark Hall's headword practice is real evidence about lexicographic convention, but it does not override the project's documented choice to target the attested unbroken register-form `tācn` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:39850-39880; Germanic/docs/DEV_NOTES.md:30069-30083].

## Open questions for later work

- If the live TSV note is ever revised, consider adding one short sentence that makes the register choice explicit, not just the proto-side morphology: the current note explains `*taiknăn→*taikną`, but not that the row deliberately retains attested unbroken `tācn` rather than the common broken competitor `tācen` [Germanic/data/germanic-aligned-final.tsv:1280-1280; Germanic/docs/DEV_NOTES.md:29937-29941,30069-30083].
- If a later final lexeme report wants source-facing precision on the proto label, it should cite the exact Kroonen and Orel headword shapes (`*taikna-`, `*taiknan`) while still explaining why the project's derivational `PROTOFORM` is normalized as `*táikną` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25907-25913; docs/references/orel_handbook_germanic_etymology.vision.txt:44219-44228].
- For index decisions, the strongest DEV_NOTES anchors are the resolved-policy lines 30069-30083 and the attestation table line 29920 with its surrounding warning at 29937-29941. Those are strong enough to support an index entry if the index is intended to capture explicit retained-unbroken policy rather than only defect rows.
