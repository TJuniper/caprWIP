# SC039 OE WI Combinative U Umlaut — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `39`
- rule_name: `OEWICombinativeUUmlaut`
- safe computational window: `13-39` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC039 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for OE WI Combinative U Umlaut.

## Later boundary
- first later break: order `40`
- crossed stage: `SC040` OE Med Unstressed U Lowering
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `widow`
- concrete failure example: PGmc `*wíduwōn` yields expected OE `wuduwe`, but the later-shifted variant yields `wudowe`
- interpretation: SC039 can move later safely through its current order, but it cannot move later across SC040. Delaying OE WI Combinative U Umlaut past OE Med Unstressed U Lowering leaves the wrong unstressed vowel sequence in the `widow` derivation.

## Chronology statement
Current first-break evidence identifies a later historical boundary for SC039 but no earlier historical one. If OE WI Combinative U Umlaut is moved later than `SC040` OE Med Unstressed U Lowering, PGmc `*wíduwōn` yields `wudowe` rather than expected OE `wuduwe`. The earlier direction found no real break through order `13` before the runner entered bundled `PWGmcChanges`, so this run does **not** yet identify any earlier historical boundary for SC039. The later side reciprocates `SC040` earlier.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but the earlier side is runner-bounded and must not be turned into a positive must-follow claim about bundled `PWGmcChanges`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
