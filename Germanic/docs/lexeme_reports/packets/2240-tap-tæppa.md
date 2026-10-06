# Evidence packet — 2240 tap / tæppa

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2240 | tap | tæppa | *táppô | *táppô | known_unmodelled | N-stem masc. nom.sg.; attested OE `tæppa` (Orel s.v. *tappòn; Kroonen n-stems §1381). The `æ` is analogical — no cell of the nominal paradigm yields lautgesetzlich `tæpp-` (all cells have back vowels in the following syllable at AFB time), and the Class I weak j-verb pathway yields `teppan` via i-umlaut (not `tæppan`). Most plausibly levelled from the co-radical j-stems which themselves show analogical `æ` in the manner of Fulk §12.19 n.6 on `stæppan`. FST's lautgesetzlich output is `tappa` by A-restoration; mismatch retained as a documented analogical case. See DEV_NOTES §17.10.16a–c. | - |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/tap.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# tap
PROTO: *táppô
EXPECTED: tæppa
OUTPUTS: tappa



### Proto-Germanic consonant inheritance

Proto Input: *táppô

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *tæppô<br>OE A Restoration: *tappô<br>OE Unstressed Long Vowel Shortening: *tappa |



### Orthography & surface

Outcome: tappa

NOTE: N-stem masc. nom.sg.; attested OE `tæppa` (Orel s.v. *tappòn; Kroonen n-stems §1381). The `æ` is analogical — no cell of the nominal paradigm yields lautgesetzlich `tæpp-` (all cells have back vowels in the following syllable at AFB time), and the Class I weak j-verb pathway yields `teppan` via i-umlaut (not `tæppan`). Most plausibly levelled from the co-radical j-stems which themselves show analogical `æ` in the manner of Fulk §12.19 n.6 on `stæppan`. FST's lautgesetzlich output is `tappa` by A-restoration; mismatch retained as a documented analogical case. See DEV_NOTES §17.10.16a–c.
```

### Matching oe_known_problems.tsv entries

| proto | status | category | reason | refs | added |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *táppô | exception | analogical_n_stem_levelling | FST correctly produces tappa (lautgesetzlich nom.sg. of n-stem masc *táppô with A-restoration before back *-ô; cf. crabba, racca, maþa per R/T p.207); attested tæppa has analogical æ — every paradigm cell traps into either A-restoration → tappa/tappan or i-umlaut → teppan, so no PGmc input yields lautgesetzlich tæpp- (Fulk §12.19 n.6 stæppan parallel; plausibly levelled from co-radical j-stems) | DEV_NOTES.md §3097, §14077, §17.10.16a-c, §17.27 | 2026-04-26 |

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:23214 (exact pair)

- Nearby heading: #### §17.10.16c — Revised proposal: accept the mismatch as analogical

```text
23212: 
23213: **Option A (revised).** Retarget TSV row 1202 to the attested n-stem
23214: nom.sg. `tæppa` (PROTOFORM `*táppô`), acknowledging in the NOTE that the
23215: `æ` is analogical (per Fulk's stæppan-style argument, plausibly sourced
23216: from the co-radical j-stems). The FST's lautgesetzlich output `tappa`
```

#### Germanic/docs/DEV_NOTES.md:23223 (exact PROTOFORM)

- Nearby heading: #### §17.10.16c — Revised proposal: accept the mismatch as analogical

```text
23221: | Field | Current | Proposed |
23222: |-------|---------|----------|
23223: | PROTOFORM / PROTO | `*táppan` | `*táppô` |
23224: | COUNTERPART | `tæppan` | `tæppa` |
23225: | NOTE | (n-stem oblique; contradicted) | N-stem nom.sg. `tæppa`; attested `æ` is analogical (Fulk §12.19 n.6 for the parallel `stæppan` case; plausibly levelled from the co-radical j-stem verb/agent noun, which themselves show analogical `æ`). Lautgesetzlich output would be `tappa` by A-restoration; retained as a documented analogical case. |
```

#### Germanic/docs/DEV_NOTES.md:30634 (exact pair)

- Nearby heading: ##### Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail

```text
30632: | 2167 | *sálbō | sealf | breaking |
30633: | 2204 | *spárrô | spearra | breaking + geminate *rr* |
30634: | 2240 | *táppô | tæppa | geminate *pp*, no back-vowel-after-cluster issue (NomSg cluster) |
30635: | 2250 | *θístilas | þistles | (gen.sg., resolved in §17.18.7) |
30636: | 2271 | *wárpą | wearp | breaking |
```

#### Germanic/docs/DEV_NOTES.md:36670 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36668: | `*spárēną` | `spearen` | `sparen` | `sparian` | mismatch (still); deferred to §17.26 (class III/II) |
36669: | `*fáraną`  | `færan`   | `faran`  | `færan`  | now mismatch (etymologically correct); user deferred to a separate loop |
36670: | `*táppô`   | `tappa`   | `tæppa`  | `tæppa`  | **now matching** (−1 mismatch, but see below — this is wrong-side-of-correct) |
36671: | `*láppô`   | `lappa`   | `læppa`  | `lappa`  | **NEW mismatch** |
36672: | `*márōn`   | `mære`    | `mare`   | `mære`   | **NEW mismatch** |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19 (note keyword: i-umlaut)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
17: - [Preconsonantal *x Loss: *xs > *s](#preconsonantal-x-loss-xs--s-before-consonant-clusters)
18: - [PGmc *d/*ð Representation Decision](#decision-2026-03-11-option-2a-confirmed)
19: - [OE þistel 'thistle': Scholarly Controversy](#oe-þistel-thistle-i-umlaut-not-preserved-2026-03-18)
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
```

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

