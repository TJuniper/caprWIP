# SC026 / SC027 adjudication — the nasal-spirant complex

Registry-verdict: SC026=SPLIT/RESTRICT/REFORMULATE; SC027=SPLIT/RESTRICT/REFORMULATE; SC103=SPLIT

## Identity

- **SC id:** SC026 (`EAFNasalSpirantLengthening`), SC027 (`EAFNasalSpirantLoss`);
  new identity created by this adjudication: SC103 (`PGmcNasalLossBeforeX`).
- **Executable identifier:** `EAFNasalSpirantLengthening`, `EAFNasalSpirantLoss`,
  `PGmcNasalLossBeforeX` (Foma `define` names; NOT stage claims).
- **Date / branch / base commit:** branch `sc001-sc020-chronology-audit`, base
  commit `5edd0354`.

## Question

- **Hypothesis or suspected problem (falsifiable):** CAPR represents SC026 and
  SC027 as two historical sound changes. Two claims are at issue.
  (1) *Unitarity*: the handbooks describe a single North Sea Germanic
  nasal-spirant law; if so, `SC026 < SC027` is an implementation dependency, not
  a historical relative chronology.
  (2) *Domain*: the executable environment is
  `EnglishStarNasal EnglishStarVoicelessFricative`, and
  `EnglishStarVoicelessFricative` was defined as `[{*f}|{*s}|{*θ}|{*x}]`. If the
  handbooks limit the North Sea Germanic law to *mf, *nþ, *ns and assign nasal
  loss before *x to an earlier pan-Germanic change, the rule overgenerates and
  its `*x` witness (`fist`) is not a witness for this law at all.
- **What would confirm / refute:** (1) is confirmed if no source reconstructs an
  interval between vowel modification and nasal loss, and refuted if any source
  dates them separately or reconstructs an intermediate stage with independent
  consequences. (2) is confirmed if the sources present two changes and if the
  comparative reflexes differ (Ingvaeonic law ⇒ non-Ingvaeonic cognates keep the
  nasal; pan-Germanic change ⇒ the nasal is lost in every daughter); refuted if
  the handbooks treat *nx as one environment of the Ingvaeonic law.

Both were confirmed.

## Current state (before any edits)

- **Existing historical characterization** (registry, quoted): SC026/SC027
  `hist_stage=eaf`, `hist_scope=north_sea_germanic`, `confidence=B`,
  `historical_stage_label=Northwest Germanic`,
  `chronology_profile=reciprocal_or_near_reciprocal`,
  `adjudication_status=unadjudicated`. `staging_notes`: "CAPR two-rule split is a
  modeling articulation of one historical bundled process; keep SC026<SC027".
  The pair therefore already *asserted* unitarity without having adjudicated it,
  and the assertion was nowhere reflected in the rule domain, the witness set, or
  the reader prose.
- **Existing executable behavior:** SC026 mapped eleven vowels
  (`*a *e *i *o *u *æ` + stressed `*á *é *í *ó *ú`) to long counterparts before
  `EnglishStarNasal EnglishStarVoicelessFricative`, at cascade position 23;
  SC027 deleted `EnglishStarNasal` in the same environment at position 24. The
  class comment already read "for NSL (Fulk §4.11: *mf, *ns, *nþ)" while the
  class itself included `{*x}` — a self-contradiction in the source.
- **Selected-input assumptions:** the corpus feeds Proto-Germanic protoforms with
  the nasal still present (`*fúnxstiz`, `*gánsz`, `*júgunθ`); nothing about nasal
  loss is pre-encoded.
