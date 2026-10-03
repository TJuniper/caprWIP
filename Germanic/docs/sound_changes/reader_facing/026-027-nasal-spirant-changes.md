# Nasal spirant changes

## Historical discussion

Germanic lost nasal consonants before voiceless fricatives twice, in two changes
that are easily confused because their outcomes look alike. Both replace a
sequence of vowel, nasal and fricative with a long nasalized vowel and the
fricative. They differ in date, in geography, and in which fricatives they
affect.

The earlier change is common Germanic and is treated in the opening chapter of
this book, on the Proto-Germanic loss of a nasal before [x]{.recon}. Its results
are shared by every daughter language, and only [a]{.recon}, [i]{.recon} and
[u]{.recon} occur in its input
[@Campbell1959, p. 44, §119; @Fulk2018, p. 55, §4.1;
@Ringe2017, pp. 149--150, §3.2.7].

The later change belongs to the dialects bordering the North Sea, that is to Old
English, Old Frisian and Old Saxon, the group traditionally called Ingvaeonic.
Here the
groups [mf]{.recon}, [ns]{.recon} and [nþ]{.recon} likewise reject the nasal with
compensatory lengthening and nasalization
[@Campbell1959, p. 47, §121; @Fulk2018, p. 72, §4.11;
@SieversBrunner1965, p. 176, §186.1; @Luick1914, p. 276, §301.1]. Ringe and Taylor call it the most obvious phonological
innovation of the northern dialects and list some thirty examples, among them
[gans]{.recon} ‘goose’ and [jugunþi]{.recon} ‘youth’
[@RingeTaylor2014, pp. 139--141]. Campbell describes it as a later change similar
to the common Germanic one, and Fulk as comparable to it; neither treats them as
the same law.

The two are told apart by what the languages outside the North Sea area show. The
common Germanic change left no nasal anywhere, so Old High German has *fūht*
‘damp’ and *fūst* ‘fist’ exactly as Old English does. The later change was
confined to the north, so the cognates of its witnesses keep the nasal: Old High
German *fimf*, *gans*, *ander*, *jugund* answer Old English *fīf* ‘five’, *gōs*
‘goose’, *ōþer* ‘other’, *ġeoguþ* ‘youth’. On this test [funhsti-]{.recon}
‘fist’, whose long vowel is shared by Old High German *fūst*, Dutch *vuist* and
German *Faust*, belongs to the earlier change and not to the North Sea law at all
[@Kroonen2013, p. 160].

Where the vowel was [a]{.recon}, the long nasalized vowel that this law produced
was afterwards rounded to *ō* in Anglo-Frisian, which is why Old English has
*gōs* ‘goose’, *tōþ* ‘tooth’ and *ōþer* ‘other’. That rounding is a third change again,
and it is the same rounding that gives *fōn* ‘seize’ and *þōhte* ‘thought’ from
the common Germanic law and *mōna* ‘moon’ and *spōn* ‘chip’ from inherited long
*ā* before a surviving nasal; Campbell states that it reached all three sources
at one and the same time [@Campbell1959, p. 50, §128 n. 1;
@SieversBrunner1965, p. 33, §26; @Fulk2018, p. 72, §4.11]. It is treated in the
chapter on the rounding of the long nasalized low vowel. That the vowel was
rounded and did not simply merge shows that its nasality survived the law that
created it: as Fulk observes, it did not fall together with the *ā* that came
from [ai]{.recon} [@Fulk2018, p. 55, §4.1]. Ringe and Taylor take the
nasalization to have remained subphonemic until it was lost separately in each
daughter [@RingeTaylor2014, p. 141]. Old Saxon shares the loss of the nasal and
the nasalization, and rounds only variably, which is why the law itself is
described as North Sea Germanic and the rounding as Anglo-Frisian
[@Campbell1959, p. 47, §121; @Fulk2018, p. 72, §4.11].

