# Northwest Germanic u-lowering

## Historical discussion

Northwest Germanic lowered \emph{*u} to \emph{*o} when the following
syllable contained a non-high vowel. Campbell describes the change and
lists *ġeoc* 'yoke' among its regular outcomes [@Campbell1959, pp. 42--43,
§115]; Fulk gives the same word as a standard example — "OIcel. ok, OE
geoc, OHG joh beside juh and OS juk" — and notes the paradigmatic
alternation between lowered and unlowered stems that the conditioning
produced [@Fulk2018, p. 56, §4.3]. A word-initial \emph{*j} does not block
the change: the blocking effect of \emph{j} concerns only a consonantal
\emph{j} standing between the target vowel and the conditioning vowel, as
in the class I weak verbs of the *cnyssan* 'strike' type
[@Fulk2018, p. 56, §4.3]. Ringe and Taylor accordingly reconstruct the
Proto-West Germanic paradigm of 'yoke' with the lowering applied
[@RingeTaylor2014, p. 129].

The clearest corpus witnesses are [ġeoc]{.iv lang=oe sort=geoc role=evidence_form} 'yoke', *nosu* 'nose',
*sċofl* 'shovel', and *sorg* 'sorrow'. Where the following syllable kept a
high vowel the lowering did not apply, as in *ġeoguþ* 'youth', whose root \emph{u}
survived [@SieversBrunner1965, pp. 64--65, §92.1].

## SC017. Lowering of \emph{*u} before following non-high vowels (`PNWGmcULowering`) {#rule-PNWGmcULowering}

```foma
define PNWGmcULowering Ctx([
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
]);
```

Lowering of \emph{u} to \emph{o} is fixed on both sides by *ġeoc* 'yoke',
*nosu*, *sċofl* 'shovel', and *sorg*.

The lowering feeds the much later West Saxon palatal-glide spelling
([SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide)): the \emph{o} that the
scribes wrote in *ġeoc* 'yoke' is the output of this change, so PGmc
[júką]{.recon} 'yoke' passes through \emph{*joką} on its way to the
attested spelling [@Fulk2018, p. 56, §4.3; @RingeTaylor2014, p. 129].
After [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), PGmc
[núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected *nosu*,
PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected
*sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather
than expected *sorg*. These witnesses place
[SC017 PNWGmcULowering](#rule-PNWGmcULowering) before final long-\emph{o}
raising, and the *ġeoc* spelling shows its output surviving into the
written record.
