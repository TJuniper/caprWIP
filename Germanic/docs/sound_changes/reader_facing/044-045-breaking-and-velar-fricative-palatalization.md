# Breaking and velar-fricative palatalization

## Historical discussion

Breaking creates \emph{eo}-type outputs before \emph{h}, \emph{rC}, and
\emph{lC}; velar-fricative palatalization then operates in that reshaped
environment. Campbell, Ringe and Taylor, and Fulk place breaking after
brightening. The following fricative palatalization is more narrowly
conditioned [@Campbell1959, pp. 54, 166, §§139, 405--406;
@RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2;
@Fulk2018, pp. 73--74, §4.13].

Breaking has the fuller handbook treatment. The *feoh* 'cattle' and
*feohtan* 'fight' type derivations preserve its velar-fricative trigger;
they do not subsequently undergo velar-fricative palatalization.

## SC044. Breaking before \emph{h}, \emph{rC}, \emph{lC}, and conditioned \emph{w} (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

Short \emph{e} and \emph{i} also develop short \emph{eo} and
\emph{io} before singleton \emph{w}, except when a high front vowel
or \emph{j} follows it. This is the regular pre-ending history of
*cneowe* 'knee (dat.sg.)', not long-diphthong promotion
[@Luick1914, p. 139, §134; @HoggGrammar2011, p. 86, §5.22;
@RingeTaylor2014, pp. 187--188, §6.2.4].
The shared w conditioner makes that exclusion explicit:

```foma
define EnglishBreakingWContext [
    {*w} [[EnglishStarVocalic | EnglishStarConsonant]
        - [{*i} | {*í} | {*ī} | {*ḯ} | {*j}]] |
    {*w} .#.
];
```

Root stress notation does not determine vowel length. The short
knee dative is the selected comparison; long endingless *cnēo*
'knee' and the restored \emph{w} of *cnēow* 'knee' are separate paradigm
histories, discussed with
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong).

Breaking must encounter the vowel created by brightening and must precede
the rule that would otherwise palatalize its velar trigger in *feoh*
'cattle' and *feohtan* 'fight'. Before [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. After [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc [féxu]{.recon} ‘cattle’ yields [*fehu*]{.pred} rather than expected OE *feoh*, and PGmc [féxtaną]{.recon} ‘fight’ yields [*fehtan*]{.pred} rather than expected *feohtan*. The fronting relation feeds breaking. The fee/fight relation instead protects
breaking's velar trigger from premature palatalization: those forms are
displacement negatives, not live
[SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization)
applications.

## SC045. Palatalization of velar fricatives beside front vowels (`OEVelarFricativePalatalization`) {#rule-OEVelarFricativePalatalization}

```foma
define OEVelarFricativePalatalization [
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j}
]
    .o. EnglishStarAlphabet*;
```

The live population concerns voiceless x, as in *hēafod* 'head' and
*heofon* 'heaven', not voiced-fricative merger. In *feoh* 'cattle' and
*feohtan* 'fight', breaking removes the original front-vowel context:
they do not change at this rule in the live derivation. Moving the rule
before [SC044 OEBreaking](#rule-OEBreaking) instead consumes its velar
trigger, yielding [*fehu*]{.pred} and [*fehtan*]{.pred}. This is
counterbleeding protection, not direct feeding.

The distant *six* 'six' displacement test supplies only a broader
constraint: after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut),
PGmc [séxs]{.recon} ‘six’ yields [*sihs*]{.pred} rather than expected
OE *six*. Neither test dates voiced g. Its articulation and disputed
merger are separately treated under
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger)
[@RingeTaylor2014, pp. 203--204; @Fulk2018, pp. 130--132].
