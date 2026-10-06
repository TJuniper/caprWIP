# SC056 OE Ws Palatal Diphthongization — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `56`
- rule_name: `OEWsPalatalDiphthongization`
- safe computational window: `56-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `55`
- crossed stage: `SC055` OE I Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `gift; sheath`
- concrete failure example: PGmc `*géftiz` yields expected OE `ġift`, but the earlier-shifted variant yields `ġieft`; PGmc `*skáiθiz` likewise yields `sċǣþ` instead of expected `sċēaþ`
- interpretation: SC056 cannot move earlier across SC055. Pulling OE Ws Palatal Diphthongization ahead of OE I Umlaut disrupts the live umlauted outcomes in these derivations.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC056 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence shows that SC056 must follow `SC055` OE I Umlaut. If OE Ws Palatal Diphthongization is moved before that stage, PGmc `*géftiz` yields `ġieft` rather than expected OE `ġift`, and PGmc `*skáiθiz` yields `sċǣþ` rather than `sċēaþ`, because the live umlaut relation has not yet been established. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC056.

## Caveats
The later side must be handled carefully in narrative synthesis. This card supports an earlier boundary across SC055, but it must **not** be rewritten into a claim that SC056 must precede SC087 OE R Metathesis.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
