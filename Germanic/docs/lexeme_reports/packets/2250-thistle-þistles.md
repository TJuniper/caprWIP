# Evidence packet — 2250 thistle / þistles

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2250 | thistle | þistles | *θéstilaz | *θístilas | late_analogy | Paradigm-cell target: GenSg þistles (masc. a-stem). NomSg simplex *þistl is unattested in OE manuscripts; the only attested simplex NomSg is broken þistel (via late-WS svarabhakti, Campbell §§360–363, Hogg §§6.30–6.36), which is not modeled in this FST since the other ten -Cl/Cn/Cm# rows (bōsm, botm, hæsl, nǣdl, ofn, hræfn, scofl, stefn, tācn, wǣpn) deliberately target unbroken Beowulf-poetic / early / Anglian forms. GenSg þistles is fully attested as the inflectional stem and lautgesetzlich (medial cluster, no parasiting; Campbell §363 textbook trio). See DEV_NOTES §17.18. | Source: Wiktionary etymology (template:inh) \| Proto corrected: Kluge-Seebold *þistila- with root *i; Orel gives underlying *þe(x)stilaz but all daughter languages show *i (see notable_findings §8) |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/thistle.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# thistle
PROTO: *θístilas
EXPECTED: þistles
OUTPUTS: þistles



### Proto-Germanic consonant inheritance

Proto Input: *θístilas

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *θístilæs<br>OE L Adjacent Syncope: *θístlæs<br>OE Unstressed AE Merger: *θístles |



### Orthography & surface

Old English Orthography: þ*ístles
Outcome: þistles

NOTE: Paradigm-cell target: GenSg þistles (masc. a-stem). NomSg simplex *þistl is unattested in OE manuscripts; the only attested simplex NomSg is broken þistel (via late-WS svarabhakti, Campbell §§360–363, Hogg §§6.30–6.36), which is not modeled in this FST since the other ten -Cl/Cn/Cm# rows (bōsm, botm, hæsl, nǣdl, ofn, hræfn, scofl, stefn, tācn, wǣpn) deliberately target unbroken Beowulf-poetic / early / Anglian forms. GenSg þistles is fully attested as the inflectional stem and lautgesetzlich (medial cluster, no parasiting; Campbell §363 textbook trio). See DEV_NOTES §17.18.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:30113 (row ID)

- Nearby heading: #### §17.18.7.2  Implementation steps

```text
30111:    *-il- shape.
30112: 
30113: 2. **TSV row 2250** (`Germanic/data/germanic-aligned-final.tsv`):
30114:    - PROTOFORM: `*θístilaz` → `*θístilas` (gen.sg.)
30115:    - PROTO: retain `*θístilaz` (etymological cognate root)
```

#### Germanic/docs/DEV_NOTES.md:30114 (exact PROTOFORM)

- Nearby heading: #### §17.18.7.2  Implementation steps

```text
30112: 
30113: 2. **TSV row 2250** (`Germanic/data/germanic-aligned-final.tsv`):
30114:    - PROTOFORM: `*θístilaz` → `*θístilas` (gen.sg.)
30115:    - PROTO: retain `*θístilaz` (etymological cognate root)
30116:    - COUNTERPART: `þistel` → `þistles`
```

#### Germanic/docs/DEV_NOTES.md:30635 (exact pair)

- Nearby heading: ##### Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail

