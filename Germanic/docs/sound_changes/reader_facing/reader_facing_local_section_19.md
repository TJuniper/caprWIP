# The ordered sound-change sequence

## Scope and orientation

The sequence begins with early West Germanic consonant and vowel changes and ends with Old English r-metathesis.

Rhotacism, brightening, breaking, umlaut, and apocope alternate with narrowly conditioned changes whose relative order rests on particular witness words.

The evidence ranges from broadly attested sound laws to lexical constraints that establish only one chronological boundary.

## Numbering note

SC numbers remain the established legacy identifiers. The Version 1 book presents the changes in historical chapter order, which differs from the computational cascade order for several rules.

SC038, SC062, and SC084 mark technical or prosodic stages rather than sound changes; SC077 is unused.


\newpage

# Chapter 1. From Proto-Germanic to Proto-Northwest Germanic


## Historical interval

This chapter covers developments that took place within the Proto-Germanic
period, from the inherited consonant system to the first changes that separate
the Northwest Germanic line from the rest of the Germanic family.

The reconstruction labelled Proto-Germanic here is the common ancestor of Gothic,
North Germanic, and West Germanic, reconstructed through the classical comparative
method from attested descendant languages. The label Proto-Northwest Germanic
designates the hypothetical node linking the ancestors of North Germanic (Old
Norse and its relatives) and West Germanic (Old English, Old High German, Old
Saxon, and Old Frisian among others), to the exclusion of Gothic and the other
East Germanic varieties.

## What this chapter contains

Chapter 1 contains one reader-facing sound-change section: the positional
allophony of Proto-Germanic \emph{*b}, implemented as `SC049 PGmcBAllophony`.
The rule governs the distribution of \emph{*b} as a stop versus a voiced
bilabial fricative \emph{*β} depending on syllabic environment. Hogg, Ringe
and Taylor, and Luick all identify this distribution as a Proto-Germanic
feature [@HoggPhonology1992, p. 108; @RingeTaylor2014, p. 121; @Luick1914, p. 107].

CAPR implements this rule late in the computational cascade because the
alternation interacts with environments shaped by intermediate rule
applications. The cascade placement therefore diverges from the historical
stage; the reader-facing section notes this divergence explicitly.

One other historically Proto-Germanic change, Gm-simplification
(`SC002 PGmcGmSimplification`), is documented in the book-entry plan and
its literature dossier confirms the source base is narrow (two lexical
families: [draugma-]{.recon .iv lang=pgmc sort=draugma} 'dream' and
[taugma-]{.recon .iv lang=pgmc sort=taugma} 'team'; [@Kroonen2013, pp. 101, 511]).
A reader-facing section for SC002 awaits a stronger explanatory source base
and is not yet assembled in the reader-facing sequence.

## Scope and genealogical context

Changes in this chapter are pan-Germanic in scope: they apply to ancestral forms
that feed both the North Germanic and West Germanic descendants, or they represent
internal Proto-Germanic processes visible across the Germanic family.

The boundary between Proto-Germanic and Proto-Northwest Germanic is not sharp in
the textbook literature. Ringe and Taylor treat many of the traditionally
"Proto-Germanic" changes as part of a shared innovation package that is
diagnostically older than North–West Germanic divergence but not necessarily
earlier than the separation of the East Germanic line
[@RingeTaylor2014, pp. 1--30]. For book purposes, the distinction matters
primarily because it separates the features inherited uniformly from all Germanic
from those shared selectively by North and West Germanic to the exclusion of
Gothic.

## A note on the rule names

The CAPR rules implemented in this chapter carry names beginning with `PGmc`.
Those names are intended as stable internal identifiers, not as claims about
the precise historical stage of every rule so labelled. A rule named `PGmcX`
may in some cases be a later development that affects only the West Germanic
or Northwest Germanic branch; the chapter assignment in this staging map takes
priority over the rule-name prefix for historical organization purposes.

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

## \CAPRRuleHeading{SC049. Distribution of \emph{*b} after vowels and liquids}{PGmcBAllophony} {#rule-PGmcBAllophony}

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

The handbooks describe \emph{*b}/\emph{*bb} as a positional alternation within the consonant system, and one compound supplies its chronological consequence. Before [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope), *reġnboga* 'rainbow' develops as [*reġnfoga*]{.pred} rather than expected OE *reġnboga*; later placement creates no comparable failure. The witness places b-allophony after compound-linking syncope without turning the alternation into an independent sound law.

\newpage

# Chapter 2. From Proto-Northwest Germanic to Proto-West Germanic


## Historical interval

This chapter covers the sound changes that took place in the proto-language shared
by the West Germanic languages — Old English, Old Frisian, Old Saxon, Old High
German, and Old Dutch — before the individual languages diverged. The starting
reconstruction is Proto-Northwest Germanic (PNWGmc), the hypothetical common
ancestor of North Germanic and West Germanic together; the ending reconstruction
is Proto-West Germanic (PWGmc), the immediate common ancestor of the West Germanic
languages specifically.

## Scope and internal diversity

Changes in this chapter are not all equally pan-West-Germanic in scope. They
may be grouped broadly as follows:

Northwest Germanic innovations (shared by both North and West Germanic):
innovations in the unstressed vowel system, certain final-syllable vowel changes,
and selected consonant cluster simplifications. Changes labelled `NWGmc` in the
CAPR rule names fall here, though rule prefixes are not always reliable guides to
historical scope.

Proto-West-Germanic innovations (shared within West Germanic but not in
North Germanic): the cluster of morphological and phonological changes that
distinguish Old English, Old High German, Old Saxon, and Old Frisian from Old
Norse. Changes labelled `PWGmc` in the CAPR rule names generally fall here.
They include early apocope rules, certain consonant assimilations, and the
West Germanic gemination of consonants before `*j`.

## Major changes

The `*ai` monophthongization (SC004) represents one of the most pervasive
shared NW–West Germanic vowel shifts, turning unstressed endings such as the
dative singular and strong-adjective plural to longer vowels. Ringe and Taylor
treat this as one of the clearest post-PNWGmc shared developments
[@RingeTaylor2014, pp. 40--41]; Fulk groups it among the North/West-Germanic
shared innovations that distinguish the period from Gothic [@Fulk2018, §5.2].

The West Germanic consonant changes of this chapter — j-gemination (SC010),
early i-apocope (SC006), coronal-w assimilation (SC008), and related rules —
represent the most productive phonological territory for the CAPR derivations.
They feed a large proportion of the distinctive consonant clusters of Old
English. Handbooks vary in exactly how they group and name these changes
[@Campbell1959, §§ 404, 406; @HoggPhonology1992, §7.1].

The nasal spirant corridor (SC026–SC027) illustrates a type of change common
in historical grammars of the "Ingvaeonic" or "North Sea Germanic" area:
nasals disappear before voiceless fricatives, with compensatory vowel
lengthening [@Campbell1959, §§ 462--463; @HoggPhonology1992, §7.77]. The CAPR model
splits this into two ordered steps to make the vowel effect computationally
tractable; the book prose explains that split against the handbook tradition,
which typically presents the change as a single process.

Several changes in this chapter carry `PWGmc` labels in the CAPR implementation
but appear later in the computational cascade than their historical stage would
suggest: final bare-`*a` loss (SC041), surviving bimoric `*ō` unrounding
(SC042), and Sievers-law syncope (SC050) are placed late in the transducer for
computational reasons. Their chapter assignment here reflects their historical
stage, not their cascade position; the individual sound-change sections note
the divergence.

## A note on source terminology and subgrouping

The literature uses several partly overlapping stage labels for this period:

* Northwest Germanic: the node uniting North and West Germanic.
* Proto-West Germanic: the node uniting only the West Germanic languages.
* North Sea Germanic or Ingvaeonic: a proposed subgroup within West
  Germanic covering Old English, Old Frisian, and Old Saxon (and sometimes Old
  Low Franconian), sharing certain innovations over a broader area.
* Anglo-Frisian: a narrower proposed subgroup linking only Old English
  and Old Frisian.

These labels are not always used consistently across sources. Ringe and Taylor
are cautious about reconstructing a discrete Proto-West-Germanic node
[@RingeTaylor2014, pp. 50--55]. Campbell notes that many of the
"West Germanic" shared features could alternatively be treated as parallel
developments rather than common inheritance [@Campbell1959, §§ 1--5].

CAPR uses `PWGmc` and `NWGmc` as organizing labels for this chapter without
claiming to have settled all questions about West Germanic subgrouping. Changes
that appear in the literature under "Ingvaeonic" labels but affect the Old
English–to-Proto-Germanic derivation chain are treated here as late expressions
of the same West Germanic developmental period unless existing CAPR dossier
research specifically argues for Anglo-Frisian or English-specific placement.

## Rule names

The CAPR rules in this chapter carry names beginning with `NWGmc` or `PWGmc`.
These names are stable internal identifiers. A name beginning with `NWGmc` does
not guarantee that the change is exclusive to Northwest Germanic, and a name
beginning with `PWGmc` does not guarantee that it is absent from North Germanic.
The historical analysis in each sound-change section takes priority over the
name prefix.

# Unstressed \emph{*a}-raising before final \emph{*m}

## Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise includes the development of early unstressed \emph{*o} to \emph{u} before \emph{m} among the similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

I restrict the change to unstressed vowels in inflectional material because the strongest evidence concerns noninitial unstressed material before final \emph{*m}.
Final \emph{*m} conditions the raising.

## SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`PNWGmcAToUBeforeM`) {#rule-PNWGmcAToUBeforeM}

```foma
define PNWGmcAToUBeforeM [
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
];
```

