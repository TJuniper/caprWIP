# Three-rule adjudication memo: decomposing SC020 final *-z deletion (2026)

Registry-verdict: SC020=SPLIT

Branch `sc001-sc020-chronology-audit`. Phase 2 of the three-rule *-z
programme. Written only after all three research dossiers were complete and
committed:

- Dossier A (`3547c8a5`): `sc020-dossier-a-root-noun-nominative-z.md`
- Dossier B (`298af531`): `sc020-dossier-b-pwgmc-unstressed-final-z.md`
- Dossier C (`108b91e1`): `sc020-dossier-c-northern-monosyllable-final-z.md`
- Phase 0 baseline audit (`bd95fe48`):
  `sc020-three-rule-phase0-current-state.md` +
  `sc020-final-z-firing-audit.tsv`

This memo adjudicates; it changes no FST, corpus, registry, or baseline
artifact. Implementation follows in Phase 3. Scope of implementation and
validation is the **Old English pipeline only** (author instruction); the
Dutch/German/modern-English doculect cascades are not under active
maintenance.

## 1. Are A, B, and C genuinely separate historical developments?

**Yes.** They differ in stage, scope, conditioning, mechanism, and
daughter-language distribution; no pair can be collapsed without
contradicting page-verified evidence.

| | A: consonant-stem nominative *-z | B: unstressed final *-z loss | C: stressed-monosyllable *-z loss |
|---|---|---|---|
| Mechanism | primarily **morphological**: endingless nom.sg. generalized in consonant-final athematic stems (Dossier A §7; Bammesberger 1990: 190–93; Ringe 2017: 306, 313) | regular **phonological** loss of word-final `*z` in unstressed syllables (R/T 2014: 44–45) | regular **phonological** loss of word-final `*z` in stressed monosyllables, with compensatory lengthening (R/T 2014: 86–87) |
| Stage | complete before PWGmc; NWGmc era (R/T 2014: 118: consonant-stem nom.sg. has "no ending" in PWGmc) | PWGmc (R/T 2014: 44–45; Crist 2002 §4 "old news") | post-PWGmc, before OE literacy (R/T 2014: 86–87) |
| Scope | WGmc entirely; NGmc conditionally (ON *bók/gás/lús/nótt* endingless vs. *fótr/mánaðr* with analogical *-r*; Fulk 2018: 167–68) | pan-WGmc (R/T 2014: 44; Frienstedt comb, Fulk 2018: 25 n. 1) | northern WGmc / Ingvaeonic only: OE, OFris, OS; OHG rhotacizes instead (R/T 2014: 86; Fulk 2018: 18 n. 6, citing Markey) |
| Segmental conditioning | after stem-final **consonant** (the nominative marker directly abuts the root coda) | any preceding segment, incl. `*-Vz` and `*-Cz` (`*fadurz`, R/T 2014: 44) | after **vowel**, with compensatory lengthening of a short nucleus |
| Prosodic conditioning | athematic monosyllabic root nouns (see §5 adjudication) | **unstressed** syllable | **stressed monosyllable** |
| Evidence that the ending was still present when the later rule applied | — | Gothic *frijōnds, mēnōþs, miluks* keep *-s*; ON *mánaðr* keeps rhotacized *-r* → the polysyllabic consonant-stem ending survived PGmc breakup and fell in WGmc by B | southern WGmc (OHG) **rhotacizes** the same `*-z` (*ir, wir, mēr*), so the segment survived B and was still present post-PWGmc |

The three-way partition also matches the corpus exactly: every one of the
114 current SC020 firings falls into exactly one of the three candidate
domains (Phase 0 §0.3), and the environments are mutually exclusive
(monosyllabic `*-Cz` / polysyllabic final `*-z` / monosyllabic `*-Vz`).

## 2. Stable ID allocation (registry inspected before allocation)

