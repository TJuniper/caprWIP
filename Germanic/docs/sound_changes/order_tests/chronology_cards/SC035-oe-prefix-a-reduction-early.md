# SC035 OE Prefix A Reduction Early — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `35`
- rule_name: `OEPrefixAReduction`
- safe computational window: `13-42` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC035 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for OE Prefix A Reduction Early.

## Later boundary
- first later break: order `43`
- crossed stage: `SC043` Anglo Frisian Brightening
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `believe`
- concrete failure example: PGmc `*galáubijaną` yields expected OE `ġelīefan`, but the later-shifted variant yields `ġealīefan`
- interpretation: SC035 can move later safely through order `42`, but it cannot move later across SC043. Delaying OE Prefix A Reduction Early leaves an unreduced prefix vowel in the `believe` derivation.

## Chronology statement
Current first-break evidence identifies a later historical boundary for SC035 but no earlier historical one. If OE Prefix A Reduction Early is moved later than `SC043` Anglo Frisian Brightening, PGmc `*galáubijaną` yields `ġealīefan` rather than expected OE `ġelīefan`. The earlier direction found no real break through order `13` before the runner entered bundled `PWGmcChanges`, so this run does **not** yet identify any earlier historical boundary for SC035.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but the earlier side is runner-bounded and must not be turned into a positive must-follow claim about bundled `PWGmcChanges`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
