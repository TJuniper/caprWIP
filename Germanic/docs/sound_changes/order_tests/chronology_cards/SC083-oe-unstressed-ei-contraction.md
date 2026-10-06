# SC083 OE Unstressed EI Contraction — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `82`
- rule_name: `OEUnstressedEIContraction`
- safe computational window: `82-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `81`
- crossed stage: `SC082` OE Intervocalic J Vocalization
- crossed stage type: `historical_sound_change`
- failure count: `8`
- representative failures: `bore; handle; learn; lick; make`
- concrete failure example: PGmc `*búrōjaną` yields expected OE `borian`, but the earlier-shifted variant yields `boreian`; PGmc `*líznōjaną` likewise yields `liorneian` instead of expected `liornian`; PGmc `*líkkōjaną` yields `licceian` instead of `liccian`
- interpretation: SC083 cannot move earlier across SC082. Pulling OE Unstressed EI Contraction ahead of OE Intervocalic J Vocalization preserves an extra `ei`-like sequence where the live chronology expects contracted `-ian` outcomes.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC083 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC083 after `SC082` OE Intervocalic J Vocalization. If OE Unstressed EI Contraction is moved before that stage, PGmc `*búrōjaną` yields `boreian` rather than expected OE `borian`, PGmc `*líznōjaną` yields `liorneian` rather than `liornian`, and PGmc `*líkkōjaną` yields `licceian` rather than `liccian`, alongside five other newly failing rows. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC083.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable and directly reciprocates `SC082` later, but the later side is runner-bounded and must **not** be rewritten into a claim that SC083 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
