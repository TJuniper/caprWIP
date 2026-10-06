# SC029 OE Awj Glide Formation — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `29`
- rule_name: `OEAwwjResolution`
- safe computational window: `13-29` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC029 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for OE Awj Glide Formation.

## Later boundary
- first later break: order `30`
- crossed stage: `SC030` OE Au Fronting
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `hay; strew`
- concrete failure example: PGmc `*xáwwją` yields expected OE `hīeġ`, but the later-shifted variant yields `hauġ`; PGmc `*stráwjaną` likewise yields `strauian` instead of expected `strīeġan`
- interpretation: SC029 can move later safely through its current order, but it cannot move later across SC030. Delaying OE Awj Glide Formation past OE Au Fronting restores unfronted `au` outputs in the same two derivations already implicated by the SC030 earlier boundary.

## Chronology statement
Current first-break evidence places SC029 before `SC030` OE Au Fronting. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break, so no earlier historical boundary is currently identified. The later search does find a tight historical boundary at `SC030`: if OE Awj Glide Formation is moved later than that stage, PGmc `*xáwwją` yields `hauġ` rather than expected OE `hīeġ`, and PGmc `*stráwjaną` yields `strauian` rather than `strīeġan`. This later side reciprocates `SC030` earlier.

## Caveats
This card is one-sided in current testing because the earlier side remains runner-limited at bundled `PWGmcChanges`. The later side, however, is a tight local reciprocal boundary.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
