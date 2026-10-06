# SC072 OE Unstressed Long Vowel Shortening — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `72`
- rule_name: `OEUnstressedLongVowelShortening`
- safe computational window: `65-72`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `64`
- crossed stage: `SC064` NWGmc In Stem N Loss
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `fright`
- concrete failure example: PGmc `*fúrxtīnaz` yields expected OE `fyrhte`, but the earlier-shifted variant yields `fyrhten`
- interpretation: SC072 can move earlier safely through order `65`, but it cannot move earlier across SC064. Pulling OE Unstressed Long Vowel Shortening ahead of NWGmc In Stem N Loss retains an extra nasal segment in the live `fright` derivation.

## Later boundary
- first later break: order `73`
- crossed stage: `SC073` OE Unstressed AE Merger
- crossed stage type: `historical_sound_change`
- failure count: `24`
- representative failures: `adder; earth; father; find; flask`
- concrete failure example: PGmc `*nḗdrōn` yields expected OE `nǣdre`, but the later-shifted variant yields `nǣdræ`; PGmc `*fádēr` likewise yields `fædær` instead of expected `fæder`
- interpretation: SC072 cannot move later across SC073. Delaying unstressed long-vowel shortening until after the unstressed `æ` merger turns a large set of final `-e` outputs into `-æ` forms.

## Chronology statement
SC072 must follow `SC064` NWGmc In Stem N Loss. If OE Unstressed Long Vowel Shortening is moved before that stage, PGmc `*fúrxtīnaz` yields `fyrhten` rather than expected OE `fyrhte`, because the live chronology has not yet removed the nasal material that should disappear before the final weak-vowel outcome stabilizes. SC072 must also precede `SC073` OE Unstressed AE Merger: if it is moved later than that stage, PGmc `*nḗdrōn` yields `nǣdræ` instead of `nǣdre`, and PGmc `*fádēr` yields `fædær` instead of `fæder`, so the live `-e` outcomes are replaced by merged `-æ` forms.

## Caveats
Both observed boundaries are historically interpretable rather than technical. SC072 is also already the later historical boundary for `SC063` OE High Vowel Apocope, so this card extends the chronology network outward from the SC063 pilot.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
