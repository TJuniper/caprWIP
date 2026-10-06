# SC027 NWGmc Nasal Spirant Loss — chronology evidence card

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
- order_at_experiment_time: `27`
- rule_name: `EAFNasalSpirantLoss`
- former_rule_name: `NWGmcNasalSpirantLoss`
- safe computational window: `27-86` (later side boundary-limited)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `26`
- crossed stage: `SC026` NWGmc Nasal Spirant Lengthening
- crossed stage type: `historical_sound_change`
- failure count: `3`
- representative failures: `fist; goose; youth`
- concrete failure example: PGmc `*fúnxstiz` yields expected OE `fȳst`, but the earlier-shifted variant yields `fyst`; PGmc `*gánsz` likewise yields `ġeas` instead of expected `gōs`; PGmc `*júgunθ` yields `ġeogoþ` instead of expected `ġeoguþ`
- interpretation: SC027 cannot move earlier across SC026. Pulling NWGmc Nasal Spirant Loss ahead of NWGmc Nasal Spirant Lengthening restores the same wrong vocalism seen from the opposite side of the pair.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC027 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC027 after `SC026` NWGmc Nasal Spirant Lengthening. If NWGmc Nasal Spirant Loss is moved earlier than that stage, PGmc `*fúnxstiz` yields `fyst` rather than expected OE `fȳst`, PGmc `*gánsz` yields `ġeas` rather than `gōs`, and PGmc `*júgunθ` yields `ġeogoþ` rather than `ġeoguþ`. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC027.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable and reciprocates `SC026` later, but the later side is a no-break-before-boundary result and must **not** be rewritten into a claim that SC027 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
