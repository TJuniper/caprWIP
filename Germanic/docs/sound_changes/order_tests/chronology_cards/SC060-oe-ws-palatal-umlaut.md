# SC060 OE Ws Palatal Umlaut — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `60`
- rule_name: `OEWsPalatalUmlaut`
- safe computational window: `56-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `55`
- crossed stage: `SC055` OE I Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `might; night`
- concrete failure example: PGmc `*máxtiz` yields expected OE `miht`, but the earlier-shifted variant yields `mieht`; PGmc `*náxti` likewise yields `nieht` instead of expected `niht`
- interpretation: SC060 can move earlier safely through order `56`, but it cannot move earlier across SC055. Pulling OE Ws Palatal Umlaut ahead of OE I Umlaut introduces `ie` outcomes where the live chronology yields simple `i`.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC060 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC060 after `SC055` OE I Umlaut. If OE Ws Palatal Umlaut is moved before that stage, PGmc `*máxtiz` yields `mieht` rather than expected OE `miht`, and PGmc `*náxti` yields `nieht` rather than `niht`, because the live umlaut sequence has been displaced and the derivations over-develop into `ie` outputs. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC060.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable, but the later side is runner-bounded and must **not** be rewritten into a claim that SC060 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
