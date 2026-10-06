# Order-sensitivity first-break gap-filling batch report

## Summary

- rules tested: `SC049`, `SC053`, `SC054`, `SC057`, `SC058`, `SC060`, `SC061`, `SC064`, `SC073`
- baseline counts: `380` tested, `373` baseline matches, `7` baseline failures
- all `18` directions completed
- `10` directions found first breaks
- `8` directions ended as no-break / boundary-limited outcomes
- later no-break searches reached the current `SC087` runner boundary for `SC049`, `SC053`, `SC057`, `SC058`, `SC060`, and `SC061`
- earlier searches for `SC053` and `SC058` were blocked by bundled `PWGmcChanges`

This pass creates the nine new chronology cards, updates the repo-facing order-sensitivity table, and refreshes the chronology-card README / index / consolidation inventory so the gap-filling batch is fully folded into the documentation layer.

## Method

This report interprets the already committed first-break TSV outputs only. A first break is a real failure where a baseline-matching Old English derivation stops matching after reordering; changed-still-passing rows may be useful context, but they do not define the boundary. No live FST order was changed in this pass, and no new first-break computations were run.

## SC049 PGmc B Allophony

- current order: `49`
- safe computational window: `38-86`
- earlier boundary: order `37`, crossing `SC037` OE Compound Linking Syncope
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: PGmc `*régna-bùgô` yields expected OE `reġnboga`, but the earlier-shifted variant yields `reġnfoga`

This is a one-sided card in current testing. The earlier side is historically interpretable; the later side is a no-break-before-boundary result and must not be rewritten as a claim that SC049 historically precedes `SC087`.

## SC053 OE Post Velar W Loss

- current order: `53`
- safe computational window: `13-86`
- earlier boundary: no real break before runner limitation; last safe order `13`, boundary `PWGmcChanges`
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: none, because no real break was found on either side

SC053 is currently a negative/boundary card rather than a chronology-constraint card. The earlier side is blocked by the current runner limitation, and the later side reaches the present search boundary with no real break.

## SC054 OE W Loss Before I

- current order: `54`
- safe computational window: `21-62`
- earlier boundary: order `20`, crossing `SC020` PGmc Final Z Deletion
- later boundary: order `63`, crossing `SC063` OE High Vowel Apocope
- representative concrete failure: PGmc `*sáiwiz` yields expected OE `sǣ`, but both the earlier-shifted and later-shifted variants yield `sǣw`

SC054 is historically interpretable on both sides, but the evidence is narrow and concentrated in the same derivation. The card therefore provides a useful local window without yet forming a reciprocal pair in the current chronology network.

## SC057 OE J Cluster Coalescence

- current order: `57`
- safe computational window: `53-86`
- earlier boundary: order `52`, crossing `SC052` OE Velar Palatalization
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failures: PGmc `*báugijaną` > expected OE `bīeġan`, variant `bēaġan`; PGmc `*sōkijaną` > expected OE `sēċan`, variant `sōċan`

This is another one-sided card in current testing. The earlier side is historically interpretable and tied to the SC052 palatalization corridor; the later side is runner-bounded and should not be turned into a must-precede claim.

## SC058 OE Nasal Dissimilation

- current order: `58`
- safe computational window: `13-86`
- earlier boundary: no real break before runner limitation; last safe order `13`, boundary `PWGmcChanges`
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: none, because no real break was found on either side

SC058 is also a negative/boundary card rather than a chronology-constraint card. Neither side currently yields a detected historical first break.

## SC060 OE Ws Palatal Umlaut

- current order: `60`
- safe computational window: `56-86`
- earlier boundary: order `55`, crossing `SC055` OE I Umlaut
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failures: PGmc `*máxtiz` > expected OE `miht`, variant `mieht`; PGmc `*náxti` > expected OE `niht`, variant `nieht`

This card is one-sided in current testing. The earlier boundary is historically interpretable; the later side is a no-break-before-boundary result and must not be narrated as if `SC087` were historically meaningful for SC060.

## SC061 OE Weak Tail Nasal Loss

- current order: `61`
- safe computational window: `24-86`
- earlier boundary: order `23`, crossing `SC023` Proto-Germanic Word-Final N Loss (formerly NWGmc N Stem N Loss)
- later boundary: no real break before runner boundary; last safe order `86`, boundary row `SC087` OE R Metathesis
- representative concrete failure: PGmc `*dōną` yields expected OE `dōn`, but the earlier-shifted variant yields no output (`+?` in the TSV)

