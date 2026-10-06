# SC025 NSGmc Long A Nasalization — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `27`
- rule_name: `EAFLongANasalRounding`
- former_rule_name: `PNWGmcLongENasalRounding` (and earlier `NWGmcLongENasalRounding`)
- safe computational window: bounded earlier by SC024 (feeding) and later by SC004 (displacement-verified)
- status: `adjudicated_displacement_probes` (post-reformulation; pre-split pilot first-break results superseded)

## Earlier boundary
- first earlier break: SC024 `PNWGmcLongELowering` (order 4), by displacement probe
- crossed stage type: `historical_sound_change` (fed by)
- failure count: `2`
- representative failures: `month; spoon`
- concrete failure example: with SC024 displaced after this rule, PGmc `*mḗnōθz` yields `mānaþ` for expected `mōnaþ` and `*spḗnuz` yields `spān` for `spōn` — the nasalization has no *ā input to consume
- interpretation: SC025 consumes the *ā produced by SC024 (historically real intermediates *mānōþ-, *spānuz, R/T 2014 p. 11). Independently demonstrated feeding.

## Later boundary
- first later break: SC004 `EAFAiMonophthongization` (order 29), by displacement probe
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `stone; home`
- concrete failure example: with SC004 displaced before SC025 (the equivalent probe after the SC025/SC104 split), PGmc `*stáinaz` yields `stōn` for expected `stān` and `*xáimaz` yields `hōm` for `hām` — the new ā < *ai is wrongly nasalized and then rounded. Displacing SC025 alone after SC004 no longer reproduces those forms; it strands the nasalized vowel and rejects `month` and `spoon`.
- interpretation: *ā < *ai arose after the nasalization and rounding of older *ā (Campbell §132 pp. 52–53; R/T 2014 pp. 169–170). Independently demonstrated.

## Chronology statement
SC025 is the nasal branch of the later northern West Germanic low-vowel development, and after the nasalized-low-vowel adjudication it performs NASALIZATION only: *ā (< *ē₁ via SC024) is nasalized before a retained nasal, `{*ā} -> {*ą̄} / _ nasal`. The rounding to *ō is the separate later Anglo-Frisian change SC104 `EAFNasalizedLowRounding`, which SC025 feeds. SC025 must follow SC024 (feeding: month, spoon) and precede SC004 (stone, home). Its adjacency to SC102 and SC101 carries no ordering claim: SC101 is the complementary oral outcome and SC102's inserted *w environment is disjoint from the nasal one; the corpus cannot order them against each other, and SC101 can no longer see the nasalized vowel at all.

## Caveats
The pre-split card recorded a both-sides-boundary-limited negative result for the old *ē > *ō / _N formulation; that result is superseded by the reformulation. Scope `north_sea_germanic` is correct for the NASALIZATION specifically: Old Saxon nasalizes its stressed low vowels (R/T §5.1.2 p. 142) and shows the variable rounding (ōdar, sōd vs. quān, sān(o)) only for the Ingvaeonic class, never for the inherited Proto-Germanic one (Campbell §119 p. 44; Fulk §4.11 p. 72). The rounding itself is `anglo_frisian` and is carried by SC104. Confidence B (inherits the disputed *ē₁ reconstruction) attaches to this rule and does NOT transfer to SC104, which is rated A on independent evidence.

## Source files
- `Germanic/docs/sound_changes/audits/sc025-sc104-nasalized-low-vowel-adjudication.md`
- `Germanic/docs/sound_changes/audits/sc024-sc025-sc101-e1-complex-adjudication.md`
- `Germanic/docs/sound_changes/registry/chronology_edges.tsv`
