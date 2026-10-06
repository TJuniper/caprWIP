---
row_id: 2250
concept: thistle
counterpart: þistles
proto: *θéstilaz
protoform: *θístilas
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2250-thistle-þistles.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2250-thistle-þistles.md
linked_dossier_or_analysis_files:
  - Germanic/docs/lexeme_reports/pilot/thistle.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2250 thistle / þistles

## Current row state

- CONCEPT: `thistle`
- COUNTERPART: `þistles`
- PROTO: `*θéstilaz`
- PROTOFORM: `*θístilas`
- DERIVATION_CLASS: `late_analogy`
- Live TSV note: `Paradigm-cell target: GenSg þistles (masc. a-stem). NomSg simplex *þistl is unattested in OE manuscripts; the only attested simplex NomSg is broken þistel (via late-WS svarabhakti, Campbell §§360–363, Hogg §§6.30–6.36), which is not modeled in this FST since the other ten -Cl/Cn/Cm# rows (bōsm, botm, hæsl, nǣdl, ofn, hræfn, scofl, stefn, tācn, wǣpn) deliberately target unbroken Beowulf-poetic / early / Anglian forms. GenSg þistles is fully attested as the inflectional stem and lautgesetzlich (medial cluster, no parasiting; Campbell §363 textbook trio). See DEV_NOTES §17.18.` [Germanic/data/germanic-aligned-final.tsv:1241]
- Live TSV history field: `Source: Wiktionary etymology (template:inh) | Proto corrected: Kluge-Seebold *þistila- with root *i; Orel gives underlying *þe(x)stilaz but all daughter languages show *i (see notable_findings §8)` [Germanic/data/germanic-aligned-final.tsv:1241]
- `oe_known_problems.tsv`: no row `2250` entry was found during the required check.
- Reused filename stem: `2250-thistle-þistles`, matching the existing packet and research memo.

## Detailed development-note summary

The live row is explicitly a **paradigm-cell row**, not a simplex headword row. `PROTO` `*θéstilaz` functions as the cognate-set / etymological headword, while `PROTOFORM` `*θístilas` is the row-specific **gen.sg.** input actually fed to the OE derivation, and `COUNTERPART` `þistles` is the corresponding attested OE **gen.sg.** output. That distinction matters because the current row is not trying to derive the dictionary simplex `þistel`, and it is equally not endorsing unattested simplex `*þistl` as the target. The selected target is the attested inflectional cell where the cluster is medial and the derivation is regular [@Campbell1959, §363; @HoggPhonology1992, §§6.30–6.36; Germanic/data/germanic-aligned-final.tsv:1241; Germanic/docs/lexeme_reports/research_memos/2250-thistle-þistles.md:42-49].

The core DEV_NOTES argument is phonological and philological at once. In the word-final nominative/accusative singular of masc./neut. a-stems, OE commonly develops a parasite vowel in obstruent + sonorant clusters, yielding broken forms such as `þistel`, `tācen`, and `wǣpen`; but in oblique cells the same cluster is medial, so parasiting does not apply and forms such as `þistles`, `tācnes`, and `wǣpnes` remain unbroken [@Campbell1959, §363; @HoggPhonology1992, §6.36; Germanic/docs/DEV_NOTES.md:29855-29868]. DEV_NOTES explicitly uses Campbell's textbook trio as the model for the row and stresses that the oblique stem is the cross-dialectally stable locus of the unbroken cluster [Germanic/docs/DEV_NOTES.md:29863-29868, 29943-29946].

The row-specific problem was therefore narrow. The project had already chosen an unbroken Beowulf-poetic / early / Anglian-looking policy for the other ten `-Cl/-Cn/-Cm#` rows, so adding a general late-WS parasiting rule just to make `þistel` derive would have damaged those already-correct targets [Germanic/docs/DEV_NOTES.md:29901-29903, 30075-30083]. At the same time, DEV_NOTES found that unbroken simplex `*þistl` is not attested in OE manuscripts as a simplex nominative at all; it survives only as an inflectional stem and in compounds, while the only attested simplex nominative is broken `þistel` [Germanic/docs/DEV_NOTES.md:29925-29931]. The project decision was therefore to keep the other ten rows unchanged and move only thistle to an attested, lautgesetzlich oblique cell.

DEV_NOTES preserves the governing project ruling in direct speech: `If unbroken versions are attested in Beowulf/poetic and early/Anglian, let's stick with them. Move ONLY thistle to another paradigm cell which is lautgesetzlich and attested.` [Germanic/docs/DEV_NOTES.md:30071-30073]. The resulting row policy is likewise explicit: target the genitive singular `þistles`, because here the cluster is medial, parasiting does not apply, and the form is directly attested [@Campbell1959, §363; @HoggPhonology1992, §6.36; Germanic/docs/DEV_NOTES.md:30094-30098]. The slice should therefore state the contrast plainly: unattested and unmodeled simplex `*þistl`; attested but unmodeled late-WS simplex `þistel`; attested and modeled row target `þistles`.

The older March 2026 thistle note remains useful only for the **etymological** side of the row. That note argued over whether the inherited Germanic form should be represented with root `*e` or `*i`, citing Orel's `*þe(x)stilaz` against Kluge-Seebold's `*þistila-`, and preserving Campbell's formulation that `e > i before i` is "carried out with practically perfect regularity in all the Germanic languages" [@Orel2003, p. 419; @KlugeSeebold2011; @Campbell1959, §112; Germanic/docs/DEV_NOTES.md:12244-12280]. That material still explains why the live TSV keeps `PROTO` and `PROTOFORM` separate: the cognate-set headword may remain `*θéstilaz`, but the row-level derivational input is the selected gen.sg. `*θístilas`, and the current row no longer depends on deriving simplex `þistel` from a nominative citation form [Germanic/docs/DEV_NOTES.md:12304-12322; Germanic/docs/lexeme_reports/research_memos/2250-thistle-þistles.md:44-50].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-29853-29947

