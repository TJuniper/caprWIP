# Evidence packet — 2216 stem / stefn

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2216 | stem | stefn | *stámnaz | *stébnō | early_analogy | Pre-OE transponent *stebn- (citation form *stebnō per R/T p.330) > OE stefn. The form stemn is a later WS variant (fn > mn assimilation, Bülbring §445: 'erst in Alfreds Zeit'). The deeper PGmc reconstruction remains disputed (see DEV_NOTES); this entry uses the local pre-OE transponent and defers cross-branch analysis. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# stem
PROTO: *stébnō
EXPECTED: stefn
OUTPUTS: stefn



### Proto-Germanic consonant inheritance

Proto Input: *stébnō

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Final Long O Raising: *stébnu | **Old English**<br>PGmc B Allophony: *stéβnu<br>OE High Vowel Apocope: *stéβn |



### Orthography & surface

Outcome: stefn

NOTE: Pre-OE transponent *stebn- (citation form *stebnō per R/T p.330) > OE stefn. The form stemn is a later WS variant (fn > mn assimilation, Bülbring §445: 'erst in Alfreds Zeit'). The deeper PGmc reconstruction remains disputed (see DEV_NOTES); this entry uses the local pre-OE transponent and defers cross-branch analysis.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:29897 (exact pair)

- Nearby heading: #### §17.18.2  Current TSV state (11 candidate words)

