# SC054 OE W Loss Before I — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `54`
- rule_name: `OEWLossBeforeI`
- safe computational window: `21-62`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `20`
- crossed stage: `SC020` PGmc Final Z Deletion
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `sea`
- concrete failure example: PGmc `*sáiwiz` yields expected OE `sǣ`, but the earlier-shifted variant yields `sǣw`
- interpretation: SC054 can move earlier safely through order `21`, but it cannot move earlier across SC020. Pulling OE W Loss Before I ahead of PGmc Final Z Deletion leaves the glide standing in the `sea` derivation where the live order removes it.

## Later boundary
- first later break: order `63`
- crossed stage: `SC063` OE High Vowel Apocope
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `sea`
- concrete failure example: PGmc `*sáiwiz` yields expected OE `sǣ`, but the later-shifted variant again yields `sǣw`
- interpretation: SC054 can move later safely through order `62`, but it cannot move later across SC063. Delaying OE W Loss Before I until after OE High Vowel Apocope again preserves the glide too long in the same derivation.

## Chronology statement
Current first-break evidence places SC054 after `SC020` PGmc Final Z Deletion and before `SC063` OE High Vowel Apocope. If OE W Loss Before I is moved before `SC020`, PGmc `*sáiwiz` yields `sǣw` rather than expected OE `sǣ`, because the glide survives too early in the derivation. If the same rule is moved later than `SC063`, the same PGmc input again yields `sǣw` instead of `sǣ`, so the live deletion window has been missed on the later side as well.

## Caveats
Both observed boundaries are historically interpretable, but the evidence is narrow: both sides are currently defined by the same `sea` derivation. This card is therefore locally useful without yet forming a reciprocal pair in the current card network.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
