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

## SC056. West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization}

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
