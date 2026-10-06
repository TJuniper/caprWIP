# Order-sensitivity first-break lower-early batch report

## Summary

- rules tested: `SC020`, `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC027`, `SC028`, `SC029`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all `20` directions completed
- `8` directions found historically interpretable first breaks
- `0` directions found non-historical computational first breaks
- `12` directions ended as runner-limited / no-break outcomes

This pass creates ten new chronology cards, adds the lower-early corridor to the repo-facing order-sensitivity table, and refreshes the chronology-card README / index / consolidation inventory so the committed lower-early batch is fully folded into the documentation layer.

## Method

This report interprets the already committed first-break TSV outputs only. A first break is a real failure where a baseline-matching Old English derivation stops matching after reordering; changed-still-passing rows may be useful context, but they do not define the boundary. Earlier searches that stop at bundled `PWGmcChanges` are treated as runner-limited rather than as ordinary historical boundaries, and later searches that reach the current `SC087` boundary with no real break are treated as no-break computational outcomes rather than as historical claims about `SC087`. Variant outputs written as `+?` are treated here as no-output / failed derivations, not as surface Old English forms.

## Clean reciprocal historical constraints

### SC026 NWGmc Nasal Spirant Lengthening / SC027 NWGmc Nasal Spirant Loss

- `SC026` current order: `26`
- `SC026` later boundary: order `27`, crossing `SC027` NWGmc Nasal Spirant Loss
- `SC027` current order: `27`
- `SC027` earlier boundary: order `26`, crossing `SC026` NWGmc Nasal Spirant Lengthening
- representative concrete failures:
  - PGmc `*fúnxstiz` > expected OE `fȳst`, variant `fyst`
  - PGmc `*gánsz` > expected OE `gōs`, variant `ġeas`
  - PGmc `*júgunθ` > expected OE `ġeoguþ`, variant `ġeogoþ`

This is the cleanest new lower-early reciprocal pair. Delaying `SC026` across `SC027`, or pulling `SC027` earlier across `SC026`, breaks the same three derivations in the same way. The pair therefore gives a tight local chronology relation inside the nasal-spirant corridor.

### SC029 OE Awj Glide Formation / SC030 OE Au Fronting

- `SC029` current order: `29`
- `SC029` later boundary: order `30`, crossing `SC030` OE Au Fronting
- `SC030` current order: `30`
- `SC030` earlier boundary: order `29`, crossing `SC029` OE Awj Glide Formation
- representative concrete failures:
  - PGmc `*xáwwją` > expected OE `hīeġ`, variant `hauġ`
  - PGmc `*stráwjaną` > expected OE `strīeġan`, variant `strauian`

This is another tight reciprocal boundary, now anchoring the immediate lower-early to upper-early transition. Moving `SC029` later than `SC030`, or moving `SC030` earlier than `SC029`, restores unfronted `au` outputs where the live sequence yields the expected glide-plus-fronting outcomes.

## One-sided historical constraints

### SC021 retired NWGmc Unstressed O Raising

`SC021` was later retired after source-led adjudication. The old runner result
is archival: its apparent SC040 break depended on the retired `*xémonų`
`heaven` proxy and SC040's former early position. Current chronology uses
SC071/SC099/SC100 instead, and SC021 is not a live one-sided constraint.

### SC023 Proto-Germanic Word-Final N Loss (adjudicated 2026; formerly NWGmc N Stem N Loss)

`SC023` also remains one-sided in current testing. No earlier real break was found before bundled `PWGmcChanges`, but moving `SC023` later than `SC047` OE Heavy Syllable Nasal Apocope turns PGmc `*dōną` into `+?` instead of expected OE `dōn`. That is a real historical boundary, but it is counterfeeding: SC023 never applies to `do` in the live cascade (OE `dōn` keeps the secondary `-n` created by SC047 precisely because the old loss was no longer active), and the wrong outcome must be described as a failed derivation rather than as a competing surface form.

### SC024 NWGmc Long E Lowering

`SC024` likewise has one historically interpretable side in the current searchable corridor. No earlier real break was found before bundled `PWGmcChanges`, but moving `SC024` later than `SC056` OE Ws Palatal Diphthongization turns PGmc `*skḗpą` into `sċīep` instead of expected OE `sċēap`, and PGmc `*jḗrą` into `ġīer` instead of expected `ġēar`.

## Broad / far historical constraints

### SC020 later across SC040

