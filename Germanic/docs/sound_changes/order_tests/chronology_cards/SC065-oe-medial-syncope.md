# SC065 OE Medial Syncope — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `65`
- rule_name: `OEMedialSyncope`
- safe computational window: `13-86` (earlier side blocked; later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC065 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for OE Medial Syncope.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC065 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence does **not** yet identify a historical first-break boundary for SC065 in either tested direction. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges`, and the later search ran safely through order `86` before stopping at the current `SC087` boundary with no real break. This card therefore records a negative computational result rather than a positive chronology constraint.

## Caveats
Both sides are boundary-limited rather than historically interpretable. This card should not be used to claim that SC065 must follow any specific earlier stage or precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