This card is also one-sided in current testing. The earlier boundary is historically interpretable, but the later side remains runner-bounded and should not be converted into a positive adjacency claim.

## SC064 NWGmc In Stem N Loss

- current order: `64`
- safe computational window: `42-71`
- earlier boundary: order `41`, crossing `SC041` PWGmc Final Bare A Loss
- later boundary: order `72`, crossing `SC072` OE Unstressed Long Vowel Shortening
- representative concrete failure: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but both the earlier-shifted and later-shifted variants yield `fyrhten`

SC064 is historically interpretable on both sides and materially strengthens the weak-tail chronology corridor. Its later boundary directly reciprocates the already established SC072 earlier boundary.

## SC073 OE Unstressed AE Merger

- current order: `73`
- safe computational window: `73-83`
- earlier boundary: order `72`, crossing `SC072` OE Unstressed Long Vowel Shortening
- later boundary: variant order `84`, crossed change `SC085` OE H Loss
- representative concrete failures: PGmc `*nḗdrōn` > expected OE `nǣdre`, variant `nǣdræ`; PGmc `*fádēr` > expected OE `fæder`, variant `fædær`; later-side PGmc `*táixōn` > expected OE `tā`, variant `tāæ`

SC073 is immediately pinned on the earlier side and broad there, with 24 newly failing rows. The later side is narrower and one-sided; the chronology interpretation should follow the TSV's `crossed_change_id` / `crossed_display_name` fields and treat the later boundary as crossing `SC085` OE H Loss.

## Runner-bounded and no-break outcomes

This batch substantially expands the set of runner-bounded observations:

1. Earlier runner-limitation results at bundled `PWGmcChanges`: `SC053`, `SC058`
2. Later no-break-before-boundary results through last safe order `86`: `SC049`, `SC053`, `SC057`, `SC058`, `SC060`, `SC061`

These are computational boundary observations, not positive historical claims about `SC087`. They show that the current runner found no real later break before the present search limit, not that those rules historically sat just before OE R Metathesis.

## Cross-rule observations

The strongest new network effects from this batch are:

1. `SC064` / `SC072`: `SC064` later and `SC072` earlier now form a reciprocal `fright`-based boundary.
2. `SC072` / `SC073`: `SC072` later and `SC073` earlier now form a reciprocal broad `-æ` boundary, with 24 newly failing rows on the SC073 earlier side.
3. `SC054` adds a one-sided bridge to `SC063`, showing that the `sea` derivation constrains OE W Loss Before I both before high-vowel apocope and after the early final-z corridor.
4. `SC049`, `SC057`, `SC060`, and `SC061` all currently behave as one-sided cards: each has an interpretable earlier boundary and a later no-break result through the present `SC087` search limit.
5. `SC053` and `SC058` are still negative cards on both sides, which is itself useful: they remain computationally unconstrained within the currently searchable corridor.

## Files changed

- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_gap_filling_batch_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/README.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_index.tsv`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/chronology_card_consolidation_report.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC049-pgmc-b-allophony.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC053-oe-post-velar-w-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC054-oe-w-loss-before-i.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC057-oe-j-cluster-coalescence.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC058-oe-nasal-dissimilation.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC060-oe-ws-palatal-umlaut.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC061-oe-weak-tail-nasal-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC064-nwgmc-in-stem-n-loss.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC073-oe-unstressed-ae-merger.md`
- `Germanic/docs/sound_changes/order_tests/first_break_batch_plan_04.md`
- `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`

## Recommended next task

The gap-filling mid corridor is now interpreted, so the next terminal batch should shift to the remaining late corridor immediately adjacent to the newly completed region:

1. `SC065` OE Medial Syncope
2. `SC066` OE L Adjacent Syncope
3. `SC067` OE Dental Assimilation
4. `SC068` OE Preconsonantal Degemination
5. `SC069` OE Early O Shortening
6. `SC070` OE Unstressed Fronting Early
7. `SC071` OE Late O Shortening
8. `SC074` OE Med Unstressed I Lowering1
9. `SC075` OE Med Unstressed I Lowering
10. `SC076` OE Prefix I Reduction

That ten-rule set would extend the now-contiguous late weak-tail corridor without yet jumping to the far-later `SC079+` region.
