# SC002 PGmc Gm Simplification — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `2`
- rule_name: `PGmcGmSimplification`
- safe computational window: `2-92` (earlier side start-bounded; later side non-historical)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at order 2`
- crossed stage: `start of tested historical chain`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The temporary early-rule harness begins SC002 at the left edge of the tested historical chain, immediately after the excluded support/input stage SC001 `EnglishProtoInput`. This is therefore a boundary-only computational result, not an earlier historical boundary for PGmc Gm Simplification.

## Later boundary
- first later break: order `93`
- crossed stage: `SC094` Old English Remove Stars
- crossed stage type: `orthography_surface`
- failure count: `2`
- representative failures: `dream; team`
- concrete failure example: PGmc `*dráugmaz` yields expected OE `drēam`, but the later-shifted variant yields `drēagm`
- interpretation: SC002 cannot move later across `SC094`, but this break crosses an orthography-surface support stage rather than an ordinary historical sound change. It is therefore a real computational break with non-historical status.

## Chronology statement
Current first-break evidence does **not** identify an ordinary historical first-break boundary for SC002 in either direction. The earlier search stopped immediately at the start boundary of the tested historical chain with no real break. The later search does find a real computational break at `SC094` Old English Remove Stars: if PGmc Gm Simplification is moved later than that orthography-surface support stage, PGmc `*dráugmaz` yields `drēagm` and PGmc `*táugmaz` yields `tēagm` rather than expected OE `drēam` and `tēam`. Because `SC094` is an orthography-surface support stage, however, that later break is non-historical and should not be used as an ordinary chronology constraint.

## Caveats
This card validates the computation for SC002, but the result remains boundary-only earlier and non-historical later. It should not be used to claim that PGmc Gm Simplification must stand on one side or the other of an ordinary historical sound-change boundary.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`
