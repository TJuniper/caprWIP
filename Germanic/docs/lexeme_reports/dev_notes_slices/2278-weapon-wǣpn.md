---
row_id: 2278
concept: weapon
counterpart: wǣpn
proto: *wḗpną
protoform: *wḗpną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2278-weapon-wǣpn.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2278-weapon-wǣpn.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2278 weapon / wǣpn

## Current row state

- CONCEPT: `weapon`
- COUNTERPART: `wǣpn`
- PROTO: `*wḗpną`
- PROTOFORM: `*wḗpną`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Proto: oblique *wēpnăn→*wēpną (n. a-stem nom.sg.; Kroonen)` [Germanic/data/germanic-aligned-final.tsv:1351].
- Existing row support files: packet and research memo both exist and are worth linking, but the memo is the safer guide to current row policy because it explicitly warns that the packet foregrounds the shared cluster background more than the later resolved-policy lines in `DEV_NOTES` [Germanic/docs/lexeme_reports/packets/2278-weapon-wǣpn.md:15-20,58-186; Germanic/docs/lexeme_reports/research_memos/2278-weapon-wǣpn.md:15-20,58-95].
- `oe_known_problems.tsv`: no row-specific `2278` problem entry was found during the required check; this fits the memo's conclusion that the row is already a settled editorial-choice case, not an open derivational defect [Germanic/docs/lexeme_reports/research_memos/2278-weapon-wǣpn.md:24-34].
- No row-specific pilot file or dedicated weapon dossier was found under the obvious lexeme-report support directories. The only nearby dossier hit is the general medial-`u` conditioning dossier, which explicitly says `tācn, wǣpn, bēacn` are "not diagnostic" for that question and therefore is not a row-specific support file [Germanic/docs/dossier-medial-u-lowering-conditioning-2026.md:343-345].

## Development-note summary

The surviving DEV_NOTES material for row 2278 is substantial, but it is mostly **shared cluster-note material** rather than a weapon-only memorandum. That matters for later use: the row is well documented, but its authority comes from the shared `-Cl/-Cn/-Cm#` note in `DEV_NOTES §17.18`, plus the live TSV row, not from a stand-alone lexeme essay. Any future report should therefore cite the exact line anchors instead of vaguely referring to a larger section [Germanic/docs/DEV_NOTES.md:29853-30083].

The phonological core is the same one that governs `tācn` and the exceptional `þistles` discussion, and row 2278 has to keep that overlap explicit. DEV_NOTES states that OE inherited stem-final obstruent-plus-sonorant clusters such as `*wǣpn-`, and that in the neuter/masculine NomSg/AccSg these clusters fall word-finally, where late OE often develops a parasite vowel: `*þistel, wǣpen, tācen, hræfen, seġel*` [Germanic/docs/DEV_NOTES.md:29855-29860; @Campbell1959, §363; @HoggPhonology1992, §§6.30-6.36]. The same note immediately contrasts the oblique paradigm, where the cluster is medial and therefore remains unbroken: `gen.sg. *þistles, tācnes, wǣpnes, hræfnes, fugles, wuldres*` [Germanic/docs/DEV_NOTES.md:29863-29868]. Campbell's textbook trio is quoted there in exactly the form needed for this row: `NomSg wǣpen / GenSg wǣpnes` alongside the analogous `tācen / tācnes` and `hræfen / hræfnes` [Germanic/docs/DEV_NOTES.md:29866-29868; @Campbell1959, §363].

The live row nonetheless remains `regular` and keeps **unbroken** `COUNTERPART = wǣpn`, because the project is not targeting the late-West-Saxon dictionary norm here. DEV_NOTES' own audit of the current TSV/FST state lists row 11 as `*wēpną | wǣpn | wǣpn | ✓` and immediately glosses that the current FST does no generalized parasiting for `-Cl/Cn/Cm#`, while the TSV is correspondingly unbroken across the class except for `þistel` [Germanic/docs/DEV_NOTES.md:29887-29904]. So for this row the present derivation is not a broken implementation waiting to be repaired; it is a current match between the selected dataset target and the selected no-parasiting register [Germanic/docs/lexeme_reports/packets/2278-weapon-wǣpn.md:17-42].

The philological complication is not derivability but **lemma choice and register**. DEV_NOTES' attestation table says `wǣpn` is attested unbroken, but mainly in compounds and poetic simplex, whereas broken `wǣpen` is the standard simplex and the BT/DOE lemma [Germanic/docs/DEV_NOTES.md:29909-29921,29933-29935]. DEV_NOTES then adds the caution that the broken nominative is the late-WS prose norm across almost the whole class, while choosing the unbroken form is only a defensible editorial decision if the project wants an older / poetic / Anglian orientation [Germanic/docs/DEV_NOTES.md:29937-29941]. This is exactly the row's present status. The row should therefore not be described as if `wǣpn` were the universally normal OE lemma; it is an attested but marked selection against the more normalized `wǣpen` headword [Germanic/docs/lexeme_reports/research_memos/2278-weapon-wǣpn.md:46-69].

