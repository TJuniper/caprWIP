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
