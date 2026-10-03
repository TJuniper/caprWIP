# J-strengthening, vocalization, and ei-contraction

## Historical discussion

[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
preserves a consonantal outcome after front diphthongs.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) then
normalizes part of the inherited intervocalic \emph{*j} domain, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) removes the
resulting \emph{ei}-like sequence in weak verbal endings.

The output of each rule conditions the next.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) has local
lexical evidence on both sides;
[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
has a distant earlier boundary, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) has no
tested later boundary.

## SC081. Strengthening of \emph{*j} after front diphthongs (`OEJStrengtheningAfterFrontDiphthong`) {#rule-OEJStrengtheningAfterFrontDiphthong}

```foma
define OEJStrengtheningAfterFrontDiphthong [
    {*j} -> {*ʒ} || [{*ēa}|{*ḗa}|{*íe}|{*īe}|{*éa}] _ EnglishStarVocalic
];
```

After the relevant front diphthongs, \emph{*j} first strengthened to a consonantal outcome; otherwise it would have vocalized too early.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [stráwjaną]{.recon} ‘strew’ yields [*strēaġan*]{.pred} rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields [*strīeian*]{.pred} rather than *strīeġan*. The order test requires [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The earlier constraint reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut) and
therefore defines a wide interval. The *strīeġan* 'strew' derivation fixes the local
relation to [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

## SC082. Bounded inherited-j normalization (`OEIntervocalicJVocalization`) {#rule-OEIntervocalicJVocalization}

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} ||
        [EnglishStarVocalic - [{*ǣ}|{*ē}|{*ḗ}]] _ EnglishStarVocalic
];
```

The former unrestricted VjV matcher wrongly gave model-only
[*cǣie*]{.pred} instead of *cǣġe* 'key'. Hogg's pre-OE
\emph{*kǣjæ} retains the glide [@Hogg1979, p. 105]. The bounded rule
therefore excludes preceding non-high long front monophthongs.

This is not a generic physical vocalization law. Hogg distinguishes
high-vowel coalescence from spellings that merely represent a consonantal
glide and from unstressed alternations
[@HoggGrammar2011, pp. 283--286, §§7.69--7.76].
The remaining weak-suffix e+j to e+i to i path telescopes later
raising/contraction, rather than asserting that its e+i intermediate is a
source reconstruction [@RingeTaylor2014, p. 228].
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction)
consumes that modeled sequence. The full residual proxy domain is not
claimed to be one independently established historical event.

The separately represented fricative ʝ passes through this zone without
being treated as inherited j. Its later merger belongs to
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger).

Moving the rule before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) makes PGmc [stráwjaną]{.recon} ‘strew’ yield [*strīeian*]{.pred} rather than expected OE *strīeġan* ‘strew’. Delaying it until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* ‘bore’, PGmc [xándlōjaną]{.recon} ‘handle’ yield [*handleian*]{.pred} rather than expected *handlian* ‘handle’, and PGmc [mákōjaną]{.recon} ‘make’ yield [*maceian*]{.pred} rather than expected *macian* ‘make’. The witness forms require [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) to follow [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) and precede [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is
therefore ordered between strengthening and contraction.

## SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

The rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Moving the rule before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* 'bore', PGmc [líznōjaną]{.recon} ‘learn’ yield [*liorneian*]{.pred} rather than expected *liornian* 'learn', and PGmc [líkkōjaną]{.recon} ‘lick’ yield [*licceian*]{.pred} rather than expected *liccian* 'lick'. The contrast requires [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) to follow [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
