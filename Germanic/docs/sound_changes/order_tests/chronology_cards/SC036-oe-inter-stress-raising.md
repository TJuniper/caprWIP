# SC036 OE Inter Stress Raising — chronology evidence card

> **Updated by the SC004 correction.** SC004 (stressed `*ái > *ā`,
> `EAFAiMonophthongization`) now executes at cascade position 25, between SC019
> and SC036. First-break re-run (`sc004corr_first_break_sc036.tsv`) shows SC036's
> **earlier boundary is now SC004** (crossing it makes `soul` `*sáiwalō` yield
> `sāwel` instead of `sāwol`), which supersedes the former SC019 boundary recorded
> below; SC019 remains a further earlier constraint. The safe earlier window
> narrows accordingly. The later side (SC040) is unchanged.

## Position at experiment time
- order_at_experiment_time: `36`
- rule_name: `OEInterStressRaising`
- safe computational window: `20-39`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `19`
- crossed stage: `SC019` NWGmc Final Long O Raising
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `soul`
- concrete failure example: PGmc `*sáiwalō` yields expected OE `sāwol`, but the earlier-shifted variant yields `sāwel`
- interpretation: SC036 can move earlier safely through order `20`, but it cannot move earlier across SC019. Pulling OE Inter Stress Raising that far back leaves the wrong unstressed vowel in the `soul` derivation.

## Later boundary
- first later break: order `40`
- crossed stage: `SC040` OE Med Unstressed U Lowering
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `soul; world`
- concrete failure example: PGmc `*sáiwalō` yields expected OE `sāwol`, but the later-shifted variant yields `sāwul`; PGmc `*wír-àldu` likewise yields `weoruld` instead of expected `weorold`
- interpretation: SC036 can move later safely through order `39`, but it cannot move later across SC040. Delaying OE Inter Stress Raising past OE Med Unstressed U Lowering changes the expected unstressed vocalism in `soul` and `world`.

## Chronology statement
Current first-break evidence places SC036 after `SC019` NWGmc Final Long O Raising and before `SC040` OE Med Unstressed U Lowering. If OE Inter Stress Raising is moved before `SC019`, PGmc `*sáiwalō` yields `sāwel` rather than expected OE `sāwol`. If it is moved later than `SC040`, PGmc `*sáiwalō` yields `sāwul` rather than `sāwol`, and PGmc `*wír-àldu` yields `weoruld` rather than `weorold`. Both sides are historically interpretable, though the earlier side lies relatively far back across `SC019`.

## Caveats
The earlier boundary is historically real, but it is broad/far enough that it should not be narrated as a tight local adjacency claim. The later side is historically interpretable but one-sided in the current reciprocal network.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
