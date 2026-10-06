# SC044 OE Breaking — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `44`
- rule_name: `OEBreaking`
- safe computational window: `44-44`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `43`
- crossed stage: `SC043` Anglo Frisian Brightening
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `slay`
- concrete failure example: PGmc `*sláxaną` yields expected OE `slēan`, but the earlier-shifted variant yields `sleaan | slēaan`
- interpretation: SC044 cannot move earlier across SC043. Breaking needs the fronted output created by Anglo-Frisian Brightening; if it is moved before that stage, the derivation overproduces an uncontracted broken sequence instead of the attested outcome.

## Later boundary
- first later break: order `45`
- crossed stage: `SC045` OE Velar Fricative Palatalization
- crossed stage type: `historical_sound_change`
- failure count: `12`
- representative failures: `fee; fight; flax; knight; laugh`
- concrete failure example: PGmc `*féxu` yields expected OE `feoh`, but the later-shifted variant yields `fehu`; PGmc `*féxtaną` likewise yields `fehtan` instead of expected `feohtan`
- interpretation: SC044 cannot move later across SC045. When breaking is delayed until after velar fricative palatalization, the live `eo`-type outcomes are lost and a cluster of velar/fricative derivations surfaces with unbroken vowels.

## Chronology statement
SC044 must follow `SC043` Anglo Frisian Brightening. If OE Breaking is moved before brightening, PGmc `*sláxaną` yields `sleaan | slēaan` rather than expected OE `slēan`, because breaking is no longer acting on the properly fronted input that the live order supplies. SC044 must also precede `SC045` OE Velar Fricative Palatalization: if breaking is moved later than that stage, PGmc `*féxu` yields `fehu` instead of `feoh`, and PGmc `*féxtaną` yields `fehtan` instead of `feohtan`, showing that the breaking step has missed the velar/fricative environment it must feed in the live chronology.

## Caveats
Both observed boundaries are historically interpretable, not technical, because both crossed stages are `historical_sound_change` rows. Unlike SC041 and SC042, SC044 is tightly constrained at its current position: it breaks immediately in both directions, and the later move across SC045 produces a broader cluster of twelve real failures in velar/fricative contexts.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
