---
row_id: 1983
concept: cud
counterpart: cwedu
proto: *kwíθuz
protoform: *kwéðuz
derivation_class: attested_variant
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1983-cud-cwedu.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1983-cud-cwedu.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1983 cud / cwedu

## Current row state

- CONCEPT: `cud`
- COUNTERPART: `cwedu`
- PROTO: `*kwíθuz` in the live TSV row, but this is now stale against both the row note and the controlling DEV_NOTES correction at `DEV_NOTES:line-28401-28519`.
- PROTOFORM: `*kwéðuz`
- DERIVATION_CLASS: `attested_variant`
- Live TSV note (abridged): the row note already encodes the current argument that Kroonen's citation form `*kweduz` and Orel's explicit `*kweðuz` point to an e-grade, voiced-dental proto; that Sanskrit `jatú` supports PIE `*gʷet-u-` with original `*t`; that ON `kváða` preserves PGmc `*ð`; and that OE attests a variant set `cwedu`, `cwidu`, `cweodu`, `cwudu`, `cudu`, with `*kwéðuz` now the intended row-level derivational input.
- `oe_known_problems.tsv`: no row-level entry.
- `report_manifest.tsv`: row 1983 is present as `pilot/cud.md`, status `pilot`.
- Working caution: this row is not an unattested reconstruction problem. The live target `cwedu` is an attested OE form chosen from a larger variant set, while the row's remaining defect is that the `PROTO` column still preserves the older, now-rejected reconstruction.

## Development-note summary

The controlling late note redefines the row as a reconstruction error plus variant-selection problem, not as a mysterious OE sound-law failure. Its starting mismatch is explicit: row 1983 had `*kwíθuz` producing `cwiþu` against target `cwedu`, and both divergences are diagnostic of the input being wrong — stem `i` where the comparative evidence points to `e`, and medial `þ` where the cognate set points to voiced `ð`/`d` [DEV_NOTES:line-28401-28519]. The source survey there is the current authority: PIE `*gʷet-u-` is supported by Sanskrit `jatú`, whose `-t-` argues for PIE plain voiceless `*t`; Verner voicing in the mobile-accent u-stem paradigm yields PGmc `*kweðuz`; Kroonen cites the lemma as `*kweduz` with Leiden `d` for intervocalic `[ð]`; Orel gives explicit `*kweðuz`; and Ringe-Taylor's PWGmc `*kwidu` presupposes exactly such a PGmc e-grade predecessor [DEV_NOTES:line-28423-28438; @Kroonen2013, p. 313; @Orel2003; @RingeTaylor2014, p. 323; @Pokorny1959].

That same late note is also the place where the OE variant system is finally laid out clearly enough for row work. `cwedu` is not a convenient reconstruction invented for the FST. It is the conservative e-grade nom.sg. outcome inherited from PGmc `*kweðuz` after NWGmc loss of final `*z` and the row's regular hardening `ð > d`; `cwidu` is the paradigm-levelled i-grade form generalized from oblique cells; `cweodu` is Anglian/Kentish back-umlaut; `cwudu` is the later West-Saxon rounded form after `/w/`; and `cudu` is the de-labialized form after `kw > k` before `/u/` [DEV_NOTES:line-28451-28485; @RingeTaylor2014, p. 323; @Campbell1959, §318; @Campbell1959, §465; @HoggPhonology1992, §§5.103ff., 5.170--5.172, 7.80]. For this row the crucial distinction is therefore three-way: the etymological cognate-set headword should be PGmc `*kwéduz` / Kroonen-style `*kweduz`; the row-specific phonological input is `*kwéðuz`; and the OE target is attested `cwedu`, one real member of the wider lexical set.

The implementation note then makes the current project policy straightforward. The transducer already hardens `*ð > *d`; it does not presently model the later branch-specific processes needed for `cweodu`, `cwudu`, or `cudu`; and when fed `*kwéðuz` it returns `cwedu` directly [DEV_NOTES:line-28487-28505]. That is why the row remains `attested_variant`: the project is intentionally targeting the conservative attested form that the existing FST can derive without extra dialect-specific machinery, not claiming that the more familiar spellings are wrong. This also means that the lingering live-TSV `PROTO` value `*kwíθuz` should be read as metadata lag, not as evidence against the corrected derivation.

The earlier March note is still worth keeping, but only with its project chronology labelled. It was already right to reject `*kwiθuz`, and it preserves direct quotations that later report writers may still want. Kroonen's entry is quoted there as "`*kwedu- 2 m. 'resin' — OE cwidu, cweodu, c(w)udu ...`"; Ringe-Taylor are quoted as "`The OE neuter cwidu, c(w)udu, gen. cwidwes 'gum, cud' could also have been a u-stem originally`"; Campbell is quoted on `-cudu` versus Epinal `-quidu`; and Hall is quoted for "`cwudu (o, i)`" [DEV_NOTES:line-6009-6085; @Kroonen2013, p. 313; @RingeTaylor2014, p. 42; @Campbell1959, §218]. But that note still belongs to an earlier row state: it frames `cudu` as the expected form, treats the row update as a `COUNTERPART` change to `cwedu`, and does not yet cleanly separate cognate-set `PROTO` from row-level `PROTOFORM`. It remains useful as a quotation cache and source audit, not as the final row policy.

One later diagnostic note should now be treated explicitly as obsolete framing. In the April `i > e` audit, the row appeared as `*kwiθuz → cwidu/cwedu/cudu`, with the question whether coronal `*θ` should have forced lowering to `*e` and whether `cwidu` therefore reflected analogy [DEV_NOTES:line-17436-17480]. That problem was real only under the obsolete input. Once the row is reset to `*kwéðuz`, the apparent `i`-lowering puzzle dissolves: `cwedu` is the direct conservative outcome, while `cwidu` is the levelled variant that needs no separate rescue rule.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6009-6085

