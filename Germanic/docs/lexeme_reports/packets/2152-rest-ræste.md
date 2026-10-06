# Evidence packet — 2152 rest / ræste

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2152 | rest | ræste | *rastō | *rástōz | late_analogy | Oblique (ō-stem gen.sg.) *rastōz > ræste: PGmc gen.sg. *-ōz did not undergo NWGmcFinalLongORaising (R/T §5.1.3) because *-ō was not word-final (*-z still present). After PWGmc z-loss with vowel shortening and simultaneous AFB-fronting of the unstressed final (*-ōz > {*æ}, R/T §6.8.3 pp.299-300; see DEV_NOTES §17.10.20), suffix is front, no A-restoration, AFB gives ræ-. Attested ræste abundantly in BT (tó ræste, on ræste, etc.). Paradigmatic leveling from oblique ræst- to nom.sg. (cf. R/T §6.3.2 on dag paradigm). | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# rest
PROTO: *rástōz
EXPECTED: ræste
OUTPUTS: ræste



### Proto-Germanic consonant inheritance

Proto Input: *rástōz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *rástō | **Old English**<br>PWGmc Surviving Bimoric O Unrounding: *rástā<br>Anglo Frisian Brightening: *ræstǣ<br>OE Unstressed Long Vowel Shortening: *ræstæ<br>OE Unstressed AE Merger: *ræste |



### Orthography & surface

Outcome: ræste

NOTE: Oblique (ō-stem gen.sg.) *rastōz > ræste: PGmc gen.sg. *-ōz did not undergo NWGmcFinalLongORaising (R/T §5.1.3) because *-ō was not word-final (*-z still present). After PWGmc z-loss with vowel shortening and simultaneous AFB-fronting of the unstressed final (*-ōz > {*æ}, R/T §6.8.3 pp.299-300; see DEV_NOTES §17.10.20), suffix is front, no A-restoration, AFB gives ræ-. Attested ræste abundantly in BT (tó ræste, on ræste, etc.). Paradigmatic leveling from oblique ræst- to nom.sg. (cf. R/T §6.3.2 on dag paradigm).
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3457 (row ID)

- Nearby heading: ### Note on ræst oblique form problem

```text
3455: The ō-stem nom.sg. path is unaffected: `rastō → rast` (NWGmcFinalLongORaising still applies when *-ō is truly word-final).
3456: 
3457: TSV row 2152 (ræst) now uses genuine PGmc gen.sg. *rastōz, target ræste. This follows the same oblique-form approach as cow (*kūi → cȳ) and fire (*fūri → fȳre): the TSV records an oblique paradigm cell that can be derived lautgesetzlich, explaining the attested OE root vowel through regular sound change rather than analogical leveling.
3458: 
3459: ### Historical phonology of final *-z loss and its interaction with rhotacism
```

#### Germanic/docs/DEV_NOTES.md:22554 (exact pair)

- Nearby heading: ### §17.10.15 — Phase 1d-β post-Option-X: source-verified research on the four residual regressions (2026-04-22)

```text
22552: | 1 | 1202    | `*táppan`          | `tappan`   | `tæppan` | `fronting_missing__afb`        |
22553: | 2 | 1051    | `*sáiwalō`         | `sāwul`    | `sāwol`  | `vowel_quality__u_o_alternation` |
22554: | 3 | 862     | `*rástōz`          | `ræst`     | `ræste`  | `final_vowel_missing__weak_noun_like` |
22555: | 4 | 314     | `*fúnðanaz`        | `fundan`   | `funden` | `vowel_quality__unstressed_vowel` |
22556: 
```

#### Germanic/docs/DEV_NOTES.md:22705 (exact pair)

- Nearby heading: #### Case 3 — `*rástōz → ræst` (expected `ræste`)

```text
22703: ---
22704: 
22705: #### Case 3 — `*rástōz → ræst` (expected `ræste`)
22706: 
22707: **Expert consensus — PGmc gen.sg. `*-ōz` → OE `-e` by regular development.**
```

#### Germanic/docs/DEV_NOTES.md:22742 (exact PROTOFORM)

- Nearby heading: #### Case 3 — `*rástōz → ræst` (expected `ræste`)

