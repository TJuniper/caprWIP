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

## SC043. Fronting of low \emph{*a} outside nasal environments (`EAFBrightening`) {#rule-EAFBrightening}

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
