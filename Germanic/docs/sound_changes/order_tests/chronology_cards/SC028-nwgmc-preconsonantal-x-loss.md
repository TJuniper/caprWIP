# SC028 Northern West Germanic *xs-Cluster Simplification — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `28`
- rule_name: `PNWGmcPreconsonantalXLoss`
- former_rule_name: `NWGmcPreconsonantalXLoss`
- safe computational window: `13-86` (earlier side runner-limited; later side boundary-limited)
- status: `first_break_complete` (adjudicated 2026: reformulated, restaged and reordered; see
  `Germanic/docs/sound_changes/audits/sc028-xs-cluster-simplification-adjudication.md`)
- canonical historical stage: `pwgmc` / `north_wgmc` (northern West Germanic; post-Gothic,
  since Gothic retains the *h in bi-niuhsjan, saihsta)

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC028 earlier safely down to order `13`, but it cannot test farther because that path enters bundled `PWGmcChanges`. This is therefore not yet an earlier historical boundary for NWGmc Preconsonantal X Loss.

## Later boundary
- first later break: `none found before runner boundary at order 86`
- crossed stage: `SC087` OE R Metathesis
- crossed stage type: `historical_sound_change` (runner-boundary result)
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no later real break was found before the runner boundary`
- interpretation: The current runner found no later real break for SC028 through last safe order `86`. This is not a detected later historical boundary for the rule; it is a no-break-before-boundary result bounded by the current search space.

## Chronology statement
Current first-break evidence does **not** yet identify a historical first-break boundary for SC028 in either tested direction. The earlier search ran safely down to order `13` before stopping at bundled `PWGmcChanges`, and the later search ran safely through order `86` before stopping at the current `SC087` boundary with no real break. This card therefore records a negative computational result rather than a positive chronology constraint.

## Adjudicated chronology (2026)
The negative computational result above is now understood and is **expected**, not a gap in the search.
The rule's order is genuinely underdetermined by the selected corpus: its only firing witness is `fist`,
and `fist` reaches the same surface form under either order relative to SC103, because removing the *x
first leaves a nasal before *s which the Ingvaeonic nasal-spirant law then removes with compensatory
lengthening. The outcome is overdetermined and no displacement probe can discriminate.

The chronology is therefore carried entirely by the comparative evidence, which supplies two bounds:
the change follows the Proto-West Germanic *-CijV- syncope, which creates the *sj of *niuhsjan
(Ringe and Taylor p. 157), and it precedes breaking, since the undiphthongized vowels of wæstm and þīsl
require the *h to have gone first (Ringe and Taylor p. 158). The rule is now composed immediately after
`PWGmcSyllabicJ`, inside that window; several placements within it commute and no finer order is claimed.
The SC103 -> SC028 relation is recorded as `stage_entailed`, with no representative lexeme.

## Caveats
Both sides are boundary-limited rather than historically interpretable. This card should not be used to claim that SC028 must follow any specific earlier stage or precede `SC087`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
