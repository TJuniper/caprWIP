# SC009 PWGmc Ij Contraction — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `9`
- rule_name: `PWGmcIjContraction`
- safe computational window: `4-31` (earlier side boundary-only; later side broad/far)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at SC014 (left-edge boundary; last_safe_order=4)`
- crossed stage: `SC014` NWGmc Unstressed Ai Monophthongization
- crossed stage type: `historical_sound_change`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The expanded-PWGmc first-break profile can move SC009 earlier safely to order `4`; the next earlier step crosses the SC014 head boundary and is out of range for this profile. This is therefore a boundary-only result rather than an earlier historical boundary for PWGmc Ij Contraction.

## Later boundary
- first later break: order `32`
- crossed stage: `SC032` OE Diphthong Leveling
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `friend`
- concrete failure example: PGmc `*fríjōndz` yields expected OE `frēond`, but the later-shifted variant yields `friund`
- interpretation: SC009 can move later safely through order `31`, but it cannot move later across SC032. Delaying PWGmc Ij Contraction that far forward leaves the wrong vowel sequence in the `friend` derivation.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC009. The earlier search moved safely to order `4` and then stopped at the SC014 left-edge boundary with no real break, so that side remains boundary-only. The later search does find a real historical boundary at `SC032` OE Diphthong Leveling: if PWGmc Ij Contraction is moved later than that stage, PGmc `*fríjōndz` yields `friund` rather than expected OE `frēond`. The later side is historically real but broad/far rather than a tight local adjacency claim.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but the lexical base remains exceptionally narrow: the `friend` family is effectively the whole historical argument, and the source tradition itself warns against broad generalization from the unique `*ijo` sequence.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc009.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc009_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc009_failures.tsv`
