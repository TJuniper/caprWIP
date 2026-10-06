# SC016 OE Ws Palatal Glide — literature dossier

## Rule metadata

- change_id: SC016
- display_name: OE Ws Palatal Glide
- FOMA rule: OEWsPalatalGlide
- current_order: 91 (Old English written-surface block, after OldEnglishOrthography; repositioned by sc016-017-adjudication.md)
- chronology_card: `Germanic/docs/sound_changes/order_tests/chronology_cards/SC016-oe-ws-palatal-glide.md`
- example_lexemes: yoke, youth
- aliases searched: OE Ws Palatal Glide; palatal glide; West Saxon palatal glide; glide-conditioned fronting; glide fronting; fronting before j; fronting before i/j; palatal diphthongization; ġeoc; geoc; yoke; *júką; juk; i-umlaut; palatal influence; breaking and palatal glide; West Saxon fronting

## 2026 adjudication update

This dossier was first compiled while SC016 was implemented as an early
glide-insertion rule (`*ju > *jeu`) composed at cascade position 13, before
SC017 `PNWGmcULowering`. The joint adjudication
`Germanic/docs/sound_changes/audits/sc016-017-adjudication.md` overturned
that architecture on the evidence assembled below and in the 017 dossier:

1. The change is Old English/West Saxon and, on the modern assessment
   (Ringe & Taylor p. 5; Hogg p. 112), an orthographic convention rather
   than a phonological insertion. It now executes in the written-surface
   block, after `OldEnglishOrthography` (executable position 91).
2. Its domain is back vowels generally after word-initial ġ — both the
   *o*-cases (*ġeoc* < WGmc *jok, Bülbring §299; Brunner §92.1b) and the
   *u*-cases (*ġeoguþ*, Brunner §92.1a; Bülbring §298).
3. The old SC016 < SC017 "technical dependency" is replaced by the
   historically supported feeding order SC017 < SC016: NWGmc u-lowering
   produced the *o* of *ġeoc* (Fulk §4.3 p. 56; Campbell §115 p. 43),
   and the WS spelling convention later rendered it ⟨eo⟩.

The sections below are updated where the repair changed the facts; the
original search log is retained with corrections noted.

## FOMA definition

```foma
define OEWsPalatalGlide [
    {*ó} -> {*éo} || .#. ġ _ ,
    {*ú} -> {*éo} || .#. ġ _ ,
    {*o} -> {*eo} || .#. ġ _ ,
    {*u} -> {*eo} || .#. ġ _
];
```

(Repaired formulation; the superseded early insertion rule
`{*j}{*u} -> {*j}{*e}{*u} …` with ʤ/ʧ/ʃ clauses is preserved in the
adjudication memo. The ʤ/ʧ/ʃ clauses were unsatisfiable at the old early
position, since palatalization had not yet occurred.)

## Working description

The CAPR rule rewrites a back vowel after word-initial ġ as the ⟨eo⟩
digraph spelling, yielding West Saxon spellings of the `geoc / geoguþ`
type. It executes in the written-surface block because the modern
assessment (Ringe & Taylor, Hogg) treats these spellings as orthography,
not phonology. The literature discusses the phenomenon, but usually not
under the exact rule name **OE Ws Palatal Glide**. Older grammars more
often describe:

1. rising diphthongs or glide spellings before back vowels in West Saxon;
2. `geoc / geong / geoguþ` as the core example set;
3. dialectal and orthographic variation among `iu / io / eo` or undiphthongized forms.

That matters for book use. The historical phenomenon is real and well attested, but the CAPR rule is a narrow formalization of it rather than a standard named sound law in the way that Anglo-Frisian Brightening or i-umlaut are.

## Search log

