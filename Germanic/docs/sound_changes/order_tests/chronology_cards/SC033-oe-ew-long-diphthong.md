# SC033 OE Ew Long Diphthong — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `33`
- rule_name: `OEEwLongDiphthong`
- safe computational window: `14-43` (earlier side non-historical)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `1`
- representative failures: `four`
- concrete failure example: PGmc `*fédwōr` yields expected OE `fēower`, but the earlier-shifted variant yields `feower`
- interpretation: The first real computational break for SC033 appears only when the move reaches bundled `PWGmcChanges`. This is therefore not an ordinary earlier historical first-break boundary for OE Ew Long Diphthong.

## Later boundary
- first later break: order `44`
- crossed stage: `SC044` OE Breaking
- crossed stage type: `historical_sound_change`
- failure count: `3`
- representative failures: `chew; four; knee`
- concrete failure example: PGmc `*kéwwaną` yields expected OE `ċēowan`, but the later-shifted variant yields `ċeowan`; PGmc `*fédwōr` likewise yields `feower` instead of expected `fēower`; PGmc `*knéwą` yields `cneow` instead of `cnēow`
- interpretation: SC033 can move later safely through order `43`, but it cannot move later across SC044. Delaying OE Ew Long Diphthong past OE Breaking removes the long-diphthong outputs expected in `chew`, `four`, and `knee`.

## Chronology statement
Current first-break evidence identifies a later historical boundary for SC033 but not an earlier ordinary historical one. If OE Ew Long Diphthong is moved later than `SC044` OE Breaking, PGmc `*kéwwaną` yields `ċeowan` rather than expected OE `ċēowan`, PGmc `*fédwōr` yields `feower` rather than `fēower`, and PGmc `*knéwą` yields `cneow` rather than `cnēow`. The earlier direction does produce a computational break at order `13`, but that break crosses bundled `PWGmcChanges`, so it should be recorded as non-historical rather than as a normal chronology constraint.

## Expanded-PWGmc supplementary note
Under the separate expanded-PWGmc profile, the earlier-side test for `SC033` no longer stops at the bundled `PWGmcChanges` boundary. Its first internal positive break appears when crossing `SC008` `PWGmc Coronal W Assimilation`, with `four` as the representative failure (`*fédwōr` > expected OE `fēower`, variant `feower`). This supplements, but does not replace, the default bundled-profile card evidence. See also the [integration policy draft](../expanded_pwgmc/expanded_pwgmc_integration_policy_draft.md), [boundary-target closure](../expanded_pwgmc/expanded_pwgmc_boundary_target_closure.md), and [phase synthesis](../expanded_pwgmc/expanded_pwgmc_phase_synthesis.md).

## Caveats
The later side is historically real, but it is broad and far across `SC044` rather than a tight local adjacency claim. The earlier side is non-historical because it only appears when the runner enters bundled `PWGmcChanges`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
