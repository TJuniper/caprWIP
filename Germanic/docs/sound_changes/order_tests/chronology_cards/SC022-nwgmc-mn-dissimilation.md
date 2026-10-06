# SC022 Common Germanic Mn Dissimilation — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `22`
- rule_name: `PNWGmcMnDissimilation`
- former_rule_name: `NWGmcMnDissimilation`
- safe computational window: `13-86` (earlier side runner-limited; later side boundary-limited)
- status: `first_break_complete`
- historical stage: `late Proto-Germanic / Common Germanic`, not securely
  Proto-Northwest Germanic; Fulk 2018, p. 121, §6.11; Polomé 1967,
  pp. 818--819

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC022 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for NWGmc Mn Dissimilation.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC022 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence does **not** identify a positive local historical
boundary for SC022 in either tested direction. The earlier search ran safely
down to order `13` before stopping at bundled `PWGmcChanges`, and the later
search ran safely through order `86` before stopping at the current `SC087`
boundary with no real break. This card therefore records a negative
computational result rather than a positive chronology constraint. The later
NWGmc/OE generalization and reversal of the cluster outcome are paradigmatic
developments, not evidence for a local SC022 cascade edge.

## Caveats
Both sides are boundary-limited rather than historically interpretable. This card should not be used to claim that SC022 must follow any specific earlier stage or precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
