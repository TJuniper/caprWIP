# Final-`*z` in `*bōkz`, `*gánsz`, `*lūsz` — historical research dossier (2026)

Branch `sc001-sc020-chronology-audit`. Research/documentation only: no
production FST, protoform, TSV, metadata, rule-ID, baseline, or binary change;
no split implemented.

## Research question

CAPR feeds three Old English derivations into the cascade with final `*z` in the
input:

- book:  PROTOFORM = `*bōkz`  → OE bōc
- goose: PROTOFORM = `*gánsz` → OE gōs
- louse: PROTOFORM = `*lūsz`  → OE lūs

Are these historically defensible input forms at the chronological stage CAPR
treats as its proto input, and what do they imply for the interpretation of
SC020?

## Current CAPR facts

- Exact PROTOFORMs: `*bōkz`, `*gánsz`, `*lūsz` (TSV `data/germanic-aligned-final.tsv`).
- SC020 behavior: `EAFFinalZDeletion  {*z} -> 0 || _ .#.` deletes the final `*z`
  of each, yielding `*bōk`, `*gáns`, `*lūs`.
- Phase 1 (provenance, from `docs/debug_snapshots/oe_full_trace_report.txt`)
  established that the final `*z` is **already present in the selected input
  (PROTO/PROTOFORM)** and is carried **unchanged** ("no-change" at every rule)
  from `ProtoInput` until `EAFFinalZDeletion`, which is the first and only rule
  to alter it. No earlier cascade rule creates the `*z`. So the question is purely
  whether the **source reconstruction** is historically appropriate for CAPR's
  West Germanic input stage — not whether the cascade manufactures the `*z`.

All three are **root nouns** (athematic consonant stems), not a- or ō-stems.
That classification drives the whole analysis, because the root-noun nom. sg.
ending is the crux.

---

## book `*bōkz`

### Source reconstructions
- **Kroonen (2013, p. 109):** `*bōk-` f. 'book'; the formation is given as
  `*bōka/ō-` — i.e. an **ō-stem / a-ō-stem** — citing ON bók (pl. bœkr), OE bōc
  (pl. bēc), OFri bōk, OHG buoh, OS bōk, Go. boka 'letter'. Related to
  `*bōk(j)ō-` 'beech'. Kroonen does **not** reconstruct a nom. sg. `*bōkōz` or
  `*bōkz`; his citation is the bare stem `*bōk-`.
- **Orel (2003):** headword `*bōkz` (sb.f.), with a derived `*bōkō` (ō-/ōn-stem;
  Goth boka 'letter'). Orel's `*bōkz` is the form CAPR's PROTOFORM matches.
- **R/T (vol. 2):** treat OE bōc/bēc as a **root noun** (mutation plural bēc),
  not an ō-stem.

### Morphology
OE bōc/bēc is a **root noun** (atypical consonant-declension, i-mutated plural
bēc, parallel to gōs/gȳs 'goose', mūs/mȳs 'mouse'). In a root noun there is **no
thematic vowel**; the case ending attaches directly to the root. Kroonen's
`*bōka/ō-` reflects a **thematized** (ō-stem) formation — a different,
competing stem formation, not the root-noun nom. sg. The two are not the same
cell and must not be conflated.

### Comparative evidence
ON bók (pl. bœkr), OE bōc (pl. bēc), OHG buoh (pl. buohhum, **with** the
root-noun dat. pl. `-um`, explicitly noted by R/T p. 134 as evidence for the
fem. root-noun dat.-inst. pl. in `*-um`). The mutation plural and the OHG
root-noun inflection confirm the root-noun class. No daughter shows a nom. sg.
reflex of final `*-z` for this word.

### Chronological interpretation
R/T (vol. 2 §3.4, pp. 133–134) are explicit: "Whatever the nom. sg. ending of
root nouns might have been in PGmc, it is reasonable to suppose that **there was
no ending in PWGmc, as none of the daughters exhibits any**." So even if PGmc
had a root-noun nom. sg. `*-s`/`*-z`, by the **PWGmc** stage the root-noun
nom. sg. was endingless. CAPR's input represents a **post-PWGmc** chronological
point (it feeds the PWGmc→OE developments), so the appropriate input is the
endingless root noun `*bōk`, not `*bōkz`.

