# SC055 OE I Umlaut — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `55`
- rule_name: `OEIUmlaut`
- safe computational window: `53-55`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `52`
- crossed stage: `SC052` OE Velar Palatalization
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `cow; lung`
- concrete failure example: PGmc `*kūi` yields expected OE `cȳ`, but the earlier-shifted variant yields `ċȳ`; PGmc `*lúnganjō` likewise yields `lunġen` instead of expected `lungen`
- interpretation: SC055 can move earlier safely through order `53`, but it cannot move earlier across SC052. Moving OE I Umlaut ahead of OE Velar Palatalization changes the palatalization status of these outputs and replaces the live spell-outs with over-palatalized variants.

## Later boundary
- first later break: order `56`
- crossed stage: `SC056` OE Ws Palatal Diphthongization
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `gift; sheath`
- concrete failure example: PGmc `*géftiz` yields expected OE `ġift`, but the later-shifted variant yields `ġieft`; PGmc `*skáiθiz` likewise yields `sċǣþ` instead of expected `sċēaþ`
- interpretation: SC055 cannot move later beyond its current order. If OE I Umlaut is delayed across SC056, the derivations feed the following palatal diphthongization stage incorrectly and the live umlauted outcomes are replaced by the wrong diphthongal forms.

## Chronology statement
SC055 must follow `SC052` OE Velar Palatalization. If OE I Umlaut is moved before that stage, PGmc `*kūi` yields `ċȳ` rather than expected OE `cȳ`, and PGmc `*lúnganjō` yields `lunġen` rather than `lungen`, because the earlier shift changes the palatalization status of the outputs. SC055 must also precede `SC056` OE Ws Palatal Diphthongization: if OE I Umlaut is moved later than that stage, PGmc `*géftiz` yields `ġieft` instead of `ġift`, and PGmc `*skáiθiz` yields `sċǣþ` instead of `sċēaþ`, so the live umlaut relation has been displaced.

## Caveats
Both observed boundaries are historically interpretable rather than technical. SC055 also already appears as the earlier historical boundary for `SC063` OE High Vowel Apocope, so this card now forms part of a growing reciprocal chronology network rather than an isolated local result.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
