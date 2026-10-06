# SC017 NWGmc U Lowering — literature dossier

## Rule metadata

- change_id: SC017
- display_name: NWGmc U Lowering
- FOMA rule: NWGmcULowering
- current_order: 17
- chronology_card: `Germanic/docs/sound_changes/order_tests/chronology_cards/SC017-nwgmc-u-lowering.md`
- example_lexemes: yoke, nose, shovel, sorrow; additional classical examples include daughter, god, gold, door, bottom, past participles such as `boren` and `holpen`
- aliases searched: NWGmc U Lowering; u lowering; lowering of u; u > o; Germanic u to o; Old English o from Germanic u; lowering before final o; lowering before final a; nose; nosu; nusu; *núsō; shovel; sċofl; sċufl; *skúflō; sorrow; sorg; surg; *súrgō; North-West Germanic; Northwest Germanic; Proto-Northwest-Germanic; lowering in Northwest Germanic

## FOMA definition

```foma
define NWGmcULowering [
    {*u} -> {*o} || .#. EnglishStarConsonant* _ [EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó} || .#. EnglishStarConsonant* _ [EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

## Working description

SC017 is a much more standard literature object than SC016. The broad phenomenon is the lowering of stressed Germanic `u` to `o` before a following non-high vowel, with regular examples like `dohtor`, `gold`, `geoc`, `botm`, `dor`, and Class II-IV past participles. The main scholarly complications are:

1. exceptions and retained `u` forms;
2. blocking before nasal environments;
3. the role of `j` or other conditioning consonants;
4. how far to describe the change as Northwest Germanic versus early Old English.

Unlike SC016, this is not merely a CAPR-internal label pasted onto a thin phenomenon. The exact label **NWGmc U Lowering** is modern modeling language, but it maps onto a long-recognized historical development.

## Search log

| Source file searched | Search terms used | Productive? | Evidence found | Notes |
| --- | --- | --- | --- | --- |
| `docs/references/kaluza_historische_grammatik_englisch.txt` | `u vor a`, `u vor o`, `u vor e`, `geoc`, `gold`, `holpen`, `Joch` | yes | compact early statement that Indo-European/Germanic `u` before `a, o, e` yields Germanic/Old English `o` when not blocked by nasal+consonant | strong early rule statement |
| `docs/references/luick_historische_grammatik.txt` | `scufel`, `scofel`, `u und o`, `spura`, `spora`, `Mord`, `Schaufel` | yes | cautionary discussion of `u/o` variation and doublets, including `scufel` beside `scofel` | useful for exceptions and lexical fluctuation |
| `docs/references/campbell_old_english_grammar.txt` | `§ 115`, `u > o`, `gold`, `geoc`, `holpen`, `dohtor` | yes | clearest handbook statement of the change and its exceptions/blocking before nasals | best single English-language witness |
| `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` | `before a mid or low vowel`, `lowered to o`, `geoc`, `gold`, `nasal consonant`, `when j preceded` | yes | modern comparative statement with chronology and explicit blocking by nasals and by `j` | best modern synthesis for CAPR comparison |
| `docs/references/hogg_vol1.txt` | `u > o`, `gold`, `geoc`, `non-high vowel`, `following syllable` | no | example mentions only; no short dossier-ready discussion recovered in this pass | checked, but not used |
| `docs/references/ringe_taylor_linguistic_history_vol2.txt` | `u became o`, `gold`, `geoc`, `botm`, `door`, `following syllable` | yes (2026 re-search) | p. 129 prints the PWGmc paradigm of 'yoke' as jok/jokas/joku, with the lowering applied; p. 5 interprets geoc as /jok/ | recovered in the 2026 adjudication pass |
| `docs/references/brunner_1965_altenglische_grammatik.txt` | `u vor a, o, e`, `gold`, `geoc`, `holpen` | no | likely relevant sections exist, but OCR was too noisy for safe quotation | checked, but not used as a primary witness |
| `docs/references/bosworth_toller_anglo_saxon_dictionary.txt` | `nosu`, `sorg`, `scofl` | no | lexical confirmation only | dictionary evidence, not historical discussion |
| `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | `nosu`, `sorg`, `scofl` | no | lexical confirmation only | dictionary evidence, not historical discussion |

## Chronological source dossier

### Kaluza 1900

- source_key: Kaluza1900
- full source title: *Historische Grammatik der englischen Sprache. Erster Teil: Geschichte der englischen Sprache, Grundzüge der Phonetik, Laut- und Formenlehre des Altenglischen*
- publication year: 1900
- locator: § 66 x), lines 4657-4662 in the local text witness
- terminology used by the source: `Idg. u vor a, o, e ... = urg. o`
- exact quotation: "Idg. u vor a, o, e, wenn nicht Nasal + Kons. dazwischenstand = urg. o ... ae. geoc Joch ... ae. gold Gold ... ae. boden geboten, ae. holpen geholfen"
- paraphrase of the source's claim: Kaluza states the rule very compactly: `u` is lowered before following `a, o, e` unless blocked by nasal plus consonant. He places `geoc`, `gold`, and past participles in the same development.
- conditioning stated by the source: `u` before `a, o, e`; blocked by nasal + consonant
- examples used by the source: `geoc`, `gold`, `boden`, `holpen`, `dohtor`, `oaca`
- chronology stated or implied by the source: pre-Old-English/early Old English development from the Germanic stage
- relation to other changes: directly paired with a following section on retention of `u` in nasal environments
- cautions, uncertainties, or disagreements: no explicit chronology against palatal glide or final `ō`-raising is given
- assessment of usefulness for the book: excellent as an early concise rule statement

