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
