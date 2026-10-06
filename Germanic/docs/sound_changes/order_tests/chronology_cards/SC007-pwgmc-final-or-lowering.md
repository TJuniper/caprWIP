# SC007 PWGmc Final Or Lowering — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `7`
- rule_name: `PWGmcFinalOrLowering`
- safe computational window: `4-42` (earlier side boundary-only; later side broad/far)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at SC014 (left-edge boundary; last_safe_order=4)`
- crossed stage: `SC014` NWGmc Unstressed Ai Monophthongization
- crossed stage type: `historical_sound_change`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The expanded-PWGmc first-break profile can move SC007 earlier safely to order `4`; the next earlier step crosses the SC014 head boundary and is out of range for this profile. This is therefore a boundary-only result rather than an earlier historical boundary for PWGmc Final Or Lowering.

## Later boundary
- first later break: order `43`
- crossed stage: `SC043` Anglo Frisian Brightening
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `water`
- concrete failure example: PGmc `*wátōr` yields expected OE `wæter`, but the later-shifted variant yields `water`
- interpretation: SC007 can move later safely through order `42`, but it cannot move later across SC043. Delaying PWGmc Final Or Lowering that far forward leaves the wrong final vowel sequence in the `water` derivation.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC007. The earlier search moved safely to order `4` and then stopped at the SC014 left-edge boundary with no real break, so that side remains boundary-only. The later search does find a real historical boundary at `SC043` Anglo Frisian Brightening: if PWGmc Final Or Lowering is moved later than that stage, PGmc `*wátōr` yields `water` rather than expected OE `wæter`. The later side is historically real but broad/far rather than a tight local adjacency claim.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but it is broad/far and the underlying source base remains narrowly tied to the `four` and `water` families rather than to a large lexical class.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc007.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc007_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc007_failures.tsv`