The local reference material supports that same split rather than collapsing it. Bright's reader paradigms normalize the neuter as `wapen` in the nominative/accusative singular and `wæpnes` in the genitive singular, then states that `"The middle vowel is generally syncopated after a long radical syllable (heafdes, wæpnes)"` [docs/references/bright_anglo_saxon_reader.vision.txt:941-948,967-969]. Clark Hall likewise lemmatizes the simplex under broken `wapen n. (nap. wap(e)n, wap(e)nu) 'weapon'` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46702-46703]. But the same reference base also preserves unbroken `wæpn` inside compounds and derivative spellings, such as `hildewæpn-` in the project summary and `ungewæpnod` in Clark Hall, which is consistent with DEV_NOTES' statement that unbroken `wǣpn` survives mainly in compounds and poetic/simplex marginal use [Germanic/docs/DEV_NOTES.md:29933-29935; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:45012-45012].

The decisive project authority is the later policy ruling in `§17.18.7`, not the earlier option-building material. DEV_NOTES preserves the user instruction: `"If unbroken versions are attested in Beowulf/poetic and early/Anglian, let's stick with them. Move ONLY thistle to another paradigm cell which is lautgesetzlich and attested."` [Germanic/docs/DEV_NOTES.md:30071-30073]. It then names `wǣpn` among the ten rows retained unchanged and says the present FST behavior is `correct for these ten lemmas` because the dataset has chosen the early / poetic / Anglian register [Germanic/docs/DEV_NOTES.md:30075-30083]. That is the controlling row policy. Unlike `þistles`, row 2278 is **not** a paradigm-cell workaround, and unlike the broken normalized simplex `wǣpen`, it is **not** trying to reproduce later prose headword practice.

The `PROTO` / `PROTOFORM` / `COUNTERPART` distinction still has to be stated explicitly even though the first two columns coincide. `PROTO = *wḗpną` is the comparative/project proto label for the cognate set. `PROTOFORM = *wḗpną` is the actual derivational input that this row feeds into the OE cascade. `COUNTERPART = wǣpn` is the selected OE output. The live row note's `oblique *wēpnăn→*wēpną` is source-side etymological background, not evidence that the row itself has shifted to an oblique paradigm cell [Germanic/data/germanic-aligned-final.tsv:1351]. Kroonen's entry in fact emphasizes stem alternation at the proto level, giving `*wēbna- ~ *wēpna- n. 'weapon'` and observing that the word shows `two different stems` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29229-29246]. Orel likewise cites the simplex under `*wēpnan sb.n.: Goth wepn 'weapon', ON vápn id., OE wapen id.` [docs/references/orel_handbook_germanic_etymology.vision.txt:50794-50796]. Those source shapes explain why the note mentions oblique background, but they do **not** override the live row's nominative-style `PROTOFORM` or its selected unbroken `COUNTERPART`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-29853-29880

- Source heading: `§17.18.1  The lautgesetzlich background (Campbell §§360–363; Hogg §§6.30–6.36; SB §§145–146)`
- Fragment type: `shared_phonology_with_weapon_examples`
- Status: `current`
- Issue tags: `parasite_vowel`; `word_final_cluster`; `wǣpn_wǣpen_wǣpnes`; `register_variation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2250; 2260; 2278`

This is the main shared phonological anchor for the row. It is explicit that the relevant class includes `*wǣpn-`, that the word-final nominative/accusative singular is the environment where parasite-vowel spellings like `wǣpen` arise, and that the oblique forms remain unbroken because the cluster is medial there [Germanic/docs/DEV_NOTES.md:29855-29868]. It also supplies the register chronology that later notes must keep visible rather than flattening away: `Late WS prose` regularizes the broken forms, while `Beowulf and other poetry` preserve unbroken `wǣpn`, and Anglian shows the rule less strongly [Germanic/docs/DEV_NOTES.md:29870-29879; @Campbell1959, §363]. For row 2278 this fragment matters because it explains both the broken dictionary lemma `wǣpen` and the dataset's continued ability to defend unbroken `wǣpn`.

### DEV_NOTES:line-29881-29904

- Source heading: `§17.18.2  Current TSV state (11 candidate words)`
- Fragment type: `dataset_state_audit`
- Status: `current`
- Issue tags: `current_row_match`; `fst_behavior`; `unbroken_target`
- Recommended next use: `cite_for_row_state`
- Shared with row IDs: `2250; 2260; 2278`

This fragment is the strongest compact statement of the row's actual computational state. It records row 11 as `*wēpną | wǣpn | wǣpn | ✓` and states that the FST currently does no generalized parasiting for this cluster class [Germanic/docs/DEV_NOTES.md:29887-29904]. That makes the live row easy to misread if later documentation only consults dictionaries: from the perspective of the existing pipeline, `wǣpn` is not an unresolved mismatch but the exact form presently derived and intentionally stored. The slice should therefore preserve this audit fragment whenever it needs to explain why `DERIVATION_CLASS = regular` is still defensible.

