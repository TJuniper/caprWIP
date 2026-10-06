# Research memo — 2092 laugh / hliehhan

## Starting point

- **ID:** 2092
- **CONCEPT:** laugh
- **COUNTERPART:** `hliehhan`
- **PROTO:** `*lákaną`
- **PROTOFORM:** `*xláxjaną`
- **DERIVATION_CLASS:** `early_analogy`
- **NOTE:** `§17.40: target hlæhhan → hliehhan (WS form per Bright p.597, Brunner §392,4; Anglian hlæhhan attested as variant — cascade defaults to WS). Added *x to PWGmcJGemination per Fulk §6.15. | R/T: PGmc *hlahjanan > OE hlæhhan/hliehhan`

The live row already distinguishes three levels: the aligned cognate-set label `*lákaną`, the OE-directed derivational input `*xláxjaną`, and the OE target `hliehhan`. Current repo state also shows that the live bin now maps `*xláxjaną` to `hliehhan`, so this is no longer a live mismatch. No pilot or full lexeme report for this row turned up; `coverage_audit.md` still marks it as report-requiring.

## Packet evidence assessment

- **Authoritative/current:** the live TSV row; the packet's compact derivation trace showing `*xláxjaną -> hliehhan`; the later `DEV_NOTES.md` implementation/verification section confirming `*xláxjaną -> hliehhan` after the *x-gemination/x-loss fix; and the current bin behavior itself, which now returns `hliehhan`.
- **Useful background:** the packet's source audit citing Bright, Brunner, Fulk, Bosworth-Toller, and Ringe/Taylor; and the packet's preservation of the longer `DEV_NOTES.md` dossier on why the old failure happened.
- **Stale or superseded:** the packet's inherited `four_complex_tsv_items.md` material and the earlier `DEV_NOTES.md` phases that still treat row 2092 as `*xlaxjăną -> hlæhhan` / `hliehan`, i.e. as an unresolved mismatch. Those passages are valuable project history, but they are not the current row state.
- **Irrelevant or misleading:** the lack of a manifest entry or `oe_known_problems.tsv` hit is not lexical evidence; and lightweight lexical-table hits, especially `old_english_wiktionary.tsv`'s bare `hlæhhan`, should not outrank the handbook/dictionary evidence for WS `hliehhan`.

