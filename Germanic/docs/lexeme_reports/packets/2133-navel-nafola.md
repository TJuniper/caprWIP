# Evidence packet — 2133 navel / nafola

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2133 | navel | nafola | *nablô | *nábulô | early_analogy | PROTOFORM updated 17.19→17.19.10: Kroonen 2013:380 lemmatises *nablan- (Latinate syncopated headword) but cites OHG nabalo/nabulo as cognates; R/T 2014:191, 270 give canonical pre-retraction *nabulō > *nǣbula > nafola with medial *u present at A-restoration. Medial *u origin contested (PIE *l̥ → *ul per Streitberg §81 / Ringe vol.1:126; or Sekundärvokal per EWA, Brunner §152, Schatz §98) but universally agreed present by PNWGmc. PROTO column retains Kroonen citation form *nablô; PROTOFORM uses R/T pre-syncope *nábulô as FST input. See DEV_NOTES §17.19 + §17.19.10 for full survey. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# navel
PROTO: *nábulô
EXPECTED: nafola
OUTPUTS: nafola



### Proto-Germanic consonant inheritance

Proto Input: *nábulô

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Med Unstressed U Lowering: *nábolô<br>Anglo Frisian Brightening: *næbolô<br>OE A Restoration: *nabolô<br>PGmc B Allophony: *naβolô<br>OE Unstressed Long Vowel Shortening: *naβola |



### Orthography & surface

Outcome: nafola

NOTE: PROTOFORM updated 17.19→17.19.10: Kroonen 2013:380 lemmatises *nablan- (Latinate syncopated headword) but cites OHG nabalo/nabulo as cognates; R/T 2014:191, 270 give canonical pre-retraction *nabulō > *nǣbula > nafola with medial *u present at A-restoration. Medial *u origin contested (PIE *l̥ → *ul per Streitberg §81 / Ringe vol.1:126; or Sekundärvokal per EWA, Brunner §152, Schatz §98) but universally agreed present by PNWGmc. PROTO column retains Kroonen citation form *nablô; PROTOFORM uses R/T pre-syncope *nábulô as FST input. See DEV_NOTES §17.19 + §17.19.10 for full survey.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:30687 (row ID)

- Nearby heading: ##### Survey conclusion

```text
30685: 
30686: Across the TSV, **the only row of the exact *V-aCl-V*-with-back-tail
30687: shape is row 2133 itself**. Other apparent *aCl/aCr* matches are either
30688: breaking environments (root-final *Cl/Cr* → diphthong, by §6.2.2), or
30689: NomSg cluster-final (no trigger), or geminate, or sC (already licensed).
```

#### Germanic/docs/DEV_NOTES.md:30690 (row ID)

- Nearby heading: ##### Survey conclusion

```text
30688: breaking environments (root-final *Cl/Cr* → diphthong, by §6.2.2), or
30689: NomSg cluster-final (no trigger), or geminate, or sC (already licensed).
30690: A surgical fix for row 2133 will not have unintended ripple effects on
30691: the rest of the dataset.
30692: 
```

#### Germanic/docs/DEV_NOTES.md:30802 (row ID)

- Nearby heading: ##### Recommended option: **Option A**

```text
30800: user instruction):**
30801: 
30802: 1. `Germanic/data/germanic-aligned-final.tsv` row 2133:
30803:    - PROTOFORM: `*náblô` → `*nábulô`
30804:    - PROTO: keep `*nablô` (Kroonen-style cross-Germanic root)
```

#### Germanic/docs/DEV_NOTES.md:30826 (exact pair)

- Nearby heading: ##### Recommended option: **Option A**

```text
30824: 3. Rebuild bins (`bash Germanic/tools/rebuild_oe_bins.sh`).
30825: 
30826: 4. Verify: `*nábulô → nafola` (correct); spot-check that `*náblô`
30827:    alone still parses (it should, since the bare `ô:{*ô}` shape at
30828:    line 407 plus the `b:{*b} l:{*l}` complex coda at line 166 still
```

#### Germanic/docs/DEV_NOTES.md:30974 (exact PROTOFORM)

- Nearby heading: ### §17.19.10  Origin and chronology of the medial *u in *nabulō: a survey of the literature

