# West Germanic rhotacism

## Historical discussion

Bammesberger states that Germanic \emph{*z} yielded \emph{*r} in intervocalic position in Old English, while final \emph{*z} was generally lost [@Bammesberger1992, p. 39]. Ringe and Taylor argue that this merger of \emph{*z} with \emph{*r} was independent in Norse and West Germanic and belongs after the Proto-West-Germanic stage [@RingeTaylor2014, pp. 52, 98, 102]. Crist likewise places rhotacism after earlier West Germanic \emph{*z}-deletion rules and rejects treating it as an inherited Proto-Northwest-Germanic innovation [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].

The internal identifier [SC003 EAFRhotacism](#rule-EAFRhotacism) places the change in CAPR's Early Anglo-Frisian corridor, the operational post-Proto-West-Germanic stage on the English line; historically the change is a West Germanic rhotacism, later than Proto-Germanic. It is also distinct from [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion), which removes final \emph{*z} before the surviving medial consonant becomes \emph{*r}.

## SC003. West Germanic rhotacism (`EAFRhotacism`) {#rule-EAFRhotacism}

```foma
define EAFRhotacism [
    {*z} -> {*r} || EnglishStarVocalic _ ?
];
```

Breaking supplies the decisive upper boundary. If rhotacism is delayed until after [SC044 OEBreaking](#rule-OEBreaking), PGmc [líznōjaną]{.recon} ‘learn’ yields [*lirnian*]{.pred} rather than expected OE *liornian* ‘learn’, PGmc [líznōθi]{.recon} ‘learns’ yields [*lirnaþ*]{.pred} rather than expected *liornaþ* 'learns', PGmc [líznô]{.recon} ‘learn’ yields [*lirna*]{.pred} rather than expected *liorna* 'learn', and PGmc [mízdai]{.recon} ‘meed’ yields [*merde*]{.pred} rather than expected OE *meorde* ‘meed’. Moving rhotacism earlier within the tested range changes no output.

The lexical evidence thus supplies a terminus ante quem but no terminus post quem. The lower boundary rests on the historical analyses cited above: Ringe and Taylor put rhotacism at the end of the sequence of \emph{*z}-losses — "first \emph{*z} was lost in a variety of environments ..., then all surviving \emph{*z} became \emph{*r}" [@RingeTaylor2014, p. 87, §3.3.1] — and Crist observes that the deletions distinguish \emph{*z} from \emph{*r} and so must precede the merger [@Crist2002, pp. 2--3]. The rule is accordingly ordered after the three final-\emph{*z} losses ([SC096 RootNounNomZLoss](#rule-RootNounNomZLoss), [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion), and [SC097 MonosyllabicFinalZLoss](#rule-MonosyllabicFinalZLoss)) and before breaking, so that the derivation follows the reconstructed chronology.
