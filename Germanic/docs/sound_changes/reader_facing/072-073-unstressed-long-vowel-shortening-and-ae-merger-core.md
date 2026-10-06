# Unstressed long-vowel shortening and ae-merger

## Historical discussion

Campbell describes the shortening of unaccented long vowels, and Ringe and
Taylor place it among the last prehistoric Old English changes before the
merger of unstressed \emph{*æ} with \emph{*e}
[@Campbell1959, p. 148, §355; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) have a reciprocal
ordering relation. [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) supplies
the earlier boundary of shortening, and [SC085 OEHLoss](#rule-OEHLoss) the
later boundary of the merger.

## SC072. Shortening of unstressed long vowels (`OEUnstressedLongVowelShortening`) {#rule-OEUnstressedLongVowelShortening}

```foma
define OEUnstressedLongVowelShortening OEUnstressedLongVowelShortening1
    .o. OEUnstressedLongVowelShortening2
    .o. OEUnstressedLongVowelShortening3
    .o. OEUnstressedLongVowelShortening5
    .o. OEUnstressedLongVowelShortening6
    .o. OEUnstressedLongVowelShortening7
    .o. OEUnstressedLongVowelShortening8;
```

The rule shortens the remaining unstressed long vowels before weak final
syllables reach their later forms. A small group of lexical witnesses fixes its
chronology.

If the rule is moved before [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss), PGmc [fúrxtīnaz]{.recon} ‘fright’ yields [*fyrhten*]{.pred} rather than expected OE *fyrhte* ‘fright’. If the rule is delayed until after [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc [nḗdrōn]{.recon} ‘adder’ yields [*nǣdræ*]{.pred} rather than expected OE *nǣdre* ‘adder’, and PGmc [fádēr]{.recon} ‘father’ yields [*fædær*]{.pred} rather than expected *fæder* ‘father’. These outputs require [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) to follow [SC064 NWGmcInStemNLoss](#rule-NWGmcInStemNLoss) and precede [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

Shortening therefore follows the earlier weak-tail preparation and immediately
precedes the merger.

## SC073. Merger of unstressed \emph{*æ} with \emph{*e} (`OEUnstressedAEMerger`) {#rule-OEUnstressedAEMerger}

The following rule handles the merger stage.

```foma
define OEUnstressedAEMerger OEWeakTailReduction3;
```

The rule merges unstressed \emph{*æ} with \emph{*e} after shortening has
produced the weak final vowels, yielding the ordinary OE \emph{-e} spellings.

Its earlier and later relations are both concrete. If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [nḗdrōn]{.recon} ‘adder’ yields [*nǣdræ*]{.pred} rather than expected OE *nǣdre* 'adder', and PGmc [fádēr]{.recon} ‘father’ yields [*fædær*]{.pred} rather than expected *fæder* 'father'. If the rule is delayed until after [SC085 OEHLoss](#rule-OEHLoss), PGmc [táixōn]{.recon} ‘toe’ yields [*tāæ*]{.pred} rather than expected OE *tā* ‘toe’. These failures show that [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) must come before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), and that [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) must come before [SC085 OEHLoss](#rule-OEHLoss).

The lexical evidence fixes the local order after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and places the merger before the later h-loss and contraction.
