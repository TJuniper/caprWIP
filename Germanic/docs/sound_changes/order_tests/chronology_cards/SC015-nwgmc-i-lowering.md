# SC015 NWGmc I Lowering — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `15`
- rule_name: `PNWGmcILowering`
- former_rule_name: `NWGmcILowering`
- safe computational window: `13-35` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC015 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for NWGmc I Lowering.

## Later boundary
- first later break: order `36`
- crossed stage: `SC036` OE Inter Stress Raising
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `world`
- concrete failure example: PGmc `*wír-àldu` yields expected OE `weorold`, but the later-shifted variant yields `wuruld`
- interpretation: SC015 can move later safely through order `35`, but it cannot move later across SC036. Delaying NWGmc I Lowering that far forward leaves the wrong vowel sequence in the `world` derivation.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC015. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break, so that side remains runner-limited. The later search does find a real historical boundary at `SC036` OE Inter Stress Raising: if NWGmc I Lowering is moved later than that stage, PGmc `*wír-àldu` yields `wuruld` rather than expected OE `weorold`.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but it is broad/far across `SC036` rather than a tight local adjacency claim; the earlier side must not be rewritten as a positive boundary because it stops at bundled `PWGmcChanges`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
