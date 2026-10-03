# Inherited short-vowel-plus-geminate-glide reanalysis

## Historical discussion

Inherited geminate glides after short vowels underwent reanalysis in
Proto-West Germanic: the first glide became the offglide of a diphthong,
while the second remained consonantal. This is not simply deletion of one
\emph{w}, and it is not the later English realization of the new diphthong.
Ringe and Taylor distinguish those histories explicitly; Fulk specifies
the short-vowel environment ([@RingeTaylor2014, pp. 41--42, 65--66,
171--175; @Fulk2018, p. 117]).

Coronal assimilation feeds the change in *fēower* 'four' and *ēow* 'you':
[SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) supplies
the geminate that becomes \emph{eu+w} or \emph{iu+w}. Inherited geminates
also supply the histories of *ċēowan* 'chew', *dēaw* 'dew' and *hēawan*
'hew'. The resulting diphthongs enter the separate English realization
described under [SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling)
([@RingeTaylor2014, pp. 41--42, 65--66, 172--175;
@Campbell1959, pp. 45--47]).

Homorganic \emph{uww} requires a separate quantity decision. We adopt
Ringe and Taylor's preferred long-\emph{u} account for *sċūwa* 'shadow',
but retain their qualification of its evidence rather than treating the
quantity as independently certain. Hypothetical inherited long-vowel-plus-
\emph{ww} sequences are not additional reconstructed witnesses: the held
description specifies inherited geminates after short vowels. The
parallel inherited \emph{jj} development is independently governed and
is not changed here ([@RingeTaylor2014, pp. 65--66; @Fulk2018, p. 117]).

## SC031. Inherited short-Vww reanalysis (`OEWWSimplification`) {#rule-OEWWSimplification}

```foma
define OEWWSimplification Ctx([
    {*a} {*w} {*w} -> {*au} {*w},
    {*á} {*w} {*w} -> {*áu} {*w},
    {*e} {*w} {*w} -> {*eu} {*w},
    {*é} {*w} {*w} -> {*éu} {*w},
    {*i} {*w} {*w} -> {*iu} {*w},
    {*í} {*w} {*w} -> {*íu} {*w},
    {*u} {*w} {*w} -> {*ū} {*w},
    {*ú} {*w} {*w} -> {*ū} {*w}
]);
```

The transport wrapper carries an independently selected sentence context
outside the segmental rewrite; it adds no reconstructed sound and does not
condition the reanalysis. Acute and unmarked spellings are notation
variants, not alternatives in sentence stress. The retained executable
name likewise does not determine the historical stage.

The modeled position after coronal assimilation and before j-gemination
is a representative serialization that keeps inherited/coronal-created
geminates distinct from the subsequently created j-path. It is not a
newly proved strict chronology between the whole events. *Hīeġ* 'hay'
and reconstructed West Saxon strew retain the separately adjudicated
[SC029 OEAwwjResolution](#rule-OEAwwjResolution) path. *Hīew* 'hue'
retains its independently governed realization and the explicitly
disclosed [SC106 OEJWWSimplification](#rule-OEJWWSimplification) residual
([@Campbell1959, pp. 45--47; @RingeTaylor2014, p. 173]).

For you, early \emph{iu+w} now reaches
[SC098 PWGmcUnstressedWordFinalIApocope](#rule-PWGmcUnstressedWordFinalIApocope).
Its weak-final context, not the former presence of literal \emph{ww},
licenses apocope before mutation. Earlier source-backed reanalysis thus
coexists with genuine prosodic conditioning rather than an output-restoring
segment proxy ([@RingeTaylor2014, pp. 41--42, 55, 57--58]).
