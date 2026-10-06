# Post-apocope \emph{*n}-loss and medial syncope

## Historical discussion

Evidence for post-apocope reduction is strikingly uneven. The inherited
feminine \emph{in}-stem represented by Gothic \emph{faurhtei}, OE \emph{fyrhtu},
and oblique OE \emph{fyrhte} supplies the relevant evidence
[@Orel2003, p. 120; @RingeTaylor2014, pp. 380--381; @Campbell1959, p. 236, §589.7].
No comparable witness orders the medial syncope that follows. Hogg, Ringe and Taylor, and Fulk describe both
processes within the late history of weak syllables
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6].

## SC064. Loss of stem-final \emph{*n} after long \emph{*ī} (`NWGmcInStemNLoss`) {#rule-NWGmcInStemNLoss}

```foma
define NWGmcInStemNLoss [{*n} -> 0 || {*ī} _ .#.];
```

Only final \emph{*n} after long \emph{*ī} is at issue, as in the inherited
\emph{in}-stem behind OE \emph{fyrhte} ‘fright’.

CAPR models the oblique OE form through the Proto-Germanic genitive singular
[fúrxtīnaz]{.recon} 'fright', following the project convention of using an appropriate
non-nominative paradigm cell when the nominative does not supply the required
derivation. Within this selected genitive derivation, the same input fixes both
ordering boundaries. Before
[SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), PGmc
[fúrxtīnaz]{.recon} ‘fright’ yields [*fyrhten*]{.pred} rather than expected OE *fyrhte* ‘fright’.
After [SC072
OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc
[fúrxtīnaz]{.recon} again yields [*fyrhten*]{.pred} rather than expected *fyrhte* 'fright'. I
therefore order final bare-a loss, stem-final n-loss, and unstressed long-vowel
shortening in that sequence. Both boundaries are firm within the selected
genitive derivation and depend on one inherited lexeme/paradigm.

## SC065. Medial syncope before dentals after heavy syllables (`OEMedialSyncope`) {#rule-OEMedialSyncope}

Loss of medial \emph{*i} before dentals belongs to the late weak-tail history
described by Hogg, Ringe and Taylor, and Fulk
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6].

```foma
define OEMedialSyncope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}],
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ [{*θ}|{*ð}|{*d}|{*t}]
];
```

No diagnostic word establishes a local chronology. Moving medial syncope to
either end of the tested range leaves every output unchanged. Its
handbook placement after apocope and before later cluster simplification
therefore remains preferable, but the present lexicon cannot demonstrate it.
