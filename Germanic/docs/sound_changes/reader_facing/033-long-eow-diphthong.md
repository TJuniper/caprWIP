# Long \emph{ēow} before following vowels

## Historical discussion

Four distinct developments shape the West Saxon diphthongal field. Campbell
discusses inherited \emph{aw}/\emph{ew} outcomes, palatal-triggered
diphthongization, and later Anglian smoothing in connected but separate parts
of the vowel history; Hogg likewise distinguishes the palatal-diphthongal
developments [@Campbell1959, pp. 46, 53--54, 65--70, 95--96,
§§120, 135--136, 170--176, 185, 223--227; @HoggPhonology1992, pp. 112--113].

Earlier inherited-glide reanalysis is now distinct from the retained
singleton and j-created realization. *Dēaw* 'dew' and *hēawan* 'hew'
pass through early au+w and later English completion, rather than late
literal ww deletion followed by the singleton aw operation
([@RingeTaylor2014, pp. 65--66, 172--175]).

The long \emph{ēow} forms of *ċēowan* ‘chew’, *fēower* ‘four’, and *cnēow*
‘knee’ form part of the West Saxon vowel history, although their clearest
ordering relation points forward. Campbell describes early \emph{eu} in Old
English, and Ringe and Taylor give the corresponding examples from chew,
four, and knee [@Campbell1959, pp. 53--54, §136;
@RingeTaylor2014, pp. 188, 202].

The early chew/four inputs now complete through
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling). The retained
[SC033 OEEwLongDiphthong](#rule-OEEwLongDiphthong) population is knee
and the independently governed j-created hue path; historical displacement
results for the former larger population do not become new dates for
this narrower operation.

## SC033. Long \emph{ēow} before following vowels and weak endings (`OEEwLongDiphthong`) {#rule-OEEwLongDiphthong}

```foma
define OEEwLongDiphthong [
    {*e} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*i} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*é} {*w} -> {*ēo} {*w} || _ OEEwLongContext,
    {*í} {*w} -> {*ēo} {*w} || _ OEEwLongContext
];
```

*Cnēow* 'knee' supplies the retained singleton contrast. *Hīew* 'hue'
retains a separate j-created sequence; the promoted long-diphthong input
still contains ww before j. Neither is a new application of inherited
short-Vww reanalysis. The source's distinctions between inherited
geminates, singleton/contraction products and later j-created sequences
remain necessary even when their English spellings converge
([@Campbell1959, pp. 45--47; @RingeTaylor2014, pp. 173--174]).

## SC106. Retained j-created glide residual (`OEJWWSimplification`) {#rule-OEJWWSimplification}

```foma
define OEJWWSimplification [
    {*w} {*w} -> {*w} || _ {*j}
];
```

This visibly retained technical operation simplifies hue's remaining
ww+j representation after promotion. It is not presented as a newly
established historical sound law or an inference from the word's final
spelling. The former unrestricted late ww operation no longer duplicates
the inherited event; its remaining j-created role is explicit and
separate from [SC031 OEWWSimplification](#rule-OEWWSimplification).