- **Existing verdicts/dossiers consulted:**
  `literature_dossiers/026-027-nasal-spirant-corridor.dossier.md`,
  `book_dossiers/026-027-nasal-spirant-corridor.book-dossier.md`,
  `cascade_baseline/historical_audit_table.tsv` (ARCHIVE; already recorded
  "one_historical_change" and "FST name NWGmc* is wrong"). **Neither dossier
  mentions *nx/*nh at all**, and both treat `fist` as a valid witness.

## Diagnosis

### Complete firing census

Before this adjudication the rules fired on 3 of 385 selected corpus rows. A
scan of the whole corpus confirms that these are the only rows containing a
nasal before a voiceless fricative, and that `fist` is the **only** *nx form.

| lexeme | protoform | V | N | fricative | reconstruction | genuine witness for the NSGmc law? | vowel development correct? | environment historically appropriate? |
|---|---|---|---|---|---|---|---|---|
| `goose` | `*gánsz` | *a | *n | *s | PGmc \*gans- (Kroonen p. 168; R&T §5.1.1 p. 140; OHG *gans*, ON *gás*) | **yes** | yes — \*a > \*ą̄ > *ō*, OE *gōs* | yes (*ns) |
| `youth` | `*júgunθ` | *u | *n | *þ | PWGmc \*jugunþi (R&T §5.1.1 p. 140; OHG *jugund*) | **yes** (unstressed-syllable branch) | yes, with a caveat — see below | yes (*nþ) |
| `fist` | `*fúnxstiz` | *u | *n | *x | PGmc \*funhsti- (Kroonen p. 160; OHG *fūst*, G *Faust*, Du *vuist*) | **no** — pan-Germanic change | n/a | **no** (*nx) |

**Overgeneration found.** The generalization over
`EnglishStarNasal EnglishStarVoicelessFricative` extended the North Sea Germanic
law to *nx, an environment no source assigns to it, and to the vowels *e, *o and
*æ, which cannot occur in this position (below).

After the corrections the census is: SC026 2 firings (`goose`, `youth`), SC027 2
firings (`goose`, `youth`), SC103 1 firing (`fist`).

### Principal witness traces (fresh stage bins, post-correction)

```
SC103 PGmcNasalLossBeforeX          fist   *fúnxstiz  *f ú n x s t i → *f ū x s t i   (attested fȳst)
SC026 EAFNasalSpirantLengthening    goose  *gánsz     *g á n s      → *g ō n s        (attested gōs)
                                    youth  *júgunθ    *j ú g u n θ  → *j ú g ū n θ    (attested ġeoguþ)
SC027 EAFNasalSpirantLoss           goose  *gánsz     *g ō n s      → *g ō s
                                    youth  *júgunθ    *j ú g ū n θ  → *j ú g ū θ
```

`fist` no longer passes through SC026/SC027 at all; its `*xst` cluster is now
created at the Proto-Germanic stage, and SC028 `PNWGmcPreconsonantalXLoss`
simplifies it exactly as before. Surface output is unchanged (`fȳst`).

### Witness role classification

| witness | role |
|---|---|
| `goose` | live application of SC026 and SC027; displacement witness for the SC026→SC027 **executable** dependency |
| `youth` | live application of SC026 and SC027; displacement witness for the same dependency |
| `fist` | **withdrawn** from SC026/SC027. Live application of SC103; feeding witness for SC103 → SC028 (SC103 creates the `*xst` cluster SC028 simplifies) |

## Literature

### Existing CAPR dossiers checked

`026-027-nasal-spirant-corridor.dossier.md`,
`026-027-nasal-spirant-corridor.book-dossier.md`. Sound on unitarity, silent on
*nx, wrong on `fist`. Both corrected by this adjudication.

### Sources checked, with page numbers

**Campbell 1959.**
§119 (p. 44): "In Prim. Gmc. the combinations *aŋx, *iŋx, *uŋx became *ā̃x, *ī̃x,
*ū̃x by loss of the nasal consonant, and compensatory lengthening and
nasalization of the vowel… while *ā̃ became ā in Goth., North Gmc., OHG, and OS,
it retained its nasalization, and ultimately became ō in OE and OFris."
Examples: *þēon, fūht, ūhte, þūhte, fōn, þōhte*.
§121 (p. 47): "In OS, OFris., and OE, the so-called Ingvaeonic languages, we find
evidence for a West Gmc. sound-change **similar to the Gmc. one described in
§119**. By this **later** change the groups **mf, ns, nþ** also reject the nasal
consonant with compensatory lengthening and nasalization of the preceding vowel
to ā̃, ī̃, ū̃." Examples: *sōfte, gōs, hōs, ōsle, ōþer, sōþ, tōþ, fīf, fīfel,
hrīþer, līþe, mīþl, sīþ, stīþ, dūst, fūs, hūsl, ūs, cūþ, cūþe, gūþ, mūþ, sūþ*.
Every example has *mf, *ns or *nþ; none has *x. Every input vowel is *a, *i or
*u.

**Fulk 2018.**
§4.1 "Compensatory lengthening upon loss of a nasal consonant": "In the **PGmc.**
consonant group *-ŋx- the nasal consonant was lost, with compensatory lengthening
of the preceding vowel. **The vowels e and o did not occur in this
environment.**… ā̃ produced this way developed to ō in Anglo-Frisian (as in OE
pret. sg. *þōhte*, OFris. *thōchte*) and **did not fall together with OE ā < ai**."
Examples include "OE OHG *fūht* 'damp' < PGmc. \*fū̃xtaz < \*fuŋxtaz".
§4.11: "In a change **comparable to that seen in PGmc. \*fanhanan > \*fā̃hanan
(§4.1)**, in North Sea Germanic a nasal consonant was lost before any voiceless
fricative… **The change thus affects mf, ns, nþ** and produces ā̃, ī̃, ū̃. The
first of these yields **ō in Anglo-Frisian (as does ā̃ inherited from PGmc.)**,
but either ā or ō in OS."

**Ringe 2006 (vol. 1).** PGmc *VN sequences "were realized phonetically as long
nasalized vowels immediately before \*h, since (i) the outcome is a long vowel
**in all the daughter languages** and (ii) the low vowel was rounded, **like
other nasalized low vowels**, in the northernmost dialects of WGmc
('Anglo-Frisian')". Examples \*hanhaną, \*linhtaz, \*þinhaną, \*þanhtaz,
\*þunhtaz.

**Ringe & Taylor 2014, §5.1.1 (pp. 139–41).** "The most obvious phonological
innovation of the northern dialects is the loss of nasals immediately preceding
fricatives, with lengthening and nasalization of the preceding vowel." The
section lists some thirty-odd examples — \*fimf, \*hamfaz, \*samfti, \*anþeraz,
\*tanþ-, \*sanþ-, \*swinþaz, \*finþaną, \*munþaz, \*kunþē, \*gunþiz, \*jugunþi,
\*anstiz, \*hansō, \*gans, \*ansuz, \*uns, \*funsaz, \*hunsla, \*amsla and the
rest — and **not one of them contains \*x**. R&T add that the rule "should have
been subphonemic until the loss of nasalization in the separate prehistories of
the daughters."

**Sievers–Brunner §186.1.** "Geschwunden sind die Nasale vor den stimmlosen
Spiranten **f, þ, s**… wobei altes a zu ō wird, s. §80, Anm. 1." Anm. 3 notes the
loss also in unstressed syllables, where the lengthened vowel is subsequently
**shortened**, citing *ġeoguþ* and *beraþ* < \*beranþ(i) via \*berōþ.
**§80 Anm. 1** unifies the rounding: nasalized ā becomes ō both "bei
gemeingerm. Ausfall vor x" (*fōn, hōn, brōhte, þōhte, ōht*) and "bei anglofries.
Ausfall eines Nasals vor þ, s, f" (*gōs, hōs, sōþ, tōþ, ōþer, softe*) — and the
same §80 covers WGmc ā before nasals (*mōna, mōnaþ, spōn*).

**Luick §301** ("Anglofriesische Wandlungen"). §301.1: V + n before voiceless
spirants gives a long nasalized vowel, later denasalized (\*duɣūþ, \*juɣūþ,
\*berāþ). §301.2: a/ā before nasals → å/ā̃ → o/ō. Luick likewise separates loss +
lengthening from low-vowel rounding, and notes the law operates in stressed and
unstressed syllables alike.

**Hogg 1992** (within pp. 80–4, on runic \*ansuz): "In the Germanic dialects
bordering the North Sea (the so-called Inguaeonic dialects), \*a before a nasal
plus fricative became /oː/ due to rounding, loss of the nasal and compensatory
lengthening"; \*ansuz > \*ōsuz > \*ōs. Compact, unordered, silent on *nh.

**Kroonen, EDPG p. 160.** \*funhsti- f. 'fist': OE *fȳst*, MDu *vuust*, Du
*vuist*, **OHG *fūst*, G *Faust*** ⇐ \*pn̥kʷ-ti-, cf. OCS *pęstь*, probably from
\*pénkwe 'five'. Cf. \*funhtu- 'moist' → OHG *fūht*, G *feucht*.

### Source-supported historical phenomenon

1. **Two distinct nasal-loss developments, not one.** Campbell (§119 vs §121),
   Fulk (§4.1 vs §4.11), Brunner (§80 Anm. 1: "gemeingerm." vs "anglofries.") and
   Ringe (vol. 1 vs R&T §5.1.1) all keep them apart, and Campbell and Fulk state
   the relation explicitly: the Ingvaeonic law is a *later* change *similar* /
   *comparable* to the pan-Germanic one.
2. **A decisive comparative diagnostic.** For the pan-Germanic change the nasal
   is lost in **every** daughter (Go. *hāhan, fāhan, þūhta, brāhta*; OHG *dīhan,
   fūht, fūst, brāhta*). For the Ingvaeonic law the nasal is **retained** outside
   the North Sea area (OHG *fimf, gans, ander, jugund*, ON *gás* excepted as an
   independent Norse development). This is not an argument from silence: it is a
   positive test that every one of R&T's thirty-odd examples passes and that
   `fist` fails.
3. **The Ingvaeonic law is one connected sound change.** Every source states the
   loss and the compensatory lengthening in one breath; the lengthening *is* the
   compensation for the loss, and no source reconstructs an interval between
   them. Campbell §121 "reject the nasal consonant **with** compensatory
   lengthening and nasalization"; Fulk §4.11 "a nasal consonant was lost before
   any voiceless fricative… **and produces** ā̃, ī̃, ū̃"; R&T "loss of nasals…
   **with** lengthening and nasalization"; Brunner §186.1; Luick §301.1.
4. **Nasalization is real and consequential, but its consequence lies
   downstream.** The nasalized long vowel remained distinct long enough to be
   *rounded* rather than merged: Fulk §4.1 is explicit that ā̃ "did not fall
   together with OE ā < ai", and R&T note it stayed subphonemic until
   denasalization in the separate daughters. Its historical work is done entirely
   by the rounding, not by any rule that reads nasality inside this complex.
5. **The rounding of nasalized \*ą̄ is a separate, later Anglo-Frisian change
   with three feeding sources.** Brunner §80 + Anm. 1 unifies (i) WGmc ā before
   nasals (*mōna, mōnaþ, spōn* — CAPR's SC025 witnesses), (ii) the pan-Germanic
   pre-*x change (*fōn, brōhte, þōhte*), and (iii) the Ingvaeonic law (*gōs, tōþ,
   ōþer*) under one rounding. Fulk §4.11 says the same ("as does ā̃ inherited from
   PGmc.").
6. **Geographical scope.** North Sea Germanic / traditionally Ingvaeonic: OE,
   OFris. and OS. Old Saxon participates in the *loss* but only variably in the
   *rounding* (Campbell §121 "West Gmc. ā̃ > ā in OS only"; Fulk §4.11 "either ā
   or ō in OS"). "Anglo-Frisian" is therefore too narrow for the law; R&T's
   "northern West Germanic" and the traditional "Ingvaeonic" pick out the same
   set. Low Franconian stands outside it (Du *gans*, *ander*).
7. **Only \*a, \*i, \*u occur.** Fulk §4.1 "the vowels e and o did not occur in
   this environment"; Campbell §116 n. 4 to the same effect; and every example in
   Campbell §121 and R&T §5.1.1 has *a*, *i* or *u*. PGmc had already raised *e
   to *i and *o to *u before a nasal + consonant.

### CAPR modelling decisions (explicitly NOT source claims)

- Splitting the single Ingvaeonic law into two ordered transducer operations.
  This is a Foma requirement: the vowel rule must read the nasal that the second
  rule deletes.
- Telescoping the Anglo-Frisian rounding of nasalized \*ą̄ into the `*a -> *ō`
  mappings of SC026 and SC103, rather than factoring it out and letting SC025
  perform it. See the SC025 follow-up in "Residue".
- Modelling the pan-Germanic change as a directly composed cascade rule at the
  pgmc editorial holding zone (beside SC022 and SC023) rather than pre-encoding
  its outcome in the corpus protoforms. CAPR models changes; it does not hide
  them in the input.
- Not introducing an explicit nasalized-vowel symbol (see "Historical analysis").

## Historical analysis

- **Historical stage.** SC026/SC027 remain `hist_stage=eaf`. Per
  `cascade_baseline/canonical_stage_scope_ontology.md`, `eaf` is CAPR's
  *operational* corridor "post-PWGmc, pre-OE, English-line" and explicitly does
  not assert Anglo-Frisian exclusivity; the sub-classification is carried by
  scope. This is correct and unchanged. SC103 is `hist_stage=pgmc`.
  The `historical_stage_label` of SC026/SC027 was **wrong** ("Northwest
  Germanic") and is corrected to "North Sea Germanic".
- **Historical scope.** SC026/SC027 `hist_scope=north_sea_germanic` — correct and
  unchanged (traditional label "Ingvaeonic"; R&T's "northern West Germanic" is
  the same set). Not `anglo_frisian`: OS participates in the loss. SC103 is
  `pan_germanic`. Confidence raised B → A: the handbooks are unanimous.
- **Relationship between phenomenon and executable proxy.** Previously
  overgenerating on two axes (the *x environment, and the vowels *e/*o/*æ). Both
  corrected; the proxy is now an exact match for the source-supported domain,
  modulo the telescoped rounding.
- **Is nasalization independently represented?** No, and deliberately so. The
  distinction does real historical work only through the rounding of \*ą̄, and
  CAPR already discharges that work by mapping straight to `*ō` in the two
  lengthening rules — so the contrast with plain `*ā` (< \*ai, SC004; < \*ē₁,
  SC024) is preserved, which is precisely what Fulk §4.1's "did not fall together
  with OE ā < ai" requires. Introducing a nasalized-vowel tier plus a
  denasalization rule would require reordering SC025/SC101/SC004, which this task
  forbids and which no corpus form currently motivates. Recorded as a follow-up,
  not implemented.
- **Chronology evidence.**

  | edge | basis | witness | role |
  |---|---|---|---|
  | SC026 < SC027 | **executable dependency**, not historical chronology | `goose`, `youth` | displacement witness — SC026 must read the nasal SC027 deletes |
  | SC103 < SC026/SC027 | `stage_entailed` (PGmc precedes North Sea Germanic) | — | — |
  | SC103 < SC028 | feeding (SC103 creates the `*xst` cluster) | `fist` | feeding witness; not promoted to an edge here — SC028 is not adjudicated |
  | SC026/SC027 < i-umlaut | executable, retained from the previous state | `goose` | the lengthened vowel must exist before umlaut |
  | earlier boundary | runner-limited by bundled `PWGmcChanges`; **not** overstated | — | — |
  | later boundary | search reached SC087 with no real break; **not** overstated | — | — |

  **The central chronological finding.** `SC026 < SC027` is *non-commutative in
  the transducer* and *not a historical relative chronology*. The two orderings
  are not two datable stages of the language; they are the only two ways to
  linearize one operation whose vowel effect is conditioned by the segment its
  consonant effect removes. The previous evidence record presented this as
  `independently_demonstrated` chronology; it is now labelled for what it is.

## Verdict

- **Verdict:**
  - **SC026 — SPLIT / RESTRICT / REFORMULATE.** \*nx split off to SC103;
    domain restricted to *mf/*nþ/*ns and to the vowels \*a/\*i/\*u; reformulated
    as step 1 of 2 of a single historical sound change.
  - **SC027 — SPLIT / RESTRICT / REFORMULATE.** Same split and restriction;
    reformulated as step 2 of 2 of the *same* historical change. Its
    `canonical_change_id` is set to `SC026` to record that CAPR recognizes **one**
    historical sound-change identity here, executed in two steps. The SC027
    number is retained as a stable executable identifier, not as a second
    historical sound law.
  - **SC103 — SPLIT (new identity).** Proto-Germanic nasal loss before \*x.
- **Hypotheses compared.** **A** (two historical changes) is rejected: no source
  reconstructs an interval, and compensatory lengthening is by definition
  simultaneous with the loss that compensates it. **B** (one law, two executable
  steps) is accepted for the *mf/*nþ/*ns domain. **C** (an articulated
  nasalization → change → deletion → denasalization sequence) is historically
  real but is rejected as a CAPR architecture for now: its only demonstrable
  consequence, the rounding of \*ą̄, is already captured, and representing it
  properly means reopening SC025, which is out of scope. **D** (heterogeneous
  developments) is accepted for the consonantal domain: \*nx belongs to the older
  pan-Germanic change. The final architecture is **D + B**.
- **Machine-readable line:**

  `Registry-verdict: SC026=SPLIT/RESTRICT/REFORMULATE; SC027=SPLIT/RESTRICT/REFORMULATE; SC103=SPLIT`
  (the machine-readable line stands at the head of this memo)

- **Justification.** Campbell §119/§121, Fulk §4.1/§4.11, Brunner §80 Anm. 1 and
  Ringe vol. 1 vs R&T §5.1.1 all distinguish a pan-Germanic loss before \*x from
  a later North Sea Germanic loss before \*f, \*þ, \*s; the comparative reflexes
  confirm the split (OHG *fūst* but OHG *gans*, *jugund*), so CAPR's broad
  voiceless-fricative class conflated two changes and `fist` was never a witness
  for the Ingvaeonic law. Within that law, every source states loss and
  compensatory lengthening as one development, so CAPR's two rules are one
  historical change linearized for the transducer, and the `SC026 < SC027`
  ordering is an executable dependency rather than a datable historical interval.
  The vowel inventory is likewise restricted, since \*e and \*o do not occur
  before nasal + obstruent in Germanic.

## Propagation (only after verdict)

- **Affected files/registries:**
  - `Germanic/fsts/germanic.txt` — `EnglishStarVoicelessFricative` replaced by
    `EnglishStarNSGmcSpirant [{*f}|{*s}|{*θ}]`; new `PGmcNasalLossBeforeX`
    composed immediately after `PNWGmcNStemNLoss`; SC026 vowel set narrowed;
    SC027 environment narrowed; SC028's dependency comment corrected.
  - `registry/sc_registry.tsv` — SC026/SC027 verdict, memo, display names,
    `historical_stage_label`, confidence, notes; SC027 `canonical_change_id`;
    new SC103 row; chapter-2 reader positions shifted by one to seat SC103 at 7.
  - `registry/chronology_edges.tsv` — `fist` withdrawn from the SC026↔SC027
    reciprocal witness set; the edge notes now state that the relation is an
    executable dependency.
  - `registry/sc_inventory_annotations.tsv` — rule snippets, example lexemes and
    notes refreshed; SC103 row added.
  - `reader_facing/026-027-nasal-spirant-changes.md`,
    `book_dossiers/026-027-nasal-spirant-corridor.book-dossier.md`,
    `literature_dossiers/026-027-nasal-spirant-corridor.dossier.md` — rewritten to
    follow the verdict.
  - Generated views regenerated by `adjudicate.py --finalize`. The ARCHIVE
    chronology cards `SC026-*.md` / `SC027-*.md` are annotated, not rewritten.
- **Regression tests added:** `Germanic/tests/test_sc026_sc027_adjudication.py` —
  positive controls (`goose`, `youth` fire in both steps; `fist` fires in SC103),
  negative controls (`fist` fires in neither SC026 nor SC027; no \*x in the
  SC026/SC027 environment; no \*e/\*o/\*æ mappings), metadata controls against the
  canonical registries, and `@requires_runtime` live flookup probes.
- **Baseline/fingerprint effect:** **none expected and none observed.** The
  correction relocates `fist`'s nasal loss from cascade position 24 to position
  23 without altering any surface form: `*fúnxstiz → *fū́xsti → *fū́sti → fȳst`
  exactly as before. Production-vs-sandbox equivalence reports 385/385 rows
  identical; the OE mismatch report holds at 7, all pre-existing documented
  exceptions.

## Residue

### Follow-up 1 — SC025 and the rounding of nasalized \*ą̄ (do not act on here)

Brunner §80 Anm. 1, Fulk §4.11 and Ringe vol. 1 make one Anglo-Frisian rounding
of nasalized low vowels responsible for three feeding sources: WGmc ā before
nasals (CAPR's SC025 `EAFLongANasalRounding`, witnesses *month*, *spoon*), the
pan-Germanic pre-\*x change (now SC103), and the Ingvaeonic law (SC026). CAPR
currently telescopes the rounding into SC026 and SC103 while implementing it
separately as SC025, so one historical change is represented in three places.
Factoring it out would require SC026/SC103 to output nasalized \*ą̄ and SC025 to
be reordered before SC027 (SC025 sits at position 28, after the nasal it
conditions on has been deleted at 25). That is a genuine cross-complex
adjudication of SC025 + SC026 + SC103 and is explicitly out of scope here. No
corpus output depends on it: the telescoped mappings give the correct surface
forms.

### Follow-up 2 — SC028 and the provenance of \*xst (do not act on here)

SC028 `PNWGmcPreconsonantalXLoss` is now fed by SC103 rather than by the
nasal-spirant law, and its source comment has been corrected accordingly. Two
questions belong to the SC028 adjudication, not this one: (i) whether SC028's
`pnwgmc` stage is right, given that OHG *fūst* (< \*funhsti-) also shows the loss
of \*h in \*hst, which would make it at least pan-West-Germanic; (ii) whether
`fist` remains SC028's only live firing once its domain is examined.

### Follow-up 3 — `youth` and unstressed-syllable shortening

Brunner §186.1 Anm. 3 and Luick §301.1 note that the law applies in unstressed
syllables too, but that the lengthened vowel is then shortened again — hence
*ġeoguþ*, not †*ġeogūþ*, and *beraþ* < \*beranþ(i) via \*berōþ. CAPR produces
`*júgūθ` at SC027 and reaches the correct *ġeoguþ* through its later unstressed
shortening machinery, so nothing is wrong; but `youth` is a *stress-conditioned*
witness and should not be cited as if it showed the law's stressed outcome.
Recorded here so that the reader prose and any future witness selection keep the
distinction.

### Not investigated

Old Frisian and Old Saxon corpora are not part of CAPR's English-line model, so
the OS variability in rounding (Campbell §121, Fulk §4.11) is recorded as a scope
fact and not modelled. The relative chronology of the law against the
Anglo-Saxon migration is not pinned down by any source consulted here.
