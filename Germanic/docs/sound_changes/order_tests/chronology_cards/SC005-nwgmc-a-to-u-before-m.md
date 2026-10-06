# SC005 NWGmc A To U Before M — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `5`
- rule_name: `PNWGmcAToUBeforeM`
- former_rule_name: `NWGmcAToUBeforeM`
- safe computational window: `4-16` (earlier side boundary-only; later side broad/far)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at SC014 (left-edge boundary; last_safe_order=4)`
- crossed stage: `SC014` NWGmc Unstressed Ai Monophthongization
- crossed stage type: `historical_sound_change`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The expanded-PWGmc first-break profile can move SC005 earlier safely to order `4`; the next earlier step crosses the SC014 head boundary and is out of range for this profile. This is therefore a boundary-only result rather than an earlier historical boundary for NWGmc A To U Before M.

## Later boundary
- first later break: order `17`
- crossed stage: `SC017` NWGmc U Lowering
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `shoulder`
- concrete failure example: PGmc `*skúldramiz` yields expected OE `sċuldrum`, but the later-shifted variant yields `sċoldrum`
- interpretation: SC005 can move later safely through order `16`, but it cannot move later across SC017. Delaying the pre-`m` raising that far forward leaves the wrong unstressed vowel in the `shoulder` derivation.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC005. The earlier search moved safely to order `4` and then stopped at the SC014 left-edge boundary with no real break, so that side remains boundary-only. The later search does find a real historical boundary at `SC017` NWGmc U Lowering: if NWGmc A To U Before M is moved later than that stage, PGmc `*skúldramiz` yields `sċoldrum` rather than expected OE `sċuldrum`. The later side is historically real, but it is broad/far rather than a tight local adjacency claim.

## Caveats
This card is one-sided in current testing. The later boundary is real but broad/far, and the historical stage label remains under review: the literature support is strongest for a morphologized pre-`m` raising in endings, while the inventory's present `NWGmc` label and the single lexical witness `shoulder` still need cautious handling.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc005.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc005_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc005_failures.tsv`