### Provisional verdict
**B — legitimate earlier reconstruction, but chronologically too early for CAPR
input.** `*bōkz` may reflect a PGmc root-noun nom. sg. with `*-z` (Orel's
notation), but the root-noun nom. sg. was endingless by PWGmc. As a **PWGmc-or-
later cascade input** the `*-z` is anachronistic. (If CAPR's proto input is
intended to be PGmc rather than PWGmc, the verdict would differ — that is a
convention question for the author, see Open decisions.)

---

## goose `*gánsz`

### Source reconstructions
- **Kroonen (2013, p. 208):** `*gans-` f. 'goose' (ON gás pl. gæss, OE gōs, OHG
  gans, etc.) < PIE `*ǵʰh₂en-s-` (cf. Skt. haṃsá-, Gk. khēn, Lat. ānser). Kroonen
  reconstructs an **ablauting root paradigm** `*gans`, gen. `*gunzaz` (< PIE
  `*ǵʰh₂én-s`, `*ǵʰh₂n-s-ós`).
- **Orel (2003):** headword `*zansz` (sb.f.), citing ON gás, OE gōs, OHG gans
  (i-stem), and "Goth. `*gansus`" (a u-stem reconstruction for Gothic).

### Morphology
The crucial structural fact: the **`-s` belongs to the stem**, not to an
inflectional ending. PIE `*ǵʰh₂en-s-` is a root **ending in `-s`**; the PGmc
nom. sg. of this root noun is `*gans`, where the final `-s` **is** the stem-final
consonant (the PIE nominative `-s` merged with the stem-final `-s`). A CAPR
input `*gánsz` therefore posits a sequence `*-s-z` — stem-final `-s` **plus** an
additional nom. sg. `*-z`. There is no comparative support for a stacked
`*-sz`: the root already ends in `-s`, and the root-noun nom. sg. is endingless
(R/T §3.4). Orel's `*zansz` is the source of CAPR's `*gánsz` but is best read as
Orel's convention for the root noun's surface shape, not as evidence for a real
`*-s-z` cluster. Gothic `*gansus` (per Orel) is a **u-stem** transfer — a
competing stem formation, again not evidence for nom. sg. `*-z`.

### Comparative evidence
ON gás (pl. gæss), OE gōs (pl. gȳs), OHG gans, OFris gōs. The plural mutation
(gȳs) and the i-stem inflection in OHG confirm a root/athematic noun that
drifted into the i-stems in WGmc. No daughter shows a nom. sg. `*-z`.

### Chronological interpretation
As with book: the root-noun nom. sg. was endingless by PWGmc (R/T §3.4). The
`*-z` in `*gánsz` is doubly questionable — both chronologically (no nom. sg.
ending by PWGmc) and structurally (it would be a stacked `*-s-z`).

### Provisional verdict
**D — likely erroneous CAPR protoform.** `*gánsz` posits a sequence `*-s-z` that
no source reconstructs as a real cluster: the `-s` is the stem-final consonant of
the root noun `*gans-`, and the root-noun nom. sg. had no further `*-z` by PWGmc.
The form is best understood as `*gans` + a spurious `*-z`.

---

## louse `*lūsz`

### Source reconstructions
- **Orel (2003):** headword `*lusz` (sb.f.), citing ON lús, OE lús, MLG lūs
  (i-stem), OHG lūs (i-stem); related to W pl. llau 'lice' < `*luwā`.
- **Kroonen (2013):** the local vision-text witness does not yield a clean
  `*lūs-` headword (OCR gap; the word is treated under related forms). Kroonen's
  practice elsewhere for root nouns is a bare stem (`*bōk-`, `*gans-`), so a
  Kroonen-style reconstruction would be `*lūs-`.
- **R/T (vol. 2):** OE lūs/lȳs is a root noun (mutation plural), parallel to
  mūs/mȳs 'mouse'.

### Morphology
Like goose, the **`-s` is stem-final**: PGmc `*lūs-` is a root noun ending in
`-s` (cf. the cognate mūs 'mouse', R/T line 3172–3173, an exactly parallel
root noun). A CAPR input `*lūsz` again posits a stacked `*-s-z`.

### Comparative evidence
ON lús, OE lús (pl. lȳs), OHG lūs (i-stem), MLG lūs. No daughter shows a
nom. sg. `*-z`; the i-stem drift in WGmc mirrors goose.

### Chronological interpretation
Same as goose and book: root-noun nom. sg. endingless by PWGmc (R/T §3.4).

