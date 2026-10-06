# SC043 Anglo Frisian Brightening — literature dossier

## Rule metadata
- change_id: SC043
- display_name: Anglo Frisian Brightening
- FOMA rule: AngloFrisianBrightening
- current_order: 43
- historical_stage: Old English (provisional filing; the current taxonomy has no separate Anglo-Frisian bucket)
- pipeline_stage: Old English
- trace_occurrence_count: 89
- example_lexemes: bake, bast, bath, beard, belly; additional compact-trace slices show day, father, far, fall
- aliases searched: Anglo Frisian Brightening; Anglo-Frisian Brightening; Anglo-Frisian brightening; first fronting; First Fronting; a-fronting; fronting of a; Germanic a to æ; West Germanic a; Old English æ; breaking after fronting; restoration of a; retraction; A-restoration; Campbell first fronting; Hogg first fronting; Ringe Taylor first fronting

## FOMA definition

```foma
define AngloFrisianBrighteningUnstressed [
    {*a} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal]
];
define AngloFrisianBrighteningStressed [
    {*á} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal | .#.]
];
define AngloFrisianBrighteningLongFinal [
    {*ā} -> {*ǣ} || _ .#.
];
define AngloFrisianBrightening [
    AngloFrisianBrighteningUnstressed .o.
    AngloFrisianBrighteningStressed .o.
    AngloFrisianBrighteningLongFinal
];
```

## Working description

The live transducer fronts low *a outside nasal environments. In trace output this feeds three recurring downstream patterns:

1. direct retention of fronted low vowels, as in *dæg;
2. later breaking to `ea`, as in *bærd > *beard and *fældaną > *fealdaną;
3. later restoration or retraction before back-vowel environments, as in *bækaną > *bakaną and *færaną > *faraną.

The literature strongly supports the order fronting before breaking and before restoration or general retraction. The most model-specific part of the current rule is the explicit unstressed clause; that clause does have handbook support in Hogg, but it remains worth watching when later dossiers are compared.

## Chronological source dossier

### Campbell 1959
- source_key: Campbell1959
- locator: § 131; §§ 139, 157-158
- terminology: early change of Germanic `a > æ`; breaking; retraction; restoration of `a` before back vowels
- quotation: "By a very early change Prim. Gmc. a > æ in OE and OFris. when not followed by a nasal consonant"; "breaking can hardly be regarded otherwise than as a change affecting front vowels"
- paraphrase: Campbell gives the baseline handbook formulation of first fronting as an early OE and Frisian change excluding nasal environments. He then builds the later OE story on top of that fronted stage: breaking operates on front vowels, and restoration of `a` before back vowels is a later reversal in specific paradigmatic environments.
- conditioning: fronting outside nasal contexts; breaking before `rC`, `lC`, and `h`; restoration before following back vowels
- chronology: fronting is very early; breaking presupposes a fronted input; restoration follows the breaking stage
- examples: `dæg`, `hwæt`, `bær`, `stæl`; restored `faran`, `bacan`
- interaction with other changes: Campbell's sections on breaking and restoration are direct evidence that SC043 must be discussed together with OE Breaking and OE A Restoration
- disagreements or cautions: Campbell also suggests the English and Frisian developments may have been independent rather than a single undifferentiated shared event
- notes: Campbell is still the cleanest section-safe source for the core order claim behind the current transducer

### Hogg 1992
- source_key: HoggPhonology1992
- locator: p. 102 (§ 3.3.3.1); p. 119; p. 445
- terminology: Anglo-Frisian Brightening; First Fronting
- quotation: "This vowel normally fronted to /ae/ by the sound change of Anglo-Frisian Brightening (or First Fronting)"; "By First Fronting ... /a/ became /ae/ as in stressed syllables"
- paraphrase: Hogg gives the most straightforward modern label pair for the change and states the main conditioning clearly: fronting is normal, but following nasals block it. He is also useful for the present transducer because he explicitly extends first fronting into the unstressed-vowel system. The later Toon chapter in the same volume preserves the standard handbook order fronting > breaking/retraction > restoration, while warning against excessive confidence about the full prehistoric sequence.
- conditioning: stressed and unstressed low `a` front; following nasals block the change
- chronology: the change belongs among the earliest stressed-syllable developments; unstressed fronting precedes later reduction of unstressed front vowels; the conventional local order is fronting before breaking and restoration
- examples: `dæg` versus German `Tag`; nasal exception in `man`; unstressed-system discussion from the development of forms like `*namani`
- interaction with other changes: later OE changes recreate back `/a/`, which is why the synchronic system can obscure the earlier fronting event
- disagreements or cautions: the Toon chapter treats the larger prehistoric ordering as contestable even if the local relation to breaking and restoration is conventional
- notes: Hogg is the best direct support for retaining an unstressed component in the internal computational rule

