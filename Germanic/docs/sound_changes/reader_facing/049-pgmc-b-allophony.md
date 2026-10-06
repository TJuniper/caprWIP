# B allophony

## Historical discussion

The positional alternation of Germanic \emph{*b} is a Proto-Germanic distributional feature. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@HoggPhonology1992, p. 108]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic \emph{*b} as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

The distribution is narrow, but later changes presuppose the stop-fricative
alternation. CAPR implements the rule at a late cascade position for computational
reasons: the alternation must interact with consonant environments shaped by
intermediate rule applications. Its historical stage is Proto-Germanic.

## SC049. Distribution of \emph{*b} after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony}

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

The handbooks describe \emph{*b}/\emph{*bb} as a positional alternation within the consonant system, and one compound supplies its chronological consequence. Before [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope), *reġnboga* 'rainbow' develops as [*reġnfoga*]{.pred} rather than expected OE *reġnboga*; later placement creates no comparable failure. The witness places b-allophony after compound-linking syncope without turning the alternation into an independent sound law.
