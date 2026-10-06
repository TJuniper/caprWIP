# Late syncope and degemination

## Historical discussion

Vowel loss creates the clusters upon which later assimilation and degemination
operate. Hogg and Ringe and Taylor describe this dependence, while Brunner's
*netle* 'nettle' beside later *netele* 'nettle' supplies a concrete lexical type
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--296, §§6.7.3--6.8.2;
@SieversBrunner1965, pp. 144--145, §§158--159]. Fulk places this syncope after
i-umlaut [@Fulk2018, p. 91, §5.6].

The three relations are not equally secure. Lexical evidence orders syncope
and degemination; the intervening dental assimilation has no independent
ordering witness.

## SC066. L-adjacent syncope in medial syllables (`OELAdjacentSyncope`) {#rule-OELAdjacentSyncope}

```foma
define OELAdjacentSyncope [
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l}
];
```

The loss of medial \emph{*i} before \emph{*l} is late enough to preserve
earlier umlaut, as *netle* ‘nettle’ and *spinl* ‘spindle’ demonstrate.

Placed before i-umlaut, PGmc [nátilōn]{.recon} ‘nettle’ yields [*nætle*]{.pred} rather than
expected OE *netle* ‘nettle’, and PGmc [spénnilō]{.recon} ‘spindle’ yields [*spenl*]{.pred} rather
than expected *spinl* ‘spindle’. Placed after preconsonantal degemination, PGmc
[spénnilō]{.recon} yields [*spinnl*]{.pred} rather than expected *spinl*. The witnesses
therefore establish the sequence i-umlaut, l-adjacent syncope, preconsonantal
degemination. The first relation separates two historical phases; the second is
a direct feeding relation, since syncope creates the cluster that degemination
simplifies.

## SC067. Dental assimilation in newly formed clusters (`OEDentalAssimilation`) {#rule-OEDentalAssimilation}

```foma
define OEDentalAssimilation [
    {*θ} -> 0 || {*t} _
];
```

Loss of \emph{*θ} after \emph{*t} resolves a dental cluster produced by syncope
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].
No witness distinguishes its position: moving dental assimilation across every
tested neighbor leaves the outputs unchanged. I nevertheless place it after
syncope, which supplies its input, and before the more general cluster
simplification described in the handbooks. This order is phonologically
motivated, not established by a lexical contrast.

## SC068. Preconsonantal degemination before sonorants (`OEPreconsonantalDegemination`) {#rule-OEPreconsonantalDegemination}

```foma
define OEPreconsonantalDegemination OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN;
```

Preconsonantal \emph{*tt} and \emph{*nn} simplify only after syncope has
created a following sonorant cluster, as in *spinl* ‘spindle’
[@RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

Placed before l-adjacent syncope, PGmc [spénnilō]{.recon} ‘spindle’ yields [*spinnl*]{.pred} rather
than expected OE *spinl* ‘spindle’. Syncope must therefore create the cluster
before degemination simplifies it. Reordering degemination against any tested
later change leaves the witness unchanged, so no terminus ante quem is known.