#### Germanic/docs/DEV_NOTES.md:48 (exact COUNTERPART)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
46: - [Labiovelar Proto-Form Corrections](#labiovelar-proto-form-corrections-and-post-velar-w-loss-rt-642)
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
50: - [z-loss/rhotacism and bimoraic/trimoraic cross-source analysis](#historical-phonology-of-final--z-loss-and-its-interaction-with-rhotacism)
```

#### Germanic/docs/DEV_NOTES.md:116 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
114: - Root nouns are a small, archaic class (burg, brust, furh, hnut-); extending the analysis to common nouns like 'wolf' and 'fowl' would be speculative.
115: 
116: **Approach D: Use a derivational form with i-umlaut trigger.**
117: For some of the items, there are derivational forms with *j or *i that block lowering: *wulfi- (hypothetical i-stem variant?), or the derived verb *fullijaną 'to fill' → OE fyllan (where *-ij- blocks lowering of root *u).
118: 
```

#### Germanic/docs/DEV_NOTES.md:120 (note keyword: i-umlaut)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
118: 
119: **What weighs against Approach D:**
120: - These derived forms already show i-umlaut (*fullijaną → fyllan, not full). We can't simultaneously have the u preserved (from the high-vowel context) AND escape i-umlaut. The derivational base is a different word, not a paradigm form of the simplex noun.
121: 
122: ### Luick's doublets evidence
```

#### Germanic/docs/DEV_NOTES.md:709 (note keyword: i-umlaut)

- Nearby heading: ### Summary of OE syncope rules (scholarly consensus)

```text
707: 1. **Non-high vowel syncope** (`*a/*e → ∅`): Applies **regardless of preceding 
708:    syllable weight**, as long as the syllable is stressed. This affects PWGmc `*a` 
709:    and its i-umlaut product `*e`.
710:    
711:    Examples:
```

#### Germanic/docs/DEV_NOTES.md:742 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
740: with paradigm variation:
741: - Nom.sg.: `*melukz` → `meoloc` (with breaking `e → eo`, no syncope)
742: - Gen./dat.sg.: `*milukiz/*miluki` → Anglian `milc` (with i-umlaut and syncope)
743: 
744: R/T §6.6.4 (p.253): "The usual WS form of 'milk' is `meolc < meoluc < *meluk`... 
```

#### Germanic/docs/DEV_NOTES.md:749 (note keyword: i-umlaut)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
747: 
748: **Key point:** The syncopated form `milc` shows **early syncope** that occurred even
749: before i-umlaut — R/T (p.257) notes this as a "possible early instance of syncope."
750: The WS form `meoloc ~ meolc` shows **variable syncope after a light syllable**.
751: 
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

#### Germanic/docs/DEV_NOTES.md:3155 (exact COUNTERPART)

- Nearby heading: ## A-restoration in ō-stems and n-stems: ræst, tæppa, stemn (fronting_missing__afb)

```text
3153: ---
3154: 
3155: ## A-restoration in ō-stems and n-stems: ræst, tæppa, stemn (fronting_missing__afb)
3156: 
3157: ### Overview
```

#### Germanic/docs/DEV_NOTES.md:3164 (exact COUNTERPART)

- Nearby heading: ### Overview

```text
3162: |-------|----------------|------------|------------|
3163: | *rastō | rast | ræst | ō-stem f. |
3164: | *tappô | tappa | tæppa | n-stem m. |
3165: | *stamnăz | stamn | stemn | (see below) |
3166: 
```

#### Germanic/docs/DEV_NOTES.md:3220 (exact COUNTERPART)

- Nearby heading: ### Case 2: *tappô → tappa (expected tæppa) — n-stem masculine

```text
3218: **Complication with (a):** The encoding *rastas uses the a-stem gen.sg. ending *-as, but *rastō is an ō-stem, whose gen.sg. is *-ōz (→ PWGmc *-a → OE -e). The pipeline cannot process *-ōz because it is not in the pgrmWeakTailVowel list, and even if added, the *-ō component would trigger A-restoration. Using *-as is thus a pragmatic encoding that gives the correct phonological result but misrepresents the morphological class.
3219: 
3220: ### Case 2: *tappô → tappa (expected tæppa) — n-stem masculine
3221: 
3222: **Pipeline derivation (nom.sg.):**
```

#### Germanic/docs/DEV_NOTES.md:3227 (exact COUNTERPART)

- Nearby heading: ### Case 2: *tappô → tappa (expected tæppa) — n-stem masculine

```text
3225: This is **phonologically correct** for the nom.sg. The *-ô ending is back and triggers restoration.
3226: 
3227: **But the attested OE form is tæppa (BT headword "tæppa, m.").**
3228: 
3229: **Explanation — paradigmatic leveling from oblique cases:**
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

#### Germanic/docs/analysis/compound_archaism_inventory.md:188 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
187: | **OE NOM.SG. (STANDARD)** | `ræst` (attested as dictionary headword; shows **paradigmatic leveling** from oblique *-æ-* stem) |
188: | **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:189 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
188: | **OE OBLIQUE (GEN.SG./ACC.SG./DAT.SG.)** | `ræste` (front vowel throughout, no A-restoration) |
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
190: | **Lautgesetzlich output** | `rast` (nom.sg., from A-restoration + apocope) BUT oblique cells show `ræste` (front *æ* from AFB, no restoration) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:192 (exact COUNTERPART)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
191: | **Attested simplex** | `ræst` (standard headword, showing paradigmatic leveling of oblique *-æ-* back to nom.sg.) |
192: | **DEV_NOTES reference** | §3.097–3.399 (A-restoration in ō-stems and n-stems: ræst, tæppa, stemn); lines c. 3097–3476 |
193: | **Attestation status** | **`ræst` standard in OE dictionaries (BT headword); oblique forms `ræste` (gen./dat.sg.) well-attested.** The nom.sg. `rast` is lautgesetzlich but rare; `ræst` is the conventional form showing paradigmatic generalization of the oblique stem. |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:48 (note keyword: i-umlaut)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
47: - **nom.sg.** cū (< leveled *kū, analogical from oblique)
48: - **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:49 (note keyword: i-umlaut)

- Nearby heading: ### OE paradigm of cū (§6.6.1, line 18238)

```text
48: - **dat.sg.** cȳ (< *kūi, regular i-umlaut: ū → ȳ)
49: - **nom.-acc.pl.** cȳ (< *kūiz, same i-umlaut)
50: - **gen.sg.** cā (< *kūiz? — form uncertain, R/T say "apparently")
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:61 (note keyword: i-umlaut)

- Nearby heading: ### Hall's Concise Anglo-Saxon Dictionary

```text
60: 
61: This matches R/T's §7 observation (line 21452): "The ō-stem gen. sg. ending -e has spread to fem. root-nouns, where it is in competition with the inherited endingless form with i-umlaut."
62: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:46 (note keyword: i-umlaut)

- Nearby heading: ### OE target assessment

```text
45: 3. **Breaking**: \*æhh → \*eahh
46: 4. **i-Umlaut**: \*eahh → \*ieahh → hiehh (WS palatal diphthong umlaut)
47: 
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:105 (note keyword: i-umlaut)

- Nearby heading: ### Proto-form assessment

```text
104: The proto `*skellinăz` does not match Kroonen's reconstruction. The \*e in
105: \*skellinăz would give OE \*sċiellen (via i-umlaut and palatalization), but the
106: attested form is sċilling with *i.
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:114 (note keyword: i-umlaut)

- Nearby heading: ### Pipeline issues

```text
113: 
114: 2. **With current proto** `skellinăz`: the pipeline produces `sċiellen` (with i-umlaut
115:    of *e → *ie, but no mechanism to produce *i in the root).
```

#### Germanic/docs/analysis/fryhtu_investigation.md:26 (note keyword: i-umlaut)

- Nearby heading: ### R/T's analysis

```text
25: 
26: R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
27: (\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
```

#### Germanic/docs/analysis/fryhtu_investigation.md:34 (note keyword: i-umlaut)

- Nearby heading: ### The \*iþō-abstract analysis

```text
33: with the suffix PGmc \*-iþō-. These are inflectionally ō-stems but contain the
34: derivational element \*-iþ- which triggers i-umlaut. Well-known examples:
35: 
```

#### Germanic/docs/analysis/fryhtu_investigation.md:45 (note keyword: i-umlaut)

- Nearby heading: ### The \*iþō-abstract analysis

```text
44: 
45: 1. **i-umlaut**: \*furhtiþō → \*fyrhtiþō (\*u → \*y, triggered by \*i in suffix)
46: 2. **Medial vowel syncope**: \*fyrhtiþō → \*fyrhþō (unstressed medial \*i lost)
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

#### Germanic/docs/analysis/notable_findings.md:638 (note keyword: A-restoration)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
637: 
638: **Background:** A-restoration (R/T §6.3.1) retracts stressed *æ → *a when
639: a back vowel follows in the next syllable. After Anglo-Frisian Brightening
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

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:239 (note keyword: i-umlaut)

- Nearby heading: ### §4.2 Phonological assessment

```text
238: * **`bȳhþ` / `bȳhst`** (3/2 sg. pres. ind.): would require
239:   i-umlaut of the *u* (or of the inherited *iu* > *í*-stage)
240:   followed by spirantisation/devoicing of the stem-final consonant
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:326 (note keyword: i-umlaut)

- Nearby heading: ### §5.2 Phonological assessment

```text
325:   a-mutation, then *-anaz > -en. Universal attestation.
326: * **`sċȳfþ`** (3 sg. pres. ind.): would require i-umlaut + cluster
327:   realisation parallel to `bȳhþ`; possible but more cascade-
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:32 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
31: > **Inherited West-Gmc /ɣ/ palatalises to OE [ʝ] > [j] (spelt ġ) when it is
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:33 (note keyword: i-umlaut)

- Nearby heading: ## 1. TL;DR

```text
32: > adjacent to a front vowel (i, ī, e, ē, æ, ǣ, y, ȳ from i-umlaut, ie/ī from
33: > i-umlaut, and the front diphthongs io/eo/ea, ie/ȳ) AND a following back
34: > vowel does not "rescue" it.**
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:79 (note keyword: i-umlaut)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959), §§ 426–430

```text
78: > i.e. by æ, e, i, by ǣ, ē, ī, by the diphthongs ǣa, ēa, eo, io, by æ̆ and
79: > ē̆ where these are due to i-umlaut, but not by y, ȳ, œ, ø̄ from i-umlaut of
80: > u, ū, o, ō (cf. § 190)."
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:176 (note keyword: i-umlaut)

- Nearby heading: #### p. 270 — `widuwe` listed under "i, u, y not syncopated"

```text
175: 
176: > A large number of examples show that *i, *u, and *y (the i-umlaut
177: > product of *u) were not syncopated after light syllables. They
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:380 (exact PROTOFORM)

- Nearby heading: ### Option B: Add to `oe_known_problems.tsv`

```text
379: This category aligns with existing `oe_known_problems.tsv` entries
380: (`*fūri` → `analogical_dat_e`; `*táppô` → `analogical_n_stem_levelling`).
381: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1163 (note keyword: i-umlaut)

- Nearby heading: ### B.8 Synthesis across the canvass: answers to questions A-G

```text
1162:   Brunner sec. 114b's account of widwe vs. WS wuduwe.
1163: - Relative to i-umlaut: not directly addressed by these
1164:   authorities for *wi → *wu specifically; Brunner sec. 114a's
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| tap | tæppa | inh | template:inh | tap |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1431 (exact pair)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1429: * `*fúglaz → fogol` (expected `fugol`) — `wontfix: u_lowering_near_labial`
1430: * `*rústō → rost` (expected `rust`) — `wontfix: u_lowering_near_labial`
1431: * `*táppô → tappa` (expected `tæppa`) — `exception: analogical_n_stem_levelling`
1432: * `*wúlfaz → wolf` (expected `wulf`) — `wontfix: u_lowering_near_labial`
1433: * `*wúllō → woll` (expected `wull`) — `wontfix: u_lowering_near_labial`
```

#### Germanic/docs/DEV_NOTES.md:3240 (concept name)

- Nearby heading: ### Case 2: *tappô → tappa (expected tæppa) — n-stem masculine

```text
3238: 
3239: **Sources:**
3240: - BT: headword "tæppa, m." — 'a tap, plug, stopper'. Oblique: tæppan.
3241: - Kroonen: *tappô is an n-stem. No further etymology.
3242: - Web search confirms: tæppa is standard WS, tappa not attested as a standard form.
```

#### Germanic/docs/DEV_NOTES.md:9539 (concept name)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9537: 
9538: - **Fixed: 6** (bake, grave, wade, wake, wash, will)
9539: - **Regressed: 9** (craft, day, mast, raven, staff, tap, wain, lap, wasp)
9540: 
9541: ### Analysis: Why the Fix Fails
```

#### Germanic/docs/DEV_NOTES.md:22946 (concept name)

- Nearby heading: #### Attestation audit for the *tap-* root

```text
22944: bugon/hæfeþ/sċufon precedent (TSV rows 119, 497, 985).
22945: 
22946: #### Attestation audit for the *tap-* root
22947: 
22948: Local reference corpus searched: Kroonen (n-stems), Orel (handbook), Bülbring
```

#### Germanic/docs/DEV_NOTES.md:22956 (concept name)

- Nearby heading: #### Attestation audit for the *tap-* root

```text
22954: | Form | Category | Source | Notes |
22955: |------|----------|--------|-------|
22956: | `tæppa`      | masc. n-stem, nom.sg. ‘tap’ | Orel s.v. `*tappòn` (line 39473); Kroonen n-stems §1381 | Root vowel `æ` |
22957: | `tæppere`    | masc. ja-stem, nom.sg. ‘tapster’ | Hall s.v. `winteppere` (line 26292: `win-tæppere` wine-tapster) | Root vowel `æ`; ja-stem agent noun |
22958: | `tæppestre`  | fem. agent noun ‘tapster-woman’ | Kroonen §1381 (cross-ref.) | (Rare; derivative of the above) |
```

#### Germanic/docs/DEV_NOTES.md:22998 (concept name)

- Nearby heading: #### A third approved path: retarget to the ja-stem weak verb

```text
22996: #### A third approved path: retarget to the ja-stem weak verb
22997: 
22998: The *tap-* root has a well-established derivational co-lexeme in PGmc: the
22999: Class I weak j-verb `*tappjaną` ‘to tap (v.)’ (Kroonen n-stems §1381,
23000: line 17684, explicitly reconstructs `*tappjan-`; cf. ON *teppa* ‘to stop up’,
```

#### Germanic/docs/DEV_NOTES.md:22999 (concept name)

- Nearby heading: #### A third approved path: retarget to the ja-stem weak verb

```text
22997: 
22998: The *tap-* root has a well-established derivational co-lexeme in PGmc: the
22999: Class I weak j-verb `*tappjaną` ‘to tap (v.)’ (Kroonen n-stems §1381,
23000: line 17684, explicitly reconstructs `*tappjan-`; cf. ON *teppa* ‘to stop up’,
23001: OHG *zepfen*, MDutch *tappen*, and ModE *tap* v. continuing a native OE
```

#### Germanic/docs/DEV_NOTES.md:36688 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36686: the rule now denies restoration to all geminate-medial forms,
36687: incorrectly bleeding it for `*láppô → læppa` (target `lappa`) and
36688: spuriously satisfying it for `*táppô → tæppa` (target `tæppa`).
36689: 
36690: The fix is to enumerate geminates as two-segment sequences:
```

#### Germanic/docs/DEV_NOTES.md:36745 (exact pair)

- Nearby heading: ### §17.25.7 Regression after first build — diagnosis and follow-up fix

```text
36743: 
36744: - `*láppô` → `lappa` (matches target — restored from regression).
36745: - `*táppô` → `tappa` (mismatch vs target `tæppa` — now correctly
36746:   diagnosed as a TSV-target issue, parallel to *márōn and *fáraną).
36747: - `*spárōjaną` → `sparian` (the original §17.25 win, retained).
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:292 (note keyword: i-umlaut)

- Nearby heading: ### 4.1 Primary handbooks

```text
291:   - Standard breaking rule: *e → *eo / __ {r, x}C
292: - **§202** (pp. 80–82): Describes i-umlaut of breaking diphthongs
293:   - "A small group of words (§124) suggest that the mutation of eo was io"
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:518 (note keyword: i-umlaut)

- Nearby heading: ### 6.2 Other *i + rd clusters (rhotacized)

```text
517: 1. `*búrdiz` 'birth' (row 1951) → FST: `byrd` ✓
518:    - Expected: `*búrdiz` → u-lowering → `*bordiz` → breaking (blocked, because *o not *e/*i) → i-umlaut `*byrd` ✓
519: 2. `*xérdō` 'herd' (row 2073) → FST: `heord` ✓
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:51 (note keyword: i-umlaut)

- Nearby heading: ## 1. Charge of this supplement

```text
50: 
51: 3. **Parallel with \*rēc** (notable_findings.md #10): OE *rēc* 'smoke' shows universal long ē across all dialects where we expect WS diphthong *īe (from *au + i-umlaut). Both *rēc* and *mēd* avoid expected diphthongs. Is there a systematic development *VzC → VːC* that yields ē regularly, making *meord* the marked form rather than *mēd*?
52: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:522 (note keyword: i-umlaut)

- Nearby heading: ### 5.1 The *rēc case (notable_findings.md #10)

```text
521: **OE rēc** 'smoke' < PGmc *\*raukiz (m. i-stem):
522: - **Expected WS outcome**: *\*rīec (from *au + i-umlaut → *īe)
523: - **Attested outcome**: **rēc** (long ē monophthong, **no diphthong**)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:556 (note keyword: i-umlaut)

- Nearby heading: ### 5.3 Testing the VzC → VːC hypothesis

```text
555: Other *i + rd clusters (after rhotacism):
556: 1. *\*búrdiz* 'birth' → OE *byrd* (no issue; *u lowers, then i-umlaut)
557: 2. *\*xérdō* 'herd' → OE *heord* ✓ (regular breaking of *e → *eo)
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| Luick1914 | single available key for Luick |
| Kaluza1906 | single available key for Kaluza |
| Fulk2018 | single available key for Fulk |
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

### Paradigm probe — tap / tæppa

- PROTO: *táppô
- PROTOFORM: *táppô
- DERIVATION_CLASS: known_unmodelled
- Morphology source: Hand-specified pilot comparison for n-stem singular cells drawn from DEV_NOTES and oe_known_problems.tsv.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen./dat./acc. stem
- Omitted cells: Plural cells omitted in v1; the ledger already states that no paradigm cell yields lautgesetzlich tæpp-.
- Winning form unique: no

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *táppô | tappa | no | TSV input; ledger says this yields regular tappa. |
| gen./dat./acc. stem | *táppan | tappan | no | Representative oblique-stem comparison from DEV_NOTES. |

