# SC043 Anglo Frisian Brightening — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `43`
- rule_name: `EAFBrightening`
- former_rule_name: `AngloFrisianBrightening`
- safe computational window: `43-43`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `42`
- crossed stage: `SC042` PWGmc Surviving Bimoric O Unrounding
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `rest`
- concrete failure example: PGmc `*rástōz` yields expected OE `ræste`, but the earlier-shifted variant yields `rasta`
- interpretation: SC043 cannot move earlier across SC042. The computational boundary is historically interpretable: the form only reaches the attested OE fronted outcome when the stage represented by SC042 has already fed the brightening environment.

## Later boundary
- first later break: order `44`
- crossed stage: `SC044` OE Breaking
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `slay`
- concrete failure example: PGmc `*sláxaną` yields expected OE `slēan`, but the later-shifted variant yields `sleaan | slēaan`
- interpretation: SC043 cannot move later across SC044. Breaking needs the fronted output created by brightening; if brightening is delayed until after breaking, the derivation produces an incorrect late broken sequence instead of the attested contracted result.

## Chronology statement
SC043 must follow `SC042` PWGmc Surviving Bimoric O Unrounding. If Anglo-Frisian Brightening is moved before that stage, PGmc `*rástōz` yields `rasta` rather than expected OE `ræste`, so the live order’s fronted derivation is lost. SC043 must also precede `SC044` OE Breaking: if brightening is moved after breaking, PGmc `*sláxaną` yields `sleaan | slēaan` instead of `slēan`, because breaking is no longer operating over the properly fronted input that the live cascade provides.

## Caveats
Both observed boundaries are historically interpretable, not merely technical. The later move across SC044 changes `29` outputs in total, but only one of those changes becomes a real new failure; many others remain changed-still-passing, such as PGmc `*bárdaz`, which yields `beard | bēard` instead of the baseline `beard`.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
- `Germanic/docs/sound_changes/order_sensitivity_first_break_pilot_03_report.md`