`sound_change_inventory.tsv` contains 93 rows covering SC001–SC095 with two
gaps: **SC058** (`OENasalDissimilation`, removed as redundant at `1996852c`)
and **SC077** (removed at `8f9b0806`). Both are **retired identifiers**, not
free ones — they persist in committed order-test artifacts
(`order_tests/expanded_pwgmc/*`, `first_break_batch_plan_04.md`) and must
not be reused. SC096 and SC097 appear nowhere in the repository.

| Process | SC ID | Fate |
|---|---|---|
| B — PWGmc unstressed final *-z loss | **SC020** (retained) | existing ID keeps the process that ~96% of its current firings instantiate |
| A — consonant-stem nominative *-z loss | **SC096** (new) | first genuinely unused ID |
| C — northern stressed-monosyllable *-z loss | **SC097** (new) | second genuinely unused ID |

No existing SC is renumbered. SC096/SC097 are chronologically *earlier/later*
than their numeric neighbours; per programme rule, chronology is expressed
by cascade order and staging metadata, never by renumbering.

## 3. Names, stages, scopes

**Naming policy (author instruction, 2026):** FST identifier names and
display names are *not* being adjudicated now. A global renaming/renumbering
pass is expected later; the present task is to get the historical content
right. The identifiers below are working placeholders so Phase 3 can build
distinct machine identities; any of them may be renamed later. In
particular, `EAFFinalZDeletion` keeps its identifier for now even though
Dossier B fixes the stage as PWGmc (making the `EAF` prefix historically
stale) — that mismatch is recorded in staging metadata, not fixed by a
rename.

### SC096 — A

- **Historical content:** loss of the nom.sg. marker `*-z` after stem-final
  consonant in athematic consonant stems
- **Working identifier (placeholder):** any distinct new `define`, e.g.
  `RootNounNomZLoss`
- **Stage/scope metadata:** complete before PWGmc, NWGmc era
  (`hist_stage=pnwgmc`); WGmc absolute, NGmc conditional (notes caveat on
  `pan_pnwgmc`)
- **Confidence:** B (secure for WGmc; NGmc distribution analysis-dependent)
- **v1 chapter:** 2 (PNWGmc→PWGmc corridor; the change must be complete by
  PWGmc per R/T 2014: 118)

### SC020 — B (retained, narrowed, restaged)

- **Historical content:** loss of word-final `*z` in unstressed syllables,
  PWGmc, pan-WGmc
- **Identifier:** `EAFFinalZDeletion` retained as-is for now (see naming
  policy above); alias `EAFFinalZLoss` unchanged
- **Stage/scope metadata:** `hist_stage` `eaf` → **`pwgmc`**, `hist_scope`
  `pan_wgmc` (confirmed, no longer provisional); the
  `rename_completed_scope_unresolved` flag's *scope* half is resolved by
  Dossier B
- **Confidence:** A for the process; the *dagaz/dagas* z-only conditioning
  (R/T 2014: 212) is secure.

### SC097 — C

- **Historical content:** loss of word-final `*z` after vowel in stressed
  monosyllables, with compensatory lengthening; northern WGmc only
- **Working identifier (placeholder):** any distinct new `define`, e.g.
  `MonosyllabicFinalZLoss`
- **Stage/scope metadata:** `hist_stage=eaf`, `hist_scope=north_wgmc`
  (same codes as SC012, the existing Northern West Germanic rule)
- **Confidence:** B (the change is secure; its exact conditioning is
  analysis-dependent — R/T quality-neutral vs. Crist front-vowel, Dossier C
  §3)
- **v1 chapter:** 3 (PWGmc→Anglo-Frisian)
- **Witness status:** genuine but **presently unwitnessed** in the OE
  baseline (Phase 0 §0.3; Dossier C §6). Carried like other unwitnessed
  rules; no protoform is altered to manufacture a witness.

## 4. Environment of each rule

The three environments partition the final-z population with no overlap and
no residue. "Monosyllable" is structural (exactly one vowel nucleus between
word edges); it does not rely on the acute stress marks, which the corpus
omits on trivially-stressed monosyllables (`*bōkz`, `*lūsz`).

