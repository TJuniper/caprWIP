# SC016 / SC017 relative-chronology adjudication

Registry-verdict: SC016=REFORMULATE/REORDER; SC017=RETAIN

Status: adjudicated (this memo governs the repair)
Scope: SC016 `OEWsPalatalGlide` and SC017 `PNWGmcULowering` only.
Supersedes: the `technical_dependency` classification of SC016 < SC017 in
`sc001-sc020-chronology-audit.tsv` and the "Do NOT move" instruction in the
SC016 row of that audit.

## 0. The problem

Until this repair, the executable cascade ran SC016 (a West Saxon Old
English development) at position 13, immediately BEFORE SC017 (a
Northwest Germanic change) at position 14. The old audit called this a
"technical dependency": *júką would otherwise be lowered to *jóką by
SC017, and SC016 — which only recognized palatal + *u — could then never
produce the ⟨eo⟩ of ġeoc. The executable order was historically inverted
and was retained only because it produced the right outputs.

This memo establishes, from the sources, what actually happened, and
concludes that the inversion concealed TWO defects (diagnosis D below):
SC016 was both in the wrong executable position and incorrectly
formulated.

## 1. Historical formulation of SC017 (u-lowering)

The sources are unanimous and mutually consistent:

- Fulk 2018 §4.3 (p. 56): "when u stood before a mid or low vowel in the
  next syllable (i.e., /a/ or /o(:)/ …) it was lowered to o." Early
  Northwest Germanic: demonstrated earlier than final *-ō > -u (5th c.),
  visible at Gallehus (horna, c. 400 CE). Blocked by a tautosyllabic
  nasal (wunden), apparently also heterosyllabic nasals (fruma, guma,
  cuman), and "when j preceded the non-high vowel conditioning the
  change" (cnyssan, trymman < *knusjaną, *trumjaną).
- Campbell 1959 §115 (p. 43): "u > o before mid and low vowels … with
  considerable regularity": dohtor, god, gold, **geoc yoke (cf. §172)**,
  coren, boren, holpen; not before nasal + consonant; u retained before
  single m (cuman, fruma, guma, sumor).
- Kaluza 1900 §66: "Idg. u vor a, o, e, wenn nicht Nasal + Kons.
  dazwischenstand = urg. o … ae. geoc Joch … ae. gold."
- Ringe & Taylor 2014 (p. 41, cf. line context of the NWGmc chapter):
  stressed *u lowered to *o throughout NWGmc unless a nasal in the
  syllable coda or *j intervened.

Two findings matter for this adjudication:

1. **A word-initial onset *j does NOT block lowering.** Fulk's
   j-blocking clause concerns *j immediately preceding the CONDITIONING
   vowel (*knu-sj-aną type), which the CAPR rule already implements as
   the NoJ restriction on the consonants BETWEEN target and trigger.
   No source gives a preceding-onset palatal any blocking effect.
2. **'yoke' is a standard positive example of the lowering.** Fulk
   (p. 56) lists "OIcel. ok, OE geoc, OHG joh beside juh and OS juk";
   his §4.3 n. 2 reconstructs the paradigmatic split "acc. sg. *joka
   beside gen. pl. *jukum". Campbell §115 lists geoc among the regular
   u > o outcomes. Ringe & Taylor's PWGmc paradigm of 'yoke' (p. 129)
   declines jok, jokas, joke, joku …: lowering applied. Bülbring 1902
   §299 derives WS gioc/geoc "aus wg. *jok, neben *juk § 298".

**Verdict: the current CAPR formulation of SC017 is historically correct
and requires no change.** Applied to the selected input *júką it must
yield *jóką, and any architecture that prevents this firing is wrong.

## 2. Historical formulation of SC016 (palatal glide before back vowels)

What the sources actually describe:

- Campbell 1959 §44 (p. 19): the graphs ea, eo, io can represent "rising
  diphthongs, which were formed when palatal glides developed before
  BACK vowels", examples geara (before a), geoc (before o), geōmrian
  (before ō); "A palatal glide + u is written eo, io or iu in W-S and
  Kt., usually iu in North." Cf. §§172–175 (pp. 65–67).