So the packet is useful only if read chronologically. It mixes current evidence with stale pre-fix workflow history, and the memo/report should separate those explicitly.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around `38872-39368`, including the pre-fix diagnosis, the long research dossier on preconsonantal *x-loss, and the later verification block.
- `Germanic/docs/analysis/four_complex_tsv_items.md`, which still preserves the older mismatch-stage analysis.
- `Germanic/docs/lexeme_reports/coverage_audit.md`.
- `Germanic/data/oe_known_problems.tsv` (no row-specific entry).
- `Germanic/data/old_english_swadesh.tsv` (`to laugh -> hliehhan`).
- `Germanic/data/old_english_wiktionary.tsv` (`laugh -> hlæhhan`).
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`.
- `docs/references/campbell_old_english_grammar.txt`.
- `docs/references/brunner_1965_altenglische_grammatik.txt`.
- `docs/references/bright_anglo_saxon_reader.txt`.
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`.
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`.
- `docs/references/hogg_vol1.txt`.

Main findings from that extra pass:

- Kroonen's comparative headword is `*hlah(j)an-`, with an explicit alternation between ON `hlæja < *hlahjan-` and OS `hlahan < *hlahan-` [@Kroonen2013].
- Ringe/Taylor explicitly derive OE `hliehhan` from `*hlahjana` and also treat Anglian poetic `hlehhan` as a variant [@RingeTaylor2014].
- Brunner, Bright, Bosworth-Toller, Campbell, Fulk, and Hogg all support preserved OE `hh` from earlier `hj/*xj`, so the old single-`h` output was a project bug, not a genuine philological competitor [@SieversBrunner1965; @BrightCassidyRingler1971; @BosworthToller1898; @Campbell1959; @Fulk2018; @HoggPhonology1992].
- The supplementary OE tables disagree (`hliehhan` in Swadesh, `hlæhhan` in Wiktionary), which is useful background but too light to settle the row against the heavier handbook evidence.

## Reconstruction and early-stage forms

This row needs a strict three-way distinction.

1. **Cognate-set proto / project headword:** `PROTO = *lákaną`. In the aligned dataset this is the comparative label shared by the Dutch/English/German rows, i.e. the non-j branch that underlies continental `lachen/laugh` outcomes.
2. **OE project input form:** `PROTOFORM = *xláxjaną`. This is the OE-facing j-present input, corresponding to the repo's `x`-notation for the velar fricative and to the comparative reconstruction `*hlahjana` / Kroonen's `*hlah(j)an-` [@Kroonen2013; @RingeTaylor2014].
3. **OE target form:** `hliehhan`, the West Saxon lemma the row now targets and the current bin now produces.

Those levels should not be collapsed. The row is not claiming that OE `hliehhan` is the direct reflex of the aligned cognate-set label `*lákaną`. It is claiming that the OE branch continues the j-present formation `*xláxjaną`, while the broader cognate set is still catalogued under the non-j comparative label.

That distinction also explains why `DERIVATION_CLASS = early_analogy` is still plausible. The special move is upstream lexeme/stem selection: the OE row is not derived from the same early-stage branch as the continental rows.

## Old English philology

This is an **attested OE lemma-level case**, not a reconstructed-OE target and not a paradigm-cell entry.

- WS `hliehhan` is solidly supported in the checked handbook and dictionary material [@BrightCassidyRingler1971; @SieversBrunner1965; @BosworthToller1898].
- Anglian/Northumbrian or otherwise non-WS variants are also real in repo-local sources, but they are variant territory, not the best current target for the default OE cascade. Repo sources variously preserve `hlehhan`, `hlæhhan`, `hlihhan`, and related forms [@RingeTaylor2014; @SieversBrunner1965; @BosworthToller1898].
- The old project bug was the loss of gemination. Fulk states that j-gemination applies after a short vowel to any consonant except `r`, and Campbell explicitly says OE geminate `x` remains as `hh`, citing `hliehhan` itself [@Fulk2018; @Campbell1959].
- The more delicate philological point is the broken vowel. Ringe/Taylor call `laugh` the unique example where breaking occurs before the palatalized geminate and say the broken vowel may have spread from the related noun `*hleahtr` by lexical analogy [@RingeTaylor2014]. Brunner likewise ties non-WS `hlæhhan` to influence from the noun [@SieversBrunner1965].

So the safest memo/report line is: `hliehhan` is an attested WS lemma with well-supported `hh`; the row's residual specialness is not the lemma itself, but the early-stage branch selection and probably analogical support behind the broken-vowel history.

## Project problem and solution

The project problem was originally twofold: (1) the FST failed to geminate `*x` before `*j`, and (2) a downstream *x-loss rule then wrongly deleted part of the new geminate. That bug trail is now historical. Current repo state shows the fix is in place and the bin returns `hliehhan`.

The remaining interpretive problem is how to describe the row without flattening the levels:

- `PROTO = *lákaną` is the aligned cognate-set label, not the OE derivational input.
- `PROTOFORM = *xláxjaną` is the input that matters for the OE derivation.
- `COUNTERPART = hliehhan` is the WS target now preferred by the project.
- `DERIVATION_CLASS = early_analogy` remains defensible because the row's special move is early branch/stem choice plus likely analogical support for the vowel history, not a late paradigm-cell substitution.

So the present row design is basically sound. What still needs care is explanatory wording: readers should be told that older `hlæhhan` material in the repo is mostly variant background or stale workflow state, not the current project target.

## Paradigm probe

No paradigm probe is required.

This is not a true paradigm-cell case. The decisive issue is lexeme/branch selection (`*lákaną` vs. OE-facing `*xláxjaną`) and the status of WS `hliehhan` versus variant forms, not the choice of one inflectional cell from within a single OE paradigm. A probe would add little unless the project later wants a purely diagnostic comparison of `*lákaną` against `*xláxjaną`, which would be background only.

## Recommended final report

Recommend a concise final report that says row 2092 keeps the aligned cognate-set label `*lákaną`, derives OE from j-present `*xláxjaną`, and targets attested WS `hliehhan` as the default OE outcome, while treating `hlehhan/hlæhhan` and other non-WS forms as variant background rather than the row's target. The report should also note that `hh` is regular once the project bug is fixed, whereas the broken vowel is the genuinely special part of the history and may owe something to analogy with `hleahtor` [@RingeTaylor2014].

## Data-change recommendations

- **TSV `PROTO`:** no change recommended. Keep `*lákaną` as the aligned cognate-set label for this multi-row set, but explain its relation to the OE j-present more clearly in prose.
- **TSV `PROTOFORM`:** no change recommended. `*xláxjaną` is the right OE-facing input.
- **TSV `COUNTERPART`:** no change recommended. Keep `hliehhan`.
- **TSV `DERIVATION_CLASS`:** no change recommended. `early_analogy` still fits better than `regular` or `late_analogy`, because the special move is upstream branch selection and probably analogical support, not a late cell rescue.
- **TSV `NOTE`:** clarification recommended. It should say more explicitly that `*lákaną` is the aligned cognate-set label, `*xláxjaną` is the OE derivational input, `hliehhan` is the WS target, and `hlæhhan/hlehhan` are variant background rather than rival current targets.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` text:** minor cleanup recommended. The older mismatch-stage discussion can remain, but it should be marked more explicitly as superseded by the later implemented-fix/verification block so packet extraction does not promote obsolete state.
- **Dossier / analysis text:** cleanup recommended. `Germanic/docs/analysis/four_complex_tsv_items.md` is now stale for row 2092 because it still frames the row as `hlæhhan` mismatch-era work; it should either be updated or clearly labelled as historical.
