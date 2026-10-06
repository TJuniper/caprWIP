# SC034 OE Aw Long Diphthong — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `34`
- rule_name: `OEAwLongDiphthong`
- safe computational window: `32-42`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `31`
- crossed stage: `SC031` OE WW Simplification
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `dew; hew`
- concrete failure example: PGmc `*dáwwō` yields expected OE `dēaw`, but the earlier-shifted variant yields `dawu`; PGmc `*xáwwaną` likewise yields `hawan` instead of expected `hēawan`
- interpretation: SC034 cannot move earlier across SC031. Pulling OE Aw Long Diphthong ahead of OE WW Simplification restores the unsimplified `aw` sequence in `dew` and `hew`.

## Later boundary
- first later break: order `43`
- crossed stage: `SC043` Anglo Frisian Brightening
- crossed stage type: `historical_sound_change`
- failure count: `6`
- representative failures: `dew; hew; show; show (3sg); show (iptv.2sg)`
- concrete failure example: PGmc `*skáwōjaną` yields expected OE `sċēawian`, but the later-shifted variant yields `sċawian`; PGmc `*skáwōθi` likewise yields `sċawaþ` instead of expected `sċēawaþ`; PGmc `*stráwą` yields `stræw` instead of expected `strēaw`
- interpretation: SC034 can move later safely through order `42`, but it cannot move later across SC043. Delaying OE Aw Long Diphthong past Anglo Frisian Brightening removes the expected long fronted diphthong outputs in the `aw` set.

## Chronology statement
Current first-break evidence places SC034 after `SC031` OE WW Simplification and before `SC043` Anglo Frisian Brightening. If OE Aw Long Diphthong is moved before `SC031`, PGmc `*dáwwō` yields `dawu` rather than expected OE `dēaw`, and PGmc `*xáwwaną` yields `hawan` rather than `hēawan`. If it is moved later than `SC043`, PGmc `*skáwōjaną` yields `sċawian` rather than expected `sċēawian`, PGmc `*skáwōθi` yields `sċawaþ` rather than `sċēawaþ`, and PGmc `*stráwą` yields `stræw` rather than `strēaw`, alongside three other newly failing rows. The earlier side reciprocates `SC031` later.

## Caveats
Both observed boundaries are historically interpretable. The earlier side is a tight local reciprocal relation with `SC031`; the later side is broader but still historical.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