```text
29895: | 7 | \*xrábnaz | hræfn | hræfn | ✓ |
29896: | 8 | \*skúflō | sċofl | sċofl | ✓ |
29897: | 9 | \*stébnō | stefn | stefn | ✓ |
29898: | 10 | \*táikną | tācn | tācn | ✓ |
29899: | 11 | \*wēpną | wǣpn | wǣpn | ✓ |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:49 (exact COUNTERPART)

- Nearby heading: ### Polished analyses (Feb–Mar 2026)

```text
47: - [Water fix: PWGmc ō-shortening](#water-fix-pwgmc-ō-shortening-and-a-restoration-correction-3a45a8b)
48: - [A-restoration: ræst, tæppa, stemn](#a-restoration-in-ō-stems-and-n-stems-ræst-tæppa-stemn-fronting_missing__afb)
49: - [The stefn/stemn Problem](#the-stefnstemn-problem-local-transponent-decision)
50: - [z-loss/rhotacism and bimoraic/trimoraic cross-source analysis](#historical-phonology-of-final--z-loss-and-its-interaction-with-rhotacism)
51: - [Stiles 1985-6 on 'four'](#stiles-1985-6-on-the-numeral-four-research-summary-2026-04-10)
```

#### Germanic/docs/DEV_NOTES.md:1483 (exact COUNTERPART)

- Nearby heading: ## Project Status (as of 2026-03-10)

```text
1481: **Key recent achievements (Feb–Mar 2026):**
1482: - Bimoraic vs. trimoraic *ō analysis completed and verified against Bülbring, Luick, R/T, Hogg
1483: - stefn/stemn dossier: pre-OE transponent *stebn- adopted, full scholarly review filed
1484: - z-loss/rhotacism chronology documented; exceptionlessness concern resolved
1485: - Campbell OEG OCR'd and integrated; EWA Band I extracted
```

#### Germanic/docs/DEV_NOTES.md:3254 (exact COUNTERPART)

- Nearby heading: ### Case 3: stefn / stemn 'voice' — the stefn/stemn problem

```text
3252: *tappăn → (AFB: root *a → *æ, suffix *ă → ... treated as front) → *tæppæn → (various) → tæppan ✓
3253: 
3254: ### Case 3: stefn / stemn 'voice' — the stefn/stemn problem
3255: 
3256: **⚠ THIS IS A MAJOR FLAGGED PROBLEM — see also notable_findings.md §5 and the "Return later" section below.**
```

#### Germanic/docs/DEV_NOTES.md:3264 (exact COUNTERPART)

- Nearby heading: #### A. Practical project decision

```text
3262: #### A. Practical project decision
3263: 
3264: **Operational decision (implemented):** The TSV uses pre-OE transponent **\*stebnō** (citation form, ō-stem nom.sg.) as input to the OE pipeline. Pipeline output: **stefn**. The OE target is **stefn**, not stemn.
3265: 
3266: The form **stemn** is treated as a later secondary WS variant produced by the assimilation fn → mn (Bülbring §485: "Im Ws. geht f vor n + Vokal in m über"; he dates the assimilation to Alfred's time or later). The OE target stefn is the conservative form attested from the earliest glossaries onward.
```

#### Germanic/docs/DEV_NOTES.md:3266 (exact COUNTERPART)

- Nearby heading: #### A. Practical project decision

```text
3264: **Operational decision (implemented):** The TSV uses pre-OE transponent **\*stebnō** (citation form, ō-stem nom.sg.) as input to the OE pipeline. Pipeline output: **stefn**. The OE target is **stefn**, not stemn.
3265: 
3266: The form **stemn** is treated as a later secondary WS variant produced by the assimilation fn → mn (Bülbring §485: "Im Ws. geht f vor n + Vokal in m über"; he dates the assimilation to Alfred's time or later). The OE target stefn is the conservative form attested from the earliest glossaries onward.
3267: 
3268: The previous TSV proto-form \*stamnăz was ad hoc — an a-stem masculine with root *a* that no source reconstructs. It produced pipeline output "stamn" (with no mechanism to front the root vowel), confirming it was wrong.
```

#### Germanic/docs/DEV_NOTES.md:3276 (exact COUNTERPART)

- Nearby heading: #### B. Why this is the right temporary decision

```text
3274: The TSV needs a form that actually yields the conservative OE output through the pipeline's sound changes. The pre-OE transponent \*stebn- (with root *e* already present, and the *-bn-* cluster that regularly becomes *-fn-*) satisfies this requirement:
3275: 
3276: - `stebnō → stefn` — pipeline output matches the attested conservative OE form
3277: - No new rules needed; *bn → fn is already handled
3278: - The root *e* is inherited (not produced by umlaut or other mechanism)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/notable_findings.md:14 (exact COUNTERPART)

- Nearby heading: ## Table of Contents

```text
13: 4. [A-restoration trigger set: {*æ} is NOT a trigger](#4-a-restoration-trigger-set-æ-is-not-a-trigger)
14: 5. [The stefn/stemn problem: transponent versus reconstruction](#5-the-stefnstemn-problem-transponent-versus-reconstruction)
15: 6. [PGmc stem-class disambiguation via OE phonology: \*kraft- and \*stab-](#6-pgmc-stem-class-disambiguation-via-oe-phonology-kraft--and-stab-)
```

#### Germanic/docs/analysis/notable_findings.md:846 (exact COUNTERPART)

- Nearby heading: ## 5. The stefn/stemn problem: transponent versus reconstruction

```text
845: 
846: ## 5. The stefn/stemn problem: transponent versus reconstruction
847: 
```

#### Germanic/docs/analysis/notable_findings.md:848 (exact COUNTERPART)

- Nearby heading: ## 5. The stefn/stemn problem: transponent versus reconstruction

```text
847: 
848: **Date discovered:** Session 046 (stefn/stemn investigation)
849: 
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| stem | stemn | inh | template:inh | stem |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10 (concept name)

- Nearby heading: ### Polished topic sections

```text
8: - [PWGmc *j-related Sound Changes](#pwgmc-j-related-sound-changes--reviewed-see-notable_findingsmd-3)
9: - [OE Medial Vowel Syncope: meolc and netle](#oe-medial-vowel-syncope-meolc-and-netle-2026-03-21)
10: - [OE duru 'door': Stem-Class Correction](#oe-duru-door-stem-class-correction)
11: - [OE botm 'bottom': Paradigmatic Leveling](#oe-botm-bottom-paradigmatic-leveling)
12: - [PGmc *i > WGmc *e Lowering](#pgmc-i--wgmc-e-lowering-the-case-of-nest-2026-03-09h)
```

#### Germanic/docs/DEV_NOTES.md:21 (concept name)

- Nearby heading: ### Mismatch fixes (Mar 2026)

```text
19: - [OE þistel 'thistle': Scholarly Controversy](#oe-þistel-thistle-i-umlaut-not-preserved-2026-03-18)
20: - [OE huniġ 'honey': The -ag > -ig Sound Change](#oe-huniġ-honey-the--ag---ig-sound-change-2026-03-19)
21: - [OE wīþiġ 'withy': ja-stem vs Sievers' Law](#oe-wīþiġ-withy-ja-stem-adjective-vs-sievers-law-syncope-2026-03-19)
22: - [OE heofon 'heaven': Back Umlaut and Nasal Dissimilation](#oe-heofon-heaven-back-umlaut-and-medial-syncope-2026-03-20)
23: - [OE lungen 'lung': The *-anjō Suffix Problem](#oe-lungen-lung-the--anjō-suffix-problem-2026-03-21)
```

#### Germanic/docs/DEV_NOTES.md:86 (concept name)

- Nearby heading: ### Summary of the scholarly literature

```text
84: **Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.
85: 
86: **R/T (§2.3.1, pp.32-33 / our OCR pp.47-48)** agree these are genuine exceptions but reach a different conclusion about paradigmatic leveling. They find it "implausible" for a-stem nouns, arguing that the only case-forms with high-vowel suffixes are functionally marginal: inst.sg. *-u, dat.pl. *-umaz, inst.pl. *-umiz. They conclude: "We do not really know why *u failed to lower in these forms."
87: 
88: ### Could we use paradigm forms? (Why we decided not to)
```

#### Germanic/docs/DEV_NOTES.md:92 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
90: For other problematic items (fire, brand, berry, thorn), we successfully resolved mismatches by adopting a paradigm form in which the phonological development is lautgesetzlich. The question is whether the same approach works for the u-lowering exceptions.
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
```

#### Germanic/docs/DEV_NOTES.md:93 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
95: **What weighs against Approach A:**
```

#### Germanic/docs/DEV_NOTES.md:96 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
94: 
95: **What weighs against Approach A:**
96: - Kroonen reconstructs *wulfa- (a-stem; p.598), *fugla- (a-stem), and *bukka(n)- (originally n-stem; p.98) — none as u-stems.
97: - There is no Gothic or comparative evidence for u-stem inflection of these words. Gothic wulfs is an a-stem, Gothic fugls is an a-stem.
98: - Using a u-stem nom.sg. would require us to posit a stem-class that is not attested in any daughter language. This would be philologically indefensible.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:367 (concept name)

- Nearby heading: ### 4.1 Pro-restoration evidence with single intervening *r* or *l* (back vowel triggers)

```text
366: | **gafol** 'fork' | *\*gabulu → \*gæbulu → gafol* | R/T 11101 |
367: | **magu** 'boy' | *\*maguz → magu* (u-stem) | R/T 11104 |
368: | **lagu** 'water, sea' | *\*laguz → \*lægu → lagu* | R/T 11106 |
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:443 (concept name)

- Nearby heading: ### 6.2 bæst

```text
442: 
443: * PGmc reconstruction: Orel §`*bastan ~ *bastaz` — neut. strong *a*-stem.
444: * The nom.-acc. sg. ending in PGmc was `*-Ø` (neuter `*a`-stems lose the bare `*a` in PWGmc, cf. R/T 3.1.2 / 3.1.4) or `*-ą`. In the FST input notation this is `*bastą`.
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:28 (concept name)

- Nearby heading: ## Introduction

```text
27: 
28: - **Compound first-elements** (especially as the first member of nominal compounds, where stem form is preserved and analogical pressure from inflectional paradigms is reduced) — this is the classical "Watkins principle" locus.
29: - **Dialectal doublets** — one OE dialect retains the lautgesetzlich form while another shows analogical leveling. Anglian forms are particularly prone to this because of conservative scribal traditions in Bede glosses, the Vespasian Psalter, and parts of the poetic corpus.
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:55 (concept name)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
54: |-------|-------|
55: | **PROTO** | `*mizdō` (f., strong ō-stem; PIE *misdʰ-o/eh₂-) |
56: | **OE FORMS** | WS **mēd** ; Anglian-leaning **meord** (dialectal doublet) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:73 (concept name)

- Nearby heading: ### Case 2: *spéru (spear) — speoru

```text
72: |-------|-------|
73: | **PROTO** | `*spéru` (m./n., light u-stem or reformed i-stem; PIE *sperH-) |
74: | **OE SIMPLEX** | `spere` (nom.sg., attested widely: Maldon, Beowulf, Ælfric; non-umlauted) |
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:19 (concept name)

- Nearby heading: ## Kroonen's reconstruction (*kō- ~ *ku-)

```text
18: >
19: > A root noun continuing the common IE word for 'cow'. Germanic has two different root variants, i.e. *kō- and *kū-, both of which belonged to an originally ablauting paradigm **nom. *kōz, obl. *kū-**, continuing a PIE u-stem *gʷéh₃-u-s, obl. *gʷh₃-u-.
20: 
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:22 (concept name)

- Nearby heading: ## Kroonen's reconstruction (*kō- ~ *ku-)

```text
21: Key points:
22: - Full-grade stem: *kō- (nominative)
23: - Zero-grade stem: *kū- (oblique cases)
```

#### Germanic/docs/analysis/cow_root_noun_investigation.md:23 (concept name)

- Nearby heading: ## Kroonen's reconstruction (*kō- ~ *ku-)

```text
22: - Full-grade stem: *kō- (nominative)
23: - Zero-grade stem: *kū- (oblique cases)
24: - Both are PIE-inherited ablaut grades, not analogical innovations
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:1 (concept name)

- Nearby heading: # Investigation: *deljăz "dill" — i-stem vs ja-stem

```text
1: # Investigation: *deljăz "dill" — i-stem vs ja-stem
2: 
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:9 (concept name)

- Nearby heading: ## Current TSV state

```text
8: - **Pipeline result**: `deljăz → dill` (wrong — expected `dile`)
9: - **Pipeline with i-stem**: `deliz → dile` ✓
10: 
```

#### Germanic/docs/analysis/dill_stem_class_investigation.md:17 (concept name)

- Nearby heading: ## Kroonen's reconstruction (*deli- ~ *delja-)

```text
16: >
17: > The material offers evidence for both an i-stem (OE dile) and a ja-stem (OS dilli, OHG tilli). Perhaps the forms with rounded vowels (OE dyle, MHG tülle) can be adduced to reconstruct an additional ablauting pair *duli- ~ *dulja-. If so, the original paradigm probably had ablaut of the root, viz. nom. *deliz, gen. *duljaz < *dhél-i-s, *dhl̥-i-ós.
18: 
```

#### Germanic/docs/analysis/final_vowel_missing_analysis.md:11 (concept name)

- Nearby heading: ### Example: 'berry'

```text
10: ### Example: 'berry'
11: - **PGmc**: `*bazją` (neut. nom.-acc.sg. ja-stem with nasal vowel)
12: - **PWGmc**: `*baʀi` (after denasalization and ja-stem reduction)
```

#### Germanic/docs/analysis/final_vowel_missing_analysis.md:12 (concept name)

- Nearby heading: ### Example: 'berry'

```text
11: - **PGmc**: `*bazją` (neut. nom.-acc.sg. ja-stem with nasal vowel)
12: - **PWGmc**: `*baʀi` (after denasalization and ja-stem reduction)
13: - **OE**: `berġe` (expected)
```

#### Germanic/docs/analysis/final_vowel_missing_analysis.md:35 (concept name)

- Nearby heading: ### 2. Ja-Stem Reduction (Light Roots)

```text
34: 
35: ### 2. Ja-Stem Reduction (Light Roots)
36: **R/T §6.8.2 (line 21868)**: "PWGmc ja-stems with light root syllables had a nom.-acc. sg. in *-i"
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:119 (concept name)

- Nearby heading: ### Pipeline issues

```text
118:    from \*skeldu- (with *e). The base vowel question is unresolved. If \*skild-
119:    (u-stem with leveled *i from oblique cases) is the base, then the proto
120:    should have *i. But that's *skild-lingaz, which is a compound our pipeline
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:141 (concept name)

- Nearby heading: ### Proto-form assessment

```text
140: 
141: The TSV proto `*furxtīn` appears to be an attempt at an ī-stem abstract noun
142: \*furhtīn-. R/T (line 21553) treat fyrhtu as an **ī-stem abstract noun**, which
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:142 (concept name)

- Nearby heading: ### Proto-form assessment

```text
141: The TSV proto `*furxtīn` appears to be an attempt at an ī-stem abstract noun
142: \*furhtīn-. R/T (line 21553) treat fyrhtu as an **ī-stem abstract noun**, which
143: would have PGmc nom.sg. \*furhtiz. But Kroonen does not reconstruct an
```

#### Germanic/docs/analysis/fryhtu_investigation.md:22 (concept name)

- Nearby heading: ### Kroonen's reconstructions

```text
21: 
22: Kroonen does not reconstruct an ī-stem \*furhtiz or an \*iþō-abstract \*furhtiþō.
23: 
```

#### Germanic/docs/analysis/fryhtu_investigation.md:26 (concept name)

- Nearby heading: ### R/T's analysis

```text
25: 
26: R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
27: (\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
```

#### Germanic/docs/analysis/fryhtu_investigation.md:27 (concept name)

- Nearby heading: ### R/T's analysis

```text
26: R/T (line 21553) treat OE fyrhtu as an **ī-stem abstract noun**. The i-umlaut
27: (\*u → y) proves an \*i-containing source, since the ō-stem \*furhtō- would give
28: OE \*forhte without umlaut.
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:240 (concept name)

- Nearby heading: ### 2.8 Campbell, *Old English Grammar* (1959)

```text
239: **(d)** §588 (line 15201) — *meord* and *mēd* listed as variants in the
240: strong-feminine ō-stem class:
241: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:362 (concept name)

- Nearby heading: ### 2.12 Ringe, *From Proto-Indo-European to Proto-Germanic* (vol. 1, 2006)

```text
361: > *mizdō (cf. OE mēd ~ meord; Goth. mizdo has been remodeled as an
362: > n-stem)"
363: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:385 (concept name)

- Nearby heading: ### 2.13 Ringe & Taylor, *The Development of Old English* (vol. 2, 2014)

```text
384: 
385: > "PGmc \*mizdō 'reward' (Goth. mizdō, remodelled as an n-stem) >
386: > PWGmc \*mizdu > OE meord ~ mēd, OF mēde ~ mide, OS mēda, OHG miata."
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:45 (concept name)

- Nearby heading: ### The core problem

```text
44: 2. **Breaking**: `*mirdō` → `*meordō` (breaking of *i → *eo before r+C)
45: 3. **Weak tail**: `*meordō` → `meord` (loss of final vowel in heavy ō-stem)
46: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:61 (concept name)

- Nearby heading: ### 2.1 Standard dictionary lemmata

```text
60: - Etymology: "from PGmc. *mizdō"
61: - Inflection: strong fem. ō-stem (nom.sg. mēd, acc.sg. mēd/mēde, gen.sg. mēde, dat.sg. mēde)
62: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:93 (concept name)

- Nearby heading: #### Form B: `meord` (diphthong eo, with medial /r/)

```text
92: 2. **Compounds and derivatives**:
93:    - **meord-gifa** 'reward-giver' (attested in early texts, showing preservation of *meord-* stem)
94:    - Campbell §210 (back umlaut section) does **not** list *meord* among his back-umlaut examples, suggesting it's not a productive form
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:137 (concept name)

- Nearby heading: #### Verdict on *meord₂* attestations

```text
136: - **Simplex *meord* 'reward'**: **NO clear attestation found** in any OE source (glossaries, prose, poetry)
137: - **Compound *\*meord-gifa* or *\*meord-lēan***: **NOT attested**; all compounds use **mēd-** stem
138: - **Dictionary listings**: BT, Clark Hall, DOE all list *meord* as a **cross-reference** or **variant form** but provide **no actual textual citations**
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:183 (concept name)

- Nearby heading: ### 3.2 Kroonen (2013), *Etymological Dictionary of Proto-Germanic*

```text
182: 
183: > PGmc \*mizdo 'reward' (Goth. mizdo, remodelled as an n-stem) > PWGmce \*mizdu >  
184: > OE meord ~ méd, OF méde ~ mide, OS méda, OHG miata;
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:188 (concept name)

- Nearby heading: ### 3.2 Kroonen (2013), *Etymological Dictionary of Proto-Germanic*

```text
187: 
188: > PGmc \*mizdo 'reward' (extended as an n-stem in Goth. mizdo) > PWGmc \*mizdu  
189: > (OF méde, OS méda, OHG miata) > OE meord ~ méd;
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:22 (concept name)

- Nearby heading: ## §1. Question

```text
21: dossier `un-to-on-chronology.md`) that the OE-internal change
22: `*-un > -on` is **phonologically blocked** by stem-`u` harmony in
23: exactly the environment these two verbs occupy: stressed `*ú` +
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:116 (concept name)

- Nearby heading: ## §2. Reconstruction of the original choice (checkpoints 064–065)

```text
115:    directly, with the FST asked to derive it), and the widow case
116:    is morphological/lexical (a single noun stem), not paradigmatic
117:    in the strong-verb sense. So the *būgan*/*sċūfan* retargeting is
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:122 (concept name)

- Nearby heading: ## §2. Reconstruction of the original choice (checkpoints 064–065)

```text
121:    stood at that time gave `bugon`/`sċufon`.** That FST did not yet
122:    have the stem-`u` harmony block on `OEMedUnstressedULowering`.
123:    Once the harmony block was reinstated for §17.51.A1 (commit
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:187 (concept name)

- Nearby heading: ### Local handbook evidence

```text
186: pl. `scyufon` — **but with `-on`, not `-un`**, and with a
187: Northumbrian-specific diphthongised stem-vowel `yu` for `ū`.
188: 
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:214 (concept name)

- Nearby heading: ### Verdict

```text
213: Northumbrian `scyufon` in the Durham Ritual, which still has `-on`
214: (it differs from southern `scufon` only in the stem-vowel
215: diphthongisation `ū > yu`, a Northumbrian phonological development
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:342 (concept name)

- Nearby heading: ## 4. The *nigon* / *wegas* principle (why a following back vowel is special)

```text
341: - *weġ* (sg., front V _ #) palatal vs. *wegas* (front V _ a-back) velar
342: - *dæġ* (sg.) palatal vs. *daga* (gen.pl.) velar (different stem vowel of
343:   course, but the synchronic alternation is *dæġ ~ dagas*)
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:8 (concept name)

- Nearby heading: ## Question

```text
7: existing dossier `widuwe-u-preservation.md` (Appendix D) blocks
8: unstressed-`*u` lowering after a stem-syllable `*u` + single consonant
9: (Brunner §44 Anm. 7, Luick §326.2). On that conditioning, `bugun`
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:10 (concept name)

- Nearby heading: ## Question

```text
9: (Brunner §44 Anm. 7, Luick §326.2). On that conditioning, `bugun`
10: (stem `u` + single `g` + `-un`) is exactly parallel to `wuduwe`,
11: `munuc`, `duguþ`: the lowering is blocked, and `-un` is the regular
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:17 (concept name)

- Nearby heading: ## Question

```text
16: (closed final syllable; verbal-ending status; etc.) makes `-un > -on`
17: in the pret.pl. a Lautgesetz that bypasses stem-`u` harmony.
18: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:151 (concept name)

- Nearby heading: #### §44 Anm. 7 — preservation list (no *w*)

```text
150: 
151: Brunner's exclusion list is **`m`, `ng`, and post-stem-`u`**. *No
152: mention of `w` or labials as a class.*
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1367 (concept name)

- Nearby heading: #### C.2.1 Ringe, *From PIE to Proto-Germanic* (vol. 1)

```text
1366: > Joseph, p.c. ca. 1980) appears in PGmc in the 'compromise form' *widuwō-n-,
1367: > with a full-grade stem vowel (extended by *-n-) and a medial syllable that
1368: > seems to owe its syllabicity to one PIE alternant and the identity of its
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1675 (concept name)

- Nearby heading: ## Appendix D — Conditioning of OE medial unstressed *u (open vs. closed; -un/-on; harmonisation)

```text
1674: 2. **Strong-verb pret. pl. ending** (`*-un` ~ `*-on`),
1675: 3. **Stress / harmony** with a preceding stem-syllable *u.
1676: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Stiles1985 | author + year mention (Stiles 1985) |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Stiles2012 | surname mention only: Stiles |
| Stiles2017 | surname mention only: Stiles |
| Stiles1986a | surname mention only: Stiles |
| Stiles1986b | surname mention only: Stiles |

