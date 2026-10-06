# SC069 OE Early O Shortening — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `69`
- rule_name: `OEEarlyOShortening`
- safe computational window: `24-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `23`
- crossed stage: `SC023` Proto-Germanic Word-Final N Loss
- crossed stage type: `historical_sound_change`
- failure count: `17`
- representative failures: `adder; earth; flask; heart; line`
- concrete failure example: PGmc `*nḗdrōn` yields expected OE `nǣdre`, but the earlier-shifted variant yields `nǣdran`; PGmc `*érθōn` likewise yields `eorþan` instead of expected `eorþe`; PGmc `*fláskōn` yields `flascan` instead of `flasce`
- interpretation: SC069 can move earlier safely through order `24`, but it cannot move earlier across SC023. Pulling OE Early O Shortening that far forward restores a broad set of final `-an` outcomes instead of the live final `-e` forms.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC069 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC069 after `SC023` Proto-Germanic Word-Final N Loss, but that earlier boundary is broad and far away rather than tightly local. If OE Early O Shortening is moved before `SC023`, PGmc `*nḗdrōn` yields `nǣdran` rather than expected OE `nǣdre`, PGmc `*érθōn` yields `eorþan` rather than `eorþe`, and PGmc `*fláskōn` yields `flascan` rather than `flasce`, alongside fourteen other newly failing rows. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC069.

## Caveats
The earlier boundary is historically real, but it should be narrated as a broad computational limit rather than as a tight local adjacency claim. The later side is runner-bounded and must **not** be turned into a must-precede claim about `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
