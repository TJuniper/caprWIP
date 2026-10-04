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

Chapter 1 contains one reader-facing sound-change section: the Proto-Germanic
loss of a nasal before \emph{*x} (`SC103 PGmcNasalLossBeforeX`), with
compensatory lengthening and nasalization of the preceding vowel. Its results
are shared by every daughter language, Gothic included, so the change belongs
to Proto-Germanic itself and precedes every Northwest Germanic and West
Germanic development treated in the chapters that follow
[@Campbell1959, p. 44, §119; @Fulk2018, p. 55, §4.1;
@Ringe2017, pp. 149--150, §3.2.7].

Another historically Proto-Germanic rule, the positional allophony of
Proto-Germanic \emph{*b} (`SC049 PGmcBAllophony`), executes late in the
computational cascade because the alternation interacts with environments
shaped by intermediate rule applications; its section therefore appears in
Chapter 4, where the divergence between cascade placement and historical
stage is noted explicitly.

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

# Proto-Germanic loss of a nasal before \emph{*x}

## Historical discussion

The oldest change treated in this book is common to the whole family. In the
group [-nx-]{.recon} the nasal consonant was lost, the preceding vowel was
lengthened in compensation, and that lengthened vowel was nasalized. Its results
are shared by every daughter language: Gothic *þeihan* ‘thrive’, *brāhta* ‘brought’, *þūhta* ‘seemed’ stand
beside Old High German *dīhan* ‘thrive’, *brāhta*, *fūht* ‘damp’ and Old English *þēon* ‘thrive’,
*brōhte* ‘brought’, *þūhte* ‘seemed’, *fūht* ‘damp’
[@Campbell1959, p. 44, §119; @Fulk2018, p. 55, §4.1;
@Ringe2017, pp. 149--150, §3.2.7]. Because no daughter keeps the nasal, the
change belongs to Proto-Germanic itself, and it precedes every Northwest
Germanic, West Germanic, North Sea Germanic and Anglo-Frisian development
described in the chapters that follow.

Only [a]{.recon}, [i]{.recon} and [u]{.recon} occur in this position. Germanic
had already raised [e]{.recon} to [i]{.recon} and [o]{.recon} to [u]{.recon}
before a nasal followed by a consonant, so the mid vowels are absent from the
input [@Fulk2018, p. 55, §4.1].

The vowel that the change creates is long and nasalized, and it is not yet
rounded. Fulk emphasizes that the lengthened vowels remained nasalized for a
considerable time, well past the close of the Northwest Germanic period, since
the nasalized low vowel produced in this way went on to develop to *ō* in
Anglo-Frisian and did not fall together with the Old English *ā* that came from
[ai]{.recon} [@Fulk2018, p. 55, §4.1]. The comparative material makes the same
point directly: Gothic, Old Norse, Old High German and Old Saxon all reflect the
Proto-Germanic nasalized low vowel as unrounded *ā*, and only Old English and
Old Frisian show *ō* [@Campbell1959, p. 44, §119; @Fulk2018, p. 72, §4.11].
Ringe describes Proto-Germanic \emph{*hanhaną} as \emph{*[xą̄xaną]} and observes
that its low vowel was rounded, along with the other nasalized low vowels, in
the northernmost West Germanic dialects [@Ringe2017, pp. 149--150, §3.2.7].
That rounding is a separate and much later change, and it is treated in the
chapter on the rounding of the long nasalized low vowel.

## \CAPRRuleHeading{SC103. Proto-Germanic nasal loss before \*x}{PGmcNasalLossBeforeX} {#rule-PGmcNasalLossBeforeX}

```foma
define PGmcNasalLossBeforeX Ctx([
    {*a} -> {*ą̄} || _ EnglishStarNasal {*x},
    {*i} -> {*ī} || _ EnglishStarNasal {*x},
    {*u} -> {*ū} || _ EnglishStarNasal {*x},
    {*á} -> {*ą̄} || _ EnglishStarNasal {*x},
    {*í} -> {*ī} || _ EnglishStarNasal {*x},
    {*ú} -> {*ū} || _ EnglishStarNasal {*x}
] .o. [
    EnglishStarNasal -> 0 || _ {*x}
]);
```

The rule performs the three parts of the change together: it lengthens the
vowel, it marks the lengthened low vowel as nasalized, and it then removes the
conditioning nasal. The low vowel is written [ą̄]{.recon} and the high vowels are
written [ī]{.recon} and [ū]{.recon}, because the nasality of the high vowels has
no further consequence: they go on to develop exactly as the inherited long
[ī]{.recon} and [ū]{.recon} do [@Campbell1959, p. 47, §121]. The nasality of the
low vowel is carried forward because its later fate depends on it.

