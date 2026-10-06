# SC066 OE L Adjacent Syncope — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `66`
- rule_name: `OELAdjacentSyncope`
- safe computational window: `56-67`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `55`
- crossed stage: `SC055` OE I Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `nettle; spindle`
- concrete failure example: PGmc `*nátilōn` yields expected OE `netle`, but the earlier-shifted variant yields `nætle`; PGmc `*spénnilō` likewise yields `spenl` instead of expected `spinl`
- interpretation: SC066 can move earlier safely through order `56`, but it cannot move earlier across SC055. Pulling OE L Adjacent Syncope ahead of OE I Umlaut leaves the `nettle` and `spindle` derivations without the live umlauted vocalism.

## Later boundary
- first later break: order `68`
- crossed stage: `SC068` OE Preconsonantal Degemination
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `spindle`
- concrete failure example: PGmc `*spénnilō` yields expected OE `spinl`, but the later-shifted variant yields `spinnl`
- interpretation: SC066 can move later safely through order `67`, but it cannot move later across SC068. Delaying OE L Adjacent Syncope past OE Preconsonantal Degemination leaves the unwanted doubled consonant cluster in the `spindle` derivation.

## Chronology statement
Current first-break evidence places SC066 after `SC055` OE I Umlaut and before `SC068` OE Preconsonantal Degemination. If OE L Adjacent Syncope is moved before `SC055`, PGmc `*nátilōn` yields `nætle` rather than expected OE `netle`, and PGmc `*spénnilō` yields `spenl` rather than `spinl`; if it is moved later than `SC068`, PGmc `*spénnilō` yields `spinnl` instead of `spinl`. The later side therefore directly reciprocates the `SC068` earlier boundary.

## Caveats
Both observed boundaries are historically interpretable, but the evidence is narrower on the later side, which is currently concentrated in the single `spindle` derivation.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
