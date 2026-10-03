# SC004 EAF ai-monophthongization — literature dossier

> **Corrected PROTOFORM pass.** This dossier covers **only** the stressed/root
> development `*ái > *ā`. The unstressed development `*ai > *ē` (final and
> nonfinal) is the separate, earlier **SC014** (see
> `014-015-opening-vowel-prelude.dossier.md`). An earlier version of this dossier
> misclassified `loam` and `whine` using the cognate-set `PROTO` field; the
> production input is the Old-English-row `PROTOFORM`, under which `loam`
> (`*láimą`) is stressed `*ái` and `whine` (`*xwḯnaną`) carries no `*ai` at all.
> Implemented on branch `historical-cascade-order` (FST split commit `f59b758d`;
> PROTOFORM correction commit `9c71aed3`).

## Historical phenomenon

The monophthongization of stressed/root `*ái` to `*ā` in the English line.
Later i-mutation can produce `ǣ`; ordinary inherited-long fronting must
not be confused with that later conditioned development
([@Campbell1959, pp. 52–53, 69]).
Common-stem versus daughter placement is reopened in the source-led packet
in the routed book dossier. An author's areal account is not CAPR's adopted
mechanism; the required Anglo-Frisian ancestral node remains in place.

## CAPR rule

- change_id: `SC004`
- display_name: `EAF Ai Monophthongization`
- rule_name: `EAFAiMonophthongization`
- former identifier: `PWGmcAiMonophthongization` (bundled rule; retained as a documented compatibility alias)
- FOMA definition: `{*ái} -> {*ā}` (stressed/root `*ái` only)
- current canonical metadata: hist_stage `eaf`; hist_scope `north_sea_germanic`;
  book Chapter 3. Executable positions are derived, not historical evidence.

## Example lexemes

1. `soul` (`*sáiwalō`; the SC036 boundary witness)
2. `stone` (`*stáinaz`)
3. `bone` (`*báiną`)
4. `loam` (`*láimą`; stressed `*ái` by its PROTOFORM)
5. `one` (`*áinaz`)

The older raw-input report counts 24 stressed protoforms, including roe
`*ráixōn` without a target. The fresh selected-387 census has 23 live
firings; roe is excluded. Loam's selected `*láimą` is explicitly a pre-OE
transponent, not its PGmc citation input. The two dat.sg `*-ai` endings
(`span`, `meed`) are unstressed and belong to SC014, not SC004.

## Source support

1. Ringe and Taylor discuss stressed ai and the inherited-long boundary in
   §6.1.2; pp. 40–41 concern unstressed ai
   ([@RingeTaylor2014, pp. 170–171]).
2. Fulk's relevant English/Frisian outcomes and disputed ai intermediate
   are in §4.12, not §5.2 ([@Fulk2018, pp. 72–73]).
3. Campbell's chronology and English ai examples are §§131–134.
   Section 417 concerns xs, not this law ([@Campbell1959, pp. 52–53]).
4. **Versloot 2017** (verified directly; see the reconciliation dossier) argues
   that stressed/root `*ai` monophthongization spread in two areal waves through
   a North Sea Germanic dialect continuum (c. AD 400--900), a diffusion rather
   than a single inherited Proto-Anglo-Frisian node; Old English is among the
   broadest monophthongizers. Versloot supports precisely the **stressed** side
   treated here. CAPR separates the conditional runic evidence from his
   diffusion mechanism ([@Versloot2017, pp. 295–297, 318]).

## Chronology / order-test status

1. Later boundary: `SC036` OE Inter Stress Raising. First-break testing with the
   corrected stressed-only rule confirms that delaying SC004 past SC036 makes
   `*sáiwalō` yield `sāwel` instead of `sāwol` (order 33; 371/372 match at the
   break). These numbers belong to that historical experiment, not the
   current 387-row census or derived executable position.
2. Earlier side: no corpus break toward the head (boundary-limited); SC004's only
   corpus-relevant boundary is SC036.
3. Formal interactions (`sc004_sc014_interaction_report.md`): SC004 non-commutes
   with `PWGmcEarlyIApocope`, `PNWGmcILowering`, `PNWGmcULowering` only on
   non-corpus `EnglishProtoInput` forms (feeding artefacts) and genuinely with
   `SC036` (the soul dependency).

## Cautions for reader-facing prose

1. Present SC004 as the stressed/root `*ái > *ā` change only; do **not**
   reintroduce unstressed `*ai` (that is SC014).
2. Distinguish the current operational EAF corridor, the required ancestral
   node and an author's areal account. The current research recommendation
   favors daughter placement of completed English contraction conditionally;
   no canonical metadata verdict follows from this source correction.
3. `loam` (`*láimą`) is a stressed witness; `whine` is not an ai-monophthongization
   case at all.
4. Treat the `SC036` relation as broad/far rather than a local seam.

See also: `014-015-opening-vowel-prelude.dossier.md` (SC014, the unstressed
change); `sc004_historical_options_report.md`; `sc004_sc014_interaction_report.md`;
`SC004-components-chronology.md`.
