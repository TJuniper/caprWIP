# A local Old English sequence from allophony to weak-tail nasal loss

## Introduction

This section continues the same local stretch of the Old English sound-change sequence. It begins with labial allophony and Sievers-law syncope, moves through palatalization, the narrow glide-loss bridge before umlaut, and the main umlautal chapter, then turns into the later sequence of j-cluster coalescence, nasal dissimilation, back mutation, and two short weak-tail notes.

The sequence is continuous without pretending to be one single historical law. Some chapters here carry substantial consonantal or vocalic developments; others remain brief because they preserve smaller linking steps whose historical range is narrower.

# B allophony and Sievers-law syncope

## Historical discussion

The two changes gathered here belong to different historical categories, and
they sit next to each other in the sequence that leads into Old English
palatalization. The first is the positional alternation of Germanic \emph{*b}. Hogg
states the Old English distribution clearly: /b/ is a stop initially, after
nasals, and in gemination, while the same segment is otherwise realized as a
voiced bilabial fricative [@HoggPhonology1992, p. 108]. Ringe and Taylor support
the broader West Germanic background by treating Proto-West-Germanic \emph{*b} as a
segment whose stop and fricative values depend on position
[@RingeTaylor2014, p. 121], and Luick's spelling evidence shows the same labial
fricative pattern in Old English [@Luick1914, p. 107].

Sievers' Law belongs to a different part of the historical discussion. It is a
prosodic and morphological adjustment in heavy stems, not a distributional
allophone of a stop consonant. Adamczyk treats the Old English reflexes of the
law as real historical material in weak verbs and related formations
[@Adamczyk2001, pp. 61--72]. Fulk gives the compact comparative summary through familiar
forms such as *biddan* ‘ask’, *sellan* ‘give’, and *nerian* ‘save’
[@Fulk2018, p. 127, §6.15]. The point of keeping the two changes together is
therefore practical and chronological. The behavior of Germanic \emph{*b} still
needs a brief place in the book, and Sievers-law syncope is the last narrow feeder
before the palatalization sequence begins in earnest.

## SC049. Distribution of \emph{*b} after vowels and liquids (`PGmcBAllophony`) {#rule-PGmcBAllophony}

The first rule formalizes the stop-fricative alternation of Germanic \emph{*b}.

```foma
define PGmcBAllophony [
    {*b} -> {*β} || PGmcStarVocalic _,
    {*b} -> {*β} || [{*l} | {*r}] _
] .o. [
    {*β} -> {*b} || _ {*b}
];
```

In prose, the rule says that \emph{*b} becomes a fricative after vowels and
liquids, while geminate \emph{*bb} keeps the stop value.

Historically, this is the sort of narrow distributional statement that the
handbooks place within the consonant system and discuss only briefly on its own.
Even so, it matters because later derivations assume that the
alternation is already in place. The clearest tested consequence appears in
*reġnboga* ‘rainbow’. If the rule is moved before the earlier linking-vowel
adjustment, the derivation yields *reġnfoga* ‘rainbow’ rather than expected OE
*reġnboga* ‘rainbow’. This gives the earlier boundary `SC037 < SC049`.
No equally sharp later lexical breakpoint emerges within the tested sequence, so
the rule has no explicit later boundary within the present sequence.

## SC050. Sievers-law syncope (`SieversLawSyncope`) {#rule-SieversLawSyncope}

The second rule removes the Sievers-law \emph{*i} before \emph{*j} after a consonant.

```foma
define SieversLawSyncope [
    {*i} -> 0 || [EnglishStarConsonant | EnglishPalatalConsonant] _ {*j}
];
```

In plain language, the rule contracts the heavier \emph{*-CijV-*} sequence to
\emph{*-CjV-*}. That is why it belongs to the historical aftermath of Sievers' Law and
stands apart from the earlier stop-fricative distribution.

