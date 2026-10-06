# Weak-tail reduction

## Historical discussion

Campbell, Hogg, Ringe and Taylor, and Fulk describe a late history in which
apocope, shortening, contraction, and further weak-tail reductions reshape
final syllables [@Campbell1959, p. 148, §355; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--91, §5.6]. Lexical failures place the remaining weak-tail
reduction after unstressed fronting and before contraction.

## SC078. Reduction of remaining weak-tail vowels (`OEWeakTailReduction`) {#rule-OEWeakTailReduction}

```foma
define OEWeakTailReduction OEWeakTailReduction1;
```

The rule reduces the remaining weak-tail vowels, preventing a broad class of
\emph{-en} and extra-vowel outcomes.

I place the change after [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and before [SC086 OEContraction](#rule-OEContraction). Moving it before
[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc
[bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc
[bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* ‘bind’, alongside
a much wider set of comparable \emph{-en} failures. If the rule is delayed until
after [SC086 OEContraction](#rule-OEContraction), PGmc [fléuxaną]{.recon} ‘flee’ yields
[*flēoan*]{.pred} rather than expected OE *flēon* ‘flee’, and PGmc [sláxaną]{.recon} ‘slay’
yields [*sleaan*]{.pred} rather than expected *slēan* ‘slay’.

The earlier boundary spans a wide interval and does not establish a close
neighboring relation. The later boundary is narrower:
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) precedes
[SC086 OEContraction](#rule-OEContraction).
