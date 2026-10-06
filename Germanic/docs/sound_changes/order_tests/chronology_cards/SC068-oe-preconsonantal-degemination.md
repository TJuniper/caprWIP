# SC068 OE Preconsonantal Degemination — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `68`
- rule_name: `OEPreconsonantalDegemination`
- safe computational window: `67-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `66`
- crossed stage: `SC066` OE L Adjacent Syncope
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `spindle`
- concrete failure example: PGmc `*spénnilō` yields expected OE `spinl`, but the earlier-shifted variant yields `spinnl`
- interpretation: SC068 can move earlier safely through order `67`, but it cannot move earlier across SC066. Pulling OE Preconsonantal Degemination ahead of OE L Adjacent Syncope leaves the `spindle` derivation with the unwanted doubled consonant cluster.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC068 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC068 after `SC066` OE L Adjacent Syncope. If OE Preconsonantal Degemination is moved before that stage, PGmc `*spénnilō` yields `spinnl` rather than expected OE `spinl`, so the cluster remains over-heavy at the point where the live ordering expects a simplified form. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC068.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable and directly reciprocates `SC066` later, but the later side is runner-bounded and must **not** be rewritten into a claim that SC068 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