```text
30972: 
30973: This appendix sits underneath §17.19.5 (which adopted Option A:
30974: PROTOFORM `*nábulô`). §17.19.5 established that R/T's derivation
30975: **PNWGmc \*nabulō > \*næbula > OE nafola** (R/T 2014: 191, 270; ref
30976: lines 11090, 15573) requires a medial *u in the FST input, and that
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:140 (row ID)

- Nearby heading: ### Case 5: *nábulō (navel) — nafola / nafela

```text
139: | **Methodological use** | The TSV targets `nafola` (nom.sg., early form). The decision illustrates that when vowel-harmony changes occur *within* OE (rather than as inherited pre-OE changes), targeting the earlier stage may be appropriate if it represents the lautgesetzlich pathway before analogical smoothing. Parallel to the "vowel-harmony reduction" precedents in §17.10–17.13 (breve elimination research). |
140: | **Implementation** | Row 2133 targets `nafola`. The FST correctly produces it from `*nabulō` via vowel harmony. |
141: 
```

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

#### Germanic/docs/DEV_NOTES.md:30158 (exact COUNTERPART)

- Nearby heading: ### §17.19  PGmc 'navel' (*nablô / *nabulō → OE *nafola*) — proto-form choice and the *Cl A-restoration question

```text
30156: research and rule sketch are preserved in §17.18.4.
30157: 
30158: ### §17.19  PGmc 'navel' (*nablô / *nabulō → OE *nafola*) — proto-form choice and the *Cl A-restoration question
30159: 
30160: **Date**: this session.
```

#### Germanic/docs/DEV_NOTES.md:30178 (exact COUNTERPART)

- Nearby heading: ### §17.19  PGmc 'navel' (*nablô / *nabulō → OE *nafola*) — proto-form choice and the *Cl A-restoration question

```text
30176: described as a heuristic, not a deeply-motivated boundary. The present
30177: section investigates whether that exclusion is empirically correct and what
30178: the right philological encoding for *nafola* is.
30179: 
30180: ---
```

#### Germanic/docs/DEV_NOTES.md:30239 (exact COUNTERPART)

- Nearby heading: ###### (a) §6.3.1 (printed p. 205–206) — General retraction of *æ

```text
30237: 
30238: > PNWGmc ***nabulō*** 'navel' (ON *nafli*, OHG *nabalo*) > ***næbula***
30239: > > OE ***nafola*** (OF *navla*).
30240: 
30241: The same exemplar list also has *nakud > nacod*, *habukaz > hafoc*,
```

#### Germanic/docs/DEV_NOTES.md:30253 (exact COUNTERPART)

- Nearby heading: ###### (b) §6.7.x (printed p. 270; ref. txt line 15573) — repeated citation

```text
30251: 
30252: > PNWGmc ***nabulō*** 'navel' (ON *nafli*) > PWGmc ***nabulō*** (OF
30253: > *navila*, OHG *nabalo*) > ***næbula*** > OE ***nafola***.
30254: 
30255: R/T's index (lines 32174 / 33394) lists the form on pp. 191, 270, 336.
```

#### Germanic/docs/DEV_NOTES.md:30726 (exact PROTOFORM)

- Nearby heading: ##### Option A — Change TSV PROTOFORM to *nabulô* (R/T-style pre-syncope reconstruction)

```text
30724:   `u:{*u} l:{*l} ô:{*ô}`. Adding it is a one-line change exactly
30725:   parallel to the existing `i:{*i} l:{*l} ō:{*ō}` shape.
30726: - A *very small* TSV edit: PROTOFORM `*náblô` → `*nábulô`; TOKENS
30727:   remain `n a f o l a`; the cognate root `*nablô` can be retained in
30728:   the PROTO field for cross-Germanic alignment if desired (parallel to
```

#### Germanic/docs/DEV_NOTES.md:30803 (exact PROTOFORM)

- Nearby heading: ##### Recommended option: **Option A**

```text
30801: 
30802: 1. `Germanic/data/germanic-aligned-final.tsv` row 2133:
30803:    - PROTOFORM: `*náblô` → `*nábulô`
30804:    - PROTO: keep `*nablô` (Kroonen-style cross-Germanic root)
30805:      **OR** update to `*nabulô` for internal consistency — see how
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:22 (exact COUNTERPART)

- Nearby heading: ## 1. Executive summary

```text
21: 
22: 2. **The hypothesis is correct.** Across the entire local reference corpus (Campbell, Hogg/CHEL, Ringe & Taylor vol. 2, Brunner, Luick, Bülbring, Kaluza, Kroonen, Orel) **no source treats a single intervening *r* or *l* as blocking A-restoration**. On the contrary, every source that supplies derivations of `sparian`, `warian`, `farian`, `talian`, `carian`, `lapian`, `bapian`, `nacod`, `nafola`, `sadol`, `stapol`, `magu`, `lagu`, `mapa`, `racca`, `crabba`, `flasce`, `mara`, `hara`, `apa`, `maga`, `naca`, `scapa`, `draca`, `cnafa`, `gegada`, `manslaga` etc. derives the surface *a* by exactly the sound-change A-restoration applying across single intervening *r*, *l*, *m*, *n*, *p*, *b*, *d*, *t*, *g*, *f*, *þ*, *s*, *k*, *w*. Liquids are not singled out as a blocking class.
23: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:151 (exact COUNTERPART)

- Nearby heading: ### 2.2 Ringe & Taylor (2014), *A Linguistic History of English vol. II* — file `ringe_taylor_linguistic_history_vol2.txt`

```text
150: 
151: > *nabulē > *næbula > OE **nafola**;
152: > *habukaz > *hæbuk > OE **hafoc**;
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:160 (exact COUNTERPART)

- Nearby heading: ### 2.2 Ringe & Taylor (2014), *A Linguistic History of English vol. II* — file `ringe_taylor_linguistic_history_vol2.txt`

```text
159: 
160: Note the consistent presence of *r*, *l* in many of these derivations (`nabula`, `gabula`, `staþul`, `sadul`, `nafola`, `gafol`) and the exceptionless retraction. R/T does not anywhere identify *r*/*l* as a blocker.
161: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:64 (exact COUNTERPART)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
63: | **Methodological use** | A textbook case of dialectal-doublet preservation: WS shows the analogical/innovative outcome (or a different sound-change pathway), Anglian-leaning sources preserve the form expected from the regular sequence rhotacism + breaking. Parallel to §17.21 (swustor/swester). The TSV target may legitimately be *meord* if we adopt the dialect-relic-targeting pattern. |
64: | **Precedent / parallels** | §17.21 (swustor → swester, Anglian-relic target adopted); §17.20 (nafola, Anglian glossary witness); §17.16 (spere/speoru paradigm cell). Methodologically equivalent to those — but operating on **dialect** rather than **paradigm cell** or **compound** as the preservation locus. |
65: | **Cross-reference to Watkins-principle (compound) cases** | The mizdō case is *not* an instance of the Watkins principle as conventionally stated, because the preservation locus is not a compound. It belongs to the broader umbrella of "archaism preservation" but is methodologically distinct. |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:126 (exact COUNTERPART)

- Nearby heading: ### Case 5: *nábulō (navel) — nafola / nafela

```text
125: 
126: ### Case 5: *nábulō (navel) — nafola / nafela
127: 
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

#### Germanic/docs/analysis/notable_findings.md:698 (exact COUNTERPART)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
697: restoration. Then nominals with *-u- or *-ō-suffixes: *nakwadaz > nacod,
698: *nabulō > nafola, *habukaz > hafoc, *sadulaz > sadol. Then n-stems
699: whose oblique endings contained *-a-/*-ō-: *askōn- > ascan, *maþō >
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:29 (exact COUNTERPART)

- Nearby heading: ## Evidence from R/T §6.9.6

```text
28: - "the first of two unstressed back vowels shows a tendency to be written e"
29: - nafola → nafela, weloras → weleras
30: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:100 (note keyword: A-restoration)

- Nearby heading: ### A-restoration — RULED OUT for unstressed syllables

```text
99: 
100: ### A-restoration — RULED OUT for unstressed syllables
101: 
```

#### Germanic/docs/analysis/unstressed_e_o_before_r.md:126 (exact COUNTERPART)

- Nearby heading: ### The a/o variation in unstressed syllables (R/T §3.1.5, §6.9.6)

```text
125: - "the first of two unstressed back vowels shows a tendency to be written e"
126: - nafola → nafela, weloras → weleras
127: - "it seems likely that the product of this merger was actually [ə]"
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

#### Germanic/docs/dossiers/un-to-on-chronology.md:170 (exact COUNTERPART)

- Nearby heading: ### Luick §326

```text
169: > Konsonanten) bewahrend**. So: (urg. u) nacod, hēafod, heofon, hamor,
170: > **ridon, wǣron**, h(e)afoc, nafola, afora; (u nach §317) sāwol,
171: > wundor, tungol; (u nach §312) huntoð, geogoð, locod, locode, leofost,
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1747 (exact COUNTERPART)

- Nearby heading: ### D.1 Open vs. closed syllable conditioning

```text
1746: > Konsonanten) bewahrend**. So: … nacod, hēafod, heofon, hamor, ridon,
1747: > wǣron, hafoc, nafola, afora; sāwol, wundor, tungol; huntoð, geogoð,
1748: > locod, locode, leofost, leofosta; **aber munuc 'Mönch', duguð
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| navel | nafola | inh | template:inh | navel |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2997 (concept name)

- Nearby heading: ### Proto-form notes

```text
2995: ### Proto-form notes
2996: 
2997: **`*nablô` (navel):** Competing reconstructions. Kroonen reconstructs PGmc *nablōn- (stem *nablan-), but R/T vol.2 §6.3.1 p.206 gives pre-retraction *nabulō with medial vowel (cf. OHG nabalo). The medial *u may be PWGmc-level epenthesis. Current TSV form *nablô follows Kroonen. For A-restoration to fire correctly in the pipeline, *nabulô may be needed, since R/T's chronology places epenthesis (§6.9.5, mid-7th c.) much later than retraction (§6.3, pre-6th c.).
2998: 
2999: ---
```

#### Germanic/docs/DEV_NOTES.md:10416 (exact pair)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10414: | 2026-04-24 | 30 | -1 | 75b8da0d | speoru: short-diphthong weight refactor; *spéru NApl (§17.17) |
10415: | 2026-04-25 | 29 | -1 | 9ccbe617 | þistles: paradigm-cell switch *þístilaz → GenSg (§17.18) |
10416: | 2026-04-25 | 28 | -1 | d5d8acc1 | nafola: PROTOFORM *náblô → *nábulô (R/T pre-syncope, §17.19) |
10417: | 2026-04-25 | 27 | -1 | 3355ec68 | tang: TSV target tange → tang, early-Anglian NomSg (§17.20) |
10418: | 2026-04-25 | 26 | -1 | 11360b2a | swustor: target switch to Anglian swester (§17.21) |
```

#### Germanic/docs/DEV_NOTES.md:30162 (row ID)

- Nearby heading: ### §17.19  PGmc 'navel' (*nablô / *nabulō → OE *nafola*) — proto-form choice and the *Cl A-restoration question

```text
30160: **Date**: this session.
30161: **Status**: research complete; awaiting Option-selection by user.
30162: **Trigger**: TSV row 2133 mismatch. PROTOFORM `*náblô` (Kroonen) currently
30163: yields FST output `næfla`; expected OE `nafola`. The two errors visible in
30164: the surface form are (a) A-fronting fired but A-restoration did not (so the
```

#### Germanic/docs/DEV_NOTES.md:30163 (exact COUNTERPART)

- Nearby heading: ### §17.19  PGmc 'navel' (*nablô / *nabulō → OE *nafola*) — proto-form choice and the *Cl A-restoration question

```text
30161: **Status**: research complete; awaiting Option-selection by user.
30162: **Trigger**: TSV row 2133 mismatch. PROTOFORM `*náblô` (Kroonen) currently
30163: yields FST output `næfla`; expected OE `nafola`. The two errors visible in
30164: the surface form are (a) A-fronting fired but A-restoration did not (so the
30165: root vowel surfaces as `æ`, not `a`); (b) the medial vowel between *b* and
```

#### Germanic/docs/DEV_NOTES.md:30189 (concept name)

- Nearby heading: ##### Kroonen 2013, *Etymological Dictionary of Proto-Germanic*

```text
30187: edition; reference txt line 22412 of the local copy):
30188: 
30189: > ***nablan-** m. 'navel' — ON *nafli* m. 'id.', Far. *nalvi* m. 'id.',
30190: > Elfd. *navel* m. 'id.', OE *nafela* m. 'navel', E *navel*, OFri.
30191: > *naula* m. 'id.', Du. *navel* c. 'id.', OHG *nabalo, nabulo* m. 'id.',
```

#### Germanic/docs/DEV_NOTES.md:30190 (concept name)

- Nearby heading: ##### Kroonen 2013, *Etymological Dictionary of Proto-Germanic*

```text
30188: 
30189: > ***nablan-** m. 'navel' — ON *nafli* m. 'id.', Far. *nalvi* m. 'id.',
30190: > Elfd. *navel* m. 'id.', OE *nafela* m. 'navel', E *navel*, OFri.
30191: > *naula* m. 'id.', Du. *navel* c. 'id.', OHG *nabalo, nabulo* m. 'id.',
30192: > G *Nabel* m. 'id.' > *h₃nobʰ-l-on-* (IE) — Gr. *omphalós* m.
```

#### Germanic/docs/DEV_NOTES.md:30191 (concept name)

- Nearby heading: ##### Kroonen 2013, *Etymological Dictionary of Proto-Germanic*

```text
30189: > ***nablan-** m. 'navel' — ON *nafli* m. 'id.', Far. *nalvi* m. 'id.',
30190: > Elfd. *navel* m. 'id.', OE *nafela* m. 'navel', E *navel*, OFri.
30191: > *naula* m. 'id.', Du. *navel* c. 'id.', OHG *nabalo, nabulo* m. 'id.',
30192: > G *Nabel* m. 'id.' > *h₃nobʰ-l-on-* (IE) — Gr. *omphalós* m.
30193: > 'navel, shield boss' < *h₃mbʰ-l-* ; Lat. *umbilīcus* m. 'navel,
```

#### Germanic/docs/DEV_NOTES.md:30193 (concept name)

- Nearby heading: ##### Kroonen 2013, *Etymological Dictionary of Proto-Germanic*

```text
30191: > *naula* m. 'id.', Du. *navel* c. 'id.', OHG *nabalo, nabulo* m. 'id.',
30192: > G *Nabel* m. 'id.' > *h₃nobʰ-l-on-* (IE) — Gr. *omphalós* m.
30193: > 'navel, shield boss' < *h₃mbʰ-l-* ; Lat. *umbilīcus* m. 'navel,
30194: > center' < *h₃mbʰ-e/ol-* + *-iko-*; OIr. *imbliu* 'navel' <
30195: > *h₃mbʰ-el-ion-*.
```

#### Germanic/docs/DEV_NOTES.md:31718 (exact PROTOFORM)

- Nearby heading: ##### §17.19.10.6.b *ô vs *ō: the trimoric question

```text
31716: nom.sg.). This is the same convention the FST uses for *gumô,
31717: *hertô, *namô etc. The §17.19.5 recommendation
31718: (`PROTOFORM: *nábulô`) is therefore **internally consistent with
31719: the FST's existing notation**, and **substantively identical** to
31720: R/T's *nabulō (since R/T's *ō here is, in their prose
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:23 (exact COUNTERPART)

- Nearby heading: # Mismatch Dossier: *mízdō 'reward, wage'

```text
22: **Status**: Research dossier only — no TSV or FST changes proposed  
23: **Methodology**: "Longest pathway of lautgesetzlichkeit" per §17.16 (spere), §17.20 (nafola), §17.21 (swustor)
24: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | author + year mention (Kroonen 2013) |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |
| Kaluza1906 | single available key for Kaluza |
| Streitberg1896 | single available key for Streitberg |
| Orel2003 | single available key for Orel |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Ringe2006 | surname mention only: Ringe |
| Ringe2017 | surname mention only: Ringe |
| RingeTaylor2014 | explicit year mention (2014) |
| Ringe1984 | surname mention only: Ringe |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

