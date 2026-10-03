# \emph{ij}-contraction in \emph{friend}

## Historical discussion

Ringe and Taylor describe a change of \emph{*ijo} to \emph{*iu} in the ancestor of \emph{friend}, with the pathway PGmc \emph{*frijōnd-} (Gothic \emph{frijonds}) → PWGmc \emph{*friund} → OE \emph{frēond}, Old Frisian \emph{frīund}, Old Saxon \emph{friund}, Old High German \emph{friunt} [@RingeTaylor2014, p. 62]. The same source immediately warns that the \emph{*ijo} sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62]. Luick (printed p. 118) notes that \emph{iu} generalised within several \emph{j}-stem paradigms through a related but differently conditioned loss of \emph{j}, but does not supply a second example of the exact stressed \emph{*ijo} sequence [@Luick1914, p. 118].

The change concerns a rare sequence attested only in the \emph{*frijōnd-} etymon and cannot safely be generalized into a broadly productive rule.

## SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

```foma
define PWGmcIjContraction Ctx([
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
]);
```

Only the \emph{*frijōnd-} etymon tests this contraction. If the rare \emph{*ijō} sequence survives until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc [fríjōndz]{.recon} ‘friend’ yields [*friund*]{.pred} rather than expected OE *frēond* 'friend'; moving contraction earlier within the tested range changes no output.

That single contrast places [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) before diphthong leveling but gives no lower boundary. It cannot establish a productive sound law beyond the \emph{*frijōnd-} etymon, precisely the reservation made by Ringe and Taylor.
