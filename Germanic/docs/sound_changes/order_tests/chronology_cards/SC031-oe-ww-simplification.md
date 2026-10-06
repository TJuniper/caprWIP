# SC031 OE WW Simplification — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `31`
- rule_name: `OEWWSimplification`
- safe computational window: `14-33` (earlier side non-historical)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `2`
- representative failures: `four; hay`
- concrete failure example: PGmc `*fédwōr` yields expected OE `fēower`, but the earlier-shifted variant yields `fēowwer`; PGmc `*xáwwją` likewise yields `hēai` instead of expected `hīeġ`
- interpretation: The first real computational break for SC031 appears only when the move reaches bundled `PWGmcChanges`. This is therefore not an ordinary earlier historical first-break boundary for OE WW Simplification.

## Later boundary
- first later break: order `34`
- crossed stage: `SC034` OE Aw Long Diphthong
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `dew; hew`
- concrete failure example: PGmc `*dáwwō` yields expected OE `dēaw`, but the later-shifted variant yields `dawu`; PGmc `*xáwwaną` likewise yields `hawan` instead of expected `hēawan`
- interpretation: SC031 can move later safely through order `33`, but it cannot move later across SC034. Delaying OE WW Simplification past OE Aw Long Diphthong restores the unsimplified `aw` sequence in `dew` and `hew`.

## Chronology statement
Current first-break evidence identifies a later historical boundary for SC031 but not an earlier ordinary historical one. If OE WW Simplification is moved later than `SC034` OE Aw Long Diphthong, PGmc `*dáwwō` yields `dawu` rather than expected OE `dēaw`, and PGmc `*xáwwaną` yields `hawan` rather than `hēawan`. The earlier direction does produce a real computational break at order `13`, but that break crosses bundled `PWGmcChanges`, so it should be recorded as non-historical / runner-limited rather than as a normal chronology constraint. The later side reciprocates `SC034` earlier.

## Expanded-PWGmc supplementary note
Under the separate expanded-PWGmc profile, the earlier-side test for `SC031` no longer stops at the bundled `PWGmcChanges` boundary. Its first internal positive break appears when crossing `SC011` `PWGmc Syllabic J`, with `hay` as the representative failure (`*xáwwją` > expected OE `hīeġ`, variant `hēai`). This supplements, but does not replace, the default bundled-profile card evidence. See also the [integration policy draft](../expanded_pwgmc/expanded_pwgmc_integration_policy_draft.md), [boundary-target closure](../expanded_pwgmc/expanded_pwgmc_boundary_target_closure.md), and [phase synthesis](../expanded_pwgmc/expanded_pwgmc_phase_synthesis.md).

## Caveats
The earlier side must not be used as an ordinary must-follow claim about a specific historical stage. It records a real computational break, but only at the bundled `PWGmcChanges` boundary.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