| Source file searched | Search terms used | Productive? | Evidence found | Notes |
| --- | --- | --- | --- | --- |
| `docs/references/kaluza_historische_grammatik_englisch.txt` | `geoc`, `gioc`, `geong`, `iung`, `Joch`, `yoke`, `palatal` | yes | early grammar statement of OE reflexes of initial Germanic `j`; `geoc / geong / geogud` example cluster | good dated witness; terminology is descriptive rather than rule-name based |
| `docs/references/bulbring_altenglisches_elementarbuch.txt` | `iuc`, `jeoc`, `geoc`, `geong`, `gio`, `geo`, `Joch` | yes | detailed West Saxon `gio/geo` discussion with `Joch`, `jung`, `Jugend` examples | especially useful for spelling variation |
| `docs/references/luick_historische_grammatik.txt` | `geoc`, `jung`, `young`, `Joch`, `zio`, `zeo` | yes | discussion of West Saxon doublets and later generalization of `geo-` spellings | useful caution about variation and chronology of spellings |
| `docs/references/campbell_old_english_grammar.txt` | `palatal glide`, `rising diphthongs`, `geoc`, `geong`, `§ 172`, `young` | yes | clearest English-language description of rising diphthongs formed by palatal glides before back vowels | best source for book-safe wording |
| `docs/references/ringe_taylor_linguistic_history_vol2.txt` | `geoc`, `/jok/`, `word-initial /j/`, `back vowel`, `West Saxon diphthongization` | yes | modern witness that `geoc` represents /jok/ after initial /j/ before back vowel | useful, but more phonological/orthographic than chronological |
| `docs/references/hogg_vol1.txt` | `geoc`, `palatal diphthongization`, `rising diphthongs`, `geong` | yes (2026 re-search) | p. 112: back-vowel cases "never anything more than an orthographic variation"; Campbell §176's contrary arguments "insubstantial" | decisive modern witness recovered in the 2026 adjudication pass |
| `docs/references/brunner_1965_altenglische_grammatik.txt` | `geoc`, `geong`, `§ 92`, `Joch` | yes (2026 re-search) | §92.1 (pp. 64–65) splits the u-subcase (ȝeong, ȝeoguþ) from the o-subcase ("Bei o und ō … ȝioc ȝeoc Joch") — yoke belongs to the o-class | recovered cleanly in the 2026 adjudication pass |
| `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` | `geoc`, `u-lowering`, `joh`, `juk` | yes (2026 search) | §4.3 p. 56 lists geoc as a plain u-lowering example (OIcel. ok, OE geoc, OHG joh beside juh, OS juk); n. 2 gives the *joka ~ *jukum paradigm split | added during the 2026 adjudication |
| `docs/references/bosworth_toller_anglo_saxon_dictionary.txt` | `geoc`, `geong`, `geoguþ` | no | lexical confirmation only | dictionary evidence, not historiographic discussion |
| `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | `geoc`, `geong`, `geoguþ` | no | lexical confirmation only | dictionary evidence, not historiographic discussion |

## Chronological source dossier

### Kaluza 1900

- source_key: Kaluza1900
- full source title: *Historische Grammatik der englischen Sprache. Erster Teil: Geschichte der englischen Sprache, Grundzüge der Phonetik, Laut- und Formenlehre des Altenglischen*
- publication year: 1900
- locator: § 90, lines 7280-7283 in the local text witness
- terminology used by the source: reflexes of initial Germanic `j` in Old English
- exact quotation: "Beispiele: a) Urg. j im Anlaut = ae. g, ge, gi, i [g, j]: ... geoc, gioc Joch (lat. jugum), geómor Jammer, geong, giung, iung jung, geogud Jugend"
- paraphrase of the source's claim: Kaluza treats `geoc / geong / geogud` as regular Old English reflexes of initial Germanic `j` in this environment. The presentation is descriptive and orthographic-phonological rather than a named sound-change chapter.
- conditioning stated by the source: initial Germanic `j` in Old English; the quoted examples show the West Saxon `ge-/gio-/gi-` spellings before back-vocalic material
- examples used by the source: `geoc`, `gioc`, `geómor`, `geong`, `giung`, `iung`, `geogud`
- chronology stated or implied by the source: implied Old English development; no explicit relative chronology against another named sound change
- relation to other changes: the passage is about reflexes of initial `j`, not about u-lowering or i-umlaut directly
- cautions, uncertainties, or disagreements: the source does not isolate a separate sound law called "palatal glide"; it groups these forms under the wider treatment of initial `j`
- assessment of usefulness for the book: useful as an early witness that the `geoc / geong / geogud` set is real and traditional, but not enough by itself to justify the exact CAPR rule name

### Bülbring 1902

- source_key: Bulbring1902
- full source title: *Altenglisches Elementarbuch. I. Teil: Lautlehre*
- publication year: 1902
- locator: §§ 298-299, lines 5970-5985 in the local text witness
- terminology used by the source: West Saxon `gio / geo` development; `io`/`eo` spellings after palatal environments
- exact quotation: "iuc, jeoc 'Joch' (< wg. *juk, niederl. juk) ... jo ist im Ws. zu gio geo geworden ... gioc geoc 'Joch' (aus wg. *jok, neben *juk § 298), giōmrian geōmrian"
- paraphrase of the source's claim: Bülbring explicitly treats West Saxon `gio / geo` as the relevant development and uses `Joch`, `jung`, and `Jugend` as the standard examples. He also preserves the coexistence of forms from both `*juk` and `*jok` type reconstructions in the explanatory tradition.
- conditioning stated by the source: West Saxon development after palatal onset; `jo` and related sequences yield `gio / geo`
- examples used by the source: `iuc / jeoc`, `gioc / geoc`, `giōmrian / geōmrian`, `iúng / gióng / geing`
- chronology stated or implied by the source: the source implies a West Saxon development and later orthographic regularization, but gives no explicit chronology against u-lowering
- relation to other changes: relation is primarily to dialectal spelling development rather than to a separate chain of vowel changes
- cautions, uncertainties, or disagreements: the reconstruction alternates between `*juk` and `*jok`, showing that the older tradition did not always isolate the exact stage CAPR now targets
- assessment of usefulness for the book: very useful for demonstrating that the `geoc / geong / geoguþ` cluster was long recognized, but also that the older literature often handled it as spelling/diphthongization rather than as a sharply bounded sound change

### Luick 1921

- source_key: Luick1921
- full source title: *Historische Grammatik der englischen Sprache*
- publication year: 1921
- locator: lines 10447-10458 in the local text witness
- terminology used by the source: West Saxon doublets; later generalization of `zeo-/geo-` spellings
- exact quotation: "Alfred zeigt jung ... daneben aber ... zēomor Jammer', geoc 'Joch'. Später wurden diese letzteren Formen ... in der Schreibung verallgemeinert"
- paraphrase of the source's claim: Luick emphasizes that West Saxon preserved competing spellings and that later `geo-` forms became generalized in writing. The phenomenon is thus treated as a real development, but one entangled with orthographic regularization and dialectal variation.
- conditioning stated by the source: West Saxon environment with the `jung / geoc / geōmor` type forms
- examples used by the source: `jung`, `zēomor`, `geoc`, `zeonz`, `zeozoo`
- chronology stated or implied by the source: later written generalization follows earlier variation; explicit ordering against u-lowering is absent
- relation to other changes: relation is to dialect and spelling history, not to an independently named chronology slot
- cautions, uncertainties, or disagreements: Luick's emphasis on doublets is a warning against treating the phenomenon as a perfectly clean single-step law
- assessment of usefulness for the book: useful mainly as a cautionary source; it helps prevent overclaiming about uniformity

### Campbell 1959

- source_key: Campbell1959
- full source title: *Old English Grammar*
- publication year: 1959
- locator: § 44, lines 2192-2199 in the local text witness
- terminology used by the source: rising diphthongs formed when palatal glides developed before back vowels
- exact quotation: "the graphs ea, eo, io are used not for the usual OE falling diphthongs, but for rising diphthongs, which were formed when palatal glides developed before back vowels, as in ... geoc yoke ... A palatal glide + u is written eo, io or iu in W-S and Kt."
- paraphrase of the source's claim: Campbell gives the clearest compact description of the phenomenon. The central claim is that West Saxon spellings like `geoc` and `geong` reflect rising diphthongs formed by palatal glides before back vowels.
- conditioning stated by the source: palatal glide before back vowel; especially palatal glide plus `u` in West Saxon and Kentish
- examples used by the source: `geoc`, `geong`, other `ea / eo / io` rising-diphthong examples
- chronology stated or implied by the source: Old English dialect development; no explicit order against u-lowering, but the description presupposes the palatal-glide outcome as a phonological fact
- relation to other changes: related to the treatment of initial palatal consonants and later dialect spelling conventions
- cautions, uncertainties, or disagreements: Campbell still describes a phonological/spelling phenomenon, not a standard separate sound law with a fixed historical label
- assessment of usefulness for the book: the best single source for book prose on the historical phenomenon behind SC016

### Ringe and Taylor 2014

- source_key: RingeTaylor2014
- full source title: *The Development of Old English*
- publication year: 2014
- locator: p. 5 in the local text witness, lines 1169-1173
- terminology used by the source: orthographic practice after word-initial `/j/` followed by a back vowel
- exact quotation: "After word-initial /j/ followed by a back vowel that practice was universal. Thus ... geoc 'yoke' is /jok/; exceptionally, geong ~ iung 'young' is /jung/."
- paraphrase of the source's claim: Ringe and Taylor explicitly treat `geoc` as an orthographic representation of /jok/ and note `geong ~ iung` as a marked variation point. This is a modern confirmation that the `geoc` type is real, but it is not presented as a standalone named sound change.
- conditioning stated by the source: word-initial `/j/` before back vowel
- examples used by the source: `geoc`, `geong ~ iung`, `geara`, `geomor`
- chronology stated or implied by the source: none explicit for the change itself; the emphasis is phonological interpretation of spellings
- relation to other changes: indirectly related to West Saxon diphthongization and to the treatment of initial palatals
- cautions, uncertainties, or disagreements: modern source still stops short of treating this as an independently named chronology anchor
- assessment of usefulness for the book: useful as a modern control on what the spellings represent, but not enough to turn SC016 into a standard literature-defined sound law

### Brunner 1965

- source_key: SieversBrunner1965
- full source title: *Altenglische Grammatik nach der angelsächsischen Grammatik von Eduard Sievers*
- publication year: 1965 (3rd ed.)
- locator: § 92.1, pp. 64–65
- terminology used by the source: development of palatal glides / diphthongal spellings after palatal onset, subdivided by the following vowel
- exact quotation: "Bei o und ō ... ȝioc ȝeoc 'Joch'" (o-subcase), beside the u-subcase with "ȝeong, ȝeoguþ"
- paraphrase of the source's claim: Brunner distinguishes the u-cases (*ġeong*, *ġeoguþ*) from the o-cases (*ġioc*, *ġeoc*): yoke belongs to the o-class, i.e. its pre-form at the time of the spelling development already had the lowered vowel.
- conditioning stated by the source: palatal onset before a back vowel, with the subclasses defined by the quality of that vowel
- examples used by the source: `ȝeong`, `ȝeoguþ` (u-class); `ȝioc`, `ȝeoc` (o-class)
- chronology stated or implied by the source: the subclassification presupposes that u-lowering had already differentiated *jok- from *jug-/juk- before the spelling development — i.e. lowering precedes the glide spelling
- relation to other changes: directly supports the feeding order SC017 < SC016
- cautions, uncertainties, or disagreements: Brunner stands in the older rising-diphthong tradition on the phonological interpretation
- assessment of usefulness for the book: decisive for the input classification of yoke; the o-subcase is the key structural fact

### Fulk 2018

- source_key: Fulk2018
- full source title: *A Comparative Grammar of the Early Germanic Languages*
- publication year: 2018
- locator: § 4.3, p. 56 (with n. 2)
- terminology used by the source: lowering of *u before non-high vowels (a-mutation)
- exact quotation: "OIcel. ok, OE geoc, OHG joh beside juh and OS juk"
- paraphrase of the source's claim: Fulk lists OE *geoc* as a regular example of Northwest Germanic u-lowering, with the paradigm split *joka ~ *jukum explaining the doublets in the daughters. A word-initial *j does not block the change; the blocking *j of the *knusjaną type stands between the target vowel and the conditioning vowel.
- conditioning stated by the source: *u > *o before a non-high vowel in the following syllable, blocked by an intervening *j or nasal
- examples used by the source: `ok`, `geoc`, `joh`, `juh`, `juk`
- chronology stated or implied by the source: the *o* of *geoc* exists from the Northwest Germanic lowering onward; the WS spelling renders that *o*
- relation to other changes: fixes the SC017 < SC016 feeding relation from the SC017 side
- cautions, uncertainties, or disagreements: none for this word
- assessment of usefulness for the book: the cleanest single statement that yoke's *o* is a u-lowering output

### Hogg 1992

- source_key: HoggPhonology1992
- full source title: local text witness `docs/references/hogg_vol1.txt` (Hogg's survey of Old English phonology; the passage carries the running head "Phonology and morphology")
- publication year: 1992
- locator: p. 113
- terminology used by the source: palatal diphthongisation; orthographic variation
- exact quotation: "there is no need to accept that a parallel change affecting back vowels, represented by examples such as sc(e)op 'poet' and sc(e)acan 'shake', was ever anything more than an orthographic variation. The change was inconsistently carried out, and the arguments of, for example, Campbell (1959: §176) to demonstrate that the change had phonetic consequences are insubstantial."
- paraphrase of the source's claim: Hogg accepts palatal diphthongisation of front vowels but rejects any phonological change before back vowels: the back-vowel spellings are purely orthographic.
- conditioning stated by the source: palatal onset before back vowel (as an orthographic practice)
- examples used by the source: `sc(e)op`, `sc(e)acan`, `secean` beside `secan`
- chronology stated or implied by the source: an orthographic convention of the written OE period, necessarily after the phonological history
- relation to other changes: places SC016 at the end of the derivation, in the written-surface stage
- cautions, uncertainties, or disagreements: directly contradicts Campbell §176's phonetic reading; CAPR follows Hogg and Ringe & Taylor
- assessment of usefulness for the book: decisive, with Ringe & Taylor p. 5, for the orthographic interpretation now implemented

## Comparative synthesis

1. **Do the sources agree on the existence of the change?**  
   Yes, in the limited sense that they agree on a real West Saxon phenomenon behind `geoc / geong / geogud` type forms. What they do **not** agree on is framing it as a standalone named sound change.

2. **Do they use the same terminology?**  
   No. Kaluza, Bülbring, and Luick describe the reflexes of initial `j` or the `gio/geo` spellings; Campbell speaks of rising diphthongs formed by palatal glides before back vowels; Ringe and Taylor frame the issue as orthographic/phonological interpretation. The exact CAPR label **OE Ws Palatal Glide** is model terminology, not a standard literature label.

3. **Do they define the same conditioning environment?**  
   Broadly yes: initial palatal onset before back-vocalic material, especially `u`. But the sources vary in how narrow they are. Campbell is closest to the CAPR environment; older grammars often speak more broadly about spelling classes and West Saxon forms.

4. **Do they use the same examples?**  
   Yes, strongly. The recurring core examples are `geoc` 'yoke', `geong` 'young', and `geogud / geoguþ` 'youth', with `geōmor` often nearby.

5. **Do they assign the same historical stage?**  
   They all place it in Old English, especially West Saxon. None of the productive sources turns it into an earlier Northwest Germanic change.

6. **Do they give an explicit relative chronology?**  
   Yes, once the o-subcase is taken seriously. Fulk (§4.3 p. 56) and Campbell (§115 p. 43) both list `geoc` as a regular output of Northwest Germanic u-lowering, and Brunner (§92.1) and Bülbring (§299) classify `geoc` under the *o*-forms (from WGmc `*jok`). The *o* that the WS scribes wrote as ⟨eo⟩ is therefore the product of SC017: u-lowering feeds the glide spelling, so SC017 < SC016.

7. **Do they conflict with the current CAPR implementation?**  
   No. Since the 2026 repair the implementation matches the sources: the rule is an OE written-surface convention over back vowels after word-initial ġ, executing after all phonology, fed by SC017.

8. **Do they support, complicate, or fail to discuss the SC016/SC017 computational boundary?**  
   They resolve it. The former inverted executable order (SC016 before SC017) existed only because the old formulation targeted `*u` and had to fire before lowering removed its input; with the source-backed domain (back vowels, including the lowered *o*) the rule sits at its historical position and the boundary is the feeding order SC017 < SC016.

9. **Is the change a standard historical sound change, a model-internal formalization, or a mixture?**  
   A mixture. The historical phenomenon is standard enough, but the exact CAPR rule name and discrete stage are model-internal formalization of material the literature usually treats under orthography, diphthongization, or palatal-glide description.

10. **What can safely be said in book prose?**  
   It is safe to say that West Saxon developed `geoc / geong / geoguþ` type outcomes through palatal-glide/rising-diphthong behavior before back vowels. It is **not** yet safe to present SC016 as a universally recognized named sound law with an independently literature-established chronology against SC017.

## Relation to CAPR implementation

Since the 2026 repair (sc016-017-adjudication.md) the implementation follows
the sources directly:

1. **FOMA definition:** `OEWsPalatalGlide` rewrites `o/ó/u/ú` after
   word-initial `ġ` as the ⟨eo⟩ digraph, in the written-surface block after
   `OldEnglishOrthography` (executable position 91). It absorbs the former
   `OEGlideUToEO` (SC093), which never fired.
2. **Chronology:** the historical partial order records SC017 < SC016 as a
   feeding edge (Fulk §4.3 p. 56; Campbell §115; Brunner §92.1;
   R&T pp. 5, 129), replacing the retracted SC016 < SC017
   "technical dependency."
3. **Witnesses:** *ġeoc* exercises the o-subcase (lowered vowel), *ġeoguþ*
   the u-subcase (lowering blocked by the following high vowel); between
   them the corpus fixes both faces of the rule.
4. **Representative failure under the old order:** none remains — the old
   claim that delaying SC016 past SC017 breaks *ġeoc* was an artifact of
   the misformulated `*ju`-only rule, which lacked an *o* clause.

## Dossier status

ready_for_book_dossier: yes (2026 adjudication; see sc016-017-adjudication.md)