### Provisional verdict
**D — likely erroneous CAPR protoform.** `*lūsz` posits a stacked `*-s-z` on a
root noun whose stem already ends in `-s`; the root-noun nom. sg. was endingless
by PWGmc. Best understood as `*lūs` + a spurious `*-z`.

---

## Positive controls

Two well-established stressed-monosyllable final-`*z` cases whose WGmc
development is explicitly discussed:

### OE mā 'more'  ←  PGmc `*maiz`
- **Reconstructed input:** PGmc `*maiz` (adv.) 'more' (Goth. mais, ON meir).
  R/T vol. 2 §3.3.1 (p. 86): "PGmc *maiz (adv.) 'more' … > PWGmc *maiz > OE mā,
  OF mā."
- **Development:** stressed monosyllable, final `*-z` **lost** in OE/OF (mā);
  ON retains it as `-r` (meir) via rhotacism. This is a genuine WGmc (Ingvaeonic)
  stressed-monosyllable `*z`-loss.
- **Geographical scope:** WGmc (OE, OF); the adverb is a function word, parallel
  to the pronouns.
- **Source:** Ringe & Taylor 2014, §3.3.1, p. 86; Crist 2002 (appendix, `*maiz`).

### OE cū 'cow'  ←  PNWGmc `*kiaz`
- **Reconstructed input:** PNWGmc `*kiaz` 'cow' (ON kýr). R/T vol. 2 §3.3.1
  (p. 86): "PNWGmc *kiaz 'cow' (?; ON kýr) > PWGmc *kuz (?) > OE cū."
- **Development:** a stressed monosyllable losing final `*-z` (OE cū). R/T note
  that OHG kuo 'cow' is best explained by nom./acc. syncretism, **not** z-loss.
- **Geographical scope:** Ingvaeonic (OE); OHG retains/avoids the loss.
- **Source:** Ringe & Taylor 2014, §3.3.1, pp. 86–87.

### Comparison with book / goose / louse
The controls (mā, cū) are **function words / pronoun-like monosyllables** —
exactly the class that R/T and Crist show DID lose final `*-z` in stressed
monosyllables (cf. the pronouns `*þiz > þē`, `*hiz > hē`, `*hwaz > hwā`). They
are also **stressed monosyllables ending in a vowel + `*-z`**, where the `*-z` is
a genuine morphological/phonological coda, not a stacked cluster.

book, goose, and louse are a **different** structural class: **lexical root
nouns whose stem already ends in the fricative** (`*bōk-` ends in `-k`; `*gans-`
and `*lūs-` end in `-s`). For goose and louse the posited `*-z` would be a
second, stacked sibilant (`*-s-z`), which no source supports; for book the `*-z`
would be a root-noun nom. sg. ending that was already lost by PWGmc. The
controls therefore support the **existence** of a later stressed-monosyllable
`*z`-loss, but they do **not** support treating book/goose/louse as witnesses to
it, because those three are not the right morphological class.

---

## Chronology of final `*-z` loss

Drawing on R/T vol. 2 ch. 3, Fulk, and Crist:

1. **Unstressed final `*-z` loss — early, pan-WGmc (PWGmc).** R/T §3.1.1
   (pp. 44–45): "it seems most reasonable to ascribe the loss of word-final *z in
   unstressed syllables to **PWGmc**." Possibly attested early (Tacitus-era Latinized
   forms; the Frienstedt comb `kaba` for `kamba`, c. 250–300 AD — Fulk §7.8 /
   Fulk p. 2180, citing Schmidt, Nedoma & Düwel 2011 — though the comb shows the
   change had not necessarily reached all of WGmc by then). Crist 2002 §5 treats
   it as established background ("first WGmc *z-deletion … old news").
