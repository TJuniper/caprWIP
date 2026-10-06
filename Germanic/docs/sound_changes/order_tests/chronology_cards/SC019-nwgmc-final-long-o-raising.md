# SC019 NWGmc Final Long O Raising — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `19`
- rule_name: `PNWGmcFinalLongORaising`
- former_rule_name: `NWGmcFinalLongORaising`
- safe computational window: `18-19`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `17`
- crossed stage: `SC017` NWGmc U Lowering
- crossed stage type: `historical_sound_change`
- failure count: `3`
- representative failures: `nose; shovel; sorrow`
- concrete failure example: PGmc `*núsō` yields expected OE `nosu`, but the earlier-shifted variant yields `nusu`; PGmc `*skúflō` likewise yields `sċufl` instead of expected `sċofl`; PGmc `*súrgō` yields `surg` instead of expected `sorg`
- interpretation: SC019 can move earlier safely through order `18`, but it cannot move earlier across SC017. Pulling NWGmc Final Long O Raising ahead of NWGmc U Lowering restores the same wrong vocalism seen from the opposite side of the pair.

## Later boundary
- first later break: order `20`
- crossed stage: `SC020` PGmc Final Z Deletion
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `rest`
- concrete failure example: PGmc `*rástōz` yields expected OE `ræste`, but the later-shifted variant yields `rast`
- interpretation: SC019 can move later safely through its current order, but it cannot move later across SC020. Delaying NWGmc Final Long O Raising past PGmc Final Z Deletion removes the expected final vocalism from the `rest` derivation.

## Chronology statement
Current first-break evidence places SC019 after `SC017` NWGmc U Lowering and before `SC020` PGmc Final Z Deletion. If NWGmc Final Long O Raising is moved earlier than `SC017`, PGmc `*núsō` yields `nusu` rather than expected OE `nosu`, PGmc `*skúflō` yields `sċufl` rather than `sċofl`, and PGmc `*súrgō` yields `surg` rather than `sorg`. If it is moved later than `SC020`, PGmc `*rástōz` yields `rast` rather than expected `ræste`. The earlier side reciprocates `SC017` later, while the later side reciprocates the already interpreted `SC020` earlier boundary. The changed-output `rust` and `wool` rows recorded in the changes TSV show nearby instability, but they do not define the earlier boundary.

## Caveats
Both observed boundaries are historically interpretable. The earlier side should be narrated from the newly failing `nose` / `shovel` / `sorrow` rows, not from the changed-still-passing `rust` / `wool` context.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
