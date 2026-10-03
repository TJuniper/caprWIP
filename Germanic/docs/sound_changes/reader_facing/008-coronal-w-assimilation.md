# Coronal-w assimilation

## Historical discussion

Ringe and Taylor treat the assimilation of \emph{*dw} and \emph{*zw} to \emph{*ww} as a shared Proto-West-Germanic innovation supported by one example of each input cluster [@RingeTaylor2014, pp. 56--57; @Stiles1985, pp. 89--94]. The \emph{*dw} example is the numeral 'four': PGmc \emph{*feðwor} (Gothic \emph{fidwor}) → WGmc \emph{*fewwar} → OE \emph{fēower}, Old Frisian \emph{fiuwer}, Old Saxon \emph{fiuwar}. The \emph{*zw} example is the second-person plural pronoun, where two oblique case forms show the change: acc./dat.\ PGmc \emph{*izwiz} (Gothic \emph{izwis}) → OE \emph{eow}, Old Frisian \emph{iu}, Old Saxon \emph{iu}, OHG \emph{iu}; and gen.\ Ringe and Taylor's PGmc \emph{*izweraz} (Gothic \emph{izwara}) → OE \emph{eower}, OHG \emph{iuwer} [@RingeTaylor2014, p. 56]. Stiles discusses the same pronominal material using his own reconstruction conventions and explicitly treats Gothic \emph{izwara} among the relevant comparanda [@Stiles1985, pp. 89--94]. These two case forms belong to a single pronominal paradigm, not to two independent etyma.

The historical support rests on a small witness set. Both coronal inputs assimilate before \emph{*w}, but the evidence for each cluster is confined: the numeral alone supplies the \emph{*dw} instance, and the oblique case forms of the second-person plural pronoun supply the \emph{*zw} instance. Both clusters are now witnessed in the corpus: 'four' for \emph{*dw}, and 'you' — selected in its dat.(-acc.) plural cell \emph{*izwiz} — for \emph{*zw}, deriving through \emph{*iwwi}, apocopated \emph{*iww}, to OE *ēow* 'you' [@RingeTaylor2014, pp. 41--42, §3.1.1; @Fulk2018, §8.3, pp. 204--205].

## SC008. Assimilation of coronal consonants before \emph{*w} (`PWGmcCoronalWAssimilation`) {#rule-PWGmcCoronalWAssimilation}

```foma
define PWGmcCoronalWAssimilation Ctx([
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
]);
```

OE *fēower* ‘four’ exposes a feeding relation: coronal assimilation creates the \emph{*ww} input of the early reanalysis in [SC031 OEWWSimplification](#rule-OEWWSimplification), yielding the diphthongal intermediate before later English realization. Ringe and Taylor explicitly give the coronal-assimilation and glide-reanalysis sequence [@RingeTaylor2014, pp. 41--42]. The earlier displacement result belonged to the superseded late \emph{*ww}-deletion proxy and does not by itself predict the result of displacing the reformulated early operation.

The numeral fixes that relative order. The pronoun now fixes a second one: assimilation must precede rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)). The \emph{*z} of \emph{*izwiz} stands between vowel and \emph{*w}; had rhotacism applied first, it would have produced [*irwiz*]{.pred}, from which OE *ēow* 'you' can never be derived. The executable cascade composes the assimilation well before rhotacism, and the corpus derivation of *ēow* 'you' fails if the two are reversed. 'Four' remains the sole \emph{*dw} witness and the sole source of the coronal-assimilation → *ww*-simplification ordering constraint. The earlier boundary of the assimilation remains undetermined.
