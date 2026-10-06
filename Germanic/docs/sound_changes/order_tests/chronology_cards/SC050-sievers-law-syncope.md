# SC050 Sievers Law Syncope — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `50`
- rule_name: `SieversLawSyncope`
- safe computational window: `13-51` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC050 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for Sievers Law Syncope.

## Later boundary
- first later break: order `52`
- crossed stage: `SC052` OE Velar Palatalization
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `stretch`
- concrete failure example: PGmc `*strákkijaną` yields expected OE `streċċan`, but the later-shifted variant yields `strecċan`
- interpretation: SC050 can move later safely through order `51`, but it cannot move later across SC052. Delaying Sievers Law Syncope until after OE Velar Palatalization disrupts the palatal/geminate outcome in the `stretch` derivation.

## Chronology statement
Current first-break evidence does not yet identify an earlier historical boundary for SC050: the runner found no earlier real break down to order `13`, then stopped at the bundled `PWGmcChanges` boundary. The later side does show a local chronology constraint: if Sievers Law Syncope is moved after `SC052` OE Velar Palatalization, PGmc `*strákkijaną` yields `strecċan` instead of expected OE `streċċan`, so the live ordering is required for the attested palatal/geminate outcome.

## Caveats
The earlier side is bounded by the current runner limitation, not by a detected historical break. This card therefore supports a later boundary for SC050, but it should not yet be used to claim that the rule must follow any specific earlier historical stage.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
