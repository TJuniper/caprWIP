# SC087 OE R Metathesis — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `86`
- rule_name: `OERMetathesis`
- safe computational window: `45-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `44`
- crossed stage: `SC044` OE Breaking
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `burst`
- concrete failure example: PGmc `*bréstaną` yields expected OE `berstan`, but the earlier-shifted variant yields `beorstan`
- interpretation: SC087 can move earlier safely through order `45`, but it cannot move earlier across SC044. Pulling OE R Metathesis that far forward lets the `burst` derivation break in a way that shows the relation is real but far from local.

## Later boundary
- first later break: `none found beyond current order 86 before runner limit`
- crossed stage: `none beyond current order`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner limit`
- interpretation: The current runner found no later real break beyond current order `86`, but the search also ends there. This is therefore not a detected later historical boundary for OE R Metathesis.

## Chronology statement
Current first-break evidence places SC087 after `SC044` OE Breaking, but that earlier boundary is far away rather than tightly local. If OE R Metathesis is moved before `SC044`, PGmc `*bréstaną` yields `beorstan` rather than expected OE `berstan`. The later direction found no real break beyond current order `86` before the runner limit, so this run does **not** identify any later historical boundary for SC087.

## Caveats
The earlier boundary is historically real, but it should be narrated as a broad/far computational limit rather than as a tight local adjacency claim. The later side is bounded by the current runner limit and must not be turned into a positive must-follow or must-precede statement.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