Its place in the sequence is clearer than that of the allophony rule. If the
change is delayed until after [velar palatalization before front
vowels (`OEVelarPalatalization`)](#rule-OEVelarPalatalization), the cluster
behind *streċċan* ‘stretch’ is affected too late. With PGmc
\emph{*strákkijaną} in the wrong order, the derivation yields *strecċan*
‘stretch’. The expected Old English form is *streċċan* ‘stretch’. That is a real chronological
consequence. No equally precise earlier lexical breakpoint fixes how far back
the syncope must stand, so the historical picture remains asymmetric. The rule
is secure as an immediate feeder into the palatalization zone, even though its
earlier limit is less sharply bounded. The later boundary is therefore
`SC050 < SC052`.

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

Luick is especially useful for the larger frame. He treats
the cluster change as part of a broader early movement toward palatal
articulation, while still allowing later vowel consequences to form a different
chapter of the history [@Luick1914, p. 157, §168]. Fulk's
summary is the most concise warning against overextension: Old English \emph{*sc} is
palatal except in the well-known back-vowel environments that preserve harder
outcomes [@Fulk2018, p. 28]. The result is a historically clear rule, but not an
excuse to merge the whole palatalization and umlaut region into one undivided
chapter.

## SC051. Palatalization of \emph{*sk} to \emph{*sc} (`OESkPalatalization`) {#rule-OESkPalatalization}

The implementation states the \emph{*sk} rule explicitly.

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

In prose, the rule turns \emph{*sk} into a palatal outcome in the environments
that lead to Old English \emph{*sc}.

Its historical place is between the earlier restoration and the later palatal
vowel developments. If it is moved too early, the forms behind *flasce* ‘flask’
and *wascan* ‘wash’ are fronted too soon, yielding *flæsce* ‘flask’ and
*wæscan* ‘wash’ rather than expected OE *flasce* and *wascan*. This gives the
earlier boundary `SC046 < SC051`. If it is moved too late, the cluster no longer feeds the later
West-Saxon diphthongal outcomes that appear in *sċeaft* ‘shaft’, *sċēar*
‘shear’, *sċēaþ* ‘sheath’, *sċēap* ‘sheep’, and *sċield* ‘shield’. That is why
the rule sits naturally beside [velar palatalization before front vowels
(`OEVelarPalatalization`)](#rule-OEVelarPalatalization) and before [West Saxon
palatal diphthongization (`OEWsPalatalDiphthongization`)](#rule-OEWsPalatalDiphthongization).

No single later wrong form is isolated for the whole group of
\emph{*sċea-* 'sea'} / \emph{*sċie-*} witnesses, but the current notes do show that the cluster
must already be palatalized before the later West-Saxon diphthongal rule
applies. This gives the later boundary `SC051 < SC056`.

The narrower chapter shape matters. The cluster rule is real and historically
visible, but it is still only one part of the broader palatalizing sequence. The
change should therefore be read as a distinct cluster development inside that
sequence, not as a complete account of Old English palatalization.

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
is important because it moves the discussion from a broad list of palatal
outcomes to a more precise phonological environment involving adjacency and
syllable structure.

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

Taken together, these accounts show a gradual tightening of focus. Luick treats
palatalization as a broad early movement. Campbell distinguishes more sharply
between plain velars and the `sk` complex. Hogg specifies the adjacency and
syllable conditions more directly. Ringe and Taylor then place the plain velar
change in an explicit sequence that leads forward to later West-Saxon
diphthongization. The literature therefore supports two claims at once: the
change belongs to a larger palatalizing environment, and it must be kept
distinct from neighboring processes if the sequence of developments is to be
described accurately.

## SC052. Palatalization of \emph{*k} before front vowels and \emph{*j} (`OEVelarPalatalizationKFront`) {#rule-OEVelarPalatalizationKFront}

The first part of the implementation isolates the `k`-side environments of the
change.

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

In prose, the rule turns plain `k` into a palatal outcome before front vowels
and `j`, including the geminated environment before `j`.

Historically, this section corresponds to the core of the older discussion of
palatalized velars. It captures the environments behind forms such as *weccan*
‘wake’, *licgan* ‘lie’, and *lecgan* ‘lay’, where front vowels or `j` trigger
the palatal outcome in the first place [@RingeTaylor2014, pp. 213--214,
§6.4.1]. It is also the part of the process that prepares forms later assumed by
[velar palatalization before front vowels
(`OEVelarPalatalization`)](#rule-OEVelarPalatalization) and, farther on, by
[fronting under i-umlaut (`OEIUmlautFronting`)](#rule-OEIUmlautFronting).

Within the present implementation, this helper rule is not ordered separately
from the broader velar-palatalization rule below. Its chronology is therefore
that of the larger rule it feeds. If the palatalization complex is moved before
Sievers-law syncope, PGmc \emph{*strákkijaną} yields *strecċan* ‘stretch’ rather
than expected OE *streċċan* ‘stretch’. If it is delayed beyond the umlautal
core, PGmc \emph{*kūi} and \emph{*lúnganjō} yield *ċȳ* ‘cows’ and *lunġen*
‘lungs’ rather than expected OE *cȳ* and *lungen*. The shared boundary pattern
is therefore `SC050 < SC052 < SC055`.

## SC052. Velar palatalization before front vowels (`OEVelarPalatalization`) {#rule-OEVelarPalatalization}

The broader rule adds the `g` environments and composes them with the `k`
palatalization rule above.

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

In prose, the rule palatalizes plain `k` and `g` in front-vocalic and
`j`-adjacent environments. Writing it as a separate rule clarifies the relative
order of plain-velar palatalization, `sk`-palatalization, and umlautal
developments.

The rule belongs after the earlier syncope that prepares forms like *streċċan*
‘stretch’ and before the later umlautal rules that would otherwise
over-palatalize forms such as *cȳ* ‘cows’ and *lungen* ‘lungs’. See [fronting
under i-umlaut (`OEIUmlautFronting`)](#rule-OEIUmlautFronting) and [the
composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut) below.

If the rule is moved too early, before the syncope that prepares the consonant
cluster, it breaks the derivation that should yield *streċċan* ‘stretch’. With
PGmc \emph{*strákkijaną} in the wrong order, the model produces *strecċan*
‘stretch’; the expected Old English form is *streċċan* ‘stretch’.

If it is moved too late, after i-umlaut, it over-palatalizes forms such as
*cȳ* ‘cows’ and *lungen* ‘lungs’. PGmc \emph{*kūi} then yields *ċȳ* ‘cows’;
the expected form is *cȳ* ‘cows’. PGmc \emph{*lúnganjō} yields *lunġen*
‘lungs’; the expected form is *lungen* ‘lungs’.

These lexical failures give the earlier boundary `SC050 < SC052` and the
later boundary `SC052 < SC055`.

Once the rule is in place, plain velars before front vowels and `j` no longer
remain plain. They become the palatal outcomes presupposed by later
developments, including the umlautal rules discussed in [fronting under
i-umlaut (`OEIUmlautFronting`)](#rule-OEIUmlautFronting). That matters for
dictionary-like forms such as *cild* ‘child’ or *dæg* ‘day’ and for the broader
relation between consonantal palatalization and later vowel-fronting processes
[@Luick1914, p. 157, §168; @Campbell1959, p. 278, §440; @RingeTaylor2014,
pp. 203--215, §§6.4.1, 6.5.1].

The evidence places the rule within a wider palatalizing environment, but it
does not require every neighboring palatal process to be merged with it. `sk`
belongs to a related but distinct development, and the later umlautal material
poses a different historical problem. The relation to the earlier syncope rule
is likewise specific and limited: the *streċċan* ‘stretch’ evidence shows a real
dependency without turning the feeder process into a coequal sound law of the
same scope.

\newpage

# The pre-umlaut bridge and loss of \emph{*w} before \emph{*i}

## Historical discussion

The two rules gathered here are unequal in weight. The first is a narrow loss of
\emph{*w} after velars in the \emph{*ngw} sequence. Ringe and Taylor make the historical core
clear when they derive PGmc \emph{*singwan} to Old English *singan* ‘sing’
[@RingeTaylor2014, p. 214, §6.4.2]. That gives the change a real comparative anchor, but
it does not turn it into a large chapter of its own. It is the kind of small
cleanup rule that needs a place in the sequence without claiming the status of a
major handbook law.

The second rule is historically more legible. Campbell notes the recurring loss
of \emph{*w} before \emph{*i} in unstressed position [@Campbell1959, p. 167, §406]. Ringe and Taylor
trace the development of *sǣ* ‘sea’ from earlier \emph{*saiwi-} / \emph{*sawi-}
[@RingeTaylor2014, p. 257, §6.7.1], and Luick gives the same trajectory in his own
historical grammar [@Luick1914, p. 173, §187]. The chapter therefore belongs in the
stretch between plain palatalization and the umlautal core, but it should keep
the asymmetry visible: the first rule is a narrow bridge, the second is a
stronger glide-loss development with a specific lexical witness.

## SC053. Loss of \emph{*w} after velars (`OEPostVelarWLoss`) {#rule-OEPostVelarWLoss}

The first rule handles the \emph{*ngw} simplification.

```foma
define OEPostVelarWLoss [
    {*w} -> 0 || {*n} {*g} _
];
```

In prose, the rule removes \emph{*w} after the velar cluster in forms of the
\emph{*singwan} type.

Historically, this is a very small rule. It keeps developments such as *singan*
‘sing’ visible in the sequence, but it does not create a large family of lexical
breakpoints. Current testing does not recover a positive earlier or later
boundary: the search reaches older material on the left and the later Old
English search limit on the right with no decisive wrong form. If the rule is
moved either earlier or later within the tested sequence, no lexical witness yet
provides a sharper wrong/expected pair. The safest reading is therefore modest:
this is a local bridge rule that belongs before the umlautal chapter without
claiming a sharper chronological slot than the evidence supports.

## SC054. Loss of \emph{*w} before final \emph{*i} (`OEWLossBeforeI`) {#rule-OEWLossBeforeI}

The second rule is the more historically legible member of the pair.

```foma
define OEWLossBeforeI [
    {*w} -> 0 || EnglishStarVocalic _ {*i} .#.
];
```

In prose, the rule removes non-initial \emph{*w} before final unstressed \emph{*i}.

The best witness is *sǣ* ‘sea’. Campbell's discussion of the loss of \emph{*w} before
\emph{*i}, Ringe and Taylor's derivation from earlier \emph{*saiwi-} / \emph{*sawi-}, and Luick's
parallel account all point to the same historical consequence
[@Campbell1959, p. 167, §406; @RingeTaylor2014, p. 257, §6.7.1; @Luick1914, p. 173, §187]. The glide has
to disappear early enough for the preceding vowel to continue into the later
fronted and lengthened outcome. If the glide survives too long, the derivation
retains \emph{*w} and misses *sǣ* ‘sea’. If the rule is moved before SC020, the
same witness yields *sǣw* ‘sea’ rather than expected OE *sǣ*. This gives the
earlier boundary `SC020 < SC054`. If the rule is delayed until after SC063, the
same witness again yields [*sǣw*]{.pred} rather than expected *sǣ*. This gives the later
boundary `SC054 < SC063`.

This is why the chapter belongs immediately before the broader umlautal
developments discussed in [the composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut).
The two rules together form a genuine bridge into that later vowel chapter, but
only the second has a strong lexical and handbook footing of its own.

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

The sequence of discussion is fairly clear. Luick, Campbell, and Hogg all give
i-umlaut primary importance. Ringe and Taylor and Fulk then help separate that
major change from the narrower West-Saxon diphthongization that stands beside
it. The literature therefore establishes a large, system-wide umlautal change
and a narrower adjoining process affecting words after initial palatals. That
distinction matters because the two processes act in different environments and
produce different lexical consequences.

## SC055. Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting}

The first component of the implementation handles the broad fronting of vowels
under the influence of following `i` or `j`.

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

In prose, the rule fronts and raises the relevant simple vowels when a following
`i` or `j` provides the trigger.

Historically, this is the most central part of the umlautal development
described by Luick, Campbell, Hogg, Ringe and Taylor, and Fulk. Within the
present implementation it stands after [velar palatalization before front vowels
(`OEVelarPalatalization`)](#rule-OEVelarPalatalization) and before the narrower
West-Saxon palatal-diphthongization rule discussed below.

The handbooks describe the same conditioning environment in different ways but
with the same phonological consequence: a following high front vocoid triggers
the fronting of earlier back vowels. That is why forms such as *fylgan*
‘follow’, *gylden* ‘golden’, *wyrm* ‘worm’, and *giest* ‘guest’ can all be
treated inside the same formal rule even though they belong to different lexical
classes [@RingeTaylor2014, p. 222, §6.6.1; @Campbell1959, pp. 69--72,
§§190--191].

The same ordering logic that governs the umlaut complex governs this component.
If the umlautal rule set is moved before SC052, PGmc \emph{*kūi} yields *ċȳ*
‘cows’ rather than expected OE *cȳ*, and \emph{*lúnganjō} yields *lunġen*
‘lungs’ rather than expected OE *lungen*. At the other edge, the later
West-Saxon diphthongization must follow the umlautal rule set: if that later
rule is moved too early, PGmc \emph{*géftiz} yields *ġieft* ‘gift’ rather than
expected OE *ġift*, and \emph{*skáiθiz} yields *sċǣþ* ‘sheath’ rather than
expected *sċēaþ*. This gives the
shared boundary pattern `SC052 < SC055 < SC056`.

As a component rule, it shares the chronology of [the composite i-umlaut rule
(`OEIUmlaut`)](#rule-OEIUmlaut).

## SC055. Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

The second component handles the raising of umlauted `æ` to `e`.

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

In plain language, this rule takes the fronted low vowel created by the earlier
fronting rule and raises it further where the same umlaut trigger still holds.

Historically, this belongs inside the same broad i-umlaut development. It is
part of the same chronological development and shares the evidence base of [the
composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut).

Like the fronting component, this raising rule belongs inside `SC052 < SC055 <
SC056`. If the umlaut complex is moved before SC052, \emph{*kūi} yields [*ċȳ*]{.pred}
instead of expected *cȳ* and \emph{*lúnganjō} yields [*lunġen*]{.pred} instead of
expected *lungen*. If the later West-Saxon diphthongization is moved too early,
\emph{*géftiz} yields [*ġieft*]{.pred} rather than expected *ġift*, and \emph{*skáiθiz}
yields [*sċǣþ*]{.pred} rather than expected *sċēaþ*.

This narrower subrule matters because the sources do not describe umlaut as
simple fronting alone. Campbell explicitly notes that the low front vowel
changes again before `m` and `n` in most dialects [@Campbell1959, p. 69, §190],
and Hogg likewise treats short front vowels as part of the same assimilatory
system [@HoggPhonology1992, p. 112].

## SC055. Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong}

The third component handles the diphthongal outcomes that also undergo
i-umlaut.

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

In prose, the rule states that diphthongal inputs are subject to umlaut as well:
the vowel change is not confined to simple vowels.

This matters historically because the handbooks describe i-umlaut as a
system-wide assimilatory development. The rule therefore stands inside the same
chronological bracket as [fronting under i-umlaut
(`OEIUmlautFronting`)](#rule-OEIUmlautFronting) and [raising under i-umlaut
(`OEIUmlautRaising`)](#rule-OEIUmlautRaising), even though its outputs are
shaped differently.

The relevant examples are the recurring West-Saxon `ie` forms cited in the
handbooks, including *giest* ‘guest’, *giefan* ‘give’, and *hierde*
‘shepherd’ in Campbell and *ciest* ‘chest’ in Hogg
[@Campbell1959, pp. 69--72, 78--80, §§190--191, 248--251; @HoggPhonology1992,
pp. 112--114]. The present formalization keeps those diphthongal outcomes
visible as a distinct part of the general umlautal development and does not
leave them implicit under the broad description of fronting.

Chronologically, this component also shares the same evidence as the umlaut
complex as a whole. If the umlaut complex is moved before SC052, it
over-palatalizes
\emph{*kūi} and \emph{*lúnganjō}; too-early West-Saxon diphthongization yields
*ġieft* and *sċǣþ* instead of expected *ġift* and *sċēaþ*. The rule therefore
belongs within `SC052 < SC055 < SC056`.

## SC055. The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

The implementation also defines a composite rule that composes the three
preceding parts.

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

In prose, this says that the implementation treats the umlaut as a sequence of
fronting, raising, and diphthongal adjustments composed in order.

Chronologically, the composite rule must follow [velar palatalization before
front vowels (`OEVelarPalatalization`)](#rule-OEVelarPalatalization). If it is
moved too early, forms such as *cȳ* ‘cows’ and *lungen* ‘lungs’ become
over-palatalized. PGmc \emph{*kūi} yields *ċȳ* ‘cows’; the expected form is
*cȳ* ‘cows’. PGmc \emph{*lúnganjō} yields *lunġen* ‘lungs’; the expected form
is *lungen* ‘lungs’.

The same local network gives the later boundary. If West-Saxon palatal
diphthongization is moved too early, PGmc \emph{*géftiz} yields *ġieft* ‘gift’
rather than expected OE *ġift*, and \emph{*skáiθiz} yields *sċǣþ* ‘sheath’
rather than expected *sċēaþ*. The composite umlaut rule therefore occupies `SC052 <
SC055 < SC056`.

Those failures show that the broad umlautal rule needs an earlier terminus post
quem in the palatalization sequence, even though it remains the main vowel
change within the present chapter.

The composite rule is important because the literature presents the umlaut as a
single historical development even while the implementation decomposes it into
formal parts. The composite definition is the point at which the separate
fronting, raising, and diphthongal effects are treated as one chronological
event in the Old English sequence.

## SC056. West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization}

The narrower West-Saxon rule is treated separately from the broader umlautal
complex.

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

In prose, this rule diphthongizes certain vowels after already palatal
consonants in West Saxon. It therefore has a narrower dialectal and
chronological scope than the broader umlaut rule.

The historical evidence for that narrower scope is concrete. Ringe and Taylor
illustrate the rule with forms such as *gieldan* ‘pay’, *scield* ‘shield’, and
*scieppan* ‘create’, where an already palatal consonant triggers the diphthongal
outcome [@RingeTaylor2014, pp. 215--216, §6.5.1]. Hogg’s *giefan* ‘give’ and
*sceap* ‘sheep’ material belongs to the same phonological zone
[@HoggPhonology1992, p. 112], while Fulk distinguishes this
palatal-consonant-triggered diphthongization from the broad front-mutation
process [@Fulk2018, p. 74, §4.13].

Its place is later than [the composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut).
If this rule is moved too early, the later ordering is constrained by forms such
as *ġift* ‘gift’ and *sċēaþ* ‘sheath’. PGmc \emph{*géftiz} then yields
*ġieft* ‘gift’; the expected form is *ġift* ‘gift’. PGmc \emph{*skáiθiz}
yields *sċǣþ* ‘sheath’; the expected form is *sċēaþ* ‘sheath’.

This gives the earlier boundary `SC055 < SC056`. No comparably sharp later
boundary is available.

No tested lexical item provides a comparably precise later terminus ante quem.
The available evidence therefore establishes the rule’s relation to the earlier
umlautal process much more clearly than it fixes a later point by which it must
already have applied.

The two rules should accordingly be kept distinct. The broad umlautal rule
accounts for a system-wide assimilatory change; the West-Saxon rule accounts for
a narrower palatal-consonant-conditioned diphthongization whose chronological
and dialectal scope is more restricted.

\newpage

# J-cluster coalescence

## Historical discussion

This chapter belongs to the later part of the palatalization and fronting
region. Campbell, Ringe and Taylor, and Fulk all discuss the same neighborhood
of palatalized and fronted outcomes that underlies forms such as *bīeġan*
‘bend’ and *sēċan* ‘seek’ [@Campbell1959, pp. 89, 107--108, §§170, 248--251;
@RingeTaylor2014, pp. 213--251, §§6.4.1, 6.5.1, 6.6.1--6.6.4; @Fulk2018, pp. 65, 75, §§4.7, 4.13]. None
of them turns this later cluster adjustment into a major independent headline.
The historical interest lies in the fact that it remains a real part of the
sequence even though the larger palatalization and umlaut chapters carry more of
the explanatory weight.

That narrower scale matters. Earlier chapters have already established the plain
velar and \emph{*sk} palatalizations, and the umlaut chapter has already handled the
major vowel consequences. The present rule is a later coalescence inside that
same neighborhood. It deserves explicit prose because the lexical outcomes are
clear, not because it eclipses the larger processes around it.

## SC057. Coalescence of velar + \emph{*j} clusters (`OEJClusterCoalescence`) {#rule-OEJClusterCoalescence}

The implementation keeps the later cluster coalescence very small and explicit.

```foma
define OEJClusterCoalescence (
    [{*g} {*j} -> {*ʤ}]
    .o. [{*k} {*j} -> {*ʧ}]
);
```

In prose, the rule coalesces \emph{*gj} and \emph{*kj} into the palatal outcomes that later
surface in forms such as *bīeġan* ‘bend’ and *sēċan* ‘seek’.

Its earlier dependency is clearer than its later limit. If the rule is moved
before [velar palatalization before front vowels (`OEVelarPalatalization`)](#rule-OEVelarPalatalization),
the developments behind *bīeġan* ‘bend’ and *sēċan* ‘seek’ are lost. Related forms such as *fylġan* ‘follow’,
*heċġ* ‘hedge’, and *sengan* ‘singe’ fail in the same broader palatalization
zone. PGmc `*báugijaną` yields *bēaġan* ‘bend’ rather than expected OE *bīeġan*,
and PGmc `*sōkijaną` yields *sōċan* ‘seek’ rather than expected *sēċan*. This
gives the earlier boundary `SC052 < SC057`. No comparably sharp later lexical
breakpoint emerges within the remaining sequence, so the chronology remains
short and one-sided.

That modest shape is historically appropriate. The rule is a real later member
of the palatalization region, but it does not need to absorb the umlautal
chapter behind it or the nasal-dissimilation chapter that follows it. The
later coalescence remains visible in the sequence once the
larger neighboring chapters are already in place.

\newpage

# Nasal dissimilation

## Historical discussion

Luick preserves individual outcomes such as *enetre* ‘yearling’ (with the
spelling *enitre* in his text) without isolating a separate law around them
[@Luick1914, p. 166]. Campbell likewise reaches forms such as *heofon* ‘heaven’
in a discussion of suffixal variation and does not set them off in any special
section on nasal dissimilation [@Campbell1959, p. 155]. Hogg mentions *heofon*
‘heaven’ in the course of his account of back mutation, again without isolating
a separate law [@HoggPhonology1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that *enetre* ‘yearling’ reflects “loss of the second
\emph{*n} by dissimilation” [@RingeTaylor2014, p. 282].

The discussion therefore develops from scattered lexical observations to a more
explicit but still cautious generalization. Luick preserves the kind of form the
rule is meant to capture. Campbell and Hogg show that related outcomes enter the
handbooks, but only incidentally, as part of larger accounts of other changes.
Fulk makes the recurrent `mn` tendency explicit, while Ringe and Taylor provide
an exact lexical case in *enetre* ‘yearling’. What emerges is a limited but
recurring dissimilatory pattern whose scope is far smaller than that of the
major Old English vowel laws.

## SC058. Nasal dissimilation in short-vowel environments (`OENasalDissimilation`) {#rule-OENasalDissimilation}

The implementation formalizes the change as a narrow rule applying in short
vowel environments before a following `n`.

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

In plain language, the rule turns medial `m` into `f` in a restricted
short-vowel environment before a following syllable containing `n`.

Historically, the rule captures the limited type of dissimilation reflected in
forms such as *heofon* ‘heaven’, *fæstenn* ‘fasting’, and *enetre* ‘yearling’.
It is much narrower than the major vowel changes and is best understood as a
recurring but partly lexicalized pattern.

The relation between the sources and the formalization is correspondingly close
but not exact. Fulk formulates the tendency at the level of `mn` clusters and
illustrates it with *heofon* ‘heaven’ and *fæstenn* ‘fasting’
[@Fulk2018, p. 121, §6.11]. Ringe and Taylor show the same kind of development
in *enetre* ‘yearling’ [@RingeTaylor2014, p. 282]. Campbell’s “heofon is for
older hefzen” and Hogg’s sequence \emph{*hefon > heofon} preserve outcomes
of the same kind as those modeled here [@Campbell1959, p. 155;
@HoggPhonology1992, p. 112]. The formal rule is therefore narrower than the total set of
handbook remarks: it models one plausible recurrent environment and does not
claim to exhaust every dissimilatory development involving nasals.

Chronologically, the available tests do not identify a sharper position within
the Old English sequence. When the rule is moved earlier, no lexical breakpoint
appears before the inherited West-Germanic material that precedes the tested Old
English changes. When it is moved later, the tests likewise fail to identify a
more precise later boundary within the remainder of the Old English sequence.

No comparable pair of lexical failures fixes a narrower slot here. The present
evidence therefore gives neither a precise terminus post quem nor a precise
terminus ante quem for the rule within the tested sequence. No exact wrong early
or late output is currently available for this chapter.

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the *heofon* ‘heaven’, *fæstenn* ‘fasting’,
and *enetre* ‘yearling’ type discussed in the literature [@Fulk2018, p. 121,
§6.11; @RingeTaylor2014, p. 282; @Campbell1959, p. 155; @Luick1914, p. 166;
@HoggPhonology1992, p. 112]. Without an explicit rule, those outcomes would be left to
diffuse analogy or to unexplained exception lists.

The evidence points to a narrow dissimilatory tendency, especially in `mn`-type
clusters and a small group of lexical outcomes. There is no support for a
regular change operating across a broad phonological field. The rule is secure
enough to model, but the available tests leave its position within the Old
English sequence underdetermined.

\newpage

# Back mutation

## Historical discussion

Back mutation is the substantive center of this part of the sequence. Campbell treats
it as a later Old English diphthongizing development before following back
vowels, and his examples already show why forms such as *heofon* ‘heaven’ are
historically legible outcomes in their own right
[@Campbell1959, p. 86, §207]. Hogg treats the same development as a later change with
clear parallels to breaking [@HoggPhonology1992, p. 112]. Ringe and Taylor sharpen the
picture by distinguishing West Saxon forms such as *giefan* ‘give’ and *wefan*
‘weave’ from non-West-Saxon forms such as *geofad* and *weofan*
[@RingeTaylor2014, p. 319, §6.9.4]. Fulk likewise treats back mutation as a distinct
historical phenomenon with its own profile beside the earlier umlautal
changes [@Fulk2018, p. 69, §4.8].

That makes back mutation different from the short notes that follow it. Back
mutation belongs to the same local stretch of the sequence, but it carries more
historical weight and clearer lexical consequences. Even so, its later relation
lies beyond this immediate stretch of the sequence, and the later weak-tail
region is best kept as a forward reference only.

## SC059. Back mutation before labials and liquids (`OEBackMutation`) {#rule-OEBackMutation}

The implementation keeps the change as one explicit rule.

```foma
define OEBackMutation [
    {*e} -> {*eo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u},
    {*æ} -> {*ea} || _ [EnglishStarLabial | EnglishStarLiquid] EnglishBackMutationTrigger,
    {*é} -> {*éo} || _ [EnglishStarLabial | EnglishStarLiquid] {*u}
];
```

In prose, the rule backs and diphthongizes earlier front vowels before a
following labial or liquid plus a back-vocalic trigger.

Its chronology is real on both sides, but not equally local. The earlier side is
already fixed by the preceding vowel and weak-tail material. If the rule is
moved too early, forms such as \emph{*gébaną} produce *ġeofan* ‘give’; the
expected form is *ġiefan* ‘give’. \emph{*stélaną} likewise produces *steolan*
‘steal’; the expected form is *stelan* ‘steal’. The later side is different. If
the rule is pushed too far to the right, \emph{*wébaną} yields *weofan*
‘weave’; the expected form is *wefan* ‘weave’.
That later edge is real, but it points beyond the present stretch of the sequence into the
later weak-tail reductions, so here it should remain only a forward reference.

These lexical failures give the earlier boundary `SC048 < SC059` and the later
boundary `SC059 < SC078`.

This is why the change can serve as the center here without implying that the
following weak-tail notes belong to the same historical law. The rule
marks a real local seam, but the section after it immediately becomes narrower.

\newpage

# West Saxon palatal umlaut

## Historical discussion

The evidence is narrow enough that the discussion can stay brief. Campbell and Ringe and Taylor both support the
development behind forms such as *miht* ‘might’ and *niht* ‘night’, while Fulk's
broader chronology makes clear that this material belongs beside the umlaut and
palatal-vowel region as a subordinate note beside it
[@Campbell1959, pp. 107--108, §§248--251; @RingeTaylor2014, pp. 215--251, §§6.5.1, 6.6.1--6.6.4;
@Fulk2018, pp. 65, 75, §§4.7, 4.13].

That is why the note belongs here after back mutation even though its clearest
historical tie still reaches back to the earlier umlautal chapter. The
phenomenon is real, yet its place in the sequence is one-sided. The evidence is
clear enough to state and narrow enough to remain brief.

## SC060. West Saxon palatal umlaut before \emph{*h}-clusters (`OEWsPalatalUmlaut`) {#rule-OEWsPalatalUmlaut}

The implementation treats the West Saxon change as one explicit rule.

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

In prose, the rule reduces short diphthongs to \emph{*i} before the relevant \emph{*h}
clusters.

The crucial point is its earlier dependency. The rule must follow [the composite
i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut), because if it is moved too early
the forms behind *miht* ‘might’ and *niht* ‘night’ remain at the overdeveloped
stage *mieht* and *nieht* rather than expected OE *miht* and *niht*. No comparably sharp later lexical breakpoint emerges
within the remainder of the section. The note therefore belongs here as a short
afterpiece to the umlaut chapter, not as the start of a new larger unit.

This gives the earlier boundary `SC055 < SC060`. No comparably sharp later
boundary is available.

\newpage

# Weak-tail nasal loss

## Historical discussion

The development belongs to the narrower end of the later weak-tail sequence. It is historically
legible through the pathway that leads to *dōn* ‘do’, and the broader late
weak-tail setting is supported by the usual handbook discussions of apocope and
related reduction [@Campbell1959, pp. 144--145, §§345--349; @HoggPhonology1992, p. 121;
@Fulk2018, p. 91, §5.6]. But the decisive lexical tie lies much farther back in the
sequence, in the older development of \emph{*dōną}. That keeps the note real,
while also keeping it small.

Within this later run of changes it follows back mutation and West Saxon
palatal umlaut, but the evidence remains slighter than theirs.

## SC061. Reduction of final nasal weak-tail endings (`OEWeakTailNasalLoss`) {#rule-OEWeakTailNasalLoss}

The implementation keeps the change as one short rule.

```foma
define OEWeakTailNasalLoss [
    {*n} {*ą} -> {*n} || _ .#.,
    {*m} {*ą} -> {*m} || _ .#.
];
```

In prose, the rule reduces final weak-tail endings of the type \emph{*-ną} and
\emph{*-mą} to plain final \emph{*-n} and \emph{*-m}.

The clearest lexical witness is the pathway to *dōn* ‘do’. If the rule is moved
too early, before the older reduction that already shapes the \emph{*dōną}
sequence,
the derivation records no output instead of expected OE *dōn* ‘do’. No equally
sharp later breakpoint appears within the tested sequence. That is why the note remains
one-sided and why its earlier relation should be understood as a distant
cross-reference only and should not reshape the broader sequence.

This gives the earlier boundary `SC023 < SC061`. No comparably sharp later
boundary is available.

The development is best treated as a small late weak-tail adjustment. It remains
visible in the sequence because it affects the pathway to *dōn* ‘do’, but the
evidence does not support treating it as the center of a wider historical
development.

\newpage

# References

::: {#refs}
:::
