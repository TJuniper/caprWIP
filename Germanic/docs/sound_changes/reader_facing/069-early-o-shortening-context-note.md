# Early o-shortening

## Historical discussion

After the principal palatal and umlautal changes, unstressed vowels undergo
shortening, fronting, merger, and sometimes complete loss. Campbell describes
the early shortening of unaccented long vowels, while Hogg, Ringe and Taylor,
and Fulk relate it to apocope, syncope, and the later reductions
[@Campbell1959, p. 148, §355; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

Early o-shortening has only a distant earlier boundary. The rules that follow,
especially [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
have more closely defined relations.

## SC069. Early shortening of unstressed \emph{*ō} before nasals (`OEEarlyOShortening`) {#rule-OEEarlyOShortening}

```foma
define OEEarlyOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ EnglishStarNasal
];
```

The rule shortens unstressed long \emph{*ō} before a following nasal. Because this shortening happens early, the resulting \emph{*a} can still participate in the later fronting and merger that shape many weak final syllables.

Moving the rule before
[SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss), PGmc [nḗdrōn]{.recon} ‘adder’ yields
[*nǣdran*]{.pred} rather than expected OE *nǣdre* ‘adder’, PGmc [érθōn]{.recon} ‘earth’ yields
[*eorþan*]{.pred} rather than expected *eorþe* ‘earth’, and PGmc [fláskōn]{.recon} ‘flask’ yields
[*flascan*]{.pred} rather than expected *flasce* ‘flask’. The same earlier shift also
disrupts forms such as *heorte* ‘heart’ and *līne* ‘line’. This broad set of
failures requires [SC069 OEEarlyOShortening](#rule-OEEarlyOShortening) to follow
[SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss).

If the rule is moved later within the tested sequence, no output differs from the
expected one. The lexical evidence therefore does not
identify a corresponding later constraint. The sources place early
\emph{*ō}-shortening before the later weak-tail changes without fixing a closer
local order.
