# SC086 OE Contraction — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `85`
- rule_name: `OEContraction`
- safe computational window: `85-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `84`
- crossed stage: `SC085` OE H Loss
- crossed stage type: `historical_sound_change`
- failure count: `4`
- representative failures: `flee; slay; ten; toe`
- concrete failure example: PGmc `*fléuxaną` yields expected OE `flēon`, but the earlier-shifted variant yields `flēoan`; PGmc `*sláxaną` likewise yields `sleaan` instead of expected `slēan`; PGmc `*téxun` yields `teoon` instead of `tēon`; PGmc `*táixōn` yields `tāe` instead of `tā`
- interpretation: SC086 cannot move earlier across SC085. Pulling OE Contraction ahead of OE H Loss reproduces the same four-row over-long vocalic set seen when SC085 is moved too late.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC086 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC086 after `SC085` OE H Loss. If OE Contraction is moved before that stage, PGmc `*fléuxaną` yields `flēoan` rather than expected OE `flēon`, PGmc `*sláxaną` yields `sleaan` rather than `slēan`, PGmc `*téxun` yields `teoon` rather than `tēon`, and PGmc `*táixōn` yields `tāe` rather than `tā`. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC086.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable and directly reciprocates `SC085` later, but the later side is runner-bounded and must **not** be rewritten into a claim that SC086 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