The corpus witnesses both branches of the rule. The high branch is
[fúnxstiz]{.recon} ‘fist’, which becomes [fū́xsti]{.recon} ‘fist’ and, after the loss of
[x]{.recon} before the cluster in
[SC028 PNWGmcPreconsonantalXLoss](#rule-PNWGmcPreconsonantalXLoss), gives Old
English *fȳst* ‘fist’. The long vowel of Old High German *fūst* ‘fist’, Dutch *vuist*
and German *Faust* shows that the word belongs here and to no later law
[@Kroonen2013, p. 160]. The rule also supplies the [xst]{.recon} cluster on
which the loss of [x]{.recon} before a consonant operates, so the two stand in a
feeding relation.

The low branch is [θánxtē]{.recon} ‘thought’, the preterite of the verb ‘to think’, whose
principal parts are reconstructed as [þankijaną]{.recon} ‘to think’, [þanhtē]{.recon} ‘thought’,
[þanhtaz]{.recon} ‘thought (past participle)’ with the nasal still standing before the fricative
[@Ringe2017, p. 281; @Ringe2017, p. 136]. Here the rule yields
[θą̄xtē]{.recon} ‘thought’, and the nasalized low vowel is later rounded by
[SC104 EAFNasalizedLowRounding](#rule-EAFNasalizedLowRounding) to give Old
English *þōhte* ‘thought’. This is the form the handbooks themselves cite for
the Anglo-Frisian rounding of the vowel produced here [@Fulk2018, p. 55, §4.1]. It does not enter the loss of [x]{.recon} before a
consonant, in which respect it differs from ‘fist’, so the fricative survives to
the surface and the word displays the vowel history alone.

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

The chapter opens with the root-noun nominative `*-z` loss (SC096), the
generalization of endingless nominatives through the athematic consonant
stems, complete before Proto-West Germanic: none of the West Germanic
daughters shows any ending in this class [@RingeTaylor2014, p. 118]. It is
the earliest of the three historically distinct final-`*z` developments; the
other two (SC020 and SC097) open Chapter 3.

The unstressed `*ai > *ē` development (SC014) represents one of the most
pervasive shared NW–West Germanic vowel shifts, turning unstressed endings
such as the dative singular and strong-adjective plural to longer vowels.
Ringe and Taylor treat this as one of the clearest post-PNWGmc shared
developments [@RingeTaylor2014, pp. 40--41]; Fulk groups it among the
North/West-Germanic shared innovations that distinguish the period from
Gothic [@Fulk2018, §5.2]. The corresponding stressed monophthongization
(SC004) belongs later in the cascade and is treated in Chapter 3.

The West Germanic consonant changes of this chapter — j-gemination (SC010),
early i-apocope (SC006), coronal-w assimilation (SC008), and related rules —
represent the most productive phonological territory for the CAPR derivations.
They feed a large proportion of the distinctive consonant clusters of Old
English. Handbooks vary in exactly how they group and name these changes
[@Campbell1959, §§ 404, 406; @HoggGrammar1992, §4.11].

Coronal assimilation also supplies the geminate in *fēower* 'four' and
*ēow* 'you', before inherited short-vowel-plus-geminate-glide reanalysis.
[SC031 OEWWSimplification](#rule-OEWWSimplification) now represents that
earlier development, not an unrestricted late deletion. The resulting
diphthong-plus-glide sequence is inherited by later English realization;
j-created and singleton paths remain distinct
[@RingeTaylor2014, pp. 41--42, 65--66; @Campbell1959, pp. 45--47].

The quoted definitions use `Ctx(...)` to carry selected sentence context
outside the segmental operation. It is computational transport, not a
reconstructed segment or an additional sound law. Lexical accent,
sentence stress and phonological-word finality are separate: the early
high-vowel-loss account requires a heavy syllable in a sentence-unstressed,
phonologically final word, not simply the absence of an acute. Ordinary
evaluation selects strong-final citation context; the explicit weak-final
selection for *ēow* is discussed with
[SC098 PWGmcUnstressedWordFinalIApocope](#rule-PWGmcUnstressedWordFinalIApocope)
[@RingeTaylor2014, pp. 55, 57--58].

The nasal spirant corridor (SC026–SC027), treated in Chapter 3 at its cascade
position, illustrates a type of change common
in historical grammars of the "Ingvaeonic" or "North Sea Germanic" area:
nasals disappear before voiceless fricatives, with compensatory vowel
lengthening [@Campbell1959, §§ 462--463; @HoggGrammar1992, p. 56, §3.14 (held 2011 reissue)]. The CAPR model
splits this into two ordered steps to make the vowel effect computationally
tractable; the book prose explains that split against the handbook tradition,
which typically presents the change as a single process.

Chapters in this part of the book follow the executable cascade order, which
models the reconstructed chronology itself. Several rules that carry `PWGmc`
labels — final bare-`*a` loss (SC041), surviving bimoric `*ō` unrounding
(SC042), and Sievers-law syncope (SC050) — execute later in the cascade and
are therefore presented in Chapter 4, where their individual sections discuss
their historical stage labels. Conversely, one rule with a West Saxon label,
the palatal-glide rule (SC016), is an orthographic rule of the written surface:
it executes after the Old English orthography stage and is presented in
Chapter 5.

One historically Proto-Germanic change, Gm-simplification
(`SC002 PGmcGmSimplification`), precedes everything in this chapter as a
support stage of the cascade. It is documented in the book-entry plan and
its literature dossier confirms the source base is narrow (two lexical
families: [draugma-]{.recon .iv lang=pgmc sort=draugma} 'dream' and
[taugma-]{.recon .iv lang=pgmc sort=taugma} 'team'; [@Kroonen2013, pp. 101, 511]).
A reader-facing section for SC002 awaits a stronger explanatory source base
and is not yet assembled in the reader-facing sequence.

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

Most CAPR rules in this chapter carry names beginning with `NWGmc` or `PWGmc`;
the reformulated inherited-glide rule retains its older `OE` identifier.
These names are stable internal identifiers. A name beginning with `NWGmc` does
not guarantee that the change is exclusive to Northwest Germanic, and a name
beginning with `PWGmc` does not guarantee that it is absent from North Germanic.
The historical analysis in each sound-change section takes priority over the
name prefix.

# Root-noun nominative \emph{*-z} loss

## Historical discussion

The athematic consonant stems — the "root nouns" of the handbooks — attached the nominative-singular marker directly to a consonant-final root, and the Proto-Germanic outcome of that collision is genuinely uncertain. Ringe gives the consonant-stem nominative ending as zero, \emph{*-z}, or possibly \emph{*-s}, and states plainly that the distribution is unrecoverable for monosyllabic stems [@Ringe2017, p. 306, §4.3.4]. His own paradigm tables carry the uncertainty into print: the nominative of 'foot' appears as "fōts? (fōs?)", while 'mouse' is plain \emph{*mūs}, its expected extra sibilant already absorbed by degemination [@Ringe2017, pp. 149, 313]. Ringe and Taylor repeat the same three-way agnosticism — the root-noun nominative "either ended in \emph{*-s} or \emph{*-z}, or was endingless" [@RingeTaylor2014, p. 28, §2.3.1].

The dictionary traditions encode this situation in different notations, and the differences are conventions of citation rather than competing claims of fact. Orel prints morphologically explicit nominatives with final \emph{-z} across the whole class: \emph{*bōkz} 'book', \emph{*ǥansz} 'goose', \emph{*lūsz} 'louse' [@Orel2003, pp. 52, 126, 252]. Kroonen cites the same words as bare stems or endingless forms, \emph{*bōk-} and \emph{*gans-} [@Kroonen2013, pp. 71--72, 168--169], and Kluge/Seebold print a third variant with voiceless \emph{-s}, as in \emph{*bōks} 'Buch' [@KlugeSeebold2011, p. 158]. Bammesberger shows why the marker is nonetheless real: for voiced-final stems the overt nominative \emph{*-z} is positively reconstructible — \emph{*burgz} (Gothic \emph{baúrgs}), \emph{*frijōndz} (Gothic \emph{frijonds}) — even though \emph{*fōt-z} is "phonotaktisch kaum denkbar", and in West Germanic the ending simply "fiel es ab" [@Bammesberger1990, pp. 190--192, §8.2.3.1]. CAPR retains Orel's morphologically explicit forms as its inputs precisely because they record the inflectional marker whose fate this rule describes.

The three focal words are only superficially parallel. The root-final \emph{s} of 'louse' is itself an extension of \emph{*luw-} on the model of 'mouse' [@Bammesberger1990, p. 195, §8.3]. For 'goose', Szemerényi's lengthening would give a Proto-Indo-European nominative \emph{*ǵʰanss} > \emph{*ǵʰān}, after which the Proto-Germanic nominative was rebuilt with a final voiced sibilant, \emph{*ganz}, reanalyzed within the paradigm [@Bammesberger1990, p. 196, §8.3; @Kroonen2013, pp. 168--169]. 'Book' preserves a plain obstruent-final root. What unites them is not a single phonetic history but membership in a paradigm class that generalized the endingless nominative.

The branch evidence dates and localizes that generalization. Gothic keeps its sibilant throughout the class (\emph{baúrgs}, \emph{nahts}, \emph{reiks}) [@Fulk2018, pp. 165--166, §§7.26--7.27]. Old Norse redistributes the ending morphologically: masculine root nouns keep \emph{-r} (\emph{fótr}), feminines are endingless (\emph{nótt}, \emph{geit}), while the vocalic-stem feminines \emph{kýr}, \emph{sýr}, \emph{ær} retain \emph{-r} from \emph{*-z} with R-umlaut [@Fulk2018, p. 167, §7.28; @Bammesberger1990, pp. 192--193]. West Germanic alone is uniform: there was "no ending in PWGmc, as none of the daughters exhibits any" [@RingeTaylor2014, p. 118, §3.4]. Fulk supplies the mechanism: Szemerényi's law removed the nominative sibilant after sonorant-final stems, and endinglessness then spread analogically through the class [@Fulk2018, p. 143, §7.2]. The development is therefore best understood as a morphological generalization enacted differently in each branch — absolute in West Germanic, consonant- and gender-conditioned in North Germanic, absent in Gothic — rather than as one exceptionless sound law.

This change is distinct from the two later final-\emph{*z} developments. It was complete before Proto-West Germanic, whereas the loss of \emph{*-z} in unstressed syllables ([SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion)) is itself a Proto-West Germanic change: polysyllabic consonant-stem nominatives such as \emph{*fadurz} 'father' — and, in this corpus, \emph{*frijōndz} 'friend', \emph{*melukz} 'milk', and \emph{*mēnōþz} 'month' — kept their ending into Proto-West Germanic and lost it there in an unstressed syllable [@RingeTaylor2014, pp. 44--45, §3.1.1]. The still later northern loss of \emph{*-z} in stressed monosyllables ([SC097 MonosyllabicFinalZLoss](#rule-MonosyllabicFinalZLoss)) affects vowel-final monosyllables like \emph{*hwaz} and does not touch the consonant-final root nouns at all, whose ending was gone long before.

## SC096. Root-noun nominative \emph{*-z} loss (`RootNounNomZLoss`) {#rule-RootNounNomZLoss}

```foma
define RootNounNomZLoss Ctx([{*z} -> 0 ||
    .#. [EnglishStarConsonant | EnglishPalatalConsonant]*
        EnglishStarVocalic+
        [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.]);
```

The rule deletes word-final \emph{*z} after a consonant in a monosyllable. Three claims of different kinds meet here and must be kept apart. The historical claim is morphological: the nominative-singular ending was lost in the athematic root-noun class, so that this one paradigm cell came to lack its marker — a development complete before Proto-West Germanic [@RingeTaylor2014, p. 118, §3.4]. The lexical claim belongs to the dictionaries: Orel's citation forms, which supply the corpus inputs, print that marker explicitly as \emph{-z} in \emph{*bōkz}, \emph{*flauxz}, \emph{*ǥansz}, and \emph{*lūsz} [@Orel2003, pp. 52, 105, 126, 252]. The executable statement is neither of these but a computational proxy for them: 'delete word-final \emph{*z} after a consonant in a monosyllable'. It is not proposed as a Proto-Germanic sound law; it earns its place only because every form the corpus submits to the morphological development is a consonant-final monosyllable, so the narrow phonological statement covers the class exactly. Four corpus derivations witness the rule, each yielding its expected Old English outcome: PGmc [bōkz]{.recon} 'book' yields OE *bōc* 'book', [gánsz]{.recon} 'goose' yields *gōs* 'goose', [lūsz]{.recon} 'louse' yields *lūs* 'louse', and [fláuxz]{.recon} 'flea' yields *flēah* 'flea'. Should the corpus ever acquire a consonant-final monosyllable in \emph{*-z} that is not a root-noun nominative, the proxy and the morphology would come apart, and the rule would need to be re-scoped; the project's regression tests pin the firing population to exactly these four words so that any fifth firing forces that adjudication rather than passing silently.

The rule applies at the head of the English line, before [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction). That ordering is fixed by the identity of the process rather than by a wrong form: contraction turns the polysyllabic [fríjōndz]{.recon} 'friend' into a monosyllable, and if the root-noun rule applied after contraction it would capture \emph{*friundz} — yet the ending of 'friend' survived into Proto-West Germanic and fell in an unstressed syllable, the change described under [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion) [@RingeTaylor2014, pp. 44--45, §3.1.1]. Because both rules delete the same segment, moving this rule later changes no Old English output; the early placement keeps the derivation of 'friend' aligned with the historical account rather than with an accident of the cascade.

Negative controls behave as the morphology predicts. Stressed monosyllables whose \emph{*z} follows a vowel — the domain of the later northern change — do not meet the post-consonantal environment. Medial \emph{*z} is untouched and remains available for rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)): PGmc [déuzą]{.recon} 'deer' still yields OE *dēor* 'deer' with its rhotacized medial consonant.

\newpage

# Early unstressed vowel changes

## Historical discussion

The first change monophthongizes unstressed \emph{*ai}; the second carries early unstressed front-vowel leveling farther in forms such as *weorold* 'world'. Both have a diagnostic later boundary in the dataset.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e}, in final and nonfinal syllables alike [@RingeTaylor2014, pp. 37--41]. Two dative-singular endings in the dataset, span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed', carry the change. The stressed development of \emph{*ái} to \emph{*ā} is treated separately as [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## \CAPRRuleHeading{SC014. Monophthongization of unstressed \emph{*ai}}{PNWGmcUnstressedAiMonophthongization} {#rule-PNWGmcUnstressedAiMonophthongization}

```foma
define PNWGmcUnstressedAiMonophthongization Ctx([
    {*ai} -> {*ē}
]);
```

The dative-singular endings span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed' carry this change; both give a final \emph{*ē}. If [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) is delayed until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), the \emph{*ē} is no longer present for shortening, so PGmc [spánnai]{.recon} 'span' yields [*spannē*]{.pred} rather than expected OE *spanne* 'span'. This shows that [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) in the modeled sequence.

Ringe and Taylor's merger of unstressed \emph{*ai} with long mid \emph{*ē} establishes the historical development, in final and nonfinal syllables alike. The stressed development of \emph{*ái} to \emph{*ā} is a separate and later change; see [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* 'world' and *weoruld* 'world' [@Campbell1959, pp. 141--142, 154--155]. These forms supply [SC015 PNWGmcILowering](#rule-PNWGmcILowering) with a firmer lexical basis than the preceding change.

## \CAPRRuleHeading{SC015. Leveling of early unstressed front vowels}{PNWGmcILowering} {#rule-PNWGmcILowering}

```foma
define PNWGmcILowering Ctx([
    {*i} -> {*e}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel,
    {*í} -> {*é}
        || .#. EnglishStarNonVelarConsonant* _
           EnglishStarCoronal+ EnglishStarNonHighVowel
]);
```

The *weorold* 'world' and *weoruld* 'world' variants turn the general source claim into an ordering test. If [SC015 PNWGmcILowering](#rule-PNWGmcILowering) is delayed until after [SC036 OEInterStressRaising](#rule-OEInterStressRaising), PGmc [wír-àldu]{.recon} ‘world’ yields [*wuruld*]{.pred} rather than expected OE *weorold* ‘world’; earlier movement changes no output.

The derivation thus fixes front-vowel leveling before interstress raising while leaving its earlier boundary open.

[SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) and [SC017 PNWGmcULowering](#rule-PNWGmcULowering) follow with a more tightly constrained local chronology.

\newpage

# Unstressed \emph{*a}-raising before final \emph{*m}

## Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise includes the development of early unstressed \emph{*o} to \emph{u} before \emph{m} among the similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

I restrict the change to unstressed vowels in inflectional material because the strongest evidence concerns noninitial unstressed material before final \emph{*m}.
Final \emph{*m} conditions the raising.

## SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`PNWGmcAToUBeforeM`) {#rule-PNWGmcAToUBeforeM}

```foma
define PNWGmcAToUBeforeM Ctx([
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
]);
```

Here the witness word and the comparative evidence serve different purposes. If raising is delayed until after [SC017 PNWGmcULowering](#rule-PNWGmcULowering), PGmc [skúldramiz]{.recon} 'shoulders' yields [*sċoldrum*]{.pred} rather than expected OE *sċuldrum* 'shoulders'; earlier placements converge on the expected output. The scope of the change is established by inflectional evidence across multiple paradigm types: a-stem dative plural ON [*dǫgum*]{.iv lang=on sort=dogum role=evidence_form} 'days', OE [*dagum*]{.iv lang=oe sort=dagum role=evidence_form} 'days', OS [*dagun*]{.iv lang=os sort=dagun role=evidence_form} 'days', OHG [*tagum*]{.iv lang=ohg sort=tagum role=evidence_form} 'days', beside Gothic [*dagam*]{.iv lang=goth sort=dagam role=evidence_form} 'days'; strong-adjective dative singular ON [*góðum*]{.iv lang=on sort=godum role=evidence_form} 'good', OE [*gōdum*]{.iv lang=oe sort=godum role=evidence_form} 'good', OS [*gōdum*]{.iv lang=os sort=godum role=evidence_form} 'good', beside Gothic [*godamma*]{.iv lang=goth sort=godamma role=evidence_form} 'good' (OS also shows variant forms gōdumu and -un); and first-plural present ON [*berum*]{.iv lang=on sort=berum role=evidence_form} 'we carry', OHG [*berumēs*]{.iv lang=ohg sort=berumes role=evidence_form} 'we carry', beside Gothic [*baíram*]{.iv lang=goth sort=bairam role=evidence_form} 'we carry'. Across these sets, North/West Germanic shows unstressed \emph{-um} where Gothic preserves \emph{-am}. The derivation of *sċuldrum* 'shoulders' supplies a CAPR ordering witness for the relative chronology, but the cognate set for 'shoulder' does not contribute comparative evidence for the rule's historical scope.

\newpage

# Northwest Germanic lowering of long \emph{ē}

## Historical discussion

Proto-Germanic \emph{*ē₁} (the long mid vowel of PIE origin, as against the later \emph{*ē₂}) split East Germanic from the rest of the family. Gothic keeps a mid vowel, written ⟨e⟩, in *gadēþs* 'deed', *slēpan* 'to sleep', *mēna* 'moon', and *jēr* 'year', while Norse and all of West Germanic show a low vowel, as in Old Norse *ráða* 'to consider, to advise', *láta* 'to let go, to allow', *ár* 'year', *nál* 'needle', Old High German *tāt* 'deed', *slāfan* 'to sleep', *jār* 'year', *māno* 'moon', Old Saxon *dād* 'deed', *slāpan* 'to sleep', *jār*. Ringe and Taylor assemble the comparative set and reconstruct a Northwest Germanic sound change \emph{*ē₁} > \emph{*ā} [@RingeTaylor2014, pp. 11--13]. The change is directly dated by the earliest epigraphy. The Early Runic accusative \emph{mākija} 'sword' (beside Gothic *mēkeis* 'sword') already shows ⟨a⟩ in the second half of the second century AD [@RingeTaylor2014, p. 12], and the a-rune likewise writes the stressed reflex in the Opedal stone's *swestar* 'sister' [@Stiles2017, p. 4]. Loanwords borrowed into Sami from early Proto-Scandinavian point the same way. Lid showed that the root vowel of Sami *mānno* 'moon', Proto-Germanic \emph{*ē} as in Gothic *mēna*, "had gone over to \emph{ā} before the word was borrowed into Sami", and adduced the parallel Sami *saððo* 'bran' beside Proto-Nordic \emph{*sāðō} from \emph{*sēðō-}, Old Norse *sáð* 'bran' [@Lid1952, p. 238]. This is Sami borrowing from Proto-Scandinavian, so it dates and localizes the \emph{ā} stage in the North; its application to West Germanic rests on the daughter correspondences above.

The change affected stressed syllables only. Ringe and Taylor restrict it explicitly: unstressed \emph{*ē} did not lower but was eventually shortened, as in \emph{*fadēr} > \emph{*fader} 'father' [@RingeTaylor2014, p. 13, and p. 147]; in the runic material the unstressed final vowel of *faþiR* 'father' has already merged with \emph{*-i} [@Stiles2017, p. 4]. Within stressed syllables, however, the lowering was unconditioned: it applied before nasals exactly as elsewhere, and Ringe and Taylor accordingly print the intermediates \emph{*mānō} 'moon', \emph{*mānōþ-} 'month', and \emph{*spānuz} 'spoon' [@RingeTaylor2014, p. 11]. The later, dialectally narrower fates of this \emph{*ā} — fronting in the North Sea area when oral, rounding when nasalized — are separate sound changes treated in their own chapters.

The reconstruction of the intermediate value is disputed. The objection is an old one: Bennett observed that the received account obliges Gothic to move \emph{ē} to \emph{ǣ} and back to \emph{ē}, and the non-West-Saxon dialects and Old Frisian to run through \emph{ē > ǣ > ā > ǣ > ē}, "with no apparent agreement among the languages and no discernible phonological trend", and that the Proto-Germanic \emph{ǣ} is on that account preserved directly nowhere [@Bennett1950, pp. 232--233, 235]. In its place he proposed that the backing to \emph{ā} began in the north of the Germanic homeland and spread southward, never reaching Gothic in the east or Anglian and Frisian in the west, so that West Saxon \emph{ǣ} is a retention of the intermediate stage rather than a re-fronting [@Bennett1950, pp. 234--235]. Fulk argues in the same direction on modern evidence: the Northwest Germanic vowel was a low front \emph{*ǣ}, retained unchanged in Anglo-Frisian, with the backing to \emph{ā} of Norse and inner West Germanic a separate areal development spreading northward from Upper German territory; on that reading the runic ⟨a⟩ spellings write a front [æː] for which the futhark had no better grapheme [@Fulk2018, pp. 60--61, §4.6]. Campbell is deliberately noncommittal, finding the \emph{*ā} stage "tempting to assume, though not definitely demonstrable" [@Campbell1959, pp. 50--51, §§128--129]. Ringe and Taylor answer with the lengthened place-adverbs *þǣr* 'there' and *hwǣr* 'where', whose front vowels are most naturally the output of fronting applied to a back \emph{*ā} [@RingeTaylor2014, pp. 13--14]. The present model adopts the two-step reconstruction while recording that the alternative remains live. Campbell is deliberately noncommittal, finding the \emph{*ā} stage "tempting to assume, though not definitely demonstrable" [@Campbell1959, pp. 50--51, §§128--129]. Ringe and Taylor answer with the lengthened place-adverbs *þǣr* 'there' and *hwǣr* 'where', whose front vowels are most naturally the output of fronting applied to a back \emph{*ā} [@RingeTaylor2014, pp. 13--14]. The present model adopts the two-step reconstruction while recording that the alternative remains live.

## SC024. Lowering of stressed long \emph{ē} (`PNWGmcLongELowering`) {#rule-PNWGmcLongELowering}

```foma
define PNWGmcLongELowering Ctx([
    {*ḗ} -> {*ā}
]);
```

The rule reads the stressed tier \emph{*ḗ} only, in keeping with the stress restriction; unstressed \emph{*ē}, as in \emph{*fadēr} 'father', is left for the unstressed-shortening rules of the Old English stage and never lowers. No segmental environment is imposed: nasal forms such as [mḗnōþz]{.recon} 'month' and [spḗnuz]{.recon} 'spoon' pass through \emph{*mānōþ-} and \emph{*spānuz} on their way to *mōnaþ* 'month' and *spōn* 'spoon', exactly as reconstructed by Ringe and Taylor [@RingeTaylor2014, p. 11].

The rule stands near the head of the cascade, before the genuinely West Germanic innovations such as early \emph{i}-apocope, \emph{*ij}-contraction, and \emph{j}-gemination — the placement follows from the dating: the second-century runic evidence puts the lowering among the earliest Northwest Germanic developments, well before the changes that separate West Germanic from Norse. Its output \emph{*ā} is consumed much later in the cascade by [SC102 EAFHiatusWInsertion](#rule-EAFHiatusWInsertion), [SC025 EAFLongANasalRounding](#rule-EAFLongANasalRounding), and [SC101 EAFLongAFronting](#rule-EAFLongAFronting): if the lowering is instead displaced after those rules, [mḗnōθz]{.recon} 'month' yields [*mānaþ*]{.pred} rather than OE *mōnaþ* 'month', [skḗpą]{.recon} 'sheep' yields [*sċāp*]{.pred} rather than *sċēap* 'sheep', and [sḗaną]{.recon} 'to sow' never acquires the hiatus-filling \emph{w} of *sāwan* 'to sow'. Within the cascade no earlier boundary has been demonstrated; the second-century runic attestation supplies the absolute dating.

\newpage

# Early i-apocope

## Historical discussion

Sievers/Brunner treats the early loss of final \emph{*i} after unstressed syllables as established by the fact that these endings no longer trigger later i-umlaut in Old English, and Ringe and Taylor make the same point through the pathway to *geoguþ* ‘youth’ [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141]. Campbell's *dugup* 'troop' and *geogup* 'youth' examples belong to the same pattern [@Campbell1959, §332].

The ending vowel disappears in a weak suffixal environment early enough to block later umlaut. This anti-umlaut chronology distinguishes the change from later final-vowel losses.

## SC006. Early i-apocope (`PWGmcEarlyIApocope`) {#rule-PWGmcEarlyIApocope}

```foma
define PWGmcEarlyIApocope Ctx([
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
]);
```

The absence of umlaut in *geoguþ* ‘youth’ provides the historical argument for early deletion. The ordered derivation supplies a different test: if apocope is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc [skáwōθi]{.recon} ‘shows’ yields [*sċēaweþ*]{.pred} rather than expected OE *sċēawaþ* 'shows'.

Early i-apocope must therefore precede the long-diphthong development. Moving it earlier within the tested range leaves every output unchanged; its early date rests on the anti-umlaut evidence, not on a lower boundary supplied by the witness words.

\newpage

# Final \emph{*ō}-lowering before \emph{*r}

## Historical discussion

Ringe and Taylor separate two points here: a broader shortening of vowels before word-final \emph{*r} in unstressed syllables (for which kinship \emph{*r}-stems such as PGmc \emph{*fadér} > PWGmc \emph{*fader} are a key diagnostic), and the specific \emph{*ō}-before-\emph{*r} development needed here [@RingeTaylor2014, pp. 58--59]. The direct lexical witnesses for \emph{*ō} in that environment are two independent etyma: PGmc [fedwōr]{.recon .iv lang=pgmc sort=fedwor role=evidence_form} 'four' with WGmc reflexes OE [*fēower*]{.iv lang=oe sort=feower role=evidence_form} 'four', OFris [*fiuwer*]{.iv lang=ofris sort=fiuwer role=evidence_form} 'four', OS [*fiuwar*]{.iv lang=os sort=fiuwar role=evidence_form} 'four'; and PGmc [watōr]{.recon .iv lang=pgmc sort=wator role=evidence_form} 'water' with OE [*wæter*]{.iv lang=oe sort=waeter role=evidence_form} 'water'.

The rule is historically secure but narrow: final or pre-final \emph{*ō} before word-final \emph{*r}. The clearest evidence remains concentrated in the `four` and `water` material.
No broader environment for \emph{*ō} is attested.

## \CAPRRuleHeading{SC007. Lowering of final bimoric \emph{*ō} before \emph{*r}}{PWGmcFinalOrLowering} {#rule-PWGmcFinalOrLowering}

```foma
define PWGmcFinalOrLowering Ctx([
    {*ō} -> {*a} || _ {*r} .#.
]);
```

OE *wæter* ‘water’ reveals why lowering must precede [SC043 EAFBrightening](#rule-EAFBrightening). If [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) is delayed until afterwards, PGmc [wátōr]{.recon} ‘water’ yields [*water*]{.pred} rather than expected OE *wæter* ‘water’: brightening can affect the vowel only after lowering has created its input. Moving the change earlier within the tested range alters no output.

The witness thus supplies a terminus ante quem at brightening but no earlier boundary. Comparative support for the \emph{*ō}-before-\emph{*r} rule comes from the two lexical witnesses [fedwōr]{.recon .iv lang=pgmc sort=fedwor role=evidence_form} 'four' and [watōr]{.recon .iv lang=pgmc sort=wator role=evidence_form} 'water' and their WGmc reflexes; kinship \emph{*r}-stems belong to the broader pre-\emph{*r} shortening context, not to a direct \emph{*ō} > \emph{*a} control. Within CAPR, [*wæter*]{.iv lang=oe sort=waeter role=evidence_form} 'water' is the form that establishes ordering before brightening. No broader lowering of \emph{*ō} is attested.

\newpage

# Coronal-w assimilation

## Historical discussion

Ringe and Taylor treat the assimilation of \emph{*dw} and \emph{*zw} to \emph{*ww} as a shared Proto-West-Germanic innovation supported by one example of each input cluster [@RingeTaylor2014, pp. 56--57; @Stiles1985, pp. 89--94]. The \emph{*dw} example is the numeral 'four': PGmc \emph{*feðwor} (Gothic \emph{fidwor}) → WGmc \emph{*fewwar} → OE \emph{fēower}, Old Frisian \emph{fiuwer}, Old Saxon \emph{fiuwar}. The \emph{*zw} example is the second-person plural pronoun, where two oblique case forms show the change: acc./dat.\ PGmc \emph{*izwiz} (Gothic \emph{izwis}) → OE \emph{eow}, Old Frisian \emph{iu}, Old Saxon \emph{iu}, OHG \emph{iu}; and gen.\ Ringe and Taylor's PGmc \emph{*izweraz} (Gothic \emph{izwara}) → OE \emph{eower}, OHG \emph{iuwer} [@RingeTaylor2014, p. 56]. Stiles discusses the same pronominal material using his own reconstruction conventions and explicitly treats Gothic \emph{izwara} among the relevant comparanda [@Stiles1985, pp. 89--94]. These two case forms belong to a single pronominal paradigm, not to two independent etyma.

The historical support rests on a small witness set. Both coronal inputs assimilate before \emph{*w}, but the evidence for each cluster is confined: the numeral alone supplies the \emph{*dw} instance, and the oblique case forms of the second-person plural pronoun supply the \emph{*zw} instance. Both clusters are now witnessed in the corpus: 'four' for \emph{*dw}, and 'you' — selected in its dat.(-acc.) plural cell \emph{*izwiz} — for \emph{*zw}, deriving through \emph{*iwwi}, apocopated \emph{*iww}, to OE *ēow* 'you' [@RingeTaylor2014, pp. 41--42, §3.1.1; @Fulk2018, §8.3, pp. 204--205].

## \CAPRRuleHeading{SC008. Assimilation of coronal consonants before \emph{*w}}{PWGmcCoronalWAssimilation} {#rule-PWGmcCoronalWAssimilation}

```foma
define PWGmcCoronalWAssimilation Ctx([
    {*d} -> {*w} || _ {*w},
    {*z} -> {*w} || _ {*w}
]);
```

OE *fēower* ‘four’ exposes a feeding relation: coronal assimilation creates the \emph{*ww} input of the early reanalysis in [SC031 OEWWSimplification](#rule-OEWWSimplification), yielding the diphthongal intermediate before later English realization. Ringe and Taylor explicitly give the coronal-assimilation and glide-reanalysis sequence [@RingeTaylor2014, pp. 41--42]. The earlier displacement result belonged to the superseded late \emph{*ww}-deletion proxy and does not by itself predict the result of displacing the reformulated early operation.

The numeral fixes that relative order. The pronoun now fixes a second one: assimilation must precede rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)). The \emph{*z} of \emph{*izwiz} stands between vowel and \emph{*w}; had rhotacism applied first, it would have produced [*irwiz*]{.pred}, from which OE *ēow* 'you' can never be derived. The executable cascade composes the assimilation well before rhotacism, and the corpus derivation of *ēow* 'you' fails if the two are reversed. 'Four' remains the sole \emph{*dw} witness and the sole source of the coronal-assimilation → *ww*-simplification ordering constraint. The earlier boundary of the assimilation remains undetermined.

\newpage

# Inherited short-vowel-plus-geminate-glide reanalysis

## Historical discussion

Inherited geminate glides after short vowels underwent reanalysis in
Proto-West Germanic: the first glide became the offglide of a diphthong,
while the second remained consonantal. This is not simply deletion of one
\emph{w}, and it is not the later English realization of the new diphthong.
Ringe and Taylor distinguish those histories explicitly; Fulk specifies
the short-vowel environment ([@RingeTaylor2014, pp. 41--42, 65--66,
171--175; @Fulk2018, p. 117]).

Coronal assimilation feeds the change in *fēower* 'four' and *ēow* 'you':
[SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) supplies
the geminate that becomes \emph{eu+w} or \emph{iu+w}. Inherited geminates
also supply the histories of *ċēowan* 'chew', *dēaw* 'dew' and *hēawan*
'hew'. The resulting diphthongs enter the separate English realization
described under [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling)
([@RingeTaylor2014, pp. 41--42, 65--66, 172--175;
@Campbell1959, pp. 45--47]).

Homorganic \emph{uww} requires a separate quantity decision. We adopt
Ringe and Taylor's preferred long-\emph{u} account for *sċūwa* 'shadow',
but retain their qualification of its evidence rather than treating the
quantity as independently certain. Hypothetical inherited long-vowel-plus-
\emph{ww} sequences are not additional reconstructed witnesses: the held
description specifies inherited geminates after short vowels. The
parallel inherited \emph{jj} development is independently governed and
is not changed here ([@RingeTaylor2014, pp. 65--66; @Fulk2018, p. 117]).

## SC031. Inherited short-Vww reanalysis (`OEWWSimplification`) {#rule-OEWWSimplification}

```foma
define OEWWSimplification Ctx([
    {*a} {*w} {*w} -> {*au} {*w},
    {*á} {*w} {*w} -> {*áu} {*w},
    {*e} {*w} {*w} -> {*eu} {*w},
    {*é} {*w} {*w} -> {*éu} {*w},
    {*i} {*w} {*w} -> {*iu} {*w},
    {*í} {*w} {*w} -> {*íu} {*w},
    {*u} {*w} {*w} -> {*ū} {*w},
    {*ú} {*w} {*w} -> {*ū} {*w}
]);
```

The transport wrapper carries an independently selected sentence context
outside the segmental rewrite; it adds no reconstructed sound and does not
condition the reanalysis. Acute and unmarked spellings are notation
variants, not alternatives in sentence stress. The retained executable
name likewise does not determine the historical stage.

The modeled position after coronal assimilation and before j-gemination
is a representative serialization that keeps inherited/coronal-created
geminates distinct from the subsequently created j-path. It is not a
newly proved strict chronology between the whole events. *Hīeġ* 'hay'
and reconstructed West Saxon strew retain the separately adjudicated
[SC029 OEAwwjResolution](#rule-OEAwwjResolution) path. *Hīew* 'hue'
retains its independently governed realization and the explicitly
disclosed [SC106 OEJWWSimplification](#rule-OEJWWSimplification) residual
([@Campbell1959, pp. 45--47; @RingeTaylor2014, p. 173]).

For you, early \emph{iu+w} now reaches
[SC098 PWGmcUnstressedWordFinalIApocope](#rule-PWGmcUnstressedWordFinalIApocope).
Its weak-final context, not the former presence of literal \emph{ww},
licenses apocope before mutation. Earlier source-backed reanalysis thus
coexists with genuine prosodic conditioning rather than an output-restoring
segment proxy ([@RingeTaylor2014, pp. 41--42, 55, 57--58]).

\newpage

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

\newpage

# West Germanic j-gemination

## Historical discussion

Fulk treats West Germanic consonant gemination before `*j` after a short vowel as a regular development and illustrates it with forms such as OE *settan* 'set' and *lecgan* 'lay' [@Fulk2018, p. 127, §6.15].

The change applies specifically after a short vowel before \emph{*j}, not to geminate consonants generally.

## SC010. West Germanic j-gemination (`PWGmcJGemination`) {#rule-PWGmcJGemination}

```foma
define PWGmcJGemination Ctx([
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
]);
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
define PWGmcSyllabicJ Ctx([
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
]);
```

The same PGmc [nátją]{.recon} ‘net’ witness supplies the only firm boundary. Placing [SC011 PWGmcSyllabicJ](#rule-PWGmcSyllabicJ) before [SC010 PWGmcJGemination](#rule-PWGmcJGemination) yields [*nete*]{.pred} rather than expected OE *nett* 'net'; moving it later changes no output.

Comparative evidence establishes postconsonantal \emph{*j} to syllabic \emph{*i} after final unstressed \emph{*a} or \emph{*ą} loss, with *here* 'army' and *rice* 'kingdom' as outcomes. The lexicon adds only that vocalization followed gemination, not where it falls among subsequent changes.

\newpage

# Simplification of the cluster \emph{*xs} before a consonant

## Historical discussion

The change treated here is narrow. When \emph{*x} stood before \emph{*s} and
that \emph{*s} was itself followed by a further consonant, the \emph{*x} was
lost and the cluster was reduced. Campbell states the rule in exactly these
terms, that when a consonant follows, \emph{*xs} becomes *s*, and he illustrates
it with *wæstm* ‘growth’ and *wæsma* ‘growth’ beside *weaxan* ‘to grow’, and with
Northumbrian *sesta* ‘sixth’ beside West Saxon *siexta*
[@Campbell1959, p. 170, §417]. Brunner gives the same statement and adds that
the following consonant may be *j* as well as a true obstruent, citing
*nēosian* ‘to visit’, *þīsl* ‘pole’, *wæsma* and *wæstm*
[@SieversBrunner1965, p. 184, §221.2]. Bülbring formulates it as a pre-English
change and is careful to say that it held as a rule, with exceptions
[@Bulbring1902, p. 215, §527].

The cluster that the change requires is a specific one, and two neighbouring
clusters show that the restriction is real. Where \emph{*xs} stood with no
consonant after it, the \emph{*x} was not lost at all. It survived long enough
to cause breaking and then hardened to the sound written *x*, that is [ks], as
in *fox* ‘fox’, *siex* ‘six’, *weaxan*, *oxa* ‘ox’ and *fleax* ‘flax’
[@Campbell1959, p. 170, §416]. Where \emph{*x} stood before a single consonant
it was likewise kept. Campbell observes that once \emph{*xs} had become [ks],
the only group in which \emph{*x} still stood before a voiceless consonant in
earliest Old English was \emph{*xt}, and that this group remained, as in
*feohtan* ‘to fight’, *miht* ‘might’, *niht* ‘night’ and *sōhte* ‘sought’
[@Campbell1959, p. 186, §464]. The contrast is attested outside English as
well. Old High German and Old Saxon *lastar* ‘reproach’ comes from
\emph{*laxstra-} with the \emph{*x} lost before \emph{*st}, while Old English
*leahtor* comes from \emph{*laxtra-} with the \emph{*x} kept before \emph{*t}
[@Campbell1959, p. 170, §417].

The change is not Proto-Germanic. Gothic keeps the \emph{*h} of this cluster in
*bi-niuhsjan* ‘to spy out’ and *saihsta* ‘sixth’, so the loss must be later than
the separation of Gothic [@RingeTaylor2014, pp. 157--158]. Campbell reports the
loss from the whole West Germanic area and from North Germanic as well, citing
Old Norse *ísl* ‘axle’ and *nýsa* ‘to investigate’, Old Saxon *weslon* ‘to exchange’, *wastum*
‘growth’ and *niustan*, and Old High German *niusen* ‘to try’
[@Campbell1959, p. 170, §417]. Ringe and Taylor set out the same comparative
material and reach a more guarded conclusion. They derive Proto-Germanic
\emph{*niuhsijaną} through Proto-West Germanic \emph{*niusjan} to Old English
*nēosan* ‘to seek out, to visit’, and \emph{*sehstō} to Northumbrian *sesta*, and they take the Old
Saxon agreement in *wastum*, *thisla* and *niusian* to show a shared northern
West Germanic change. Against that they weigh the competition between *þixl* ‘pole’
and *þīsl* ‘pole’ in early Mercian, the survival of \emph{*x} in *eaxl* ‘shoulder’ from
\emph{*ahslu}, and the retention in Old High German *sehsto* and *dihsala*.
Their conclusion is that the \emph{*h} was lost, possibly variably and possibly
only in some dialects, when two or more consonants followed, and that the loss
may have been in part a parallel development in the diverging Northwest Germanic
dialects [@RingeTaylor2014, pp. 157--158]. The existence of the change is
therefore secure while its exact date and extent are not, and the rating given
here reflects that division.

Two chronological anchors are available. Ringe and Taylor place the loss after
the Proto-West Germanic syncope of \emph{*-CijV-}, since it is that syncope
which brings the \emph{*s} and the \emph{*j} of \emph{*niuhsjan} together
[@RingeTaylor2014, p. 157]. They place it before breaking, observing that the
undiphthongized vowels of *wæstm* ‘growth’ and *þīsl* ‘pole’ can be accounted for only by
supposing that these \emph{*h} were lost before breaking took place
[@RingeTaylor2014, p. 158]. The rule is stated between those two points.

One witness in this collection undergoes the change. Proto-Germanic
\emph{*funxstiz} ‘fist’ reaches the rule as \emph{*fū́xstiz}, the long vowel
having been produced by the Proto-Germanic loss of a nasal before \emph{*x}
described in [SC103 PGmcNasalLossBeforeX](#rule-PGmcNasalLossBeforeX). The
cluster \emph{*xst} is then reduced to \emph{*st}, and the word continues to Old
English *fȳst* ‘fist’. The comparative set for this particular word is West
Germanic throughout, with Old Frisian *fēst* ‘fist’, Old Saxon and Old High German
*fūst* ‘fist’, Dutch *vuist* and German *Faust*
[@Kroonen2013, p. 160; @Orel2003, p. 157]. Neither Gothic nor Old Norse
preserves a reflex of it, so the word bears on the domain of the change rather
than on its date.

The word *thought* is the control. Proto-Germanic \emph{*θánxtē} also passes
through [SC103 PGmcNasalLossBeforeX](#rule-PGmcNasalLossBeforeX), which leaves
\emph{*θą̄xtē}, but the \emph{*x} there stands before a single \emph{*t} and not
before \emph{*s}, so the present rule does not touch it and Old English has
*þōhte* ‘thought’ with its *h* intact. The pair *fist* and *thought* reproduces
within this collection the same contrast that *lastar* and *leahtor* show across
the West Germanic languages.

The relation between the two rules should not be overstated. The earlier rule
does supply the cluster that this one simplifies, but the order of the two is
established by their stages and not by any word in this collection. If the
present rule were stated first, *fist* would still reach *fȳst* ‘fist’, because
removing the \emph{*x} from \emph{*funxstiz} leaves a nasal before *s*, and that
nasal is removed with compensatory lengthening by the North Sea Germanic
nasal-spirant law. The outcome is overdetermined, and the chronology rests on
Gothic *bi-niuhsjan* ‘to spy out’ and *saihsta* instead.

## \CAPRRuleHeading{SC028. Simplification of \emph{*xs} before a consonant}{PNWGmcPreconsonantalXLoss} {#rule-PNWGmcPreconsonantalXLoss}

```foma
define PNWGmcPreconsonantalXLoss Ctx([
    {*x} -> 0 || _ {*s} EnglishStarConsonant
]);
```

The \emph{*s} in the structural description carries the whole weight of the
rule. Without it the rule would delete \emph{*x} before any two consonants, and
it would then wrongly remove the first element of a geminate \emph{*xx} before
\emph{*j}, where Old English in fact has *hliehhan* ‘to laugh’ with the geminate
written *hh* [@Campbell1959, p. 186, §464]. The rule fires on *fist* and on no
other word in this collection, and it leaves *fox*, *six*, *wax*, *flax* and
*ox* untouched, as it must, along with *thought*, *fight*, *night*, *light*,
*might*, *knight*, *fright* and *wight*.

The implementation name retains an older description of the rule and will be
brought into line in a separate pass.

\newpage

# \emph{lþ}-voicing

## Historical discussion

Ringe and Taylor treat word-internal \emph{*lþ} > \emph{*ld} as a regular sound change in northern West Germanic and illustrate it with forms such as *fealdan* 'fold', *beald* 'bold', *wuldor* 'glory', and *gylden* 'golden' [@RingeTaylor2014, pp. 170--171]. Campbell gives a similar West-Germanic-facing formulation with examples such as *fealdan*, *wuldor*, *beald*, *gold* 'gold', and *feld* 'field' [@Campbell1959, p. 169, §414].

The comparative evidence supports \emph{lþ > ld} most clearly in northern West
Germanic, not as an unqualified pan-PWGmc development.

## SC012. Northern West Germanic \emph{lþ}-voicing (`EAFLThVoicing`) {#rule-EAFLThVoicing}

```foma
define EAFLThVoicing Ctx([
    {*θ} -> {*d} || {*l} _
]);
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
define PWGmcDentalHardening Ctx([
    {*ð} -> {*d}
]);
```

Dental hardening has systemic scope: voiced fricative \emph{*ð} became stop \emph{*d} throughout early West Germanic. Moving [SC013 PWGmcDentalHardening](#rule-PWGmcDentalHardening) earlier or later changes no output.

Comparative evidence establishes the sound law; the present lexicon leaves its exact position approximate.

\newpage

# Northwest Germanic u-lowering

## Historical discussion

Northwest Germanic lowered \emph{*u} to \emph{*o} when the following
syllable contained a non-high vowel. Campbell describes the change and
lists *ġeoc* 'yoke' among its regular outcomes [@Campbell1959, pp. 42--43,
§115]; Fulk gives the same word as a standard example — "OIcel. ok, OE
geoc, OHG joh beside juh and OS juk" — and notes the paradigmatic
alternation between lowered and unlowered stems that the conditioning
produced [@Fulk2018, p. 56, §4.3]. A word-initial \emph{*j} does not block
the change: the blocking effect of \emph{j} concerns only a consonantal
\emph{j} standing between the target vowel and the conditioning vowel, as
in the class I weak verbs of the *cnyssan* 'strike' type
[@Fulk2018, p. 56, §4.3]. Ringe and Taylor accordingly reconstruct the
Proto-West Germanic paradigm of 'yoke' with the lowering applied
[@RingeTaylor2014, p. 129].

The clearest corpus witnesses are [ġeoc]{.iv lang=oe sort=geoc role=evidence_form} 'yoke', *nosu* 'nose',
*sċofl* 'shovel', and *sorg* 'sorrow'. Where the following syllable kept a
high vowel the lowering did not apply, as in *ġeoguþ* 'youth', whose root \emph{u}
survived [@SieversBrunner1965, pp. 64--65, §92.1].

## \CAPRRuleHeading{SC017. Lowering of \emph{*u} before following non-high vowels}{PNWGmcULowering} {#rule-PNWGmcULowering}

```foma
define PNWGmcULowering Ctx([
    {*u} -> {*o}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó}
        || .#. EnglishStarConsonant* _
           [EnglishStarConsonantNoJ - EnglishStarNasal]
           EnglishStarConsonantNoJ* EnglishStarNonHighVowel
]);
```

Lowering of \emph{u} to \emph{o} is fixed on both sides by *ġeoc* 'yoke',
*nosu*, *sċofl* 'shovel', and *sorg*.

The lowering feeds the much later West Saxon palatal-glide spelling
([SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide)): the \emph{o} that the
scribes wrote in *ġeoc* 'yoke' is the output of this change, so PGmc
[júką]{.recon} 'yoke' passes through \emph{*joką} on its way to the
attested spelling [@Fulk2018, p. 56, §4.3; @RingeTaylor2014, p. 129].
After [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), PGmc
[núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected *nosu*,
PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected
*sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather
than expected *sorg*. These witnesses place
[SC017 PNWGmcULowering](#rule-PNWGmcULowering) before final long-\emph{o}
raising, and the *ġeoc* spelling shows its output surviving into the
written record.

\newpage

# Stressed monosyllable \emph{*ō}-raising

## Historical discussion

Campbell treats the development of final accented \emph{ō} to \emph{ū} in stressed monosyllables directly, with the familiar outcomes behind *cū* ‘cow’, *hū* ‘how’, *tū* ‘two’, and *bū* ‘both’ [@Campbell1959, p. 47, §122].

The change is historically secure, but the tested forms determine no close relative position for it.
Its input is final \emph{*ō} in a stressed monosyllable.

## \CAPRRuleHeading{SC018. Raising of final stressed monosyllabic \emph{*ō}}{PNWGmcStressedMonosyllableORaising} {#rule-PNWGmcStressedMonosyllableORaising}

```foma
define PNWGmcStressedMonosyllableORaising Ctx([
    {*ō} -> {*ū} || .#. [EnglishStarConsonant | EnglishPalatalConsonant]* _ .#.
]);
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
define PNWGmcFinalLongORaising Ctx([
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
]);
```

Two groups of witnesses confine final unstressed long \emph{*ō} > \emph{*u}. The forms *nosu* 'nose', *sċofl* 'shovel', and *sorg* 'sorrow' fix its lower boundary.

Before [SC017 PNWGmcULowering](#rule-PNWGmcULowering), PGmc [núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected OE *nosu* 'nose', PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected *sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather than expected *sorg* 'sorrow'. After word-final \emph{*z}-deletion ([SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion)), PGmc [rástōz]{.recon} 'rest' yields [*rast*]{.pred} rather than expected *ræste* 'rest'. These failures place [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising) after u-lowering and before final \emph{z}-loss.

\newpage

# Chapter 3. From Proto-West Germanic to Anglo-Frisian


## Historical interval

This chapter covers the sound changes that occurred after the Proto-West Germanic
period and before, or during the emergence of, the specifically English line. The
starting reconstruction is Proto-West Germanic; the end point is the
Anglo-Frisian ancestor required by the model's historical tree. Its existence
and the identification of its innovations are separate questions. Its inventory
must be reconstructed from conditioned laws and daughter chronologies, not
from the traditional subgroup label alone.

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
  inheritance [@Bremmer2009, pp. 24–27, 126–128].
* Anglo-Frisian: a label used specifically for the Old English / Old Frisian
  branch, or for innovations shared between the two languages. Its use presupposes
  a tighter relationship between English and Frisian than between either and
  Old Saxon.
* Proto-Anglo-Frisian (PAF): the strongest interpretation, positing a discrete
  reconstructed common ancestor for Old English and Old Frisian specifically.
  This is the position of Ringe and Taylor, who reconstruct a PAF stage between
  Proto-West Germanic and Proto-Old-English [@RingeTaylor2014, pp. 54--68].

CAPR requires a discrete Anglo-Frisian ancestral node. This does not guarantee
that every traditionally associated innovation is inherited from it, or exclusive
to English and Frisian. A broader innovation can already be present in its
input; similar daughter outcomes can also result from independent events.
Authors' diffusion interpretations remain accurately attributed, but they
cannot resolve an incompatible chronology within CAPR's ordered tree
[@Versloot2017, pp. 302--319; @Bremmer2008, pp. 284, 292--293].

## A worked historical tree test

If a supposed shared innovation obligatorily follows a daughter-only change
in Frisian which English never underwent, it cannot occupy the common stem
under those premises. Either the ordering or scope premise must change,
the innovation happened independently, or the apparently identical events
are historically different. The required ancestor is not removed.

Campbell reconstructs Frisian au contraction before ordinary fronting;
Goblirsch instead proposes a shared diphthong followed by Frisian stress shift
and contraction [@Campbell1939, pp. 91, 104; @Goblirsch1991, pp. 17, 20--21].
The daughter-only event is a predecessor in the first account and a follower
in the second. The second is compatible with sharing, but does not attest
the reconstructed Frisian intermediate. Surface agreement, compatibility
with inheritance, compelled parallelism under premises, and unresolved history
must therefore remain distinct judgments.

## The working account and why it is used

The English reconstruction adopted as a working scaffold is the conventional
account developed by Campbell and critically refined by Ringe and Taylor.
It distinguishes inherited long vowels from the long vowels produced by
diphthong contraction, and it treats fronting, breaking, restoration and
mutation as conditioned phonological developments. That scaffold is useful
because it specifies contrasting inputs and intermediate states, not because
one author's authority decides the history
[@Campbell1959, pp. 52–53, 60–72; @RingeTaylor2014, pp. 170–173, 215–237].

The comparative specialists test particular load-bearing premises.
Campbell's argument about English and Frisian fronting, Versloot's runic
interpretations and Goblirsch's proposed lost Frisian diphthong do not form
one automatically compatible package
[@Campbell1939, pp. 90–91, 104; @Versloot2017, pp. 295–297, 318;
@Goblirsch1991, pp. 17–21]. Where an alternative changes the inherited
inventory or the identity of an event, it must be evaluated as that
alternative, not inserted into the conventional chain without its premises.

CAPR implements regular sound laws. Prosodic and phonological conditions
may distinguish environments, but lexical diffusion, grammatical categories
and individually selected exceptions cannot repair a contradiction.
Paradigm remodeling and borrowing may affect which historical form a
lexical entry represents; they are not thereby conditions on a sound law.
This methodological choice is distinct from faithfully reporting an author's
different theoretical account.

## Long vowels, diphthongs and the ancestral inventory

The inherited-long contrast is central. On the conventional reconstruction,
inherited oral long \emph{*ā} has already acquired a front quality when
English stressed \emph{*ai} completes its development to a new back
\emph{*ā}. Otherwise the new vowel should share the inherited vowel's
fronting. Ringe and Taylor formulate this as a relation between temporal
milestones: inherited-long fronting must be well under way before
contraction completes. They allow overlap; a serial implementation is not
proof that the changes occupied disjoint periods
[@Campbell1939, p. 90; @RingeTaylor2014, p. 170].

The inherited vowel itself is disputed. Fulk's retained-front reconstruction
does not require precisely the same earlier backing and re-fronting as
Ringe and Taylor's account. That is a disagreement about the input
inventory, not a small adjustment to the position of an otherwise identical
rule [@Fulk2018, pp. 60–61; @RingeTaylor2014, pp. 10–13].
Nielsen also proposes a different causal relation between contraction and
long-vowel restructuring, allowing co-occurrence rather than imposing the
conventional strict sequence [@Nielsen2001, pp. 514–516, 521].

Luick's proposed fronted-ai path is a further alternative, not an observed
intermediate series. His conjecture is \emph{*æe > *æə > *æa > *ā};
the middle offglide is schwa. Campbell rejects that explanation, but the
rejection is not an independent observation that such a phonetic path is
impossible [@Luick1914, pp. 132–133; @Campbell1939, p. 90, n. 3].
The inherited-long and secondary-long histories must consequently remain
separate even where later mutation makes their final vowels converge.

Nasal environments require another distinction. Nasalization, loss of a
nasal with compensatory lengthening, rounding and eventual merger are not
one event. The nasalized input can escape an oral-fronting law before its
later rounded outcome is established. A shared final vowel therefore does
not place every substep at the same ancestral node
[@Bremmer2009, pp. 24–27; @RingeTaylor2014, pp. 142–146].

The following table specifies the relevant inventory questions at a
conservative ancestral cut. It is a working reconstruction, not a newly
adjudicated full phoneme inventory. Earlier West Germanic developments can
be inherited at this cut without being exclusively Anglo-Frisian innovations.

| Input class | Conservative working ancestral state | English daughter consequence | Remaining premise |
|---|---|---|---|
| Inherited oral long vowel | Front long vowel under the conventional account | Subsequent dialectal and palatal treatment | Earlier back versus retained-front input |
| Nasal long vowel | Distinguished from the oral long vowel | Rounding and merger must be dated separately | Which nasal substeps precede the cut |
| Stressed ai | Retained diphthong before completed English contraction | Secondary back long vowel, eligible for later mutation | Runic interpretation and any limited ancestral onset |
| Ordinary short non-nasal a | Unfronted at this conservative cut | Ordinary English fronting | Daughter contraction before fronting |
| Inherited au | Not identified with completed English or Frisian outcome | English front element and later offglide development | Identity with ordinary short fronting |
| Supported inherited Vww classes | Adopted West Germanic a/e/i-ww reanalysis; separate homorganic uww quantity | Later English diphthong realization, not inherited English surface vowels | Qualified long-u shadow account; j-created classes remain separate |
| Velars and palatal tendencies | No blanket completed assibilation is stipulated | Class-specific daughter histories | Articulation, cutoff and merger are distinct |

The evidence underlying these qualifications is component-specific
[@RingeTaylor2014, pp. 41–42, 65–66, 170–173;
@Versloot2017, pp. 295–297, 318; @Laker2007, pp. 167–184].
The table does not assign inherited-short fronting to the stem merely
because the node is called Anglo-Frisian.

The inherited-glide component is now implemented rather than left as a
possible future decomposition.
[SC031 OEWWSimplification](#rule-OEWWSimplification) belongs to the earlier
West Germanic account discussed in Chapter 2: short nonhomorganic
\emph{*Vww} gives \emph{*Vuw}, with retained consonantal \emph{*w};
homorganic \emph{*uww} separately gives long \emph{*ūw}.
The latter follows Ringe and Taylor's preferred but qualified shadow
analysis. These earlier products can be inherited at the Anglo-Frisian
node without placing the later English long diphthongs there.
The selected sentence context for early apocope is independent of the
segmental reconstruction and of lexical accent
[@RingeTaylor2014, pp. 41--42, 55, 57--58, 65--66, 171--175;
@Fulk2018, p. 117].

## Alternative cuts and their tree consequences

A more expansive common-stem reconstruction is possible only with different
premises. In Luick's account, participation of the diphthong nucleus in
fronting can coexist with a conjectured later Frisian development.
In Goblirsch's account, a common fronted au diphthong precedes Frisian
stress shift and contraction. Both require historical intermediates whose
existence must be argued, not obtained from the name of the subgroup
[@Luick1914, pp. 130–133; @Goblirsch1991, pp. 17, 20–21].

| Proposed common-stem content | Required premise | Conditional consequence |
|---|---|---|
| Inherited-long restructuring, but retained ai and short a | Completed English contraction is later | Compatible conservative cut |
| Ordinary short fronting | Its secure predecessors can also occur before the split | Excluded if daughter-only English contraction obligatorily precedes it |
| Shared fronted-au development | Frisian stress shift/contraction follows that development | Compatible in Goblirsch's account, not proof of inheritance |
| Shared consonantal palatalization | Corresponding consonant classes and necessary predecessors are genuinely identical | Unresolved; apparent similarities do not settle all layers |

Campbell's English chain makes the second row especially consequential:
if completed contraction is English-only and ordinary fronting must follow
it, the latter cannot be inherited from the common stem. The corresponding
English and Frisian frontings are then parallel under those premises.
Changing a disputed premise can change that conclusion, but cannot remove
the required ancestor [@Campbell1939, pp. 90–91;
@Versloot2017, pp. 295–297, 318].

## Palatalization is not a single subgroup character

A palatal articulation can precede phonemic contrast, and the productive
cutoff of a conditioning process can precede its eventual assibilated
reflex. Fricative-g merger with j is different again. Geminate and
postnasal stops, singleton fricatives, k, h and sk must not be treated as
one dated change simply because later spellings look palatal
[@Hogg1979, pp. 100–111; @Laker2007, pp. 167–168, 175–184].

The shared-palatalization hypothesis must therefore identify which layer
is inherited. A daughter-specific predecessor can exclude a completed
component from the stem without excluding every earlier articulatory
tendency. Conversely, removing an argument against sharing establishes
compatibility, not that one common event actually occurred
[@Laker2007, pp. 175–184].
The vowel diphthongization following initial palatals is another event;
Luick explicitly distinguishes the similar Frisian and English outcomes
[@Luick1914, pp. 162–163].

The English implementation now distinguishes singleton palatal fricatives
from gg/ng stops and adopts postmutation fricative merger as a working
account [@RingeTaylor2014, pp. 203–204; @Fulk2018, pp. 130–132].
Hogg's objection remains explicit [@Hogg1979, pp. 102–111].
This daughter account does not select a complete ancestral inventory,
exclude every shared early articulatory tendency, or date stop affrication
from an eventual written reflex.

## What the runes date

An inscription dates a written object. A sound-change terminus additionally
requires the reading, etymology, linguistic affiliation and relation of the
grapheme to phonetic or phonemic structure. The interpretation of the
Caistor inscription as retaining ai and the interpretation of Frisian
retention are consequential but conditional
[@Versloot2017, pp. 295–297, 318].
Waxenberger likewise distinguishes early allophonic mutation from later
phonemicization and lacks immediate runic evidence for every short-vowel
split [@Waxenberger2019, pp. 63–74].

No one calendar date is therefore attached here to every change described
as Anglo-Frisian. The English discussion that follows starts from the
working inventory and makes its necessary daughter developments explicit.
Canonical classification, preferred reconstruction and an unresolved
component are kept distinct until individual adjudication.

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

### Word-final `*z` deletion (SC020) and the three final-`*z` developments

The loss of word-final `*z` is not one process but three historically
distinct developments, and this chapter contains two of them. The central
one, SC020, is the Proto-West Germanic loss of `*z` in unstressed syllables,
seen in forms such as [rástōz]{.recon .iv lang=pgmc sort=rastoz} 'rest
(nom.sg.)' and stated for the whole branch by Ringe and Taylor
[@RingeTaylor2014, pp. 44--45]; Crist's analysis distinguishes it both from
the earlier NWGmc changes and from the later narrower Ingvaeonic deletion
rules [@Crist2002, pp. 1, 4]. Earlier still, the consonant-stem root nouns
had generalized endingless nominatives before Proto-West Germanic (SC096,
Chapter 2). Later, and only in the north, `*z` was lost in stressed
monosyllables with compensatory lengthening (SC097, this chapter); the
southern dialects instead retained and rhotacized it. The standard handbooks
confirm the West Germanic deletion in general terms: Bammesberger gives a clean
statement that Germanic `*z` is generally lost in final position
[@Bammesberger1992, p. 39]; the three-way division refines those summaries rather
than contradicting them.

The CAPR rule for the unstressed loss is still named `EAFFinalZDeletion`,
an identifier that predates the restaging of the change to Proto-West
Germanic; the name is retained as a stable identifier pending a global
renaming pass, and the historical stage recorded in the staging metadata
takes priority over the name prefix. SC020 remains presented in this
chapter, beside rhotacism, because the two changes jointly determine the
fate of every remaining `*z`.

### Completed English ai contraction (SC004, treated in Chapter 4)

The English outcome of stressed/root \emph{*ai} is \emph{*ā}. Versloot
distinguishes an early velar-conditioned Frisian contraction from later
non-velar treatment, with mutation and delabialization intervening
[@Versloot2017, pp. 302--309, 316]. His wave account is an author's
interpretation, not CAPR's own genealogy. CAPR now places completed English
contraction on the daughter branch, while preserving the distinct possibility
of a narrower conditioned ancestral onset
[@Campbell1939, pp. 90–91; @Versloot2017, pp. 295–297, 318].
This local decision does not select every component of the ancestral inventory.

The current [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization)
models English contraction after
[SC101 EAFLongAFronting](#rule-EAFLongAFronting). The new ai-derived
\emph{*ā} escaped the earlier fronting of inherited oral \emph{*ā};
Campbell states that inference and Ringe and Taylor retain it
[@Campbell1959, pp. 52--53, §132; @RingeTaylor2014, pp. 169--170].
Soul provides another implementation boundary at interstress raising, not
the sole historical argument or proof of inherited contraction.

The unstressed development `*ai > *ē` (in final and nonfinal syllables) is a
separate and earlier Proto-Northwest Germanic change (SC014), discussed in
Chapter 2; its corpus witnesses are the dative-singular endings of `span`
([spánnai]{.recon} 'span' > *spanne* 'span') and `meed` ([mízdai]{.recon}
'meed' > *meorde* 'meed').

### Anglo-Frisian brightening (SC043, treated in Chapter 4)

The fronting of low \emph{*a} to \emph{*æ} outside nasal environments is
traditionally called Anglo-Frisian brightening. The name does not establish
one inherited event. It executes later in the cascade than the changes of
this chapter, so its full section appears in Chapter 4; it is introduced here
because it anchors the "Anglo-Frisian" label that names this period. Campbell
gives the classical statement: "By a very early change Prim. Gmc. `a > æ` in
OE and OFris. when not followed by a nasal consonant"
[@Campbell1959, p. 52, §131].
The traditional name also appears in modern comparative treatments; it
does not independently establish a shared event [@Fulk2018, pp. 72–73].

The change is notable for what follows it: OE Breaking presupposes the fronted
input; OE a-Restoration partially undoes it in back-vowel environments. The
three-change sequence is the conventional English working account, but its
components and conditioning remain individually arguable. Versloot proposes
restricted early fronting and late e-breaking; final forms can coincide under
front-and-restore and never-front histories
[@Versloot2025, pp. 123, 125--128, 131--135].

Campbell notes that English and Frisian may not simply reflect one
undifferentiated shared prehistoric event, and Ringe and Taylor leave open
whether the wider spread of fronted outcomes happened mainly on the continent
or in Britain [@RingeTaylor2014, pp. 60--62]. CAPR's implementation treats the
stressed English component separately from the retained unstressed and
final-vowel representations.

The completed ordinary stressed component is now characterized on the
English daughter under Campbell's conventional working chain
[@Campbell1939, pp. 90--91; @Campbell1959, pp. 52--53].
Ringe and Taylor's diphthong-nucleus objection remains explicit
[@RingeTaylor2014, pp. 170--175]; earlier restricted ancestral tendencies
are not excluded. English plain-a/au process identity is distinct from
inherited stem identity, and their current serialization is retained.
The unstressed and final-vowel contributions are not assigned the same
date from this argument. This local adoption does not select the complete
ancestral inventory.

## Cascade vs. historical order in this chapter

The sections follow executable serialization so that derivations are inspectable.
That order is not an independently demonstrated total historical chronology.
The broader final-z loss, later northern loss and rhotacism are distinguished
by their actual environments [@RingeTaylor2014, pp. 44--45;
@Crist2002, pp. 1, 4].

Earlier-stage proxies remain in this editorial corridor. The cluster change
represented by [SC022 PNWGmcMnDissimilation](#rule-PNWGmcMnDissimilation)
and final-n loss represented by
[SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss) are classified as
Common Germanic/Proto-Germanic despite retained name prefixes
[@Fulk2018, p. 121; @Ringe2017, pp. 101--103].
The retired unstressed-o raising is not an active member. Book order,
computational position and historical stage must remain separate.

# West Germanic final \emph{*z}-deletion

## Historical discussion

Word-final \emph{*z} in unstressed syllables was lost in Proto-West Germanic. Ringe and Taylor state the change for the whole branch and illustrate it with the nominative plural \emph{*dagōz} > \emph{*dagō} and the consonant-stem nominative \emph{*fadurz} > \emph{*fadur}, noting that the ending is lost after consonants as well as after vowels [@RingeTaylor2014, pp. 44--45, §3.1.1]. Crist's handout formulates the same development and its Ingvaeonic sequels [@Crist2002, p. 2, §§5--6]. The change is pan-West-Germanic, not specifically Ingvaeonic: every West Germanic daughter shows the loss, and the Frienstedt comb inscription \emph{kaba} < \emph{*kambaz} 'comb' (c. 250--300 CE) supplies early epigraphic confirmation [@Fulk2018, p. 25, n. 1].

The conditioning segment is specifically the voiced sibilant \emph{*z}, never \emph{*s}: Ringe and Taylor's near-minimal pair of nominative singular \emph{*dagaz} > \emph{*dag} beside genitive singular \emph{*dagas}, which keeps its sibilant into Old English \emph{dæġes}, shows that the change reads the Verner voicing distinction [@RingeTaylor2014, p. 212, §6.1]. Where the handbooks disagree about whether a given ending had \emph{*-s} or \emph{*-z} — as for the nominative plural \emph{*-ōz} — the disagreement matters directly to whether this rule applies [@RingeTaylor2014, pp. 115--116, §4.2.1].

This is the middle of three historically distinct final-\emph{*z} developments, and Ringe and Taylor explicitly separate it from the later loss in stressed monosyllables, citing Crist's demonstration that they are two changes [@RingeTaylor2014, pp. 44--45, §3.1.1]. Earlier, the consonant-stem (root-noun) nominatives of monosyllables had already generalized endinglessness before Proto-West Germanic ([SC096 RootNounNomZLoss](#rule-RootNounNomZLoss)), so forms like \emph{*bōkz} 'book' never reach this rule with their marker intact. Later, and only in the north, \emph{*z} was lost in stressed monosyllables with compensatory lengthening ([SC097 MonosyllabicFinalZLoss](#rule-MonosyllabicFinalZLoss)); the present rule leaves stressed monosyllables untouched. Older accounts that grouped all of these under one loss of final \emph{*z}, such as Campbell's, are superseded by this three-way division [@Campbell1959, p. 166].

At the boundary with Chapter 2's Northwest Germanic sequence, the derivation of *ræste* 'rest' shows that final \emph{*ō}-raising ([SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising)) must precede this rule: raising applies to \emph{*-ō} but not to \emph{*-ōz}, whose final vowel is still sheltered by the sibilant when raising runs [@RingeTaylor2014, pp. 15--16, 24]. On the later side, Ringe and Taylor order the loss of \emph{*z} before the loss of word-final bare \emph{*-a}, since \emph{*dagaz} first becomes \emph{*daga} and only then \emph{*dag} [@RingeTaylor2014, pp. 45--46, §3.1.2].

## SC020. West Germanic final \emph{*z}-deletion (`EAFFinalZDeletion`) {#rule-EAFFinalZDeletion}

```foma
define EAFFinalZDeletion Ctx([{*z} -> 0 ||
    .#. ?* EnglishStarVocalic
        [EnglishStarConsonant | EnglishPalatalConsonant]+
        EnglishStarVocalic ?* _ .#.,
    .#. [EnglishStarConsonant | EnglishPalatalConsonant]*
        EnglishStarVocalic+
        [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.]);
```

The rule deletes word-final \emph{*z} in unstressed syllables, stated through two environments. The first clause covers polysyllables, where the final syllable of these corpus forms is unstressed: this is the ordinary case, with 110 corpus derivations, such as PGmc [bárdaz]{.recon} 'beard' on its way to OE *beard* 'beard' and [rástōz]{.recon} 'rest' on its way to *ræste* 'rest'. The second clause covers post-consonantal \emph{*z} in monosyllables. By the time this rule runs, [SC096 RootNounNomZLoss](#rule-RootNounNomZLoss) has already removed the genuine root-noun nominative endings, so the only form reaching the second clause is [fríjōndz]{.recon} 'friend', contracted to monosyllabic \emph{*fríundz} by [SC009 PWGmcIjContraction](#rule-PWGmcIjContraction); its ending, like that of \emph{*fadurz}, stood in an unstressed syllable when the Proto-West Germanic change applied and so belongs here rather than to the root-noun development [@RingeTaylor2014, pp. 44--45, §3.1.1]. Stressed monosyllables ending in vowel plus \emph{*z} meet neither clause and are left for [SC097 MonosyllabicFinalZLoss](#rule-MonosyllabicFinalZLoss).

The chronology of word-final \emph{*z}-loss is unusually well delimited: *ræste* 'rest' supplies its early boundary, while later weak syllables supply its late boundary.

Before [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising), PGmc [rástōz]{.recon} 'rest' yields [*rast*]{.pred} rather than expected OE *ræste* 'rest'. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc [bébruz]{.recon} 'beaver' yields [*befro*]{.pred} rather than expected *befer* 'beaver', PGmc [kwéðuz]{.recon} 'cud' yields [*cwedo*]{.pred} rather than expected *cwedu* 'cud', and PGmc [félθuz]{.recon} 'field' yields [*feldo*]{.pred} rather than expected *feld* 'field', alongside eight other newly failing rows. Final \emph{z}-loss therefore follows [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising) and precedes [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The [rástōz]{.recon} 'rest' derivation fixes the local relation to [SC019 PNWGmcFinalLongORaising](#rule-PNWGmcFinalLongORaising). The distant boundary at [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) shows only that word-final \emph{*z}-loss precedes the later weak-syllable sequence; its placement within that wider interval follows the handbook chronology after final \emph{*ō}-raising.

\newpage

# Early apocope in unstressed words

## Historical discussion

Alongside the regular loss of word-final short high vowels in third syllables ([SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope)), Ringe and Taylor identify a second, earlier apocope: "Short high vowels were also lost after heavy syllables in unstressed words" [@RingeTaylor2014, pp. 57--58, §3.1.4]. The two laws must not be conflated. Fully stressed disyllables kept their final \emph{*-i} long enough to cause i-umlaut — OE *ġiest* 'guest' < \emph{*gastiz} and *fȳr* 'fire' < \emph{*fūri} require exactly that survival [@RingeTaylor2014, p. 55, §3.1.4] — whereas words that carried no sentence stress lost the vowel already in Proto-West Germanic.

The conditioning is prosodic. Like Verner's law, the change is governed by accent: it applied in words unstressed in the sentence, and its apparent exceptions are systematic, not sporadic. Forms such as OE *ymbe* 'around' and OHG \emph{umbi} kept their final vowel because, as Ringe and Taylor observe, proclitics "were not phonologically word-final" and so stood outside the environment altogether [@RingeTaylor2014, pp. 57--58, §3.1.4]. Sentence-level accent placement therefore decides which sandhi variant each daughter language continues, and doublets across the family reflect the stressed and unstressed sentence forms of the same word — regular sandhi, not lexical diffusion.

The diagnostic witness is the second-person plural pronoun. Ringe and Taylor print the Proto-West Germanic form as a doublet: PGmc \emph{*izwiz} (Gothic \emph{izwis}) → \emph{*iwwi} (by [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) and the loss of final \emph{*z}, [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion)) → PWGmc \emph{*iuwi} ~ \emph{*iuw} [@RingeTaylor2014, pp. 41--42, §3.1.1]. Old English continues the apocopated, unstressed variant, and Ringe and Taylor's proof is the vocalism itself: "OE iow 'you (dat. pl.)' definitely does [show early apocope] (since it does not exhibit i-umlaut)" [@RingeTaylor2014, pp. 57--58, §3.1.4]. Had the \emph{*-i} survived, i-umlaut ([SC055 OEIUmlaut](#rule-OEIUmlaut)) would have fronted the diphthong; West Saxon *ēow* 'you' beside early West Saxon and Northumbrian *īow* 'you' shows the normal unumlauted development [@Campbell1959, §702, p. 283].

## \CAPRRuleHeading{SC098. Early apocope in unstressed words}{PWGmcUnstressedWordFinalIApocope} {#rule-PWGmcUnstressedWordFinalIApocope}

```foma
define PWGmcUnstressedWordFinalIApocope [
    [ [{*i}|{*u}] -> 0 || .#. {*ᵘ} ?* [
        [EnglishStarLongVowel | EnglishStarLongDiphthong] EnglishStarConsonant*
        | EnglishStarShortVowel EnglishStarConsonant EnglishStarConsonant+
    ] _ .#. ]
    .o. [{*ᵘ} -> 0]
    .o. [
        [{*ᶜ}:0 [EnglishStarAlphabet - {*ᶜ}]* 0:{*ᶜ}]
        | [EnglishStarAlphabet - {*ᶜ}]*
    ]
];
```

Sentence stress and phonological finality are now explicit, independently
selected context. They do not alter the PGmc reconstruction, the selected
segmental input or its historical stage. The computational marks in the
rule distinguish weak-final context from weak-nonfinal context; they are
not reconstructed phonemes and are absent from displayed forms. Ordinary
evaluation explicitly chooses strong-final citation context. You selects
the independently source-discussed weak-final variant, not an unstressed
classification inferred from a pronoun label or missing acute.

The worked history is \emph{*izwiz} → \emph{*iwwiz} by assimilation →
\emph{*iuwiz} by [SC031 OEWWSimplification](#rule-OEWWSimplification) →
\emph{*iuwi} by final \emph{z}-loss → weak-final \emph{*iuw} by this
rule → OE *ēow*. The operation requires a heavy syllable and a
phonologically final short high vowel: long vowel/diphthong weight or a
short vowel followed by a closing consonant cluster, not literal
\emph{ww}. Its condition therefore survives glide reanalysis.
Loss of final \emph{z} still feeds it, and removal of \emph{i} bleeds
[SC055 OEIUmlaut](#rule-OEIUmlaut). Its PWGmc placement precedes the
later northern loss of stressed-monosyllabic final \emph{z}
([SC097 MonosyllabicFinalZLoss](#rule-MonosyllabicFinalZLoss))
([@RingeTaylor2014, pp. 41--42, 55, 57--58]).

The staged strong contexts retain the high vowel in the histories of
*ġiest* 'guest' and *fȳr* 'fire'. A weak-final and context yields *and* 'and', whereas
the proposed proclitic context retains the vowel in *ymbe* through the
later apocope corridor. The right-boundary annotation is removed only
after [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope) has had the
opportunity to apply. These controls implement the defended exceptionless
account; they do not claim direct observation of prehistoric sentence
stress or lexical optionality ([@RingeTaylor2014, pp. 55, 57--58]).

The corresponding English realization of \emph{iu+w} belongs to
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), not a late
vocalization of retained \emph{ww}. The model's retained-i counterfactual
produces an umlauted result after intervening w-loss; its exact terminal
spelling is a computational prediction, not an attested strong OE form.
The attested weak-final target and the source's mutation argument must
not be replaced by that counterfactual
([@RingeTaylor2014, pp. 41--42, 57--58, 173--175;
@Campbell1959, p. 283]).

\newpage

# Northern monosyllabic final \emph{*z}-loss

## Historical discussion

Long after the Proto-West Germanic loss of final \emph{*z} in unstressed syllables ([SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion)), the northern West Germanic dialects lost word-final \emph{*z} in stressed monosyllables as well, with compensatory lengthening of a short nucleus. Ringe and Taylor's witness set is OE *mā* 'more' < \emph{*maiz}, the pronouns *wē* 'we', *ġē* 'you', *mē* 'me', *þē* 'thee', *hē* 'he', *hwā* 'who' < \emph{*hwaz}, and — hedged in their own print with question marks — *cū* 'cow' [@RingeTaylor2014, p. 86, §3.3.1]. The southern dialects retained the sibilant and rhotacized it: Old High German \emph{mir}, \emph{wir}, \emph{mēr}, \emph{er} answer the Old English endingless forms, which is why Fulk counts this loss among the diagnostic Ingvaeonic features [@Fulk2018, p. 18, n. 6]. Ringe and Taylor explicitly treat this as a change separate from the Proto-West Germanic unstressed loss, citing Crist's demonstration that the two must be distinguished [@RingeTaylor2014, pp. 44--45, §3.1.1].

The scholarship disagrees about the exact conditioning, and the disagreement is worth recording. An older account, represented by Campbell and going back to Luick, derived the endingless pronouns from unaccented sentence variants rather than from a regular sound change [@Campbell1959, p. 166; @Luick1914, p. 819]. Ringe and Taylor reject that analysis because *mā* 'more' and *cū* 'cow' are not plausibly unaccented words [@RingeTaylor2014, p. 86, §3.3.1]. Crist formulates an Ingvaeonic rule in which \emph{*z} is lost after front vowels, with compensatory lengthening, covering preconsonantal cases as well; his data contain no word-final back-vowel monosyllables, so forms like \emph{*hwaz} and the ancestor of *cū* fall outside what his statement can decide — a documented gap rather than a refutation [@Crist2002, pp. 1, 4, §§1, 10]. Kilday narrows the preconsonantal subcase to Old Saxon and Old Frisian while accepting the word-final monosyllabic loss for Old English, contrasting regular *meord* 'reward' with the loanword-influenced *mēd* 'reward' [@Kilday2024, pp. 1--3]. CAPR adopts Ringe and Taylor's quality-neutral formulation because it alone generates the back-vowel witnesses, while noting that the front-vowel forms are compatible with both analyses.

Apparent counterexamples are analogical, not phonological: OE *dēor* 'deer', *ār* 'oar', and *gār* 'spear' show final \emph{-r} from levelling out of inflected forms where the sibilant was word-internal and regularly rhotacized, not from retention of word-final \emph{*z} [@RingeTaylor2014, p. 86, §3.3.1, n. 24]. The change precedes rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)), which Ringe and Taylor place last in this sequence of northern developments [@RingeTaylor2014, p. 87, §3.3.1].

The corpus now witnesses this change directly. The interrogative pronoun 'who' is selected in its nominative singular masculine cell, PGmc \emph{*hwaz} (Gothic \emph{hwas}), precisely the form Ringe and Taylor cite for this loss [@RingeTaylor2014, p. 86, §3.3.1]: the rule lengthens the short nucleus and deletes the sibilant, giving \emph{*hwā}, whence OE *hwā* 'who'. The resulting back vowel never undergoes Anglo-Frisian brightening — "\emph{*hwǣ} does not exist", as Campbell puts it [@Campbell1959, §125, p. 49; @SieversBrunner1965, §137 Anm. 1, p. 129] — so the derivation ends with the attested form. Other members of Ringe and Taylor's witness set remain outside the corpus because it selects oblique or plural cells for them — 'cow' and 'meed', for instance, enter the cascade in inflected forms whose \emph{*z}, where present, is word-internal.

## \CAPRRuleHeading{SC097. Northern monosyllabic final \emph{*z}-loss}{MonosyllabicFinalZLoss} {#rule-MonosyllabicFinalZLoss}

```foma
define MonosyllabicFinalZLoss [
    {*a} -> {*ā}, {*á} -> {*ā},
    {*e} -> {*ē}, {*é} -> {*ḗ},
    {*i} -> {*ī}, {*í} -> {*ḯ},
    {*o} -> {*ō}, {*ó} -> {*ō},
    {*u} -> {*ū}, {*ú} -> {*ū}
        || .#. [EnglishStarConsonant | EnglishPalatalConsonant]*
            _ {*z} .#.
] .o. [
    {*z} -> 0 ||
        .#. [EnglishStarConsonant | EnglishPalatalConsonant]*
            EnglishStarVocalic+ _ .#.
];
```

The rule first lengthens a short nucleus standing immediately before word-final \emph{*z} in a monosyllable, then deletes the \emph{*z} after any vowel in a monosyllable. The principal synthetic controls run the change on Ringe and Taylor's own witnesses, fed to the rule in their chronologically correct intermediate shapes. Short-nucleus inputs show both halves of the change at once: \emph{*hwaz} yields \emph{*hwā} and \emph{*hiz} yields \emph{*hī}, each with loss of the sibilant and compensatory lengthening [@RingeTaylor2014, p. 86, §3.3.1]. A form whose nucleus is already bimoric skips the lengthening step and simply loses the sibilant: \emph{*maiz} yields \emph{*mai} at this stage, with its diphthong intact; the attested OE *mā* 'more' arises only later, when the stressed monophthongization ([SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization)) takes \emph{*ai} to \emph{*ā}. The word 'cow', whose history Ringe and Taylor themselves print with question marks and whose analysis remains disputed, is deliberately not used as a principal control; a long-vowel input of that shape (\emph{*kūz} yielding \emph{*kū}) merely repeats what \emph{*maiz} already demonstrates, and the word's evidentiary weight is discussed in the historical dossier rather than leaned on here.

The corpus derivation of *hwā* 'who' now fixes this rule's position empirically as well as philologically. It stands after [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion), since the two losses are historically distinct changes with the unstressed loss earlier [@RingeTaylor2014, pp. 44--45, §3.1.1]. Rhotacism ([SC003 EAFRhotacism](#rule-EAFRhotacism)) follows in the executable cascade as in the historical account: Ringe and Taylor place rhotacism after this loss, at the end of the sequence of \emph{*z}-losses [@RingeTaylor2014, p. 87, §3.3.1], and the cascade composes it immediately after this rule, so a sibilant removed here can never surface as \emph{-r} — were the order reversed, \emph{*hwaz} would rhotacize to \emph{*hwar} and 'who' could never be derived; the negative controls below confirm this. Consonant-final monosyllables are untouched: their nominative \emph{*-z}, where it ever existed, was eliminated before Proto-West Germanic under [SC096 RootNounNomZLoss](#rule-RootNounNomZLoss). Word-internal \emph{*z}, as in PGmc [déuzą]{.recon} 'deer' on its way to OE *dēor* 'deer', does not meet the environment of this rule and duly rhotacizes.

\newpage

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

\newpage

# \emph{mn}-dissimilation

## Historical discussion

In the inherited \emph{n}-stem paradigm the zero-grade oblique cells brought
\emph{m} and \emph{n} into direct contact, and in that adjacent cluster the
labial nasal dissimilated to a labial spirant: \emph{mn} > \emph{βn} (surfacing
as \emph{fn}). Old Norse preserves the older paradigmatic distribution, with the
labial confined to the oblique cluster (\emph{himinn} 'heaven' beside dative
\emph{hifni}); Old English and Old Saxon generalized it. Fulk treats the cluster
change among developments common to Germanic, while warning that its surface
results are irregular and that reverse \emph{bn} > \emph{mn} is later well
attested in Northwest Germanic [@Fulk2018, p. 121, §6.11]. The relevant
\emph{heofon} 'heaven' and \emph{mōnaþ} 'month' material is discussed by Campbell
[@Campbell1959, pp. 189, 195, §§470, 484].

The underlying cluster change is therefore late Proto-Germanic / Common
Germanic, not securely a pan-Northwest-Germanic innovation; `PNWGmc` remains a
stable executable identifier only. The lexical evidence does not constrain a
positive local cascade position.

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

## \CAPRRuleHeading{SC026. North Sea Germanic nasal-spirant law, first step}{EAFNasalSpirantLengthening} {#rule-EAFNasalSpirantLengthening}

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

## \CAPRRuleHeading{SC027. North Sea Germanic nasal-spirant law, second step}{EAFNasalSpirantLoss} {#rule-EAFNasalSpirantLoss}

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

\newpage

# The hiatus-breaking \emph{w} of the verba pura

## Historical discussion

The small class of Germanic strong verbs whose roots ended in a vowel, the \emph{verba pura}, reached Northwest Germanic with a morphologically expected hiatus. Ringe and Taylor reconstruct Proto-Germanic \emph{*sēaną} 'to sow' (Gothic *saian*), which the Northwest Germanic lowering of \emph{*ē₁} carried to \emph{*sāaną}; the West Germanic languages then "exhibit innovative consonants that eliminated" the hiatus [@RingeTaylor2014, p. 12]. The repair differs by branch, and the difference dates and localizes the change. Old English and Old Frisian inserted \emph{w}, as in Old English *sāwan* 'to sow' and Old Frisian *sāwinge* 'sowing' beside *grōwinge* 'growth', while Old Saxon and Old High German used \emph{j} (*sāian* 'to sow', *sāen* 'to sow', *sājen* 'to sow') [@RingeTaylor2014, pp. 12, 151]. The insertion of \emph{w} is therefore an Anglo-Frisian development and the consonant of *sāwan* is not inherited; it must not be projected back into the protoform.

The origin of that \emph{w} is neither inherited nor morphological. Þórhallsdóttir, in the standard treatment of the problem, rejects in turn the derivation of the West Germanic \emph{w} from a Proto-Indo-European \emph{u}-perfect [@Thorhallsdottir1993, pp. 115--117], from a \emph{*ue/o}-present [@Thorhallsdottir1993, pp. 117--119], and from the transfer of a preterite \emph{w} into the present [@Thorhallsdottir1993, pp. 121--122]. The \emph{w} "rather has an inner-Germanic phonological explanation" [@Thorhallsdottir1993, p. 136]. It began as an ordinary phonetic glide filling the hiatus, and it began in one narrow environment, before \emph{*u}. The cells in question, as Bremer had already seen, are the first singular and first plural of the present indicative together with the plural of the reduplicated preterite in \emph{*-um}, \emph{*-uþ}, \emph{*-un} [@Thorhallsdottir1993, p. 120]. Þórhallsdóttir sets out the pre-Old English present indicative with the hiatus still intact, first singular \emph{*sā'u}, second \emph{*sā'is}, third \emph{*sā'iþ}, first plural \emph{*sā'um}, second plural \emph{*sā'iþ}, third plural \emph{*sā'anþ}, and observes that "the glide \emph{w} was a natural hiatus filler before the \emph{u} of the endings of the 1st person singular and plural" [@Thorhallsdottir1993, p. 127]. The preterite stem \emph{*seuwun} arose by the same insertion before the \emph{*u} of the plural endings [@Thorhallsdottir1993, p. 126].

From those few cells the \emph{w} was carried through the whole paradigm by analogy. Three forces converge. Levelling proceeded out of the \emph{*u}-cells themselves; the preterite stem \emph{*seuw}, \emph{*seuwun} "would have assisted in extending the new \emph{w} to all forms of the present paradigm" and to the preterite participle; and verbs with an etymological \emph{*w}, above all *flōwan* 'to flow' from the root \emph{*pleu-}, exerted their own attraction [@Thorhallsdottir1993, p. 127]. The result, complete already in pre-Old English, is the uniform pattern \emph{*sāwan}, \emph{*seuw}, \emph{*seuwun}, \emph{*sāwan-} [@Thorhallsdottir1993, p. 136]. Old Frisian inherits the same generalized type, so that its \emph{w} and the Old English \emph{w} are one Anglo-Frisian event [@Thorhallsdottir1993, pp. 130, 134]. The scattered \emph{w}-forms of Old High German are a separate and later inner-German development and are not to be identified with it [@Thorhallsdottir1993, pp. 119, 123].

This layering matters for how the rule below should be read. Old English citation forms are infinitives, and the infinitive \emph{*sā'an} is precisely one of the cells that never received \emph{w} by the phonological rule, so the \emph{w} of *sāwan* 'to sow' is analogical. The rule therefore models the outcome of the generalization, and its environment, any vowel after \emph{ā}, is a citation-form proxy for a paradigm-wide result. It is not a reconstruction of the conditioning of the original insertion.

The chronology is fixed on both sides by Ringe and Taylor. The \emph{w} must postdate the West Germanic loss of intervocalic \emph{*w}, or the new glide would itself have been swept away [@RingeTaylor2014, p. 151, n. 9]; and it "must have occurred early enough to prevent fronting of \emph{*ā}" in pre-Old English [@RingeTaylor2014, p. 151]. The whole reason *sāwan* 'to sow', *cnāwan* 'to know', *blāwan* 'to blow', and *māwan* 'to mow' keep their back vowel is that the \emph{w} was already in place when the North Sea Germanic fronting applied. Since it is the generalized \emph{w} that stands in the infinitive, this later boundary constrains the generalization itself. The rule accordingly stands before the fronting in the cascade, even though on the present corpus the two orders happen to produce the same outputs, since the fronting rule as implemented does not touch a prevocalic \emph{ā} in any case; the ordering encodes the historical chronology, and no corpus-internal contrast demonstrates it. That chronology rests on Ringe and Taylor alone, for Þórhallsdóttir's chapter nowhere discusses the fronting of \emph{*ā} and supplies no independent evidence for the order.

## \CAPRRuleHeading{SC102. Generalized hiatus-breaking \emph{w} after long \emph{ā}}{EAFHiatusWInsertion} {#rule-EAFHiatusWInsertion}

```foma
define EAFHiatusWInsertion [
    [..] -> {*w} || {*ā} _ EnglishStarVocalic
];
```

The rule is fed by [SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering), which creates the \emph{ā}-initial hiatus it repairs; [sḗaną]{.recon} 'to sow' passes through \emph{*sāaną} to \emph{*sāwaną} on its way to *sāwan* 'to sow'. Displaced before the lowering, the rule can never apply, since the root vowel is still \emph{*ē} and no hiatus after \emph{ā} exists, and the derivation loses its consonant altogether.

Its output in turn feeds the blocking environment of [SC101 EAFLongAFronting](#rule-EAFLongAFronting): the inserted \emph{w} is precisely what shields the \emph{ā} of *sāwan* 'to sow' from fronting, as treated in that chapter. The corpus carries *sāwan* as the diagnostic witness of the class; *cnāwan* 'to know', *blāwan* 'to blow', *māwan* 'to mow', *wāwan* 'to blow (of wind)', and *þrāwan* 'to turn' instantiate the same derivation [@RingeTaylor2014, p. 151].

\newpage

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

## \CAPRRuleHeading{SC025. Nasalization of long \emph{ā} before nasals}{EAFLongANasalRounding} {#rule-EAFLongANasalRounding}

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

\newpage

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

## \CAPRRuleHeading{SC104. Rounding of the long nasalized low vowel}{EAFNasalizedLowRounding} {#rule-EAFNasalizedLowRounding}

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

\newpage

# North Sea Germanic fronting of long \emph{ā}

## Historical discussion

Long after the Northwest Germanic lowering of \emph{*ē₁} to \emph{*ā}, the dialects of the North Sea coast fronted the surviving oral \emph{*ā} to a low front vowel: West Saxon \emph{ǣ} in *dǣd* 'deed', *slǣpan* 'to sleep', *lǣtan* 'to let', *rǣdan* 'to read', and *mǣl* 'meal', against Anglian, Kentish, and Old Frisian \emph{ē} (*dēd* 'deed', *slēpa* 'to sleep', *jēr* 'year') [@RingeTaylor2014, pp. 146--150; @Campbell1959, pp. 50--51, §128]. Old Saxon and Old High German keep the back vowel (Old Saxon *dād* 'deed', Old High German *tāt* 'deed', *slāfan* 'to sleep', *lāzan* 'to let'), but sporadic Old Saxon spellings in ⟨e⟩ show that the fronting lapped unevenly into Old Saxon territory [@RingeTaylor2014, p. 150]. The change is therefore a North Sea Germanic development rather than an exclusively Anglo-Frisian one, though only Old English and Old Frisian carry it through systematically.

The fronting affected stressed, non-nasalized \emph{*ā}; nasalized \emph{*ą̄} was instead rounded, as treated in the rounding chapter. Ringe and Taylor further establish a conditioning by a following \emph{*w}. Before \emph{*w} plus a back or non-high vowel the \emph{*ā} was retained: the clearest witnesses are the *verba pura* — *sāwan* 'to sow', *cnāwan* 'to know', *blāwan* 'to blow', *māwan* 'to mow', *þrāwan* 'to turn' — together with *clāwu* 'claw' [@RingeTaylor2014, p. 151]; the simplest hypothesis, which Ringe and Taylor adopt from Hogg, is that fronting never occurred in that environment [@RingeTaylor2014, p. 151; @HoggGrammar1992, p. 81]. Before \emph{*w} plus a high front vocalic, by contrast, the fronting did apply: \emph{*lēwijaną} 'to betray' (Gothic *lēwjan* 'to betray', Old High German *gilāen* 'to betray') yields West Saxon *lǣwan* 'to betray', and the same environment appears in *eltǣwe* 'entire' and *brǣw* 'eyelid' [@RingeTaylor2014, p. 150]. Both sides of the condition are encoded in the rule below and witnessed in the corpus. Bennett states the retaining environment independently from the West Saxon evidence alone, and slightly more broadly: West Saxon "shows \emph{ǣ} as a regular isolative development of IE \emph{ē} but has \emph{ā} before \emph{w} or \emph{g} plus a back vowel", with the paradigmatic alternation *wǣg* 'wave' beside plural *wāgas* 'waves' [@Bennett1950, p. 235, n. 6]. The rule below encodes the \emph{w} environment, for which the corpus supplies witnesses on both sides; the parallel \emph{g} environment is left for separate treatment.

Whether this fronting restored a front vowel that had earlier been backed, or whether — as Fulk argues — the North Sea dialects simply retained an old front \emph{*ǣ} that was never backed at all, is the same dispute recorded in the lowering chapter [@Fulk2018, pp. 60--61, §4.6; @Campbell1959, pp. 50--51, §§128--129]. On the retention analysis this chapter's change dissolves into the non-event of staying put; the present model follows Ringe and Taylor's two-step reconstruction, on the strength of the runic evidence for an early [aː] and the place-adverbs *þǣr* 'there' and *hwǣr* 'where' [@RingeTaylor2014, pp. 13--14].

## \CAPRRuleHeading{SC101. Fronting of long \emph{ā} outside nasal and \emph{w} environments}{EAFLongAFronting} {#rule-EAFLongAFronting}

```foma
define EAFLongAFronting [
    {*ā} -> {*ǣ} || _ [EnglishStarConsonant - EnglishStarNasal - {*w}],
    {*ā} -> {*ǣ} || _ {*w} EnglishIUmlautTrigger
];
```

The first clause fronts \emph{*ā} before any oral consonant other than \emph{*w}; the second admits the fronting before \emph{*w} exactly when a high front vocalic follows. The two corpus witnesses of the \emph{w} condition form a minimal contrast. [sḗaną]{.recon} 'to sow', whose hiatus-filling \emph{w} is supplied by [SC102 EAFHiatusWInsertion](#rule-EAFHiatusWInsertion), reaches this rule as \emph{*sāwaną} and is left unfronted, surfacing as *sāwan* 'to sow'; were the \emph{w}-block removed, the cascade would deliver [*sǣwan*]{.pred} instead. [lḗwijaną]{.recon} 'to betray', whose inherited \emph{w} is followed by \emph{*i}, is fronted by the second clause to \emph{*lǣwijaną} at this rule's own stage — before, and independently of, the much later i-umlaut — and surfaces as *lǣwan* 'to betray'.
The rule consumes the \emph{*ā} created by [SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering); displaced before the lowering, it has nothing to front, and [skḗpą]{.recon} 'sheep' surfaces as [*sċāp*]{.pred} rather than OE *sċēap* 'sheep', [jḗrą]{.recon} 'year' as [*ġār*]{.pred} rather than *ġēar* 'year', [slḗpaną]{.recon} 'to sleep' as [*slāpan*]{.pred} rather than *slǣpan* 'to sleep'.

Two later boundaries carry real historical content. First, the fronting must precede the completion of [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization): the \emph{ā} that arose from \emph{*ai} was never fronted — *stān* 'stone', *hām* 'home', *lāþ* 'hostile', *rāp* 'rope', *tācn* 'token', *gāst* 'spirit' all keep the back vowel. Campbell draws exactly this chronological inference [@Campbell1959, pp. 52--53, §132], and Ringe and Taylor endorse it as cogent [@RingeTaylor2014, pp. 169--170]; in the present cascade the inference is enforced by rule order, and displacing the fronting after the monophthongization wrongly yields [*lǣþ*]{.pred}, [*rǣp*]{.pred}, [*tǣcn*]{.pred}, [*sǣwol*]{.pred}, and [*ġēast*]{.pred}. Historically the two changes may well have overlapped in time; the discrete ordering is the grammar's way of stating that inherited \emph{ā} had been fronted before the new \emph{ā} arose.

Second, the fronting must precede [SC056 OEWsPalatalDiphthongization](#rule-OEWsPalatalDiphthongization), which operated on the already-fronted vowel: \emph{ǣ} > \emph{ēa} after the palatals, as in *sċēap* 'sheep' and *ġēar* 'year' [@Campbell1959, pp. 69--70, §185; @RingeTaylor2014, pp. 215--216, §6.5.1]. Displaced after the diphthongization, the cascade yields [*sċǣp*]{.pred} and [*ġǣr*]{.pred} instead.

\newpage

# Chapter 4. From Anglo-Frisian to Old English


## Historical interval

This chapter follows the English daughter from the required Anglo-Frisian
ancestor through prehistoric English to attested Old English. It includes
changes earlier than the manuscript period, not merely changes within it.
West Saxon is the principal target; each comparison still requires its actual
dialect, paradigm cell and evidential status.

## Scope and dialect variation

Not every change in this chapter has pan-Old-English scope. Some changes — most
notably ordinary West Saxon palatal diphthongization and parts of the
back-mutation history — are specifically West Saxon or more broadly southern
Old English phenomena. The diphthong corridor also represents earlier West
Germanic feeders; a West Saxon final outcome does not date every feeder to
West Saxon [@RingeTaylor2014, pp. 41--42, 65--66, 171--173, 215--217].
(The West Saxon palatal-glide
spellings, SC016, belong to the written surface of Old English and are treated
in Chapter 5.)

The CAPR derivations target West Saxon Old English citation forms as the default
comparator. Changes that belong to other dialects, or that are absent from West
Saxon, may appear in lexical entries as comparanda rather than as derivational
steps.

The distinction between West Saxon and Anglian comparanda requires the
actual text and dialect, not merely a regional label. Hogg discusses the
limits of the traditional divisions and the evidence for the principal
textual varieties [@HoggGrammar1992, pp. 3--8, §§1.5--1.12].

## Chapter structure

The changes in this chapter fall into several natural historical subgroups,
though the boundaries between them are not always sharp:

Prehistoric English contraction and fronting:
Completed stressed \emph{*ai > *ā} is now adopted on the English daughter
in [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).
The new long vowel is distinguished from inherited oral long vowels;
the source milestones allow overlap with their earlier restructuring
[@Campbell1939, pp. 90–91; @RingeTaylor2014, pp. 170–171].
This placement leaves possible conditioned ancestral onset and the
runic interpretation qualifications explicit
[@Versloot2017, pp. 295–297, 318].

Early Old English changes linked to the Anglo-Frisian inheritance:
Changes that feed directly on, or are closely related to, Anglo-Frisian
brightening (SC043), whose section opens the vowel corridor of this chapter.
The \emph{*awj} resolution, \emph{*au} fronting and diphthong operations
currently execute before ordinary-a brightening. They cannot be described as
consuming its output. Their histories combine earlier glide reanalysis with
English diphthong realization [@Campbell1959, pp. 44--47;
@RingeTaylor2014, pp. 65--66, 171--173].
The conventional breaking/restoration account instead presupposes fronted
\emph{*æ}. English plain-a/au process identity and inherited stem identity
remain separate questions.

A coordinated formalization of ordinary \emph{*a} fronting and
\emph{*au} fronting with its completion has now been tested over the
selected lexical material. Its twenty au paths wait until the ordinary
fronting corridor and then converge with the current derivations before
breaking. This establishes computational compatibility, not historical
event identity. The production serialization remains unchanged, and the
unstressed and surviving-long-final fronting components are not dated
from this test. The completed ordinary stressed component is now independently
characterized on the English daughter. Its English-episode interpretation remains
explicitly dependent on its contraction and nucleus premises
[@Campbell1939, pp. 90–91; @Campbell1959, p. 52;
@RingeTaylor2014, pp. 170–175].

The earlier unstressed contribution is not the complete unstressed law:
[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) separately
implements fronting before heterosyllabic nasals, whereas the coda-nasal
history protects other endings [@Campbell1959, pp. 140--141].
The retained final-vowel helper connects unrounding's carried quantity to
later shortening and merger; it does not establish an independent historical
long-a fronting [@RingeTaylor2014, pp. 58--59, 299--300].

Old English consonantal changes:
Velar palatalization (SC052), palatalization of `*sk` (SC051), j-cluster
coalescence (SC057), and related changes produce the characteristically
Old English consonant phonemes. Hogg discusses these as OE consonant changes
with class-specific conditions and chronology [@Hogg1979, pp. 90–111].

Old English i-umlaut and its context:
The i-umlaut changes vowels under a following high front vocoid; paradigm
alternations are evidence for that phonological conditioning, not grammatical
conditions on the law [@Campbell1959, pp. 69--72, §§190--197;
@RingeTaylor2014, p. 222]. Ordinary West Saxon palatal diphthongization
precedes mutation in the handbook account, while the later treatment of some
mutation products after *sċ* follows it [@Fulk2018, p. 74;
@Campbell1959, pp. 68--69; @RingeTaylor2014, pp. 215--217, 235].
The adopted cascade now places the ordinary component before mutation and
retains the late approximation afterward. Gift enters with the earlier-raised
vowel, following Ringe's explicitly PGmc reconstruction
[@Ringe2017, p. 135, pp. 151–153]. Its lexical section discusses the
published e-alternatives and the confidence in this choice.

Late Old English syllabic reduction and apocope:
High-vowel apocope (SC063), medial syncope (SC065), and the cluster of
late unstressed-vowel changes (SC069–SC078) represent the later stage of Old
English phonological history, when the syllabic structure of the language
began to shift toward the more reduced profile of Middle English.

## The English partial chains

The working historical scaffold has several connected chains, not one
uniquely demonstrated total order. Their evidential strength differs.
An explicit handbook derivation, a contrast between original and secondary
vowels, and the survival of a modeled output are not interchangeable
arguments [@RingeTaylor2014, pp. 170–173, 215–237;
@Hogg1979, pp. 100–110].

| Historical relation | Evidence and interpretation | Limitation |
|---|---|---|
| Coronal assimilation before inherited ww reanalysis | Four and the second-person pronoun have assimilated inputs to vocalization | Does not date every j-created geminate |
| Inherited-long restructuring before completed ai contraction | New ai-derived long a escapes inherited-long fronting | Temporal overlap is possible |
| Completed ai contraction before ordinary short fronting | Conventional Campbell chain | Depends on the diphthong-nucleus premise |
| Ordinary fronting before breaking/restoration | Conventional English reconstruction | Never-fronted and restored outputs can coincide |
| Breaking before ordinary palatal diphthongization before mutation | Broken inputs and worked handbook vowel histories | Does not date every consonantal palatal layer |
| Mutation before the later sc treatment | Ai-derived mutation products such as sheath | Exact later conditioner remains unresolved |
| Initial productive palatal cutoff before mutation-created fronts | Unrounded mutation vowels are the stronger controls | Medial fricative merger is a separate problem |

The first three relations are supported and qualified by the earlier
vowel accounts [@RingeTaylor2014, pp. 41–42, 65–66, 170–173;
@Campbell1939, pp. 90–91]. The palatal and mutation relations require
their own evidence [@Luick1914, pp. 162–163; @Fulk2018, p. 74;
@RingeTaylor2014, pp. 215–217, 235; @Hogg1979, pp. 100–110].
The table states the defended historical targets; it does not claim that
every present executable proxy already realizes them faithfully.

## Early glide history and the English outcome

The diphthong corridor includes inherited ww, assimilated ww and geminates
created later before j. These inputs must be distinguished before assigning
one date to their long-vowel outputs. Ringe and Taylor describe inherited
glide reanalysis separately from the English realization of its products
[@RingeTaylor2014, pp. 41–42, 65–66, 171–173].
The model now separates the earlier reanalysis from English realization.

| Witness | Adopted earlier checkpoint | Later English outcome | What it tests |
|---|---|---|---|
| Four | Assimilated ww is reanalyzed as eu plus w | fēower ‘four’ | Assimilation feeder and retained glide |
| Hew | Inherited a plus ww gives au plus w | hēawan ‘hew’ | Reanalysis distinct from English realization |
| You | Vocalized iu plus w with a surviving final i before apocope | ēow ‘you’ | Prosody/apocope compatibility, not merely quantity |
| Hue | Later j-gemination creates a distinct glide input | hīew ‘hue’ | Negative control for the earlier inherited-ww subset |
| Hay | Later awj history remains separate | hīeġ ‘hay’ | Gemination and secondary glide resolution |

These are existing lexical witnesses, not new corpus admissions.
The current spelling differences also require their actual dialectal
interpretation [@Campbell1959, pp. 44–47;
@RingeTaylor2014, pp. 41–42, 57–58, 171–173].
The reconstructed West Saxon strew target is a computational control,
not an additional attested form.

The completed decomposition replaces the old consonantal-ww apocope
proxy with the historical condition: a short final high vowel after a
heavy syllable in a sentence-unstressed, phonologically final word.
You selects that weak-final context independently of its unchanged PGmc
reconstruction. Thus \emph{*iuwi} loses the final vowel to give
\emph{*iuw} before mutation. A proclitic context retains the vowel, as
in *ymbe* 'around'; weak-final *and* 'and' and stressed *ġiest* 'guest' /
*fȳr* 'fire' check the positive and negative conditions
[@RingeTaylor2014, pp. 41--42, 55, 57--58; @Campbell1959, p. 283].

The computational retained-i counterfactual for you yields a predicted
[*īei*]{.pred}, not a source-backed strong Old English spelling: the
existing w-loss before i intervenes before mutation. It tests the
represented alternative context, not an additional attestation.
Unmarked evaluation explicitly selects strong-final citation context;
absence of an acute is never used to infer sentence stress.
All selected final outputs remain unchanged.

The later realization paths are now explicit. Chew, dew, four, hew and
you complete their earlier products through
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) retains only the
disclosed j-created hue representation. Knee instead selects the
regular dative *cneowe* 'knee (dat.sg.)': its short pre-ending
diphthong comes from [SC044 OEBreaking](#rule-OEBreaking), not
singleton lengthening. The long endingless *cnēo* 'knee' and
analogically restored final \emph{w} in *cnēow* 'knee' remain a separate
paradigm comparison; later long obliques must not be confused with
the selected short cell
[@Campbell1959, pp. 232--233; @HoggGrammar2011, pp. 21--22, 86;
@RingeTaylor2014, pp. 187--188, 387].
[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) retains the singleton
show/straw forms. Hue's remaining ww before j is simplified by the
separately disclosed [SC106 OEJWWSimplification](#rule-OEJWWSimplification),
a technical residual rather than a newly established sound law.
The before-j placement of early reanalysis is a representative
serialization, not a new strict historical chronology claim
[@Campbell1959, pp. 45--47; @RingeTaylor2014, pp. 65--66, 171--175].

## Ordinary fronting, breaking and restoration

The preferred conventional account identifies ordinary non-nasal short-a
fronting and fronting of au's first element as one English episode.
The later offglide development is distinct. Early spellings record the
fronted element, but do not measure the simultaneity of two laws
[@Campbell1939, p. 91; @Campbell1959, pp. 52–53;
@Luick1914, pp. 130–131].
English episode identity is not inherited Anglo-Frisian event identity.
Nor does it identify the stressed-short process with every unstressed
or long-final clause in the present model.

Breaking then has vowel, quantity, consonantal and dialectal conditions.
Restoration in a following back-vowel environment can remove a previously
fronted vowel. A final restored vowel alone cannot distinguish that history
from original blocking of fronting
[@Hogg1979, pp. 90–97; @Versloot2025, pp. 104, 123].
The conventional account is retained as the working baseline because of
the combined argument, not because the more elaborate intermediate path
is inherently preferable.

Versloot's late Anglian alternatives must be compared in their exact domains.
His mutation-created e argument and the unbroken neighboring environments
are relevant to a restricted e-breaking component, not to a wholesale
postmutation relocation of every West Saxon breaking law
[@Versloot2025, pp. 126–128, 131–135].
A different dialectal target cannot be silently substituted for a West
Saxon lexical target. Similarly, Frisian closed-syllable breaking is not
English rC breaking merely because both are called breaking
[@Bremmer2009, pp. 33–35, 37].

## Palatal consonants and the key–day problem

The useful chronological contrast is between original conditioning fronts
and front vowels created by mutation. Rounded mutation products alone
may support a weaker conclusion, a cutoff before later unrounding.
Unrounded mutation-created fronts more directly test whether initial
velar palatalization was still productive
[@Hogg1979, pp. 100–103; @Laker2007, pp. 167–168].
This cutoff does not by itself date assibilation or every earlier
articulatory tendency.

Hogg's key and day paradigms identify the disputed merger premise.
The initial key consonant survives a mutation-created unrounded front
vowel; the day paradigm does not show the mutation that would follow
if its new medial palatal element were already equivalent to inherited j.
These statements concern particular historical cells, not arbitrary
exceptions to a sound law [@Hogg1979, pp. 102–110].

| Diagnostic | Required distinction | What is not established |
|---|---|---|
| Key oblique vowel | Original fronts versus mutation-created fronts | Date of all palatal articulation |
| Day oblique vowel | Inherited j versus a palatal fricative at mutation | Unanimous agreement on merger timing |
| Geminate/postnasal g | Stop-class history versus singleton fricative | One universal g-to-j change |
| h | Breaking trigger versus subsequent palatal/weakening history | Identity with voiced-fricative chronology |
| sk | Own consonantal law versus later sc vowel treatment | A single combined palatalization event |

Hogg considers several resolutions without endorsing one as demonstrated
[@Hogg1979, pp. 103–111]. Ringe and Taylor, however, explicitly adopt
merger after mutation [@RingeTaylor2014, p. 204]. CAPR now implements
that regular working account, preserving Hogg's phonetic objection rather
than claiming consensus. Singleton g is a fricative, including initially;
gg/ng are stops [@Fulk2018, pp. 130–132].

At Hogg's pre-palatal, pre-OE checkpoint, key has \emph{*kājæ} and day
\emph{*dæɣæ}. The inherited j in the former causes mutation, producing
\emph{*kǣjæ} without reactivating initial-k palatalization. In the latter,
the newly palatal fricative remains ʝ and the vowel stays æ:
\emph{*dæʝæ}. Native realization then gives *cǣġe* 'key' and *dæġe*
'day' [@Hogg1979, p. 105; @RingeTaylor2014, p. 204].
Premature merger instead supplies a j trigger and wrongly raises the day
vowel. These oblique cells are non-corpus diagnostics, not new selected
PGmc reconstructions; the existing day nominative cannot substitute for them.

The complete key suffix exposed a second defect: unrestricted inherited-j
normalization would erase its retained glide. The repaired
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization)
excludes non-high long front monophthongs. Its residual weak-suffix
normalization is a telescoped representation, not a universal historical
VjV vocalization law [@HoggGrammar2011, pp. 283–286;
@RingeTaylor2014, p. 228].

The fricative merger has its own visible
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger).
Its late execution after suffix raising is a tested computational holding
zone, not a precisely proved historical date. Likewise stop ʧ/ʤ are
eventual-reflex proxies, not early affricate claims. Cluster coalescence
and a dotted written reflex cannot identify all these classes as one
historical sound [@RingeTaylor2014, pp. 203–204;
@Laker2007, pp. 167–168; @Fulk2018, pp. 131–132].

## Three different mutation and diphthongization arguments

Guest, sheath and gift do not establish the same chronological relation.
The guest derivation passes through ordinary palatal diphthongization
before mutation in both the handbook account and the adopted model.
The former model raised a simple vowel before diphthongizing it. Both paths reach
*ġiest* 'guest', so their final agreement does not select the earlier path
[@RingeTaylor2014, p. 216].

The following worked comparison abstracts from consonant notation and
retains the vocalic trigger where it matters. For guest, the source starts
with PGmc \emph{*gastiz} 'guest', continued as PWGmc \emph{*gasti} 'guest'.
The vowel history is \emph{*a > *æ > *ea > *ie}; final loss of the
trigger follows the mutation it caused
[@RingeTaylor2014, pp. 216, 287].

| Checkpoint | Handbook and adopted guest path | Superseded modeled guest path |
|---|---|---|
| Ordinary fronting | Short a becomes æ | Short a becomes æ |
| After palatal conditioning is established | Original front vowel is available to ordinary PD | Original front vowel is available, but PD remains later |
| First disputed vowel operation | æ becomes ea by ordinary PD | æ becomes e at mutation |
| Second disputed vowel operation | ea becomes ie at mutation | e becomes ie in the bundled PD proxy |
| Written result | ġiest ‘guest’ | ġiest ‘guest’ |

The agreement in the last row is precisely why the intermediate rows
must be tested. This table does not treat the implementation's
palatal-consonant symbol as proof of a uniquely dated phonetic merger
[@Hogg1979, pp. 103–110].

| Witness | Source-supported distinction | Present model consequence |
|---|---|---|
| Guest | Ordinary palatal diphthongization feeds mutation | Adopted æ > ea > ie replaces the output-equivalent old path |
| Sheath | Ai-derived ā mutates; a later sc layer can affect its product | Its unchanged late clause is separately retained as an approximation |
| Gift | Earlier inherited e-to-i raising is distinct from English mutation | Selected PGmc i is outside ordinary diphthongization |
| Sheep/year | Ordinary palatal diphthongization without a mutation trigger | Controls for the ordinary component |
| Cow/lung | Mutation changes the productive consonantal environment | Controls for cutoff, not diphthongal mutation |

For sheath, *sċēaþ* 'sheath' beside *sċǣþ* 'sheath' belongs to the
separately described later group. Reporting both outcomes does not
authorize lexical optionality in the law; the exact phonological layer
and conditioner still require a defended specification
[@Campbell1959, pp. 68–69; @RingeTaylor2014, p. 235].
The incremental repair preserves the literal late clause as a visible
approximation, not a lexical exception or a newly established conditioner.

The sheath comparison instead follows the ai-derived long vowel:
\emph{*ai > *ā > *ǣ}, with the final step supplied by mutation.
The separately discussed later sc treatment can then give
\emph{*ēa}. The vowel available to the earlier ordinary process and
the vowel created later by mutation are therefore different historical
inputs, which the adopted model now separates
[@Campbell1959, pp. 68–69; @RingeTaylor2014, p. 235].

For gift, Ringe reconstructs PGmc \emph{*giftiz} 'gift', with the Old
English plural *ġifta* 'wedding', and describes the earlier raising separately
[@Ringe2017, p. 135, pp. 151–153].
Ringe and Taylor explicitly distinguish that early change from the much
later English vowel history [@RingeTaylor2014, p. 220].
The selected input now follows that earlier-raised reconstruction. The
choice is lexical and source-led, not a new raising rule justified by
output fit. Orel and Kluge–Seebold print e-vowel alternatives
[@Orel2003, p. 130; @KlugeSeebold2011, p. 359];
the lexical section compares their evidence with the e-grade presentations
and Ringe's qualified PGmc dating rather than claiming unanimous agreement.

## Quantity, reduction and the written surface

Later apocope and syncope depend on prosody and syllable structure;
earlier input conventions and surviving triggers must be inspected before
their effects are used as dates for other changes. Morphological cells
provide evidence for such environments, not grammatical conditions on
phonological rules [@RingeTaylor2014, pp. 57–59, 299–300].
Inherited quantity, compensatory lengthening, diphthong quantity and
later shortening must likewise remain separate dimensions.

The transition to Chapter 5 is a transition to the written surface, not
proof that an orthographic change is a newly dated sound change.
A single spelling can represent different historical consonant inputs,
and a changed spelling need not change the phonetic derivation.
The source discussions and worked lexical entries distinguish implemented
laws from working reconstructions and localized unresolved components.

## Executable serialization and unresolved interfaces

Sections follow executable order to make derivations inspectable, not because
that serialization proves a unique total history. Final agreement can conceal
different intermediate paths. Some proxies execute here with earlier historical
classifications; renaming identifiers would not resolve that substantive
distinction:

* SC041 (PWGmc Final Bare-`*a` Loss) and SC042 (Surviving Bimoric `*ō`
  Unrounding) carry Proto-West Germanic labels but execute in this stretch of
  the cascade.
* SC064 (NWGmc `*-n` Stem `*n` Loss) carries a Northwest Germanic label but
  executes after OE High-Vowel Apocope (SC063).
* SC049 (PGmc B Allophony) carries a Proto-Germanic label but executes here.

## Sources

Campbell's *Old English Grammar* is the primary source for the dating and
scope of individual changes in this chapter [@Campbell1959, pp. 52–72].
Hogg provides critical reassessments of palatal conditioning and its
relative chronology [@Hogg1979, pp. 90–112]. Ringe and Taylor supply the most
detailed relative-chronology analysis for the earlier portion of the chapter,
through back-mutation [@RingeTaylor2014, pp. 169--173, 215--237]. Fulk's *Comparative
Grammar* provides additional coverage for phonological conditioning
[@Fulk2018, pp. 58–61, 72–74]. For individual changes, source-specific citations appear in the
relevant sound-change sections.

# English stressed ai contraction

## Historical discussion

Inherited stressed \emph{*ái} yields \emph{*ā} in English. Ringe and Taylor
discuss this development separately from the earlier unstressed contraction.
The distinction between inherited long vowels and new \emph{*ā} requires
inherited-long fronting to have been well under way before contraction
completed; it does not prove that the two developments could not overlap
[@RingeTaylor2014, pp. 170–171]. Campbell gives the stricter conventional
sequence and places contraction before ordinary short-vowel fronting
[@Campbell1959, pp. 52–53]. Later i-mutation of the new long vowel is a
separate conditioned development, not that ordinary fronting
[@Campbell1959, p. 69].

Versloot proposes a wave account of the regional outcomes, but CAPR does
not adopt diffusion as a solution to the comparative tree problem.
His readings of early English and Frisian inscriptions are relevant
evidence independently of that mechanism, conditional on their provenance,
etymology and phonetic interpretation
[@Versloot2017, pp. 295–297, 318]. The required Anglo-Frisian ancestral node
is retained. CAPR places completed English contraction on the daughter
branch, while leaving a possible earlier conditioned onset on the common
stem distinct. This is the defended working placement under the cited
runic and comparative premises, not proof against every ancestral onset
[@Campbell1939, pp. 90–91; @Versloot2017, pp. 295–297, 318].
The inherited-long relation permits temporal overlap; the retained
executable order does not assert a strict order between entire events.

The live selected-corpus census has twenty-three applications, all carrying
stressed \emph{*ái}. Loam's selected \emph{*láimą} 'loam' is explicitly a
pre-Old-English model input, not an independent Proto-Germanic witness.
The raw corpus's additional roe reconstruction has no attested target and
is excluded from that census. The unstressed development \emph{*ai > *ē}
is the separate earlier change
[SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).

## SC004. English stressed ai contraction (`EAFAiMonophthongization`) {#rule-EAFAiMonophthongization}

```foma
define EAFAiMonophthongization [
    {*ái} -> {*ā}
];
```

The soul form fixes the relation to interstress raising. If the monophthongization is delayed until after that change, PGmc [sáiwalō]{.recon} 'soul' yields [*sāwel*]{.pred} rather than expected OE *sāwol* 'soul'. An earlier placement changes no output. This shows that [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The unstressed development \emph{*ai > *ē} in final and nonfinal syllables is a separate and earlier change; see [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).

\newpage

# Awj resolution and the English brightening of au

## Historical discussion

Two changes stand between the Proto-Germanic diphthong \emph{*au} and its Old
English reflex *ēa*. The earlier one repairs a West Germanic gemination and
restores a diphthong that the gemination had obscured. The later one fronts the
first element of every \emph{*au}, whether inherited or newly created, and
belongs with Anglo-Frisian brightening.

The two are separate developments with separate domains. The first concerns a
handful of words in which \emph{*w} stood before \emph{*j}. The second concerns
the whole Old English history of \emph{*au}, for which *lēaf* ‘leaf’,
*strēam* ‘stream’ and *brēad* ‘bread’ are ordinary witnesses, and to which the
first change merely adds two more inputs.

## Historical discussion of the resolution of \emph{*awj}

Old English *hīeġ* ‘hay’ and *strīeġan* ‘strew’ go back to forms in which
\emph{*w} preceded \emph{*j}. West Germanic doubled every consonant except
\emph{*r} before \emph{*j} after a short syllable, and \emph{*w} was an
ordinary member of that law [@Campbell1959, p. 167, §407]. Proto-Germanic
\emph{*hawja-} therefore appears as West Germanic \emph{*hauuj}
[@Campbell1959, p. 46, §120.2]. Campbell writes the sequence as \emph{auj} >
\emph{auuj} > \emph{auj}, with the diphthong restored before the Old English
developments begin.

Ringe and Taylor reach the same result and explain why it is possible
[@RingeTaylor2014, p. 53, §3.1.3]. They find the gemination of \emph{*wj}
clearest where the preceding vowel was \emph{*i}, as in Proto-Germanic
\emph{*niwjaz} ‘new’ and \emph{*siwjaną} ‘sew’, which give Old Saxon and Old
High German *niuwi* and *siuwen*. Gemination was reversible, since it merged
nothing and altered no underlying form, so the sequence Northwest Germanic
\emph{*awj} to West Germanic \emph{*[aw'w']} to pre-Old English \emph{*[auj]}
can have run its course and then undone itself. Their derivations give
Proto-Germanic \emph{*hawja} through \emph{*hauj-} to *hīeġ* ‘hay’, and
Proto-Germanic \emph{*strawjaną} through \emph{*straujan} to Anglian
*strēgan* ‘strew’ [@RingeTaylor2014, p. 173].

The strongest comparative argument for the doubled stage comes from paradigms
in which some cells had \emph{*j} in the ending and others had \emph{*i}. Only
the first group could double, and the two outcomes then sat side by side. Old
High German has *hewi* ‘hay’ beside *houwi*, and Old English itself preserves
both in one word, *glīg* ‘mirth’ from the undoubled nominative beside *glīowes* ‘of mirth’
in the genitive [@RingeTaylor2014, p. 53, §3.1.3]. The continental forms *houwi*
and *gistrouwen* ‘bestrew’, and Old Saxon *hoi* ‘hay’, point to the same West
Germanic stage, which English alone went on to resolve [@RingeTaylor2014,
p. 173].

The resolution did not treat every doubled \emph{*w} alike, and the difference
is what allows the doubling to be seen apart from it. Campbell sets the two
vowel types side by side: \emph{auj} becomes \emph{auuj} and then \emph{auj},
while \emph{iuj} becomes \emph{iuuj} and then \emph{iuj}. Thereafter they part
company, since the \emph{u} of \emph{auuj} is generally lost while the \emph{j}
of \emph{iuuj} is lost [@Campbell1959, p. 46, §120.2]. Old English *hīeġ* ‘hay’
and *hīew* ‘form, hue’ begin from shapes that differ in a single vowel and end
with different survivors. *Hīeġ* keeps its \emph{*j}, written *ġ*, while *hīew*
keeps its \emph{*w}. Campbell’s other examples of the second type are *nīowe* ‘new’,
*nīewe* ‘new’ and *glīow* ‘mirth’, *glīw* ‘mirth’.

One qualification belongs in the record. Fulk holds that \emph{*w} was never
consonantal here, so that Proto-Germanic already had \emph{*straujaną} with
its diphthong in place and there is no gemination to undo [@Fulk2018, p. 73,
§4.10 n. 1]. The account followed here is the handbook one, which the
comparative material supports: the doubled stage that the continental and
paradigm-internal forms point to is precisely the one Fulk denies ever existed.
Both accounts agree that \emph{*auj} is what enters Old English, and the
disagreement concerns whether a discrete change took place.

## SC029. Resolution of \emph{*awj} to \emph{*auj} (`OEAwwjResolution`) {#rule-OEAwwjResolution}

```foma
define OEAwwjResolution [
    {*á} {*w} {*w} {*j} -> {*áu} {*j},
    {*a} {*w} {*w} {*j} -> {*au} {*j}
];
```

The change is confined to the \emph{*a} type. PGmc [xáwją]{.recon} ‘hay’ is
doubled to \emph{*xáwwją} by the West Germanic law and then resolved to
\emph{*xáują}, and PGmc [stráwjaną]{.recon} ‘strew’ is doubled to
\emph{*stráwwjaną} and resolved to \emph{*stráujaną}, yielding *hīeġ* ‘hay’ and
*strīeġan* ‘strew’ once the later diphthong changes and \emph{i}-umlaut have applied.
PGmc [xéwją]{.recon} ‘form, hue’ is doubled by the same law, and there the
doubling holds: it passes through this change untouched and surfaces as *hīew* ‘form, hue’.

The resolution has to precede
[SC030 OEAuBrightening](#rule-OEAuBrightening), since the fronting needs a
diphthong to work on. Ringe and Taylor state the same dependence when they
observe that these new instances of \emph{*au} went on to share the ordinary
development [@RingeTaylor2014, p. 173].

## Historical discussion of the brightening of \emph{*au}

The fronting of \emph{*au} is the application to a diphthong of the same
process that fronts plain \emph{*a}, the process usually called Anglo-Frisian
brightening. Campbell arrives at the point while establishing the order of the
early vowel changes, remarking
that the normal development of Proto-Germanic \emph{*au} to Old English *ēa*
shows that the change of \emph{a} to \emph{æ} would affect the first element of
a diphthong [@Campbell1959, p. 52, §132]. His ordered list accordingly places
West Germanic \emph{a} > Old English \emph{æ} and West Germanic \emph{*au} >
Old English \emph{*æu} in one and the same step. Fulk puts it in a single
sentence, saying that this fronting of \emph{a} applied also to the diphthong
\emph{au} in Old English [@Fulk2018, p. 73, §4.12].

The intermediate stage is directly attested. Ringe and Taylor describe
\emph{*au} as first tensed and fronted to \emph{*æu}, a spelling still found
occasionally in eighth-century documents, with the offglide unrounded and
lowered only later [@RingeTaylor2014, p. 172]. Early spellings such as
*Eadbald* with an initial \emph{aeo} preserve the rounded offglide, and the
rounding survives in late Northumbrian [@Fulk2018, p. 73, §4.12]. The outcome
of the whole sequence is the *ēa* of *dēaþ* ‘death’, *ēage* ‘eye’ and
*lēaf* ‘leaf’ [@Campbell1959, p. 53, §135].

The geographical reach of the diphthongal fronting is narrower than that of the
plain one. Old Frisian shows no such fronting and has \emph{ā}, so that Old
English *ēac* ‘also’, *ēage* ‘eye’ and *bēam* ‘tree’ stand against Old Frisian
*āk* ‘also’, *āge* ‘eye’ and *bām* ‘tree’ [@Fulk2018, p. 73, §4.12; @RingeTaylor2014, p. 172]. A
later change supplies independent confirmation. Old English *gēac* ‘cuckoo’ has
a palatalized initial, which requires a front vowel to have followed it, while
Old Frisian *gāk* ‘cuckoo’ has none [@Fulk2018, p. 73, §4.12]. Brightening of plain
\emph{*a} is shared with Frisian; brightening of the first element of
\emph{*au} is English.

## SC030. Brightening of \emph{*au} to \emph{*æu} (`OEAuBrightening`) {#rule-OEAuBrightening}

```foma
define OEAuBrightening [
    {*au} -> {*aeu},
    {*áu} -> {*áeu}
];
```

Most of the words that pass through the change carry \emph{*au} inherited
straight from Proto-Germanic. PGmc [láubą]{.recon} ‘leaf’ gives *lēaf* ‘leaf’, PGmc
[stráumaz]{.recon} ‘stream’ gives *strēam* ‘stream’, PGmc [bráudą]{.recon} ‘bread’
gives *brēad* ‘bread’, and PGmc [dráugmaz]{.recon} ‘dream’ gives *drēam* ‘dream’. Where a
following \emph{*j} or \emph{*i} survives long enough to cause \emph{i}-umlaut,
the *ēa* appears in West Saxon as *īe*, as in *ġelīefan* ‘believe’ from PGmc
[galáubijaną]{.recon} ‘believe’ and *nīed* ‘need’ from PGmc [náudiz]{.recon} ‘need’
[@Campbell1959, p. 46, §120.2]. The two words supplied by
[SC029 OEAwwjResolution](#rule-OEAwwjResolution), *hīeġ* ‘hay’ and
*strīeġan* ‘strew’, join this second group.

The proportions matter for what the rule is. This is the general Old English
treatment of \emph{*au}, to which the resolution of \emph{*awj} contributes two
further inputs; the history of *hīeġ* ‘hay’ and *strīeġan* ‘strew’ does not define it.

The fronted \emph{*æu} has no independent life. It is taken up at once by the
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), which lowers
the offglide and delivers *ēa*.
Ringe and Taylor give that order explicitly when they place the tensing and
fronting first and the unrounding and lowering later [@RingeTaylor2014, p. 172].

\newpage

# Short pre-w diphthongs and the retained j-created long tier

## Historical discussion

Ordinary diphthongization before singleton \emph{w} must be distinguished
from long diphthong formation in endingless forms and from the
independently created \emph{wwj} sequences. Their similar Old English
spellings do not establish one sound law assigning long quantity
before every retained vowel ending.

For *cneowe* 'knee (dat.sg.)', the regular pre-ending stem has short
\emph{eo}. Hogg explicitly identifies the dative as a short-diphthong
example, and Campbell and Luick distinguish its genitive and dative
from the long endingless form
[@HoggGrammar2011, pp. 21--22, 86, §§2.33, 5.22;
@Campbell1959, pp. 232--233, §584; @Luick1914, p. 139, §134].
Ringe and Taylor likewise distinguish short \emph{cneow-} before
syllabic endings from long endingless *cnēo* 'knee'. The final
\emph{w} of *cnēow* 'knee' is generalized from the obliques, not
retained by an unrestricted prevocalic lengthening law
[@RingeTaylor2014, pp. 187--188, 387, §§6.2.4, 7.2.4].

The selected comparison is therefore the dative *cneowe*, from the
constructed PGmc dative \emph{*knéwai}, while citation
\emph{*knéwą} remains the lexeme-level reconstruction. Fulk prefers
the \emph{*-ai} analysis for the West Germanic dative line but
discusses alternatives; the complete selected input is a paradigm
construction, not a quotation of a whole-word reconstruction
[@Fulk2018, p. 147, §7.8].

Its short diphthong is supplied by
[SC044 OEBreaking](#rule-OEBreaking), with the source's exclusion
before a following high front vocalic. Long quantity could later
spread from endingless forms into obliques, but that leveling is
not the selected short dative's sound-law history. Campbell describes
the extension; Ringe and Taylor qualify the knee quantity inference
because decisive verse evidence is elusive
[@Campbell1959, p. 233; @RingeTaylor2014, p. 387].

Earlier inherited-glide reanalysis is independently represented by
[SC031 OEWWSimplification](#rule-OEWWSimplification). Chew, dew,
four, hew and you complete its products through
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
The operation below neither repeats that inherited event nor
implements the regular singleton history
[@RingeTaylor2014, pp. 41--42, 65--66, 171--175].

## \CAPRRuleHeading{SC033. Retained j-created long-diphthong representation}{OEEwLongDiphthong} {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

The conditioner is now restricted to the second \emph{w} followed
by \emph{j}, not a general following vowel or weak ending:

```foma
define OEEwLongContext [{*w} {*j}];
```

*Hīew* 'hue' retains this j-created path, whereas *cneowe* does not
enter it. Campbell distinguishes the \emph{iwj} class from the
low-vowel \emph{awj} class and gives the West Saxon \emph{īew}
reflex [@Campbell1959, p. 46, §120.2].

The retained mapping is a disclosed representation component, not
a newly established historical \emph{ew} to long \emph{ēow} law.
Hue's selected e-vowel input still omits the separate earlier
raising assumed by the source's i-vowel account. Its successful
final spelling does not prove that omitted intermediate or date
this mapping to an independently demonstrated West Saxon event.
The stable rule label is retained for continuity, without assigning
the technical component an invented historical stage or confidence.

## SC106. Retained j-created glide residual (`OEJWWSimplification`) {#rule-OEJWWSimplification}

```foma
define OEJWWSimplification [
    {*w} {*w} -> {*w} || _ {*j}
];
```

This technical component simplifies hue's remaining \emph{wwj}
representation after promotion. It does not restore nominative
\emph{w} in knee and does not duplicate inherited short-Vww
reanalysis. The distinct endingless and inflected histories remain
visible even where later paradigm leveling makes their spellings
converge [@Campbell1959, pp. 45--47, 232--233;
@Fulk2018, p. 154].

\newpage

# Leveling of diphthongal outputs

## Historical discussion

Forms such as *hēafod* ‘head’ reflect the redistribution of diphthongal
outcomes across a wider set of words. Campbell describes smoothing and related
later monophthongization, although the rule below is more narrowly conditioned
than any single textbook label [@Campbell1959, pp. 95--96, §§223--227].

The evidence for [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling) is less
self-contained than that for the *dēaw* 'dew' / *hēawan* 'hew' developments.

The atomic \emph{*aeu}, \emph{*eu} and \emph{*iu} clauses complete English
realization, including products of earlier
[SC031 OEWWSimplification](#rule-OEWWSimplification).
They are not the earlier West Germanic vocalization itself. Dew and hew
arrive through fronted \emph{*au}, whereas chew, four and you arrive through
\emph{*eu} or \emph{*iu}; the following consonantal glide survives.
The split-symbol clauses remain separate representation paths and do not
license arbitrary short-to-long mappings. The current operation changes
32 selected forms, rather than the previous 27
[@RingeTaylor2014, pp. 41--42, 65--66, 171--175].

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

Fronting must supply its product before the offglide changes realize it:
Ringe and Taylor explicitly distinguish these two developments
[@RingeTaylor2014, p. 172].
Earlier displacement tests that left \emph{*aeu} unrealized produced
\emph{+?}, a rejection by the computational representation rather than an
attested linguistic outcome. They therefore cannot independently establish
the historical interval. The input of *hēafod* 'head' also requires the
remaining medial unstressed vowel to reach its lowering rule; this is a
distinct dependency, not evidence that every clause above is one historical
sound law.

\newpage

# Long \emph{ēaw} before following vowels

## Historical discussion

Singleton \emph{aw} before a following vowel develops into long \emph{ēaw},
as in *sċēawian* 'show' and *strēaw* 'straw'. This remaining singleton path
must be distinguished from the inherited geminates of *dēaw* 'dew' and
*hēawan* 'hew'. Those now undergo early
[SC031 OEWWSimplification](#rule-OEWWSimplification), producing
\emph{*au} plus retained \emph{*w}, followed by English fronting and
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
Campbell distinguishes the glide histories; Ringe and Taylor distinguish
earlier reanalysis from later English realization
[@Campbell1959, pp. 45--47, 53--54; @RingeTaylor2014, pp. 65--66, 171--175].
The resulting long diphthong is \emph{ēaw}.

[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) retains its singleton
operation before [SC043 EAFBrightening](#rule-EAFBrightening).

## SC034. Long \emph{ēaw} before following vowels (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong [
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
];
```

The current operation changes four singleton show/straw forms. Dew and
hew no longer demonstrate a local simplification-then-lengthening chain
here: their earlier reanalysis has already removed that input shape.
The older displacement results for those geminates describe the superseded
representation, not independent dates for the adopted early event.
The singleton operation itself remains unchanged; this decomposition
does not give every glide history a new historical verdict
[@Campbell1959, pp. 45--47; @RingeTaylor2014, pp. 171--175].

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

# Ordinary English fronting

## Historical discussion

Anglo-Frisian Brightening or First Fronting turns low \emph{*a} into fronted \emph{*æ}-type outcomes outside nasal environments. Later Old English developments presuppose this fronted stage even where they partly conceal it. Campbell gives the classical statement of the change, Hogg supplies the standard modern labels, and Ringe and Taylor establish its local chronology with breaking and restoration [@Campbell1959, p. 52, §131; @HoggPhonology1992, pp. 102, 105; @RingeTaylor2014, pp. 157--158, 189--190; @Fulk2018, pp. 73--74, §§4.12--4.13].

Brightening creates the input to [SC044 OEBreaking](#rule-OEBreaking), while [SC046 OEARestoration](#rule-OEARestoration) later partly reverses its outcome before back vowels.

The traditional name does not itself establish one inherited event.
Under Campbell's premise that the daughter contractions precede ordinary
fronting, comparable English and Frisian outcomes require separate
daughter frontings in the strict tree. Chapter 3 develops that conditional
argument without removing the ancestral node
[@Campbell1939, pp. 90–91].
The model adopts the completed ordinary English stressed component on the
English daughter under this conventional working account. This is not a
claim that every author proves contraction before ordinary fronting:
Ringe and Taylor explicitly question whether diphthong nuclei must behave
like the plain short vowel [@RingeTaylor2014, pp. 170--175].
Earlier restricted ancestral fronting remains possible.

The separately retained unstressed and final-vowel components are not dated
by that argument. The first supplies an earlier nonnasal contribution;
[SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) separately
implements the broader unstressed domain, including the contrast between
coda and heterosyllabic nasals [@Campbell1959, pp. 140--141, §§333--334].
The second carries the model's preserved final-vowel quantity into later
shortening and merger. Its long intermediate is a representation choice,
not independent evidence for a historical long-vowel fronting
[@RingeTaylor2014, pp. 58--59, 299--300].

## \CAPRRuleHeading{SC043. Fronting of low \emph{*a} outside nasal environments}{EAFBrightening} {#rule-EAFBrightening}

```foma
define EAFBrightening [
    EAFBrighteningStressed
];
```

### Stressed component

```foma
define EAFBrighteningStressed [
    {*á} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal | .#.]
];
```

Slay requires breaking to receive the fronted root vowel: delaying the
stressed member until after [SC044 OEBreaking](#rule-OEBreaking) gives
\emph{sleaan | slēaan}, rather than OE *slēan* ‘slay’.
Rest involves two different changes, root fronting and the separately
retained final-vowel representation. Its final-vowel dependency must not
be used to date this stressed rule.

### Retained unstressed contribution

```foma
define EAFBrighteningUnstressed [
    {*a} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
```

This earlier contribution is preserved without identifying it with the
entire unstressed history. The later syllabic rule also fronts surviving
unstressed vowels before heterosyllabic nasals; an exception before every
nasal would therefore be too broad [@Campbell1959, pp. 140--141].

### Retained final-vowel representation

```foma
define EAFBrighteningLongFinal [
    {*ā} -> {*ǣ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

In *ræste* ‘rest’, this helper receives the length-preserved outcome of
[SC042 PWGmcSurvivingBimoricOUnrounding](#rule-PWGmcSurvivingBimoricOUnrounding).
The preceding-nucleus guard excludes stressed monosyllabic *hwā* ‘who’.
Later shortening and merger complete the ending; the carried long vowel
does not establish a separate dated long-a law
[@RingeTaylor2014, pp. 58--59, 299--300; @Campbell1959, p. 49, §125].

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

Breaking has the fuller handbook treatment. The *feoh* 'cattle' and
*feohtan* 'fight' type derivations preserve its velar-fricative trigger;
they do not subsequently undergo velar-fricative palatalization.

## SC044. Breaking before \emph{h}, \emph{rC}, \emph{lC}, and conditioned \emph{w} (`OEBreaking`) {#rule-OEBreaking}

```foma
define OEBreaking OEBreakingA
    .o. OEBreakingE
    .o. OEBreakingI;
```

Short \emph{e} and \emph{i} also develop short \emph{eo} and
\emph{io} before singleton \emph{w}, except when a high front vowel
or \emph{j} follows it. This is the regular pre-ending history of
*cneowe* 'knee (dat.sg.)', not long-diphthong promotion
[@Luick1914, p. 139, §134; @HoggGrammar2011, p. 86, §5.22;
@RingeTaylor2014, pp. 187--188, §6.2.4].
The shared w conditioner makes that exclusion explicit:

```foma
define EnglishBreakingWContext [
    {*w} [[EnglishStarVocalic | EnglishStarConsonant]
        - [{*i} | {*í} | {*ī} | {*ḯ} | {*j}]] |
    {*w} .#.
];
```

Root stress notation does not determine vowel length. The short
knee dative is the selected comparison; long endingless *cnēo*
'knee' and the restored \emph{w} of *cnēow* 'knee' are separate paradigm
histories, discussed with
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong).

Breaking must encounter the vowel created by brightening and must precede
the rule that would otherwise palatalize its velar trigger in *feoh*
'cattle' and *feohtan* 'fight'. Before [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [sláxaną]{.recon} ‘slay’ yields \emph{sleaan | slēaan} rather than expected OE *slēan* ‘slay’. After [SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization), PGmc [féxu]{.recon} ‘cattle’ yields [*fehu*]{.pred} rather than expected OE *feoh*, and PGmc [féxtaną]{.recon} ‘fight’ yields [*fehtan*]{.pred} rather than expected *feohtan*. The fronting relation feeds breaking. The fee/fight relation instead protects
breaking's velar trigger from premature palatalization: those forms are
displacement negatives, not live
[SC045 OEVelarFricativePalatalization](#rule-OEVelarFricativePalatalization)
applications.

## \CAPRRuleHeading{SC045. Palatalization of velar fricatives beside front vowels}{OEVelarFricativePalatalization} {#rule-OEVelarFricativePalatalization}

```foma
define OEVelarFricativePalatalization [
    {*x} -> {*ç} || _ EnglishStarFrontVowel,
    {*x} -> {*ç} || EnglishStarFrontVowel _,
    {*x} -> {*ç} || _ {*j}
]
    .o. EnglishStarAlphabet*;
```

The live population concerns voiceless x, as in *hēafod* 'head' and
*heofon* 'heaven', not voiced-fricative merger. In *feoh* 'cattle' and
*feohtan* 'fight', breaking removes the original front-vowel context:
they do not change at this rule in the live derivation. Moving the rule
before [SC044 OEBreaking](#rule-OEBreaking) instead consumes its velar
trigger, yielding [*fehu*]{.pred} and [*fehtan*]{.pred}. This is
counterbleeding protection, not direct feeding.

The distant *six* 'six' displacement test supplies only a broader
constraint: after [SC060 OEWsPalatalUmlaut](#rule-OEWsPalatalUmlaut),
PGmc [séxs]{.recon} ‘six’ yields [*sihs*]{.pred} rather than expected
OE *six*. Neither test dates voiced g. Its articulation and disputed
merger are separately treated under
[SC052 OEVelarPalatalization](#rule-OEVelarPalatalization) and
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger)
[@RingeTaylor2014, pp. 203--204; @Fulk2018, pp. 130--132].

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

# Palatalization of \emph{*sk} to \emph{*sc}

## Historical discussion

The palatalization of \emph{*sk} to Old English \emph{*sc} is one of the recognizable early
cluster changes in the larger palatalization zone. Campbell distinguishes the
cluster from plain velars when he remarks that \emph{*sk} is especially prone to
palatalization and assibilation [@Campbell1959, p. 278, §440]. Hogg gives the
same change a clearer structural place by treating \emph{*sk} beside the palatalization
of plain velars and before the later West Saxon diphthongal developments
[@HoggPhonology1992, pp. 106--108, 113]. Ringe and Taylor make the same sequence
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

# Class-distinct velar palatalization and fricative merger

## Historical discussion

Singleton g, including initial g, was a fricative when palatalization
occurred; gg and postnasal g were stops. Palatal articulation, productive
cutoff, merger and later affrication are therefore separate questions
[@Fulk2018, pp. 130--132; @Laker2007, pp. 166--168, 175--184].
The dotted spelling in *dæġ* 'day' cannot establish an early affricate or
identify every palatal consonant with inherited j.

The adopted working account keeps a palatal fricative ʝ distinct from j
during mutation, then merges it with j. Ringe and Taylor explicitly propose
this chronology [@RingeTaylor2014, pp. 203--204]. It is not unanimous:
Hogg objects to the phonetic plausibility of delayed merger and leaves the
key/day contradiction unresolved [@Hogg1979, pp. 102--111].
We prefer the regular class-distinct account because it explains the
contrasting mutation triggers without lexical or grammatical conditions.
The objection remains substantive, not silently superseded by a matching
final spelling.

Eligibility also requires attribution. Ringe and Taylor's medial-g table
is narrower than Fulk's before-front-vowel description
[@RingeTaylor2014, pp. 203--204; @Fulk2018, pp. 130--132].
The present fricative implementation retains its broader domain; this
merger decision is not a covert adoption of the narrower table.

## SC052. Singleton-fricative articulation (`OEGFricativePalatal`) {#rule-OEGFricativePalatal}

```foma
define OEGFricativePalatal [
    [{*g}|{*ɣ}] -> {*ʝ} ||
        [.#.|[EnglishStarAlphabet - [{*g}|{*n}|{*ŋ}]]]
        _ EnglishStarFrontVowel,
    [{*g}|{*ɣ}] -> {*ʝ} || EnglishStarFrontVowel _ .#.,
    [{*g}|{*ɣ}] -> {*ʝ} || EnglishStarFrontVowel
        _ [EnglishStarConsonant - [{*j}|{*g}]]
] .o. [
    [{*g}|{*ɣ}] -> {*ʝ} ||
        [.#.|[EnglishStarAlphabet - [{*g}|{*n}|{*ŋ}]]] _ {*j}
];
```

The guards keep gg/ng in their stop paths. The value ʝ is a real phonetic
class, not a tag recording a consonant's ancestry. It is transparent to a
following mutation trigger, but is not itself j at that date.
The source comparison normalizes older fricative notation to modern ɣ/ʝ,
never to the digit 3 [@Hogg1979, p. 105; @RingeTaylor2014, p. 204].

## \CAPRRuleHeading{SC052. K articulation and eventual reflex}{OEVelarPalatalizationKFront} {#rule-OEVelarPalatalizationKFront}

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
];
```

Here ʧ is a telescoped eventual-reflex proxy, not a claim that early
palatal stops were already affricates. Ringe and Taylor explicitly separate
the initial palatal stop from subsequent affrication and its syncope
dependencies [@RingeTaylor2014, pp. 203--204].
The *weccan* 'wake', *licgan* 'lie' and *lecgan* 'lay' examples concern
inherited j-clusters, not independent proof of every plain-velar conditioner
[@RingeTaylor2014, pp. 213--214].

The deterministic kk-before-j path protects *streċċan* 'stretch'.
The original-front versus secondary-front distinction is more directly
tested by unrounded key than by rounded *cȳ* 'cow'; rounding alone can
give only a cutoff before later unrounding
[@Hogg1979, pp. 100--105; @Laker2007, pp. 167--168].

## SC052. Retained stop paths (`OEVelarPalatalizationStops`) {#rule-OEVelarPalatalizationStops}

```foma
define OEVelarPalatalizationStops [
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

Singleton fricatives have already left this domain. The remaining gg/ng
paths use ʤ as an eventual-reflex proxy; the initial singleton fricative
is no longer represented as an early affricate. *Wicg* 'horse' is a
geminate-class illustration, *senġan* 'singe' a postnasal control, and
*lungen* 'lung' the unchanged back-vowel negative
[@RingeTaylor2014, pp. 203--204, 213--214; @Fulk2018, pp. 131--132].

## SC052. Combined articulation (`OEVelarPalatalization`) {#rule-OEVelarPalatalization}

```foma
define OEVelarPalatalization [
    OEGFricativePalatal .o. OEVelarPalatalizationStops
];
```

The combined operation does not give every class one sharply dated
palatalization/affrication/merger event. It supplies the class distinctions
needed by ordinary palatal diphthongization and mutation.
The common-stem onset remains a separate question
[@Luick1914, pp. 835--841; @Fulk2018, pp. 130--132].

### Key and day at the mutation checkpoint

Hogg's oblique comparison starts here from pre-palatal, pre-OE
\emph{*kājæ} and \emph{*dæɣæ}; neither is silently fed through a PGmc
prefix [@Hogg1979, p. 105]. The source target is *cǣġe* 'key',
with velar initial k, versus *dæġe* 'day'.

| Checkpoint | Key | Day under the adopted account |
|---|---|---|
| Before palatalization | \emph{*kājæ} | \emph{*dæɣæ} |
| Before mutation | Inherited j remains | Palatal ʝ is distinct from j |
| After mutation | \emph{*kǣjæ}, without new initial palatalization | \emph{*dæʝæ}, without æ-raising |
| After merger and native realization | *cǣġe* | *dæġe* |

Premature merger instead predicts pre-OE [\emph{*dejæ}]{.pred} under
these premises. The experiment tests that source-based contrast; the
existing day nominative is not the oblique discriminator
[@Hogg1979, pp. 105--110; @RingeTaylor2014, p. 204].

The complete key suffix additionally requires
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization)
to retain j after its non-high long front vowel. A correct mutation
checkpoint followed by model-only [*cǣie*]{.pred} would not constitute a
correct native derivation [@Hogg1979, p. 105].

## \CAPRRuleHeading{SC109. Postmutation merger serialization}{OEPalatalFricativeMerger} {#rule-OEPalatalFricativeMerger}

```foma
define OEPalatalFricativeMerger [
    {*ʝ} -> {*j}
];
```

The historical commitment is merger after mutation
[@RingeTaylor2014, p. 204]. Its execution after
[SC089 OELateUnstressedAgSuffix](#rule-OELateUnstressedAgSuffix)
is a computational holding zone, not proof of an exact historical date.
It keeps the fricative out of inherited-j normalization while preserving
late palatal raising, syllable weight, reduction and native rendering.
[SC057 OEJClusterCoalescence](#rule-OEJClusterCoalescence) remains a
different cluster process. Stop affrication dates and the precise
disputed eligibility domain are not settled by this merger.

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
of vowel quality across the Old English vowel system [@HoggPhonology1992, pp. 113--114].

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

Two further distinctions are essential to their relative chronology. First,
the raising of inherited Germanic \emph{*e} to \emph{*i} before a following
high front vocoid is much earlier than Old English i-umlaut. Ringe reconstructs
PGmc [giftiz]{.recon .iv lang=pgmc sort=giftiz} 'gift', with OE plural *ġifta*
'wedding', and discusses that earlier raising separately
[@Ringe2017, p. 135, pp. 151--153]. Ringe and Taylor likewise caution that
raising of inherited \emph{*e} occurred hundreds of years before the Old
English changes; a later repetition is rare and doubtful
[@RingeTaylor2014, p. 220]. The selected gift input now has the earlier-raised vowel. Its lack of
ordinary diphthongization therefore does not date the general West Saxon
process. Published e-reconstructions remain genuine alternatives
[@Orel2003, p. 130; @KlugeSeebold2011, p. 359]; the lexical discussion
compares their evidence and explains the attributed working choice.

Second, the ordinary diphthongization of inherited/fronted non-high vowels
must be distinguished from the later treatment of some mutation products
after *sċ*. Campbell separates that small group from his general front-vowel
diphthongization: the group includes *sċēaþ* 'sheath' beside *sċǣþ* 'sheath'
[@Campbell1959, pp. 68--69, §§184--185]. Ringe and Taylor explicitly place
the treatment of the ai-derived mutation product after mutation, giving the
same two sheath outcomes [@RingeTaylor2014, p. 235]. Their ordinary
West Saxon derivations, including *ġiest* 'guest' and *ċytel* 'kettle',
instead pass through palatal diphthongization before mutation
[@RingeTaylor2014, pp. 215--217, 222].

The historically preferred working account therefore has ordinary palatal
diphthongization before Old English mutation, with the separately evidenced
later *sċ* treatment after it. The adopted cascade separates these operations: ordinary diphthongization
precedes mutation, and the unchanged late approximation follows it.
The sources' alternate spellings do not by themselves supply an
exceptionless conditioning law for the later group; its full conditioner
remains unresolved.

## \CAPRRuleHeading{SC056. West Saxon palatal diphthongization}{OEWsPalatalDiphthongization} {#rule-OEWsPalatalDiphthongization}

```foma
define OEWsPalatalDiphthongization [
    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

West Saxon *gieldan* ‘pay’, *scield* ‘shield’, and *scieppan* ‘create’ show diphthongization after an already palatal consonant [@RingeTaylor2014, pp. 215--216, §6.5.1]. Their dialectal and phonological restriction separates this development from system-wide i-umlaut.

Hogg's *giefan* ‘give’ and *sceap* ‘sheep’ belong to the same palatal-consonant environment [@HoggPhonology1992, p. 112]. Fulk likewise assigns this diphthongization a place before front mutation and distinguishes the two processes [@Fulk2018, p. 74, §4.13].

The ordinary live applications comprise *ġiefan* 'give', *ġiest* 'guest',
*sċeaft* 'shaft', *sċieran* 'shear', *sċēap* 'sheep',
*sċield* 'shield' and *ġēar* 'year'. Gift is unchanged at this rule because
its selected vowel already reflects earlier raising. Sheath changes from the mutation product
\emph{*ǣ} to \emph{*ēa}; it supplies evidence for the later *sċ* layer, not
the date of the ordinary treatment represented by the other examples.

The adopted ordinary process precedes mutation and preserves the split-
diphthong and high-i negative controls. The reported absence of a later
displacement failure supplies no positive historical terminus.

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

The selected cow and lung inputs are negative controls on the present
palatalization rule. Moving the composite umlaut rule before that rule yields
[*ċȳ*]{.pred} and [*lunġen*]{.pred} instead of *cȳ* 'cow' and *lungen* 'lung'. This
constrains the current rule's productive domain; it does not assign every
consonantal layer the same date. In particular the selected *cȳ* is a
dative-singular input, not evidence from an assumed generic plural.

The stored gift and sheath displacement failures constrain the current
serialization, not a universal historical upper boundary. The former gift input
left an earlier raising to this late rule; sheath represents the later
*sċ* treatment of a mutation product. Moving the entire palatal-diphthongization
bundle earlier strands sheath and diphthongizes the model's still-unraised
gift vowel. Neither failure overturns the independently supported ordinary
palatal-diphthongization-before-mutation account.

## SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

Raising of umlauted `æ` to `e` continues the same assimilatory event as fronting and therefore shares the chronology of general i-umlaut.

The four displacement controls concern the composite rule. They are not
independent tests of this raising component: for example, the cow vowel
changes in the fronting component, not in this \emph{*æ}-raising clause.
Component chronology must follow the source-supported assimilatory event,
with ordinary palatal diphthongization and the later *sċ* extension kept
distinct.

The sources do not describe umlaut as simple fronting alone. Campbell notes that
the low front vowel
changes again before `m` and `n` in most dialects [@Campbell1959, p. 69, §190],
and Hogg likewise treats short front vowels as part of the same assimilatory
system [@HoggPhonology1992, p. 113].

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
[@Campbell1959, pp. 69--72, 78--80, §§190--191, 248--251; @HoggPhonology1992, pp. 113--114]. These diphthongal outcomes form a distinct part of the general
umlautal development alongside simple fronting.

Those composite displacement controls do not isolate diphthongal mutation:
neither the cow input nor the gift input has a diphthong here. In the
conventional history, diphthongs produced by ordinary palatal diphthongization
can be mutated, as in the source derivation of *ġiest* 'guest'
[@RingeTaylor2014, p. 216]. The adopted derivation now follows that ea-to-ie source path. The former
simple-vowel route converged on the same final form, showing why final
agreement alone could not establish the relative chronology.

## SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

The literature presents fronting, raising, and diphthongal mutation as effects of one historical development. They consequently occupy a single place in the Old English chronology.

The cow/lung displacement results require the present productive
palatalization rule not to consume those mutation-created environments.
The historical interpretation still depends on the relevant consonantal
layer and inherited versus secondary front-vowel conditions.

There is no single source-supported upper boundary at the entire West
Saxon bundle. Ordinary palatal diphthongization precedes mutation in the
handbook account; the later *sċ* treatment of some mutation products follows
it. The former gift input and sheath's later layer explained the old bundled
serialization, not a date for every historical palatal process.

## Retained late palatal-diphthongization approximation {#rule-OELatePalatalDiphthong}

```foma
define OELatePalatalDiphthong [
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

This support operation retains exactly the former postmutation long-vowel
clause. Its sole current application is *sċēaþ* 'sheath'. The four initial
triggers are an unchanged approximation, not a source-proven complete
historical conditioner. Campbell and Ringe–Taylor distinguish the later
class [@Campbell1959, pp. 68–69; @RingeTaylor2014, p. 235];
the incremental implementation does not claim to have resolved it.

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
constrains this computational cluster consumer. It does not independently
date all singleton-fricative articulation or merger: the latter is distinct
from this rule and is now explicit under
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger)
[@RingeTaylor2014, p. 204; @Laker2007, pp. 167--168].
Nothing in the present lexicon supplies a terminus ante quem for the
cluster consumer.

\newpage

# Back mutation

## Historical discussion

West Saxon *giefan* ‘give’ and *wefan* ‘weave’ stand against non-West-Saxon
*geofad* 'gave' and *weofan* 'weave'. Ringe and Taylor use this contrast to define the
dialectal profile of back mutation [@RingeTaylor2014, p. 319, §6.9.4].
Campbell's treatment of diphthongization before following back vowels includes
*heofon* ‘heaven’ [@Campbell1959, p. 86, §207], while Hogg draws the instructive
comparison with breaking [@HoggPhonology1992, p. 113]. Fulk accordingly separates back
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

This later loss is distinct from the West Germanic weak-word loss of
[SC098 PWGmcUnstressedWordFinalIApocope](#rule-PWGmcUnstressedWordFinalIApocope).
A selected proclitic context does not become word-final merely because its
citation spelling ends there. Its temporary boundary annotation blocks
the final-position conditions below and is removed only after their
application; it is not a segment of the linguistic reconstruction.
The vowel-replacement clauses themselves are unchanged
[@RingeTaylor2014, pp. 57--58, 284--303].

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
] .o. [{*ᶜ} -> 0];
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
    {*ō} -> {*o} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]*
];
```

The rule shortens the remaining unstressed long \emph{*ō} after fronting. The
shortened vowel is then resolved by the following medial/final distribution,
not directly as \emph{a} [@StauslandJohnsen2015, pp. 28--31].

Moving the rule before [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly) makes PGmc [búrōθi]{.recon} ‘bears’ yield [*boreþ*]{.pred} rather than expected OE *boraþ* 'bears', and PGmc [líznōθi]{.recon} ‘learns’ yield [*liorneþ*]{.pred} rather than expected *liornaþ* 'learns'. The contrast requires [SC071 OELateOShortening](#rule-OELateOShortening) to follow [SC070 OEUnstressedFrontingEarly](#rule-OEUnstressedFrontingEarly).

## \CAPRRuleHeading{SC099. Medial raising of shortened unstressed \emph{*o}}{OEMedUnstressedORaising} {#rule-OEMedUnstressedORaising}

```foma
define OEMedUnstressedORaising [
    {*o} -> {*u} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]* EnglishStarVocalic
];
```

After [SC071 OELateOShortening](#rule-OELateOShortening), the shortened vowel gives \emph{u} in an unstressed medial
syllable. The rule encodes Stausland Johnsen's statistically supported account
of West Saxon ō-verb pasts, not a general rule for inherited short \emph{*o}
or for nominal morphology [@StauslandJohnsen2015, pp. 28--31, 36]. His
diagnostic derivation is PGmc [wúndōdē]{.recon} ‘wounded’ > [wundode]{.pred}
> OE [wundude]{.iv lang=oe sort=wundude role=evidence_form} ‘wounded’ [@StauslandJohnsen2015, pp. 28--29].

## \CAPRRuleHeading{SC100. Final lowering of shortened unstressed \emph{*o}}{OEFinalUnstressedOLowering} {#rule-OEFinalUnstressedOLowering}

```foma
define OEFinalUnstressedOLowering [
    {*o} -> {*a} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [EnglishStarConsonant | EnglishPalatalConsonant]* .#.
];
```

In a final syllable the same shortened vowel gives \emph{a}. Thus the existing
month control continues PGmc [mḗnōθz]{.recon} ‘month’ through shortened
\emph{*o} to OE [mōnaþ]{.iv lang=oe sort=monath role=evidence_form} ‘month’, while [wúndōdē]{.recon} ‘wounded’ takes
[SC099 OEMedUnstressedORaising](#rule-OEMedUnstressedORaising)
instead. The medial/final contrast and its chronology after long-vowel
shortening are Stausland Johnsen's analysis [@StauslandJohnsen2015,
pp. 28--31].

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
normalizes part of the inherited intervocalic \emph{*j} domain, and
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

## \CAPRRuleHeading{SC082. Bounded inherited-j normalization}{OEIntervocalicJVocalization} {#rule-OEIntervocalicJVocalization}

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} ||
        [EnglishStarVocalic - [{*ǣ}|{*ē}|{*ḗ}]] _ EnglishStarVocalic
];
```

The former unrestricted VjV matcher wrongly gave model-only
[*cǣie*]{.pred} instead of *cǣġe* 'key'. Hogg's pre-OE
\emph{*kǣjæ} retains the glide [@Hogg1979, p. 105]. The bounded rule
therefore excludes preceding non-high long front monophthongs.

This is not a generic physical vocalization law. Hogg distinguishes
high-vowel coalescence from spellings that merely represent a consonantal
glide and from unstressed alternations
[@HoggGrammar2011, pp. 283--286, §§7.69--7.76].
The remaining weak-suffix e+j to e+i to i path telescopes later
raising/contraction, rather than asserting that its e+i intermediate is a
source reconstruction [@RingeTaylor2014, p. 228].
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction)
consumes that modeled sequence. The full residual proxy domain is not
claimed to be one independently established historical event.

The separately represented fricative ʝ passes through this zone without
being treated as inherited j. Its later merger belongs to
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger).

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

# Late unstressed suffix raising

## Historical discussion

The late history of unstressed \emph{*-ag-} differs from prehistoric
i-mutation. Ringe and Taylor give the sequence through fronting and
raising to \emph{-ig-}, explicitly placing its final stage long after
mutation. Their examples include *huniġ* 'honey'; a velar intermediate
can survive before a back vowel [@RingeTaylor2014, pp. 334--335, §6.9.6].
These are the printed pages, not the PDF sheet labels.

## SC089. Late suffix consumer (`OELateUnstressedAgSuffix`) {#rule-OELateUnstressedAgSuffix}

```foma
define OELateUnstressedAgSuffix (
    [{*a} -> {*e} ||
        EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*g}]
    .o.
    [{*g} -> {*ʝ} ||
        EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ {*e} _ .#.]
    .o.
    [{*e} -> {*i} ||
        EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ [{*ʝ}|{*ʤ}]]
);
```

The singleton consonant is a palatal fricative, not an early affricate
[@Fulk2018, pp. 130--132]. The raising consumer therefore recognizes ʝ
alongside retained stop-reflex compatibility. This does not make ʝ a
prehistoric mutation trigger: later raising and earlier i-mutation have
different conditioning histories.

The present late applications are *huniġ* 'honey' and *wīþiġ* 'withy'.
The word-final guard remains narrow; this implementation is not an
exhaustive model of every inflected suffix form.
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger) follows
here as a disclosed serialization, not proof of a uniquely dated historical
merger immediately after this raising
[@RingeTaylor2014, p. 204, pp. 334--335].

\newpage

# Chapter 5. Old English orthography and the written surface


## Historical interval

This short chapter stands apart from the derivational chapters that precede
it. The changes of Chapters 1–3 are sound changes: they altered the spoken
form of the language. The material treated here belongs instead to the
written surface of Old English — scribal conventions that determined how the
results of the completed phonological history were committed to parchment.

In the executable model these conventions apply after every phonological
rule, at the very end of the cascade, because that is where they belong
historically: a spelling practice can only render forms that the spoken
language had already produced.

## Scope

The one rule treated here is the West Saxon palatal-glide spelling (SC016),
by which back vowels following word-initial [j] — spelled *g* — came to be
written with a preceding front glide letter, as in *geoc* 'yoke' for spoken
[jok] and *geoguþ* 'youth' for a form whose root vowel remained [u]. Ringe and Taylor state the modern assessment
directly: the *eo* of *geoc* is a spelling convention, and the word was
pronounced [jok] [@RingeTaylor2014, p. 5]. Hogg reaches the same verdict for
the back-vowel cases generally [@HoggPhonology1992, p. 113]. The older handbooks —
Campbell, Brunner, Bülbring, Luick — analysed the same spellings as rising
diphthongs; the section below presents both views
[@Campbell1959, p. 17, § 44; @SieversBrunner1965, pp. 64--65, § 92].

## Sources

Ringe and Taylor provide the modern phonological interpretation
[@RingeTaylor2014, p. 5]. Campbell [@Campbell1959, pp. 17, 64--67, §§ 44, 170--176], Brunner
[@SieversBrunner1965, pp. 64--65, § 92], and Bülbring
[@Bulbring1902, p. 120, §§ 298--299] document the
distribution of the spellings; Hogg supplies the critical reassessment
[@HoggPhonology1992, p. 113].

# West Saxon palatal-glide spelling before back vowels

## Historical discussion

West Saxon spellings such as *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ*
'youth' write a front glide letter between a word-initial palatal and a
following back vowel. Campbell describes the phenomenon as the development
of rising diphthongs when "palatal glides developed before back vowels"
and cites *ġeoc* directly [@Campbell1959, p. 17, §44]; Brunner separates
the \emph{u}-cases (*ġeong*, *ġeoguþ*) from the \emph{o}-cases (*ġioc* 'yoke',
*ġeoc*) [@SieversBrunner1965, pp. 64--65, §92.1]; Bülbring likewise treats
*iuguð* 'youth' and *iuc* under \emph{ju} but derives *ġioc*, *ġeoc* from West
Germanic \emph{*jok} [@Bulbring1902, p. 120, §§298--299]; and Luick groups
all of these under his "schwebende Diphthonge" after palatal onsets
[@Luick1914, pp. 158--159, §169].

The phonological interpretation of these spellings is disputed. The older
handbook tradition — Campbell, Brunner, Bülbring, Luick — reads them as
genuine rising diphthongs. The modern assessment is orthographic: Ringe and
Taylor state flatly that *ġeoc* "is /jok/", the digraph being a spelling
convention that became universal after word-initial /j/
[@RingeTaylor2014, p. 5], and Hogg concludes that the back-vowel cases were
"never anything more than an orthographic variation", judging Campbell's
arguments to the contrary "insubstantial" [@HoggPhonology1992, p. 113;
@Campbell1959, pp. 66--67, §176]. This model follows Ringe and Taylor and
Hogg: the rule is a spelling convention applied to the finished phonology,
and it therefore stands at the end of the derivation, in the written-surface
stage of the cascade.

Its position also settles a relative chronology. The \emph{o} of *ġeoc* 'yoke'
is itself the product of Northwest Germanic u-lowering
([SC017 PNWGmcULowering](#rule-PNWGmcULowering)): Fulk lists *ġeoc* as a
regular lowering example beside OIcel *ok* and OHG *joh*
[@Fulk2018, p. 56, §4.3], and Campbell gives *ġeoc* among the regular
\emph{u} > \emph{o} words [@Campbell1959, p. 43, §115]. The lowering
therefore feeds the spelling: first \emph{*juk-} became \emph{*jok-} in
Northwest Germanic, and only much later did West Saxon scribes write the
result as *ġeoc*. Where lowering did not apply, as in *ġeoguþ* 'youth',
whose root \emph{u} was protected by the high vowel of the following
syllable, the same convention wrote the retained \emph{u} with the same
digraph [@SieversBrunner1965, pp. 64--65, §92.1].

## \CAPRRuleHeading{SC016. West Saxon palatal-glide spelling before back vowels}{OEWsPalatalGlide} {#rule-OEWsPalatalGlide}

```foma
define OEWsPalatalGlide [
    {*ó} -> {*éo} || .#. ġ _ ,
    {*ú} -> {*éo} || .#. ġ _ ,
    {*o} -> {*eo} || .#. ġ _ ,
    {*u} -> {*eo} || .#. ġ _
];
```

The rule rewrites a back vowel after word-initial \emph{ġ} as the digraph
spelling, covering both the lowered \emph{o}-cases (*ġeoc* 'yoke') and the
retained \emph{u}-cases (*ġeoguþ* 'youth'). Because it is a convention of the
written language, it applies after every phonological change; in
particular it follows [SC017 PNWGmcULowering](#rule-PNWGmcULowering),
which supplies the \emph{o} of *ġeoc*. If the spelling rule were placed
before u-lowering, the derivation would have to treat an Old English
scribal practice as a Northwest Germanic sound change, an ordering that
no source supports. The witnesses *ġeoc* and *ġeoguþ* between them fix
both faces of the rule: one shows the convention applied to lowered
\emph{o}, the other to unlowered \emph{u}. The handbook domain is broader
(it also includes \emph{a}/\emph{ā}/\emph{ō} contexts after word-initial
palatals), but this executable rule is intentionally complete for the
currently selected corpus witnesses rather than a maximal dialectal
enumeration.

\newpage

# References

::: {#refs}
:::
