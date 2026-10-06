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
