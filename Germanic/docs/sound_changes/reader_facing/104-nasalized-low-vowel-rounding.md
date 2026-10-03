# Anglo-Frisian rounding of the long nasalized low vowel

## Historical discussion

Three separate developments described in earlier chapters end in the same
sound: a long, nasalized, low vowel. The oldest is the Proto-Germanic loss of a
nasal before [x]{.recon}; the second is the North Sea Germanic nasal-spirant
law; the third is the nasalization of the inherited long *ā* before a nasal that
survived. In Old English and Old Frisian all three surface as *ō*, and Campbell
states the unification without qualification: the nasalized vowel became
identical with the *ō* inherited from Proto-Germanic already in prehistoric Old
English, and the same change affected the nasalized vowel of the Proto-Germanic
law and the nasalized vowel of the Ingvaeonic law at one and the same time
[@Campbell1959, p. 50, §128 n. 1]. One later sound change therefore accounts for
all three, and the appearance of three independent roads to *ō* is an illusion
created by looking only at the Old English surface.

That the intermediate vowel was nasalized and unrounded is shown by a form in
which it was shortened very early. Campbell's example is *samcucu* ‘half alive’,
where the shortened reflex is *a* and never *o*; the vowel that the earlier laws
produced was therefore a nasalized [ą̄]{.recon}, and the rounding is a distinct
and later event [@Campbell1959, p. 50, §128 n. 1]. Sievers and Brunner describe
the same nasalized long vowel and its rounded Old English outcome
[@SieversBrunner1965, p. 33, §26; p. 58, §64].

The geography is Anglo-Frisian. Old Saxon nasalized its stressed low vowels
along with the rest of the northern West Germanic area
[@RingeTaylor2014, p. 142, §5.1.2], and it shares the loss of the nasal in both
of the earlier laws; the categorical, systematic rounding, however, it does not
share. For the
Proto-Germanic nasalized low vowel Old Saxon retains *ā* consistently, and for
the vowel created by the nasal-spirant law it has *ā* or *ō* according to word
and dialect, while Old English and Old Frisian have *ō* throughout
[@Campbell1959, p. 44, §119; @Fulk2018, p. 72, §4.11]. That partial and
lexically variable Old Saxon rounding is comparative evidence bearing on the
innovation rather than participation in it. Ringe treats the rounding
as a parallel development of the diverging northern dialects and locates it in
the northernmost of them, that is in Anglo-Frisian
[@Ringe2017, pp. 149--150, §3.2.7; @RingeTaylor2014, p. 142, §5.1.2]. Luick
groups the whole set of changes among those peculiar to the Anglo-Frisian
dialect group and notes that the nasalized vowel later gave up its nasality
[@Luick1914, p. 276, §301.1]. The rounding is accordingly Anglo-Frisian, and the
nasalization that feeds it is the wider North Sea Germanic property.

Ringe and Taylor confirm that a single rounding covers all the sources: the
rounding affected the nasalized low vowels of the nasal-spirant law, the
nasalized low vowels of the accompanying list, and the reflexes of
Proto-Germanic \emph{*/anh/} alike [@RingeTaylor2014, p. 142, §5.1.2]. The
condition on the input is nasality and nothing else, which is why the long *ā*
that Old English later won from [ai]{.recon} escapes: that vowel was oral, and
it came into being after the rounding had run its course. Fulk makes this the
central argument for the long survival of the nasality, since the nasalized
vowel developed to *ō* and did not fall together with Old English *ā* from
[ai]{.recon} [@Fulk2018, p. 55, §4.1].

## SC104. Rounding of the long nasalized low vowel (`EAFNasalizedLowRounding`) {#rule-EAFNasalizedLowRounding}

```foma
define EAFNasalizedLowRounding [
    {*ą̄} -> {*ō}
];
```

The rule is unconditioned, since the vowel it operates on exists only where one
of the three earlier changes created it. Its inputs arrive from
[SC103 PGmcNasalLossBeforeX](#rule-PGmcNasalLossBeforeX), from
[SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) and from
[SC025 EAFLongANasalRounding](#rule-EAFLongANasalRounding), and each of those
three stands in a feeding relation to it: stated before any one of them, the
rule leaves that source's nasalized vowel untouched and the cascade returns no
form at all for its witnesses.

Four lexemes in the present corpus reach Old English through this rule, and
between them they witness all three sources.
[gánsz]{.recon} ‘goose’ arrives as [gą̄s]{.recon} ‘goose’ from the North Sea Germanic
law and gives *gōs* ‘goose’; [mḗnōθz]{.recon} ‘month’ arrives as [mą̄nōþ]{.recon} ‘month’ and
gives *mōnaþ* ‘month’; [spḗnuz]{.recon} ‘spoon’ arrives as [spą̄nu]{.recon} ‘spoon’ and gives
*spōn* ‘spoon’. The Proto-Germanic law contributes [θánxtē]{.recon} ‘thought’, the preterite of
the verb ‘to think’, which arrives as [θą̄xtē]{.recon} ‘thought’ and gives *þōhte*
‘thought’. That is the very form cited for this rounding, beside Old Frisian
*thochte*, and it is the evidence that the vowel did not fall together with the
*ā* of *stān* ‘stone’ [@Fulk2018, p. 55, §4.1; @Campbell1959, p. 44, §119]. The other
firing of the Proto-Germanic law, the high vowel of *fȳst* ‘fist’, does not
reach this rule at all.

The counterpart is what the rule leaves alone. [stáinaz]{.recon} ‘stone’ and
[xáimaz]{.recon} ‘home’ acquire their long *ā* from
[SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization), which follows
this rule, and their vowel was never nasalized; they surface as *stān* ‘stone’ and
*hām* ‘home’. Placing the monophthongization before the nasalization and the rounding
makes that vowel eligible and the cascade then yields [*stōn*]{.pred} and
[*hōm*]{.pred}, which is the chronological inference Campbell draws for the
treatments of the old low vowel generally
[@Campbell1959, pp. 52--53, §132; @RingeTaylor2014, pp. 169--170].
