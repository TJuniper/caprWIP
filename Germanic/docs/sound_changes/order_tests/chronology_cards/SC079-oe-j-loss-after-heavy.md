# SC079 OE J Loss After Heavy — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `78`
- rule_name: `OEJLossAfterHeavy`
- safe computational window: `56-78`
- status: `first_break_complete`

## Earlier boundary
- first earlier break: order `55`
- crossed stage: `SC055` OE I Umlaut
- crossed stage type: `historical_sound_change`
- failure count: `26`
- representative failures: `believe; bow; fast; follow; heal`
- concrete failure example: PGmc `*galáubijaną` yields expected OE `ġelīefan`, but the earlier-shifted variant yields `ġelēafan`; PGmc `*báugijaną` likewise yields `bēaġan` instead of expected `bīeġan`; PGmc `*fúlgijaną` yields `fulġan` instead of `fylġan`
- interpretation: SC079 can move earlier safely through order `56`, but it cannot move earlier across SC055. Pulling OE J Loss After Heavy that far forward undoes the live umlaut-sensitive vowel development across a broad set of derivations.

## Later boundary
- first later break: order `79`
- crossed stage: `SC080` OE Final Geminate Simplification
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `lung`
- concrete failure example: PGmc `*lúnganjō` yields expected OE `lungen`, but the later-shifted variant yields `lungenn`
- interpretation: SC079 can move later safely through its current order, but it cannot move later across SC080. Delaying OE J Loss After Heavy past OE Final Geminate Simplification leaves an unwanted doubled nasal in the `lung` derivation.

## Chronology statement
Current first-break evidence places SC079 after `SC055` OE I Umlaut and before `SC080` OE Final Geminate Simplification. If OE J Loss After Heavy is moved before `SC055`, PGmc `*galáubijaną` yields `ġelēafan` rather than expected OE `ġelīefan`, PGmc `*báugijaną` yields `bēaġan` rather than `bīeġan`, and PGmc `*fúlgijaną` yields `fulġan` rather than `fylġan`, alongside twenty-three other newly failing rows. If it is moved later than `SC080`, PGmc `*lúnganjō` yields `lungenn` instead of `lungen`. The later side therefore directly reciprocates `SC080` earlier.

## Caveats
The earlier boundary is historically real, but it is broad across SC055 rather than a tight local adjacency claim. The later side is much narrower and currently concentrated in the single `lung` derivation.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_pilot_03_failures.tsv`
- `Germanic/docs/sound_changes/sound_change_order_sensitivity.tsv`
