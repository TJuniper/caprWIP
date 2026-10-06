# Early unstressed vowel changes

## Historical discussion

The first change monophthongizes unstressed \emph{*ai}; the second carries early unstressed front-vowel leveling farther in forms such as *weorold* 'world'. Both have a diagnostic later boundary in the dataset.

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the broad Northwest Germanic reduction of unstressed \emph{*ai} to a long mid vowel that merges with unstressed \emph{*e}, in final and nonfinal syllables alike [@RingeTaylor2014, pp. 37--41]. Two dative-singular endings in the dataset, span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed', carry the change. The stressed development of \emph{*ái} to \emph{*ā} is treated separately as [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## SC014. Monophthongization of unstressed \emph{*ai} (`PNWGmcUnstressedAiMonophthongization`) {#rule-PNWGmcUnstressedAiMonophthongization}

```foma
define PNWGmcUnstressedAiMonophthongization Ctx([
    {*ai} -> {*ē}
]);
```

The dative-singular endings span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed' carry this change; both give a final \emph{*ē}. If [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) is delayed until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), the \emph{*ē} is no longer present for shortening, so PGmc [spánnai]{.recon} 'span' yields [*spannē*]{.pred} rather than expected OE *spanne* 'span'. This shows that [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) in the modeled sequence.

Ringe and Taylor's merger of unstressed \emph{*ai} with long mid \emph{*ē} establishes the historical development, in final and nonfinal syllables alike. The stressed development of \emph{*ái} to \emph{*ā} is a separate and later change; see [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## Historical discussion of early unstressed front-vowel leveling

Campbell treats the merger of unstressed front vowels directly and also records the variation of *weorold* 'world' and *weoruld* 'world' [@Campbell1959, pp. 141--142, 154--155]. These forms supply [SC015 PNWGmcILowering](#rule-PNWGmcILowering) with a firmer lexical basis than the preceding change.

## SC015. Leveling of early unstressed front vowels (`PNWGmcILowering`) {#rule-PNWGmcILowering}

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
