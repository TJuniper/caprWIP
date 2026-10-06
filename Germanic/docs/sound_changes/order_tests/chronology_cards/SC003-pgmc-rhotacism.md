# SC003 West Germanic rhotacism — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `3`
- rule_name: `EAFRhotacism`
- former_rule_name: `PGmcRhotacism`
- safe computational window: `2-43` (earlier side boundary-only; later side broad/far)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before tested-chain boundary at order 2`
- crossed stage: `SC002` Gm Simplification
- crossed stage type: `historical_sound_change`
- failure count: `0`
- representative failures: `none`
- concrete failure example: `none — no earlier real break was found before the tested-chain boundary`
- interpretation: The temporary early-rule harness can move SC003 earlier safely across SC002 down to order `2`, but it cannot test farther because that reaches the left edge of the tested historical chain. This is therefore a boundary-only result rather than an earlier historical boundary for PGmc Rhotacism.

## Later boundary
- first later break: order `44`
- crossed stage: `SC044` OE Breaking
- crossed stage type: `historical_sound_change`
- failure count: `4`
- representative failures: `learn; learn (3sg); learn (iptv.2sg); meed`
- concrete failure example: PGmc `*líznōjaną` yields expected OE `liornian`, but the later-shifted variant yields `lirnian`
- interpretation: SC003 can move later safely through order `43`, but it cannot move later across SC044. Delaying PGmc Rhotacism that far forward leaves the wrong consonant-and-vowel sequence in the `learn` family, and the same shift also yields `lirnaþ`, `lirna`, and `merde`.

## Chronology statement
Current first-break evidence identifies one historically interpretable boundary for SC003. The earlier search moved safely across SC002 down to order `2` and then stopped at the left edge of the tested historical chain with no real break, so that side remains boundary-only rather than a positive chronology constraint. The later search does find a real historical boundary at `SC044` OE Breaking: if PGmc Rhotacism is moved later than that stage, PGmc `*líznōjaną` yields `lirnian` rather than expected OE `liornian`, and related witnesses such as `*líznōθi`, `*líznô`, and `*mízdai` likewise yield `lirnaþ`, `lirna`, and `merde` instead of `liornaþ`, `liorna`, and `meorde`.

## Caveats
This card is one-sided in current testing. The later boundary is historically interpretable, but it is broad/far across SC044 rather than a tight local adjacency claim. The backend report layer now treats the historical stage as post-PWGmc West Germanic; CAPR's internal rule name is now `EAFRhotacism` (former `PGmcRhotacism`), and the chronology evidence should be read with that distinction in mind.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`
