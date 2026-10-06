# SC081 OE J Strengthening After Front Diphthong — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `80`
- rule_name: `OEJStrengtheningAfterFrontDiphthong`
- safe computational window: `56-80`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `55`
- crossed stage: `SC055` OE I Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `strew`
- concrete failure example: PGmc `*stráwjaną` yields expected OE `strīeġan`, but the earlier-shifted variant yields `strēaġan`
- interpretation: SC081 can move earlier safely through order `56`, but it cannot move earlier across SC055. Pulling OE J Strengthening After Front Diphthong that far forward leaves the `strew` derivation with the wrong pre-strengthening vowel sequence.

## Later boundary
- first later break: order `81`
- crossed stage: `SC082` OE Intervocalic J Vocalization
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `strew`
- concrete failure example: PGmc `*stráwjaną` yields expected OE `strīeġan`, but the later-shifted variant yields `strīeian`
- interpretation: SC081 can move later safely through its current order, but it cannot move later across SC082. Delaying OE J Strengthening After Front Diphthong past OE Intervocalic J Vocalization turns the expected strengthened `ġ` outcome into vocalized `i`.

## Chronology statement
Current first-break evidence places SC081 after `SC055` OE I Umlaut and before `SC082` OE Intervocalic J Vocalization. If OE J Strengthening After Front Diphthong is moved before `SC055`, PGmc `*stráwjaną` yields `strēaġan` rather than expected OE `strīeġan`; if it is moved later than `SC082`, the same PGmc input yields `strīeian` instead of `strīeġan`. The later side therefore directly reciprocates `SC082` earlier.

## Caveats
The earlier boundary is real, but it crosses SC055 from far away and should not be narrated as a tight local adjacency claim. The later side is tighter and currently concentrated in the same `strew` derivation.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
