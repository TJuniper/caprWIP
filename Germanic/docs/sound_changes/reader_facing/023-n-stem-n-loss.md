# Word-final \emph{n}-loss

## Historical discussion

The change isolated here is far older than its position in the cascade suggests: it is the general (pre-)Proto-Germanic loss of word-final \emph{*n}, with nasalization of the preceding vowel, in polysyllables. Ringe's proof set for the law spans the whole grammar — nouns such as \emph{*yugón} > \emph{*juką} 'yoke', pronouns such as \emph{*tón} > \emph{*þanǭ}, and even the verb form \emph{*dedǭ} 'I did' — so it is general phonology, not a fact about any one declension [@Ringe2017, pp. 101--103]. Gothic \emph{tuggo} shares the weak nominative-singular outcome, and the nasalized reflex \emph{*-ǭ} remained contrastive into Proto-West Germanic before yielding OE \emph{-e} [@RingeTaylor2014, pp. 54--55, 58--59].

Within the present corpus the change surfaces in exactly one shape: the weak nouns are cited in the stem form \emph{*-ōn-}, and this rule carries them to the Proto-Germanic nominative singular in \emph{*-ǭ}, as in \emph{*túngōn} > \emph{*túngǭ} > *tunge* 'tongue', alongside *eorþe* 'earth', *heorte* 'heart', *nǣdre* 'adder', and thirteen further weak nouns. The masculine weak nominative singular in trimoric \emph{*-ô} never had a final \emph{*-n} to lose, and Proto-Germanic \emph{*sebun} 'seven', \emph{*nigun} 'nine', and \emph{*tehun} 'ten' kept their \emph{-n} by lexical analogy among the numerals [@Ringe2017, p. 103]; the rule's narrow \emph{*-ōn} environment leaves all of these correctly untouched.

## SC023. Loss of word-final \emph{*n} after \emph{*ō} (`PNWGmcNStemNLoss`) {#rule-PNWGmcNStemNLoss}

```foma
define PNWGmcNStemNLoss [
    {*ō} {*n} -> {*ǭ} || _ .#.
];
```

The verb *dōn* 'do' supplies the negative, counterfeeding witness for the chronology. PGmc [dōną]{.recon} 'do' passes this rule untouched; only [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) later strips the final [ą]{.recon} and creates a new word-final [-ōn]{.recon}. That secondary [-n]{.recon} survives into *dōn* precisely because the old loss was no longer active: if [SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss) is displaced after the apocope, it consumes the new nasal and the derivation collapses entirely (\emph{+?}).

The retained \emph{-n} of *dōn* 'do' therefore supplies a terminus ante quem for the loss — it must be dead before the apocope — while the seventeen weak nouns above are its positive witnesses; the lower boundary remains unattested within the cascade, as befits a change already complete in Proto-Germanic.