### DEV_NOTES:line-29905-29946

- Source heading: `§17.18.3  Attestation findings (per agent research, sources cited at end)`
- Fragment type: `attestation_and_lemma_choice`
- Status: `current`
- Issue tags: `poetic_simplex`; `compound_survival`; `bt_doe_headword`; `oblique_control`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2260; 2278`

This is the fragment that keeps the row honest philologically. The table says `wǣpn` is attested, but only marginally as simplex and especially in compounds/poetic usage, while `wǣpen` is the BT/DOE lemma and the standard simplex [Germanic/docs/DEV_NOTES.md:29920-29921,29933-29935]. The surrounding warning is equally important: the broken nominative is the late-WS prose norm, whereas choosing the unbroken form is only a defensible editorial choice that reflects older / poetic / Anglian usage [Germanic/docs/DEV_NOTES.md:29937-29941]. For row 2278 this fragment is stronger than a generic attestation note because it directly names the exact conflict among row target, normalized lemma, and oblique control form `wǣpnes` [Germanic/docs/DEV_NOTES.md:29943-29946; @Campbell1959, §363].

### DEV_NOTES:line-30062-30083

- Source heading: `§17.18.7  Decision and implementation plan` / `§17.18.7.1  Resolved policy`
- Fragment type: `resolved_row_policy`
- Status: `current`
- Issue tags: `retain_wǣpn`; `thistle_exception_only`; `early_poetic_register`; `indexable_anchor`
- Recommended next use: `primary_index_anchor`
- Shared with row IDs: `2250; 2260; 2278`

This is the controlling current authority for row 2278. It preserves the user ruling in direct quotation and then explicitly includes `wǣpn` among the ten rows retained unchanged [Germanic/docs/DEV_NOTES.md:30071-30083]. The importance of this fragment is that it resolves the ambiguity left by the earlier options: `wǣpn` is not being kept because the project forgot about `wǣpen`, and it is not being moved to `wǣpnes` as a paradigm-cell repair. It is being kept because the dataset deliberately selected the attested early / poetic / Anglian register for this lexeme class.

## Superseded or diagnostic material

The option-building material in `§17.18.4-§17.18.5` should be preserved, but not treated as current row policy. Those lines still matter for project history because they show that the team seriously considered either (a) relemmatizing the whole class to broken nominatives such as `wǣpen` or (b) moving the whole class to oblique targets such as `wǣpnes` [Germanic/docs/DEV_NOTES.md:29959-30032]. Both proposals are now superseded for row 2278 by `§17.18.7`, which kept `wǣpn` unchanged.

One detail in that option block is especially diagnostic rather than authoritative for this row. `Option 1` says the same philological objection applies to `*wǣpn` as to unattested `*þistl` [Germanic/docs/DEV_NOTES.md:29952-29957]. That wording should not be quoted as the row's current evidence state without qualification, because the immediately preceding attestation table and the later resolved-policy section both treat unbroken `wǣpn` as **attested**, though marginal and non-dominant [Germanic/docs/DEV_NOTES.md:29921,29933-29935,30075-30083]. The safest reading is that the option note was using starred `*wǣpn` loosely while building alternatives, and that it has been overtaken by the more precise later account.

The packet's compact header is likewise partly diagnostic rather than sufficient. It initially says `DEV_NOTES hits: None` in the high-confidence section, then later preserves the actual shared `DEV_NOTES` lines under supporting/background evidence [Germanic/docs/lexeme_reports/packets/2278-weapon-wǣpn.md:15-20,48-130]. That is not wrong so much as incomplete: the packet is useful for source gathering, but the slice should follow the memo in treating `§17.18.7` as the necessary corrective layer for current row policy [Germanic/docs/lexeme_reports/research_memos/2278-weapon-wǣpn.md:15-20,62-69].

## Open questions for later work

- If the live TSV note is ever revised, it should probably keep the existing Kroonen-style proto background but add one sentence stating the actual row policy: the dataset intentionally targets attested unbroken `wǣpn`, while BT/DOE and late West Saxon prose normally prefer `wǣpen`, and `wǣpnes` is the regular unbroken oblique comparator [Germanic/data/germanic-aligned-final.tsv:1351; Germanic/docs/DEV_NOTES.md:29933-29946,30071-30083].
- If `index.tsv` is updated later, the strongest current anchors are the attestation/policy pair `DEV_NOTES:line-29905-29946` and `DEV_NOTES:line-30062-30083`. The earlier shared phonology block `DEV_NOTES:line-29853-29880` is also useful, but it is more background than row-specific authority.
- No paradigm probe is required for the present row state. Unlike `þistles`, row 2278 is not presently a paradigm-cell solution; the relevant comparison set is explanatory only: unbroken selected `wǣpn`, broken normalized simplex `wǣpen`, and oblique `wǣpnes` [Germanic/docs/lexeme_reports/research_memos/2278-weapon-wǣpn.md:71-81].