### Ringe and Taylor 2014
- source_key: RingeTaylor2014
- locator: § 5.1.2, pp. 157-158; § 6.1.1, pp. 168-169; § 6.3.1, pp. 189-190
- terminology: nasalization, fronting, and related changes; fronting of low vowels; general retraction of `*æ`
- quotation: "Stressed low vowels were nasalized when immediately followed by a nasal"; "Since no specifically OE sound changes can be dated before the fronting, while one of the earliest must have followed it"; "retraction must have occurred subsequently to fronting and subsequently to breaking"
- paraphrase: Ringe and Taylor divide the dossier problem cleanly into three steps. First, they treat nasalization before nasals as the major northern WGmc exception to fronting. Second, they place the fronting early enough that it predates the earliest specifically OE changes and already sits behind dialect diversification. Third, they argue explicitly that general retraction must be later than both fronting and breaking, because breaking only affected front vowels.
- conditioning: nasal branch before immediate nasals; fronted outcomes elsewhere; later retraction before back-vowel environments
- chronology: fronting is earlier than breaking; general retraction is later than both fronting and breaking
- examples: `mona`, `comon`; West Saxon lower outcomes versus Anglian and Kentish higher outcomes; `sléan` and `dagum` for the retraction argument
- interaction with other changes: this is the strongest single source for how SC043 should be related to OE Breaking and OE A Restoration in the eventual volume
- disagreements or cautions: they leave open whether much of the variable spread of fronting happened on the continent or in Britain
- notes: especially useful for chapter architecture, because the source states the relative order more explicitly than Campbell or Hogg

### Fulk 2018
- source_key: Fulk2018
- locator: § 4.12, p. 73; § 4.13, pp. 73-74
- terminology: Anglo-Frisian Brightening; breaking; retraction
- quotation: "Elsewhere, a was fronted to æ ... This fronting is commonly referred to as Anglo-Frisian Brightening"; "Before r plus any consonant ... æ and e are broken to ea and eo"
- paraphrase: Fulk gives the clearest compact definition of Anglo-Frisian Brightening and immediately follows it with the early OE breaking section, which makes the sequencing easy to capture. He also notes an Anglian retraction branch before checked `l`, which matters for later order-sensitivity planning.
- conditioning: nasalization before nasals; fronting elsewhere; breaking before `rC`, `lC`, and `h`; Anglian retraction before checked `l`
- chronology: brightening precedes the early OE breaking stage and the later front-umlaut developments referenced in the same section
- examples: `fæder`, `dæg`, `læt`; `bearn`, `healdan`, `cald`
- interaction with other changes: Fulk provides a compact bridge from SC043 to OE Breaking and to the later dialect-specific retraction patterns
- disagreements or cautions: Old Frisian keeps `a` in several special environments, so not every Anglo-Frisian reflex should be collapsed into a single OE-centered narrative
- notes: the Google Vision OCR witness was sufficient; the PDF did not need to be opened in this pass

## Thematic synthesis

### Names and terminology

The dossier confirms that two names dominate the modern handbook tradition: **Anglo-Frisian Brightening** and **First Fronting**. Campbell does not foreground either label in the same way, instead describing the change directly as early `a > æ` outside nasal environments. For chapter drafting, "Anglo-Frisian Brightening" works well as the main heading, but "First Fronting" should appear early as the standard alternate term.

### Conditioning

All verified sources agree on the core conditioning: low `a` fronts outside nasal environments, while vowels before nasals follow a separate nasalization branch. The most important complications are not at the fronting stage itself but in the later reshaping of outputs:

1. breaking before `rC`, `lC`, and `h`;
2. restoration or general retraction before following back vowels;
3. dialect-specific exceptions or alternative outcomes, especially Anglian checked-`l` retraction and some Old Frisian non-fronting environments.

Hogg also gives support for extending the fronting into the unstressed system, which is relevant to the current FOMA rule.

### Chronology and ordering

The strongest shared chronology is:

1. fronting of low `a`;
2. breaking of the fronted vowel in certain consonantal environments;
3. restoration or general retraction before back-vowel contexts.

