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
