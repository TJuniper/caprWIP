# SC078 OE Weak Tail Reduction — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `77`
- rule_name: `OEWeakTailReduction`
- safe computational window: `71-84`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `70`
- crossed stage: `SC070` OE Unstressed Fronting Early
- crossed stage type: `historical_sound_change`
- failure count: `87`
- representative failures: `bake; begin; believe; bind; bore`
- concrete failure example: PGmc `*bákaną` yields expected OE `bacan`, but the earlier-shifted variant yields `bacen`; PGmc `*bíndaną` likewise yields `binden` instead of expected `bindan`
- interpretation: SC078 can move earlier safely through order `71`, but it cannot move earlier across SC070. Moving weak-tail reduction too early produces a very broad class of spurious `-en` outputs.

## Later boundary
- first later break: order `85`
- crossed stage: `SC086` OE Contraction
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `flee; slay`
- concrete failure example: PGmc `*fléuxaną` yields expected OE `flēon`, but the later-shifted variant yields `flēoan`; PGmc `*sláxaną` likewise yields `sleaan` instead of expected `slēan`
- interpretation: SC078 can move later safely through order `84`, but it cannot move later across SC086. Delaying weak-tail reduction until after OE Contraction leaves extra vowels in forms that the live order has already reduced.

## Chronology statement
First-break evidence places SC078 after a broad earlier computational boundary at `SC070` OE Unstressed Fronting Early and before `SC086` OE Contraction. If OE Weak Tail Reduction is moved before `SC070`, PGmc `*bákaną` yields `bacen` rather than expected OE `bacan`, and PGmc `*bíndaną` yields `binden` rather than `bindan`, because the live chronology no longer prevents a broad class of spurious `-en` outputs. The later side is much narrower: if SC078 is moved later than `SC086`, PGmc `*fléuxaną` yields `flēoan` instead of `flēon`, and PGmc `*sláxaną` yields `sleaan` instead of `slēan`, so the extra vowels that the live weak-tail reduction removes survive too long.

## Caveats
The earlier boundary is very broad, with 87 newly failing rows, so it should be narrated carefully as a large computational limit rather than as a narrow local adjacency claim. The later boundary is much tighter and easier to interpret directly.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
