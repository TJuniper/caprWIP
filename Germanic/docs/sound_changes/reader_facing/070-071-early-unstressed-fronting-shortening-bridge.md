# Early unstressed fronting and later o-shortening

## Historical discussion

Campbell distinguishes the shortening of unaccented long vowels, while Hogg,
Ringe and Taylor, and Fulk place fronting and shortening within a later history
of syncope and final-vowel adjustment [@Campbell1959, p. 148, §355;
@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7]. Earlier unstressed fronting precedes later
o-shortening.

[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) has both an
earlier and a later lexical breakpoint.
[SC071 OELateOShortening](#rule-OELateOShortening) confirms their reciprocal
order, but no lexical evidence fixes its later boundary.

## SC070. Early fronting of unstressed \emph{*a} (`OEUnstressedFrontingEarly`) {#rule-OEUnstressedFrontingEarly}

```foma
define OEUnstressedFrontingEarly OEUnstressedAFronting;
```

The rule fronts unstressed \emph{*a} to \emph{*æ} after the earlier shortening
has created a frontable vowel but before the later shortening of unstressed
\emph{*ō}. It produces endings such as OE \emph{-en} in *lungen* ‘lungs’.

If the rule is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected OE *lungen* ‘lungs’. If the rule is delayed until after [SC071 OELateOShortening](#rule-OELateOShortening), PGmc [búrōθi]{.recon} ‘bears’ yields [*boreþ*]{.pred} rather than expected OE *boraþ* ‘bears’, and PGmc [mḗnōθz]{.recon} ‘month’ yields [*mōneþ*]{.pred} rather than expected *mōnaþ* ‘month’. The witness forms require [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) to follow [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and precede [SC071 OELateOShortening](#rule-OELateOShortening).

The relation to [SC071 OELateOShortening](#rule-OELateOShortening) is local.
The earlier boundary at
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) places fronting after
the older palatal developments.

## SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening [
    {*ō} -> {*o} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

The rule shortens the remaining unstressed long \emph{*ō} after fronting. The
shortened vowel is then resolved by the following medial/final distribution,
not directly as \emph{a} [@StauslandJohnsen2015, pp. 28--31].

Moving the rule before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) makes PGmc [búrōθi]{.recon} ‘bears’ yield [*boreþ*]{.pred} rather than expected OE *boraþ* 'bears', and PGmc [líznōθi]{.recon} ‘learns’ yield [*liorneþ*]{.pred} rather than expected *liornaþ* 'learns'. The contrast requires [SC071 OELateOShortening](#rule-OELateOShortening) to follow [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly).

## SC099. Medial raising of shortened unstressed \emph{*o} (`OEMedUnstressedORaising`) {#rule-OEMedUnstressedORaising}

```foma
define OEMedUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]* EnglishStarVocalic
];
```

After [SC071 OELateOShortening](#rule-OELateOShortening), the shortened vowel gives \emph{u} in an unstressed medial
syllable. The rule encodes Stausland Johnsen's statistically supported account
of West Saxon ō-verb pasts, not a general rule for inherited short \emph{*o}
or for nominal morphology [@StauslandJohnsen2015, pp. 28--31, 36]. His
diagnostic derivation is PGmc [wúndōdē]{.recon} ‘wounded’ > [wundode]{.pred}
> OE [wundude]{.iv lang=oe sort=wundude role=evidence_form} ‘wounded’ [@StauslandJohnsen2015, pp. 28--29].

## SC100. Final lowering of shortened unstressed \emph{*o} (`OEFinalUnstressedOLowering`) {#rule-OEFinalUnstressedOLowering}

```foma
define OEFinalUnstressedOLowering [
    {*o} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]* .#.
];
```

In a final syllable the same shortened vowel gives \emph{a}. Thus the existing
month control continues PGmc [mḗnōθz]{.recon} ‘month’ through shortened
\emph{*o} to OE [mōnaþ]{.iv lang=oe sort=monath role=evidence_form} ‘month’, while [wúndōdē]{.recon} ‘wounded’ takes
[SC099 OEMedUnstressedORaising](#rule-OEMedUnstressedORaising)
instead. The medial/final contrast and its chronology after long-vowel
shortening are Stausland Johnsen's analysis [@StauslandJohnsen2015,
pp. 28--31].
