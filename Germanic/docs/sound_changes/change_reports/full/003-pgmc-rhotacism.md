# West Germanic rhotacism

### Sound-change report

#### Historical formulation

SC003 `EAFRhotacism` appears here as a singleton consonant report for the change of medial `*z` to `*r`. Historically, the change is better treated as a **post-PWGmc West Germanic rhotacism** than as a Proto-Germanic innovation proper. Ringe and Taylor place rhotacism in the post-PWGmc sound-change layer and stress that it was not uniform within WGmc [@RingeTaylor2014, pp. 98, 102], while Crist argues that it cannot be inherited from Proto-Northwest Germanic and must follow earlier WGmc `*z`-deletion rules [@Crist2001, pp. 104-106; @Crist2002, pp. 1, 4].

That does not make the CAPR rule name unusable. It does mean the backend apparatus should distinguish the implementation label `EAFRhotacism` from the source-supported historical stage label.

#### Source tradition

The source support for the phenomenon itself is strong. Bammesberger states succinctly that Germanic `/z/` yielded `/r/` in intervocalic position in Old English, though it was generally lost finally [@Bammesberger1992, p. 39]. Ringe and Taylor go farther: they first note that the change occurred independently in Norse and WGmc and was not uniform even in the latter [@RingeTaylor2014, p. 52], and later advise assigning the process to the post-PWGmc period [@RingeTaylor2014, pp. 98, 102]. Crist's analysis aligns with that caution by arguing that rhotacism is not inherited from Proto-Northwest Germanic and must follow earlier WGmc `*z`-deletion rules [@Crist2001, pp. 104-106; @Crist2002, pp. 1, 4].

This is enough source support not only for a backend report but for a cautious historical label. The clearest sources support the change itself strongly and support locating it in the West Germanic area after PWGmc rather than at Proto-Germanic proper.

#### CAPR implementation

CAPR models the development as one explicit rewrite in vocalic medial environments:

```foma
define EAFRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

The implementation is broader than a strictly intervocalic `V_V` rule because the current model also needs to retain medial `VzC` environments. That choice matches the local FST comment, but it should still be kept distinct from the narrower formulations in the historical literature.

For implementation continuity, CAPR keeps the exact rule name `EAFRhotacism`. That identifier should be read as a model label rather than as the best historical stage label.

#### Place in the cascade

In the current inventory ordering, SC003 follows SC002 `PGmcGmSimplification` and precedes the Proto-West-Germanic developments that begin with SC004. In the implementation, however, it remains inside the same bundled Proto-Germanic consonant block that also contains final `*z` deletion.

That placement still matters, but the early-rule harness now exposes SC003 to standalone first-break testing without changing the production bundle. The rule therefore has direct chronology support even though the live cascade remains bundled, and the historical prose can now say more clearly that the modeled stage name is earlier than the source-supported historical interpretation.

#### Order evidence

Validated order evidence now exists through the temporary early-rule harness:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_early_rules_01_failures.tsv`

The earlier search moved SC003 safely across SC002 down to order `2` and then reached the left edge of the tested historical chain with no real break. That side is therefore boundary-only rather than a positive earlier chronology constraint.

The later search does find a real historical break at order `44` across `SC044` OE Breaking. If PGmc Rhotacism is delayed past that stage, PGmc `*líznōjaną` yields `lirnian` rather than `liornian`, `*líznōθi` yields `lirnaþ` rather than `liornaþ`, `*líznô` yields `lirna` rather than `liorna`, and `*mízdai` yields `merde` rather than `meorde`.

That later boundary is historically interpretable, but it is broad/far rather than a tight local adjacency claim.

#### Interpretation

SC003 is now substantially stronger than SC002 on both the chronology and source sides. It has a validated one-sided historical boundary and exact wrong-output diagnostics, and the literature now supports a cautious historical label: **post-PWGmc West Germanic rhotacism**. That is enough for a cautious singleton report, provided the prose keeps the CAPR rule name and the historical label clearly distinct.

#### Remaining cautions

Two cautions still matter most. First, backend prose should keep rhotacism distinct from final `*z` deletion, because the literature treats them as separate events with their own chronology. Second, the later boundary with `SC044` is broad/far rather than a tight local adjacency claim. The prose should therefore continue to describe the historical stage as post-PWGmc West Germanic while reserving `EAFRhotacism` for the CAPR rule label.