2. **Stressed-monosyllable final `*-z` loss — late, northern WGmc /
   Ingvaeonic.** R/T §3.1.1 (pp. 44–45) and §3.3.1 (pp. 86–87): "the loss of *-z
   in stressed syllables—i.e. monosyllables—… was not uniform throughout WGmc
   and was clearly a **late** change, probably **post-PWGmc**." The clear
   witnesses are **pronouns and function words** (`*þiz > þē`, `*hiz > hē`,
   `*hwaz > hwā`, `*maiz > mā`, `*kiaz > cū`); OHG retains monosyllabic `-z`
   ("The certain examples of monosyllables ending in *-z did not lose that
   consonant in OHG"). Fulk (citing Markey 1976) lists loss of `*-z` in
   monosyllabic pronouns as typically **Ingvaeonic**. Crist 2002 narrows the
   secondary deletion to a front-vowel environment (`{*i,*e} _ $`).
3. **Lexical monosyllables with stem-final coda `*-z` rhotacize instead of
   deleting.** R/T §3.3.1 (p. 86): PWGmc `*deuz` > OE dēor 'animal',
   `*aiz` > OE ār 'bronze', `*gaiz` > OE gār 'spear' — the `*-z` becomes `-r`
   (rhotacism), and these "can of course owe their -r to levelling from forms
   with overt endings." These do **not** simply delete.
4. **Relation to rhotacism:** all `*z`-loss precedes rhotacism; surviving `*z >
   *r` across WGmc; the whole process is post-PWGmc (R/T §3.3.1 p. 87; Crist 2001
   pp. 106–108). "It seems advisable to assign the entire process to the
   post-PWGmc period."

**The crucial answer:** it is not enough that PGmc had `*-z`. By CAPR's WGmc
input stage, the **unstressed-ending** `*-z` is correctly still present (it is
deleted by SC020 at the right point), but the **root-noun nom. sg. `*-z`** was
already gone by PWGmc, and the **stressed-monosyllable lexical** `*-z` (the
deor/ār/gār type) rhotacized rather than deleting. So the chronological stage at
which CAPR stops representing `*-z` **differs** between unstressed endings
(present until SC020) and stressed lexical monosyllables (already absent, or
rhotacized, by the WGmc stage).

---

## Synthesis

**Historical-rule question:** Is there good evidence for two historically
distinct final-`*z` losses — early in unstressed endings, later northern in
stressed monosyllables? **Yes.** R/T state the two-change analysis explicitly
(§3.1.1, citing Crist 2001: 107–8) and assign the unstressed loss to PWGmc and
the stressed-monosyllable loss to the post-PWGmc (northern/Ingvaeonic) period.

**Corpus-witness question:** Do book, goose, and louse genuinely instantiate the
second (later, stressed-monosyllable) rule? **No — not as currently modeled.**

- The genuine witnesses to the later loss are **pronouns and function words**
  (mā, cū, þē, hē, hwā) — stressed monosyllables ending in a vowel + a real
  morphological `*-z`.
- book (`*bōk-`), goose (`*gans-`), louse (`*lūs-`) are **lexical root nouns**
  whose stem ends in a consonant (`-k`, `-s`, `-s`). Their nom. sg. was
  **endingless by PWGmc** (R/T §3.4), so no `*-z` should be present at CAPR's
  WGmc input stage. For goose and louse the posited `*-z` is additionally a
  **stacked `*-s-z`** with no comparative support.

**Therefore the evidence supports option (b):** the two historical changes are
real, but **some or all of the three current corpus witnesses are bad
protoforms** for CAPR's WGmc input stage. Specifically, goose and louse look
like erroneous stacked-`*z` protoforms (verdict D), and book looks like a
legitimate-but-too-early PGmc form (verdict B).

**Chronology constraint if SC020 is split:** Yes — the later stressed-
monosyllable rule should independently bear a **before-rhotacism (SC003)**
constraint, because Crist's secondary deletion must precede rhotacism (original
`*r` does not delete in those environments) and R/T assign the whole `*z`-loss /
rhotacism complex to the post-PWGmc period. This is independent of the early
rule's existing `SC019 < SC020 < SC003` placement.

## Implications for CAPR

1. The two-loss analysis of SC020 stands (early PWGmc unstressed vs later
   northern stressed monosyllable), and the corpus firing split (111 unstressed
   vs 3 monosyllabic) is real.
2. However, the 3 monosyllabic firings (book, goose, louse) are **not** clean
   witnesses to the later rule. They reach SC020 with a final `*z` that, on the
   evidence, should not have been present at the WGmc input stage at all
   (root-noun nom. sg. was endingless by PWGmc). This points to a **protoform /
   input-selection** issue, not a vindication of the current unconditional rule.
3. The genuine later-loss witnesses (mā, cū, pronouns) are mostly **not** in the
   current 380-row OE corpus as stressed-monosyllable `*z`-deletion cases, so the
   later rule currently has **no clean corpus anchor** among book/goose/louse.
4. Any future split must (a) restrict the early rule to unstressed endings and
   (b) define the later rule's environment from the pronoun/function-word class,
   and (c) resolve what to do about the three current protoforms separately.

