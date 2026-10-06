# SC052 OE Velar Palatalization — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `52`
- rule_name: `OEVelarPalatalization`
- safe computational window: `51-54`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `50`
- crossed stage: `SC050` Sievers Law Syncope
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `stretch`
- concrete failure example: PGmc `*strákkijaną` yields expected OE `streċċan`, but the earlier-shifted variant yields `strecċan`
- interpretation: SC052 can move earlier safely through order `51`, but it cannot move earlier across SC050. Moving OE Velar Palatalization ahead of Sievers Law Syncope disrupts the live palatal/geminate outcome in `stretch`.

## Later boundary
- first later break: order `55`
- crossed stage: `SC055` OE I Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `cow; lung`
- concrete failure example: PGmc `*kūi` yields expected OE `cȳ`, but the later-shifted variant yields `ċȳ`; PGmc `*lúnganjō` likewise yields `lunġen` instead of expected `lungen`
- interpretation: SC052 can move later safely through order `54`, but it cannot move later across SC055. Delaying velar palatalization until after OE I Umlaut changes the palatalization status of the outputs and produces over-palatalized forms.

## Chronology statement
SC052 must follow `SC050` Sievers Law Syncope. If OE Velar Palatalization is moved before that stage, PGmc `*strákkijaną` yields `strecċan` rather than expected OE `streċċan`, because the live syncope step no longer feeds the palatal/geminate output correctly. SC052 must also precede `SC055` OE I Umlaut: if it is moved later than that stage, PGmc `*kūi` yields `ċȳ` instead of `cȳ`, and PGmc `*lúnganjō` yields `lunġen` instead of `lungen`, so the live chronology that controls palatalization and umlaut has been displaced.

## Caveats
Both boundaries are narrow and historically interpretable. This card anchors SC052 between the one-sided SC050 result on the left and the already-documented SC055 relation on the right, turning those earlier findings into a clearer local network.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