```text
30633: | 2204 | *spárrô | spearra | breaking + geminate *rr* |
30634: | 2240 | *táppô | tæppa | geminate *pp*, no back-vowel-after-cluster issue (NomSg cluster) |
30635: | 2250 | *θístilas | þistles | (gen.sg., resolved in §17.18.7) |
30636: | 2271 | *wárpą | wearp | breaking |
30637: | 2272 | *wáskaną | wascan | sC cluster, A-restoration fires (Campbell §158, *flasce*-class) |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:342 (note keyword: Anglian)

- Nearby heading: # Block if stressed syllable (first syllable) contains *u

```text
340:    - `*wúduwōn` → `wuduwe` (medial `u` preserved, not lowered to `o`)
341: 
342: 3. **Syncopation** in Anglian:
343:    - `*wuduwā` → `widwe` (Mercian), `widua` (Northumbrian)
344: 
```

#### Germanic/docs/DEV_NOTES.md:415 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
413: removing the triggering `*u`, so back mutation couldn't apply.
414: 
415: **Possible explanations for Mercian/Anglian `widwe`:**
416: 
417: 1. **Pre-OE dialectal syncopation**: Some Northwest Germanic dialects may have 
```

#### Germanic/docs/DEV_NOTES.md:464 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
462: |------|------------------------|-------|
463: | `wuduwe` | *widuwō → back mutation → *wuduwō → wuduwe | **WS regular** |
464: | `widwe` | *widuwō → early syncopation → *widwō → widwe | **Anglian/Mercian** |
465: | `widuwe` | `widwe` + analogical vowel restoration → widuwe | **Analogical** (Luick) |
466: | `widua` | = `widuwa` → widua | **Northumbrian** (no syncopation, no BM) |
```

#### Germanic/docs/DEV_NOTES.md:477 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
475: dialectal developments:
476: - WS: no early syncopation → back mutation applies → `wuduwe`
477: - Anglian: early syncopation → back mutation can't apply → `widwe`
478: 
479: The form `widuwe` is **analogical** — a compromise between the syncopated Anglian
```

#### Germanic/docs/DEV_NOTES.md:479 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
477: - Anglian: early syncopation → back mutation can't apply → `widwe`
478: 
479: The form `widuwe` is **analogical** — a compromise between the syncopated Anglian
480: `widwe` and the full three-syllable structure expected from the etymology.
481: 
```

#### Germanic/docs/DEV_NOTES.md:483 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
481: 
482: **For the FST:** Target `wuduwe` as the regular WS outcome. The FST cannot model
483: the early Anglian syncopation (which may be a dialectal retention from NWGmc or
484: a sequence-specific contraction), nor the subsequent analogical restoration to
485: `widuwe`.
```