## Open author decisions

1. **CAPR input-stage convention:** is the cascade's "proto input" intended to be
   **PGmc** or **PWGmc**? This determines whether `*bōkz` is verdict B (too early
   for a PWGmc input) or acceptable (if the input is PGmc). The chronology
   argument (root-noun nom. sg. endingless by PWGmc) only bites if the input
   represents PWGmc-or-later.
2. **The three protoforms:** whether to correct `*gánsz`/`*lūsz` (drop the
   stacked `*-z`) and re-examine `*bōkz` (root-noun vs ō-stem). This is a data
   decision for Phase 3+, not made here.
3. **Later-rule environment:** whether to adopt Crist's front-vowel conditioning
   (`{*i,*e} _ $`) or a simpler stressed-monosyllable statement — pending a
   decision on whether the genuine witnesses are exclusively front-vowel.
4. **New stable SC id** for the later rule, if a split proceeds (per existing
   convention, not chosen by chronology).

## Bibliography / exact references

- **Ringe, Don & Ann Taylor. 2014.** *The Development of Old English* (A
  Linguistic History of English, vol. 2). Oxford: OUP.
  - §3.1.1, pp. 44–45: loss of word-final `*z` in unstressed syllables ascribed
    to PWGmc; explicit separation from the later stressed-monosyllable loss;
    "two historically separate sound changes (so Crist 2001: 107–8)".
  - §3.3.1, pp. 86–87: stressed-monosyllable `*-z` loss (mā, cū, þē, hē, hwā);
    lexical monosyllables `*deuz>dēor`, `*aiz>ār`, `*gaiz>gār` rhotacize; OHG
    retains monosyllabic `-z`; all `*z`-loss precedes rhotacism; whole process
    post-PWGmc.
  - §3.4, pp. 133–134: root-noun nom. sg. endingless by PWGmc ("none of the
    daughters exhibits any"); OHG buohhum 'books' evidences fem. root-noun dat.
    pl. `-um`.
- **Crist, Sean. 2001.** *Conspiracy in Historical Phonology* (dissertation).
  pp. 106–108: the two final-`*z` deletions as separate changes; rhotacism
  follows.
- **Crist, Sean. 2002.** *An Analysis of *z Loss in West Germanic.* §5 (pan-WGmc
  unstressed final loss, "old news"); §§6–10 (secondary Ingvaeonic deletion,
  front-vowel conditioned `*z > ∅ / {*i,*e} _ $`; never after back vowels; must
  precede rhotacism); appendix (stressed-coda `*z` words incl. `*maiz`).
- **Fulk, R. D. 2018.** *A Comparative Grammar of the Early Germanic Languages.*
  §7.8 (loss of nom. sg. `*-az`); monosyllabic-pronoun `*-z` loss as Ingvaeonic
  (citing Markey 1976); Frienstedt comb `kaba` (c. 250–300) as early but not yet
  pan-WGmc (citing Schmidt, Nedoma & Düwel 2011).
- **Kroonen, Guus. 2013.** *Etymological Dictionary of Proto-Germanic.* Leiden:
  Brill. `*bōk-` f. 'book' (p. 109, ō-stem formation `*bōka/ō-`); `*gans-` f.
  'goose' (p. 208, ablauting root paradigm `*gans`, gen. `*gunzaz`).
- **Orel, Vladimir. 2003.** *A Handbook of Germanic Etymology.* Leiden: Brill.
  `*bōkz` sb.f.; `*bōkō` (ō-/ōn-stem); `*zansz` sb.f. (with Goth. `*gansus`
  u-stem); `*lusz` sb.f.
- **Hogg, Richard M. 1992.** *The Cambridge History of the English Language,
  vol. 1.* p. 37: Gmc `*z` rhotacizes intervocalically, generally lost finally.
- **Campbell, Alistair. 1959.** *Old English Grammar.* p. 166: `*z` "later lost
  or changed to r"; lost finally in unaccented syllables.

**Citation caution:** Kroonen and Orel give **stem / citation** reconstructions
(`*bōk-`, `*gans-`, `*lūs-`); Orel's trailing `z`/`-sz` is a notation for the
root noun's surface shape and is **not** evidence for a stacked `*-s-z` cluster.
R/T's two-change claim is their own analysis citing Crist; Crist's narrower
front-vowel formulation is his own. These have been kept distinct and not
laundered into stronger claims.