Campbell implies this order by building breaking and restoration from an earlier fronted input. Ringe and Taylor make it explicit: retraction must be later than fronting and later than breaking because breaking only affected front vowels. The broader geographic question remains open: Ringe and Taylor treat the spread and raising of the fronted outcomes as compatible with either continental or early-insular diffusion.

### Examples

Examples cited by the literature:

1. Campbell: `dæg`, `hwæt`, `bær`, `stæl`; restored `faran`, `bacan`
2. Hogg: `dæg` versus `Tag`; `man` as the nasal exception
3. Fulk: `fæder`, `dæg`, `læt`; `bearn`, `healdan`, `cald`
4. Ringe and Taylor: `mona`, `comon`, `sléan`, `dagum`

Examples from the transducer trace:

1. `bake`: `*bækaną` after SC043, later restored to `*bakaną`
2. `beard`: `*bærd` after SC043, later broken to `*beard`
3. `father`: `*fædǣr` after SC043, later shortened and merged to `*fæder`
4. `day`: `*dæg` after SC043 with no restoration
5. `fall`: `*fællaną` after SC043, later broken to `*feallaną`

### Disagreements and open questions

0. **The Anglo-Frisian status of this change is unresolved, and this dossier
   does not settle it.** The label "Anglo-Frisian Brightening" is a
   historiographical inheritance, not a finding. Whether the fronting can
   actually be placed on a shared English/Frisian stem — as against having
   happened independently in the two languages — depends on relative
   chronologies that the handbook sources above do not adjudicate, and on
   which the Frisian specialist literature directly contradicts itself.
   Campbell 1939 argues that the relative order of \emph{*ai}-monophthong-
   ization and short-\emph{*a} fronting is *reversed* between the two
   languages, and concludes the fronting was independent
   [@Campbell1939, pp. 90–91]; Kortlandt 2008 places the fronting on the
   shared stem as AF 6 [@Kortlandt2008, p. 270]. Both readings are live;
   compatibility under an author's proposed chain is not proof of inheritance.

   That comparison is maintained in one place and must not be re-derived
   here or in any other memo:

   `anglo_frisian/anglo-frisian-chronology.synthesis.md`

   with per-source evidence in `anglo_frisian/source_cards/`. This dossier
   defers to it. Point 1 below is the earlier, weaker statement of the same
   caution and is retained for continuity.

1. The English-Frisian subgrouping question is not identical to the narrower question of how to narrate the fronting event itself; Campbell is more cautious than the modern label "Anglo-Frisian Brightening" may suggest.
2. Ringe and Taylor leave open whether the spread of the fronted outcomes happened mainly on the continent or in Britain.
3. The transducer's explicit unstressed clause is defensible from Hogg, but the chapter will need to decide whether to foreground that or keep the main prose centered on the stressed-vowel rule and mention unstressed fronting briefly.
4. The eventual volume must decide whether OE Breaking and OE A Restoration are described as separate entries with cross-references, or whether SC043 gets an unusually strong forward link because its outputs are so often masked by later stages.

## Source desiderata

1. Luick1914: search completed in the local text witness, but no clean locator-safe SC043 passage was harvested in this pass.
2. Bulbring1902: local OCR search surfaced relevant chapter headings, but not yet a clean extract suitable for matrix quotation.
3. Kaluza1906: searched in the local text witness without a clean dossier-ready extract in this pass.
4. SieversBrunner1965: Google Vision OCR is available and should be revisited when a second-round historical grammar sweep is done.
5. Stiles1985 and Stiles1986a/b: likely useful for Anglo-Frisian and Ingvaeonic subgroup questions if the eventual chapter needs a fuller historiography of the label rather than only the sound change.
6. **Stiles 1995, "Remarks on the 'Anglo-Frisian' Thesis", is the highest-priority
   missing item for this change.** Bremmer, Laker, Kortlandt and Repansek all
   engage with its chronological argument directly, so CAPR currently knows it
   only at second hand. See
   `anglo_frisian/missing-direct-sources.md` for the full acquisition list and
   priority order; nothing reported *about* Stiles by another author may be
   treated as direct evidence from Stiles until a copy is held.
7. Nine Anglo-Frisian specialist sources were ingested in the 2026 source pass
   and are now held locally: Campbell 1939, Laker 2007, Bremmer 2008,
   Kortlandt 2008, Repansek 2012, Versloot 2017, 2021 and 2025, Waxenberger 2019.
   Their bearing on this change is recorded in the synthesis dossier.

## Dossier status

pilot_complete
