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
