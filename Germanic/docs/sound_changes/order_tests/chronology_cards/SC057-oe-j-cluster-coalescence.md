# SC057 OE J Cluster Coalescence — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `57`
- rule_name: `OEJClusterCoalescence`
- safe computational window: `53-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `52`
- crossed stage: `SC052` OE Velar Palatalization
- crossed stage type: `historical_sound_change`
- failure count: `7`
- representative failures: `bow; follow; hedge; seek; singe`
- concrete failure example: PGmc `*báugijaną` yields expected OE `bīeġan`, but the earlier-shifted variant yields `bēaġan`; PGmc `*sōkijaną` likewise yields `sōċan` instead of expected `sēċan`
- interpretation: SC057 can move earlier safely through order `53`, but it cannot move earlier across SC052. Pulling OE J Cluster Coalescence ahead of OE Velar Palatalization disrupts the live fronted and palatalized outputs across a small cluster of derivations.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC057 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC057 after `SC052` OE Velar Palatalization. If OE J Cluster Coalescence is moved before that stage, PGmc `*báugijaną` yields `bēaġan` rather than expected OE `bīeġan`, and PGmc `*sōkijaną` yields `sōċan` rather than `sēċan`, because the live palatalized and fronted outcomes are no longer fed in the right order. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC057.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable, but the later side is runner-bounded and must **not** be rewritten into a claim that SC057 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
