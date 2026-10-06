# Evidence packet — 2046 grave / grafan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2046 | grave | grafan | *grábaną | *grábaną | regular | OE target: græf→græfan (inf. of str.v. class VI 'to dig, grave') \| OE target: grafan (not græfan); Hogg §5.3.1, Hall s.v. grafan. Proto encoding: -aną for A-restoration; R/T §6.3.1 | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# grave
PROTO: *grábaną
EXPECTED: grafan
OUTPUTS: grafan



### Proto-Germanic consonant inheritance

Proto Input: *grábaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>Anglo Frisian Brightening: *græbaną<br>OE A Restoration: *grabaną<br>OE Heavy Syllable Nasal Apocope: *graban<br>OE Secondary Nasalization: *grabąn<br>PGmc B Allophony: *graβąn<br>OE Weak Tail Reduction: *graβan |



### Orthography & surface

Outcome: grafan

NOTE: OE target: græf→græfan (inf. of str.v. class VI 'to dig, grave') | OE target: grafan (not græfan); Hogg §5.3.1, Hall s.v. grafan. Proto encoding: -aną for A-restoration; R/T §6.3.1
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:30620 (exact pair)

- Nearby heading: ##### Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail

```text
30618: | 2025 | *fálθaną | fealdan | breaking |
30619: | 2030 | *fúglaz | fugol | *u*-vowel, not A-restoration; handled by `OEGLInsertion` (germanic.txt) |
30620: | 2046 | *grábaną | grafan | single *b*, A-restoration fires correctly |
30621: | 2050 | *xáglą | hæġl | *Cl* word-final NomSg, no back-vowel trigger; *æ* expected (cf. Campbell §158: *hægl ~ hagol* doublet — TSV chose the *NomSg* unbroken/*æ*-form) |
30622: | 2052 | *xállō | heall | geminate *ll* |
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

#### Germanic/docs/DEV_NOTES.md:3151 (exact COUNTERPART)

- Nearby heading: ### Impact

```text
3149: ### Impact
3150: - No regressions. 106 mismatches (unchanged). Health check clean.
3151: - All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct.
3152: 
3153: ---
```

#### Germanic/docs/DEV_NOTES.md:9501 (exact COUNTERPART)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9499: 2. TSV: Changed 5 OE strong verb infinitives from `-aną` to `-ăną`:
9500:    - `*bakaną` → `*bakăną` (bacan)
9501:    - `*grabaną` → `*grabăną` (grafan)  
9502:    - `*wadaną` → `*wadăną` (wadan)
9503:    - `*wakaną` → `*wakăną` (wacan)
```

#### Germanic/docs/DEV_NOTES.md:9509 (exact COUNTERPART)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9507: ```
9508: bakăną → bacan ✓ (was bacen)
9509: grabăną → grafan ✓ (was græfen)
9510: wadăną → wadan ✓ (was wæden)
9511: wakăną → wacan ✓ (was wæcen)
```

#### Germanic/docs/DEV_NOTES.md:10089 (exact COUNTERPART)

- Nearby heading: #### Results

```text
10087: Fixed forms (strong verb infinitives):
10088: - `*bakaną` → `bacan` ✓ (was `bacen`)
10089: - `*grafaną` → `grafan` ✓ (was `græfen`) 
10090: - `*wadaną` → `wadan` ✓ (was `wæden`)
10091: - `*wakaną` → `wacan` ✓ (was `wæcen`)
```

#### Germanic/docs/DEV_NOTES.md:10205 (exact COUNTERPART)

- Nearby heading: ### Why This Wasn't Caught Earlier

```text
10203: 
10204: The nasalization fix (commit 18b921e) was tested on **infinitives** (which worked
10205: correctly: `bacan`, `grafan`, `wadan`, etc.). The bug only affects **participles**,
10206: which have a different suffix structure. The `*funðanăz → funden` entry was added
10207: to the TSV as a Verner's Law fix, and only then did we notice the `-en` → `-an`
```

#### Germanic/docs/DEV_NOTES.md:22575 (exact COUNTERPART)

- Nearby heading: #### Case 1 — `*táppan → tappan` (expected `tæppan`)

```text
22573: Campbell §158 (lines 4733–4737):
22574: > "The restoration of a is common before all single consonants and geminates,
22575: > e.g. faran, calan, bacan, gnagan, grafan, stapol, sadol, latost, lapode,
22576: > cassoc, hassuc, mattoc, **crabba, hnappian, racca, lappa**."
22577: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:1 (note keyword: A-restoration)

- Nearby heading: # A-Restoration in Old English: the role of intervening *r and *l

```text
1: # A-Restoration in Old English: the role of intervening *r and *l
2: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:81 (exact COUNTERPART)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959) — file `campbell_old_english_grammar.txt`

```text
80: 
81: > § 158. The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig, *stapol* pillar, *sadol* saddle, *latost* latest, *lapode* he invited, *cassoc* rough grass, *hassuc* the same, *mattoc* mattock, *hnappian* fall asleep, *racca* cord, *lappa* skirt.
82: >
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:210 (exact COUNTERPART)

