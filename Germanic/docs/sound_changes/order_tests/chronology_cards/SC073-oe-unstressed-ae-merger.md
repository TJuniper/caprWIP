# SC073 OE Unstressed AE Merger — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `73`
- rule_name: `OEUnstressedAEMerger`
- safe computational window: `73-83`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `72`
- crossed stage: `SC072` OE Unstressed Long Vowel Shortening
- crossed stage type: `historical_sound_change`
- failure count: `24`
- representative failures: `adder; earth; father; find; flask`
- concrete failure example: PGmc `*nḗdrōn` yields expected OE `nǣdre`, but the earlier-shifted variant yields `nǣdræ`; PGmc `*fádēr` likewise yields `fædær` instead of expected `fæder`
- interpretation: SC073 cannot move earlier across SC072. Moving OE Unstressed AE Merger one step earlier turns a broad set of live final `-e` outputs into merged `-æ` forms.

## Later boundary
- first later break: order `84`
- crossed stage: `SC085` OE H Loss
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `toe`
- concrete failure example: PGmc `*táixōn` yields expected OE `tā`, but the later-shifted variant yields `tāæ`
- interpretation: SC073 can move later safely through order `83`, but it cannot move later across SC085. Delaying OE Unstressed AE Merger past OE H Loss leaves an extra final vowel in the `toe` derivation.

## Chronology statement
Current first-break evidence places SC073 immediately after `SC072` OE Unstressed Long Vowel Shortening and before `SC085` OE H Loss. If OE Unstressed AE Merger is moved earlier than `SC072`, PGmc `*nḗdrōn` yields `nǣdræ` rather than expected OE `nǣdre`, and PGmc `*fádēr` yields `fædær` rather than `fæder`, because the live `-e` outcomes are merged to `-æ` too early across a broad set of derivations. If SC073 is moved later than `SC085`, PGmc `*táixōn` yields `tāæ` instead of `tā`, so the live weak final outcome is lost on the later side.

## Caveats
The earlier boundary is broad, with 24 newly failing rows, and it directly reciprocates the existing SC072 later boundary. The later side is much narrower and should be keyed to `SC085` OE H Loss as recorded in the TSV even though the variant id is `later_order_84`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
