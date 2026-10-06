# SC014 NWGmc Unstressed Ai Monophthongization — chronology evidence card

> **Corrected PROTOFORM pass.** SC014 is the unstressed monophthongization
> `*ai > *ē` (final AND nonfinal; Ringe-Taylor's rule, not merely word-final),
> split out of the former bundled SC004. An earlier version of this card called
> SC014 "corpus-inert"; that was a cognate-set `PROTO`-field artefact. Under the
> production `PROTOFORM`, SC014 has **two corpus witnesses** and a real later
> boundary. The stressed `*ái > *ā` development is SC004 `EAFAiMonophthongization`
> (see `SC004-pwgmc-ai-monophthongization.md`, `SC004-components-chronology.md`).

## Position at experiment time
- current_order (SC id): `14`
- executable cascade position: `1` (head of `EarlyEnglishLineChanges`, the former SC004 slot)
- rule_name: `PNWGmcUnstressedAiMonophthongization`
- former_rule_name: `NWGmcUnstressedAiMonophthongization`
- live Foma rule: `{*ai} -> {*ē}` (unstressed `*ai`, final and nonfinal)
- corpus witnesses: `span` (`*spánnai` > spanne), `meed` (`*mízdai` > meorde)
- status: `first_break_complete`

## Earlier boundary
- first earlier break: `none — SC014 already executes at the cascade head (pos 1)`
- crossed stage: `n/a`
- crossed stage type: `head_of_cascade`
- interpretation: SC014 is at position 1, so it cannot be moved earlier; the
  earlier side is bounded by the cascade head, not by a historical break.

## Later boundary
- first later break: order `69`, crossing **SC072 OE Unstressed Long Vowel Shortening**
- crossed stage type: `historical_sound_change`
- failure count: `2`
- representative failures: `span`, `meed`
- concrete failure example: if SC014 is delayed past SC072, the `*-ē` it produces
  from `*-ai` is no longer available for shortening, so PGmc `*spánnai` yields
  `spannē` instead of expected `spanne`, and `*mízdai` yields `meordē` instead of
  `meorde` (370/372 match at the break).
- interpretation: SC014 must precede the unstressed-long-vowel shortening (SC072)
  so that the monophthong it creates in the dat.sg `*-ai` endings is shortened to
  final `-e`. This is a genuine lexical ordering constraint.

## Chronology statement
SC014 is **corpus-active** (two dat.sg `*-ai` witnesses, `span` and `meed`). Its
earlier side is bounded by the cascade head; its later side has a real
first-break boundary at SC072 OE Unstressed Long Vowel Shortening. Its historical
stage — early Proto-Northwest Germanic, with the `*ē` outcome merging into long
mid `*ē` — is established both by these corpus endings and by the literature
(R/T pp. 37–41, §6.1.5; Fulk §5.2). The nonfinal unstressed environment (e.g.
`*berain > *berēn`) is corpus-inert but is covered by the rule and confirmed by
Foma probe.

## Caveats
The earlier "corpus-inert" card and the still-earlier bundled-runner-limitation
card are both superseded: the first by the PROTOFORM correction (which surfaces
span and meed), the second by the split itself.

## Source files
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc014.tsv`
- `Germanic/docs/sound_changes/order_tests/summaries/sc004corr_first_break_sc014_changes.tsv`
- `Germanic/docs/sound_changes/order_tests/sc004_component_application_report.tsv`