| Rule | Historical environment | Implementable statement (Phase 3 designs the Foma) | Corpus domain |
|---|---|---|---|
| A (SC096) | nom.sg. marker `*-z` eliminated in consonant-final athematic stems (morphological, analogically enacted; Dossier A §7) | word-final `z` after a consonant in a monosyllable | 4 forms: `*bōkz`, `*fláuxz`, `*gánsz`, `*lūsz` |
| B (SC020) | word-final `*z` in unstressed syllables, any preceding segment; `*z` only, never `*s` (R/T 2014: 44–45, 212) | word-final `z` in a polysyllable, plus word-final post-consonantal `z` in a monosyllable at corridor stage (catches only contraction-created `*fríundz`; genuine `-Cz#` monosyllables were already consumed by A upstream) | 110 forms (see §5) |
| C (SC097) | word-final `*z` after vowel in a stressed monosyllable; loss + compensatory lengthening (R/T 2014: 86–87) | word-final `z` after a vowel in a monosyllable, with lengthening of a short nucleus | 0 forms |

Two provisos, both recorded rather than hidden:

1. **A's implementable statement is a proxy.** The dossier's verdict is that
   A is primarily morphological (endingless nominative generalized through
   the consonant-stem paradigm), but the corpus contains no morphological
   features the FST could condition on. In this corpus the phonological
   proxy "monosyllabic `-Cz#`" is *exactly coextensive* with the
   morphological class (Phase 0 §0.3), so no lexical list is needed — the
   programme's prohibition on lexical lists disguised as sound laws is
   respected. The prose (book chapter, dossier) carries the morphological
   analysis; the proxy status must be stated in the rule's comment block.
   Should a future corpus row ever present a monosyllabic `-Cz#` form that
   is *not* a consonant-stem nominative, the proxy breaks and the rule must
   be revisited — this guard belongs in the Phase 3 comment.
2. **C is unwitnessed**, so its compensatory-lengthening clause has zero
   corpus effect; it is validated by synthetic unit examples from the
   sources (`*maiz` → `mā`, `*hwaz` → `hwā`; R/T 2014: 86), per the
   programme's allowance for source-based unit tests.

## 5. Adjudication: friend, milk, month → B

The one allocation the dossiers left open (Dossier A §8; Dossier B §7): do
the three polysyllabic consonant-stem nominatives — friend `*fríjōndz`,
milk `*mélukz`, month `*mḗnōθz` — fall under A (with book/goose/louse, as
consonant-stem nominatives) or under B (with the ordinary unstressed class)?

**Decision: B.** Four independent lines of evidence converge:

1. **Direct precedent in the primary source.** R/T 2014: 44 derive
   `*fadurz` — a polysyllabic consonant-stem nominative, structurally
   identical to the friend/milk/month type — by the ordinary PWGmc
   unstressed final `*-z` loss. That is exactly rule B applied to exactly
   this word class.
2. **The ending demonstrably survived into the separate branches.** Gothic
   *frijōnds*, *mēnōþs*, *miluks* retain the nominative sibilant; ON
   *mánaðr* retains its rhotacized reflex (Fulk 2018: 167–68; Bammesberger
   1990: 192–93 fn. 306 for the ON gender split). A process "complete
   before PWGmc and conditionally shared with NGmc" (= A) cannot be what
   removed an ending that North Germanic still shows as *-r*. The
   monosyllabic root nouns behave oppositely: ON *bók*, *gás*, *lús*,
   *nótt* are endingless — they, and only they, pattern with A.
3. **Bammesberger's "nicht lautgesetzlich" does not transfer.** His
   *mēnōþ*-discussion (1990: 186–87) concerns the nominative *without* the
   dental (`*mēnō(z)` with `-þ-` restored from the oblique stem), i.e. a
   vowel-final reconstruction — it is not evidence about the fate of an
   Orel-style `*-θz` cluster and cannot pull month into A.
4. **The author's own programme statement.** Hypothesis A was defined by
   the candidate examples `*bōkz`, `*gánsz`, `*lūsz`; hypothesis B by "the
   large ordinary class currently caught by SC020". Friend/milk/month have
   always been part of that large class.