The North Sea Germanic law is a single connected sound change: in every handbook
account the nasal is lost *with* compensatory lengthening, and the lengthening is
the compensation for the loss. It is stated here as two rules only because the
vowel must be adjusted while the conditioning nasal is still present, before the
nasal can be removed. The order of
[SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) before
[SC027 EAFNasalSpirantLoss](#rule-EAFNasalSpirantLoss) is a requirement of the
statement, not evidence for two successive historical stages.

## SC026. North Sea Germanic nasal-spirant law, first step (`EAFNasalSpirantLengthening`) {#rule-EAFNasalSpirantLengthening}

```foma
define EAFNasalSpirantLengthening [
    {*a} -> {*ą̄} || _ EnglishStarNasal EnglishStarNSGmcSpirant,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarNSGmcSpirant,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarNSGmcSpirant,
    {*á} -> {*ą̄} || _ EnglishStarNasal EnglishStarNSGmcSpirant,
    {*í} -> {*ī} || _ EnglishStarNasal EnglishStarNSGmcSpirant,
    {*ú} -> {*ū} || _ EnglishStarNasal EnglishStarNSGmcSpirant
];
```

The environment is nasal plus [f]{.recon}, [þ]{.recon} or [s]{.recon}. The
fricative [x]{.recon} is excluded: nasal loss before [x]{.recon} is the earlier
change stated as
[SC103 PGmcNasalLossBeforeX](#rule-PGmcNasalLossBeforeX). Campbell names the
groups [mf]{.recon}, [ns]{.recon} and [nþ]{.recon}, Fulk says the change affects
[mf]{.recon}, [ns]{.recon} and [nþ]{.recon}, Sievers and Brunner name the
fricatives [f]{.recon}, [þ]{.recon} and [s]{.recon}, and no example in Ringe and
Taylor's list contains [x]{.recon}
[@Campbell1959, p. 47, §121; @Fulk2018, p. 72, §4.11;
@SieversBrunner1965, p. 176, §186.1; @RingeTaylor2014, pp. 139--141]. As in the
earlier change, only [a]{.recon}, [i]{.recon} and [u]{.recon} occur. The outcome
of [a]{.recon} is the long nasalized [ą̄]{.recon}, which
[SC104 EAFNasalizedLowRounding](#rule-EAFNasalizedLowRounding) later rounds; the
outcomes of [i]{.recon} and [u]{.recon} are written [ī]{.recon} and [ū]{.recon},
their nasality having no further consequence [@Campbell1959, p. 47, §121].

Two witnesses apply in the present corpus. PGmc [gánsz]{.recon} ‘goose’ becomes
[gą̄ns]{.recon} ‘goose’, and PGmc [júgunθ]{.recon} ‘youth’ becomes [júgūnθ]{.recon} ‘youth’. In
*ġeoguþ* ‘youth’ the syllable carrying the lengthened vowel is unstressed, and the length
is given up again by the later shortening of unstressed syllables; Sievers and
Brunner note the same course in *beraþ* ‘they carry’ from [beranþi]{.recon} ‘they carry’
through [berōþ]{.recon} ‘they carry’ [@SieversBrunner1965, p. 176, §186.1 Anm. 3;
@Luick1914, p. 276, §301.1].

If the rule is stated after the loss of the nasal, PGmc [gánsz]{.recon} ‘goose’ yields
[*ġeas*]{.pred} in place of *gōs* ‘goose’, and PGmc [júgunθ]{.recon} ‘youth’ yields
[*ġeogoþ*]{.pred} in place of *ġeoguþ* ‘youth’. This shows only that the vowel must be
adjusted before its conditioning nasal is removed. It does not establish a date
for either operation, and no earlier or later boundary is claimed here.

## SC027. North Sea Germanic nasal-spirant law, second step (`EAFNasalSpirantLoss`) {#rule-EAFNasalSpirantLoss}

```foma
define EAFNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarNSGmcSpirant
];
```

The nasal is removed in the environment that conditioned the lengthening, giving
[gą̄s]{.recon} ‘goose’ and [júgūθ]{.recon} ‘youth’. The rule completes the statement of the single
change begun in
[SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening); the two are
not independent sound laws. The converse test, stating the loss first, merely
reproduces the same two wrong forms. Nothing in the material fixes a later
boundary for the loss.