```text
22740: **What our pipeline does.**
22741: 
22742: 1. `PGmcFinalOZShortening: {*ō}{*z} -> {*a}` turns `*rástōz → *rásta`.
22743: 2. `PWGmcFinalBareALoss: {*a} -> 0 / _ .#.` (our new rule from Option X) deletes
22744:    the `*-a` → `*rást`.
```

#### Germanic/docs/DEV_NOTES.md:23486 (exact pair)

- Nearby heading: #### Decision

```text
23484: 
23485: Mismatch count: **40 → 38**. Case 2 closed. Next: Case 3
23486: (`*rástōz → ræst`, expected `ræste`).
23487: 
23488: 
```

#### Germanic/docs/DEV_NOTES.md:23492 (exact pair)

- Nearby heading: ### §17.10.20 — Case 3 implementation: PGmcFinalOZShortening outputs `{*æ}` directly (Option γ)

```text
23490: ### §17.10.20 — Case 3 implementation: PGmcFinalOZShortening outputs `{*æ}` directly (Option γ)
23491: 
23492: **Case**: `*rástōz → ræst` (expected `ræste`). Final `-e` of f.ō-stem
23493: gen.sg. never materialises — the FST apocopates it.
23494: 
```

#### Germanic/docs/DEV_NOTES.md:23629 (exact pair)

- Nearby heading: #### Probe result

```text
23627: Option γ:               37 mismatches  (Δ = −1)
23628: 
23629: fixed:             *rástōz → ræste
23630: new regressions:   none
23631: ```
```

#### Germanic/docs/DEV_NOTES.md:24149 (exact pair)

- Nearby heading: #### 5. Worked derivation: \*rástōz → ræste under the new pipeline

```text
24147: handles step 8 as before.
24148: 
24149: #### 5. Worked derivation: \*rástōz → ræste under the new pipeline
24150: 
24151:   (a) Input:                              \*rástōz
```

#### Germanic/docs/DEV_NOTES.md:24199 (row ID)

- Nearby heading: #### 7. Pre-implementation audit checklist

```text
24197: 
24198:   [D] **No other \*-ōz-final OE PROTOFORM in the TSV.**
24199:       Already audited §17.10.22: only row 2152. Re-confirm before
24200:       commit.
24201: 
```

#### Germanic/docs/DEV_NOTES.md:25308 (row ID)

- Nearby heading: #### Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)