- Nearby heading: ### 2.5 Luick, *Historische Grammatik der englischen Sprache* — file `luick_historische_grammatik.txt`

```text
209: >
210: > 1. am deutlichsten in offener Silbe: *hara* Hase, *faran* fahren, *farað* sie fahren, *talu* Erzählung, *apa* Affe, *sacu* Sache, *nacod* nackt, *macian* machen, *wadan* waten, *sadol* Sattel, *gad(e)rian* sammeln, *grafan* graben, *hraðor* schneller, *staðol* Stütze, *staðelian* befestigen, *magu* Knabe, *dagas, -a, -um* plur. zu *dæg* Tag, *fatu, -a, -um* plur. zu *fæt* Faß usw.;
211: >
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

#### Germanic/docs/analysis/compound_archaism_inventory.md:190 (note keyword: A-restoration)

- Nearby heading: ### Case 8: *rastō (rest) — ræst / ræste

```text
189: | **Sound changes** | AFB (A-restoration trigger = back vowel in suffix *-u*; fires in nom.sg., blocked in obliques with front *-æ*, *-e*) |
190: | **Lautgesetzlich output** | `rast` (nom.sg., from A-restoration + apocope) BUT oblique cells show `ræste` (front *æ* from AFB, no restoration) |
191: | **Attested simplex** | `ræst` (standard headword, showing paradigmatic leveling of oblique *-æ-* back to nom.sg.) |
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

#### Germanic/docs/analysis/notable_findings.md:754 (exact COUNTERPART)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
753: Silbe" ('PGmc *a = OE a in open syllable before a dark vowel of the
754: following syllable'). His examples (dagas, fatu, gladu, faran, grafan)
755: all have back suffixal vowels. But Kaluza adds a critical observation in
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
| grave | græf | inh | template:inh | grave |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:3202 (concept name)

- Nearby heading: ### Case 1: *rastō → rast (expected ræst) — ō-stem feminine

```text
3200: 
3201: **Sources:**
3202: - BT: headword "ræst" f. 'rest, repose, bed, grave'. Oblique forms: ræste (gen./dat.sg.).
3203: - Kroonen (p.420): *rasto- f. 'interval' — Go. rasta, ON rost, OE rest, OS rasta, OHG rasta. (Kroonen gives OE "rest", i.e. ræst with late OE æ→e.)
3204: - R/T §6.3.1–6.3.2: paradigmatic alternation between a and æ due to A-restoration is explicitly discussed for a-stems (dæg/dagas); same logic applies to ō-stems.
```

#### Germanic/docs/DEV_NOTES.md:9538 (concept name)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9536: **Mismatch count:** 78 → 79 (net +1 WORSE)
9537: 
9538: - **Fixed: 6** (bake, grave, wade, wake, wash, will)
9539: - **Regressed: 9** (craft, day, mast, raven, staff, tap, wain, lap, wasp)
9540: 
```

#### Germanic/docs/DEV_NOTES.md:20622 (concept name)

- Nearby heading: ### §16.4 Not yet adopted: grave for secondary stress

```text
20620: referenced in FST rules.
20621: 
20622: ### §16.4 Not yet adopted: grave for secondary stress
20623: 
20624: A future extension could use grave accent (`à è ì ò ù`) for secondary-stressed
```

#### Germanic/docs/DEV_NOTES.md:20624 (concept name)

- Nearby heading: ### §16.4 Not yet adopted: grave for secondary stress

```text
20622: ### §16.4 Not yet adopted: grave for secondary stress
20623: 
20624: A future extension could use grave accent (`à è ì ò ù`) for secondary-stressed
20625: vowels in compound second elements (e.g. `*wérd-àldu`). This would support:
20626: - Inter-stress `*a → *u` raising (between primary and secondary stress peaks)
```

#### Germanic/docs/DEV_NOTES.md:27486 (concept name)

- Nearby heading: ## §16.6 Grave-accent notation for secondary stress — three-agent

```text
27484: 
27485: ───────────────────────────────────────────────────────────────
27486: ## §16.6 Grave-accent notation for secondary stress — three-agent
27487: ## research audit (2026-04)
27488: 
```

#### Germanic/docs/DEV_NOTES.md:27489 (concept name)

- Nearby heading: ## research audit (2026-04)

```text
27487: ## research audit (2026-04)
27488: 
27489: §16.4 ("Not yet adopted: grave for secondary stress") is
27490: re-opened. Following the workflow now documented in
27491: `WORKFLOW.md` ("Default Research Practice: Three-Agent Source
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| Kaluza1906 | single available key for Kaluza |

### Low-confidence candidates

_None_

