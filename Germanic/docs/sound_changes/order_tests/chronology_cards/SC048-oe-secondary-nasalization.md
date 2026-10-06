# SC048 OE Secondary Nasalization — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `48`
- rule_name: `OESecondaryNasalization`
- safe computational window: `48-58`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `47`
- crossed stage: `SC047` OE Heavy Syllable Nasal Apocope
- crossed stage type: `historical_sound_change`
- failure count: `87`
- representative failures: `bake; begin; believe; bind; bore`
- concrete failure example: PGmc `*bákaną` yields expected OE `bacan`, but the earlier-shifted variant yields `bacen`; PGmc `*bíndaną` likewise yields `binden` instead of expected `bindan`
- interpretation: SC048 cannot move earlier across SC047. If OE Secondary Nasalization is moved before OE Heavy Syllable Nasal Apocope, the same broad set of spurious `-en` outputs appears that already marks the reciprocal SC047 later boundary.

## Later boundary
- first later break: order `59`
- crossed stage: `SC059` OE Back Mutation
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `steal; weave`
- concrete failure example: PGmc `*stélaną` yields expected OE `stelan`, but the later-shifted variant yields `steolan`; PGmc `*wébaną` likewise yields `weofan` instead of expected `wefan`
- interpretation: SC048 can move later safely through order `58`, but it cannot move later across SC059. Delaying OE Secondary Nasalization beyond OE Back Mutation allows back-mutated diphthongal outcomes to appear where the live order suppresses them.

## Chronology statement
First-break evidence places SC048 after a broad earlier computational boundary at `SC047` OE Heavy Syllable Nasal Apocope and before `SC059` OE Back Mutation. If OE Secondary Nasalization is moved before `SC047`, PGmc `*bákaną` yields `bacen` rather than expected OE `bacan`, and PGmc `*bíndaną` yields `binden` rather than `bindan`, because the live order no longer removes a broad reciprocal class of spurious `-en` outputs. The later side is tighter: if SC048 is moved later than `SC059`, PGmc `*stélaną` yields `steolan` instead of `stelan`, and PGmc `*wébaną` yields `weofan` instead of `wefan`, so the live chronology that blocks those back-mutated forms is lost.

## Caveats
The earlier boundary is directly reciprocal with SC047 later and carries the same very broad 87-row failure set. The later boundary is much narrower, so SC048 combines one tight local relation to SC059 with one very broad reciprocal relation to SC047.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
