# SC010 PWGmc J Gemination — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `10`
- rule_name: `PWGmcJGemination`
- safe computational window: `4-10` (earlier side boundary-only; later side local reciprocal)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at SC014 (left-edge boundary; last_safe_order=4)`
- crossed stage: `SC014` NWGmc Unstressed Ai Monophthongization
- crossed stage type: `historical_sound_change`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The expanded-PWGmc first-break profile can move SC010 earlier safely to order `4`; the next earlier step crosses the SC014 head boundary and is out of range for this profile. This is therefore a boundary-only result rather than an earlier historical boundary for PWGmc J Gemination.

## Later boundary
- first later break: order `11`
- crossed stage: `SC011` PWGmc Syllabic J
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `net`
- concrete failure example: PGmc `*nátją` yields expected OE `nett`, but the later-shifted variant yields `nete`
- interpretation: SC010 can move later safely only through order `10`; it cannot move later across SC011. Delaying PWGmc J Gemination past PWGmc Syllabic J leaves the `net` derivation too light, so the later side is a tight local reciprocal boundary rather than a broad/far relation.

## Chronology statement
Current first-break evidence identifies one historically interpretable local boundary for SC010. The earlier search moved safely to order `4` and then stopped at the SC014 left-edge boundary with no real break, so that side remains boundary-only. The later search finds an immediate real boundary at `SC011` PWGmc Syllabic J: if PWGmc J Gemination is moved later than that stage, PGmc `*nátją` yields `nete` rather than expected OE `nett`. This later boundary reciprocates SC011 earlier and should be read as a local seam between the two rules.

## Caveats
This card is one-sided in current testing. The later boundary is tight and historically interpretable, but the source layer is still dominated by handbook discussion of j-gemination in general rather than by a large SC010-specific chronology literature.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc010.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc010_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc010_failures.tsv`
