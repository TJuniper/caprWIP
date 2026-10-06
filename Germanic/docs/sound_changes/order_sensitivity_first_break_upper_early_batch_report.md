# Order-sensitivity first-break upper-early batch report

## Summary

- rules tested: `SC030`, `SC031`, `SC032`, `SC033`, `SC034`, `SC035`, `SC036`, `SC037`, `SC039`, `SC040`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all `20` directions completed
- `14` directions found historically interpretable first breaks
- `3` directions found non-historical computational first breaks (`SC031` earlier, `SC033` earlier, `SC037` later)
- `3` directions ended as no-break / runner-limited outcomes before bundled `PWGmcChanges` (`SC035` earlier, `SC037` earlier, `SC039` earlier)

This pass creates ten new chronology cards, updates the repo-facing order-sensitivity table, and refreshes the chronology-card README / index / consolidation inventory so the upper-early batch is fully folded into the documentation layer.

## Method

This report interprets the already committed first-break TSV outputs only. A first break is a real failure where a baseline-matching Old English derivation stops matching after reordering; changed-still-passing rows may be useful context, but they do not define the boundary. Variant outputs written as `+?` are treated here as no-output / failed derivations, not as surface Old English forms. No live FST order was changed in this pass, and no new first-break computations were run.

## Strong historical reciprocal / near-reciprocal constraints

### SC030 OE Au Fronting / SC032 OE Diphthong Leveling

- `SC030` current order: `30`
- `SC030` later boundary: order `32`, crossing `SC032` OE Diphthong Leveling
- `SC032` current order: `32`
- `SC032` earlier boundary: order `30`, crossing `SC030` OE Au Fronting
- representative concrete failures:
  - PGmc `*galáubijaną` > expected OE `ġelīefan`, variant `+?` (no output)
  - PGmc `*bráudą` > expected OE `brēad`, variant `+?` (no output)
  - PGmc `*dráugmaz` > expected OE `drēam`, variant `+?` (no output)

This is the strongest new upper-early reciprocal pair. Delaying `SC030` past `SC032`, or pulling `SC032` earlier than `SC030`, collapses the same eighteen derivations into no-output failures rather than alternate surface forms. That makes the `SC030` / `SC032` relation historically interpretable, but it also requires careful prose: the bad outcomes are failed derivations, not attested competing Old English reflexes.

### SC031 OE WW Simplification / SC034 OE Aw Long Diphthong

- `SC031` later boundary: order `34`, crossing `SC034` OE Aw Long Diphthong
- `SC034` earlier boundary: order `31`, crossing `SC031` OE WW Simplification
- representative concrete failures:
  - PGmc `*dáwwō` > expected OE `dēaw`, variant `dawu`
  - PGmc `*xáwwaną` > expected OE `hēawan`, variant `hawan`

This is a tight local near-reciprocal pair around the `dew` / `hew` corridor. `SC031`'s historically interpretable side is its later boundary, and `SC034` confirms that same local relation from the opposite side. The broader non-historical `SC031` earlier result across bundled `PWGmcChanges` does not weaken the local historical evidence connecting `SC031` and `SC034`.

### SC039 OE WI Combinative U Umlaut / SC040 OE Med Unstressed U Lowering

- `SC039` later boundary: order `40`, crossing `SC040` OE Med Unstressed U Lowering
- `SC040` earlier boundary: order `39`, crossing `SC039` OE WI Combinative U Umlaut
- representative concrete failures:
  - PGmc `*wíduwōn` > expected OE `wuduwe`, variant `wudowe`

This is a clean reciprocal local widow-based boundary. Moving `SC039` later or `SC040` earlier across the other rule produces the same wrong unstressed vowel sequence, so the pair gives a compact historical anchor inside the upper-early unstressed-vowel corridor.

## Broad / far historical constraints

### SC033 later across SC044

`SC033` later is historically real, but it is broad and far away rather than tightly local. Moving OE Ew Long Diphthong later than `SC044` OE Breaking turns PGmc `*kéwwaną` into `ċeowan` instead of expected `ċēowan`, PGmc `*fédwōr` into `feower` instead of `fēower`, and PGmc `*knéwą` into `cneow` instead of `cnēow`.

### SC036 earlier across SC019

`SC036` earlier is also historically real but relatively far back. Moving OE Inter Stress Raising earlier than `SC019` NWGmc Final Long O Raising turns PGmc `*sáiwalō` into `sāwel` instead of expected `sāwol`, so this side should be narrated as a broader earlier constraint rather than as a neighboring-stage adjacency claim.

### SC040 later across SC072

`SC040` later is a real historical boundary, but it is broad and far away across `SC072`. Moving OE Med Unstressed U Lowering later than OE Unstressed Long Vowel Shortening turns PGmc `*júgunθ` into `ġeogoþ` instead of expected `ġeoguþ`, so this later side should not be narrated as a tight local adjacency claim.

