# SC049 PGmc B Allophony — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `49`
- rule_name: `PGmcBAllophony`
- safe computational window: `38-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `37`
- crossed stage: `SC037` OE Compound Linking Syncope
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `rainbow`
- concrete failure example: PGmc `*régna-bùgô` yields expected OE `reġnboga`, but the earlier-shifted variant yields `reġnfoga`
- interpretation: SC049 can move earlier safely through order `38`, but it cannot move earlier across SC037. Pulling PGmc B Allophony ahead of OE Compound Linking Syncope disrupts the voiced compound outcome in `rainbow`.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC049 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC049 after `SC037` OE Compound Linking Syncope. If PGmc B Allophony is moved before that stage, PGmc `*régna-bùgô` yields `reġnfoga` rather than expected OE `reġnboga`, because the live compound-linked environment no longer feeds the voiced allophone at the right point in the cascade. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC049.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable, but the later side is runner-bounded and must **not** be rewritten into a claim that SC049 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
