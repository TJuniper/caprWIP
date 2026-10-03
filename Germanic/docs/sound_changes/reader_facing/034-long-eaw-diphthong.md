# Long \emph{ēaw} before following vowels

## Historical discussion

Singleton \emph{aw} before a following vowel develops into long \emph{ēaw},
as in *sċēawian* 'show' and *strēaw* 'straw'. This remaining singleton path
must be distinguished from the inherited geminates of *dēaw* 'dew' and
*hēawan* 'hew'. Those now undergo early
[SC031 OEWWSimplification](#rule-OEWWSimplification), producing
\emph{*au} plus retained \emph{*w}, followed by English fronting and
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
Campbell distinguishes the glide histories; Ringe and Taylor distinguish
earlier reanalysis from later English realization
[@Campbell1959, pp. 45--47, 53--54; @RingeTaylor2014, pp. 65--66, 171--175].
The resulting long diphthong is \emph{ēaw}.

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) retains its singleton
operation before [SC043 EAFBrightening](#rule-EAFBrightening).

## SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

The current operation changes four singleton show/straw forms. Dew and
hew no longer demonstrate a local simplification-then-lengthening chain
here: their earlier reanalysis has already removed that input shape.
The older displacement results for those geminates describe the superseded
representation, not independent dates for the adopted early event.
The singleton operation itself remains unchanged; this decomposition
does not give every glide history a new historical verdict
[@Campbell1959, pp. 45--47; @RingeTaylor2014, pp. 171--175].