```text
25306: Methodologically this matches prior precedents: **mannes** (row 2119,
25307: gen.sg. `*mannas`), **spanne** (row 2140, dat.sg. `*spannăi`),
25308: **ræste** (row 2152, gen.sg. `*rastōz`), and **cow/fire** (§3399).
25309: The rule is: when the attested OE form arose by morphological transfer
25310: in a specific cell, encode that cell — do not rig phonology to
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:36 (note keyword: A-restoration)

- Nearby heading: ### Project status and archived work

```text
34: - [Project Status (as of 2026-03-10)](#project-status-as-of-2026-03-10)
35: - [Consonant Mismatch Bucket Refinement (2026-02-07)](#consonant-mismatch-bucket-refinement-2026-02-07)
36: - [A-Restoration Fix (2026-02-06)](#a-restoration-fix-2026-02-06)
37: 
38: ### Working diary
```

#### Germanic/docs/DEV_NOTES.md:47 (note keyword: A-restoration)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
45: - [Cognate set 379 "rock" → corrected to "coat"](#cognate-set-379-rock--corrected-to-coat-rukkăz)
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
```

#### Germanic/docs/DEV_NOTES.md:48 (note keyword: A-restoration)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
50: - [z-loss/rhotacism and bimoraic/trimoraic cross-source analysis](#historical-phonology-of-final--z-loss-and-its-interaction-with-rhotacism)
```

#### Germanic/docs/DEV_NOTES.md:93 (note keyword: gen.sg.)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
95: **What weighs against Approach A:**
```

#### Germanic/docs/DEV_NOTES.md:1379 (note keyword: gen.sg.)

- Nearby heading: ### 1. PWGmcSyllabicJ: *ja/*ją → *i (after light syllable, word-finally)

```text
1377: **Conditioning:** After a light syllable (short vowel + single consonant), word-finally.
1378: **Examples in our data:**
1379: - *bazją → *bazi → berġes ('berry', gen.sg.)
1380: - *harjaz → *hari → here ('army')
1381: - *natją → *nati → net ('net')
```

#### Germanic/docs/DEV_NOTES.md:1649 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1647: ---
1648: 
1649: ## A-Restoration Fix (2026-02-06)
1650: 
1651: **Summary:** Fixed critical foma syntax bug causing A-restoration to apply unconditionally, 
```

#### Germanic/docs/DEV_NOTES.md:1651 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1649: ## A-Restoration Fix (2026-02-06)
1650: 
1651: **Summary:** Fixed critical foma syntax bug causing A-restoration to apply unconditionally, 
1652: then implemented chronology fix to move apocope after restoration.
1653: 
```

#### Germanic/docs/DEV_NOTES.md:1704 (note keyword: A-restoration)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1702:   - Also expanded `OldEnglishARestorationBackVowel` to include `{*ă}` and `{*ą}` (reduced back vowels),
1703:     and expanded `OldEnglishARestorationStrongOTail` to include common weak-tail patterns where
1704:     A-restoration should still apply (infinitives, agent nouns, etc.).
1705:   - Result: `fronting_missing_no_trigger` dropped from 30 to 11 (19 words fixed).
1706: - Top mismatch counts (2026-02-06 report; 280 total at the time):
```

#### Germanic/docs/DEV_NOTES.md:2733 (note keyword: gen.sg.)

- Nearby heading: ### The Three Fates of Word-Final *ō

```text
2731: - Examples: ō-stem acc.sg. *gebō(n?) → *gebō (after ending loss) → PWGmc
2732:     *geba → OE giefe
2733:   ō-stem gen.sg. *gebōz → *gebō (after z-loss) → PWGmc *geba → OE giefe
2734:   fem. n-stem nom.sg. *tungōn → *tungō̃ (after n-loss, nasalized) →
2735:     PWGmc *tunga → OE tunge
```

#### Germanic/docs/DEV_NOTES.md:2738 (note keyword: gen.sg.)

- Nearby heading: ### The Three Fates of Word-Final *ō

```text
2736: - **Our FST**: For fem. n-stems, modelled by NWGmcNStemNLoss: {*ō}{*n} →
2737:   {*ǭ} word-finally, then {*ǭ} → {*æ} → OE -e. This covers the n-stem case.
2738:   For other "surviving bimoric" cases (acc.sg., gen.sg. of ō-stems), we DON'T
2739:   have a rule — but these paradigm cells aren't in our TSV data.
2740: 
```

#### Germanic/docs/DEV_NOTES.md:3131 (note keyword: gen.sg.)

- Nearby heading: ### Root cause: {*æ} should NOT trigger A-restoration

```text
3129: ### Root cause: {*æ} should NOT trigger A-restoration
3130: 
3131: The `{*æ}` symbol was added to the A-restoration trigger set based on an incorrect analysis that suffix *a (like gen.sg. *-as), after being fronted to *æ by AFB, still triggers restoration as an "underlyingly back" vowel.
3132: 
3133: **R/T's paradigm disproves this (§6.3.2, p. 199):**
```

#### Germanic/docs/DEV_NOTES.md:3134 (note keyword: gen.sg.)

- Nearby heading: ### Root cause: {*æ} should NOT trigger A-restoration

```text
3132: 
3133: **R/T's paradigm disproves this (§6.3.2, p. 199):**
3134: - gen.sg. *dagas → *dæges → OE **dæges** (NOT *dages) — A-restoration does NOT fire
3135: - nom.pl. *dagos → OE **dagas** — A-restoration DOES fire (suffix *-os has genuine back *o)
3136: - dat.pl. *dagum → OE **dagum** — A-restoration DOES fire (suffix *-um has genuine back *u)
```

#### Germanic/docs/DEV_NOTES.md:3193 (exact COUNTERPART)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3191: The ō-stem paradigm of *rastō:
3192: - Nom.sg. *rastō → *rastu → restoration → rast (back *-u triggers)
3193: - Acc.sg. *rastō̃ → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3194: - Gen.sg. *rastōz → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3195: - Dat.sg. *rastōi → PWGmc *rastē → AFB (no *a in suffix to front) → ræste (no restoration)
```

#### Germanic/docs/DEV_NOTES.md:3194 (exact COUNTERPART)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3192: - Nom.sg. *rastō → *rastu → restoration → rast (back *-u triggers)
3193: - Acc.sg. *rastō̃ → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3194: - Gen.sg. *rastōz → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3195: - Dat.sg. *rastōi → PWGmc *rastē → AFB (no *a in suffix to front) → ræste (no restoration)
3196: 
```

#### Germanic/docs/DEV_NOTES.md:3195 (exact COUNTERPART)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3193: - Acc.sg. *rastō̃ → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3194: - Gen.sg. *rastōz → PWGmc *rasta → AFB *ræstæ → ræste (front suffix, no restoration)
3195: - Dat.sg. *rastōi → PWGmc *rastē → AFB (no *a in suffix to front) → ræste (no restoration)
3196: 
3197: Only the nom.sg. has the back suffix *-u that triggers A-restoration. All oblique cases (acc., gen., dat.) have front suffix vowels → no restoration → ræst- throughout. The majority oblique pattern was generalized to the nom.sg.: ræst.
```

#### Germanic/docs/DEV_NOTES.md:3202 (exact COUNTERPART)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3200: 
3201: **Sources:**
3202: - BT: headword "ræst" f. 'rest, repose, bed, grave'. Oblique forms: ræste (gen./dat.sg.).
3203: - Kroonen (p.420): *rasto- f. 'interval' — Go. rasta, ON rost, OE rest, OS rasta, OHG rasta. (Kroonen gives OE "rest", i.e. ræst with late OE æ→e.)
3204: - R/T §6.3.1–6.3.2: paradigmatic alternation between a and æ due to A-restoration is explicitly discussed for a-stems (dæg/dagas); same logic applies to ō-stems.
```

#### Germanic/docs/DEV_NOTES.md:3454 (exact COUNTERPART)

- Nearby heading: ### Note on ræst oblique form problem

```text
3452: 2. A new rule `PGmcFinalOZShortening` in PGmcFinalZLoss that maps `{*ō}{*z} → {*a}` at word boundary, applied BEFORE general z-deletion via sequential composition (.o.).
3453: 
3454: **Result:** `rastōz → ræste` ✓ (PGmc gen.sg. *rastōz → OE gen.sg. ræste, well-attested in BT).
3455: The ō-stem nom.sg. path is unaffected: `rastō → rast` (NWGmcFinalLongORaising still applies when *-ō is truly word-final).
3456: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:1 (note keyword: A-restoration)

- Nearby heading: # A-Restoration in Old English: the role of intervening *r and *l

```text
1: # A-Restoration in Old English: the role of intervening *r and *l
2: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:4 (note keyword: A-restoration)

- Nearby heading: # A-Restoration in Old English: the role of intervening *r and *l

```text
3: **Status:** research note (no FST or TSV modifications made).
4: **Scope:** Diagnose why the current FST blocks A-restoration before single *r* and *l*, document the canonical conditioning environment from the philological literature, and propose a single, surgical change to `OEARestorationIntervening` in `Germanic/fsts/germanic.txt`.
5: **Date:** generated 2026-03 from local `docs/references/`.
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:22 (note keyword: A-restoration)

- Nearby heading: ## 1. Executive summary

```text
21: 
22: 2. **The hypothesis is correct.** Across the entire local reference corpus (Campbell, Hogg/CHEL, Ringe & Taylor vol. 2, Brunner, Luick, Bülbring, Kaluza, Kroonen, Orel) **no source treats a single intervening *r* or *l* as blocking A-restoration**. On the contrary, every source that supplies derivations of `sparian`, `warian`, `farian`, `talian`, `carian`, `lapian`, `bapian`, `nacod`, `nafola`, `sadol`, `stapol`, `magu`, `lagu`, `mapa`, `racca`, `crabba`, `flasce`, `mara`, `hara`, `apa`, `maga`, `naca`, `scapa`, `draca`, `cnafa`, `gegada`, `manslaga` etc. derives the surface *a* by exactly the sound-change A-restoration applying across single intervening *r*, *l*, *m*, *n*, *p*, *b*, *d*, *t*, *g*, *f*, *þ*, *s*, *k*, *w*. Liquids are not singled out as a blocking class.
23: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:181 (exact COUNTERPART)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
180: 
181: ### Case 8: *rastō (rest) — ræst / ræste
182: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:188 (exact COUNTERPART)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
187: | **OE NOM.SG. (STANDARD)** | `ræst` (attested as dictionary headword; shows **paradigmatic leveling** from oblique *-æ-* stem) |
188: | **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:50 (note keyword: gen.sg.)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
50: - **gen.sg.** cā (< *kūiz? — form uncertain, R/T say "apparently")
51: - **dat.pl.** cūm (< *kūm(az))
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:56 (note keyword: gen.sg.)

- Nearby heading: ### Hall's Concise Anglo-Saxon Dictionary

```text
55: Hall's confirms:
56: - gen.sg. cū(e), cȳ, or cūs (multiple competing forms — inherited umlaut cȳ vs. analogical -e/-s from other classes)
57: - dat.sg. cȳ
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:69 (note keyword: gen.sg.)

- Nearby heading: ## Full PGmc paradigm reconstruction (Wiktionary + Kroonen + R/T)

```text
68: | acc.sg. | *kōų | cū | Possibly regular (acc. *kōų > *kū after loss of *-ų?), but uncertain |
69: | gen.sg. | *kūiz | cā (or cȳ, cū(e)) | cȳ would be regular i-umlaut; cā is uncertain |
70: | dat.sg. | *kūi | cȳ | **Lautgesetzlich**: i-umlaut ū → ȳ, then contraction/loss of *-i |
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:809 (note keyword: gen.sg.)

- Nearby heading: ## 5. FST-probe relevance

```text
808: 4. The FST output of `meorde` from BOTH `mizdai` (dat.sg.) and
809:    `mizdōz` (gen.sg.) is striking: it means the **paradigm-cell
810:    targeting** approach (the user's preferred framing under
```

#### Germanic/docs/analysis/notable_findings.md:13 (note keyword: A-restoration)

- Nearby heading: ## Table of Contents

```text
12: 3. [PWGmc \*j-related sound changes: formalization of under-specified rules](#3-pwgmc-j-related-sound-changes-formalization-of-under-specified-rules)
13: 4. [A-restoration trigger set: {*æ} is NOT a trigger](#4-a-restoration-trigger-set-æ-is-not-a-trigger)
14: 5. [The stefn/stemn problem: transponent versus reconstruction](#5-the-stefnstemn-problem-transponent-versus-reconstruction)
```

#### Germanic/docs/analysis/notable_findings.md:634 (note keyword: A-restoration)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
633: 
634: ## 4. A-restoration trigger set: {*æ} is NOT a trigger
635: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:66 (note keyword: gen.sg.)

- Nearby heading: ### For \*sumaraz and \*xamaras

```text
65: 4. Both `hamor` and `hamer` are **attested** (Wiktionary: "OE hamor, hamer, homer")
66: 5. Hall's dictionary gives gen.sg. **sumeres** (with -e-), confirming -e- in oblique forms
67: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:100 (note keyword: A-restoration)

- Nearby heading: ### A-restoration — RULED OUT for unstressed syllables

```text
99: 
100: ### A-restoration — RULED OUT for unstressed syllables
101: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:103 (note keyword: A-restoration)

- Nearby heading: ### A-restoration — RULED OUT for unstressed syllables

```text
102: R/T §6.3.1: "those **stressed** \*æ which were immediately followed by a single
103: or geminate consonant... followed by a back vowel became a." A-restoration
104: explicitly applies to **stressed** vowels only. It would not affect the unstressed
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:391 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
390: 
391: ## 4. Retraction and a-restoration
392: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:393 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
392: 
393: a-restoration: Prim. OE `æ` reverts to `a` in open syllables when a back
394: vowel follows in the next syllable. Campbell §157 introduces this as "one
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:419 (note keyword: A-restoration)

- Nearby heading: ## 4. Retraction and a-restoration

```text
418: fronting of /a/ to /a/ or /æ/" — i.e. this is the input to second fronting
419: (see §6 below), distinct from a-restoration proper.
420: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| rest | ræst | inh | template:inh | rest |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2228 (concept name)

- Nearby heading: ### Emergency English rollback

```text
2226: - Restored the production English cascade to the pre-brace definitions so the UI has a working analyzer again. Replaced the brace-aware block in `server/fsts/germanic.txt` with the legacy IPA rules while keeping the sandbox (`server/fsts/english_brace_sandbox.txt`) intact for ongoing experiments.
2227: - Recompiled via `docker compose exec backend sh -lc 'cd /usr/app && foma -f fsts/germanic.txt'`; the resulting `english.bin` once again has full state/arc counts.
2228: - Regression harness replacement: piped all 362 attested English IPA forms through both stacks. `english.bin` now reconstructs 119 forms (rest still `+?` due to longstanding gaps), while `english_brace_sandbox.bin` remains empty—exactly what we want for comparing future brace work against a functioning baseline.
2229: - Next brace steps stay in the sandbox: feed `pgrmWord`, rebuild brace-aware surface filters, only then swap the finished automaton back into `server/fsts/germanic.txt`.
2230: 
```

#### Germanic/docs/DEV_NOTES.md:2917 (concept name)

- Nearby heading: ### Test forms: imperative 2sg and 3sg present indicative

```text
2915: - The *i in *-ōθi triggers i-umlaut of the *ō, giving *ē → e
2916: - The regular phonological outcome is -eþ, not -aþ
2917: - Attested macaþ has -aþ by analogy with the rest of the paradigm
2918: 
2919: ### Findings
```

#### Germanic/docs/DEV_NOTES.md:3203 (concept name)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3201: **Sources:**
3202: - BT: headword "ræst" f. 'rest, repose, bed, grave'. Oblique forms: ræste (gen./dat.sg.).
3203: - Kroonen (p.420): *rasto- f. 'interval' — Go. rasta, ON rost, OE rest, OS rasta, OHG rasta. (Kroonen gives OE "rest", i.e. ræst with late OE æ→e.)
3204: - R/T §6.3.1–6.3.2: paradigmatic alternation between a and æ due to A-restoration is explicitly discussed for a-stems (dæg/dagas); same logic applies to ō-stems.
3205: 
```

#### Germanic/docs/DEV_NOTES.md:16406 (concept name)

- Nearby heading: ### The Regular `*-ar → -er` Development

```text
16404: ### The Regular `*-ar → -er` Development
16405: 
16406: Once we have `*-ar`, the rest is regular per R/T §6.9.6:
16407: 
16408: 1. **Unstressed *a fronting** (§5.1.2): `*a → *æ` in unstressed syllables
```

#### Germanic/docs/DEV_NOTES.md:21942 (concept name)

- Nearby heading: #### B. The A-restoration case analysed phonologically

```text
21940: and j-verbs will still surface correctly.
21941: 
21942: And for non-j-verbs (Class VI and the rest), if we migrate all tail breves
21943: to plain, restoration will fire wherever R/T predicts it — because the rule
21944: already conditions on "back vowel following single non-r-non-l intervening
```

#### Germanic/docs/DEV_NOTES.md:23577 (exact PROTOFORM)

- Nearby heading: #### Option γ — output `{*æ}` directly

```text
23575:   unstressed `{*æ}` to `{*e}` at the expected stage: confirmed.
23576: 
23577: Expected derivation for `*rástōz`:
23578: 
23579: ```
```

#### Germanic/docs/DEV_NOTES.md:23838 (row ID)

- Nearby heading: #### 1. TSV audit (Old_English doculect only)

```text
23836: ```
23837: PROTOFORM-final    count   notes
23838: *-ōz                  1    Row 2152: *rástōz (Case 3 target itself)
23839: *-ô (trimoric)       21    masc. n-stem nom.sg.; distinct symbol
23840: *-ôz                  0    —
```

#### Germanic/docs/DEV_NOTES.md:23931 (row ID)

- Nearby heading: #### 5. Regression-risk summary

```text
23929:     `NWGmcNStemNLoss` before interacting with any of these rules.
23930:   - 0 rows with bare final `*-a` or `*-ā`: **NOT APPLICABLE**.
23931:   - Row 2152 `*rástōz` (Case 3): expected outcome unchanged
23932:     (`ræste`).
23933: 
```

#### Germanic/docs/DEV_NOTES.md:24218 (row ID)

- Nearby heading: #### 8. Expected outcome

```text
24216: 
24217:   - Mismatch count: **37** (unchanged from Option γ).
24218:   - Behaviour for row 2152: `*rástōz → ræste` ✓.
24219:   - Behaviour for all 34 \*-ō, 21 \*-ô, 20 \*-ōn rows: unchanged.
24220:   - No new chronological bundling; each rule corresponds to exactly
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:196 (row ID)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
195: | **Methodological use** | Per the precedent of fire/cow/night/hammer (§3.150), the TSV can target either (a) the oblique form `*rastōz → ræste` (changing both proto and target), or (b) document `ræst` as a paradigmatic-leveling exception with an ALIGNMENT note. The decision depends on whether we prefer "pure lautgesetzlich" or "conventional attested form." |
196: | **Implementation** | TSV now uses gen.sg. `*rastōz`, target `ræste` (following the precedent of paradigm-cell targeting; see §3.399: "RST row 2152 (ræst) now uses genuine PGmc gen.sg. *rastōz, target ræste..."). |
197: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:298 (concept name)

- Nearby heading: ### 2.10 Crist, *Conspiracy in Historical Phonology* (PhD diss., U Penn, 2001)

```text
297: > one possible explanation is that … the rule in question was
298: > lautgesetzlich within Ingvaeonic but sporadic in the rest of WGmc.
299: > Or, perhaps OHG mēta is a loan from Ingvaeonic; it is certainly
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:61 (note keyword: gen.sg.)

- Nearby heading: ### 2.1 Standard dictionary lemmata

```text
60: - Etymology: "from PGmc. *mizdō"
61: - Inflection: strong fem. ō-stem (nom.sg. mēd, acc.sg. mēd/mēde, gen.sg. mēde, dat.sg. mēde)
62: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:260 (note keyword: gen.sg.)

- Nearby heading: ### 3.5 Pathway reconciliation

```text
259: **Option 2**: Analogical leveling from oblique cases
260: - If oblique forms like gen.sg. `*mirdōz` underwent cluster simplification (*rd → *d) early, and the resulting `*mīdōz` was then generalized to the nominative, bypassing the breaking that would have applied to the nom.sg. form
261: - This is highly speculative and lacks parallels
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:414 (note keyword: gen.sg.)

- Nearby heading: ### H2: Target switch to a paradigm cell that doesn't require breaking

```text
413: - **Acc.sg.**: `*mizdō` → same as nom.sg. → `meord`
414: - **Gen.sg.**: `*mizdōz` → final *-ōz → PWGmc *-a → `*mirda` → breaking → `*meorda` → WS `*meorde`
415: - **Dat.sg.**: `*mizdōi` → `*mirdōi` → breaking → `*meordōi` → apocope → `*meorde`
```

#### Germanic/docs/analysis/notable_findings.md:1521 (concept name)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1520:   rīecan retains WS īe regularly. The noun could have been levelled
1521:   toward a vowel-grade variant in the rest of the paradigm (e.g.,
1522:   zero-grade or o-grade in the gen./dat. singular or plural). However,
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:490 (concept name)

- Nearby heading: ### §7.3 Cross-verb summary

```text
489: 1. It is the **morphological pivot** on which the analogical *ū-
490:    present is built, so it is the form that the rest of the
491:    paradigm is most clearly secondary to.
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |
| Kaluza1906 | single available key for Kaluza |
| Orel2003 | single available key for Orel |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Ringe2006 | surname mention only: Ringe |
| Ringe2017 | surname mention only: Ringe |
| RingeTaylor2014 | surname mention only: Ringe |
| Ringe1984 | surname mention only: Ringe |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