## One-sided historical constraints

### SC033 OE Ew Long Diphthong

`SC033` currently has one historically interpretable side. Its later boundary across `SC044` is real, but its earlier side crosses bundled `PWGmcChanges` and is therefore non-historical in the current runner.

### SC035 OE Prefix A Reduction Early

`SC035` currently also has one historically interpretable side. No earlier real break was found before the runner entered bundled `PWGmcChanges`, but moving `SC035` later than `SC043` Anglo Frisian Brightening turns PGmc `*galáubijaną` into `ġealīefan` instead of expected `ġelīefan`.

## Non-historical / runner-limited / technical-marker outcomes

### SC031 earlier across bundled PWGmcChanges

- first earlier computational break: order `13`
- crossed stage type: `blocked_by_runner_limitation`
- representative concrete failures:
  - PGmc `*fédwōr` > expected OE `fēower`, variant `fēowwer`
  - PGmc `*xáwwją` > expected OE `hīeġ`, variant `hēai`

This is a real computational break, but it is not an ordinary historical first-break constraint because the move enters bundled `PWGmcChanges`.

### SC033 earlier across bundled PWGmcChanges

- first earlier computational break: order `13`
- crossed stage type: `blocked_by_runner_limitation`
- representative concrete failure:
  - PGmc `*fédwōr` > expected OE `fēower`, variant `feower`

Again, this is a non-historical computational break rather than an ordinary chronology constraint.

### SC035 earlier, SC037 earlier, and SC039 earlier

These earlier searches found no real break before the runner entered bundled `PWGmcChanges`; all three therefore remain runner-limited on the earlier side rather than historically interpretable.

### SC037 later across SC038 OE Strip Secondary Stress

- first later computational break: order `38`
- crossed stage type: `technical_marker`
- representative concrete failure:
  - PGmc `*régna-bùgô` > expected OE `reġnboga`, variant `reġnefoga`

This is a real computational break, but it crosses a technical marker (`SC038`) rather than an ordinary historical sound change. It therefore belongs in the documentation layer as a technical caution, not as a historical adjacency claim.

## Cross-rule observations

The strongest new network effects from this batch are:

1. `SC030` / `SC032`: an eighteen-row reciprocal no-output boundary now anchors the au / diphthong-leveling corridor.
2. `SC031` / `SC034`: a tight `dēaw` / `dawu` and `hēawan` / `hawan` relation sharpens the upper-early `ww` / `aw` corridor.
3. `SC039` / `SC040`: the `wuduwe` / `wudowe` pair gives a clean local reciprocal unstressed-vowel constraint.
4. `SC031` earlier and `SC033` earlier show that bundled `PWGmcChanges` can still produce real computational breaks that are not yet ordinary historical chronology evidence.
5. `SC037` later shows the same caution for a technical marker: crossing `SC038` yields a real computational break, but not a historical sound-change boundary.
6. `SC033` later across `SC044`, `SC036` earlier across `SC019`, and `SC040` later across `SC072` are all real but broad/far historical constraints rather than tight local adjacencies.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_upper_early_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_consolidation_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC030-oe-au-fronting.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC031-oe-ww-simplification.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC032-oe-diphthong-leveling.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC033-oe-ew-long-diphthong.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC034-oe-aw-long-diphthong.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC035-oe-prefix-a-reduction-early.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC036-oe-inter-stress-raising.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC037-oe-compound-linking-syncope.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC039-oe-wi-combinative-u-umlaut.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC040-oe-med-unstressed-u-lowering.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`
- `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`

## Recommended next task

The upper-early batch is now interpreted, so the next terminal batch should shift back to the remaining lower-early explicit corridor immediately below it. After the SC021 adjudication, the retired former unstressed-o rule is not a current candidate:

1. `SC020` PGmc Final Z Deletion
2. `SC022` Common Germanic Mn Dissimilation (executable holding-zone placement)
3. `SC023` Proto-Germanic Word-Final N Loss (formerly NWGmc N Stem N Loss)
4. `SC024` NWGmc Long E Lowering
5. `SC025` NWGmc Long E Nasal Rounding
6. `SC026` NWGmc Nasal Spirant Lengthening
7. `SC027` NWGmc Nasal Spirant Loss
8. `SC028` NWGmc Preconsonantal X Loss
9. `SC029` OE Awj Glide Formation

That nine-rule set fills the contiguous lower-early gap directly below the newly completed `SC030`-`SC040` band while also capturing stages already implicated by the new `SC030` and old `SC041` evidence. `SC019` remains an immediate follow-up singleton, but keeping SC021 retired makes `SC020`, `SC022`-`SC029` the cleaner next corridor.
