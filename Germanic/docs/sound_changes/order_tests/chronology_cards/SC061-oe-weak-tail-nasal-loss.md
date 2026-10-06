# SC061 OE Weak Tail Nasal Loss — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `61`
- rule_name: `OEWeakTailNasalLoss`
- safe computational window: `24-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `23`
- crossed stage: `SC023` Proto-Germanic Word-Final N Loss
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `do`
- concrete failure example: PGmc `*dōną` yields expected OE `dōn`, but the earlier-shifted variant yields no output (`+?` in the TSV)
- interpretation: SC061 can move earlier safely through order `24`, but it cannot move earlier across SC023. Pulling OE Weak Tail Nasal Loss ahead of Proto-Germanic Word-Final N Loss collapses the `do` derivation instead of preserving the live OE form.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC061 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC061 after `SC023` Proto-Germanic Word-Final N Loss. If OE Weak Tail Nasal Loss is moved before that stage, PGmc `*dōną` no longer yields expected OE `dōn`, and the variant row records no output at all (`+?`), showing that the live weak-tail sequence has been disrupted. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC061.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable, but the later side is runner-bounded and must **not** be rewritten into a claim that SC061 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