### Luick 1921

- source_key: Luick1921
- full source title: *Historische Grammatik der englischen Sprache*
- publication year: 1921
- locator: lines 6108-6123 in the local text witness
- terminology used by the source: fluctuation between `u` and `o`; `Doppelformen`
- exact quotation: "Die Zahl der Doppelformen wie spura/spora war ... viel größer ... So ist zu erschließen ... *scufel ... neben scofel Schaufel'. ... Dies Schwanken zwischen u und o erklärt sich daraus ..."
- paraphrase of the source's claim: Luick accepts the lowering pattern, but stresses that actual Old English and post-Old-English transmission often preserve doublets and analogical fluctuation. `Scufel / scofel` is a particularly relevant witness for the `shovel` lexeme family.
- conditioning stated by the source: not restated as a single formula in this passage; emphasis is on resulting alternation and analogical redistribution
- examples used by the source: `spura/spora`, `*smuca/*smoca`, `*scufel/scofel`, `*murpor/morpor`
- chronology stated or implied by the source: later textual and analogical variation after the basic lowering pattern
- relation to other changes: tied to paradigmatic and inflectional alternation rather than to one isolated sound law
- cautions, uncertainties, or disagreements: very useful caution against treating every `u/o` distribution as a pure direct phonological outcome
- assessment of usefulness for the book: useful chiefly for the exception/variation section rather than for the headline statement

### Campbell 1959

- source_key: Campbell1959
- full source title: *Old English Grammar*
- publication year: 1959
- locator: § 115, lines 3770-3783; § 116, lines 3790-3794; § 117, lines 3810-3817 in the local text witness
- terminology used by the source: "`u > o before mid and low vowels`"; redistribution blocked before nasals
- exact quotation: "`u > o before mid and low vowels. In OE forms this change occurs with considerable regularity ... dohtor daughter, god god, gold gold, geoc yoke ... coren, boren, holpen.`"
- paraphrase of the source's claim: Campbell presents the standard handbook rule: `u` lowers to `o` before following mid and low vowels, with many regular Old English outcomes. He then adds two important restrictions: the redistribution does not take place before nasal+consonant clusters, and Old English also preserves `u` before single `m` in words like `cuman`, `fruma`, and `guma`.
- conditioning stated by the source: before mid and low vowels; blocked before nasal+consonant; also special retention before single `m`
- examples used by the source: `dohtor`, `god`, `gold`, `geoc`, `coren`, `boren`, `holpen`; blocked examples `hund`, `wind`, `swimmen`, `bindan`, `springan`; retention before single `m`: `cuman`, `fruma`, `guma`, `sumor`
- chronology stated or implied by the source: Germanic-to-Old-English vowel redistribution preceding later specifically Old English developments
- relation to other changes: explicitly tied to the wider redistribution of `e / i / o / u`; the `geoc` reference cross-links to Campbell's later discussion of palatal-glide spellings
- cautions, uncertainties, or disagreements: Campbell emphasizes many exceptions and preserved `u` forms, especially where other West Germanic languages have `o`
- assessment of usefulness for the book: the best primary handbook source for the core rule and its principal exceptions

### Fulk 2018

- source_key: Fulk2018
- full source title: *A Comparative Grammar of the Early Germanic Languages*
- publication year: 2018
- locator: § 4.3, lines 3719-3740 in the local text witness
- terminology used by the source: lowering of `u` to `o` before a mid or low vowel in the next syllable
- exact quotation: "when u stood before a mid or low vowel in the next syllable ... it was lowered to o ... This lowering is prevented before a tautosyllabic nasal consonant ... Lowering is prevented also when j preceded the non-high vowel conditioning the change"
- paraphrase of the source's claim: Fulk gives the cleanest modern comparative account. The change is early, predates the fifth-century raising of final `-ō` to `-u`, is visible in early Runic material, and is blocked both by nasal environments and by `j` before the conditioning non-high vowel.
- conditioning stated by the source: `u` before a mid or low vowel in the next syllable; blocked by tautosyllabic nasal, apparently also by heterosyllabic nasal, and by `j` before the conditioning vowel
- examples used by the source: `scolu`, `geoc`, `gold`, `dor`, `botm`, `stolen`; blocked examples `wunden`, `sund`, `fruma`, `guma`, `cuman`; `j`-blocked `cnyssan`, `trymman`
- chronology stated or implied by the source: relatively early Northwest Germanic development, already visible before final `-ō > -u`
- relation to other changes: explicitly connected to later unstressed-vowel developments and to parallel i-lowering
- cautions, uncertainties, or disagreements: the exact reach of heterosyllabic nasal blocking is phrased more cautiously than the main rule statement
- assessment of usefulness for the book: best modern synthesis and best direct support for most of the current CAPR conditioning

