# J-cluster coalescence

## Historical discussion

Only a small lexical group reveals the coalescence of velars with \emph{*j}.
Plain-velar and \emph{*sk} palatalization must already have run before
\emph{*gj} and \emph{*kj} acquire their later outcomes.
Campbell, Ringe and Taylor, and Fulk discuss the palatalized and fronted
outcomes in *bīeġan* ‘bend’ and *sēċan* ‘seek’ without assigning this later
cluster adjustment the status of a major sound law [@Campbell1959, pp. 89,
107--108, §§170, 248--251; @RingeTaylor2014, pp. 213--251, §§6.4.1, 6.5.1,
6.6.1--6.6.4; @Fulk2018, pp. 65, 75, §§4.7, 4.13].

## SC057. Coalescence of velar + \emph{*j} clusters (`OEJClusterCoalescence`) {#rule-OEJClusterCoalescence}

```foma
define OEJClusterCoalescence (
    [{*g} {*j} -> {*ʤ}]
    .o. [{*k} {*j} -> {*ʧ}]
);
```

The forms *bīeġan* ‘bend’ and *sēċan* ‘seek’ determine the earlier boundary.
If coalescence precedes [SC052
OEVelarPalatalization](#rule-OEVelarPalatalization),
the developments behind *bīeġan* ‘bend’ and *sēċan* ‘seek’ are lost. Related
forms such as *fylġan* ‘follow’,
*heċġ* ‘hedge’, and *sengan* ‘singe’ fail in the same broader palatalization
zone. PGmc [báugijaną]{.recon} 'bow' yields [*bēaġan*]{.pred} rather than expected OE *bīeġan*,
and PGmc [sōkijaną]{.recon} 'seek' yields [*sōċan*]{.pred} rather than expected *sēċan*. This
constrains this computational cluster consumer. It does not independently
date all singleton-fricative articulation or merger: the latter is distinct
from this rule and is now explicit under
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger)
[@RingeTaylor2014, p. 204; @Laker2007, pp. 167--168].
Nothing in the present lexicon supplies a terminus ante quem for the
cluster consumer.
