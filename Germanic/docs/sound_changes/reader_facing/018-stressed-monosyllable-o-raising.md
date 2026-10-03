# Stressed monosyllable \emph{*ō}-raising

## Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

The change is historically secure, but the tested forms determine no close relative position for it.
Its input is final \emph{*ō} in a stressed monosyllable.

## SC018. Raising of final stressed monosyllabic \emph{*ō} (`PNWGmcStressedMonosyllableORaising`) {#rule-PNWGmcStressedMonosyllableORaising}

```foma
define PNWGmcStressedMonosyllableORaising Ctx([
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
]);
```

Campbell's *cū* 'cow', *hū* 'how', and *tū* 'two' establish final stressed monosyllabic \emph{*ō} > \emph{*ū}.

Reversing [SC018 PNWGmcStressedMonosyllableORaising](#rule-PNWGmcStressedMonosyllableORaising) with neighboring changes leaves every output unchanged. The sound change is secure, but its exact position in the early history of long vowels rests on the handbooks.
