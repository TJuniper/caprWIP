# SC042 PWGmc Surviving Bimoric O Unrounding — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `42`
- rule_name: `PWGmcSurvivingBimoricOUnrounding`
- safe computational window: `21-42`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `20`
- crossed stage: `SC020` PGmc Final Z Deletion
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `rest`
- concrete failure example: PGmc `*rástōz` yields expected OE `ræste`, but the earlier-shifted variant yields `rasta`
- interpretation: SC042 can move earlier safely through order `21`, but it cannot move earlier across SC020. The live derivation needs the SC020 material to precede this unrounding stage; if SC042 is pulled earlier than that point, the pathway that yields the attested fronted/restored output for `rest` collapses.

## Later boundary
- first later break: order `43`
- crossed stage: `SC043` Anglo Frisian Brightening
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `rest`
- concrete failure example: PGmc `*rástōz` yields expected OE `ræste`, but the later-shifted variant yields `rasta`
- interpretation: SC042 can move later only up to its current order. If it is delayed across SC043, the reciprocal relation with brightening is broken and the same `rest` derivation fails.

## Chronology statement
SC042 must follow `SC020` PGmc Final Z Deletion. If PWGmc Surviving Bimoric O Unrounding is moved before that stage, PGmc `*rástōz` yields `rasta` rather than expected OE `ræste`, so the later fronted/restored pathway never materializes. SC042 must also precede `SC043` Anglo Frisian Brightening: if the unrounding stage is delayed across brightening, the same PGmc input again surfaces as `rasta` instead of `ræste`, giving a reciprocal computational boundary with SC043.

## Caveats
Both observed boundaries are historically interpretable, because both crossed stages are `historical_sound_change` rows. This is a narrow local constraint rather than a broad instability window: each boundary produces only one newly failing row, and both sides converge on the same `rest` derivation.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
