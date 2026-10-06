# SC059 OE Back Mutation — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `59`
- rule_name: `OEBackMutation`
- safe computational window: `49-76`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `48`
- crossed stage: `SC048` OE Secondary Nasalization
- crossed stage type: `historical_sound_change`
- failure count: `4`
- representative failures: `give; shear; steal; weave`
- concrete failure example: PGmc `*gébaną` yields expected OE `ġiefan`, but the earlier-shifted variant yields `ġeofan`; PGmc `*stélaną` likewise yields `steolan` instead of expected `stelan`
- interpretation: SC059 can move earlier safely through order `49`, but it cannot move earlier across SC048. Moving OE Back Mutation ahead of OE Secondary Nasalization produces back-mutated diphthongal outputs where the live chronology does not.

## Later boundary
- first later break: order `77`
- crossed stage: `SC078` OE Weak Tail Reduction
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `steal; weave`
- concrete failure example: PGmc `*stélaną` yields expected OE `stelan`, but the later-shifted variant yields `steolan`; PGmc `*wébaną` likewise yields `weofan` instead of expected `wefan`
- interpretation: SC059 can move later safely through order `76`, but it cannot move later across SC078. Delaying OE Back Mutation until after late weak-tail reduction again allows back-mutated forms to surface where the live order blocks them.

## Chronology statement
SC059 must follow `SC048` OE Secondary Nasalization. If OE Back Mutation is moved before that stage, PGmc `*gébaną` yields `ġeofan` rather than expected OE `ġiefan`, and PGmc `*stélaną` yields `steolan` rather than `stelan`, because the live chronology does not yet license those back-mutated diphthongal outputs. SC059 must also precede `SC078` OE Weak Tail Reduction: if it is moved later than that stage, PGmc `*stélaną` again yields `steolan` instead of `stelan`, and PGmc `*wébaną` yields `weofan` instead of `wefan`, so the same back-mutated outputs reappear on the later side.

## Caveats
Both boundaries are historically interpretable and fairly stable, but the same lexical pair (`steal`, `weave`) anchors the later side in both SC048 and SC078 relations. This makes SC059 a useful bridge node between the mid-OE mutation corridor and the later weak-tail zone.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