- Brunner 1965 §92.1 (pp. 64–65) separates the two subcases exactly as
  the phonology requires:
  - §92.1a: eo, early-WS io **for æ. u** in ȝeong 'young', ȝeoguþ
    'youth' (beside iu-/u-forms; late WS regularly eo);
  - §92.1b: "Bei o und ō (verschiedener Herkunft) ist iō, eō ziemlich
    gemein-ae., so ws. ȝioc ȝeoc Joch, ȝiōmrian ȝeōmrian, ȝeōmor" —
    i.e. **yoke belongs to the o-subcase**: the glide spelling applied
    to the product of u-lowering.
- Bülbring 1902 §§298–299 (p. 120): §298 treats iu/ju (iuguð ġuguð
  ġioguð ġeoguð 'youth'; iúng ġúng gióng 'young'; iuc ġeoc); §299
  treats **jo**: "jo ist im Ws. zu gio geo geworden … gioc geoc 'Joch'
  (aus wg. *jok, neben *juk § 298), giōmrian geōmrian … ġeōmor (aus
  *jōmor)". Again two subcases: unlowered u (youth, young) and lowered
  o (yoke, geōmor).
- Luick 1921 §169 (pp. 158–159): before a back vowel after a palatal —
  "hauptsächlich bei anlautendem j" — arose the level-stress
  ("schwebende") diphthongs iu, eo, ea; WS doublets jung/ȝung,
  iuȝoð/ȝuȝod beside ȝionȝ, ȝioȝoð, ȝeo, ȝēomor, geoc; the geo-forms
  were later generalized in spelling. His Anm. 3 supplies the crucial
  internal argument: original FALLING *iu/*eo would have undergone
  Anglian smoothing to *ȝing, *ȝec (§235); attested Anglian geocc,
  ȝiung therefore must be read as ȝ + back vowel (rising), i.e. [jok],
  [jung].
- Ringe & Taylor 2014 (p. 5): "After word-initial /j/ followed by a
  back vowel that practice [writing ⟨e⟩ to mark a palatal] was
  universal. Thus geāra 'formerly' is /jaːra/, geōmor 'sad' is /joːmor/,
  **geoc 'yoke' is /jok/**; exceptionally, geong ~ iung 'young' is
  /jung/." After /tʃ ʃ dʒ/ the practice was not universal.
- Hogg, CHEL I (1992), ch. 3 (p. 112): palatal diphthongisation of
  FRONT vowels is real, but "there is no need to accept that a parallel
  change affecting back vowels … was ever anything more than an
  orthographic variation. The change was inconsistently carried out,
  and the arguments of, for example, Campbell (1959: §176) to
  demonstrate that the change had phonetic consequences are
  insubstantial."

Findings:

1. **Domain.** The phenomenon covers word-initial palatal + BACK vowel
   generally: u (young, youth), o (yoke), ō (geōmor), a/ā (geara, geō).
   The pre-repair CAPR rule recognized only palatal + *u — too narrow —
   and therefore could not treat yoke's lowered *o at all, which is
   what forced the historically inverted early position.
2. **Stage.** Every source places the phenomenon inside the Old English
   period (WS/Kt eo/io, Northumbrian iu, Mercian largely
   undiphthongized). No source places it before Northwest Germanic
   u-lowering; Brunner §92.1b and Bülbring §299 explicitly make lowered
   *o its INPUT.
3. **Phonological status.** The older school (Campbell, Luick, Brunner,
   Bülbring) speaks of real rising/level-stress diphthongs; the modern
   authorities (Ringe & Taylor; Hogg, explicitly against Campbell §176)
   treat the ⟨e⟩ as purely orthographic. The substance is smaller than
   it looks: for word-initial *j the "rising diphthong" [i̯u], [i̯o] is
   segmentally identical to /j/ + back vowel, and the palatal /j/ was
   inherited, not newly developed. Luick's own smoothing argument
   (Anm. 3) and his Jugurtha ~ Ieoweorda evidence show that the nucleus
   remained the back vowel. Middle English reflexes (yok, youthe,
   yong) likewise continue the back vowels directly. CAPR therefore
   follows Ringe & Taylor and Hogg: **no segmental change occurred in
   the ġ + back vowel words; the ⟨e⟩ of ġeoc, ġeoguþ is the West Saxon
   scribal palatal-glide marker.** The disagreement is recorded here
   and in the reader chapter, not silently suppressed.

**Verdict: SC016 as previously implemented (a pre-NWGmc phonological
insertion of *e between palatal and *u) is historically wrong on
formulation, stage, and status.** Its historically defensible content is
an Old English orthographic convention: after word-initial ġ /j/, a back
vowel is written with a preceding glide letter (WS-normalized ⟨eo⟩).

## 3. Supported relative chronology

SC017 precedes SC016 — not as an FST convenience but as history:

1. Stage evidence: SC017 is early NWGmc (Gallehus horna c. 400; before
   final *-ō > -u, Fulk p. 56). SC016 is an OE-period, dialectally
   differentiated WS/Kt practice (Campbell §44; Luick §169; Brunner
   §92; Bülbring §§298–299).
2. Feeding evidence: SC016's domain includes *o < *u (yoke; Brunner
   §92.1b; Bülbring §299; Campbell §115 cross-referencing §172), so
   u-lowering's output is SC016's input. A rule cannot precede the rule
   that creates part of its input class.
3. Trigger evidence: the previous SC016 trigger set included *ʧ, *ʤ, *ʃ
   — segments that do not exist until Old English palatalization, many
   positions later. In its old early slot those clauses were
   unsatisfiable dead code.

## 4. Derivation of YOKE (adjudicated)

PGmc *júką
  → SC017 PNWGmcULowering: *jóką        (Fulk p. 56; Campbell §115;
                                          R&T PWGmc paradigm jok, p. 129)
  → final *-ą apocope: *jók
  → orthography *j → ġ: ġók (phonologically /jok/, R&T p. 5)
  → SC016 (WS glide spelling after word-initial ġ): ġeoc
                                          (Brunner §92.1b; Bülbring §299;
                                          Campbell §§44, 115, 172–173)

Northern control: Li. geocc, Rit./Ru. ioc — Campbell §173: "the basis is
probably o not u", confirming lowering in all dialects with dialectal
spelling of the glide.

## 5. Derivation of YOUTH (adjudicated, independent control)

PGmc *júgunθ-
  → SC017 inapplicable: the following vowel *u is HIGH; the environment
    requires a mid/low vowel (Fulk p. 56). Root *u is retained — this is
    the control that distinguishes a correctly generalized glide rule
    from an over-broadened one.
  → nasal-spirant lengthening and loss: *júgūθ
  → unstressed long-vowel shortening: *júguθ
  → orthography: ġúguþ (phonologically /juɣuθ/)
  → SC016 (glide spelling, u-subcase): ġeoguþ
                                          (Brunner §92.1a; Bülbring §298;
                                          Campbell §172; Luick §169)

The u-subcase and o-subcase surface identically in normalized late WS
(⟨eo⟩), exactly as Brunner's §92.1a/b split describes; early WS io
(gioc, ġioguð) and Anglian iu variants are dialectal spellings not
modeled by CAPR's normalized WS output.

## 6. Dialect restriction

The glide spelling is WS/Kentish ⟨eo/io⟩, Northumbrian usually ⟨iu⟩,
Mercian (Vesp. Ps., Ru.1) regularly undiphthongized (Bülbring §298;
Brunner §92.1; Luick §169.1–3). CAPR's output register is normalized
(late) West Saxon; the rule is scoped accordingly. After /tʃ ʃ/ the
practice was not universal (R&T p. 5; Hogg p. 112 on sc(e)op-type
inconsistency), so the repaired rule is restricted to word-initial ġ
(< PGmc *j; palatalized *ɣ never precedes a back vowel word-initially),
and the old unsatisfiable ʧ/ʤ/ʃ clauses are dropped.

## 7. Uncertainty in the literature

The genuine disagreement is the phonemic status of the glide (real
rising diphthong: Campbell §§44, 170–176, Luick §169, Brunner §92,
Bülbring §§47, 298–299 — versus orthographic marker: R&T p. 5, Hogg CHEL
I p. 112). It does not affect the relative chronology (all parties place
the phenomenon in OE and derive geoc through *jok), only the label of
the final step. CAPR adopts the orthographic reading for the reasons in
§2.3 and presents the disagreement in the reader chapter.

## 8. Why the inverted architecture arose

The original SC016 was written narrowly as palatal + *u because its
paradigm words (yoke, youth) still showed *u at the PGmc input stage. In
that formulation it had to fire before SC017 or yoke would surface as
×ġoc. The inversion was then rationalized as a "technical dependency"
instead of being recognized as the symptom of a mis-formulated,
mis-staged rule. The chronology-card edge "SC016 < SC017 (support 2,
representative failure yoke)" recorded a property of the wrong
formulation, not of history; it is removed and replaced by the
historical edge SC017 < SC016 (feeding, yoke).

## 9. Diagnosis

**D — more than one of the above:**

- (A) SC016 was in the wrong executable position (pre-NWGmc instead of
  Old English), AND
- (B) SC016 was formulated incorrectly (palatal + *u insertion of a
  phonological *e, instead of the WS glide spelling of back vowels
  after word-initial ġ).
- (C) is rejected: SC017's formulation is fully supported and unchanged.

## 10. Implementation directives (govern Phase 3)

1. Remove `OEWsPalatalGlide` from cascade position 13 (both composition
   sites); SC017 fires on yoke's *júką as history requires.
2. Re-implement SC016 in the orthography/surface block, after
   `OldEnglishOrthography` (ġ must exist): after word-initial ġ, back
   vowels *ó/*ú (stressed root vowels of the witnessed domain) are
   written ⟨eo⟩ (starred-tier {*éo}, unstarred by RemoveStars).
   The ā/ō subcases (geara, geōmor) are documented but not implemented:
   no corpus row exercises them and the corresponding CAPR symbols
   never occur after word-initial ġ.
3. Absorb SC093 `OEGlideUToEO` (0 firings; it existed only to repair
   the artificial early-glide path) into the repaired SC016; its R&T
   citation and analysis carry over.
4. Update chronology metadata: SC016 stage → Old English orthographic
   practice (WS); partial order gains SC017 < SC016 (feeding, yoke);
   the old SC016 < SC017 technical edge is deleted.
5. Regression tests: yoke must show *jóką in its trace (SC017 fires);
   youth must show NO lowering of the root vowel; god-type positive and
   nasal/high-vowel negative controls for SC017; ġ+o and ġ+u positive
   controls and non-initial/velar negative controls for SC016.

## Sources

- Campbell, A. 1959. Old English Grammar. §44 (p. 19), §115 (p. 43),
  §§172–175 (pp. 65–67), §176.
- Ringe, D. & A. Taylor. 2014. The Development of Old English. p. 5
  (spelling practice, /jok/); p. 41 (NWGmc u-lowering); p. 129 (PWGmc
  'yoke' paradigm).
- Fulk, R. D. 2018. A Comparative Grammar of the Early Germanic
  Languages. §4.3 (p. 56) with n. 2 (*joka ~ *jukum).
- Hogg, R. M. 1992. "Phonology and morphology", CHEL I, ch. 3. p. 101
  (diphthong system), p. 112 (back-vowel cases orthographic; contra
  Campbell §176).
- Brunner, K. 1965. Altenglische Grammatik. §92.1a–b (pp. 64–65).
- Bülbring, K. 1902. Altenglisches Elementarbuch I. §47 (p. 18),
  §§298–299 (p. 120).
- Luick, K. 1921. Historische Grammatik der englischen Sprache.
  §169 with Anm. 2–4 (pp. 158–159).
- Kaluza, M. 1900. Historische Grammatik der englischen Sprache I.
  §66, §90.