## Comparative synthesis

1. **Do the sources agree on the existence of the change?**  
   Yes. All productive sources recognize a genuine lowering of Germanic `u` to `o` in an appropriate following-vowel environment.

2. **Do they use the same terminology?**  
   Not exactly. Kaluza and Campbell describe the rule as `u` before `a, o, e` or before mid/low vowels. Fulk speaks of `u` before a mid or low vowel in the next syllable. Luick discusses the resulting `u/o` fluctuation more than the headline law. The CAPR name **NWGmc U Lowering** is a modern repository label, but it maps well onto the literature.

3. **Do they define the same conditioning environment?**  
   Broadly yes. The shared core is stressed `u` lowering before a following non-high vowel. Campbell and Kaluza emphasize the general environment plus nasal blocking. Fulk adds the most explicit modern statement of blocking by `j` and of the change's early Northwest Germanic date.

4. **Do they use the same examples?**  
   There is strong overlap. `geoc`, `gold`, `dohtor`, and participles like `holpen / boren / coren` are recurrent. The exact chronology-card set `nosu / sċofl / sorg` is not the standard handbook example triad, but Luick's `scufel / scofel` variation is directly relevant to one of those CAPR lexemes.

5. **Do they assign the same historical stage?**  
   Yes in broad terms. The development belongs before classical Old English surface forms stabilize; Fulk makes the earliest-stage claim most explicitly by tying it to the period before final `-ō > -u`.

6. **Do they give an explicit relative chronology?**  
   Only partially. Fulk gives the clearest relative chronology by making the rule earlier than final `-ō > -u`. The productive sources do **not** explicitly discuss the CAPR labels SC016 or SC019, but they do support the wider chronological neighborhood.

7. **Do they conflict with the current CAPR implementation?**  
   Mostly no. The CAPR rule's stressed-syllable restriction, nasal blocking, and `j` blocking are compatible with Fulk and Campbell. The main difference is that CAPR turns the literature into a single sharply delimited stage with exact input restrictions and immediate local neighbors.

8. **Do they support, complicate, or fail to discuss the SC016/SC017 computational boundary?**  
   (Updated by the 2026 adjudication, sc016-017-adjudication.md.) They resolve it in the opposite direction from the original CAPR architecture: Fulk (§4.3 p. 56) lists `geoc` as a plain u-lowering output and Campbell (§115) gives it among the regular `u > o` words, so the lowering produced the *o* that the West Saxon glide spelling (SC016) later rendered as ⟨eo⟩. SC017 therefore historically precedes and feeds SC016; the old claim that the glide stage must precede the lowering was an artifact of the misformulated early SC016.

9. **Is the change a standard historical sound change, a model-internal formalization, or a mixture?**  
   Mostly a standard historical sound change. The CAPR rule sharpens the conditioning and chronology, but the underlying phenomenon is well established in the literature.

10. **What can safely be said in book prose?**  
   It is safe to say that early Northwest Germanic / pre-Old-English stressed `u` was often lowered to `o` before a following non-high vowel, with major lexical examples including `geoc`, `gold`, and `dohtor`, and with important blocking near nasals and some `j` environments. The relation to the West Saxon glide spelling is now source-backed: the lowering fed the spelling (Fulk §4.3 p. 56; Brunner §92.1; Bülbring §299).

## Relation to CAPR implementation

(Updated by the 2026 adjudication, sc016-017-adjudication.md.) The CAPR implementation aligns well with the literature:

1. **FOMA definition:** `PNWGmcULowering` lowers initial-syllable `u/ú` before a following non-high vowel while excluding nasal codas and any `j` in the intervening post-target consonants. The adjudication confirmed this formulation unchanged: a word-initial *j does not block the change (Fulk §4.3 p. 56, *knusjaną* type), so `*juką > *joką` is regular.
2. **Current order:** SC017 executes at position 13 in the Northwest Germanic corridor; SC016 now executes in the Old English written-surface block (position 91), which SC017 feeds.
3. **Chronology:** the historical partial order records SC005 < SC017 and the feeding edge SC017 < SC016 (yoke), plus the later boundary against SC019 on `nose; shovel; sorrow`.
4. **Representative failures:** moving SC017 later than SC019 yields `nusu`, `sċufl`, and `surg` instead of `nosu`, `sċofl`, and `sorg`. The former claim that SC017 had to follow SC016 (else `ġoc`) is retracted: with the repaired SC016 the derivation is `*juką → *joką → ġoc (orthography stage) → ġeoc (glide spelling)`.
5. **Corpus witnesses:** `geoc`, `nosu`, `sċofl`, `sorg` for the lowering; `geoguþ` as the negative control whose root `u` is protected by the following high vowel.

## Dossier status

ready_for_book_dossier: yes
