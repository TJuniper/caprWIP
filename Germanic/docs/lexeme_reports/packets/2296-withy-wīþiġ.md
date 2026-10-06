# Evidence packet — 2296 withy / wīþiġ

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2296 | withy | wīþiġ | *wáiθiz | *wḯθagą | early_analogy | Campbell §275(7), §376: OE -ig < PGmc *-ag- (cf. *xúnagą → huniġ); see DEV_NOTES §17.10.35 and notable_findings §9. Wiktionary/Kluge *wīþja- cannot derive -ig (heavy ja-stem yields -e/-Ø). | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# withy
PROTO: *wḯθagą
EXPECTED: wīþiġ
OUTPUTS: wīþiġ



### Proto-Germanic consonant inheritance

Proto Input: *wḯθagą

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *wḯθægą<br>OE Heavy Syllable Nasal Apocope: *wḯθæg<br>OE Velar Palatalization: *wḯθæʤ<br>OE Unstressed AE Merger: *wḯθeʤ<br>OE Late Unstressed Ag Suffix: *wḯθiʤ |



### Orthography & surface

Old English Orthography: *wḯþiġ
Outcome: wīþiġ

NOTE: Campbell §275(7), §376: OE -ig < PGmc *-ag- (cf. *xúnagą → huniġ); see DEV_NOTES §17.10.35 and notable_findings §9. Wiktionary/Kluge *wīþja- cannot derive -ig (heavy ja-stem yields -e/-Ø).
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:12489 (row ID)

- Nearby heading: ### The Problem

```text
12487: ### The Problem
12488: 
12489: TSV row 2296:
12490: ```
12491: PROTOFORM: *wīθijăz
```

#### Germanic/docs/DEV_NOTES.md:26205 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26203: **Bucket**: `palatalization_missing` (1 case).
26204: 
26205: **Symptom**: TSV row 2296 has PROTOFORM `*wīθijaz`, COUNTERPART `wīþiġ`,
26206: but the FST emits bare `wīþ` (suffix lost entirely). Probe:
26207: 
```

