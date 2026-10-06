# SC047 OE Heavy Syllable Nasal Apocope — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `47`
- rule_name: `OEHeavySyllableNasalApocope`
- safe computational window: `35-47`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `34`
- crossed stage: `SC034` OE Aw Long Diphthong
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `straw`
- concrete failure example: PGmc `*stráwą` yields expected OE `strēaw`, but the earlier-shifted variant yields `stræw`
- interpretation: SC047 can move earlier safely through order `35`, but it cannot move earlier across SC034. Pulling heavy-syllable nasal apocope ahead of the OE Aw Long Diphthong step disrupts the live diphthongal outcome in `straw`.

## Later boundary
- first later break: order `48`
- crossed stage: `SC048` OE Secondary Nasalization
- crossed stage type: `historical_sound_change`
- failure count: `87`
- representative failures: `bake; begin; believe; bind; bore`
- concrete failure example: PGmc `*bákaną` yields expected OE `bacan`, but the later-shifted variant yields `bacen`; PGmc `*bíndaną` likewise yields `binden` instead of expected `bindan`
- interpretation: SC047 cannot move later across SC048. Delaying heavy-syllable nasal apocope until after OE Secondary Nasalization produces a very broad set of spurious `-en` outputs across the lexicon.

## Chronology statement
First-break evidence places SC047 after `SC034` OE Aw Long Diphthong and before a broad later computational boundary at `SC048` OE Secondary Nasalization. On the earlier side, if OE Heavy Syllable Nasal Apocope is moved before `SC034`, PGmc `*stráwą` yields `stræw` rather than expected OE `strēaw`, because the live diphthongal development has been short-circuited. On the later side, the evidence is much broader: if SC047 is moved later than `SC048`, PGmc `*bákaną` yields `bacen` instead of `bacan`, and PGmc `*bíndaną` yields `binden` instead of `bindan`, representing a large reciprocal `-en` failure set rather than a single-example adjacency effect.

## Caveats
Both observed boundaries are historically interpretable rather than technical. The later boundary is especially broad, with 87 newly failing rows, so it should be narrated as a large computational limit rather than as a single-example adjacency claim.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