`SC020` is historically interpretable on both sides, but its later side is broad and far rather than local. Moving PGmc Final Z Deletion later than `SC040` OE Med Unstressed U Lowering newly fails eleven rows, including PGmc `*bébruz` > expected OE `befer`, variant `befro`; PGmc `*kwéðuz` > expected OE `cwedu`, variant `cwedo`; and PGmc `*félθuz` > expected OE `feld`, variant `feldo`. The earlier side across `SC019` is real and local, but the later side should not be narrated as a tight adjacency claim.

### SC021 later across SC040 (retired archival result)

This old broad/far result is no longer a current historical constraint.
Moving the retired NWGmc Unstressed O Raising later than OE Med Unstressed U
Lowering broke the then-current `heaven` proxy (`*xémonų` > `heofun` instead
of `heofon`), but that proxy and the active SC021 rule have both been retired.

### SC023 later across SC047

`SC023` later is historically real (as stage-entailed counterfeeding evidence; the rule never applies to `do` live), but it is not a local neighboring-stage constraint. The first break appears only at order `47`, crossing `SC047` OE Heavy Syllable Nasal Apocope, where PGmc `*dōną` stops producing OE `dōn` and instead yields no output (`+?`).

### SC024 later across SC056

`SC024` later is another broad/far one-sided boundary. The first real break appears only when the rule is delayed to order `56`, crossing `SC056` OE Ws Palatal Diphthongization, where PGmc `*skḗpą` yields `sċīep` instead of `sċēap` and PGmc `*jḗrą` yields `ġīer` instead of `ġēar`.

## Negative / runner-limited / no-break outcomes

### Earlier runner-limited sides at bundled PWGmcChanges

The earlier searches for `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, and `SC029` all ran safely down to order `13` before the runner entered bundled `PWGmcChanges`. None of those earlier sides should be rewritten as ordinary historical boundaries.

### Negative / boundary cards: SC022, SC025, SC028

`SC022`, `SC025`, and `SC028` are pure negative / boundary cards in the current searchable corridor. On the earlier side, each search stops at bundled `PWGmcChanges` with no real break. On the later side, each search runs through order `86` with no real break before the current `SC087` boundary. These cards therefore record the present search limits rather than positive chronology constraints.

### Later no-break-before-boundary outcomes

The later searches for `SC022`, `SC025`, `SC027`, and `SC028` found no real break before the current `SC087` boundary. Those are computational observations only. They must not be rewritten as claims that any of those rules historically must precede `SC087`.

## Cross-rule observations

The strongest new network effects from this batch are:

1. `SC026` / `SC027`: a clean reciprocal three-row boundary now anchors the nasal-spirant corridor around `fȳst`, `gōs`, and `ġeoguþ`.
2. `SC029` / `SC030`: the `hay` / `strew` evidence now anchors the immediate handoff from lower-early glide formation to upper-early au-fronting.
3. `SC020` later and `SC021` later both point forward to the much later unstressed-vowel corridor at `SC040`, but those links are broad/far computational boundaries rather than local adjacency claims.
4. `SC023` later across `SC047` and `SC024` later across `SC056` show that one-sided lower-early rules can still have historically interpretable later limits deep into the middle chronology, but those limits remain broad and must be narrated carefully.
5. `SC022`, `SC025`, and `SC028` remain genuinely negative cards: the current searchable corridor does not yet yield a historical first break for them in either direction.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_lower_early_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_consolidation_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC020-pgmc-final-z-deletion.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC021-nwgmc-unstressed-o-raising.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC022-nwgmc-mn-dissimilation.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC023-nwgmc-n-stem-n-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC024-nwgmc-long-e-lowering.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC025-nwgmc-long-e-nasal-rounding.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC026-nwgmc-nasal-spirant-lengthening.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC027-nwgmc-nasal-spirant-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC028-nwgmc-preconsonantal-x-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC029-oe-awj-glide-formation.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`
- `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`

## Recommended next task

The lower-early batch is now interpreted, so the next terminal batch should shift to the remaining early explicit corridor:

1. `SC014` NWGmc Unstressed Ai Monophthongization
2. `SC015` NWGmc I Lowering
3. `SC016` OE Ws Palatal Glide
4. `SC017` NWGmc U Lowering
5. `SC018` NWGmc Stressed Monosyllable O Raising
6. `SC019` NWGmc Final Long O Raising

That six-rule set closes the last open explicit-chain gap below the newly interpreted `SC020`-`SC040` region while also picking up `SC019`, which is now implicated both by `SC020` earlier and by the older `SC036` earlier boundary.
