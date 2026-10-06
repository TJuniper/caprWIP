# SC032 OE Diphthong Leveling — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `32`
- rule_name: `OEDiphthongLeveling`
- safe computational window: `31-39`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `30`
- crossed stage: `SC030` OE Au Fronting
- crossed stage type: `historical_sound_change`
- failure count: `18`
- representative failures: `believe; bow; bread; dream; flea`
- concrete failure example: PGmc `*galáubijaną` yields expected OE `ġelīefan`, but the earlier-shifted variant yields `+?` (no output); PGmc `*báug` likewise yields no output instead of expected `bēag`; PGmc `*bráudą` yields no output instead of expected `brēad`
- interpretation: SC032 cannot move earlier across SC030. Pulling OE Diphthong Leveling ahead of OE Au Fronting causes a large set of derivations to fail outright rather than to yield alternate surface reflexes.

## Later boundary
- first later break: order `40`
- crossed stage: `SC040` OE Med Unstressed U Lowering
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `head`
- concrete failure example: PGmc `*xáubudą` yields expected OE `hēafod`, but the later-shifted variant yields `hēafud`
- interpretation: SC032 cannot move later across SC040. Delaying OE Diphthong Leveling past OE Med Unstressed U Lowering leaves the wrong unstressed vowel in the `head` derivation.

## Chronology statement
Current first-break evidence places SC032 after `SC030` OE Au Fronting and before `SC040` OE Med Unstressed U Lowering. If OE Diphthong Leveling is moved before `SC030`, PGmc `*galáubijaną`, `*báug`, `*bráudą`, and fifteen other derivations fail to produce output at all (`+?`) instead of yielding their expected Old English forms. If it is moved later than `SC040`, PGmc `*xáubudą` yields `hēafud` rather than expected OE `hēafod`. The earlier side therefore reciprocates `SC030` later.

## Caveats
The earlier failure set should be narrated as no-output / failed derivations, not as a cluster of surface OE alternatives. The later side is historically real but one-sided in the current reciprocal network.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