Source heading: early cud note correcting `*kwiθuz` and surveying OE variants  
Source line or section hint: lines 6009-6085  
Status: background  
Issue tags: reconstruction_disagreement;OE_variation;u_stem;source_audit  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This early note remains valuable because it preserves the source quotations behind the later correction. Kroonen is quoted directly: "`*kwedu- 2 m. 'resin' — OE cwidu, cweodu, c(w)udu ...`", which already rules out the old row's `*kwiθuz` and shows that the lexeme belongs to a real attested variant set [@Kroonen2013, p. 313]. Ringe-Taylor are also quoted directly: "`The OE neuter cwidu, c(w)udu, gen. cwidwes 'gum, cud' could also have been a u-stem originally`", preserving the useful u-stem and oblique-form evidence [@RingeTaylor2014, p. 42]. Campbell's note on `-cudu` versus Epinal `-quidu`, and Hall's dictionary summary "`cwudu (o, i)`", are likewise worth carrying forward because they document the later `cwudu/cudu` side of the paradigm [@Campbell1959, §218]. What is no longer current inside this fragment is the project framing: it still treats `cudu` as the expected form and does not yet distinguish cleanly between corrected cognate-set reconstruction and row-specific FST input.

### DEV_NOTES:line-17436-17480

Source heading: diagnostic `i`-lowering question built on old `*kwiθuz` input  
Source line or section hint: lines 17436-17480  
Status: diagnostic_only  
Issue tags: i_lowering;reconstruction_disagreement;project_history;diagnostic_probe  
Recommended use: use_as_project_history_only  
Shared with row IDs:  
Text or paraphrase:
This fragment should be kept only so later workers do not accidentally revive the wrong problem. It asks whether `*kwiθuz` ought to lower to an `e`-grade outcome because the coda consonant is coronal, and then wonders whether attested `cwidu` reflects analogical restoration. That was a reasonable diagnostic question before the row's reconstruction was repaired, but it depends entirely on the obsolete input `*kwiθuz`. After the correction to `*kwéðuz`, the row is no longer evidence for an unresolved NWGmc `i > e` problem.

### DEV_NOTES:line-28401-28519

Source heading: `cwedu` protoform correction and OE variant map  
Source line or section hint: lines 28401-28519  
Status: current  
Issue tags: protoform_vs_proto;Verner_law;OE_variation;attested_variant;reconstruction_disagreement  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This is the controlling row note. It treats the mismatch `*kwíθuz → cwiþu` versus target `cwedu` as evidence that the row's input was reconstructed incorrectly, not as evidence for a missing OE repair rule. The source survey ties together the IE and Germanic evidence: Sanskrit `jatú` points to PIE `*gʷet-u-` with original `*t`; Verner's Law and paradigm levelling give PGmc `*kweðuz`; Kroonen's citation form `*kweduz` is compatible with that because Leiden `d` stands for intervocalic `[ð]`; ON `kváða / kvoða` preserves the voiced dental directly; and OHG `quiti / kuti` fits PWGmc dental hardening from `*ð` to `*d`, not a PGmc `*þ` source [@Pokorny1959; @Kroonen2013, p. 313; @Orel2003; @RingeTaylor2014, p. 323]. The same fragment then maps the OE forms explicitly: inherited conservative `cwedu`, levelled `cwidu`, back-umlauted `cweodu`, rounded `cwudu`, and simplified `cudu`. For current row policy, its most important practical statement is that feeding `*kwéðuz` to the present FST yields `cwedu` directly, so the target form is both attested and derivable without adding further dialect-specific rules. The only unresolved inconsistency it leaves behind is external to the note itself: it assumes the cognate-set `PROTO` field has been aligned to `*kwéduz`, whereas the live TSV row still preserves stale `*kwíθuz`.

## Superseded or diagnostic material

Two older materials need to stay visible but clearly labelled. First, the March note at `DEV_NOTES:line-6009-6085` is not wrong in its source audit; it is simply tied to an earlier project state in which the row still had to be narrated as a move away from `cudu` and `*kwiθuz`. Use it for quotations and variant attestations, not for final row policy. Second, the April `i`-lowering audit at `DEV_NOTES:line-17436-17480` should now be treated as closed diagnostic history, because it tests a phantom issue created by the obsolete protoform.

The active caution for later work is not phonological but editorial. `DEV_NOTES:line-28401-28519` assumes a clean split between cognate-set `PROTO` (`*kwéduz` / Kroonen-style `*kweduz`) and row-level `PROTOFORM` (`*kwéðuz`), but the live TSV row has only half of that repair: `PROTOFORM` is corrected, `PROTO` is not. Any final report or future data cleanup must keep that mismatch explicit rather than silently pretending the row metadata is already synchronized.

## Open questions for later work

- Decide whether the central TSV cleanup should finally align live `PROTO` with the corrected cognate-set reconstruction `*kwéduz` / `*kweduz`, since the row note and DEV_NOTES already operate on that assumption.
- Decide how much of the direct quotation cache from `DEV_NOTES:line-6009-6085` belongs in the final report, especially Kroonen's variant list and Ringe-Taylor's `cwidwes` quotation.
- When writing the final report, keep the variant hierarchy explicit: `cwedu` as the conservative attested target, `cwidu` as the paradigm-levelled form, and `cweodu` / `cwudu` / `cudu` as later dialectal or phonological developments rather than competing proto-level reconstructions.
