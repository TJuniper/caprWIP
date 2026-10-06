# SC004 EAF Ai Monophthongization — chronology evidence card

> **Corrected PROTOFORM pass.** SC004 is the stressed/root change `*ái > *ā`
> only. The unstressed development `*ai > *ē` (final and nonfinal) is the separate
> **SC014** (see `SC014-nwgmc-unstressed-ai-monophthongization.md` and
> `SC004-components-chronology.md`). SC014 is corpus-active (witnesses span, meed),
> not corpus-inert; the SC036 `soul` boundary belongs to SC004.

## Position at experiment time
- current_order (SC id): `4`
- executable cascade position: `25` (EAF corridor, immediately after SC028 `PNWGmcPreconsonantalXLoss`)
- rule_name: `EAFAiMonophthongization`
- former_rule_name: `PWGmcAiMonophthongization` (bundled rule; retained as a documented compatibility alias)
- live Foma rule: `{*ái} -> {*ā}` (stressed/root `*ái` only)
- corpus witnesses: 24 stressed (23 attested + roe), incl. soul, stone, bone, loam
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none found before the SC014 head boundary (last_safe_order=4)`
- crossed stage: `SC014` NWGmc Unstressed Ai Monophthongization
- crossed stage type: `boundary_limited`
- failure count: `0`
- interpretation: Moving SC004 earlier from pos 25 toward the head produces no
  corpus break before the SC014 boundary (first-break
  `sc004corr_first_break_sc004.tsv`, earlier direction). Its formal earlier
  non-commutations (`PNWGmcILowering`,
  `PNWGmcULowering`) are feeding artefacts on non-corpus `EnglishProtoInput`
  forms only (`sc004_sc014_interaction_report.md`).

## Later boundary
- first later break: order `33`, crossing **SC036 OE Inter Stress Raising**
- crossed stage type: `historical_sound_change`
- failure count: `1`
- representative failures: `soul`
- concrete failure example: PGmc `*sáiwalō` yields expected OE `sāwol`, but if
  SC004 is delayed past SC036 the variant yields `sāwel` (371/372 match at the
  break).
- interpretation: SC004 must precede interstress raising; delaying the stressed
  monophthongization past SC036 leaves the wrong vowel in the `soul` derivation.
  Re-run with the corrected stressed-only rule (not copied from the pre-split
  campaign).

## Chronology statement
First-break evidence identifies one historically interpretable boundary for
SC004: the later boundary at `SC036` OE Inter Stress Raising (order 33), with
`soul`. The earlier side has no corpus break before the SC014 boundary. The
stressed target `*ái` is disjoint from SC014's unstressed `*ai`, so the two
rules are independent.

## Caveats
The later boundary is real but broad/far rather than a tight local adjacency.
SC004 executes at cascade position 25; the boundary at SC036 (order 33) leaves an
eight-position safe window above it.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc004.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc004_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/sc004_component_application_report.tsv`
