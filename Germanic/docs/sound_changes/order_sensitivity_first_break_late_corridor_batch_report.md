# Order-sensitivity first-break late-corridor batch report

## Summary

- rules tested: `SC065`, `SC066`, `SC067`, `SC068`, `SC069`, `SC070`, `SC071`, `SC074`, `SC075`, `SC076`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all `20` directions completed
- `10` directions found first breaks
- `10` directions ended as no-break / boundary-limited outcomes
- later no-break searches reached the current `SC087` runner boundary for `SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, and `SC076`
- earlier searches for `SC065`, `SC067`, and `SC076` were blocked by bundled `PWGmcChanges`

This pass creates ten new chronology cards, updates the repo-facing order-sensitivity table, and refreshes the chronology-card README / index / consolidation inventory so the late-corridor batch is fully folded into the documentation layer.

## Method

This report interprets the already committed first-break TSV outputs only. A first break is a real failure where a baseline-matching Old English derivation stops matching after reordering; changed-still-passing rows may be useful context, but they do not define the boundary. No live FST order was changed in this pass, and no new first-break computations were run.

## Strong chronology constraints

### SC066 OE L Adjacent Syncope

- current order: `66`
- safe computational window: `56-67`
- earlier boundary: order `55`, crossing `SC055` OE I Umlaut
- later boundary: order `68`, crossing `SC068` OE Preconsonantal Degemination
- representative concrete failures: PGmc `*nátilōn` > expected OE `netle`, variant `nætle`; PGmc `*spénnilō` > expected OE `spinl`, earlier variant `spenl`, later variant `spinnl`

SC066 is historically interpretable on both sides. The earlier side shows that OE L Adjacent Syncope cannot move ahead of OE I Umlaut without losing the live umlauted vocalism in forms such as `netle` and `spinl`; the later side shows that delaying SC066 past OE Preconsonantal Degemination leaves the unwanted doubled consonant cluster in `spinnl`. The later side directly reciprocates `SC068` earlier.

### SC068 OE Preconsonantal Degemination

- current order: `68`
- safe computational window: `67-86`
- earlier boundary: order `66`, crossing `SC066` OE L Adjacent Syncope
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: PGmc `*spénnilō` > expected OE `spinl`, variant `spinnl`

SC068 is one-sided in current testing. Its earlier boundary is historically interpretable and reciprocates `SC066` later around the `spindle` derivation, but the later search reached the current `SC087` boundary with no real break and therefore does **not** show that SC068 historically had to precede `SC087`.

### SC070 OE Unstressed Fronting Early

- current order: `70`
- safe computational window: `53-70`
- earlier boundary: order `52`, crossing `SC052` OE Velar Palatalization
- later boundary: order `71`, crossing `SC071` OE Late O Shortening
- representative concrete failures: PGmc `*lúnganjō` > expected OE `lungen`, variant `lunġen`; PGmc `*búrōθi` > expected OE `boraþ`, variant `boreþ`; PGmc `*mḗnōθz` > expected OE `mōnaþ`, variant `mōneþ`

SC070 is historically interpretable on both sides. Moving it earlier than `SC052` lets palatalization intrude too early in the `lung` derivation, while moving it later than `SC071` creates a six-row set of wrong unstressed-vowel outputs in forms such as `boreþ` and `mōneþ`. That later side forms a strong reciprocal relation with `SC071` earlier.

### SC071 OE Late O Shortening

- current order: `71`
- safe computational window: `71-86`
- earlier boundary: order `70`, crossing `SC070` OE Unstressed Fronting Early
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failures: PGmc `*búrōθi` > expected OE `boraþ`, variant `boreþ`; PGmc `*líznōθi` > expected OE `liornaþ`, variant `liorneþ`; PGmc `*mḗnōθz` > expected OE `mōnaþ`, variant `mōneþ`

SC071 is strongly pinned on the earlier side and one-sided later. Moving it earlier than `SC070` reproduces the same six-row failure set seen on `SC070` later, so the reciprocal relation is secure; the later search again reached `SC087` with no real break, which is only a computational boundary observation.

### SC074 OE Med Unstressed I Lowering1

- current order: `74`
- safe computational window: `73-74`
- earlier boundary: order `72`, crossing `SC072` OE Unstressed Long Vowel Shortening
- later boundary: order `75`, crossing `SC075` OE Med Unstressed I Lowering
- representative concrete failures: PGmc `*fúrxtīnaz` > expected OE `fyrhte`, variant `fyrhti`; PGmc `*skíllingaz` > expected OE `sċilling`, variant `sċilleng`

SC074 is historically interpretable on both sides. Moving it earlier than `SC072` leaves the `fright` derivation with final `-i` instead of live `-e`, while moving it later than `SC075` produces `sċilleng` rather than `sċilling` in the `shilling` derivation. The later side directly reciprocates `SC075` earlier.

### SC075 OE Med Unstressed I Lowering

- current order: `75`
- safe computational window: `75-86`
- earlier boundary: order `74`, crossing `SC074` OE Med Unstressed I Lowering1
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: PGmc `*skíllingaz` > expected OE `sċilling`, variant `sċilleng`

SC075 is one-sided later, but its earlier boundary is historically strong because it directly reciprocates `SC074` later around the `shilling` derivation. The later no-break result should again be treated only as a boundary of the present search space, not as a claim that SC075 historically sat just before `SC087`.

## Broad / one-sided historical boundary

### SC069 OE Early O Shortening

- current order: `69`
- safe computational window: `24-86`
- earlier boundary: order `23`, crossing `SC023` Proto-Germanic Word-Final N Loss (formerly NWGmc N Stem N Loss)
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failures: PGmc `*nḗdrōn` > expected OE `nǣdre`, variant `nǣdran`; PGmc `*érθōn` > expected OE `eorþe`, variant `eorþan`; PGmc `*fláskōn` > expected OE `flasce`, variant `flascan`

SC069 does have a real earlier first break, but it is broad and far away rather than a tight local adjacency. Moving SC069 earlier across `SC023` creates a 17-row set of restored final `-an` outcomes, so this side should be narrated as a broad computational boundary. The later direction found no real break before `SC087`, so the card remains one-sided in current testing.

## Negative / runner-bounded outcomes

### SC065 OE Medial Syncope

- current order: `65`
- safe computational window: `13-86`
- earlier boundary: no real break before runner limitation; last safe order `13`, boundary `PWGmcChanges`
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: none, because no real break was found on either side

SC065 is a negative/boundary card rather than a chronology-constraint card. The earlier side is blocked by the current runner limitation inside `PWGmcChanges`, and the later side reaches the present `SC087` search boundary with no real break.

### SC067 OE Dental Assimilation

- current order: `67`
- safe computational window: `13-86`
- earlier boundary: no real break before runner limitation; last safe order `13`, boundary `PWGmcChanges`
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: none, because no real break was found on either side

SC067 is also a negative/boundary card rather than a chronology-constraint card. Neither tested direction currently yields a historical first-break boundary within the searchable corridor.

### SC076 OE Prefix I Reduction

- current order: `76`
- safe computational window: `13-86`
- earlier boundary: no real break before runner limitation; last safe order `13`, boundary `PWGmcChanges`
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: none, because no real break was found on either side

SC076 completes the same negative pattern seen for SC065 and SC067. It is useful computationally because it shows the current searchable corridor still does not force a historical first break for the rule in either direction.

## Cross-rule observations

The strongest new network effects from this batch are:

1. `SC066` / `SC068`: a reciprocal `spindle`-based relation ties the syncope and degemination corridor together.
2. `SC070` / `SC071`: a reciprocal six-row unstressed-vowel set confirms the order of early fronting and late o-shortening.
3. `SC074` / `SC075`: a reciprocal `shilling`-based boundary strengthens the late weak-tail corridor.
4. `SC069` earlier is historically real, but it is broad and far away across `SC023`, so it should not be flattened into a tight adjacency claim.
5. Several later searches reached `SC087` with no real break (`SC065`, `SC067`, `SC068`, `SC069`, `SC071`, `SC075`, `SC076`), which is informative about the current search space but not historically meaningful as an `SC087` adjacency claim.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_late_corridor_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_consolidation_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC065-oe-medial-syncope.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC066-oe-l-adjacent-syncope.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC067-oe-dental-assimilation.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC068-oe-preconsonantal-degemination.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC069-oe-early-o-shortening.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC070-oe-unstressed-fronting-early.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC071-oe-late-o-shortening.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC074-oe-med-unstressed-i-lowering1.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC075-oe-med-unstressed-i-lowering.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC076-oe-prefix-i-reduction.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`
- `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`

## Recommended next task

The late-corridor batch is now interpreted, so the next terminal batch should shift to the remaining far-late explicit corridor:

1. `SC079` OE J Loss After Heavy
2. `SC080` OE Final Geminate Simplification
3. `SC081` OE J Strengthening After Front Diphthong
4. `SC082` OE Intervocalic J Vocalization
5. `SC083` OE Unstressed EI Contraction
6. `SC085` OE H Loss
7. `SC086` OE Contraction
8. `SC087` OE R Metathesis

That eight-rule set finishes the remaining explicit late corridor without mixing in the much earlier queued region.