- Source heading: `Word-final obstruent + sonorant clusters: lautgesetzlich background and attestation findings`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `parasiting`; `cluster_nouns`; `attestation`; `paradigm_cell`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2053; 2183; 2246; 2250`

This is the main current background fragment. DEV_NOTES says that in NomSg/AccSg the cluster is word-final and late OE develops a parasite vowel, but in oblique cells the cluster is medial and "parasiting does not apply: gen.sg. *þistles, tācnes, wǣpnes, hræfnes, fugles, wuldres*" [Germanic/docs/DEV_NOTES.md:29857-29868]. The same block then records the decisive attestation contrast: `*þistl is NOT attested as a simplex NomSg spelling in any OE MS`, whereas broken `þistel` is the standard simplex form and the GenSg / oblique stem is uniformly unbroken across the whole class [Germanic/docs/DEV_NOTES.md:29925-29931, 29943-29946]. For row 2250 this fragment supplies both the phonological premise and the manuscript-attestation premise behind the gen.sg. target [@Campbell1959, §363; @HoggPhonology1992, §6.36].

### DEV_NOTES:line-30067-30116

- Source heading: `Resolved policy and row-2250 implementation`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_policy`; `single_row_exception`; `protoform_vs_proto`; `genitive_singular`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2250`

This is the strongest current row-specific authority. DEV_NOTES preserves the user ruling to keep the other ten rows in their unbroken poetic / early / Anglian orientation and to "Move ONLY thistle to another paradigm cell which is lautgesetzlich and attested" [Germanic/docs/DEV_NOTES.md:30071-30073]. It then states the solution in row-specific terms: the single exception is thistle, the unbroken simplex `*þistl` is unattested, broken `þistel` would require a parasiting rule the project has chosen not to model, and therefore the row should target gen.sg. `þistles` instead [Germanic/docs/DEV_NOTES.md:30085-30098]. This fragment is current even though one implementation bullet later preserves a stale `PROTO` spelling; the row-policy statement itself matches the live TSV and should anchor the slice.

### DEV_NOTES:line-12181-12340

- Source heading: `March 2026 thistle note on i-umlaut and etymological reconstruction`
- Fragment type: `lexeme_specific`
- Status: `diagnostic_only`
- Issue tags: `etymology`; `umlaut`; `proto_dispute`; `superseded_target`
- Recommended next use: `background_only`
- Shared with row IDs: `2250`

This older fragment is not current row authority for the **target cell**, but it remains useful background on the `PROTO` / `PROTOFORM` split. It preserves Orel's `*þe(x)stilaz`, Kluge-Seebold's `*þistila-`, the daughter-language `i` evidence, and Campbell's quotation `e > i before i ... carried out with practically perfect regularity in all the Germanic languages` [Germanic/docs/DEV_NOTES.md:12244-12280]. It also records the earlier project move to change a nominative-style protoform to `*θistilaz` in order to derive simplex `þistel` [Germanic/docs/DEV_NOTES.md:12313-12322]. That specific nominative targeting is now superseded for row 2250, but the etymological discussion still helps explain why the live row keeps etymological `PROTO` `*θéstilaz` separate from derivational `PROTOFORM` `*θístilas` [@Orel2003, p. 419; @KlugeSeebold2011; @Campbell1959, §112].

## Superseded or diagnostic material

The superseded row state is the older nominative-style pairing `*θístilaz -> þistel`. DEV_NOTES opened §17.18 with exactly that mismatch and initially treated thistle as the lone outlier among eleven cluster nouns [Germanic/docs/DEV_NOTES.md:29848-29850, 29887-29890]. That remains useful chronology, but it is no longer the live row. The current row is the paradigm-cell pair `*θístilas -> þistles`.

The March 2026 note should also be handled as superseded **row policy** even where its etymological observations remain helpful. Its verification block and update sentence were written for a world where the project still wanted simplex `þistel` as the row target [Germanic/docs/DEV_NOTES.md:12313-12322]. After the later §17.18 decision, that is no longer the governing task. The live row now targets the attested gen.sg. because the project chose not to generalize a late-WS parasiting rule across the whole `-Cl/-Cn/-Cm#` class [Germanic/docs/DEV_NOTES.md:30075-30098].

One DEV_NOTES implementation detail is stale and should be treated as diagnostic only inside this slice. Line 30115 says `PROTO: retain *θístilaz (etymological cognate root)`, but the live TSV row now has `PROTO` `*θéstilaz` and reserves `*θístilas` for `PROTOFORM` [Germanic/docs/DEV_NOTES.md:30113-30116; Germanic/data/germanic-aligned-final.tsv:1241]. For current work the TSV is the authority. The slice should therefore preserve that DEV_NOTES line as project history while explicitly marking the `PROTO` spelling there as superseded or mistaken relative to the live row.

## Open questions for later work

- If `index.tsv` is updated later, decide whether to index both the shared current fragment `DEV_NOTES:line-29853-29947` and the row-specific current fragment `DEV_NOTES:line-30067-30116`, while keeping `DEV_NOTES:line-12181-12340` as diagnostic-only background rather than primary authority.
- If DEV_NOTES itself is revised in a future pass, line 30115 should be reconciled with the live TSV so that `PROTO` `*θéstilaz` and `PROTOFORM` `*θístilas` are no longer blurred.
- If a later final report wants fuller philological support, add direct dictionary citations for attested `þistles` and for the broken simplex `þistel`; the packet and memo already summarize the distinction, but the slice presently relies on DEV_NOTES plus the live TSV note for that contrast.
