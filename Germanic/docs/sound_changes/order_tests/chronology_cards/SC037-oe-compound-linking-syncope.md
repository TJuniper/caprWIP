# SC037 OE Compound Linking Syncope — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `37`
- rule_name: `OECompoundLinkingSyncope`
- safe computational window: `13-37` (earlier side runner-bounded; later side non-historical)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC037 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for OE Compound Linking Syncope.

## Later boundary
- first later break: order `38`
- crossed stage: `SC038` OE Strip Secondary Stress
- crossed stage type: `technical_marker`
- failure count: `1`
- representative failures: `rainbow`
- concrete failure example: PGmc `*régna-bùgô` yields expected OE `reġnboga`, but the later-shifted variant yields `reġnefoga`
- interpretation: SC037 cannot move later across `SC038`, but this break crosses a technical marker rather than an ordinary historical sound change. It is therefore a real computational break with non-historical status.

## Chronology statement
Current first-break evidence does **not** yet identify an ordinary historical first-break boundary for SC037 in either direction. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break. The later search does find a real computational break at `SC038` OE Strip Secondary Stress: if OE Compound Linking Syncope is moved later than that technical marker, PGmc `*régna-bùgô` yields `reġnefoga` rather than expected OE `reġnboga`. Because `SC038` is a technical marker, however, that later break should be recorded as non-historical / technical-marker evidence rather than as a normal chronology constraint.

## Caveats
This card records a real computational later break, but not an ordinary historical adjacency. Neither side should currently be used to claim that SC037 must stand on one side or the other of a normal historical sound-change boundary.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
