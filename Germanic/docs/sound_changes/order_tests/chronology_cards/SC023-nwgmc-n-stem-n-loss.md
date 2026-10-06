# SC023 Proto-Germanic Word-Final N Loss — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `23`
- rule_name: `PNWGmcNStemNLoss` (stable executable identifier; not a stage claim)
- former_rule_name: `NWGmcNStemNLoss`
- canonical historical stage: `pgmc` (general (pre-)PGmc loss of word-final
  `*-n` with nasalization; Ringe 2017: 101–103; see
  `Germanic/docs/sound_changes/audits/sc023-adjudication.md`)
- safe computational window: `13-46` (earlier side runner-bounded)
- status: `first_break_complete` (adjudicated 2026: scope/stage reformulated,
  edges retained)

## Live firing population
SC023 fires on exactly 17 corpus rows, all weak n-stem nouns cited in the
stem form `*-ōn-` (adder, earth, flask, heart, line, list, nettle,
nightmare, side, sun, swallow, toe, tongue, wart, weasel, whore, widow):
citation-stem `*túngōn` → PGmc nom. sg. `*túngǭ`. The verb `do` is NOT a
live application — `*dōną` passes position 23 untouched.

## Earlier boundary
- first earlier break: `none found before runner boundary at order 13`
- crossed stage: `PWGmcChanges`
- crossed stage type: `blocked_by_runner_limitation`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the runner boundary`
- interpretation: The current runner can move SC023 earlier safely down to
  order `13`, but it cannot test farther because that path enters bundled
  `PWGmcChanges`. Historically no earlier boundary is expected in this
  cascade at all: the change is (pre-)Proto-Germanic, so every executable
  rule of the cascade is historically later than it.

## Later boundary
- first later break: order `47`
- crossed stage: `SC047` OE Heavy Syllable Nasal Apocope
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `do`
- concrete failure example: PGmc `*dōną` yields expected OE `dōn`, but the later-shifted variant yields `+?` (no output)
- evidence type: **counterfeeding, stage-entailed** — `do` is a negative
  witness, not a domain application. SC047 deletes final `*ą`, creating a
  *secondary* word-final `*-ōn` in `*dōn`; a displaced SC023 then fires
  anachronistically (`*dōn > *dǭ`) and the derivation collapses. The
  historical content is the classical counterfeeding argument: OE `dōn`
  retains its secondary final `-n`, so the (pre-)PGmc word-final `*-n`
  loss was complete and inactive before the OE-period apocope. Because the
  change is general phonology (Ringe's proof set includes the verb form
  `*dedǭ` 'I did'), the verb `dōn` is a legitimate witness of this
  inactivity.
- interpretation: SC023 can move later safely through order `46` but not
  across SC047. The ordering SC023 < SC047 is real but stage-entailed
  ((pre-)PGmc ≪ OE), not a discovered tight local adjacency.

## Chronology statement
The earlier search ran safely down to order `13` before stopping at bundled
`PWGmcChanges` with no real break; that side is runner-limited, and no
earlier in-cascade boundary is historically expected for a (pre-)PGmc
change. The later boundary at `SC047` is genuine counterfeeding evidence:
delaying the word-final `*-n` loss past the `*ą`-apocope wrongly consumes
the secondary `-n` of `*dōn` and collapses the `do` derivation. The
independent SC023 < SC069 boundary (recorded on the SC069 card) rests on
the seventeen in-domain weak-noun witnesses and is unaffected by the `do`
reclassification.

## Caveats
This card is one-sided in current testing. The later boundary is
historically interpretable as counterfeeding, but it is broad/far across
`SC047` rather than a tight local adjacency claim; the bad outcome must be
narrated as a failed derivation rather than as a competing surface form,
and `do` must never be presented as a lexeme that undergoes the change.

## Source files
- `Germanic/docs/sound_changes/audits/sc023-adjudication.md`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