#### Germanic/docs/DEV_NOTES.md:10415 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10413: | 2026-04-24 | 31 | -1 | 5fa587ab | sife: PROTOFORM *síbaz → *síbi (§17.15) |
10414: | 2026-04-24 | 30 | -1 | 75b8da0d | speoru: short-diphthong weight refactor; *spéru NApl (§17.17) |
10415: | 2026-04-25 | 29 | -1 | 9ccbe617 | þistles: paradigm-cell switch *þístilaz → GenSg (§17.18) |
10416: | 2026-04-25 | 28 | -1 | d5d8acc1 | nafola: PROTOFORM *náblô → *nábulô (R/T pre-syncope, §17.19) |
10417: | 2026-04-25 | 27 | -1 | 3355ec68 | tang: TSV target tange → tang, early-Anglian NomSg (§17.20) |
```

#### Germanic/docs/DEV_NOTES.md:29865 (exact COUNTERPART)

- Nearby heading: #### §17.18.1  The lautgesetzlich background (Campbell §§360–363; Hogg §§6.30–6.36; SB §§145–146)

```text
29863: In **oblique** cells with a vocalic ending (gen.sg. *-es*, dat.sg. *-e*,
29864: nom/acc.pl. *-as/-u*) the same cluster falls **medially**, and parasiting
29865: **does not apply**: gen.sg. *þistles, tācnes, wǣpnes, hræfnes, fugles,
29866: wuldres*. Campbell §363 gives the trio *NomSg tācen / GenSg tācnes*,
29867: *NomSg wǣpen / GenSg wǣpnes*, *NomSg hræfen / GenSg hræfnes* as the
```

#### Germanic/docs/DEV_NOTES.md:29926 (exact COUNTERPART)

- Nearby heading: #### §17.18.3  Attestation findings (per agent research, sources cited at end)

```text
29924: 
29925: 1. **\*þistl is NOT attested as a simplex NomSg spelling in any OE MS.**
29926:    It exists only as inflectional stem (gen.sg. *þistles*, nom/acc.pl.
29927:    *þistlas*) and in compounds (*þistel-twige*, *þistel-mere* — note
29928:    *þistel-* with parasite restored at composition boundary, never
```

#### Germanic/docs/DEV_NOTES.md:29944 (exact COUNTERPART)

- Nearby heading: #### §17.18.3  Attestation findings (per agent research, sources cited at end)

```text
29942: 
29943: 4. **The GenSg / oblique stem is uniformly unbroken** for all 11 words
29944:    across all dialects and registers: *þistles, bōsmes, botmes, hæsles,
29945:    nǣdle, ofnes, hræfnes, scofle, stefnes, tācnes, wǣpnes*. Campbell
29946:    §363 explicitly invokes this trio as the textbook contrast.
```

#### Germanic/docs/DEV_NOTES.md:29999 (exact COUNTERPART)

- Nearby heading: ##### Option 3 — Paradigm-cell strategy: target GenSg (or other oblique) for the whole class

```text
29997: across all dialects:
29998: 
29999:    *þistles, bōsmes, botmes, hæsles, nǣdla*(?), *ofnes, hræfnes, scofle,
30000:    stefnes, tācnes, wǣpnes*.
30001: 
```

#### Germanic/docs/DEV_NOTES.md:30096 (exact COUNTERPART)

- Nearby heading: #### §17.18.7.1  Resolved policy

```text
30094: The resolution is therefore to **target a different, fully attested,
30095: fully lautgesetzlich paradigm cell** for *þistilaz: the **gen.sg.**
30096: *þistles*. In gen.sg. the cluster is medial (no word-final environment),
30097: parasiting does not apply (Campbell §363, Hogg §6.36), and *þistles* is
30098: directly attested as an inflectional form throughout the OE corpus.
```

#### Germanic/docs/DEV_NOTES.md:30108 (exact PROTOFORM)

- Nearby heading: #### §17.18.7.2  Implementation steps

```text
30106:    gen.sg. masc a-stem ending `i:{*i} l:{*l} a:{*a} s:{*s}` parallel to
30107:    the existing nom.sg. `i:{*i} l:{*l} a:{*a} z:{*z}`. This admits
30108:    `*θístilas` as a valid PROTOFORM. No other gate changes required;
30109:    line 319's `a:{*a} s:{*s}` already handles *-as for syncopated heavy
30110:    stems, so the *-ilas* twin only needs to cover the unsyncopated
```

#### Germanic/docs/DEV_NOTES.md:30715 (exact PROTOFORM)

- Nearby heading: ##### Option A — Change TSV PROTOFORM to *nabulô* (R/T-style pre-syncope reconstruction)

```text
30713: - **Consistent with project precedent**: this is the same kind of
30714:   proto-form refinement done in §17.14 (*\*kwedu* > *\*kweðuz*), §17.16
30715:   (*\*spéru*), and §17.18.7 (*\*θístilaz* → *\*θístilas*) — pick the
30716:   proto-form that matches the lautgesetzlich derivation in R/T.
30717: 
```

#### Germanic/docs/DEV_NOTES.md:30955 (exact PROTOFORM)

- Nearby heading: #### §17.19.6  Bibliography

```text
30953:   - DEV_NOTES.md §17.15 / §17.16: *sife*, *spere* PROTOFORM research —
30954:     same Option A precedent.
30955:   - DEV_NOTES.md §17.18.7 (lines 29932ff.): *\*θístilas* paradigm-cell
30956:     fix; sets the convention of splitting PROTOFORM (the input the FST
30957:     actually consumes) from PROTO (the cross-Germanic etymological
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:14 (note keyword: Anglian)

- Nearby heading: # Archaism Preservation Inventory: Where Lautgesetzlich Forms Survive in OE

```text
13: > but no such compound is attested. The actual preservation locus for *meord* is
14: > a **dialectal doublet** (Anglian *meord* vs. WS *mēd*), not a compound.
15: >
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:29 (note keyword: Anglian)

- Nearby heading: ## Introduction

```text
28: - **Compound first-elements** (especially as the first member of nominal compounds, where stem form is preserved and analogical pressure from inflectional paradigms is reduced) — this is the classical "Watkins principle" locus.
29: - **Dialectal doublets** — one OE dialect retains the lautgesetzlich form while another shows analogical leveling. Anglian forms are particularly prone to this because of conservative scribal traditions in Bede glosses, the Vespasian Psalter, and parts of the poetic corpus.
30: - **Oblique paradigm cells** — non-nominative cases (gen.sg., dat.sg., pl.) sometimes retain forms that the nom.sg. has lost.
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:56 (note keyword: Anglian)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
55: | **PROTO** | `*mizdō` (f., strong ō-stem; PIE *misdʰ-o/eh₂-) |
56: | **OE FORMS** | WS **mēd** ; Anglian-leaning **meord** (dialectal doublet) |
57: | **Preservation locus** | **Dialectal doublet** — not a compound. The lautgesetzlich post-rhotacism + breaking output (*z → r*; *i → eo / _r+C*) is preserved as the Anglian-leaning simplex *meord*, while WS shows the post-z-loss outcome *mēd* (z-loss + comp. lengthening + lowering of long *ī to ē). |
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:36 (note keyword: Anglian)

- Nearby heading: ### OE target assessment

```text
35: The TSV has `hlæhhan`. R/T give the WS form as **hliehhan** (lines 3674, 10264,
36: 13896, 19594) and the Anglian poetic form as **hlehhan** (line 13897). The form
37: `hlæhhan` is not specifically given by R/T.
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:53 (note keyword: Anglian)

- Nearby heading: ### OE target assessment

```text
52: 
53: **TSV target should be `hliehhan`** (WS) or `hlehhan` (Anglian).
54: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:133 (note keyword: Anglian)

- Nearby heading: ### 2.4 Brunner, *Altenglische Grammatik* (3rd ed. 1965, after Sievers)

```text
132: 
133: **Position.** Brunner explicitly characterises *meord* as **Anglian and
134: poetic**, with the diphthong *eo* arising from the breaking-style
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:139 (note keyword: Anglian)

- Nearby heading: ### 2.4 Brunner, *Altenglische Grammatik* (3rd ed. 1965, after Sievers)

```text
138: uniformly under *mēd-*, consistent with Brunner treating *meord* as
139: the Anglian/poetic doublet member.
140: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:546 (note keyword: Anglian)

- Nearby heading: ### 2.17 Kilday, "Crist's Law, Smith's Law, and English *wizen*" (2024 draft)

```text
545: this distribution claim; the cited primary attestations in §1 above
546: are all from Anglian-leaning texts (Bede translation, Phoenix,
547: Gregory's Dialogues), consistent with Kilday but not strictly proving
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:1 (note keyword: Anglian)

- Nearby heading: # West Saxon vs. Anglian: dialect differences in Old English

```text
1: # West Saxon vs. Anglian: dialect differences in Old English
2: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:31 (note keyword: Anglian)

- Nearby heading: ## 1. Smoothing (Anglian monophthongisation before velars)

```text
30: 
31: ## 1. Smoothing (Anglian monophthongisation before velars)
32: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:37 (note keyword: Anglian)

- Nearby heading: ## 1. Smoothing (Anglian monophthongisation before velars)

```text
36: It does **not** apply before dental clusters or non-velar environments. It
37: is the diagnostic Anglian feature.
38: 
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:156 (note keyword: Anglian)

- Nearby heading: ## §3. The fault-line: `-un > -on` for stem-`u` verbs is analogical

```text
155:   Brunner §364.2 Anm. 4). For the two specific verbs we care about
156:   here, the early Anglian/Mercian witnesses simply do not contain
157:   a finite 3 pl. pret. token — the verb is unattested in those
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:117 (note keyword: Anglian)

- Nearby heading: ### Direct corpus attestations

```text
116: 
117: The early Anglian/Mercian texts that *would* show `-un` if they
118: preserved this verb in 3 pl. pret. — the Épinal, Erfurt, and Corpus
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:125 (note keyword: Anglian)

- Nearby heading: ### Direct corpus attestations

```text
124: i.e. weak `bīegan` 'to bend (something)', not the strong intransitive
125: `būgan`.) The `-un` Anglian preterite-plurals well-attested for other
126: verbs (e.g. VP `forleortun`, `fornōmun`, `āwoestun`, `gnornadun`,
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:178 (note keyword: Anglian)

- Nearby heading: ### Local handbook evidence

```text
177: **Bülbring §302** (`bulbring_altenglisches_elementarbuch.txt`, line
178: 6031–6033) gives the **only Anglian/Northumbrian** pret. pl.
179: attestation of this verb that I can locate in the handbook tradition:
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:183 (note keyword: Anglian)

- Nearby heading: ### Luick §326

```text
182:    -on` is, on Luick's account, the **same Lautgesetz** as that which
183:    produces `heafod` from `*hēafud`. (Anglian `wērun`, `heafud`,
184:    `wuldur`, `leofuste` confirm the Anglian retention pattern.)
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:184 (note keyword: Anglian)

- Nearby heading: ### Luick §326

```text
183:    produces `heafod` from `*hēafud`. (Anglian `wērun`, `heafud`,
184:    `wuldur`, `leofuste` confirm the Anglian retention pattern.)
185: 
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:358 (note keyword: Anglian)

- Nearby heading: ## Chronology

```text
357: 
358: The dialect distribution is clear: Mercian (Anglian) preserves `-un`
359: robustly into the 10th c.; West Saxon shifts to `-on` by the early 9th
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:28 (note keyword: Anglian)

- Nearby heading: ## §1. TL;DR

```text
27:    outcomes from PGmc *widuwōn- are:
28:    * **Anglian:** `widwe` (regular early syncope of medial `*u`).
29:    * **West Saxon:** `wuduwe` (combinative u-umlaut / "verstärkter
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:130 (note keyword: Anglian)

- Nearby heading: #### §114b — explicit "widuwe is analogical"

```text
129: 
130: Translation: "Anglian **widwe** (L, Rit., R², Vesp. Ps.) beside WS
131: **wuduwe** 'widow' is to be explained by early syncope. By analogical
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:138 (note keyword: Anglian)

- Nearby heading: #### §114b — explicit "widuwe is analogical"

```text
137: **analogical / leveled** forms, not as direct Lautgesetz reflexes.
138: The two Lautgesetz outcomes are: Anglian `widwe` (with syncope) and
139: WS `wuduwe` (with combinative u-umlaut of root `wi → wu` and medial
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| thistle | þistel | inh | template:inh | thistle |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:19 (concept name)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
17: - [Preconsonantal *x Loss: *xs > *s](#preconsonantal-x-loss-xs--s-before-consonant-clusters)
18: - [PGmc *d/*ð Representation Decision](#decision-2026-03-11-option-2a-confirmed)
19: - [OE þistel 'thistle': Scholarly Controversy](#oe-þistel-thistle-i-umlaut-not-preserved-2026-03-18)
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
```

#### Germanic/docs/DEV_NOTES.md:10393 (concept name)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10391: | 2026-03-14 16:17 | 70 | -2 | 223ad24 | Verner TSV fixes: lade, needle |
10392: | 2026-03-14 20:34 | 65 | -5 | 62fced4 | Participle nasalization fix (funden) |
10393: | 2026-03-19 | 57 | -8 | — | Multiple TSV/FST fixes (huniġ, thistle, etc.) |
10394: | 2026-04-05 | 55 | -2 | — | span fix (feminine ō-stem dat.sg.) |
10395: | 2026-04-06 | 52 | -3 | — | TSV fixes: dile, lappa, cnobba |
```

#### Germanic/docs/DEV_NOTES.md:12181 (concept name)

- Nearby heading: ## OE þistel 'thistle': I-Umlaut Not Preserved (2026-03-18)

```text
12179: ---
12180: 
12181: ## OE þistel 'thistle': I-Umlaut Not Preserved (2026-03-18)
12182: 
12183: ### The Problem
```

#### Germanic/docs/DEV_NOTES.md:12240 (concept name)

- Nearby heading: ### Resolution: TSV Updated Despite Scholarly Controversy

```text
12238: **The Problem:**
12239: 
12240: The etymology of Germanic "thistle" is genuinely contested, with scholars disagreeing not just about the root vowel but about the underlying Indo-European etymology itself.
12241: 
12242: **Scholarly sources consulted:**
```

#### Germanic/docs/DEV_NOTES.md:12245 (concept name)

- Nearby heading: ### Resolution: TSV Updated Despite Scholarly Controversy

```text
12243: 
12244: **Orel (2003), p. 419:**
12245: > "*þe(x)stilaz sb.m.: ON þistill 'thistle', OE äistel id., EFris dìssel id., OS thistil id., OHG distil id. (also fem. distila). **Derivationally identical with Lat textilis 'woven'. Further related to *þexsanan.** T-F 184; H AEEW 366; WH II 678–679; **P I 1016 (to IE *steig- 'to prick')**; F 1065; V ANEW 611; Z II 176; O 918; K-S 185."
12246: 
12247: Orel reconstructs `*þe(x)stilaz` with root `*e` (the `(x)` indicates uncertainty about a medial laryngeal/velar). Critically, Orel gives **two competing etymologies**:
```

#### Germanic/docs/DEV_NOTES.md:12259 (concept name)

- Nearby heading: ### Resolution: TSV Updated Despite Scholarly Controversy

```text
12257: > "*þexsanan str.vb.: MHG dehsan 'to swingle (flax)' (str. pret.). Related to Hitt tak"- 'to tie, to join', Toch B tàks- 'to chop up, to grind up', Skt tákšati 'to fashion, to create, to do carpentry', Av ta"- 'to cut (out)', **Lat texò 'to weave'**, Lith ta"aU, ta"ÿti 'to chop off, to do carpentry', Slav *tesati 'to hew'."
12258: 
12259: If thistle is related to `*þexsanan` via IE *tek̂s-, the root vowel `*e` is original.
12260: 
12261: **The Two Competing IE Etymologies:**
```

#### Germanic/docs/DEV_NOTES.md:12322 (row ID)

- Nearby heading: ### Resolution: TSV Updated Despite Scholarly Controversy

```text
12320: ```
12321: 
12322: **TSV UPDATED (2026-03-18):** Changed PROTOFORM from `*θestilăz` to `*θistilăz` (row 2250). The scholarly controversy remains unresolved, but since all daughter languages show `*i` and the FST correctly produces `þistel` from `*θistilăz`, we adopt Kluge-Seebold's reconstruction. Note added to TSV referencing notable_findings §8.
12323: 
12324: **Further research needed:** Specialist literature on the *þe(x)stilaz/*þistilaz controversy. Sources to consult (not in local collection):
```

#### Germanic/docs/DEV_NOTES.md:30125 (exact pair)

- Nearby heading: #### §17.18.7.2  Implementation steps

```text
30123: 
30124: 4. **Verify** (post-rebuild):
30125:    - `*θístilas → þistles` ✓ (new target match)
30126:    - `*θístilaz → þistl` (unchanged; still derivable as the
30127:      unbroken-NomSg variant, but no longer the active TSV target)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:13 (note keyword: Anglian)

- Nearby heading: # Mismatch Dossier: *mízdō 'reward, wage'

```text
12: >   Reader (in a poetic line, glossed as "(dial.)"), and Hall's Concise Dictionary.
13: >   It is a dialectal (Anglian-leaning) variant of WS *mēd*.
14: >
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:69 (note keyword: Anglian)

- Nearby heading: ### 2.1 Standard dictionary lemmata

```text
68: - Lemma: **mēd** (primary)
69: - Variant: **meord** (marked as early/Anglian, rare in simplex but preserved in compounds)
70: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:89 (note keyword: Anglian)

- Nearby heading: #### Form B: `meord` (diphthong eo, with medial /r/)

```text
88: 1. **Early glossaries** (7th–8th century):
89:    - **Épinal-Erfurt Glossary** (ca. 700, Mercian/Anglian base): no direct attestation of the simplex found, but compound forms suggest *meord-*
90:    - **Corpus Glossary** (ca. 800, Mercian): potential attestation (requires verification)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:22 (note keyword: Anglian)

- Nearby heading: # Supplement to Mismatch Dossier: *mízdō 'reward, wage'

```text
21: > **withdrawn**. Kroonen's "(dialectally dependent?) doublet *méd : meord*"
22: > (EDPG p. 376) reflects genuine primary attestation in Anglian-leaning sources.
23: > The handbook agreement reflects shared evidence, not lexicographic recycling.
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:524 (note keyword: Anglian)

- Nearby heading: ### 5.1 The *rēc case (notable_findings.md #10)

```text
523: - **Attested outcome**: **rēc** (long ē monophthong, **no diphthong**)
524: - **Distribution**: **Universal across all OE dialects** (Anglian, WS, Kentish, Northumbrian)
525: 
```

#### Germanic/docs/analysis/notable_findings.md:17 (concept name)

- Nearby heading: ## Table of Contents

```text
16: 7. [NWGmc \*i > \*e lowering: consonant-conditioned blocking and rule ordering](#7-nwgmc-i--e-lowering-consonant-conditioned-blocking-and-rule-ordering)
17: 8. [PGmc \*þistilaz 'thistle': unresolved \*e/\*i reconstruction problem](#8-pgmc-þistilaz-thistle-unresolved-ei-reconstruction-problem)
18: 9. [OE wīþiġ 'withy': ja-stem vs. -ig suffix problem](#9-oe-wīþiġ-withy-ja-stem-vs--ig-suffix-problem)
```

#### Germanic/docs/analysis/notable_findings.md:1222 (concept name)

- Nearby heading: ## 8. PGmc \*þistilaz 'thistle': unresolved \*e/\*i reconstruction problem

```text
1221: 
1222: ## 8. PGmc \*þistilaz 'thistle': unresolved \*e/\*i reconstruction problem
1223: 
```

#### Germanic/docs/analysis/notable_findings.md:1228 (concept name)

- Nearby heading: ## 8. PGmc \*þistilaz 'thistle': unresolved \*e/\*i reconstruction problem

```text
1227: 
1228: All Germanic daughter languages attest 'thistle' with root vowel \*i:
1229: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |
| Orel2003 | single available key for Orel |
| Seebold1970 | single available key for Seebold |
| KlugeSeebold2011 | single available key for Kluge |
| Kilday2024 | single available key for Kilday |

### Low-confidence candidates

_None_

## Paradigm probe

### Paradigm probe — thistle / þistles

- PROTO: *θéstilaz
- PROTOFORM: *θístilas
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for citation nom.sg. vs. selected gen.sg. cell.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen.sg.
- Omitted cells: Alternative *i-root nominative and other oblique cells omitted in v1; they should be added once the raising/epenthesis question is formalized.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *θéstilaz | þistl | no | Citation proto used for comparison. |
| gen.sg. | *θístilas | þistles | yes | Chosen genitive singular cell in TSV. |

