# Class-distinct velar palatalization and fricative merger

## Historical discussion

Singleton g, including initial g, was a fricative when palatalization
occurred; gg and postnasal g were stops. Palatal articulation, productive
cutoff, merger and later affrication are therefore separate questions
[@Fulk2018, pp. 130--132; @Laker2007, pp. 166--168, 175--184].
The dotted spelling in *dæġ* 'day' cannot establish an early affricate or
identify every palatal consonant with inherited j.

The adopted working account keeps a palatal fricative ʝ distinct from j
during mutation, then merges it with j. Ringe and Taylor explicitly propose
this chronology [@RingeTaylor2014, pp. 203--204]. It is not unanimous:
Hogg objects to the phonetic plausibility of delayed merger and leaves the
key/day contradiction unresolved [@Hogg1979, pp. 102--111].
We prefer the regular class-distinct account because it explains the
contrasting mutation triggers without lexical or grammatical conditions.
The objection remains substantive, not silently superseded by a matching
final spelling.

Eligibility also requires attribution. Ringe and Taylor's medial-g table
is narrower than Fulk's before-front-vowel description
[@RingeTaylor2014, pp. 203--204; @Fulk2018, pp. 130--132].
The present fricative implementation retains its broader domain; this
merger decision is not a covert adoption of the narrower table.

## SC052. Singleton-fricative articulation (`OEGFricativePalatal`) {#rule-OEGFricativePalatal}

```foma
define OEGFricativePalatal [
    [{*g}|{*ɣ}] -> {*ʝ} ||
        [.#.|[EnglishStarAlphabet - [{*g}|{*n}|{*ŋ}]]]
        _ EnglishStarFrontVowel,
    [{*g}|{*ɣ}] -> {*ʝ} || EnglishStarFrontVowel _ .#.,
    [{*g}|{*ɣ}] -> {*ʝ} || EnglishStarFrontVowel
        _ [EnglishStarConsonant - [{*j}|{*g}]]
] .o. [
    [{*g}|{*ɣ}] -> {*ʝ} ||
        [.#.|[EnglishStarAlphabet - [{*g}|{*n}|{*ŋ}]]] _ {*j}
];
```

The guards keep gg/ng in their stop paths. The value ʝ is a real phonetic
class, not a tag recording a consonant's ancestry. It is transparent to a
following mutation trigger, but is not itself j at that date.
The source comparison normalizes older fricative notation to modern ɣ/ʝ,
never to the digit 3 [@Hogg1979, p. 105; @RingeTaylor2014, p. 204].

## SC052. K articulation and eventual reflex (`OEVelarPalatalizationKFront`) {#rule-OEVelarPalatalizationKFront}

```foma
define OEVelarPalatalizationKFront [
    {*k} -> {*ʧ} || .#. _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || _ [{*i} | {*ī}],
    {*k} -> {*ʧ} || _ {*ḯ},
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || {*ḯ} _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ .#.,
    {*k} -> {*ʧ} || {*ḯ} _ .#.
] .o. [
    {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j}
] .o. [
    {*k} -> {*ʧ} || _ {*j}
];
```

Here ʧ is a telescoped eventual-reflex proxy, not a claim that early
palatal stops were already affricates. Ringe and Taylor explicitly separate
the initial palatal stop from subsequent affrication and its syncope
dependencies [@RingeTaylor2014, pp. 203--204].
The *weccan* 'wake', *licgan* 'lie' and *lecgan* 'lay' examples concern
inherited j-clusters, not independent proof of every plain-velar conditioner
[@RingeTaylor2014, pp. 213--214].

The deterministic kk-before-j path protects *streċċan* 'stretch'.
The original-front versus secondary-front distinction is more directly
tested by unrounded key than by rounded *cȳ* 'cow'; rounding alone can
give only a cutoff before later unrounding
[@Hogg1979, pp. 100--105; @Laker2007, pp. 167--168].

## SC052. Retained stop paths (`OEVelarPalatalizationStops`) {#rule-OEVelarPalatalizationStops}

```foma
define OEVelarPalatalizationStops [
    OEVelarPalatalizationKFront
] .o. [
    {*g} -> {*ʤ} || _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ [EnglishStarConsonant - {*j}],
    {*g} {*g} -> {*ʤ} {*ʤ} || _ {*j}
] .o. [
    {*g} -> {*ʤ} || _ {*j}
];
```

Singleton fricatives have already left this domain. The remaining gg/ng
paths use ʤ as an eventual-reflex proxy; the initial singleton fricative
is no longer represented as an early affricate. *Wicg* 'horse' is a
geminate-class illustration, *senġan* 'singe' a postnasal control, and
*lungen* 'lung' the unchanged back-vowel negative
[@RingeTaylor2014, pp. 203--204, 213--214; @Fulk2018, pp. 131--132].

## SC052. Combined articulation (`OEVelarPalatalization`) {#rule-OEVelarPalatalization}

```foma
define OEVelarPalatalization [
    OEGFricativePalatal .o. OEVelarPalatalizationStops
];
```

The combined operation does not give every class one sharply dated
palatalization/affrication/merger event. It supplies the class distinctions
needed by ordinary palatal diphthongization and mutation.
The common-stem onset remains a separate question
[@Luick1914, pp. 835--841; @Fulk2018, pp. 130--132].

### Key and day at the mutation checkpoint

Hogg's oblique comparison starts here from pre-palatal, pre-OE
\emph{*kājæ} and \emph{*dæɣæ}; neither is silently fed through a PGmc
prefix [@Hogg1979, p. 105]. The source target is *cǣġe* 'key',
with velar initial k, versus *dæġe* 'day'.

| Checkpoint | Key | Day under the adopted account |
|---|---|---|
| Before palatalization | \emph{*kājæ} | \emph{*dæɣæ} |
| Before mutation | Inherited j remains | Palatal ʝ is distinct from j |
| After mutation | \emph{*kǣjæ}, without new initial palatalization | \emph{*dæʝæ}, without æ-raising |
| After merger and native realization | *cǣġe* | *dæġe* |

Premature merger instead predicts pre-OE [\emph{*dejæ}]{.pred} under
these premises. The experiment tests that source-based contrast; the
existing day nominative is not the oblique discriminator
[@Hogg1979, pp. 105--110; @RingeTaylor2014, p. 204].

The complete key suffix additionally requires
[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization)
to retain j after its non-high long front vowel. A correct mutation
checkpoint followed by model-only [*cǣie*]{.pred} would not constitute a
correct native derivation [@Hogg1979, p. 105].

## SC109. Postmutation merger serialization (`OEPalatalFricativeMerger`) {#rule-OEPalatalFricativeMerger}

```foma
define OEPalatalFricativeMerger [
    {*ʝ} -> {*j}
];
```

The historical commitment is merger after mutation
[@RingeTaylor2014, p. 204]. Its execution after
[SC089 OELateUnstressedAgSuffix](#rule-OELateUnstressedAgSuffix)
is a computational holding zone, not proof of an exact historical date.
It keeps the fricative out of inherited-j normalization while preserving
late palatal raising, syllable weight, reduction and native rendering.
[SC057 OEJClusterCoalescence](#rule-OEJClusterCoalescence) remains a
different cluster process. Stop affrication dates and the precise
disputed eligibility domain are not settled by this merger.
