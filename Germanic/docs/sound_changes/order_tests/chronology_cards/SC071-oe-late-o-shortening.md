# SC071 OE Late O Shortening — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `71`
- rule_name: `OELateOShortening`
- safe computational window: `71-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `70`
- crossed stage: `SC070` OE Unstressed Fronting Early
- crossed stage type: `historical_sound_change`
- failure count: `6`
- representative failures: `bore (3sg); learn (3sg); lick (3sg); make (3sg); month`
- concrete failure example: PGmc `*búrōθi` yields expected OE `boraþ`, but the earlier-shifted variant yields `boreþ`; PGmc `*líznōθi` likewise yields `liorneþ` instead of expected `liornaþ`
- interpretation: SC071 cannot move earlier across SC070. Pulling OE Late O Shortening ahead of OE Unstressed Fronting Early creates the same six-row unstressed-vowel failure set seen when SC070 is moved too late.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC071 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC071 after `SC070` OE Unstressed Fronting Early. If OE Late O Shortening is moved before that stage, PGmc `*búrōθi` yields `boreþ` rather than expected OE `boraþ`, PGmc `*líznōθi` yields `liorneþ` rather than `liornaþ`, and four other related derivations fail in the same way. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC071.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable and directly reciprocates `SC070` later, but the later side is runner-bounded and must **not** be rewritten into a claim that SC071 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