Here the witness word and the comparative evidence serve different purposes. If raising is delayed until after [SC017 PNWGmcULowering](#rule-PNWGmcULowering), PGmc [skúldramiz]{.recon} 'shoulders' yields [*sċoldrum*]{.pred} rather than expected OE *sċuldrum* 'shoulders'; earlier placements converge on the expected output. The scope of the change is established by inflectional evidence across multiple paradigm types: a-stem dative plural ON [*dǫgum*]{.iv lang=on sort=dogum role=evidence_form} 'days', OE [*dagum*]{.iv lang=oe sort=dagum role=evidence_form} 'days', OS [*dagun*]{.iv lang=os sort=dagun role=evidence_form} 'days', OHG [*tagum*]{.iv lang=ohg sort=tagum role=evidence_form} 'days', beside Gothic [*dagam*]{.iv lang=goth sort=dagam role=evidence_form} 'days'; strong-adjective dative singular ON [*góðum*]{.iv lang=on sort=godum role=evidence_form} 'good', OE [*gōdum*]{.iv lang=oe sort=godum role=evidence_form} 'good', OS [*gōdum*]{.iv lang=os sort=godum role=evidence_form} 'good', beside Gothic [*godamma*]{.iv lang=goth sort=godamma role=evidence_form} 'good' (OS also shows variant forms gōdumu and -un); and first-plural present ON [*berum*]{.iv lang=on sort=berum role=evidence_form} 'we carry', OHG [*berumēs*]{.iv lang=ohg sort=berumes role=evidence_form} 'we carry', beside Gothic [*baíram*]{.iv lang=goth sort=bairam role=evidence_form} 'we carry'. Across these sets, North/West Germanic shows unstressed \emph{-um} where Gothic preserves \emph{-am}. The derivation of *sċuldrum* 'shoulders' supplies a CAPR ordering witness for the relative chronology, but the cognate set for 'shoulder' does not contribute comparative evidence for the rule's historical scope.

\newpage

# Early i-apocope

## Historical discussion

Sievers/Brunner treats the early loss of final \emph{*i} after unstressed syllables as established by the fact that these endings no longer trigger later i-umlaut in Old English, and Ringe and Taylor make the same point through the pathway to *geoguþ* ‘youth’ [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141]. Campbell's *dugup* 'troop' and *geogup* 'youth' examples belong to the same pattern [@Campbell1959, §332].

The ending vowel disappears in a weak suffixal environment early enough to block later umlaut. This anti-umlaut chronology distinguishes the change from later final-vowel losses.

## SC006. Early i-apocope (`PWGmcEarlyIApocope`) {#rule-PWGmcEarlyIApocope}

```foma
define PWGmcEarlyIApocope [
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
];
```

The absence of umlaut in *geoguþ* ‘youth’ provides the historical argument for early deletion. The ordered derivation supplies a different test: if apocope is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc [skáwōθi]{.recon} ‘shows’ yields [*sċēaweþ*]{.pred} rather than expected OE *sċēawaþ* 'shows'.

Early i-apocope must therefore precede the long-diphthong development. Moving it earlier within the tested range leaves every output unchanged; its early date rests on the anti-umlaut evidence, not on a lower boundary supplied by the witness words.

\newpage

# Final \emph{*ō}-lowering before \emph{*r}

## Historical discussion

Ringe and Taylor separate two points here: a broader shortening of vowels before word-final \emph{*r} in unstressed syllables (for which kinship \emph{*r}-stems such as PGmc \emph{*fadér} > PWGmc \emph{*fader} are a key diagnostic), and the specific \emph{*ō}-before-\emph{*r} development needed for this chapter [@RingeTaylor2014, pp. 58--59]. The direct lexical witnesses for \emph{*ō} in that environment are two independent etyma: PGmc [fedwōr]{.recon .iv lang=pgmc sort=fedwor role=evidence_form} 'four' with WGmc reflexes OE [*fēower*]{.iv lang=oe sort=feower role=evidence_form} 'four', OFris [*fiuwer*]{.iv lang=ofris sort=fiuwer role=evidence_form} 'four', OS [*fiuwar*]{.iv lang=os sort=fiuwar role=evidence_form} 'four'; and PGmc [watōr]{.recon .iv lang=pgmc sort=wator role=evidence_form} 'water' with OE [*wæter*]{.iv lang=oe sort=waeter role=evidence_form} 'water'.

The rule is historically secure but narrow: final or pre-final \emph{*ō} before word-final \emph{*r}. The clearest evidence remains concentrated in the `four` and `water` material.
No broader environment for \emph{*ō} is attested.

## \CAPRRuleHeading{SC007. Lowering of final bimoric \emph{*ō} before \emph{*r}}{PWGmcFinalOrLowering} {#rule-PWGmcFinalOrLowering}

```foma
define PWGmcFinalOrLowering [
    {*ō} -> {*a} || _ {*r} .#.
];
```

OE *wæter* ‘water’ reveals why lowering must precede [SC043 EAFBrightening](#rule-EAFBrightening). If [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) is delayed until afterwards, PGmc [wátōr]{.recon} ‘water’ yields [*water*]{.pred} rather than expected OE *wæter* ‘water’: brightening can affect the vowel only after lowering has created its input. Moving the change earlier within the tested range alters no output.

The witness thus supplies a terminus ante quem at brightening but no earlier boundary. Comparative support for the \emph{*ō}-before-\emph{*r} rule comes from the two lexical witnesses [fedwōr]{.recon .iv lang=pgmc sort=fedwor role=evidence_form} 'four' and [watōr]{.recon .iv lang=pgmc sort=wator role=evidence_form} 'water' and their WGmc reflexes; kinship \emph{*r}-stems belong to the broader pre-\emph{*r} shortening context, not to a direct \emph{*ō} > \emph{*a} control. Within CAPR, [*wæter*]{.iv lang=oe sort=waeter role=evidence_form} 'water' is the form that establishes ordering before brightening. No broader lowering of \emph{*ō} is attested.

\newpage

# Coronal-w assimilation

## Historical discussion

Ringe and Taylor treat the assimilation of \emph{*dw} and \emph{*zw} to \emph{*ww} as a shared Proto-West-Germanic innovation supported by one example of each input cluster [@RingeTaylor2014, pp. 56--57; @Stiles1985, pp. 89--94]. The \emph{*dw} example is the numeral 'four': PGmc \emph{*feðwor} (Gothic \emph{fidwor}) → WGmc \emph{*fewwar} → OE \emph{fēower}, Old Frisian \emph{fiuwer}, Old Saxon \emph{fiuwar}. The \emph{*zw} example is the second-person plural pronoun, where two oblique case forms show the change: acc./dat.\ PGmc \emph{*izwiz} (Gothic \emph{izwis}) → OE \emph{eow}, Old Frisian \emph{iu}, Old Saxon \emph{iu}, OHG \emph{iu}; and gen.\ Ringe and Taylor's PGmc \emph{*izweraz} (Gothic \emph{izwara}) → OE \emph{eower}, OHG \emph{iuwer} [@RingeTaylor2014, p. 56]. Stiles discusses the same pronominal material using his own reconstruction conventions and explicitly treats Gothic \emph{izwara} among the relevant comparanda [@Stiles1985, pp. 89--94]. These two case forms belong to a single pronominal paradigm, not to two independent etyma.

The historical support rests on a small witness set. Both coronal inputs assimilate before \emph{*w}, but the evidence for each cluster is confined: the numeral alone supplies the \emph{*dw} instance, and the oblique case forms of the second-person plural pronoun supply the \emph{*zw} instance.

## \CAPRRuleHeading{SC008. Assimilation of coronal consonants before \emph{*w}}{PWGmcCoronalWAssimilation} {#rule-PWGmcCoronalWAssimilation}

```foma
define PWGmcCoronalWAssimilation [
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
];
```

OE *fēower* ‘four’ exposes a feeding relation: coronal assimilation must create \emph{*ww} while simplification can still reduce it. If [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) is delayed until after [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc [fédwōr]{.recon} ‘four’ yields [*fēowwer*]{.pred} rather than expected OE *fēower* ‘four’. Earlier placements alter no output.

The numeral fixes that relative order. The pronominal forms supply the parallel \emph{*zw} evidence; 'four' remains the sole \emph{*dw} witness and the sole source of the coronal-assimilation → *ww*-simplification ordering constraint. The earlier boundary of the assimilation remains undetermined.

\newpage

# \emph{ij}-contraction in \emph{friend}

## Historical discussion

Ringe and Taylor describe a change of \emph{*ijo} to \emph{*iu} in the ancestor of \emph{friend}, with the pathway PGmc \emph{*frijōnd-} (Gothic \emph{frijonds}) → PWGmc \emph{*friund} → OE \emph{frēond}, Old Frisian \emph{frīund}, Old Saxon \emph{friund}, Old High German \emph{friunt} [@RingeTaylor2014, p. 62]. The same source immediately warns that the \emph{*ijo} sequence is unique enough that wider generalization is inadvisable [@RingeTaylor2014, p. 62]. Luick (printed p. 118) notes that \emph{iu} generalised within several \emph{j}-stem paradigms through a related but differently conditioned loss of \emph{j}, but does not supply a second example of the exact stressed \emph{*ijo} sequence [@Luick1914, p. 118].

The change concerns a rare sequence attested only in the \emph{*frijōnd-} etymon and cannot safely be generalized into a broadly productive rule.

## SC009. \emph{ij}-contraction in \emph{friend} (`PWGmcIjContraction`) {#rule-PWGmcIjContraction}

```foma
define PWGmcIjContraction [
    {*i} {*j} {*ō} -> {*iu} || _ EnglishStarConsonant,
    {*í} {*j} {*ō} -> {*íu} || _ EnglishStarConsonant
];
```

Only the \emph{*frijōnd-} etymon tests this contraction. If the rare \emph{*ijō} sequence survives until after [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), PGmc [fríjōndz]{.recon} ‘friend’ yields [*friund*]{.pred} rather than expected OE *frēond* 'friend'; moving contraction earlier within the tested range changes no output.

That single contrast places [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction) before diphthong leveling but gives no lower boundary. It cannot establish a productive sound law beyond the \emph{*frijōnd-} etymon, precisely the reservation made by Ringe and Taylor.

\newpage

# West Germanic j-gemination

## Historical discussion

Fulk treats West Germanic consonant gemination before `*j` after a short vowel as a regular development and illustrates it with forms such as OE *settan* 'set' and *lecgan* 'lay' [@Fulk2018, p. 127, §6.15].

The change applies specifically after a short vowel before \emph{*j}, not to geminate consonants generally.

## SC010. West Germanic j-gemination (`PWGmcJGemination`) {#rule-PWGmcJGemination}

```foma
define PWGmcJGemination [
    {*p} -> {*p} {*p} || EnglishStarShortVowel _ {*j},
    {*b} -> {*b} {*b} || EnglishStarShortVowel _ {*j},
    {*t} -> {*t} {*t} || EnglishStarShortVowel _ {*j},
    {*d} -> {*d} {*d} || EnglishStarShortVowel _ {*j},
    {*k} -> {*k} {*k} || EnglishStarShortVowel _ {*j},
    {*g} -> {*g} {*g} || EnglishStarShortVowel _ {*j},
    {*f} -> {*f} {*f} || EnglishStarShortVowel _ {*j},
    {*s} -> {*s} {*s} || EnglishStarShortVowel _ {*j},
    {*m} -> {*m} {*m} || EnglishStarShortVowel _ {*j},
    {*n} -> {*n} {*n} || EnglishStarShortVowel _ {*j},
    {*l} -> {*l} {*l} || EnglishStarShortVowel _ {*j},
    {*ŋ} -> {*ŋ} {*ŋ} || EnglishStarShortVowel _ {*j},
    {*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j}
];
```

OE *nett* 'net' fixes the order because the syllabic-\emph{j} development would remove the glide that conditions gemination. If [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) precedes [SC010 PWGmcJGemination](#rule-PWGmcJGemination), PGmc [nátją]{.recon} ‘net’ yields [*nete*]{.pred} rather than expected OE *nett* 'net'. Earlier movement of gemination changes no output.

The chronology is phonologically transparent: the consonant must geminate before \emph{*j} ceases to be consonantal. The witness establishes no earlier boundary.

\newpage

# Syllabic j after final-vowel loss

## Historical discussion

Ringe and Taylor state directly that after final unstressed `*a` and `*ą` were lost, postconsonantal `*j` became syllabic `*i`, with outcomes behind OE *here* 'army' and *rice* 'kingdom' [@RingeTaylor2014, p. 46].

The sources establish the development, although the lexical evidence supplies
little independent support for its position. Its scope is postconsonantal j,
not high-vowel vocalization generally.

## SC011. Syllabic \emph{*j} after final-vowel loss (`PWGmcSyllabicJ`) {#rule-PWGmcSyllabicJ}

```foma
define PWGmcSyllabicJ [
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
];
```

The same PGmc [nátją]{.recon} ‘net’ witness supplies the only firm boundary. Placing [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) before [SC010 PWGmcJGemination](#rule-PWGmcJGemination) yields [*nete*]{.pred} rather than expected OE *nett* 'net'; moving it later changes no output.

Comparative evidence establishes postconsonantal \emph{*j} to syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} loss, with *here* 'army' and *rice* 'kingdom' as outcomes. The lexicon adds only that vocalization followed gemination, not where it falls among subsequent changes.

\newpage

# \emph{lþ}-voicing

## Historical discussion

Ringe and Taylor treat word-internal \emph{*lþ} > \emph{*ld} as a regular sound change in northern West Germanic and illustrate it with forms such as *fealdan* 'fold', *beald* 'bold', *wuldor* 'glory', and *gylden* 'golden' [@RingeTaylor2014, pp. 170--171]. Campbell gives a similar West-Germanic-facing formulation with examples such as *fealdan*, *wuldor*, *beald*, *gold* 'gold', and *feld* 'field' [@Campbell1959, p. 169, §414].

The comparative evidence supports \emph{lþ > ld} most clearly in northern West
Germanic, not as an unqualified pan-PWGmc development.

## SC012. Northern West Germanic \emph{lþ}-voicing (`EAFLThVoicing`) {#rule-EAFLThVoicing}

```foma
define EAFLThVoicing [
    {*θ} -> {*d} || {*l} _
];
```

The `field`, `fold`, `gold`, and `wold` families preserve \emph{*lþ} to \emph{*ld}, but none dates the change against a neighboring rule. Every output remains unchanged when the voicing is moved in either direction.

Comparative reconstruction therefore establishes northern West Germanic \emph{lþ > ld}, but the witness forms fix no date. Neither a pan-PWGmc attribution nor an exact local placement follows from the evidence presented here.

\newpage

# Dental hardening

## Historical discussion

Ringe and Taylor state directly that in PWGmc voiced dental fricative `*ð` became stop `*d` in all positions [@RingeTaylor2014, p. 43].

The change is systemic across early West Germanic and extends beyond any one
lexical family.

## SC013. Dental hardening (`PWGmcDentalHardening`) {#rule-PWGmcDentalHardening}

```foma
define PWGmcDentalHardening [
    {*ð} -> {*d}
];
```

Dental hardening has systemic scope: voiced fricative \emph{*ð} became stop \emph{*d} throughout early West Germanic. Moving [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) earlier or later changes no output.

Comparative evidence establishes the sound law; the present lexicon leaves its exact position approximate.

\newpage

# Early unstressed vowel changes

## Historical discussion

The first change monophthongizes unstressed \emph{*ai}; the second carries early unstressed front-vowel leveling farther in forms such as *weorold* 'world'. Both have a diagnostic later boundary in the dataset.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e}, in final and nonfinal syllables alike [@RingeTaylor2014, pp. 37--41]. Two dative-singular endings in the dataset, span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed', carry the change. The stressed development of \emph{*ái} to \emph{*ā} is treated separately as [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## \CAPRRuleHeading{SC014. Monophthongization of unstressed \emph{*ai}}{PNWGmcUnstressedAiMonophthongization} {#rule-PNWGmcUnstressedAiMonophthongization}

```foma
define PNWGmcUnstressedAiMonophthongization [
    {*ai} -> {*ē}
];
```

The dative-singular endings span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed' carry this change; both give a final \emph{*ē}. If [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) is delayed until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), the \emph{*ē} is no longer present for shortening, so PGmc [spánnai]{.recon} 'span' yields [*spannē*]{.pred} rather than expected OE *spanne* 'span'. This shows that [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) in the modeled sequence.

Ringe and Taylor's merger of unstressed \emph{*ai} with long mid \emph{*ē} establishes the historical development, in final and nonfinal syllables alike. The stressed development of \emph{*ái} to \emph{*ā} is a separate and later change; see [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* 'world' and *weoruld* 'world' [@Campbell1959, pp. 141--142, 154--155]. These forms supply [SC015 PNWGmcILowering](#rule-PNWGmcILowering) with a firmer lexical basis than the preceding change.

## \CAPRRuleHeading{SC015. Leveling of early unstressed front vowels}{PNWGmcILowering} {#rule-PNWGmcILowering}

```foma
define PNWGmcILowering [
    {*i} -> {*e}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel
];
```

The *weorold* 'world' and *weoruld* 'world' variants turn the general source claim into an ordering test. If [SC015 PNWGmcILowering](#rule-PNWGmcILowering) is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc [wír-àldu]{.recon} ‘world’ yields [*wuruld*]{.pred} rather than expected OE *weorold* ‘world’; earlier movement changes no output.

The derivation thus fixes front-vowel leveling before interstress raising while leaving its earlier boundary open.

[SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 PNWGmcULowering](#rule-PNWGmcULowering) follow with a more tightly constrained local chronology.

\newpage

# Northwest Germanic u-lowering

## Historical discussion

The derivation of *ġeoc* 'yoke' passes through both this change and the
preceding West Saxon palatal glide ([SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide)).
Campbell treats the West Saxon rising-diphthong spellings before back vowels,
while the same handbook tradition describes the lowering of \emph{u} before a
following non-high vowel separately [@Campbell1959, p. 17, §44;
@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].
The first change creates the West Saxon \emph{ġeoc} type; u-lowering then
carries the same material into the subsequent vowel history.

After the glide-conditioned West Saxon spellings are in place, the broader Northwest Germanic lowering of \emph{u} to \emph{o} before a following non-high vowel provides the clearest standard sound change in this small region. Campbell and Fulk both describe that change directly [@Campbell1959, pp. 42--43, §115; @Fulk2018, p. 56, §4.3].

[SC017 PNWGmcULowering](#rule-PNWGmcULowering) thus rests on a broader source base than the preceding West Saxon rule.

## \CAPRRuleHeading{SC017. Lowering of \emph{*u} before following non-high vowels}{PNWGmcULowering} {#rule-PNWGmcULowering}

```foma
define PNWGmcULowering [
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

Lowering of \emph{u} to \emph{o} is fixed on both sides by *ġeoc* 'yoke', *nosu* 'nose', *sċofl* 'shovel', and *sorg* 'sorrow'.

Before [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), PGmc [júką]{.recon} 'yoke' yields [*ġoc*]{.pred} rather than expected OE *ġeoc* 'yoke'. After [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), PGmc [núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected *nosu* 'nose', PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected *sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather than expected *sorg* 'sorrow'. The two witness sets place [SC017 PNWGmcULowering](#rule-PNWGmcULowering) after glide formation and before final long-\emph{o} raising.

\newpage

# Stressed monosyllable \emph{*ō}-raising

## Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

The change is historically secure, but the tested forms determine no close relative position for it.
Its input is final \emph{*ō} in a stressed monosyllable.

## \CAPRRuleHeading{SC018. Raising of final stressed monosyllabic \emph{*ō}}{PNWGmcStressedMonosyllableORaising} {#rule-PNWGmcStressedMonosyllableORaising}

```foma
define PNWGmcStressedMonosyllableORaising [
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
];
```

Campbell's *cū* 'cow', *hū* 'how', and *tū* 'two' establish final stressed monosyllabic \emph{*ō} > \emph{*ū}.

Reversing [SC018 PNWGmcStressedMonosyllableORaising](#rule-PNWGmcStressedMonosyllableORaising) with neighboring changes leaves every output unchanged. The sound change is secure, but its exact position in the early history of long vowels rests on the handbooks.

\newpage

# Raising of final unstressed long \emph{*ō}

## Historical discussion

Ringe and Taylor describe the change of unstressed final non-nasalized long
\emph{*ō} to short \emph{*u} as a Northwest Germanic development
[@RingeTaylor2014, p. 30]. It applies in the same final-syllable environment
as the subsequent loss of word-final \emph{*z}. The derivation of *ræste*
'rest' fixes their local order: [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising)
must still see final \emph{*ō}, and word-final \emph{*z}-deletion removes the following
\emph{*z} only afterward.

The change supplies the final vowel of forms such as *nosu* 'nose', *sċofl*
'shovel', and *sorg* 'sorrow'.

## \CAPRRuleHeading{SC019. Raising of final unstressed long \emph{*ō}}{PNWGmcFinalLongORaising} {#rule-PNWGmcFinalLongORaising}

```foma
define PNWGmcFinalLongORaising [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

Two groups of witnesses confine final unstressed long \emph{*ō} > \emph{*u}. The forms *nosu* 'nose', *sċofl* 'shovel', and *sorg* 'sorrow' fix its lower boundary.

Before [SC017 PNWGmcULowering](#rule-PNWGmcULowering), PGmc [núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected OE *nosu* 'nose', PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected *sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather than expected *sorg* 'sorrow'. After word-final \emph{*z}-deletion ([SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion)), PGmc [rástōz]{.recon} 'rest' yields [*rast*]{.pred} rather than expected *ræste* 'rest'. These failures place [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising) after u-lowering and before final \emph{z}-loss.

\newpage

# Unstressed \emph{*o}-raising

## Historical discussion

In the Northwest Germanic period an unstressed \emph{*o} was raised to \emph{*u}
when \emph{*u} followed in the next syllable. The clearest case is the
\emph{n}-stem accusative singular, where inherited \emph{*-onų} was regularly
raised to \emph{*-unų} before the following high vowel; Campbell treats the
resulting unstressed \emph{u} and \emph{o} alternations for Old English
[@Campbell1959, pp. 155--156, §§373--374]. The change is a general development of
the unstressed suffix, not tied to any single lexeme.

## \CAPRRuleHeading{SC021. Raising of unstressed \emph{*o} before later \emph{*u}}{PNWGmcUnstressedORaising} {#rule-PNWGmcUnstressedORaising}

```foma
define PNWGmcUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ EnglishStarConsonant* {*ų}
];
```

No word in the present selected corpus supplies this environment: no selected
input carries an unstressed \emph{*o} before a following \emph{*ų}, so
[SC021 PNWGmcUnstressedORaising](#rule-PNWGmcUnstressedORaising) fires in no
current derivation. The earlier witness [*heofon*]{.iv lang=oe sort=heofon role=evidence_form}
'heaven' no longer applies here: its selected input is now Ringe and Taylor's
northern West Germanic [hebun]{.recon .iv lang=nsgmc sort=hebun role=evidence_form}
'heaven', which already carries the generalized labial and contains no unstressed
\emph{*o} before \emph{*ų} [@RingeTaylor2014, p. 287]. The rule is retained as a
genuine Northwest Germanic change, but it is presently unwitnessed and
boundary-limited: no lexical form now constrains its position within the Old
English sequence, and moving it earlier or later leaves every output unchanged.

\newpage

# \emph{mn}-dissimilation

## Historical discussion

In the inherited \emph{n}-stem paradigm the zero-grade oblique cells brought
\emph{m} and \emph{n} into direct contact, and in that adjacent cluster the
labial nasal dissimilated to a labial spirant: \emph{mn} > \emph{βn} (surfacing
as \emph{fn}). Old Norse preserves the older paradigmatic distribution, with the
labial confined to the oblique cluster (\emph{himinn} 'heaven' beside dative
\emph{hifni}); Old English and Old Saxon generalized it. Fulk treats the cluster
change for early Germanic [@Fulk2018, §6.14, p. 121], and the relevant
\emph{heofon} 'heaven' and \emph{mōnaþ} 'month' material is discussed by Campbell
[@Campbell1959, pp. 189, 195, §§470, 484].

The pattern is historically established, but the lexical evidence does not constrain its position.

## SC022. Dissimilation of adjacent \emph{mn} (`PNWGmcMnDissimilation`) {#rule-PNWGmcMnDissimilation}

```foma
define PNWGmcMnDissimilation [
    {*m} -> {*β}
        || EnglishStarVocalic _ {*n}
];
```

The rule fires only where \emph{m} stands directly before \emph{n}. It supplies
the labial of \emph{stefn} 'stem, trunk' from the \emph{mn}-cluster of the
\emph{stamn}-family, and it is the historical change behind the labial of
\emph{heofon} 'heaven', which was generalized from the oblique cluster into the
vowel-bearing stem before the Old English vocalic changes. (An earlier
cross-syllable formulation that labialized an intervocalic \emph{m} before a
later nasal has been retired: it simulated paradigm levelling rather than a sound
law.)

Moving [SC022 PNWGmcMnDissimilation](#rule-PNWGmcMnDissimilation) earlier or later leaves every output unchanged. Its executable place in this holding zone is therefore editorial/computational, while its historical classification rests on the handbook account of \emph{mn}-dissimilation.

\newpage

# Word-final \emph{n}-loss

## Historical discussion

The change isolated here is far older than its position in the cascade suggests: it is the general (pre-)Proto-Germanic loss of word-final \emph{*n}, with nasalization of the preceding vowel, in polysyllables. Ringe's proof set for the law spans the whole grammar — nouns such as \emph{*yugón} > \emph{*juką} 'yoke', pronouns such as \emph{*tón} > \emph{*þanǭ}, and even the verb form \emph{*dedǭ} 'I did' — so it is general phonology, not a fact about any one declension [@Ringe2017, pp. 101--103]. Gothic \emph{tuggo} shares the weak nominative-singular outcome, and the nasalized reflex \emph{*-ǭ} remained contrastive into Proto-West Germanic before yielding OE \emph{-e} [@RingeTaylor2014, pp. 54--55, 58--59].

Within the present corpus the change surfaces in exactly one shape: the weak nouns are cited in the stem form \emph{*-ōn-}, and this rule carries them to the Proto-Germanic nominative singular in \emph{*-ǭ}, as in \emph{*túngōn} > \emph{*túngǭ} > *tunge* 'tongue', alongside *eorþe* 'earth', *heorte* 'heart', *nǣdre* 'adder', and thirteen further weak nouns. The masculine weak nominative singular in trimoric \emph{*-ô} never had a final \emph{*-n} to lose, and Proto-Germanic \emph{*sebun} 'seven', \emph{*nigun} 'nine', and \emph{*tehun} 'ten' kept their \emph{-n} by lexical analogy among the numerals [@Ringe2017, p. 103]; the rule's narrow \emph{*-ōn} environment leaves all of these correctly untouched.

## SC023. Loss of word-final \emph{*n} after \emph{*ō} (`PNWGmcNStemNLoss`) {#rule-PNWGmcNStemNLoss}

```foma
define PNWGmcNStemNLoss [
    {*ō} {*n} -> {*ǭ} || _ .#.
];
```

The verb *dōn* 'do' supplies the negative, counterfeeding witness for the chronology. PGmc [dōną]{.recon} 'do' passes this rule untouched; only [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope) later strips the final [ą]{.recon} and creates a new word-final [-ōn]{.recon}. That secondary [-n]{.recon} survives into *dōn* precisely because the old loss was no longer active: if [SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss) is displaced after the apocope, it consumes the new nasal and the derivation collapses entirely (\emph{+?}).

The retained \emph{-n} of *dōn* 'do' therefore supplies a terminus ante quem for the loss — it must be dead before the apocope — while the seventeen weak nouns above are its positive witnesses; the lower boundary remains unattested within the cascade, as befits a change already complete in Proto-Germanic.

\newpage

# Long \emph{ē}-lowering

## Historical discussion

The later West Saxon forms *sċēap* ‘sheep’ and *ġēar* ‘year’ imply an earlier lowering of long \emph{ē} before the palatal diphthongal outcomes described more fully later in the sequence. Campbell and Ringe and Taylor discuss those later West Saxon outputs directly [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1].

The change is historically recognizable, but the lexical evidence establishes only a later boundary.

## \CAPRRuleHeading{SC024. Lowering of long \emph{ē} before non-nasal consonants}{PNWGmcLongELowering} {#rule-PNWGmcLongELowering}

```foma
define PNWGmcLongELowering [
    {*ē} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal],
    {*ḗ} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

After [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), long \emph{ē} > \emph{ǣ} can no longer produce the expected West Saxon forms: PGmc [skḗpą]{.recon} ‘sheep’ yields [*sċīep*]{.pred} rather than OE *sċēap* ‘sheep’, and PGmc [jḗrą]{.recon} ‘year’ yields [*ġīer*]{.pred} rather than *ġēar* ‘year’. Earlier placement changes no output, so [SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering) has a secure upper boundary.

Its lower boundary remains a matter of handbook chronology.

\newpage

# Long \emph{ē} nasal-rounding

## Historical discussion

Before nasals, older long \emph{ē} can round toward the \emph{ō}-vocalism seen later in *mōnaþ* 'month' and *mōna* 'moon' / *mōn* 'moon'-type material. Campbell treats this split directly in his discussion of Germanic long \emph{ē} before nasal consonants [@Campbell1959, p. 53, §129].

The change is historically recognizable, but the tested forms supply no close relative chronology.

## \CAPRRuleHeading{SC025. Rounding of long \emph{ē} before nasals}{PNWGmcLongENasalRounding} {#rule-PNWGmcLongENasalRounding}

```foma
define PNWGmcLongENasalRounding [
    {*ē} -> {*ō} || _ EnglishStarNasal,
    {*ḗ} -> {*ō} || _ EnglishStarNasal
];
```

Reversing [SC025 PNWGmcLongENasalRounding](#rule-PNWGmcLongENasalRounding) with neighboring changes leaves every output unchanged. Its position beside the other \emph{ē}-developments therefore follows the handbooks.

\newpage

# Nasal spirant changes

## Historical discussion

The two rules state successive phases of a single development. Campbell
describes nasal loss before voiceless spirants with compensatory lengthening and
nasalization of the preceding vowel. Ringe and Taylor assign the same outcomes
to inherited northern West Germanic, before late Old English
[@Campbell1959, p. 47, §121; @RingeTaylor2014, pp. 140--141].

[SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) adjusts the vowel while the nasal-plus-spirant sequence remains present; [SC027 EAFNasalSpirantLoss](#rule-EAFNasalSpirantLoss) then removes the nasal. The first rule must therefore precede the second.

## \CAPRRuleHeading{SC026. North Sea Germanic nasal-spirant lengthening}{EAFNasalSpirantLengthening} {#rule-EAFNasalSpirantLengthening}

```foma
define EAFNasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*æ} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*á} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*é} -> {*ḗ} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*í} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ó} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ú} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative
];
```

All three witnesses require the vowel adjustment while the nasal is still present. If [SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) follows [SC027 EAFNasalSpirantLoss](#rule-EAFNasalSpirantLoss), PGmc [fúnxstiz]{.recon} ‘fist’ yields [*fyst*]{.pred} rather than expected OE *fȳst* ‘fist’, PGmc [gánsz]{.recon} ‘goose’ yields [*ġeas*]{.pred} rather than expected *gōs* ‘goose’, and PGmc [júgunθ]{.recon} ‘youth’ yields [*ġeogoþ*]{.pred} rather than expected *ġeoguþ* ‘youth’. Earlier placement changes no output. The evidence requires lengthening to precede nasal loss without supplying a lower boundary, in agreement with the handbook treatment of the two as successive phases.

## \CAPRRuleHeading{SC027. North Sea Germanic nasal-spirant loss}{EAFNasalSpirantLoss} {#rule-EAFNasalSpirantLoss}

```foma
define EAFNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

The converse test fixes the same boundary: placing [SC027 EAFNasalSpirantLoss](#rule-EAFNasalSpirantLoss) before [SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) produces the same errors in *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’. Later placement changes no output. These forms prove that the vowel was adjusted before the nasal disappeared; they provide no upper boundary for the loss.

\newpage

# Preconsonantal \emph{*x}-loss

## Historical discussion

Campbell explicitly treats loss of \emph{x} and gives forms such as *fléam* ‘flight’ and *hēla* ‘heel’ as examples of the same broad development [@Campbell1959, p. 186, §461].

The historical evidence is firmer than the chronology: the lexical evidence does not constrain the rule's position.

## SC028. Loss of preconsonantal \emph{*x} (`PNWGmcPreconsonantalXLoss`) {#rule-PNWGmcPreconsonantalXLoss}

```foma
define PNWGmcPreconsonantalXLoss [
    {*x} -> 0 || _ {*s} EnglishStarConsonant
];
```

No witness word dates preconsonantal \emph{*x}-loss before \emph{*s} plus another consonant: moving [SC028 PNWGmcPreconsonantalXLoss](#rule-PNWGmcPreconsonantalXLoss) in either direction leaves every output unchanged. Its position within this stretch therefore rests on the handbook chronology for \emph{x}-loss.

\newpage

# Final bare-\emph{a} loss

## Historical discussion

I isolate the loss of final short low vowels within the broader erosion of final syllables described by the handbooks [@Campbell1959, p. 143, §341; @RingeTaylor2014, pp. 60--61].

Final bare-a loss follows the medial unstressed vowel changes and
precedes restoration, which depends on the environment left by the loss.

## SC041. Loss of final bare \emph{*a} (`PWGmcFinalBareALoss`) {#rule-PWGmcFinalBareALoss}

```foma
define PWGmcFinalBareALoss [
    {*a} -> 0 || _ .#.
];
```

The two sides of final bare-\emph{a} loss rest on different evidence. Applied before final \emph{z}-deletion, the change gives the wrong outputs: PGmc [bárdaz]{.recon} ‘beard’ yields [*bearda*]{.pred} rather than expected OE *beard* ‘beard’, and PGmc [kámbaz]{.recon} ‘comb’ yields [*camba*]{.pred} rather than expected *camb* ‘comb’. Applied after restoration, PGmc [kráftaz]{.recon} ‘craft’ yields [*craft*]{.pred} rather than expected OE *cræft* ‘craft’, and PGmc [dágaz]{.recon} ‘day’ yields [*dag*]{.pred} rather than expected *dæġ* ‘day’. The distant lower limit follows final \emph{z}-loss; the local feeding relation precedes restoration, which requires the environment created by the vowel loss.

\newpage

# Surviving bimoric \emph{*ō} unrounding

## Historical discussion

The handbooks do not isolate a large independent sound change under this label.
The surviving bimoric \emph{*ō} in the pathway to *ræste* ‘rest’ nevertheless
undergoes unrounding before
[SC043 EAFBrightening](#rule-EAFBrightening). Campbell, Hogg,
and Ringe and Taylor describe the surrounding fronting and restoration history
without naming this feeder separately [@Campbell1959, pp. 52, 60,
§§131, 157--158; @HoggPhonology1992, pp. 102, 105; @RingeTaylor2014, pp. 157--158,
189--190].

The sole witness establishes a local relation to brightening but supports no broader generalization.

## \CAPRRuleHeading{SC042. Unrounding of the surviving bimoric \emph{*ō}}{PWGmcSurvivingBimoricOUnrounding} {#rule-PWGmcSurvivingBimoricOUnrounding}

```foma
define PWGmcSurvivingBimoricOUnrounding [
    {*ō} -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

The single *ræste* ‘rest’ derivation carries the chronology of bimoric \emph{*ō} > \emph{*ā}. Before [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion) or after [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [rástōz]{.recon} ‘rest’ yields [*rasta*]{.pred} rather than expected OE *ræste*. Unrounding must therefore follow final \emph{z}-loss and precede brightening, although only the relation to brightening is local.

\newpage

# Sievers-law syncope

## Historical discussion

Sievers' Law concerns a prosodic and morphological adjustment in heavy stems.
It is a distributional rule distinct from b-allophony ([SC049 PGmcBAllophony](#rule-PGmcBAllophony)). Adamczyk treats
the Old English reflexes of the law as historical evidence from weak verbs and
related formations [@Adamczyk2001, pp. 61--72]. Fulk gives the compact
comparative summary through familiar forms such as *biddan* 'ask', *sellan*
'give', and *nerian* 'save' [@Fulk2018, p. 127, §6.15].

Sievers-law syncope is narrow in scope, but its relation to the following
palatalization is lexically secure. Its earlier limit is less sharply defined
than that of the preceding allophony rule.

## SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

The Sievers-law reduction \emph{*-CijV-*} > \emph{*-CjV-*}, including loss of \emph{*i} before \emph{*j}, must precede palatalization. If [SC050 SieversLawSyncope](#rule-SieversLawSyncope) follows [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc [strákkijaną]{.recon} 'stretch' yields [*strecċan*]{.pred} rather than expected OE *streċċan* 'stretch'; earlier placement creates no comparably precise error. The single cluster witness therefore places syncope before velar palatalization.

\newpage

# Chapter 3. From Proto-West Germanic to Anglo-Frisian


## Historical interval

This chapter covers the sound changes that occurred after the Proto-West Germanic
period and before, or during the emergence of, the specifically English line. The
starting reconstruction is Proto-West Germanic; the end point is the
Proto-Anglo-Frisian stage — or more precisely, the cluster of innovations that
define the English and Frisian branch within West Germanic.

## A necessary terminological caution

The title of this chapter uses "Anglo-Frisian" as an organizing historical
concept. That choice requires an explicit qualification.

The scholarly literature uses several overlapping terms for this developmental
period:

* North Sea Germanic and Ingvaeonic: labels used by some scholars for a
  proposed subgroup comprising Old English, Old Frisian, and Old Saxon (or more
  narrowly, Old English and Old Frisian only). The innovations associated with
  this label — especially the nasal spirant changes and certain vowel
  developments — are sometimes described as diffusion rather than shared
  inheritance [@Campbell1959, §§ 1--3].
* Anglo-Frisian: a label used specifically for the Old English / Old Frisian
  branch, or for innovations shared between the two languages. Its use presupposes
  a tighter relationship between English and Frisian than between either and
  Old Saxon.
* Proto-Anglo-Frisian (PAF): the strongest interpretation, positing a discrete
  reconstructed common ancestor for Old English and Old Frisian specifically.
  This is the position of Ringe and Taylor, who reconstruct a PAF stage between
  Proto-West Germanic and Proto-Old-English [@RingeTaylor2014, pp. 54--68].

CAPR does not commit to a universally accepted discrete PAF node. The chapter
title uses "Anglo-Frisian" because the key changes of this period — especially
West Germanic rhotacism (SC003), word-final `*z` deletion (SC020), and
Anglo-Frisian brightening (SC043) — are most prominently associated with that
label in the handbook literature. But the analysis does not require that every
change passed through a single genealogical PAF stage. Some changes may be
West Germanic broadly; others may reflect areal diffusion. The existing CAPR
dossiers record the source-by-source picture where these distinctions matter.

## Major changes and their historical basis

### West Germanic rhotacism (SC003)

The medial change of `*z` to `*r` in environments such as [déuzaz]{.recon .iv lang=pgmc sort=deuzaz} 'deer',
[xúrdaz]{.recon .iv lang=pgmc sort=xurdaz} 'hoard', and
[líznōjaną]{.recon .iv lang=pgmc sort=liznojana} 'learn' is historically a
post-Proto-West-Germanic development. Ringe and Taylor argue that rhotacism was
not inherited from Proto-Northwest Germanic and was not uniform within West
Germanic [@RingeTaylor2014, pp. 52, 98, 102]. Crist separates this change
explicitly from the deletion of word-final `*z` and argues that rhotacism must
follow the deletion rules [@Crist2001, pp. 104--106; @Crist2002, pp. 1, 4].
Bammesberger gives the standard Old English–facing summary: `*z` yielded `*r` in
intervocalic position but was generally lost in final position
[@Bammesberger1992, p. 39].

The CAPR rule is named `EAFRhotacism`, placing it in the Early Anglo-Frisian
corridor, CAPR's operational post-Proto-West-Germanic stage on the English line;
the reader-facing chapter label describes the change as a West Germanic
rhotacism.

### Word-final `*z` deletion (SC020)

The deletion of word-final `*z` in forms such as [rástōz]{.recon .iv lang=pgmc sort=rastoz} 'rest (nom.sg.)'
is placed here on the basis of Crist's analysis, which distinguishes
a pan-West-Germanic loss of `*z` after unstressed vowels from the earlier
NWGmc changes and from the later narrower Ingvaeonic deletion rules
[@Crist2002, pp. 1, 4]. The standard handbooks confirm a West Germanic
deletion: Campbell notes that `*z` is "later lost or changed to `r`"
[@Campbell1959]; Bammesberger gives a clean statement that Germanic `*z` is generally
lost in final position [@Bammesberger1992, p. 39].

The CAPR rule is named `EAFFinalZDeletion`, which is historically misleading.
The existing reader-facing prose already notes this: the current assembled
section correctly describes SC003 as presupposing an earlier loss of final `*z`,
creating a presentational tension with SC020's place at cascade position 20.
This tension is a targeted audit item for the next phase of the chronology work.

### Anglo-Frisian ai-monophthongization (SC004)

The monophthongization of stressed/root `*ái` to `*ā`, seen in the soul
derivation, is a North Sea Germanic
areal development. Versloot argues that it spread in successive waves through a
dialect continuum, with Old English among the widest to carry it, so the change
is better read as an areal diffusion through the continuum than as a single
dated node [@Versloot2017, pp. 281--324]. The resulting `*ā` is later fronted to
`ǣ` in the relevant Old English environments.

The CAPR rule is named `EAFAiMonophthongization` and executes at cascade
position 25. That position is CAPR's operational home for a North Sea Germanic
areal change on the English line; it is a modelling choice, not a claim that the
change passed through a discrete Proto-Anglo-Frisian node. The one usable
chronological anchor is the `soul` derivation, which requires the
monophthongization to precede OE interstress raising (SC036).

The unstressed development `*ai > *ē` (in final and nonfinal syllables) is a
separate and earlier Proto-Northwest Germanic change (SC014), discussed in
Chapter 2; its corpus witnesses are the dative-singular endings of `span`
([spánnai]{.recon} 'span' > *spanne* 'span') and `meed` ([mízdai]{.recon}
'meed' > *meorde* 'meed').

### Anglo-Frisian brightening (SC043)

The fronting of low `*a` to `*æ` outside nasal environments is the defining
Anglo-Frisian change and the central event of this chapter. Campbell gives the
classical statement: "By a very early change Prim. Gmc. `a > æ` in OE and OFris.
when not followed by a nasal consonant" [@Campbell1959, §§ 163--165].
Hogg gives the most familiar modern label pair: "This vowel normally fronted
to /ae/ by the sound change of Anglo-Frisian Brightening (or First Fronting)"
[@HoggPhonology1992, §5.8].

The change is notable for what follows it: OE Breaking presupposes the fronted
input; OE a-Restoration partially undoes it in back-vowel environments. The
three-change sequence (brightening, breaking, restoration) is one of the clearest
relative-chronology chains in the Old English historical grammar.

Campbell notes that English and Frisian may not simply reflect one
undifferentiated shared prehistoric event, and Ringe and Taylor leave open
whether the wider spread of fronted outcomes happened mainly on the continent
or in Britain [@RingeTaylor2014, pp. 60--62]. CAPR's implementation treats the
change as a single rule; the book prose acknowledges the uncertainty about its
exact geographical scope.

The current CAPR inventory has this change labeled "Old English" in the pipeline
taxonomy (no separate Anglo-Frisian bucket previously existed). The historical
staging map now places it in Chapter 3, correcting that provisional label.

## Cascade vs. historical order in this chapter

The four changes in this chapter currently occur at cascade positions 3, 19–20,
25, and 43 respectively. These cascade positions reflect computational dependencies,
not historical sequence. The reader-facing book order in this chapter places
rhotacism first (as the post-PWGmc WGmc change), then word-final `*z` deletion
(SC020, closely related to rhotacism and discussed in the same reader-facing
section as SC019), then Anglo-Frisian ai-monophthongization (SC004, the North
Sea Germanic areal vowel change), then Anglo-Frisian brightening as the
culminating change of the pre-OE period.

The divergence between cascade order and book order in this chapter is one of
the clearest illustrations of the principle that FST dependency does not
automatically equal historical sequence.

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

The lexical evidence thus supplies a terminus ante quem but no terminus post quem. Its placement after the earlier loss of final \emph{*z} rests on the historical analyses cited above.

\newpage

# West Germanic final \emph{*z}-deletion

## Historical discussion

The loss of word-final \emph{*z} is a West Germanic development. Standard handbook tradition and Crist's West Germanic discussion establish the development within broader accounts of inflectional morphology [@Bammesberger1992, p. 39; @Crist2002, p. 1]. The derivation of *ræste* 'rest' demonstrates the local order: final \emph{*ō}-raising ([SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), Chapter 2) must precede final \emph{*z}-loss.

The internal CAPR rule is labelled [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion), placing it in the Early Anglo-Frisian corridor (CAPR's operational post-Proto-West-Germanic stage on the English line); the historical development is a West Germanic pan-WGmc loss of final \emph{*z}, not a Proto-Germanic one. The exact scope (whether all West Germanic or specifically Ingvaeonic) and the precise relationship between this rule and West Germanic rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)) remain flagged for targeted chronology audit.

Final z-loss follows long-o raising and precedes the later changes in weak
syllables.

## SC020. West Germanic final \emph{*z}-deletion (`EAFFinalZDeletion`) {#rule-EAFFinalZDeletion}

```foma
define EAFFinalZDeletion [{*z} -> 0 || _ .#.];
```

The chronology of word-final \emph{*z}-loss is unusually well delimited: *ræste* 'rest' supplies its early boundary, while later weak syllables supply its late boundary.

Before [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), PGmc [rástōz]{.recon} 'rest' yields [*rast*]{.pred} rather than expected OE *ræste* 'rest'. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [bébruz]{.recon} 'beaver' yields [*befro*]{.pred} rather than expected *befer* 'beaver', PGmc [kwéðuz]{.recon} 'cud' yields [*cwedo*]{.pred} rather than expected *cwedu* 'cud', and PGmc [félθuz]{.recon} 'field' yields [*feldo*]{.pred} rather than expected *feld* 'field', alongside eight other newly failing rows. Final \emph{z}-loss therefore follows [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising) and precedes [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The [rástōz]{.recon} 'rest' derivation fixes the local relation to [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising). The distant boundary at [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) shows only that word-final \emph{*z}-loss precedes the later weak-syllable sequence; its placement within that wider interval follows the handbook chronology after final \emph{*ō}-raising.

\newpage

# Anglo-Frisian ai-monophthongization

## Historical discussion

Inherited stressed \emph{*ái} monophthongized to \emph{*ā} across the North Sea Germanic area. Ringe and Taylor place the monophthongization of \emph{*ai} among the widespread early vowel developments of the English line [@RingeTaylor2014, pp. 40--41]. Versloot shows that the stressed development spread in successive waves through a dialect continuum, with Old English among the widest to carry it [@Versloot2017, pp. 281--324]. The Old English \emph{*ā} is later fronted to \emph{ǣ} in the relevant environments.

The change is areal in character. It is shared with Frisian, and its spread through the continuum gives it a range of dates and no single sharp moment.

All twenty-four corpus witnesses carry stressed \emph{*ái}; loam \emph{*láimą} 'loam' is one of them, stressed in its Old English protoform. The unstressed development \emph{*ai > *ē} is the separate earlier change [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).

## \CAPRRuleHeading{SC004. Anglo-Frisian ai-monophthongization}{EAFAiMonophthongization} {#rule-EAFAiMonophthongization}

```foma
define EAFAiMonophthongization [
    {*ái} -> {*ā}
];
```

The soul form fixes the relation to interstress raising. If the monophthongization is delayed until after that change, PGmc [sáiwalō]{.recon} 'soul' yields [*sāwel*]{.pred} rather than expected OE *sāwol* 'soul'. An earlier placement changes no output. This shows that [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The unstressed development \emph{*ai > *ē} in final and nonfinal syllables is a separate and earlier change; see [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).

\newpage

# Anglo-Frisian brightening

## Historical discussion

Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments. Later Old English developments presuppose this fronted stage even where they partly conceal it. Campbell gives the classical statement of the change, Hogg supplies the standard modern labels, and Ringe and Taylor establish its local chronology with breaking and restoration [@Campbell1959, p. 52, §131; @HoggPhonology1992, pp. 102, 105; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

Brightening creates the input to [SC044 OEBreaking](#rule-OEBreaking), while [SC046 OEARestoration](#rule-OEARestoration) later partly reverses its outcome before back vowels.

## \CAPRRuleHeading{SC043. Fronting of low \emph{*a} outside nasal environments}{EAFBrightening} {#rule-EAFBrightening}

```foma
define EAFBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

Two derivations place low \emph{*a} > \emph{*æ} between unrounding and breaking. Before [SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding), PGmc [rástōz]{.recon} ‘rest’ yields [*rasta*]{.pred} rather than expected OE *ræste* ‘rest’. After [SC044 OEBreaking](#rule-OEBreaking), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. The first witness requires brightening to receive the outcome of the surviving-bimoric \emph{*ō} development; the second requires breaking to receive the fronted vowel.

\newpage

# Chapter 4. From Anglo-Frisian to Old English


## Historical interval

This chapter covers the sound changes that occurred within the Old English period:
the changes that produced attested Old English from the prehistoric English forms
that emerged from the Anglo-Frisian stage. The starting point is the end of the
Anglo-Frisian changes of Chapter 3; the ending point is attested West Saxon Old
English, the primary dialect of the CAPR corpus.

## Scope and dialect variation

Not every change in this chapter has pan-Old-English scope. Some changes — most
notably the West Saxon palatal-glide effects (SC016) and West Saxon palatal
umlaut (SC060), the back-mutation rules (SC059), and the West Saxon diphthong
chain (SC031–SC034) — are specifically West Saxon or more broadly southern Old
English phenomena.

The CAPR derivations target West Saxon Old English citation forms as the default
comparator. Changes that belong to other dialects, or that are absent from West
Saxon, may appear in lexical entries as comparanda rather than as derivational
steps.

The existing reader-facing sound-change sections record which changes have
pan-Old-English scope and which are specifically West Saxon or Anglian
[@Campbell1959, §§ 1--10; @HoggPhonology1992, §§ 1.1--1.15].

## Chapter structure

The changes in this chapter fall into several natural historical subgroups,
though the boundaries between them are not always sharp:

Early Old English changes linked to the Anglo-Frisian inheritance:
Changes that feed directly on, or are closely related to, the brightening of
Chapter 3. The `*awj` glide formation (SC029), `*au` fronting (SC030), and
the West Saxon diphthong chain (SC031–SC034) all operate on the vowel inventory
shaped by Anglo-Frisian brightening. OE Breaking (SC044) and
a-Restoration (SC046) similarly presuppose the fronted `*æ` input.

Old English consonantal changes:
Velar palatalization (SC052), palatalization of `*sk` (SC051), j-cluster
coalescence (SC057), and related changes produce the characteristically
Old English consonant phonemes. Hogg discusses these as OE consonant changes
that are not broadly West Germanic [@HoggPhonology1992, §§ 7.18--7.23].

Old English i-umlaut and its context:
The i-umlaut (SC055) is one of the most productive changes in the Old English
nominal and verbal morphology. Its relative chronology in relation to breaking,
palatalization, and back-mutation is carefully documented in the existing
CAPR chronology evidence audit and individual dossiers
[@Campbell1959, §§ 193--204; @HoggPhonology1992, §§ 5.62--5.68].

Late Old English syllabic reduction and apocope:
High-vowel apocope (SC063), medial syncope (SC065), and the cluster of
late unstressed-vowel changes (SC069–SC078) represent the later stage of Old
English phonological history, when the syllabic structure of the language
began to shift toward the more reduced profile of Middle English.

## Cascade positions and historical order

The cascade positions of changes in this chapter broadly follow historical
sequence within the Old English period. Some divergences exist and are documented
in the individual sound-change sections:

* SC041 (PWGmc Final Bare-`*a` Loss) and SC042 (Surviving Bimoric `*ō`
  Unrounding) appear late in the cascade but are assigned to Chapter 2
  (Proto-West Germanic) for historical reasons; their sections appear there.
* SC064 (NWGmc `*-n` Stem `*n` Loss) carries a Northwest Germanic label and is
  assigned to Chapter 2 historically, but appears in the cascade after OE
  High-Vowel Apocope (SC063). Its section cross-references this divergence.
* SC049 (PGmc B Allophony) is assigned to Chapter 1 historically but appears
  in the cascade here; its section cross-references Chapter 1.

## Sources

Campbell's *Old English Grammar* is the primary source for the dating and
scope of individual changes in this chapter [@Campbell1959].
Hogg's *Grammar of Old English* provides modern reassessments and additional
relative-chronology evidence [@HoggGrammar1992]. Ringe and Taylor supply the most
detailed relative-chronology analysis for the earlier portion of the chapter,
through back-mutation [@RingeTaylor2014, pp. 70--160]. Fulk's *Comparative
Grammar* provides additional coverage for morphological conditioning
[@Fulk2018]. For individual changes, source-specific citations appear in the
relevant sound-change sections.

# West Saxon palatal glide before back vowels

## Historical discussion

West Saxon spellings such as *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ*
'youth' reflect an early Old English development before back vowels. Campbell gives the
most direct handbook statement of the phenomenon [@Campbell1959, p. 17, §44].

The sources establish [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide), although the lexical evidence establishes only a later boundary. The rule is computationally
positioned before [SC017 PNWGmcULowering](#rule-PNWGmcULowering) because the
derivation of *ġeoc* 'yoke' requires glide insertion before u-lowering applies. That
computational dependency places [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) in the Old English section of the cascade
even though the cascade position precedes many Northwest Germanic changes.

## \CAPRRuleHeading{SC016. West Saxon palatal glide before back vowels}{OEWsPalatalGlide} {#rule-OEWsPalatalGlide}

```foma
define OEWsPalatalGlide [
    {*j} {*u} -> {*j} {*e} {*u} || .#. _,
    {*j} {*ú} -> {*j} {*é} {*u} || .#. _
] .o. [
    {*ʤ} {*u} -> {*ʤ} {*e} {*u} || .#. _,
    {*ʤ} {*ú} -> {*ʤ} {*é} {*u} || .#. _
] .o. [
    {*ʧ} {*u} -> {*ʧ} {*e} {*u} || .#. _,
    {*ʧ} {*ú} -> {*ʧ} {*é} {*u} || .#. _
] .o. [
    {*ʃ} {*u} -> {*ʃ} {*e} {*u} || .#. _,
    {*ʃ} {*ú} -> {*ʃ} {*é} {*u} || .#. _
];
```

OE *ġeoc* 'yoke' fixes the close relation between glide insertion before back-vocalic \emph{u} and the following change.

If glide insertion follows [SC017 PNWGmcULowering](#rule-PNWGmcULowering), PGmc [júką]{.recon} 'yoke' yields [*ġoc*]{.pred} rather than expected OE *ġeoc* 'yoke'; earlier placement changes no output. The witness therefore dates [SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) before u-lowering without supplying an earlier boundary. The *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ* 'youth' material establishes the lexical scope of the West Saxon development.

\newpage

# Awj glide formation and au-fronting

## Historical discussion

The *hīeġ* 'hay' and *strīeġan* 'strew' material undergoes both changes. Glide formation reshapes the older \emph{awj} sequence, and fronting then affects the resulting \emph{au}. Campbell's discussion of these outcomes and Ringe and Taylor's derivations of *hīeġ* and *strīeġan* describe the same sequence [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

Glide formation creates the input to fronting; diphthong leveling follows both.

## Historical discussion of awj glide formation

Older \emph{awj} sequences are the source of forms such as *hīeġ* ‘hay’ and *strīeġan* ‘strew’. Campbell treats the relevant developments directly, and Ringe and Taylor likewise trace the same material through intermediate \emph{auj}-type stages [@Campbell1959, p. 46, §120; @RingeTaylor2014, p. 188].

The sources establish glide formation, while the witness forms supply only a later boundary.

## SC029. Glide formation in \emph{*awj} (`OEAwjGlideFormation`) {#rule-OEAwjGlideFormation}

```foma
define OEAwjGlideFormation [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j},
    {*á} {*w}      {*j} -> {*áu} {*j},
    {*a} {*w}      {*j} -> {*au} {*j}
];
```

The *hīeġ* 'hay' and *strīeġan* 'strew' derivations show that \emph{awj} reshaping prepared the input to fronting. If fronting is applied first, PGmc [xáwwją]{.recon} ‘hay’ yields [*hauġ*]{.pred} rather than expected OE *hīeġ* ‘hay’, and PGmc [stráwjaną]{.recon} ‘strew’ yields [*strauian*]{.pred} rather than expected *strīeġan* ‘strew’. Earlier placement of glide formation changes no output, so these forms supply an upper boundary without a corresponding lower one.

## Historical discussion of au-fronting

Once the glide sequence is in place, \emph{au}-fronting produces the fronted
diphthongal outcomes of the broader West Saxon vowel history. Campbell
describes \emph{au} > \emph{ēa} [@Campbell1959, pp. 53--54, §135].

Fronting must follow glide formation and precede diphthong leveling, which applies to a wider set of derivations.

## SC030. Fronting of \emph{*au} (`OEAuFronting`) {#rule-OEAuFronting}

```foma
define OEAuFronting [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

Two distinct failure sets confine fronting. Placed before glide formation, it produces the wrong forms: PGmc [xáwwją]{.recon} ‘hay’ yields [*hauġ*]{.pred} rather than expected OE *hīeġ* ‘hay’, and PGmc [stráwjaną]{.recon} ‘strew’ yields [*strauian*]{.pred} rather than expected *strīeġan* ‘strew’. Placed after diphthong leveling, PGmc [galáubijaną]{.recon} ‘believe’, [bráudą]{.recon} ‘bread’, and [dráugmaz]{.recon} ‘dream’, together with sixteen other derivations, fail to produce output at all (\emph{+?}) instead of yielding expected OE *ġelīefan* ‘believe’, *brēad* ‘bread’, and *drēam* ‘dream’. The lexical errors require fronting to follow glide formation, while the failed derivations require it to precede diphthong leveling.

The later failure set consists of failed derivations, not competing Old English
surface forms.

\newpage

# West Saxon diphthong sequence

## Historical discussion

Four distinct developments shape the West Saxon diphthongal field. Campbell
discusses inherited \emph{aw}/\emph{ew} outcomes, palatal-triggered
diphthongization, and later Anglian smoothing in connected but separate parts
of the vowel history; Hogg likewise distinguishes the palatal-diphthongal
developments [@Campbell1959, pp. 46, 53--54, 65--70, 95--96,
§§120, 135--136, 170--176, 185, 223--227; @HoggPhonology1992, p. 112].

The closest interaction joins \emph{ww}-simplification and long-\emph{aw} diphthongization, which together shape *dēaw* ‘dew’ and *hēawan* ‘hew’. Diphthong leveling regularizes a wider field, while long-\emph{ew} diphthongization carries \emph{ēow} into the later environment of breaking.

## Historical discussion of WW simplification

West Germanic \emph{ww} sequences lie behind forms such as *dēaw* ‘dew’ and *hēawan* ‘hew’, and Campbell treats them as part of the early West Germanic diphthong history [@Campbell1959, p. 46, §120].

[SC031 OEWWSimplification](#rule-OEWWSimplification) precedes the later
long-diphthong outcomes.

## SC031. Simplification of \emph{*ww} sequences (`OEWWSimplification`) {#rule-OEWWSimplification}

```foma
define OEWWSimplification [
    {*w} {*w} -> {*w}
];
```

The *dēaw* 'dew' and *hēawan* 'hew' derivations establish that doubled \emph{w} was simplified before the long \emph{ēaw} development. If [SC031 OEWWSimplification](#rule-OEWWSimplification) follows [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc [dáwwō]{.recon} ‘dew’ yields [*dawu*]{.pred} rather than expected OE *dēaw* ‘dew’, and PGmc [xáwwaną]{.recon} ‘hew’ yields [*hawan*]{.pred} rather than expected *hēawan* ‘hew’. Earlier placement changes no output. The witnesses require simplification before the long-diphthong change and leave the lower boundary to the broader West Saxon chronology.

## Historical discussion of diphthong leveling

Forms such as *hēafod* ‘head’ reflect the redistribution of diphthongal
outcomes across a wider set of words. Campbell describes smoothing and related
later monophthongization, although the rule below is more narrowly conditioned
than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

The evidence for [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) is less
self-contained than that for the *dēaw* 'dew' / *hēawan* 'hew' developments.

## SC032. Leveling of diphthongal outputs (`OEDiphthongLeveling`) {#rule-OEDiphthongLeveling}

```foma
define OEDiphthongLeveling [
    {*aeu} -> {*ēa},
    {*áeu} -> {*ēa},
    {*eu} -> {*ēo},
    {*éu} -> {*ēo},
    {*iu} -> {*ēo},
    {*íu} -> {*ēo},
    {*e} {*u} -> {*eo},
    {*é} {*u} -> {*éo},
    {*i} {*u} -> {*eo}
];
```

The two edges of this interval fail differently. Before [SC030 OEAuFronting](#rule-OEAuFronting), PGmc [galáubijaną]{.recon} ‘believe’, [báug]{.recon} ‘bow’, and [bráudą]{.recon} ‘bread’ produce no output (\emph{+?}) instead of expected OE *ġelīefan* ‘believe’, *bēag* ‘bow’, and *brēad* ‘bread’, alongside fifteen other failed derivations. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [xáubudą]{.recon} ‘head’ yields [*hēafud*]{.pred} rather than expected *hēafod* ‘head’. Absence at the lower edge places diphthong leveling after fronting; the wrong surface form at the upper edge places it before medial unstressed-\emph{u} lowering.

## Historical discussion of long \emph{ēow}

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow*
‘knee’ form part of the West Saxon vowel history, although their clearest
ordering relation points forward. Campbell describes early \emph{eu} in Old
English, and Ringe and Taylor give the corresponding examples from chew,
four, and knee [@Campbell1959, pp. 53--54, §136;
@RingeTaylor2014, pp. 188, 202].

The only boundary established by the lexical evidence for
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) lies ahead at
[SC044 OEBreaking](#rule-OEBreaking).

## \CAPRRuleHeading{SC033. Long \emph{ēow} before following vowels and weak endings}{OEEwLongDiphthong} {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

The long \emph{ēow} of *ċēowan* 'chew', *fēower* 'four', and *cnēow* 'knee' supplies only a terminus ante quem. If [SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) follows [SC044 OEBreaking](#rule-OEBreaking), PGmc [kéwwaną]{.recon} ‘chew’ yields [*ċeowan*]{.pred} rather than expected OE *ċēowan* ‘chew’, PGmc [fédwōr]{.recon} ‘four’ yields [*feower*]{.pred} rather than expected *fēower* ‘four’, and PGmc [knéwą]{.recon} ‘knee’ yields [*cneow*]{.pred} rather than expected *cnēow* ‘knee’. Earlier placement changes no output. The sources associate \emph{ew} and \emph{iw} with the same diphthongal history but furnish no lower boundary.

## Historical discussion of long \emph{ēaw}

After [SC031 OEWWSimplification](#rule-OEWWSimplification) has reduced \emph{ww} to single \emph{w}, the remaining \emph{aw} sequence can develop into the long \emph{ēaw} seen in *dēaw* 'dew' and *hēawan* 'hew'. Campbell treats these outputs in the early diphthong history of West Germanic and Old English [@Campbell1959, pp. 46, 53--54, §§120, 135--136].
The resulting long diphthong is \emph{ēaw}.

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) follows [SC031 OEWWSimplification](#rule-OEWWSimplification) locally and must also precede [SC043 EAFBrightening](#rule-EAFBrightening).

## SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

A local feeding relation and a later vowel change confine \emph{aw} > \emph{ēaw}. Before [SC031 OEWWSimplification](#rule-OEWWSimplification), PGmc [dáwwō]{.recon} ‘dew’ yields [*dawu*]{.pred} rather than expected OE *dēaw* ‘dew’, and PGmc [xáwwaną]{.recon} ‘hew’ yields [*hawan*]{.pred} rather than expected *hēawan* ‘hew’. After [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [skáwōjaną]{.recon} ‘show’ yields [*sċawian*]{.pred} rather than expected OE *sċēawian* ‘show’, PGmc [skáwōθi]{.recon} ‘shows’ yields [*sċawaþ*]{.pred} rather than expected *sċēawaþ* 'shows', and PGmc [stráwą]{.recon} ‘straw’ yields [*stræw*]{.pred} rather than expected *strēaw* ‘straw’. The *dēaw* and *hēawan* forms require long-diphthong formation after simplification, while *sċēawian* requires it before brightening; the handbooks assign the same interval to the West Saxon development.

\newpage

# Prefix and compound adjustments

## Historical discussion of prefixal \emph{*a}-reduction

Weakly stressed prefixes can lose their older low vowel early in Old English,
and that is the historical setting for
[SC035 OEPrefixAReduction](#rule-OEPrefixAReduction). Campbell treats the
small class of pretonic losses directly, while Ringe and Taylor's derivation of
[galaubijana]{.recon} ‘believe’ supplies the comparative witness for the same development
[@Campbell1959, p. 147, §354; @RingeTaylor2014, p. 245;
@RingeTaylor2014, p. 267].

The rule has a narrow historical range and gives prefixed forms the weak vowel inherited by later vocalic changes.

## SC035. Reduction of prefixal \emph{*a} (`OEPrefixAReduction`) {#rule-OEPrefixAReduction}

```foma
define OEPrefixAReduction [
    {*a} -> {*ĕ}
        || .#. {*g} _
           [EnglishStarConsonant | EnglishPalatalConsonant]
           EnglishStarVocalic
];
```

The prefix of *ġelīefan* 'believe' supplies the upper boundary for \emph{*ga-} > \emph{*ge-}. If [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) follows [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [galáubijaną]{.recon} ‘believe’ yields [*ġealīefan*]{.pred} rather than expected OE *ġelīefan* ‘believe’. Earlier placement changes no output, so the witness dates prefix reduction before brightening without locating its beginning.

## Historical discussion of inter-stress raising

[SC036 OEInterStressRaising](#rule-OEInterStressRaising) has the strongest evidence of the three. Campbell's discussion of *weorold* 'world' / *weoruld* 'world' and Ringe and Taylor's derivation of [weraldu]{.recon} 'world' > [weruldu]{.recon} 'world' > OE *weorold* place the rule squarely in the history of low-stress medial vowels [@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 322, §6.3.3].

The rule changes the vowel between stronger stress peaks, and its witnesses consequently constrain the relative chronology.

## \CAPRRuleHeading{SC036. Raising of medial \emph{*a} between stress peaks}{OEInterStressRaising} {#rule-OEInterStressRaising}

```foma
define OEInterStressRaising [
    {*a} -> {*u}
        || PGmcStarVowel EnglishStarConsonant* _
           [EnglishStarConsonant - {*j}]+ [{*u}|{*ū}],
    {*à} -> {*u}
];
```

The two boundaries have unequal force. Before [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), PGmc [sáiwalō]{.recon} ‘soul’ yields [*sāwel*]{.pred} rather than expected OE *sāwol* ‘soul’; after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), it yields [*sāwul*]{.pred} rather than *sāwol*, while PGmc [wír-àldu]{.recon} ‘world’ yields [*weoruld*]{.pred} rather than *weorold* ‘world’. The distant lower boundary places inter-stress raising after final long-\emph{o} raising, and the local upper boundary places it before medial unstressed-\emph{u} lowering. In handbook terms, medial \emph{*a} > \emph{*u} belongs to the \emph{world}- and \emph{soul}-type low-stress vocalism that followed the earlier final-vowel changes.

## Historical discussion of compound linking syncope

Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

[SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope) captures this
pattern in compounds such as *reġnboga* ‘rainbow’. The only boundary the lexical evidence supplies
is the immediately following technical stress-stripping stage, which is not a
sound change.

## \CAPRRuleHeading{SC037. Syncope of compound linking vowels}{OECompoundLinkingSyncope} {#rule-OECompoundLinkingSyncope}

```foma
define OECompoundLinkingSyncope [
    [{*a}|{*i}|{*u}] -> 0
        || PGmcStarAcuteVowel OEAnyConsonant+ _
           OEAnyConsonant+ PGmcStarGraveVowel
];
```

The *reġnboga* 'rainbow' test exposes a bookkeeping dependency rather than a historical sound-change boundary. After SC038 OEStripSecondaryStress, PGmc [régna-bùgô]{.recon} ‘rainbow’ yields [*reġnefoga*]{.pred} rather than expected OE *reġnboga* ‘rainbow’, because the technical stage has erased the stress information that licenses syncope. The handbooks instead place weakened compound junctures with the behavior described under [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising).

\newpage

# Medial unstressed vowel changes

## Historical discussion

The history of *wuduwe* ‘widow’ orders these two changes within the same
low-stress vocalic development. Campbell discusses both the
\emph{w}-conditioned \emph{u} forms and the later *weorold* 'world' / *weoruld* 'world'
alternation, while Ringe and Taylor give the same connection comparatively in
\emph{*widuwon-}, [weraldu]{.recon} 'world', and [jugunþi]{.recon} 'youth'
[@Campbell1959, p. 92, §218; @Campbell1959, p. 140, §332;
@Campbell1959, pp. 141--142, §§338--339; @RingeTaylor2014, p. 267;
@RingeTaylor2014, p. 322, §6.3.3].

[SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) feeds the vowel
sequence subsequently reshaped by
[SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).
Initial \emph{w} conditions the first change.

## SC039. Combinative \emph{*u}-umlaut in \emph{wi}-forms (`OEWICombinativeUUmlaut`) {#rule-OEWICombinativeUUmlaut}

```foma
define OEWICombinativeUUmlaut [
    {*í} -> {*ú}
        || .#. {*w} _ EnglishStarConsonant [{*u} | {*o}]
];
```

The *wuduwe* ‘widow’ derivation answers one narrow question about \emph{wi}-forms. If [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) follows [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [wíduwōn]{.recon} ‘widow’ yields [*wudowe*]{.pred} rather than expected OE *wuduwe*; earlier placement changes no output. The witness requires combinative u-umlaut to precede medial lowering and supplies no lower boundary.

## \CAPRRuleHeading{SC040. Lowering of medial unstressed \emph{*u}}{OEMedUnstressedULowering} {#rule-OEMedUnstressedULowering}

```foma
define OEMedUnstressedULowering [
    {*u} -> {*o}
        || [EnglishStarVocalic - [{*u}|{*ū}|{*ú}]]
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _
           [[EnglishStarConsonant | EnglishPalatalConsonant] - {*m}]
];
```

The two witnesses date medial unstressed \emph{*u} > \emph{*o} at very different scales. Before [SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut), PGmc [wíduwōn]{.recon} ‘widow’ yields [*wudowe*]{.pred} rather than expected OE *wuduwe* ‘widow’; after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [júgunθ]{.recon} ‘youth’ yields [*ġeogoþ*]{.pred} rather than expected *ġeoguþ* ‘youth’. The local *weorold* 'world' and widow evidence places lowering after combinative u-umlaut, while the youth form supplies only the distant requirement that lowering precede unstressed long-vowel shortening.

\newpage

# Breaking and velar-fricative palatalization

## Historical discussion

Breaking creates \emph{eo}-type outputs before \emph{h}, \emph{rC}, and
\emph{lC}; velar-fricative palatalization then operates in that reshaped
environment. Campbell, Ringe and Taylor, and Fulk place breaking after
brightening. The following fricative palatalization is more narrowly
conditioned [@Campbell1959, pp. 54, 166, §§139, 405--406;
@RingeTaylor2014, pp. 168--169, 213--214, §§6.2.1--6.2.3, 6.4.1--6.4.2;
@Fulk2018, pp. 73--74, §4.13].

Breaking has the fuller handbook treatment, while velar-fricative palatalization follows it locally in the *feoh* 'cattle' and *feohtan* 'fight' type derivations.

## SC044. Breaking before \emph{h}, \emph{rC}, and \emph{lC} (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

Breaking must encounter the vowel created by brightening and must precede the fricative change seen in *feoh* ‘fee’ and *feohtan* ‘fight’. Before [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. After [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc [féxu]{.recon} ‘cattle’ yields [*fehu*]{.pred} rather than expected OE *feoh*, and PGmc [féxtaną]{.recon} ‘fight’ yields [*fehtan*]{.pred} rather than expected *feohtan*. The two feeding relations place breaking between brightening and velar-fricative palatalization.

## \CAPRRuleHeading{SC045. Palatalization of velar fricatives beside front vowels}{OEVelarFricativePalatalization} {#rule-OEVelarFricativePalatalization}

```foma
define OEVelarFricativePalatalization [
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*ɣ} -> {*j} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*ɣ} -> {*j} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j},
    {*ɣ} -> {*j} || _ {*j}
]
    .o. EnglishStarAlphabet*;
```

The local chronology comes from *feoh* 'cattle' and *feohtan* 'fight'. Before [SC044 OEBreaking](#rule-OEBreaking), palatalization of \emph{*x} and \emph{*ɣ} beside front vowels or \emph{*j} makes PGmc [féxu]{.recon} ‘cattle’ yield [*fehu*]{.pred} rather than expected OE *feoh*, and PGmc [féxtaną]{.recon} ‘fight’ yield [*fehtan*]{.pred} rather than expected *feohtan*. The distant upper limit comes from *six* 'six': after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut), PGmc [séxs]{.recon} ‘six’ yields [*sihs*]{.pred} rather than expected OE *six*. Breaking therefore feeds velar-fricative palatalization directly, while palatal umlaut supplies only the broader upper limit.

\newpage

# A-restoration and nasal changes

## Historical discussion of A-restoration

Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's later retraction describe the same post-brightening development [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. Some outcomes of Anglo-Frisian fronting survive only in environments where restoration does not return them to back \emph{a}.

[SC046 OEARestoration](#rule-OEARestoration) has firmer handbook support than the two following nasal rules.

## \CAPRRuleHeading{SC046. Restoration of \emph{*a} before following back vowels}{OEARestoration} {#rule-OEARestoration}

```foma
define OEARestoration (
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
);
```

Restoration must receive fronted \emph{*æ} and return \emph{*a} before the nasal-tail changes. Before [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [bákaną]{.recon} ‘bake’ yields [*bæcan*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc [fáraną]{.recon} ‘fare’ yields [*færan*]{.pred} rather than expected *faran* ‘fare’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), [bákaną]{.recon} again yields [*bæcan*]{.pred} instead of *bacan*, while PGmc [wádaną]{.recon} ‘wade’ yields [*wædan*]{.pred} instead of *wadan* ‘wade’. These independent witness pairs place restoration after brightening and before secondary nasalization.

## Historical discussion of heavy-syllable nasal loss and secondary nasalization

Heavy-syllable nasal apocope removes the final nasalized vowel; secondary
nasalization then marks the preceding \emph{a} before final \emph{n}. The
handbooks do not isolate both developments under equally prominent labels.
Campbell describes later nasal loss and the back-mutation environment; Ringe
and Taylor provide the later relation to back mutation
[@Campbell1959, pp. 86, 166, §§205--206, 403;
@RingeTaylor2014, p. 319, §6.9.4].

The reciprocal failure set fixes the order: apocope removes the ending before
secondary nasalization acts on the remaining structure. Restoration receives
the fuller historical treatment in the handbooks.

## \CAPRRuleHeading{SC047. Heavy-syllable nasal apocope of final \emph{*ą}}{OEHeavySyllableNasalApocope} {#rule-OEHeavySyllableNasalApocope}

```foma
define OEHeavySyllableNasalApocope [
    {*ą} -> 0 || OEAnyConsonant _ .#.
];
```

The evidence for final nasalized \emph{*ą} loss is sharply asymmetric. Before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), the single PGmc witness [stráwą]{.recon} ‘straw’ yields [*stræw*]{.pred} rather than expected OE *strēaw* ‘straw’. After [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc [bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc [bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* ‘bind’, alongside a broad \emph{-en} failure set. One lower witness places apocope after long-diphthong formation; many reciprocal upper failures place it before secondary nasalization.

## \CAPRRuleHeading{SC048. Secondary nasalization before final \emph{*n}}{OESecondaryNasalization} {#rule-OESecondaryNasalization}

```foma
define OESecondaryNasalization [
    {*a} -> {*ą} || _ {*n} .#.
];
```

The broad \emph{-an}/\emph{-en} split fixes the lower boundary of final \emph{*a} nasalization before \emph{n}. Before [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope), PGmc [bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* 'bake', and PGmc [bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* 'bind'. The upper boundary comes from back mutation. After [SC059 OEBackMutation](#rule-OEBackMutation), PGmc [stélaną]{.recon} ‘steal’ yields [*steolan*]{.pred} rather than expected OE *stelan* ‘steal’, and PGmc [wébaną]{.recon} ‘weave’ yields [*weofan*]{.pred} rather than expected *wefan* ‘weave’. Reciprocal nasal-tail failures place secondary nasalization after apocope, and the later mutation witnesses place it before back mutation; [SC046 OEARestoration](#rule-OEARestoration) retains the clearest independent historical support.

\newpage

# Palatalization of \emph{*sk} to \emph{*sc}

## Historical discussion

The palatalization of \emph{*sk} to Old English \emph{*sc} is one of the recognizable early
cluster changes in the larger palatalization zone. Campbell distinguishes the
cluster from plain velars when he remarks that \emph{*sk} is especially prone to
palatalization and assibilation [@Campbell1959, p. 278, §440]. Hogg gives the
same change a clearer structural place by treating \emph{*sk} beside the palatalization
of plain velars and before the later West Saxon diphthongal developments
[@HoggPhonology1992, pp. 107, 112]. Ringe and Taylor make the same sequence
explicit when they distinguish the earlier palatalization of velars and \emph{*sk} from
the later diphthongization after already palatal consonants
[@RingeTaylor2014, pp. 213--216, §§6.4.1, 6.5.1].

Luick places the cluster change within a broader early movement toward palatal
articulation, while still allowing later vowel consequences to form a different
chapter of the history [@Luick1914, p. 157, §168]. Fulk's
summary is the most concise warning against overextension: Old English \emph{*sc} is
palatal except in the well-known back-vowel environments that preserve harder
outcomes [@Fulk2018, p. 28]. The result is a historically clear rule, but not an
identity between the cluster change and the later umlautal developments.

## SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization}

```foma
define OESkPalatalization [
    {*s} {*k} -> {*ʃ} || .#. _
] .o. [
    {*s} {*k} -> {*ʃ} || EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)
] .o. [
    {*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel
] .o. [
    {*s} {*k} -> {*ʃ} || _ {*j}
] .o. [
    {*s} {*k} -> {*ʃ} || {*j} _
];
```

The non-fronted vowels of *flasce* ‘flask’ and *wascan* ‘wash’ fix the lower boundary of \emph{*sk} > \emph{*sc}. Before [SC046 OEARestoration](#rule-OEARestoration), the forms are fronted too soon, yielding *flæsce* ‘flask’ and *wæscan* ‘wash’ rather than expected OE *flasce* and *wascan*. This places [SC051 OESkPalatalization](#rule-OESkPalatalization) after restoration.

Five witnesses establish the upper boundary collectively. The palatal cluster must already underlie *sċeaft* ‘shaft’, *sċēar* ‘shear’, *sċēaþ* ‘sheath’, *sċēap* ‘sheep’, and *sċield* ‘shield’ before [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization). The \emph{*sċea-* 'sea'}/\emph{*sċie-*} set therefore places cluster palatalization before the West Saxon vowel change. The cluster change occupies the same palatalization zone as [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) while remaining distinct from plain-velar palatalization and the later vowel changes.

\newpage

# Velar palatalization before front vowels

## Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168]. His emphasis falls on the environment first: velars
before bright vowels and in the vicinity of the palatal glide belong to one
early phonological sequence. The examples associated with that sequence, such as
*ceaster* ‘town’, *geaf* ‘gave’, *giefan* ‘give’, and *giest* ‘guest’, already
show that consonantal palatalization and later vowel effects stand close
together historically, even when they must be distinguished analytically
[@Luick1914, pp. 157--167, §§168--182].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to
palatalization and assibilation than [k]” is brief, but it makes clear that
different members of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440]. Elsewhere in the same part of the grammar he uses
forms such as *cild* ‘child’, *dæg* ‘day’, *giefan* ‘give’, and *giest*
‘guest’, which show how palatalized velars, palatal influence, and later
umlautal outcomes meet in the same region of the lexicon without collapsing
into one process [@Campbell1959, pp. 69--72, 89, §§170, 190--191].

Hogg makes the conditioning sharper still. He states that the change takes place
when the velar consonant is adjacent to and in the same syllable as a front
vowel or the palatal consonant `j` [@HoggPhonology1992, p. 106]. This formulation
replaces a broad list of palatal outcomes with a phonological environment
defined by adjacency and syllable structure.

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and \emph{*sk} had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1]. Their own examples of the plain-velar rule,
such as \emph{weccan} ‘wake’, \emph{licgan} ‘lie’, \emph{lecgan} ‘lay’,
\emph{secg} ‘retainer’, \emph{ecg} ‘edge’, \emph{wicg} ‘horse’, and
\emph{brycg} ‘bridge’, illustrate the same point in lexical detail: front
vowels and `j` create the palatal environment in which plain `k` and `g` cease
to behave as plain velars [@RingeTaylor2014, pp. 213--214, §6.4.1].

Luick describes a broad early movement; Campbell distinguishes plain velars
from the `sk` complex; Hogg specifies the adjacency and syllable conditions;
and Ringe and Taylor order the plain-velar change before West-Saxon
diphthongization. Plain-velar palatalization thus forms part of a wider
palatalizing environment without being identical to its neighboring changes.

## \CAPRRuleHeading{SC052. Palatalization of \emph{*k} before front vowels and \emph{*j}}{OEVelarPalatalizationKFront} {#rule-OEVelarPalatalizationKFront}

```foma
define OEVelarPalatalizationKFront [
    {*k} -> {*ʧ} || .#. _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || _ [{*i} | {*ī}],
    {*k} -> {*ʧ} || _ {*ḯ},
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || {*ḯ} _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ .#.,
    {*k} -> {*ʧ} || {*ḯ} _ .#.
] .o. [
    {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j}
] .o. [
    {*k} -> {*ʧ} || _ {*j}
] ;
```

The *weccan* ‘wake’, *licgan* ‘lie’, and *lecgan* ‘lay’ set identifies front vowels and `j` as the environment for palatalization of `k` [@RingeTaylor2014, pp. 213--214, §6.4.1]. These forms establish the conditioning; different witnesses establish the chronology.

Applied before Sievers-law syncope, PGmc [strákkijaną]{.recon} ‘stretch’ yields [*strecċan*]{.pred} rather than expected OE *streċċan* ‘stretch’. Applied after i-umlaut fronting, PGmc [kūi]{.recon} ‘cow’ and [lúnganjō]{.recon} ‘lungs’ yield *ċȳ* 'cows' and *lunġen* 'lungs' rather than expected OE *cȳ* 'cows' and *lungen* 'lungs'. The front-vowel `k` change therefore follows Sievers-law syncope and precedes i-umlaut fronting.

## \CAPRRuleHeading{SC052. Velar palatalization before front vowels}{OEVelarPalatalization} {#rule-OEVelarPalatalization}

```foma
define OEVelarPalatalization [
    OEVelarPalatalizationKFront
] .o. [
    {*g} -> {*ʤ} || _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ [EnglishStarConsonant - {*j}],
    {*g} {*g} -> {*ʤ} {*ʤ} || _ {*j}
] .o. [
    {*g} -> {*ʤ} || _ {*j}
];
```

Plain `k` and `g` palatalization in front-vocalic and `j`-adjacent environments follows `sk`-palatalization and occupies a sharply defined pre-umlaut interval. Applied before Sievers-law syncope, PGmc [strákkijaną]{.recon} ‘stretch’ yields [*strecċan*]{.pred} rather than expected OE *streċċan* ‘stretch’. Applied after general i-umlaut, PGmc [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} rather than expected *cȳ* ‘cows’, and PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected *lungen* ‘lungs’. These witnesses place velar palatalization after Sievers-law syncope and before umlaut.

Luick, Campbell, and Ringe and Taylor place *cild* ‘child’ and *dæg* ‘day’ in a consonantal palatalization that precedes later vowel fronting [@Luick1914, p. 157, §168; @Campbell1959, p. 278, §440; @RingeTaylor2014, pp. 203--215, §§6.4.1, 6.5.1]. The umlautal developments therefore receive plain `k` and `g` already reshaped beside front vowels and `j`.

The `sk` change belongs to the same palatalizing region with a separate scope. The *streċċan* ‘stretch’ evidence establishes a specific dependency on earlier syncope; it does not merge the two changes into one process.

\newpage

# Post-velar \emph{*w}-loss and loss of \emph{*w} before final \emph{*i}

## Historical discussion

The first rule is a narrow loss of \emph{*w} after velars in the \emph{*ngw}
sequence. Ringe and Taylor derive PGmc [singwan]{.recon} ‘sing’ to Old English *singan*
‘sing’ [@RingeTaylor2014, p. 214, §6.4.2]. This comparative evidence establishes
the change, although no lexical evidence fixes its order relative to a neighboring
rule.

The second rule is historically more legible. Campbell notes the recurring loss
of \emph{*w} before \emph{*i} in unstressed position [@Campbell1959, p. 167, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier \emph{*saiwi-} / \emph{*sawi-}
[@RingeTaylor2014, p. 257, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, p. 173, §187]. The first rule is restricted to
the \emph{*ngw} sequence; the second has a specific lexical witness and defined
earlier and later limits.

## SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

The comparative development `*singwan > singan` establishes narrow post-velar \emph{*w}-loss in the \emph{*ngw} sequence, yielding *singan* ‘sing’. Moving [SC053 OEPostVelarWLoss](#rule-OEPostVelarWLoss) earlier or later leaves every output unchanged. Its pre-umlaut position therefore rests on comparative evidence, while the present lexicon supplies no neighboring boundary.

## SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

The history of *sǣ* ‘sea’ explains why non-initial \emph{*w} disappeared before final unstressed \emph{*i}. Campbell describes the loss, Ringe and Taylor derive the form from \emph{*saiwi-}/\emph{*sawi-}, and Luick gives the parallel trajectory [@Campbell1959, p. 167, §406; @RingeTaylor2014, p. 257, §6.7.1; @Luick1914, p. 173, §187]. Loss of the glide allowed the preceding vowel to undergo the later fronting and lengthening.

The same witness supplies two distant limits. Before [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion) or after [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope), [SC054 OEWLossBeforeI](#rule-OEWLossBeforeI) yields [*sǣw*]{.pred} rather than expected OE *sǣ* 'sea'. The loss must therefore follow final \emph{z}-deletion and precede high-vowel apocope, while its exact position within that broad interval remains source-based.

\newpage

# The Old English i-umlaut and West Saxon palatal diphthongization

## Historical discussion

Luick gives the change its traditional scale:

> Der wichtigste Fall von palataler Beeinflussung … war die Veränderung der
> urenglischen Vokale durch i oder j der Folgesilbe.
>
> [@Luick1914, pp. 166--167, §182]

Campbell gives the most compact classical formulation in English when he writes
that “the process known as i-umlaut or i-mutation operates on practically all
the sounds which it could theoretically affect in OE” [@Campbell1959, p. 69,
§190]. He immediately defines the core conditioning environment as a following
`i` or `j`, and he goes on to trace the consequences across much of the vowel
system, including forms such as *giest* ‘guest’, *giefan* ‘give’, *hierde*
‘shepherd’, and *ieldra* ‘older’ [@Campbell1959, pp. 69--72, §§190--197].

Hogg continues in the same vein: “we come now to a change which is almost as
uncontroversial as it is important” [@HoggPhonology1992, p. 113]. His examples, such as
*bryd* ‘bride’, *trymman* ‘strengthen’, *bedd* ‘bed’, *ciest* ‘chest’, and
*wiersa* ‘worse’, likewise emphasize that the change is a broad redistribution
of vowel quality across the Old English vowel system [@HoggPhonology1992,
pp. 113--114].

The narrower palatal-diphthongal material is described differently. Ringe and
Taylor treat West-Saxon diphthongization after initial palatals as a distinct
process [@RingeTaylor2014, p. 215, §6.5.1], and Fulk is even more explicit about
its chronological delicacy when he calls it “diphthongization by initial
palatal consonants (which precedes front umlaut but not breaking)”
[@Fulk2018, p. 74, §4.13]. Ringe and Taylor’s examples such as *gieldan* ‘pay’,
*scield* ‘shield’, and *scieppan* ‘create’ show that this narrower process is
triggered by already palatal consonants and leads to specifically West-Saxon
diphthongal outputs [@RingeTaylor2014, pp. 215--216, §6.5.1].

Luick, Campbell, and Hogg treat i-umlaut as a system-wide change. Ringe and
Taylor and Fulk distinguish from it a narrower West-Saxon process affecting
words after initial palatals. The two changes act in different environments and
produce different lexical consequences.

## SC055. Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting}

```foma
define OEIUmlautFronting [
    {*a} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ā} -> {*ǣ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*e} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*o} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ō} -> {*ē} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*u} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ū} -> {*ȳ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*á} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*é} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ó} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ú} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

The breadth of i-umlaut appears in lexical classes that share only a following high front vocoid. The forms *fylgan* ‘follow’, *gylden* ‘golden’, *wyrm* ‘worm’, and *giest* ‘guest’ exemplify the same `i`- or `j`-conditioned fronting across different vowels [@RingeTaylor2014, p. 222, §6.6.1; @Campbell1959, pp. 69--72, §§190--191].

The cow and lung forms establish the lower boundary. If fronting precedes velar palatalization, PGmc [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} rather than expected OE *cȳ* 'cows', and [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected OE *lungen* 'lungs'. The consonantal change must therefore precede fronting.

The gift and sheath forms establish the upper boundary. If West Saxon palatal diphthongization precedes fronting, PGmc [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected OE *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ* 'sheath'. Fronting consequently follows velar palatalization and precedes the West Saxon change; the other components of i-umlaut share those bounds.

## SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Raising of umlauted `æ` to `e` continues the same assimilatory event as fronting and therefore shares the chronology of general i-umlaut.

The same four forms fix both boundaries. If raising precedes velar palatalization, [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} instead of expected *cȳ* 'cows' and [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} instead of expected *lungen* 'lungs'. If West Saxon palatal diphthongization precedes raising, [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ* 'sheath'. These forms place raising after velar palatalization and before West Saxon palatal diphthongization.

The sources do not describe umlaut as simple fronting alone. Campbell notes that
the low front vowel
changes again before `m` and `n` in most dialects [@Campbell1959, p. 69, §190],
and Hogg likewise treats short front vowels as part of the same assimilatory
system [@HoggPhonology1992, p. 112].

## SC055. Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong}

```foma
define OEIUmlautDiphthong [
    {*ea} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēa} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*io} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*īo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*eo} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éa} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éo} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ío} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Diphthongal outcomes belong to the same system-wide assimilation as simple-vowel fronting and raising. All three therefore belong to a single historical event.

The relevant examples are the recurring West-Saxon `ie` forms cited in the
handbooks, including *giest* ‘guest’, *giefan* ‘give’, and *hierde*
‘shepherd’ in Campbell and *ciest* ‘chest’ in Hogg
[@Campbell1959, pp. 69--72, 78--80, §§190--191, 248--251; @HoggPhonology1992,
pp. 112--114]. These diphthongal outcomes form a distinct part of the general
umlautal development alongside simple fronting.

The chronology comes from the cow/lung and gift/sheath contrasts. Placed before velar palatalization, diphthongal mutation over-palatalizes [kūi]{.recon} ‘cow’ and [lúnganjō]{.recon} ‘lungs’; placed after West Saxon palatal diphthongization, it yields [*ġieft*]{.pred} and [*sċǣþ*]{.pred} instead of expected *ġift* 'gift' and *sċēaþ* 'sheath'. These failures place diphthongal mutation after velar palatalization and before West Saxon palatal diphthongization.

## SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

The literature presents fronting, raising, and diphthongal mutation as effects of one historical development. They consequently occupy a single place in the Old English chronology.

The lower boundary is consonantal. If general umlaut precedes velar palatalization, PGmc [kūi]{.recon} ‘cow’ yields [*ċȳ*]{.pred} rather than expected *cȳ* 'cows', and PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected *lungen* 'lungs'. These over-palatalized forms place general umlaut after velar palatalization.

The upper boundary separates general umlaut from the narrower West Saxon process. If West Saxon palatal diphthongization precedes umlaut, PGmc [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected OE *ġift* 'gift', and [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ* 'sheath'. Together the two witness pairs place general umlaut after velar palatalization and before the West Saxon process.

## \CAPRRuleHeading{SC056. West Saxon palatal diphthongization}{OEWsPalatalDiphthongization} {#rule-OEWsPalatalDiphthongization}

```foma
define OEWsPalatalDiphthongization [
    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

West Saxon *gieldan* ‘pay’, *scield* ‘shield’, and *scieppan* ‘create’ show diphthongization after an already palatal consonant [@RingeTaylor2014, pp. 215--216, §6.5.1]. Their dialectal and phonological restriction separates this development from system-wide i-umlaut.

Hogg's *giefan* ‘give’ and *sceap* ‘sheep’ belong to the same palatal-consonant environment [@HoggPhonology1992, p. 112]. Fulk likewise assigns this diphthongization a place before front mutation and distinguishes the two processes [@Fulk2018, p. 74, §4.13].

The forms *ġift* ‘gift’ and *sċēaþ* ‘sheath’ fix the lower boundary. If West Saxon palatal diphthongization precedes general i-umlaut, PGmc [géftiz]{.recon} ‘gift’ yields [*ġieft*]{.pred} rather than expected *ġift*, and PGmc [skáiθiz]{.recon} ‘sheath’ yields [*sċǣþ*]{.pred} rather than expected *sċēaþ*. These witnesses place West Saxon palatal diphthongization after general umlaut; no tested lexical item supplies a later terminus ante quem.

The one-sided chronology reflects the difference in scale. General umlaut reorganizes the vowel system, whereas West Saxon palatal diphthongization affects a narrower dialectal class after palatal consonants. Its exact later placement remains undemonstrated by the present lexicon.

\newpage

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
demonstrates that velar palatalization preceded coalescence. Nothing in the
present lexicon supplies a terminus ante quem.

\newpage

# Back mutation

## Historical discussion

West Saxon *giefan* ‘give’ and *wefan* ‘weave’ stand against non-West-Saxon
*geofad* 'gave' and *weofan* 'weave'. Ringe and Taylor use this contrast to define the
dialectal profile of back mutation [@RingeTaylor2014, p. 319, §6.9.4].
Campbell's treatment of diphthongization before following back vowels includes
*heofon* ‘heaven’ [@Campbell1959, p. 86, §207], while Hogg draws the instructive
comparison with breaking [@HoggPhonology1992, p. 112]. Fulk accordingly separates back
mutation from the earlier umlautal changes [@Fulk2018, p. 69, §4.8].

## SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation}

```foma
define OEBackMutation [
    {*e} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger,
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
];
```

Three witness forms bracket the chronology. If back mutation precedes
[SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), forms such as
[gébaną]{.recon} ‘give’ produce *ġeofan* ‘give’; the
expected form is *ġiefan* ‘give’. [stélaną]{.recon} ‘steal’ likewise produces *steolan*
‘steal’; the expected form is *stelan* ‘steal’. At the other edge, delaying
back mutation until after
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) makes
[wébaną]{.recon} ‘weave’ yield *weofan* ‘weave’; the expected form is *wefan* ‘weave’.
Thus back mutation follows secondary nasalization but precedes the weak-tail
reductions.

\newpage

# West Saxon palatal umlaut

## Historical discussion

The reflexes *miht* ‘might’ and *niht* ‘night’ place West Saxon palatal umlaut
after the principal umlautal developments. Campbell and Ringe and Taylor
describe the forms themselves; Fulk supplies the broader chronology of
palatal-vowel change [@Campbell1959, pp. 107--108, §§248--251;
@RingeTaylor2014, pp. 215--251, §§6.5.1, 6.6.1--6.6.4; @Fulk2018, pp. 65, 75,
§§4.7, 4.13].

## \CAPRRuleHeading{SC060. West Saxon palatal umlaut before \emph{*h}-clusters}{OEWsPalatalUmlaut} {#rule-OEWsPalatalUmlaut}

```foma
define OEWsPalatalUmlaut [
    {*eo} -> {*i} || _ OEHCluster .#.,
    {*io} -> {*i} || _ OEHCluster .#.,
    {*ie} -> {*i} || _ OEHCluster .#.,
    {*eo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*io} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ie} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*éo} -> {*i} || _ OEHCluster .#.,
    {*ío} -> {*i} || _ OEHCluster .#.,
    {*íe} -> {*i} || _ OEHCluster .#.,
    {*éo} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*ío} -> {*i} || _ OEHCluster EnglishStarFrontVowel,
    {*íe} -> {*i} || _ OEHCluster EnglishStarFrontVowel
];
```

The change to \emph{*i} before \emph{*h}-clusters can be ordered only on its
earlier side. If palatal umlaut precedes
[SC055 OEIUmlaut](#rule-OEIUmlaut),
the forms behind *miht* ‘might’ and *niht* ‘night’ remain at the overdeveloped
stage [*mieht*]{.pred} and [*nieht*]{.pred} rather than expected OE *miht* and *niht*.
Consequently, i-umlaut precedes palatal umlaut. Reordering the latter against
any tested later change leaves both witness forms unchanged.

\newpage

# Weak-tail nasal loss

## Historical discussion

The pathway from [dōną]{.recon} ‘do’ to *dōn* ‘do’ supplies the sole lexical thread
through this reduction. Campbell, Hogg, and Fulk place such weak-tail losses
among apocope and related late reductions [@Campbell1959, pp. 144--145,
§§345--349; @HoggPhonology1992, p. 121; @Fulk2018, p. 91, §5.6]. The witness,
however, ties the change to a much older development. Its immediate neighbors
remain untested.

## \CAPRRuleHeading{SC061. Reduction of final nasal weak-tail endings}{OEWeakTailNasalLoss} {#rule-OEWeakTailNasalLoss}

```foma
define OEWeakTailNasalLoss [
    {*n} {*ą} -> {*n} || _ .#.,
    {*m} {*ą} -> {*m} || _ .#.
];
```

Final weak-tail \emph{*-ną} and \emph{*-mą} accordingly yield plain
\emph{*-n} and \emph{*-m}.

Only *dōn* ‘do’ constrains the relative order. Placing this loss before
the older n-stem loss makes the derivation record no output instead of expected
OE *dōn* ‘do’. The older loss must therefore precede weak-tail nasal loss.
Nothing in the current lexicon distinguishes among its possible later
positions, and one witness cannot establish a wider historical development.

\newpage

# High-vowel apocope

## Historical discussion

Final high vowels must survive long enough to condition umlaut before apocope
removes them after heavy syllables and in the relevant trisyllabic patterns.
Campbell, Hogg, Ringe and Taylor, and Fulk agree on this Old English
development, though they differ over the extent of the surrounding syncope
[@Campbell1959, pp. 144--145, §§345--349; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 284--303, §§6.8.1, 6.8.4; @Fulk2018, p. 91, §5.6].

## \CAPRRuleHeading{SC063. High-vowel apocope after heavy syllables and in trisyllables}{OEHighVowelApocope} {#rule-OEHighVowelApocope}

```foma
define OEHighVowelApocope [
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
    {*u} -> 0 || {*x} _ .#.,
    {*ų} -> 0 || {*x} _ .#.,
    {*i} -> 0 || {*x} _ .#.
];
```

Final \emph{*i}, \emph{*u}, and \emph{*ų} cannot disappear before completing
their umlautal work. Applied before
[SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [kūi]{.recon} ‘cow’ yields [*cū*]{.pred} rather than
expected OE *cȳ* ‘cow’, and PGmc [brūdiz]{.recon} ‘bride’ yields [*brūd*]{.pred} rather than
expected OE *brȳd* ‘bride’. Conversely, if apocope waits until after
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
PGmc [fúrxtīnaz]{.recon} ‘fright’ yields [*fyrht*]{.pred} rather than expected OE *fyrhte*
‘fright’. The three witnesses establish the sequence i-umlaut, high-vowel
apocope, unstressed long-vowel shortening.

\newpage

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

## \CAPRRuleHeading{SC065. Medial syncope before dentals after heavy syllables}{OEMedialSyncope} {#rule-OEMedialSyncope}

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

\newpage

# Late syncope and degemination

## Historical discussion

Vowel loss creates the clusters upon which later assimilation and degemination
operate. Hogg and Ringe and Taylor describe this dependence, while Brunner's
*netle* 'nettle' beside later *netele* 'nettle' supplies a concrete lexical type
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--296, §§6.7.3--6.8.2;
@SieversBrunner1965, pp. 144--145, §§158--159]. Fulk places this syncope after
i-umlaut [@Fulk2018, p. 91, §5.6].

The three relations are not equally secure. Lexical evidence orders syncope
and degemination; the intervening dental assimilation has no independent
ordering witness.

## \CAPRRuleHeading{SC066. L-adjacent syncope in medial syllables}{OELAdjacentSyncope} {#rule-OELAdjacentSyncope}

```foma
define OELAdjacentSyncope [
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarDiphthong OEAnyConsonant+ _ {*l}
];
```

The loss of medial \emph{*i} before \emph{*l} is late enough to preserve
earlier umlaut, as *netle* ‘nettle’ and *spinl* ‘spindle’ demonstrate.

Placed before i-umlaut, PGmc [nátilōn]{.recon} ‘nettle’ yields [*nætle*]{.pred} rather than
expected OE *netle* ‘nettle’, and PGmc [spénnilō]{.recon} ‘spindle’ yields [*spenl*]{.pred} rather
than expected *spinl* ‘spindle’. Placed after preconsonantal degemination, PGmc
[spénnilō]{.recon} yields [*spinnl*]{.pred} rather than expected *spinl*. The witnesses
therefore establish the sequence i-umlaut, l-adjacent syncope, preconsonantal
degemination. The first relation separates two historical phases; the second is
a direct feeding relation, since syncope creates the cluster that degemination
simplifies.

## \CAPRRuleHeading{SC067. Dental assimilation in newly formed clusters}{OEDentalAssimilation} {#rule-OEDentalAssimilation}

```foma
define OEDentalAssimilation [
    {*θ} -> 0 || {*t} _
];
```

Loss of \emph{*θ} after \emph{*t} resolves a dental cluster produced by syncope
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].
No witness distinguishes its position: moving dental assimilation across every
tested neighbor leaves the outputs unchanged. I nevertheless place it after
syncope, which supplies its input, and before the more general cluster
simplification described in the handbooks. This order is phonologically
motivated, not established by a lexical contrast.

## \CAPRRuleHeading{SC068. Preconsonantal degemination before sonorants}{OEPreconsonantalDegemination} {#rule-OEPreconsonantalDegemination}

```foma
define OEPreconsonantalDegemination OEPreconsonantalDegemTT .o. OEPreconsonantalDegemNN;
```

Preconsonantal \emph{*tt} and \emph{*nn} simplify only after syncope has
created a following sonorant cluster, as in *spinl* ‘spindle’
[@RingeTaylor2014, pp. 279--296, §§6.7.5, 6.8.2].

Placed before l-adjacent syncope, PGmc [spénnilō]{.recon} ‘spindle’ yields [*spinnl*]{.pred} rather
than expected OE *spinl* ‘spindle’. Syncope must therefore create the cluster
before degemination simplifies it. Reordering degemination against any tested
later change leaves the witness unchanged, so no terminus ante quem is known.

\newpage

# Early o-shortening

## Historical discussion

After the principal palatal and umlautal changes, unstressed vowels undergo
shortening, fronting, merger, and sometimes complete loss. Campbell describes
the early shortening of unaccented long vowels, while Hogg, Ringe and Taylor,
and Fulk relate it to apocope, syncope, and the later reductions
[@Campbell1959, p. 148, §355; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7].

Early o-shortening has only a distant earlier boundary. The rules that follow,
especially [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening),
have more closely defined relations.

## \CAPRRuleHeading{SC069. Early shortening of unstressed \emph{*ō} before nasals}{OEEarlyOShortening} {#rule-OEEarlyOShortening}

```foma
define OEEarlyOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ EnglishStarNasal
];
```

The rule shortens unstressed long \emph{*ō} before a following nasal. Because this shortening happens early, the resulting \emph{*a} can still participate in the later fronting and merger that shape many weak final syllables.

Moving the rule before
[SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss), PGmc [nḗdrōn]{.recon} ‘adder’ yields
[*nǣdran*]{.pred} rather than expected OE *nǣdre* ‘adder’, PGmc [érθōn]{.recon} ‘earth’ yields
[*eorþan*]{.pred} rather than expected *eorþe* ‘earth’, and PGmc [fláskōn]{.recon} ‘flask’ yields
[*flascan*]{.pred} rather than expected *flasce* ‘flask’. The same earlier shift also
disrupts forms such as *heorte* ‘heart’ and *līne* ‘line’. This broad set of
failures requires [SC069 OEEarlyOShortening](#rule-OEEarlyOShortening) to follow
[SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss).

If the rule is moved later within the tested sequence, no output differs from the
expected one. The lexical evidence therefore does not
identify a corresponding later constraint. The sources place early
\emph{*ō}-shortening before the later weak-tail changes without fixing a closer
local order.

\newpage

# Early unstressed fronting and later o-shortening

## Historical discussion

Campbell distinguishes the shortening of unaccented long vowels, while Hogg,
Ringe and Taylor, and Fulk place fronting and shortening within a later history
of syncope and final-vowel adjustment [@Campbell1959, p. 148, §355;
@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--96, §§5.6--5.7]. Earlier unstressed fronting precedes later
o-shortening.

[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) has both an
earlier and a later lexical breakpoint.
[SC071 OELateOShortening](#rule-OELateOShortening) confirms their reciprocal
order, but no lexical evidence fixes its later boundary.

## \CAPRRuleHeading{SC070. Early fronting of unstressed \emph{*a}}{OEUnstressedFrontingEarly} {#rule-OEUnstressedFrontingEarly}

```foma
define OEUnstressedFrontingEarly OEUnstressedAFronting;
```

The rule fronts unstressed \emph{*a} to \emph{*æ} after the earlier shortening
has created a frontable vowel but before the later shortening of unstressed
\emph{*ō}. It produces endings such as OE \emph{-en} in *lungen* ‘lungs’.

If the rule is moved before [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization), PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lunġen*]{.pred} rather than expected OE *lungen* ‘lungs’. If the rule is delayed until after [SC071 OELateOShortening](#rule-OELateOShortening), PGmc [búrōθi]{.recon} ‘bears’ yields [*boreþ*]{.pred} rather than expected OE *boraþ* ‘bears’, and PGmc [mḗnōθz]{.recon} ‘month’ yields [*mōneþ*]{.pred} rather than expected *mōnaþ* ‘month’. The witness forms require [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) to follow [SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and precede [SC071 OELateOShortening](#rule-OELateOShortening).

The relation to [SC071 OELateOShortening](#rule-OELateOShortening) is local.
The earlier boundary at
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) places fronting after
the older palatal developments.

## SC071. Later shortening of unstressed \emph{*ō} (`OELateOShortening`) {#rule-OELateOShortening}

The following rule handles the later shortening stage.

```foma
define OELateOShortening [
    {*ō} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

The rule shortens the remaining unstressed long \emph{*ō} after fronting,
producing the later “stable a” endings in OE *boraþ* ‘bears’ and *liornaþ*
‘learns’.

Moving the rule before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) makes PGmc [búrōθi]{.recon} ‘bears’ yield [*boreþ*]{.pred} rather than expected OE *boraþ* 'bears', and PGmc [líznōθi]{.recon} ‘learns’ yield [*liorneþ*]{.pred} rather than expected *liornaþ* 'learns'. The contrast requires [SC071 OELateOShortening](#rule-OELateOShortening) to follow [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly). Moving it later within the tested range creates no equally sharp failure.

\newpage

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

## \CAPRRuleHeading{SC072. Shortening of unstressed long vowels}{OEUnstressedLongVowelShortening} {#rule-OEUnstressedLongVowelShortening}

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

\newpage

# Medial unstressed-i lowering

## Historical discussion

Hogg and Ringe and Taylor treat the late weakening and merger of unstressed
vowels as a continuing history [@HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 327--332, §§6.9.5--6.9.6].
[SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) lowers
medial unstressed \emph{i}; [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering)
preserves \emph{i} before \emph{*ng} in words of the *sċilling* ‘shilling’
type.

General lowering precedes the restricted restoration before \emph{*ng}. The
evidence is narrower than that for
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening)
and [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

## \CAPRRuleHeading{SC074. First medial unstressed-\emph{i} lowering}{OEMedUnstressedILowering1} {#rule-OEMedUnstressedILowering1}

```foma
define OEMedUnstressedILowering1 [
    {*i} -> {*e} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _
];
```

The rule lowers medial unstressed \emph{*i} to \emph{*e} after a preceding
vocalic syllable. The resulting \emph{e}-outcome is reversed before
\emph{*ng}.

If the rule is moved before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc [fúrxtīnaz]{.recon} ‘fright’ yields [*fyrhti*]{.pred} rather than expected OE *fyrhte* ‘fright’. If it is delayed until after [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering), PGmc [skíllingaz]{.recon} ‘shilling’ yields [*sċilleng*]{.pred} rather than expected *sċilling* ‘shilling’. The derivations require [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) to follow [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) and precede [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering).

The evidence is narrow on each side. The rule follows unstressed long-vowel
shortening and precedes the more specific \emph{*ng} preservation.

## \CAPRRuleHeading{SC075. Preservation of medial unstressed \emph{*i} before \emph{*ng}}{OEMedUnstressedILowering} {#rule-OEMedUnstressedILowering}

The following rule reverses the lowering before \emph{*ng}.

```foma
define OEMedUnstressedILowering [
    {*e} -> {*i} || _ {*n} {*g}
];
```

The rule restores \emph{*i} before \emph{*ng}, preventing the broader lowering from producing the wrong medial vowel in forms such as *sċilling* ‘shilling’.

Moving the rule before [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1) makes PGmc [skíllingaz]{.recon} ‘shilling’ yield [*sċilleng*]{.pred} rather than expected OE *sċilling* 'shilling'. On this evidence, I take [SC075 OEMedUnstressedILowering](#rule-OEMedUnstressedILowering) to follow [SC074 OEMedUnstressedILowering1](#rule-OEMedUnstressedILowering1). Moving it later within the tested range creates no equally sharp failure.

\newpage

# Prefix i-reduction

## Historical discussion

Late weak-tail reduction affects unstressed prefixes as well as inflectional
endings and medial vowels. Fulk's discussion of prefix vowels accounts for OE
\emph{*be-} and \emph{*ne-} [@Fulk2018, p. 97, §5.7]. Hogg and Ringe and
Taylor place such weakening within the broader late history of unstressed
vowels [@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 298--332,
§§6.8.3--6.9.6].

The tested forms do not determine the rule's position relative to a neighboring
change.

## \CAPRRuleHeading{SC076. Reduction of prefixal \emph{*i} in unstressed position}{OEPrefixIReduction} {#rule-OEPrefixIReduction}

```foma
define OEPrefixIReduction [
    {*i} -> {*ĕ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

The rule reduces unstressed prefixal \emph{*i} to a weaker vowel in the
\emph{bi-} and \emph{ni-} type prefixes before a consonant plus a following
vowel. The development accounts for later prefix spellings such as OE
\emph{*be-} and \emph{*ne-}.

If the rule is moved earlier or later within the tested sequence, no output differs from the expected one. The lexical evidence therefore does not place [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) before or after any specific neighboring change.

The handbooks attest late prefix-vowel weakening, but the precise placement
remains approximate. No lexical failure fixes it.

\newpage

# Weak-tail reduction

## Historical discussion

Campbell, Hogg, Ringe and Taylor, and Fulk describe a late history in which
apocope, shortening, contraction, and further weak-tail reductions reshape
final syllables [@Campbell1959, p. 148, §355; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 298--314, §§6.8.3--6.9.3;
@Fulk2018, pp. 90--91, §5.6]. Lexical failures place the remaining weak-tail
reduction after unstressed fronting and before contraction.

## \CAPRRuleHeading{SC078. Reduction of remaining weak-tail vowels}{OEWeakTailReduction} {#rule-OEWeakTailReduction}

```foma
define OEWeakTailReduction OEWeakTailReduction1;
```

The rule reduces the remaining weak-tail vowels, preventing a broad class of
\emph{-en} and extra-vowel outcomes.

I place the change after [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly)
and before [SC086 OEContraction](#rule-OEContraction). Moving it before
[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly), PGmc
[bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE *bacan* ‘bake’, and PGmc
[bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred} rather than expected *bindan* ‘bind’, alongside
a much wider set of comparable \emph{-en} failures. If the rule is delayed until
after [SC086 OEContraction](#rule-OEContraction), PGmc [fléuxaną]{.recon} ‘flee’ yields
[*flēoan*]{.pred} rather than expected OE *flēon* ‘flee’, and PGmc [sláxaną]{.recon} ‘slay’
yields [*sleaan*]{.pred} rather than expected *slēan* ‘slay’.

The earlier boundary spans a wide interval and does not establish a close
neighboring relation. The later boundary is narrower:
[SC078 OEWeakTailReduction](#rule-OEWeakTailReduction) precedes
[SC086 OEContraction](#rule-OEContraction).

\newpage

# Final-j loss and final geminate simplification

## Historical discussion

After [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) removes \emph{*j} in
heavy environments, forms such as *lungen* ‘lungs’ acquire a final geminate.
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification)
then removes the second nasal.

[SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) has a broad earlier boundary
at [SC055 OEIUmlaut](#rule-OEIUmlaut).
[SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) is
fixed only by the final \emph{nn} outcome in the following derivation.

## SC079. Loss of \emph{*j} after heavy syllables (`OEJLossAfterHeavy`) {#rule-OEJLossAfterHeavy}

```foma
define OEJLossAfterHeavy [
    {*j} -> 0 || (EnglishStarLongVowel | EnglishStarDiphthong) [EnglishStarConsonantNoR | EnglishPalatalConsonant] _,
    {*j} -> 0 || EnglishStarShortVowel [EnglishStarConsonant | EnglishPalatalConsonant] [EnglishStarConsonantNoR | EnglishPalatalConsonant] _
];
```

The rule removes \emph{*j} after the relevant heavy-syllable configurations,
after the earlier umlaut-sensitive vocalism has developed.
The affected glide is \emph{*j}.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [galáubijaną]{.recon} ‘believe’ yields [*ġelēafan*]{.pred} rather than expected OE *ġelīefan* ‘believe’, PGmc [báugijaną]{.recon} ‘bow’ yields [*bēaġan*]{.pred} rather than expected *bīeġan* ‘bow’, and PGmc [fúlgijaną]{.recon} ‘follow’ yields [*fulġan*]{.pred} rather than expected *fylġan* ‘follow’. If it is delayed until after [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification), PGmc [lúnganjō]{.recon} ‘lungs’ yields [*lungenn*]{.pred} rather than expected OE *lungen* ‘lungs’. I accordingly take [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification).

The earlier boundary is broad, but the relation to final geminate
simplification is local.

## \CAPRRuleHeading{SC080. Simplification of final geminates}{OEFinalGeminateSimplification} {#rule-OEFinalGeminateSimplification}

The following rule handles the final simplification directly.

```foma
define OEFinalGeminateSimplification [
    {*n} -> 0 || {*n} _ .#.
];
```

The rule removes the extra final nasal in forms where the preceding derivation has already created a final geminate.

Moving the rule before [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy) makes PGmc [lúnganjō]{.recon} ‘lungs’ yield [*lungenn*]{.pred} rather than expected OE *lungen* 'lungs'. These failures require [SC080 OEFinalGeminateSimplification](#rule-OEFinalGeminateSimplification) to follow [SC079 OEJLossAfterHeavy](#rule-OEJLossAfterHeavy). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.

\newpage

# J-strengthening, vocalization, and ei-contraction

## Historical discussion

[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
preserves a consonantal outcome after front diphthongs.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) then
vocalizes the remaining intervocalic \emph{*j}, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) removes the
resulting \emph{ei}-like sequence in weak verbal endings.

The output of each rule conditions the next.
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) has local
lexical evidence on both sides;
[SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong)
has a distant earlier boundary, and
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) has no
tested later boundary.

## \CAPRRuleHeading{SC081. Strengthening of \emph{*j} after front diphthongs}{OEJStrengtheningAfterFrontDiphthong} {#rule-OEJStrengtheningAfterFrontDiphthong}

```foma
define OEJStrengtheningAfterFrontDiphthong [
    {*j} -> {*ʒ} || [{*ēa}|{*ḗa}|{*íe}|{*īe}|{*éa}] _ EnglishStarVocalic
];
```

After the relevant front diphthongs, \emph{*j} first strengthened to a consonantal outcome; otherwise it would have vocalized too early.

If the rule is moved before [SC055 OEIUmlaut](#rule-OEIUmlaut), PGmc [stráwjaną]{.recon} ‘strew’ yields [*strēaġan*]{.pred} rather than expected OE *strīeġan* ‘strew’. If it is delayed until after [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization), the same PGmc form yields [*strīeian*]{.pred} rather than *strīeġan*. The order test requires [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) to follow [SC055 OEIUmlaut](#rule-OEIUmlaut) and precede [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

The earlier constraint reaches back to [SC055 OEIUmlaut](#rule-OEIUmlaut) and
therefore defines a wide interval. The *strīeġan* 'strew' derivation fixes the local
relation to [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization).

## \CAPRRuleHeading{SC082. Intervocalic vocalization of \emph{*j}}{OEIntervocalicJVocalization} {#rule-OEIntervocalicJVocalization}

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule vocalizes intervocalic \emph{*j} to \emph{*i}, creating the
\emph{ei}-like sequence later removed by
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) in many weak
verb forms.

Moving the rule before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) makes PGmc [stráwjaną]{.recon} ‘strew’ yield [*strīeian*]{.pred} rather than expected OE *strīeġan* ‘strew’. Delaying it until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* ‘bore’, PGmc [xándlōjaną]{.recon} ‘handle’ yield [*handleian*]{.pred} rather than expected *handlian* ‘handle’, and PGmc [mákōjaną]{.recon} ‘make’ yield [*maceian*]{.pred} rather than expected *macian* ‘make’. The witness forms require [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) to follow [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) and precede [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is
therefore ordered between strengthening and contraction.

## SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

The final rule removes the extra unstressed \emph{e} before \emph{i}.

```foma
define OEUnstressedEIContraction [
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
];
```

The rule contracts the unstressed \emph{ei}-like sequence that the preceding vocalization would otherwise leave behind in forms such as *borian* ‘bore’ and *liccian* ‘lick’.

Moving the rule before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* 'bore', PGmc [líznōjaną]{.recon} ‘learn’ yield [*liorneian*]{.pred} rather than expected *liornian* 'learn', and PGmc [líkkōjaną]{.recon} ‘lick’ yield [*licceian*]{.pred} rather than expected *liccian* 'lick'. The contrast requires [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) to follow [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.

\newpage

# H-loss and contraction

## Historical discussion

When [SC085 OEHLoss](#rule-OEHLoss) removes intervocalic \emph{*h}, it creates
hiatus. [SC086 OEContraction](#rule-OEContraction) immediately resolves the
resulting vowel sequence.

Ringe and Taylor describe this late sequence of \emph{h}-loss and contraction
[@RingeTaylor2014, pp. 305--314, §§6.9.1--6.9.3]. Fulk places the contracted
verbs in a broader Germanic context [@Fulk2018, p. 270, §12.21], and Luick
describes the corresponding West Germanic contractions [@Luick1914, p. 165].

## SC085. Loss of intervocalic \emph{*h} (`OEHLoss`) {#rule-OEHLoss}

```foma
define OEHLoss [
    {*x} -> 0 || EnglishStarVocalic _ EnglishStarVocalic
];
```

The rule removes intervocalic \emph{*h}, creating the hiatus that later contraction must resolve.

If the rule is moved before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), PGmc [táixōn]{.recon} ‘toe’ yields [*tāæ*]{.pred} rather than expected OE *tā* ‘toe’. If it is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc [fléuxaną]{.recon} ‘flee’ yields [*flēoan*]{.pred} rather than expected OE *flēon* ‘flee’, PGmc [sláxaną]{.recon} ‘slay’ yields [*sleaan*]{.pred} rather than expected *slēan* ‘slay’, PGmc [téxun]{.recon} ‘draw’ yields [*teoon*]{.pred} rather than expected *tēon* ‘draw’, and PGmc [táixōn]{.recon} yields [*tāe*]{.pred} rather than expected *tā*. These outputs require [SC085 OEHLoss](#rule-OEHLoss) to follow [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger) and precede [SC086 OEContraction](#rule-OEContraction).

The earlier boundary rests on one witness; the four later witnesses establish
the immediate relation to contraction.

## SC086. Contraction of the resulting hiatus (`OEContraction`) {#rule-OEContraction}

The following rule contracts the hiatus left by [SC085 OEHLoss](#rule-OEHLoss).

```foma
define OEContraction [
    {*a} {*a} -> {*ā},
    {*e} {*e} -> {*ē},
    {*i} {*i} -> {*ī},
    {*o} {*o} -> {*ō},
    {*u} {*u} -> {*ū},
    {*ea} {*a} -> {*ēa},
    {*ēa} {*a} -> {*ēa},
    {*eo} {*a} -> {*ēo},
    {*ēo} {*a} -> {*ēo},
    {*eo} {*o} -> {*ēo},
    {*ēo} {*o} -> {*ēo},
    {*éo} {*o} -> {*ḗo},
    {*ḗo} {*o} -> {*ḗo},
    {*ā} {*a} -> {*ā},
    {*ā} {*e} -> {*ā},
    {*ē} {*a} -> {*ē},
    {*ē} {*e} -> {*ē},
    {*ḗ} {*a} -> {*ḗ},
    {*ḗ} {*e} -> {*ḗ},
    {*ī} {*a} -> {*ī},
    {*ī} {*e} -> {*ī},
    {*ḯ} {*a} -> {*ḯ},
    {*ḯ} {*e} -> {*ḯ},
    {*ō} {*a} -> {*ō},
    {*ō} {*e} -> {*ō},
    {*ū} {*a} -> {*ū},
    {*ū} {*e} -> {*ū}
];
```

The rule contracts the vowel sequences created after \emph{h}-loss, producing
*flēon* ‘flee’, *slēan* ‘slay’, and *tēon* ‘draw’.

Moving contraction before [SC085 OEHLoss](#rule-OEHLoss) makes PGmc [fléuxaną]{.recon} ‘flee’ yield [*flēoan*]{.pred} rather than expected OE *flēon* 'flee', PGmc [sláxaną]{.recon} ‘slay’ yield [*sleaan*]{.pred} rather than expected *slēan* 'slay', PGmc [téxun]{.recon} ‘draw’ yield [*teoon*]{.pred} rather than expected *tēon* 'draw', and PGmc [táixōn]{.recon} ‘toe’ yield [*tāe*]{.pred} rather than expected *tā* 'toe'. The derivations require [SC086 OEContraction](#rule-OEContraction) to follow [SC085 OEHLoss](#rule-OEHLoss). Moving it later within the tested range before [SC087 OERMetathesis](#rule-OERMetathesis) creates no new failure.
The more distant [SC078 OEWeakTailReduction](#rule-OEWeakTailReduction)
relation establishes only that weak-tail reduction precedes contraction.

\newpage

# R-metathesis

## Historical discussion

Sievers-Brunner describes r-metathesis in forms such as *berstan* ‘burst’,
*forst* ‘frost’, and *cærse* ‘cress’
[@SieversBrunner1965, p. 159, §179]. Luick likewise treats it as a later
rearrangement whose interaction with breaking remains variable
[@Luick1914, p. 201].

The evidence establishes that breaking precedes metathesis. It does not
establish an ordering relation between
[SC086 OEContraction](#rule-OEContraction) and
[SC087 OERMetathesis](#rule-OERMetathesis).

## \CAPRRuleHeading{SC087. Metathesis of \emph{*r} with a following short vowel}{OERMetathesis} {#rule-OERMetathesis}

```foma
define OERMetathesis [
    {*r} {*e} -> {*e} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*u} -> {*u} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*i} -> {*i} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*o} -> {*o} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*a} -> {*a} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*é} -> {*é} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*ó} -> {*ó} {*r} || EnglishStarConsonant _ {*s} {*t},
    {*r} {*á} -> {*á} {*r} || EnglishStarConsonant _ {*s} {*t}
];
```

The rule moves \emph{*r} across a following short vowel in the relevant late clusters, producing forms such as *berstan* ‘burst’ where an earlier order would still show a broken vowel sequence.

Moving the rule before [SC044 OEBreaking](#rule-OEBreaking) makes PGmc [bréstaną]{.recon} ‘burst’ yield [*beorstan*]{.pred} rather than expected OE *berstan* ‘burst’. On this evidence, I take [SC087 OERMetathesis](#rule-OERMetathesis) to follow [SC044 OEBreaking](#rule-OEBreaking). Moving it later within the tested sequence alters no output.

The lexical evidence fixes the earlier relation but does not identify a corresponding
later constraint. The sources treat r-metathesis as a late rearrangement after
breaking without placing it immediately beside contraction.

\newpage

# References

::: {#refs}
:::
