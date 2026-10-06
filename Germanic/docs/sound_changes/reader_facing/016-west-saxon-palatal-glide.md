# West Saxon palatal-glide spelling before back vowels

## Historical discussion

West Saxon spellings such as *ġeoc* 'yoke', *ġeong* 'young', and *ġeoguþ*
'youth' write a front glide letter between a word-initial palatal and a
following back vowel. Campbell describes the phenomenon as the development
of rising diphthongs when "palatal glides developed before back vowels"
and cites *ġeoc* directly [@Campbell1959, p. 17, §44]; Brunner separates
the \emph{u}-cases (*ġeong*, *ġeoguþ*) from the \emph{o}-cases (*ġioc* 'yoke',
*ġeoc*) [@SieversBrunner1965, pp. 64--65, §92.1]; Bülbring likewise treats
*iuguð* 'youth' and *iuc* under \emph{ju} but derives *ġioc*, *ġeoc* from West
Germanic \emph{*jok} [@Bulbring1902, p. 120, §§298--299]; and Luick groups
all of these under his "schwebende Diphthonge" after palatal onsets
[@Luick1914, pp. 158--159, §169].

The phonological interpretation of these spellings is disputed. The older
handbook tradition — Campbell, Brunner, Bülbring, Luick — reads them as
genuine rising diphthongs. The modern assessment is orthographic: Ringe and
Taylor state flatly that *ġeoc* "is /jok/", the digraph being a spelling
convention that became universal after word-initial /j/
[@RingeTaylor2014, p. 5], and Hogg concludes that the back-vowel cases were
"never anything more than an orthographic variation", judging Campbell's
arguments to the contrary "insubstantial" [@HoggPhonology1992, p. 113;
@Campbell1959, pp. 66--67, §176]. This model follows Ringe and Taylor and
Hogg: the rule is a spelling convention applied to the finished phonology,
and it therefore stands at the end of the derivation, in the written-surface
stage of the cascade.

Its position also settles a relative chronology. The \emph{o} of *ġeoc* 'yoke'
is itself the product of Northwest Germanic u-lowering
([SC017 PNWGmcULowering](#rule-PNWGmcULowering)): Fulk lists *ġeoc* as a
regular lowering example beside OIcel *ok* and OHG *joh*
[@Fulk2018, p. 56, §4.3], and Campbell gives *ġeoc* among the regular
\emph{u} > \emph{o} words [@Campbell1959, p. 43, §115]. The lowering
therefore feeds the spelling: first \emph{*juk-} became \emph{*jok-} in
Northwest Germanic, and only much later did West Saxon scribes write the
result as *ġeoc*. Where lowering did not apply, as in *ġeoguþ* 'youth',
whose root \emph{u} was protected by the high vowel of the following
syllable, the same convention wrote the retained \emph{u} with the same
digraph [@SieversBrunner1965, pp. 64--65, §92.1].

## SC016. West Saxon palatal-glide spelling before back vowels (`OEWsPalatalGlide`) {#rule-OEWsPalatalGlide}

```foma
define OEWsPalatalGlide [
    {*ó} -> {*éo} || .#. ġ _ ,
    {*ú} -> {*éo} || .#. ġ _ ,
    {*o} -> {*eo} || .#. ġ _ ,
    {*u} -> {*eo} || .#. ġ _
];
```

The rule rewrites a back vowel after word-initial \emph{ġ} as the digraph
spelling, covering both the lowered \emph{o}-cases (*ġeoc* 'yoke') and the
retained \emph{u}-cases (*ġeoguþ* 'youth'). Because it is a convention of the
written language, it applies after every phonological change; in
particular it follows [SC017 PNWGmcULowering](#rule-PNWGmcULowering),
which supplies the \emph{o} of *ġeoc*. If the spelling rule were placed
before u-lowering, the derivation would have to treat an Old English
scribal practice as a Northwest Germanic sound change, an ordering that
no source supports. The witnesses *ġeoc* and *ġeoguþ* between them fix
both faces of the rule: one shows the convention applied to lowered
\emph{o}, the other to unlowered \emph{u}. The handbook domain is broader
(it also includes \emph{a}/\emph{ā}/\emph{ō} contexts after word-initial
palatals), but this executable rule is intentionally complete for the
currently selected corpus witnesses rather than a maximal dialectal
enumeration.
