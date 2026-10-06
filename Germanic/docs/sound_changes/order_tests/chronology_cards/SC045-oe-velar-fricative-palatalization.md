# SC045 OE Velar Fricative Palatalization — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `45`
- rule_name: `OEVelarFricativePalatalization`
- safe computational window: `45-59`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `44`
- crossed stage: `SC044` OE Breaking
- crossed stage type: `historical_sound_change`
- failure count: `12`
- representative failures: `fee; fight; flax; knight; laugh`
- concrete failure example: PGmc `*féxu` yields expected OE `feoh`, but the earlier-shifted variant yields `fehu`; PGmc `*féxtaną` likewise yields `fehtan` instead of expected `feohtan`
- interpretation: SC045 cannot move earlier across SC044. If OE Velar Fricative Palatalization is pulled ahead of OE Breaking, the live broken outputs are lost and the derivations surface with unbroken vowels.

## Later boundary
- first later break: order `60`
- crossed stage: `SC060` OE Ws Palatal Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `six`
- concrete failure example: PGmc `*séxs` yields expected OE `six`, but the later-shifted variant yields `sihs`
- interpretation: SC045 can move later safely through order `59`, but it cannot move later across SC060. Delaying velar fricative palatalization past OE Ws Palatal Umlaut disrupts the live derivation of `six`.

## Chronology statement
SC045 must follow `SC044` OE Breaking. If OE Velar Fricative Palatalization is moved before breaking, PGmc `*féxu` yields `fehu` rather than expected OE `feoh`, and PGmc `*féxtaną` yields `fehtan` rather than `feohtan`, because the live broken outputs are no longer in place when palatalization runs. SC045 must also precede `SC060` OE Ws Palatal Umlaut: if it is moved later than that stage, PGmc `*séxs` yields `sihs` instead of `six`, so the live ordering that produces the attested consonant-vowel shape is lost.

## Caveats
Both observed boundaries are historically interpretable rather than technical. The earlier side is directly reciprocal with the existing SC044 later boundary, so this card confirms that SC044 and SC045 form a tight local chronology constraint.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
