# SC101 EAF Long A Fronting — chronology evidence card

## Position at experiment time
- order_at_experiment_time: `28`
- rule_name: `EAFLongAFronting`
- former_rule_name: `none` (new identity from the SC024 split; the behavior was formerly telescoped inside one-step SC024)
- safe computational window: bounded earlier by SC024 (feeding) and later by SC004 and SC056 (displacement-verified)
- status: `adjudicated_displacement_probes`

## Earlier boundary
- first earlier break: SC024 `PNWGmcLongELowering` (order 4), by displacement probe
- crossed stage type: `historical_sound_change` (fed by)
- failure count: `3+`
- representative failures: `sheep; year; sleep`
- concrete failure example: with SC024 displaced after this rule, PGmc `*skḗpą` yields `sċāp` for expected `sċēap`, `*jḗrą` yields `ġār` for `ġēar`, `*slḗpaną` yields `slāpan` for `slǣpan`
- interpretation: SC101 consumes the *ā produced by SC024. Independently demonstrated feeding; historically several centuries separate the two changes.

## Later boundary
- first later break: SC004 `EAFAiMonophthongization` (order 29), by displacement probe
- crossed stage type: `historical_sound_change`
- failure count: `5`
- representative failures: `loath; rope; token; soul; ghost`
- concrete failure example: with SC101 displaced after SC004, PGmc `*láiθaz` yields `lǣþ` for expected `lāþ`, and likewise `rǣp`, `tǣcn`, `sǣwol`, `ġēast` for `rāp`, `tācn`, `sāwol`, `gāst`
- interpretation: fronting of inherited *ā was well under way before *ai > ā was complete, else ā < *ai would show fronting (Campbell §132 pp. 52–53, endorsed as cogent by R/T 2014 pp. 169–170). Independently demonstrated; historically the two changes may have overlapped — the discrete cascade order is the executable expression of the non-merger.
- additional later boundary (broad/far): SC056 `OEWsPalatalDiphthongization` — with SC101 displaced after SC056, `*skḗpą` yields `sċǣp` for `sċēap` and `*jḗrą` yields `ġǣr` for `ġēar` (WS diphthongization operated on the already-fronted vowel: Campbell §185 pp. 69–70; R/T 2014 p. 216). This is the genuine content of the former SC024 → SC056 sheep/year edge.

## Chronology statement
SC101 is Change B of the *ē₁ complex: much later northern West Germanic fronting of non-nasalized stressed *ā > *ǣ (WS ǣ; Angl./Kent./OFris ē; sporadic OS e), `{*ā} -> {*ǣ} / _ [C - nasal - w]`, plus fronting before *w + high front vocalic, at order 28, immediately before SC004. It must follow SC024 (feeding) and SC102 (which supplies the *w that blocks sow), precede SC004 (non-fronting of stān/hām-type ā < *ai), and precede SC056 (sheep, year).

## Caveats
New rule: it has not yet been through a pilot first-break runner pass; all boundaries above are adjudication displacement probes over the full 383-row corpus. The historical *w conditioning (R/T pp. 150–151) is now encoded: fronting is blocked before *w (sow, *sāwaną → sāwan) unless the *w is followed by high front vocalic (betray, *lāwijaną → *lǣwijaną at this boundary, later lǣwan). The SC102 → SC101 order is historically asserted (R/T p. 151) but commutes executably because this rule is preconsonantal. Confidence B (Fulk 2018 §4.6 reads the front vowel as retained rather than restored by fronting).

## Source files
- `Germanic/docs/sound_changes/audits/sc024-sc025-sc101-e1-complex-adjudication.md`
- `Germanic/docs/sound_changes/registry/chronology_edges.tsv`
