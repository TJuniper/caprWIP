# SC080 OE Final Geminate Simplification — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `79`
- rule_name: `OEFinalGeminateSimplification`
- safe computational window: `79-86` (later side runner-bounded)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `78`
- crossed stage: `SC079` OE J Loss After Heavy
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `lung`
- concrete failure example: PGmc `*lúnganjō` yields expected OE `lungen`, but the earlier-shifted variant yields `lungenn`
- interpretation: SC080 cannot move earlier across SC079. Pulling OE Final Geminate Simplification ahead of OE J Loss After Heavy leaves an unwanted doubled nasal in the `lung` derivation.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC080 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence places SC080 after `SC079` OE J Loss After Heavy. If OE Final Geminate Simplification is moved before that stage, PGmc `*lúnganjō` yields `lungenn` rather than expected OE `lungen`, so the live far-late simplification sequence has been inverted. The later direction found no real break through order `86`, so this run does **not** identify any later historical boundary for SC080.

## Caveats
This card is one-sided in current testing. The earlier boundary is historically interpretable and directly reciprocates `SC079` later, but the later side is runner-bounded and must **not** be rewritten into a claim that SC080 must precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