Computational corollary, which independently favours the same answer: the
corpus also contains shoulder `*skúldramiz` (dat.pl., unstressed `-iz`,
polysyllabic). Any attempt to state A so that it captures polysyllabic
friend/milk/month phonologically would either wrongly capture shoulder or
require a lexical list. With the B-allocation, no lexical conditioning is
needed anywhere.

Consequence for A's formulation: A applies to the **monosyllabic** core of
the consonant-stem class (root nouns proper). The polysyllabic consonant
stems lost their `*-z` later, by the regular unstressed loss — which is
also why NGmc, which does not undergo B, still shows *-r* there. This is
historically coherent, not a convenience: stress is the conditioning
difference, and the nominative marker in a stressed monosyllable sits in
the one position B never touches.

Resulting counts: **A = 4, B = 110, C = 0; total = 114** = the frozen SC020
firing total. No firing disappears from the accounting.

## 6. Chronology and cascade position

Historical (partial) order, from the dossiers:

1. **A** — complete before PWGmc (R/T 2014: 118, 306, 313).
2. **SC019** `PNWGmcFinalLongORaising` — PNWGmc `*-ō` → `*-u`; `*-ōz`
   sheltered (R/T 2014: 15–16, 24; witness: rest `*rástōz`).
3. **B** — PWGmc; before `*a`/`*ą` apocope (R/T 2014: 45–46); feeds
   `PWGmcSurvivingBimoricOUnrounding` and `PWGmcFinalBareALoss` (SC041).
4. **C** — post-PWGmc, northern WGmc only (R/T 2014: 86–87).
5. **Rhotacism** (SC003 `EAFRhotacism`) — last; already scoped non-final
   (`_ ?`), so word-final `*z` is never rhotacized in this cascade
   regardless of order.

Chronological note on A vs. SC019: A precedes PWGmc, and SC019 is PNWGmc,
so their true relative order is A-then-raising or overlapping; they share
no inputs (A: `-Cz#`; SC019: `-ō#`), so cascade order between them is
computationally free with respect to SC019 itself. However, Phase 3
implementation found a hard constraint elsewhere: `PWGmcIjContraction`
(inside `EarlyEnglishLineChanges`) contracts historically polysyllabic
`*fríjōndz` to monosyllabic `*fríundz`, and A's monosyllabic `-Cz#`
environment would then wrongly consume friend (adjudicated to B in §5).
A must therefore be composed **at the head of `EnglishProtoToOE`, before
`EarlyEnglishLineChanges`** — which also best reflects A's pre-PWGmc
date. The hard constraints are:

- A before `PWGmcIjContraction` (so A sees friend in its uncontracted
  polysyllabic shape and passes over it);
- A before B (so book/flea/goose/louse are consumed by A, not B — though
  with the partitioned environments neither can capture the other's
  domain, order still encodes chronology);
- SC019 before B (existing constraint, unchanged: `*-ōz` shelter);
- B before `PWGmcFinalBareALoss`/`PWGmcSurvivingBimoricOUnrounding`
  (existing constraint, unchanged);
- C after B and before rhotacism's stage (computationally free — C's
  domain is untouched by every other rule; place it immediately after B).

No existing ordering constraint in the corridor (Phase 0 §0.2) is
disturbed: the partition of SC020's environment is invisible to every
neighbouring rule because the union of A/B/C's domains equals old SC020's
domain and the outputs are identical for all corpus inputs. **The final
output fingerprint is therefore expected to be exactly unchanged**
(`a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc`); any
deviation in Phase 4 is a stop-and-inspect event, not a refreeze.

## 7. Witnesses vs. comparative controls

