# North Sea Germanic nasalization of long \emph{ā} before a nasal

## Historical discussion

In the dialects along the North Sea coast the long low vowel \emph{*ā} —
centrally the vowel produced from \emph{*ē₁} by the Northwest Germanic lowering
— was nasalized when a nasal consonant followed and survived. The nasalized
vowel was afterwards rounded in Anglo-Frisian, which is why Old English has
*mōna* ‘moon’, *mōnaþ* ‘month’ and *spōn* ‘spoon’ against Old High German
*māno* ‘moon’, *mānōd* ‘month’, *spān* ‘spoon’ and Old Norse *máni* ‘moon’, *mánaðr* ‘month’, *spánn* ‘spoon’. Campbell
describes the split of Germanic \emph{ǣ¹} before nasals in these terms and
identifies the vowel that the rounding operated on as a nasalized and unrounded
[ą̄]{.recon} [@Campbell1959, p. 50, §127; p. 50, §128 n. 1]. Fulk places the
rounded outcome of \emph{*ǣ} before nasals among the Anglo-Frisian changes and
derives it from an earlier nasalized vowel [@Fulk2018, pp. 72--73, §4.12].

The nasalization and the rounding have different geographies, and separating
them resolves an apparent disagreement in the handbooks. Ringe and Taylor state
that stressed low vowels were nasalized in the northern West Germanic dialects,
Old Saxon among them [@RingeTaylor2014, p. 142, §5.1.2]; Old Saxon accordingly
shows *ōdar* ‘other’ and *sōd* ‘true’ beside unrounded *quān* ‘wife’ and *sāno*
‘immediately’ [@RingeTaylor2014, pp. 150--151]. What Old Saxon shares is the
nasalization; what it shares only in part is the rounding, and for the vowel
inherited from Proto-Germanic it does not share the rounding at all
[@Campbell1959, p. 44, §119; @Fulk2018, p. 72, §4.11]. The nasalization stated
here is therefore North Sea Germanic, and the rounding treated in the chapter on
the long nasalized low vowel is Anglo-Frisian.

The nasalization is the conditioned counterpart of the fronting of oral
\emph{*ā} treated in the fronting chapter: a following nasal gives nasalization
and eventual rounding, and its absence gives fronting. Together the two exhaust
the fate of the old low vowel in this area. The comparative material does not
order the two branches against each other, and no such ordering is claimed here.

## SC025. Nasalization of long \emph{ā} before nasals (`EAFLongANasalRounding`) {#rule-EAFLongANasalRounding}

```foma
define EAFLongANasalRounding [
    {*ā} -> {*ą̄} || _ EnglishStarNasal
];
```

The rule consumes the \emph{*ā} created by
[SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering): displacing the lowering
after this rule leaves the nasalization without an input, and [mḗnōθz]{.recon}
‘month’ surfaces as [*mānaþ*]{.pred} in place of OE *mōnaþ* ‘month’, [spḗnuz]{.recon}
‘spoon’ as [*spān*]{.pred} in place of *spōn* ‘spoon’. Its output is consumed in turn by
[SC104 EAFNasalizedLowRounding](#rule-EAFNasalizedLowRounding), which supplies
the rounded vowel that the two words actually show.

Equally important is what the rule must precede. The monophthongization of
\emph{*ai} in [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization)
creates a new long \emph{ā}, and that vowel was never nasalized and never
rounded before nasals: *stān* ‘stone’ and *hām* ‘home’ keep \emph{ā}. Stating
the monophthongization before this rule makes the new vowel eligible for
nasalization and hence for rounding, and the cascade then wrongly yields
[*stōn*]{.pred} and [*hōm*]{.pred}. This is the same chronological inference
Campbell draws for the fronting: the treatments of the old low vowel were
complete, or at least under way, before \emph{ai}-monophthongization supplied a
new one [@Campbell1959, pp. 52--53, §132; @RingeTaylor2014, pp. 169--170].
