# SC070 OE Unstressed Fronting Early — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `70`
- rule_name: `OEUnstressedFrontingEarly`
- safe computational window: `53-70`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `52`
- crossed stage: `SC052` OE Velar Palatalization
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `lung`
- concrete failure example: PGmc `*lúnganjō` yields expected OE `lungen`, but the earlier-shifted variant yields `lunġen`
- interpretation: SC070 can move earlier safely through order `53`, but it cannot move earlier across SC052. Pulling OE Unstressed Fronting Early ahead of OE Velar Palatalization lets the `lung` derivation pick up the wrong palatalized consonant outcome.

## Later boundary
- first later break: order `71`
- crossed stage: `SC071` OE Late O Shortening
- crossed stage type: `historical_sound_change`
- failure count: `6`
- representative failures: `bore (3sg); learn (3sg); lick (3sg); make (3sg); month`
- concrete failure example: PGmc `*búrōθi` yields expected OE `boraþ`, but the later-shifted variant yields `boreþ`; PGmc `*mḗnōθz` likewise yields `mōneþ` instead of expected `mōnaþ`
- interpretation: SC070 can move later safely through its current order, but it cannot move later across SC071. Delaying OE Unstressed Fronting Early past OE Late O Shortening produces the wrong unstressed vowel in a six-row set of verbal and nominal endings.

## Chronology statement
Current first-break evidence places SC070 after `SC052` OE Velar Palatalization and before `SC071` OE Late O Shortening. If OE Unstressed Fronting Early is moved before `SC052`, PGmc `*lúnganjō` yields `lunġen` rather than expected OE `lungen`; if it is moved later than `SC071`, PGmc `*búrōθi` yields `boreþ` rather than `boraþ`, and PGmc `*mḗnōθz` yields `mōneþ` rather than `mōnaþ`. The later side therefore directly reciprocates `SC071` earlier.

## Caveats
Both observed boundaries are historically interpretable, but the earlier side is currently narrow and concentrated in `lung`, whereas the later side is broader and concentrated in a related six-row unstressed-vowel set.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