| Rule | CAPR witnesses (selected derivations) | Comparative controls (sources only, not in corpus) |
|---|---|---|
| A (SC096) | book `*bōkz`, flea `*fláuxz`, goose `*gánsz`, louse `*lūsz` (4) | mouse `*mūs` (endingless already in Ringe 2017: 149, 313), foot, night, tooth; ON *bók/gás/lús/nótt* vs. *fótr/mánaðr*; Gothic *baúrgs*, *nahts* |
| B (SC020) | 110 = 107 ordinary (67 `-az`, 23 `-iz` incl. shoulder `*skúldramiz`, 14 `-uz`, rest `*rástōz` `-ōz`, three `*θréjez` `-ez`) + friend `*fríjōndz`, milk `*mélukz`, month `*mḗnōθz` (§5) | `*fadurz` (R/T 2014: 44); Frienstedt comb *kaba* (Fulk 2018: 25 n. 1); early runic retentions (`-gastiz`) |
| C (SC097) | **none** (genuine but unwitnessed) | `*maiz` > `mā`, `*hiz`, `*þiz`, `*hwaz` > `hwā`, `*kūz` > `cū` (R/T 2014: 86–87); OHG *ir/wir/mēr* rhotacized (southern contrast) |
| — negative controls (z survives, non-final → rhotacism) | berry `*bázjas`, deer `*déuzą`, hoard `*xúzdą`, learn `*líznō-` (3 rows), meed `*mízdai` (7 rows, 5 lexemes; SC003 witnesses) | OE *dēor, ār, gār* levelled/rhotacized forms (R/T 2014: 86) |

Corpus footnote: row 1935 ball `*bálluz` ends in `-uz` but has
COUNTERPART "-" and is outside the 380-row accepted baseline; it is not
among the 114 audited firings and stays outside the witness accounting
(the narrowed B still covers it identically, so nothing changes for it).

## 8. Fate of SC020 and gate to Phase 3

- **SC020 is retained** with its stable ID and (for now) its existing FST
  identifier, narrowed to the unstressed/polysyllabic environment; its
  staging metadata is corrected to `pwgmc` per Dossier B. It keeps 110 of
  its 114 firings.
- **SC096 (A)** and **SC097 (C)** are created as new, distinct machine
  identities with their own registry rows, staging entries, aliases,
  sandbox checkpoints, and trace stages.
- The old unconditional `EAFFinalZDeletion` body (`{*z} -> 0 || _ .#.`)
  must not survive anywhere in the composition chain once the three rules
  exist; Phase 3 must verify no masking (the sandbox mirror
  `old_english_sandbox.txt` `SEAFFinalZDeletion` included).
- English/German/Dutch doculect cascades share `OldEnglishCore` upstream
  (`EnglishReflexes`, germanic.txt line 3301) and contain final-z inputs
  (`*kōz`, `*brústz`, `*náxtz`) that the narrowed rules treat differently
  from old SC020 (`*kōz` is a stressed monosyllabic `-Vz` → now C's
  domain, with lengthening it previously did not get). Per author scope
  ruling these doculects are out of maintenance: Phase 4 validates the OE
  baseline only, and non-OE drift is noted, not chased. Phase 3 should
  still avoid gratuitous breakage where free choices exist.
- **No unresolved environment blocks implementation.** The single open
  allocation (friend/milk/month) is adjudicated in §5 on page-verified
  evidence; A's proxy status and C's unwitnessed status are recorded, not
  blocking. **Phase 3 may proceed.**

## 9. Answers to the programme's synthesis questions (index)

1. Genuinely separate? — Yes (§1).
2. Best names? — Historical content fixed in §3; identifier naming
   deferred by author instruction (§3 policy note).
3. Stage/scope? — §3 (A: pre-PWGmc NWGmc-era, WGmc + conditional NGmc;
   B: PWGmc, pan-WGmc; C: post-PWGmc, northern WGmc).
4. Environments? — §4.
5. Partial chronology? — §6 (A < B < C < rhotacism).
6. Position vs. rhotacism/vowel rules? — §6 (SC019 < B < SC041; rhotacism
   non-final, unaffected).
7. Witnesses? — §7 (A: 4; B: 110; C: 0).
8. Comparative controls? — §7.
9. Unwitnessed? — C, explicitly retained as such (§3, §7).
10. SC020's fate? — retained for B, narrowed, restaged (§8).