#### Germanic/docs/DEV_NOTES.md:26348 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26346: **Plan**:
26347: 
26348: 1. Edit row 2296: PROTOFORM `*wīθijaz` → `*wīθagą`,
26349:    TOKENS `w ī θ i j a z` → `w ī θ a g ą`,
26350:    PROTO column likewise updated to `*wīþagą` (the `*wīθijaz`
```

### Analysis and dossier hits

#### Germanic/docs/analysis/notable_findings.md:1318 (row ID)

- Nearby heading: ## 9. OE wīþiġ 'withy': ja-stem vs. -ig suffix problem

```text
1317: 
1318: OE `wīþiġ` 'withy, willow' (TSV row 2296) is reconstructed as a ja-stem:
1319: 
```

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:21 (exact COUNTERPART)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
19: - [OE þistel 'thistle': Scholarly Controversy](#oe-þistel-thistle-i-umlaut-not-preserved-2026-03-18)
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
22: - [OE heofon 'heaven': Back Umlaut and Nasal Dissimilation](#oe-heofon-heaven-back-umlaut-and-medial-syncope-2026-03-20)
23: - [OE lungen 'lung': The *-anjō Suffix Problem](#oe-lungen-lung-the--anjō-suffix-problem-2026-03-21)
```

#### Germanic/docs/DEV_NOTES.md:10260 (exact COUNTERPART)

- Nearby heading: ### Similar Cases to Review

```text
10258: 1. ✓ `lade`: `*xlaθaną` → `*xlaðaną` (FIXED)
10259: 2. `needle`: `*nēθlō` → `*nēdlō` (TO FIX)
10260: 3. `withy`: `*wīθijăz` → expected `wīþiġ` — this has `þ` in OE, so NOT Verner
10261: 
10262: For `withy`, OE `wīþiġ` has voiceless `þ`, matching PGmc `*θ`. The mismatch is
```

#### Germanic/docs/DEV_NOTES.md:10262 (exact COUNTERPART)

- Nearby heading: ### Similar Cases to Review

```text
10260: 3. `withy`: `*wīθijăz` → expected `wīþiġ` — this has `þ` in OE, so NOT Verner
10261: 
10262: For `withy`, OE `wīþiġ` has voiceless `þ`, matching PGmc `*θ`. The mismatch is
10263: something else (probably suffix handling, not Verner).
10264: 
```

#### Germanic/docs/DEV_NOTES.md:10409 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10407: | 2026-04-21 | 37 | -1 | dab140a9 | §17 refactor baseline confirmed post-prosodic-tier merge |
10408: | 2026-04-23 | 36 | -1 | aa241224 | findan: PP target switch → fundene (§17.10.31, Case 4 Path α) |
10409: | 2026-04-23 | 35 | -1 | 5e733bb3 | wīþiġ: PROTOFORM *wīθijaz → *wīθagą (§17.10.35, Campbell -ag- suffix) |
10410: | 2026-04-23 | 34 | -1 | 29f4e924 | hīeġ: OEAwwjResolution *aw(w)+*j → *au+*j (§17.10.36 stages 1–2) |
10411: | 2026-04-24 | 33 | -1 | 0c6ab468 | strīeġan: OEJStrengtheningAfterFrontDiphthong (§17.10.36-q3) |
```

#### Germanic/docs/DEV_NOTES.md:12482 (exact COUNTERPART)

- Nearby heading: ## OE wīþiġ 'withy': ja-stem Adjective vs Sievers' Law Syncope (2026-03-19)

```text
12480: ---
12481: 
12482: ## OE wīþiġ 'withy': ja-stem Adjective vs Sievers' Law Syncope (2026-03-19)
12483: 
12484: **Date:** 2026-03-19
```

#### Germanic/docs/DEV_NOTES.md:12492 (exact COUNTERPART)

- Nearby heading: ### The Problem

```text
12490: ```
12491: PROTOFORM: *wīθijăz
12492: COUNTERPART: wīþiġ
12493: ```
12494: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/fryhtu_investigation.md:226 (exact COUNTERPART)

- Nearby heading: ### The pattern

```text
225: - Before \*n: no clear evidence of syncope before \*n in our data
226: - Before \*j: wīþiġ preserves the vowel
227: - Before \*s: hierfest preserves the vowel
```

#### Germanic/docs/analysis/fryhtu_investigation.md:306 (exact COUNTERPART)

- Nearby heading: ### Test battery (all verified)

```text
305: | skellinăz | sċiellen | sċilling | — (pre-existing mismatch) |
306: | wīθijăz | wīþeġ | wīþiġ | — (pre-existing mismatch) |
307: | xarbistuz | hierfest | hierfest | ✓ (no regression) |
```

#### Germanic/docs/analysis/notable_findings.md:18 (exact COUNTERPART)

- Nearby heading: ## Table of Contents

```text
17: 8. [PGmc \*þistilaz 'thistle': unresolved \*e/\*i reconstruction problem](#8-pgmc-þistilaz-thistle-unresolved-ei-reconstruction-problem)
18: 9. [OE wīþiġ 'withy': ja-stem vs. -ig suffix problem](#9-oe-wīþiġ-withy-ja-stem-vs--ig-suffix-problem)
19: 10. [OE rēc 'smoke': the missing WS rīec problem](#10-oe-rēc-smoke-the-missing-ws-rīec-problem)
```

#### Germanic/docs/analysis/notable_findings.md:1312 (exact COUNTERPART)

- Nearby heading: ## 9. OE wīþiġ 'withy': ja-stem vs. -ig suffix problem

```text
1311: 
1312: ## 9. OE wīþiġ 'withy': ja-stem vs. -ig suffix problem
1313: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| withy | wīþiġ | inh | template:inh | withy |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:12557 (concept name)

- Nearby heading: ### The Distinction

```text
12555: The question is: when did ja-stem `-ij-` survive vs. when was it leveled?
12556: 
12557: For OE `wīþiġ` 'withy':
12558: - Proto: `*wīþijaz` (ja-stem masc. nom.sg.)
12559: - The `-ij-` represents the ja-stem thematic suffix
```

#### Germanic/docs/DEV_NOTES.md:12623 (concept name)

- Nearby heading: #### Primary Etymological Sources

```text
12621: 
12622: **Orel (*lukkaz)** (p. 534):
12623: > "Related to IE *leug- 'to bend', cf. Gk λύγος 'withy; screw-press', Lith. lùgnas 'supple, flexible'."
12624: 
12625: This confirms 'withy' refers to flexible willow branches for plaiting.
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| KlugeSeebold2011 | single available key for Kluge |

### Low-confidence candidates

_None_

