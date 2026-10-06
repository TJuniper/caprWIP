# SC075 OE Med Unstressed I Lowering — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `75`
- rule_name: `OEMedUnstressedILowering`
- safe computational window: `75-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `74`
- crossed stage: `SC074` OE Med Unstressed I Lowering1
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `shilling`
- concrete failure example: PGmc `*skíllingaz` yields expected OE `sċilling`, but the earlier-shifted variant yields `sċilleng`
- interpretation: SC075 cannot move earlier across SC074. Pulling OE Med Unstressed I Lowering ahead of OE Med Unstressed I Lowering1 lowers the medial vowel too early in the `shilling` derivation.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC075 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC075 after `SC074` OE Med Unstressed I Lowering1. If OE Med Unstressed I Lowering is moved before that stage, PGmc `*skíllingaz` yields `sċilleng` rather than expected OE `sċilling`, showing that the lowering sequence has been inverted. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC075.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable and directly reciprocates `SC074` later, but the later side is runner-bounded and must **not** be rewritten into a claim that SC075 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
