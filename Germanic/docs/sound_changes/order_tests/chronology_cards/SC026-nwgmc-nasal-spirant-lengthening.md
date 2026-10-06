# SC026 NWGmc Nasal Spirant Lengthening — chronology evidence card

> **Superseded in part.** See
> `Germanic/docs/sound_changes/audits/sc026-sc027-nasal-spirant-adjudication.md`.
> `fist` has been withdrawn from this witness set: its nasal loss is the
> pan-Germanic change before \*x (SC103 `PGmcNasalLossBeforeX`), not the North
> Sea Germanic nasal-spirant law. The surviving witnesses are `goose` and
> `youth`. The reciprocal SC026/SC027 relation recorded here is an **executable
> dependency** — SC026 must read the nasal that SC027 deletes — and is not a
> demonstrated historical relative chronology; the two rules implement one
> historical sound change.


## Position at experiment time
- order_at_experiment_time: `26`
- rule_name: `EAFNasalSpirantLengthening`
- former_rule_name: `NWGmcNasalSpirantLengthening`
- safe computational window: `13-26` (earlier side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC026 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for NWGmc Nasal Spirant Lengthening.

## Later boundary
- first later break: order `27`
- crossed stage: `SC027` NWGmc Nasal Spirant Loss
- crossed stage type: `historical_sound_change`
- failure count: `3`
- representative failures: `fist; goose; youth`
- concrete failure example: PGmc `*fúnxstiz` yields expected OE `fȳst`, but the later-shifted variant yields `fyst`; PGmc `*gánsz` likewise yields `ġeas` instead of expected `gōs`; PGmc `*júgunθ` yields `ġeogoþ` instead of expected `ġeoguþ`
- interpretation: SC026 can move later safely through its current order, but it cannot move later across SC027. Delaying NWGmc Nasal Spirant Lengthening past NWGmc Nasal Spirant Loss restores the wrong vocalism in the shared nasal-spirant failure set.

## Chronology statement
Current first-break evidence places SC026 before `SC027` NWGmc Nasal Spirant Loss. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges` with no real break, so no earlier historical boundary is currently identified. The later search does find a tight historical boundary at `SC027`: if NWGmc Nasal Spirant Lengthening is moved later than that stage, PGmc `*fúnxstiz` yields `fyst` rather than expected OE `fȳst`, PGmc `*gánsz` yields `ġeas` rather than `gōs`, and PGmc `*júgunθ` yields `ġeogoþ` rather than `ġeoguþ`. This later side reciprocates `SC027` earlier.

## Caveats
This card is one-sided in current testing because the earlier side remains runner-limited at bundled `PWGmcChanges`. The later side, however, is a tight local reciprocal boundary.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
