# \emph{mn}-dissimilation

## Historical discussion

In the inherited \emph{n}-stem paradigm the zero-grade oblique cells brought
\emph{m} and \emph{n} into direct contact, and in that adjacent cluster the
labial nasal dissimilated to a labial spirant: \emph{mn} > \emph{βn} (surfacing
as \emph{fn}). Old Norse preserves the older paradigmatic distribution, with the
labial confined to the oblique cluster (\emph{himinn} 'heaven' beside dative
\emph{hifni}); Old English and Old Saxon generalized it. Fulk treats the cluster
change among developments common to Germanic, while warning that its surface
results are irregular and that reverse \emph{bn} > \emph{mn} is later well
attested in Northwest Germanic [@Fulk2018, p. 121, §6.11]. The relevant
\emph{heofon} 'heaven' and \emph{mōnaþ} 'month' material is discussed by Campbell
[@Campbell1959, pp. 189, 195, §§470, 484].

The underlying cluster change is therefore late Proto-Germanic / Common
Germanic, not securely a pan-Northwest-Germanic innovation; `PNWGmc` remains a
stable executable identifier only. The lexical evidence does not constrain a
positive local cascade position.

## SC022. Dissimilation of adjacent \emph{mn} (`PNWGmcMnDissimilation`) {#rule-PNWGmcMnDissimilation}

```foma
define PNWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _ {*n}
];
```

The rule fires only where \emph{m} stands directly before \emph{n}. It supplies
the labial of \emph{stefn} 'stem, trunk' from the \emph{mn}-cluster of the
\emph{stamn}-family, and it is the historical change behind the labial of
\emph{heofon} 'heaven', which was generalized from the oblique cluster into the
vowel-bearing stem before the Old English vocalic changes. (An earlier
cross-syllable formulation that labialized an intervocalic \emph{m} before a
later nasal has been retired: it simulated paradigm levelling rather than a sound
law.)

Moving [SC022 PNWGmcMnDissimilation](#rule-PNWGmcMnDissimilation) earlier or later leaves every output unchanged. Its executable place in this holding zone is therefore editorial/computational, while its historical classification rests on the handbook account of \emph{mn}-dissimilation.
