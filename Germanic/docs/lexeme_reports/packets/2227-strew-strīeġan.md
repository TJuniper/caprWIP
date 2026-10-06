# Evidence packet — 2227 strew / strīeġan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2227 | strew | strīeġan | *stráwjaną | *stráwjaną | reconstructed_oe | Unattested West Saxon cognate; reconstructed *strīeġan per regular WS development of PGmc *straujan-. Attested Anglian strēgan (cf. Ringe & Taylor vol.2 §6.1) proves the class 1 weak verb was inherited into English; the WS form was remodelled as class 2 strewian. We target the predicted WS reflex and deliberately do not model the Anglian-specific smoothing *ēa → *ē / _ġ. See DEV_NOTES §17.10.36. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# strew
PROTO: *stráwjaną
EXPECTED: strīeġan
OUTPUTS: strīeġan



### Proto-Germanic consonant inheritance

Proto Input: *stráwjaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Awj Glide Formation: *stráujaną<br>OE Au Fronting: *stráeujaną<br>OE Diphthong Leveling: *strēajaną<br>OE Heavy Syllable Nasal Apocope: *strēajan<br>OE Secondary Nasalization: *strēająn<br>OE I Umlaut: *strīejąn<br>OE Weak Tail Reduction: *strīejan<br>OE J Strengthening After Front Diphthong: *strīeʒan |



### Orthography & surface

Old English Orthography: *strīeġan
Outcome: strīeġan

NOTE: Unattested West Saxon cognate; reconstructed *strīeġan per regular WS development of PGmc *straujan-. Attested Anglian strēgan (cf. Ringe & Taylor vol.2 §6.1) proves the class 1 weak verb was inherited into English; the WS form was remodelled as class 2 strewian. We target the predicted WS reflex and deliberately do not model the Anglian-specific smoothing *ēa → *ē / _ġ. See DEV_NOTES §17.10.36.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:26825 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26823:     Reachable with stages 2, 4 added (stages 1, 3, 5-WS exist).
26824: 
26825: Target 2: row 2227 *strawjaną → strēgan (Anglian).
26826:     Anglian pathway (stages 1-5):
26827:       *strawjaną → stage 1 → *strawwjaną
```

#### Germanic/docs/DEV_NOTES.md:26843 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26841: ~~~~~~~~~~~~~~~~~~~~~~~~~~
26842: 
26843: Our TSV target for row 2227 is the Anglian form (strēgan),
26844: because no WS regular reflex exists. Our TSV target for row
26845: 2061 is the WS form (hīeġ). A single deterministic FST cannot
```

#### Germanic/docs/DEV_NOTES.md:26852 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26850:        too (regression risk to be surveyed: cnēoris, dēag,
26851:        sēag, etc.), or
26852:    (b) we change the row 2227 target to predicted WS
26853:        *strīegan and document this as "predicted regular WS
26854:        reflex; attested form is morphologically remodelled
```

#### Germanic/docs/DEV_NOTES.md:26856 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26854:        reflex; attested form is morphologically remodelled
26855:        streowian", forgoing the Anglian attestation, or
26856:    (c) we leave row 2227 as a documented exception (no
26857:        grammar change), and only add stages 1-2 to fix row
26858:        2061 (hīeġ), netting one fix instead of two.
```

#### Germanic/docs/DEV_NOTES.md:27121 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
27119: 
27120: CONTEXT: Q1 and Q2 have been implemented (OEAwwjResolution rule,
27121: commit 158e951). Row 2061 (*xáwwją → hīeġ) now matches. Row 2227
27122: (*stráwjaną → expected strīeġan) still mismatches: FST produces
27123: strīeian (intervocalic *j vocalized to *i via OEIntervocalicJVocalization
```

#### Germanic/docs/DEV_NOTES.md:27122 (exact pair)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
27120: CONTEXT: Q1 and Q2 have been implemented (OEAwwjResolution rule,
27121: commit 158e951). Row 2061 (*xáwwją → hīeġ) now matches. Row 2227
27122: (*stráwjaną → expected strīeġan) still mismatches: FST produces
27123: strīeian (intervocalic *j vocalized to *i via OEIntervocalicJVocalization
27124: line 2355) rather than strīeġan (expected *j preserved, spelled ġ
```

#### Germanic/docs/DEV_NOTES.md:27124 (exact COUNTERPART)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
27122: (*stráwjaną → expected strīeġan) still mismatches: FST produces
27123: strīeian (intervocalic *j vocalized to *i via OEIntervocalicJVocalization
27124: line 2355) rather than strīeġan (expected *j preserved, spelled ġ
27125: via OldEnglishOrthography).
27126: 
```

#### Germanic/docs/DEV_NOTES.md:27128 (exact COUNTERPART)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
27126: 
27127: The user accepted an Option-B style TSV treatment (like cnobba row
27128: 609): target unattested WS *strīeġan, note in TSV that Anglian strēgan
27129: proves class-1 inheritance but we do not model Anglian-specific
27130: smoothing. Row 2227 has been updated accordingly. The remaining
```

#### Germanic/docs/DEV_NOTES.md:27131 (exact COUNTERPART)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
27129: proves class-1 inheritance but we do not model Anglian-specific
27130: smoothing. Row 2227 has been updated accordingly. The remaining
27131: question (Q3) is: should we add a phonological rule to derive strīeġan,
27132: or accept the mismatch as a documented exception?
27133: 
```

#### Germanic/docs/DEV_NOTES.md:27375 (exact pair)

- Nearby heading: ## Probe 1: All PROTOFORMs with *Vw+*j in input

```text
27373: Result (2 hits):
27374:     509   *xáwwją       hīeġ      (already matches post-Q1/Q2)
27375:     1153  *stráwjaną    strīeġan  (target of the proposed rule)
27376: 
27377: No other *Vw+*j inputs exist. The entire class is exhausted by
```

#### Germanic/docs/DEV_NOTES.md:27464 (exact pair)

- Nearby heading: ## CONCLUSION

```text
27462: Regression surface for OEJStrengtheningAfterFrontDiphthong is
27463: **empirically zero** across the 386 OE forms in the corpus.
27464: The rule changes exactly one form: *stráwjaną → strīeġan (a
27465: current mismatch becomes a match), with no other form affected.
27466: 
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

#### Germanic/docs/DEV_NOTES.md:483 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
481: 
482: **For the FST:** Target `wuduwe` as the regular WS outcome. The FST cannot model
483: the early Anglian syncopation (which may be a dialectal retention from NWGmc or
484: a sequence-specific contraction), nor the subsequent analogical restoration to
485: `widuwe`.
```

#### Germanic/docs/DEV_NOTES.md:639 (note keyword: West Saxon)

- Nearby heading: #### 2. OE Medial Unstressed *u → *o (Campbell §373)

```text
637: #### 2. OE Medial Unstressed *u → *o (Campbell §373)
638: 
639: **Rule:** Unstressed medial `*u → *o` in West Saxon and Northumbrian, but NOT after
640: an accented `*u` in the preceding syllable.
641: 
```

#### Germanic/docs/DEV_NOTES.md:1110 (note keyword: West Saxon)

- Nearby heading: ### Campbell on the phonology

```text
1108: ### Campbell on the phonology
1109: 
1110: Campbell (OEG §419-420) discusses the cluster `*-pm- > -tm-` in West Saxon:
1111: 
1112: > "After a short vowel, pl, pm > tl, tm in W-S, e.g. botl building, bytla builder, setl seat, botm bottom, bytme keel."
```

#### Germanic/docs/DEV_NOTES.md:1795 (note keyword: West Saxon)

- Nearby heading: ### English sandbox todo — surface accuracy focus

```text
1793:   - Rhotic data audit: 118 English proto entries contain `{r}`; the problematic clusters are `rdă` (4 entries), `rgă` (1), `rwō` (1), `rθo` (1). These align exactly with `tmp/rhotic_test_set.txt`. We need historically grounded rewrites (e.g. `{*rgă → {*rəʊ}}`, `{*rdă → {*ər}}`, `{*rwō → {*rəʊ}}`, `{*erθo → {*erθ}}) before `EnglishSandboxPostVocalicRLoss` deletes `{*r}`.
1794:   - Next session: redesign `EnglishSandboxProtoRhoticFronting`/`EnglishSandboxRhoticBreaking` around those phonetic targets, rerun the rhotic tracer, and rerun `python3 tools/english_apply_down_stats.py` (current baseline: 333/376 single outputs, 20 exact matches).
1795: - **Add the missing palatalisation pass.** Insert a dedicated `EnglishSandboxPalatalisation` stage (after West Germanic or glide deletion) that maps `{*bj→v}`, `{*gj→dʒ}`, `{*kj→tʃ}`, `{*sk→ʃ}` before front vowels. This captures the well-known West Saxon/Midlands changes needed for `believe/beech/chew/shield/ship` and collapses a large swath of remaining errors.
1796: - Once these three TODOs land, rerun `tools/english_apply_down_stats.py` to confirm the “exactly one correct output” count climbs beyond the current ~20/376.
1797: 
```

#### Germanic/docs/DEV_NOTES.md:2296 (note keyword: smoothing)

- Nearby heading: ### Failure buckets & historical targets

```text
2294: - Top-down staging notes before touching code:
2295:   - **Late OE short-vowel conditioning**: finish the FOOT–STRUT stage so `{*u}` first branches to `{ʊ}` in dark-l/velar/alveolar codas, then feeds `{ʌ}` in open or dental contexts; likewise confine the KIT split to nasal/liquid + consonant codas (stop globally rewriting `{e}`).
2296:   - **ME /r/-loss**: add a post-breaking stage that deletes `{r}` after vowels/codas (mirroring historical smoothing) so `{*bōr}` surfaces as `{bɔː}` before Late Reduction derives `board`/`bier` outcomes.
2297:   - **Weak-tail clean-up**: continue driving reductions via `EnglishSandboxWeakTailVowel` so schwa mappings target the templated tails instead of ad-hoc contexts.
2298: - For each block, validate against the relevant bucket from `tmp/english_sandbox_results.json` and log stage traces so the top-down picture stays anchored to the bottom-up error counts.
```

#### Germanic/docs/DEV_NOTES.md:2309 (note keyword: smoothing)

- Nearby heading: ### KIT sweep (status: reverted to baseline)

```text
2307: 
2308: - Replayed the dockered `flookup` harness (`python3 - <<'PY' …`) to isolate the true KIT cases (filtering out `aɪ/eɪ/ɔɪ`). We still have 35 `{ɪ}` forms headed by `fish/give/six/will` plus the `{ɪə}`+`r` items (`beard/bier/deer/spear/year`).
2309: - Restored the brace-aware helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`), the `{*u}` contexts, and `EnglishSandboxPostVocalicRLoss` after rolling back an experimental smoothing stage that tanked the harness. `english_brace_sandbox.bin` is back to the 179/376 success baseline.
2310: - `python3 server/tools/api_regression.py` remains green, so the sandbox is stable again for the next round of KIT work (detailed smoothing + consonant-cluster contexts).
2311: 
```

#### Germanic/docs/DEV_NOTES.md:2310 (note keyword: smoothing)

- Nearby heading: ### KIT sweep (status: reverted to baseline)

```text
2308: - Replayed the dockered `flookup` harness (`python3 - <<'PY' …`) to isolate the true KIT cases (filtering out `aɪ/eɪ/ɔɪ`). We still have 35 `{ɪ}` forms headed by `fish/give/six/will` plus the `{ɪə}`+`r` items (`beard/bier/deer/spear/year`).
2309: - Restored the brace-aware helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`), the `{*u}` contexts, and `EnglishSandboxPostVocalicRLoss` after rolling back an experimental smoothing stage that tanked the harness. `english_brace_sandbox.bin` is back to the 179/376 success baseline.
2310: - `python3 server/tools/api_regression.py` remains green, so the sandbox is stable again for the next round of KIT work (detailed smoothing + consonant-cluster contexts).
2311: 
2312: ### Short-vowel fixes + /r/-loss scaffold
```

#### Germanic/docs/DEV_NOTES.md:2316 (note keyword: smoothing)

- Nearby heading: ### Short-vowel fixes + /r/-loss scaffold

```text
2314: - Added plain helper sets (`EnglishSandboxPlainVocalic/Liquid/Nasal`) so late-stage rules can reason about the brace-free vowels while still matching against the starred consonants passed along from the proto inventory.
2315: - Reworked `EnglishSandboxShortVowelSplit` to cover the documented FOOT/STRUT environments: `{*u}` now targets `{ʊ}` before velars, `{*z/m/n}` plus weak-tail templates, dark `{*l}`, `{*r}`, and the `{*f}/{*s}/{*θ}` codas (`wolf/wool`), while KIT contexts keep `{*e}`→`{ɪ}` before nasals/liquids. Everything else still falls through to `{ʌ}`/`{ɛ}`.
2316: - Inserted `EnglishSandboxPostVocalicRLoss` (after the vowel stack but before weak-tail reductions) so `{*r}` drops after any plain vowel plus a consonant/word boundary, giving us a chronological hook for the upcoming smoothing work.
2317: - Reran the attested-form sweep (same `python3 - <<'PY' …` harness as above): 179/376 English entries now reconstruct (up from 119), with the failure buckets collapsing to KIT = 61, FOOT = 3, weak-tail schwa = 51, /r/-bearing = 54, and `{ɔ/əʊ}` = 18. Spot checks show `bəʊn/bəʊθ` retrieving `{*bōr}` bundles prior to loss, while known outliers like `bʊzəm` and the irregular `ʋʊl/ʋʊlf` remain on the TODO list.
2318: - `python3 server/tools/api_regression.py` still PASS for Burmish & Germanic after the rewrites, so the sandbox tweaks stay isolated.
```

#### Germanic/docs/DEV_NOTES.md:2324 (note keyword: smoothing)

- Nearby heading: ### KIT sweep (WIP)

```text
2322: - Fed the KIT bucket through the same dockered `flookup` harness (`python3 - <<'PY' …`) after filtering out diphthongs (`aɪ/eɪ/ɔɪ`). The remaining 35 entries are the genuine `{ɪ}` cases headed by `fish/give/six/will` alongside the `{ɪə}` + post-vocalic /r/ cohort (`beard/bier/deer/spear/ year`, etc.).
2323: - Updated `EnglishSandboxCoreVowelRules` so short `{*i}` finally drops its star and enters the plain alphabet, and extended `EnglishSandboxShortVowelSplit` with `{i}`→`{ɪ}` rewrites in closed syllables / word-final contexts. This keeps the KIT conditioning in the same stage as the `{*e}`/{`*u`} splits instead of leaving `{*i}` untouched.
2324: - The attested-form harness still lands at 179/376 successes (KIT bucket = 35) because the stubborn cases need post-vocalic /r/ smoothing (`{ɪ}`→`{ɪə}` before the new `EnglishSandboxPostVocalicRLoss`) or suffixal analogies (`sieve/singe/timber`). Logged them here so the next pass can target `{ɪə}` outputs without sacrificing the `{bəʊn}/{fʊt}` improvements we just landed.
2325: 
2326: ## 2025-12-04
```

#### Germanic/docs/DEV_NOTES.md:2328 (note keyword: smoothing)

- Nearby heading: ### KIT/FOOT contexts + /r/-smoothing harness

```text
2326: ## 2025-12-04
2327: 
2328: ### KIT/FOOT contexts + /r/-smoothing harness
2329: 
2330: - Extended EnglishSandboxShortVowelSplit so FOOT now targets alveolar codas in both starred and plain alphabets ({t/d/z} + weak-tail templates, plain {l/r} codas) and added a plain {*i}->{i} feed so the KIT split can finally act on closed {i} syllables. Introduced EnglishSandboxPostVocalicRSmoothing between the vowel stack and /r/-loss so {ɪ} can surface as {ɪə} before EnglishSandboxPostVocalicRLoss deletes {r}.
```

#### Germanic/docs/DEV_NOTES.md:3321 (note keyword: West Saxon)

- Nearby heading: #### C. Primary Old English and English-historical evidence

```text
3319: 1. Pre-OE \*stebn- (preserved in CorpGl stebn, c.800)
3320: 2. Early OE stefn (bn → fn; general across all dialects)
3321: 3. Late WS stemn (fn → mn; specifically West Saxon, Alfredian period or later)
3322: 4. ME stevne (continues the fn-type, confirming stemn is secondary)
3323: 
```

#### Germanic/docs/DEV_NOTES.md:3568 (note keyword: West Saxon)

- Nearby heading: #### Where the sources may disagree

```text
3566: #### Where the sources may disagree
3567: 
3568: 1. **Gen.sg. *-ōz: bimoraic or trimoraic?** R/T treat the gen.sg. *-ōz as BIMORAIC (p.73, listed among bimoric forms; outcome: PWGmc *-a → OE -e). Bülbring §390 lists "ws. kent. Gen. Sg. der Abstrakta auf ung: leasunga 'Truges' (urg. -ōz)" under TRIMORAIC (outcome: OE -a). However, this appears to be a CLASS-SPECIFIC or DIALECTAL variant: (a) the -ung abstract class may have had different mora assignment; (b) Bülbring specifies "ws. kent." (West Saxon/Kentish), suggesting dialectal conditioning; (c) the standard WS gen.sg. of ō-stems is -e (giefe), not -a (cf. R/T p.314). Our pipeline follows R/T in treating the gen.sg. as bimoraic, giving -e, which is the standard WS outcome.
3569: 
3570: 2. **Mechanism of *-ōz shortening**: R/T present *-ōz → *-a as a single PWGmc development (p.58: *gebōz → *geba with no intermediate stage). Luick implies a two-step process: (a) z was present during early bimoraic shortening (§299 Anm. 2), so the *-ō in *-ōz was not word-final and did not undergo §299 shortening; (b) z was then lost; (c) the freed *-ō was shortened by a later change. Both analyses produce the same result (*-ōz → *-a), but Luick's is more decomposed. Our pipeline follows R/T's single-step approach, which is also technically necessary: a separate "final *-ō → *-a" rule would incorrectly affect nom.sg. *-ō (see discussion above).
```

#### Germanic/docs/DEV_NOTES.md:4116 (note keyword: West Saxon)

- Nearby heading: ### The attested OE paradigm cells (Campbell §762)

```text
4114: Campbell gives the following actual OE forms:
4115: 
4116: **West Saxon:**
4117: | Cell | Form | Notes |
4118: |------|------|-------|
```

#### Germanic/docs/DEV_NOTES.md:10411 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10409: | 2026-04-23 | 35 | -1 | 5e733bb3 | wīþiġ: PROTOFORM *wīθijaz → *wīθagą (§17.10.35, Campbell -ag- suffix) |
10410: | 2026-04-23 | 34 | -1 | 29f4e924 | hīeġ: OEAwwjResolution *aw(w)+*j → *au+*j (§17.10.36 stages 1–2) |
10411: | 2026-04-24 | 33 | -1 | 0c6ab468 | strīeġan: OEJStrengtheningAfterFrontDiphthong (§17.10.36-q3) |
10412: | 2026-04-24 | 32 | -1 | 6a2bbda2 | cwedu: PROTOFORM *kwíθuz → *kwéðuz (§17.14) |
10413: | 2026-04-24 | 31 | -1 | 5fa587ab | sife: PROTOFORM *síbaz → *síbi (§17.15) |
```

#### Germanic/docs/DEV_NOTES.md:27143 (exact COUNTERPART)

- Nearby heading: ## A. GERMAN PHILOLOGICAL TRADITION — STRONG POSITIVE SUPPORT

```text
27141: Four major German OE grammars treat j-preservation after long
27142: vowels/diphthongs as an established (*gesichert*) rule, with all
27143: four explicitly listing strēgan/strīeġan in this class.
27144: 
27145: ### Kaluza, Historische Grammatik des Englischen §89(b)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:184 (note keyword: West Saxon)

- Nearby heading: ### 2.3 Hogg / *Cambridge History of the English Language* vol. I — file `hogg_vol1.txt`

```text
183: 
184: > Class VI verbs should, because of the sound change of restoration of *a* (see §3.3.3.1), have varied between /a/ and /æ/ in the present tense and the past participle, but in West Saxon at least /a/ was generalised throughout the present and was normal in the past participle. Hence we find *faran* ~ *for* ~ *foron* ~ *færen* 'go'.
185: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:96 (note keyword: smoothing)

- Nearby heading: ### Case 3: *swéstēr (sister) — swester (lautgesetzlich) vs. swustor (late-WS innovation)

```text
95: | **OE SIMPLEX (WS)** | `sweostor` (early WS, showing breaking *e → eo*); `swostor` (later leveling); **`swustor`** (late WS, **10th–11th c. only**, showing labio-velar rounding e → u after labial+velar; innovation, not lautgesetzlich) |
96: | **Sound changes** | Breaking (*e → eo* before labial+velar) in WS; Anglian smoothing (*eo → e* before dental t) gives *swester* |
97: | **Lautgesetzlich output** | `swester` (Anglian, FST: ✓ correct; no eo-umlaut in Anglian) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:139 (note keyword: smoothing)

- Nearby heading: ### Case 5: *nábulō (navel) — nafola / nafela

```text
138: | **Classification** | Unlike *meord*, *spere*, *tangle*, this case involves **oblique paradigm cells**: the oblique forms of the n-stem all show *a (e.g., *nafolan*), which preserves the *u of the root indirectly. The nominative singular `nafola` vs. `nafela` represents two diachronic stages of vowel harmony within OE, not a pre-OE phenomenon. |
139: | **Methodological use** | The TSV targets `nafola` (nom.sg., early form). The decision illustrates that when vowel-harmony changes occur *within* OE (rather than as inherited pre-OE changes), targeting the earlier stage may be appropriate if it represents the lautgesetzlich pathway before analogical smoothing. Parallel to the "vowel-harmony reduction" precedents in §17.10–17.13 (breve elimination research). |
140: | **Implementation** | Row 2133 targets `nafola`. The FST correctly produces it from `*nabulō` via vowel harmony. |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:330 (note keyword: smoothing)

- Nearby heading: ### Analysis

```text
329: - Unlike *leornian*, the simplex `mēd` is **universally attested** across all OE dialects with no dialectal split (Anglian *meord*, WS *mēd*).
330: - Unlike *tang*/*tange*, the analogical smoothing happened **pre-OE or very early OE** (before the major dialect split), so all documented OE shows `mēd`, not `meord`.
331: 
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

#### Germanic/docs/analysis/notable_findings.md:1550 (note keyword: smoothing)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1549: `Germanic/data/oe_known_problems.tsv` (status `wontfix`, category
1550: `smoothing_anglian_relic`). The earlier H1 recommendation (*rōkiz) is
1551: **withdrawn**.
```

#### Germanic/docs/analysis/notable_findings.md:1568 (note keyword: smoothing)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1567: the regular `rēac`. To derive the attested *rēc* lautgesetzlich
1568: requires Anglian smoothing (`ēa → ē / _velar`) inserted between
1569: `OEDiphthongLeveling` and `OEVelarPalatalization`. Adding that
```

#### Germanic/docs/analysis/notable_findings.md:1572 (note keyword: smoothing)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1571: *bēacen*, *hēah*, *ēage*, *sēah*, *tēah* — all WS forms that
1572: retain the diphthong. Smoothing is dialectally restricted (Anglian)
1573: and only lexically diffused into WS for a small set (lēac/lēc, rēc,
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:10 (note keyword: smoothing)

- Nearby heading: # West Saxon vs. Anglian: dialect differences in Old English

```text
9: Cross-references inside the repository:
10: - `Germanic/docs/DEV_NOTES.md §15` — `swustor`/`swester` smoothing/back-mutation
11:   discussion, including Campbell §210 fn. 1 on combinative back umlaut after `w`.
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:25 (note keyword: smoothing)

- Nearby heading: # West Saxon vs. Anglian: dialect differences in Old English

```text
24: | Hogg, *A Grammar of OE*, vol. 1: Phonology | `docs/references/hogg_vol1.txt` | §3 (breaking, BM) ll. 5050–5780; ch. 6 (dialects) ll. 20330–21260 |
25: | Campbell, *Old English Grammar* (1959) | `docs/references/campbell_old_english_grammar.txt` | §§139–169 (breaking, retraction, second fronting) ll. 4360–4940; §§205–233 (BM, smoothing) ll. 6140–6920 |
26: | Ringe & Taylor, *The Development of Old English* (2014) | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | §6.5 (PD + 2nd fronting) ll. 12450–12800; §6.9.2 (smoothing) ll. 17660–17850; §6.9.4 (back umlaut) ll. 18300–18500 |
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:26 (note keyword: smoothing)

- Nearby heading: # West Saxon vs. Anglian: dialect differences in Old English

```text
25: | Campbell, *Old English Grammar* (1959) | `docs/references/campbell_old_english_grammar.txt` | §§139–169 (breaking, retraction, second fronting) ll. 4360–4940; §§205–233 (BM, smoothing) ll. 6140–6920 |
26: | Ringe & Taylor, *The Development of Old English* (2014) | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | §6.5 (PD + 2nd fronting) ll. 12450–12800; §6.9.2 (smoothing) ll. 17660–17850; §6.9.4 (back umlaut) ll. 18300–18500 |
27: | Brunner, *Altenglische Grammatik* (1965) | `docs/references/brunner_1965_altenglische_grammatik.txt` | §119 (Ebnung) ll. 4745–4840 |
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

#### Germanic/docs/dossiers/widuwe-u-preservation.md:669 (note keyword: smoothing)

- Nearby heading: ### B.1 Bulbring, Altenglisches Elementarbuch sec. 264

```text
668: ised back to i in Anglian, sec. 230) — implies the rule is later
669: than Anglian smoothing.
670: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1157 (note keyword: smoothing)

- Nearby heading: ### B.8 Synthesis across the canvass: answers to questions A-G

```text
1156:   *wiu intermediate is consistent with this).
1157: - Anglian smoothing of *iu → *i (sec. 230) is later, only
1158:   affecting Anglian: this is why Anglian has wicu rather than
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1169 (note keyword: smoothing)

- Nearby heading: ### B.8 Synthesis across the canvass: answers to questions A-G

```text
1168:   (so the *u trigger is still present when the rule fires), and
1169:   must precede whatever models Anglian smoothing if such forms
1170:   enter the cogset.
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| strew | strewian | inh | template:inh | strew |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:479 (note keyword: Anglian)

- Nearby heading: ### Paradigm-cell analysis: Where does `widwe` come from? (2026-03-21)

```text
477: - Anglian: early syncopation → back mutation can't apply → `widwe`
478: 
479: The form `widuwe` is **analogical** — a compromise between the syncopated Anglian
480: `widwe` and the full three-syllable structure expected from the etymology.
481: 
```

#### Germanic/docs/DEV_NOTES.md:26377 (exact PROTOFORM)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26375: Mismatch (initial state)
26376: ------------------------
26377: PROTOFORM `*stráwjaną` (Class I weak); current FST output `strewan`;
26378: TSV target `strewian`. The FST loses *j after the heavy *aw-diphthong
26379: root (the regular Sievers / heavy-stem Class I behavior that gives
```

#### Germanic/docs/DEV_NOTES.md:26517 (exact PROTOFORM)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26515: 
26516: **Option A: post-transference Class II input → strēawian (1 attested target swap)**
26517:    - PROTOFORM `*stráwjaną` → `*stráwōjaną`
26518:    - COUNTERPART `strewian` → `strēawian`
26519:    - PROTO column: leave as `*strāwjaną` to preserve the PGmc
```

#### Germanic/docs/DEV_NOTES.md:26529 (exact PROTOFORM)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26527: 
26528: **Option B: Anglian-target with grammar extension → strēgan (longest stretch)**
26529:    - Keep PROTOFORM `*stráwjaną` (PGmc Class I, opinio communis).
26530:    - COUNTERPART `strewian` → `strēgan` (Anglian dialect, attested in
26531:      Hall p.32698; R/T vol.2 §14271 derive it lautgesetzlich).
```

#### Germanic/docs/DEV_NOTES.md:26597 (concept name)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26595: | *hawja 'hay'             | hīeġ       | hēġ        | hēġ           | §14268-14269  |
26596: | *kawjan / *kaw'wjan 'call' | cieġan   | cēġan      | ceiga         | §14274-14275  |
26597: | *strawjanǭ 'strew'       | (rebuilt)  | (rebuilt)  | (Angl.) strēgan | §14271-14272 |
26598: 
26599: Every dialect that fed the chain through to the OE stage produces a
```

#### Germanic/docs/DEV_NOTES.md:26634 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26632:                                                           intervenes between *w and *j
26633:   2198 *smérwijaną       smierwan       smierwan        ✓ heavy ja-stem, j-loss correct
26634:   2227 *stráwjaną        strewan        strewian        ✗ MISMATCH (R/T §6.1 case)
26635:   2288 *wíduwōn          widowe         widuwe          ✓ no *j; vowel-quality issue
26636:   2298 *wúlfaz           wolf           wulf            ✓ unrelated (u-lowering)
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:171 (note keyword: smoothing)

- Nearby heading: ### 3.2 The attested form: `mēd`

```text
170: 1. **Loss of medial /r/**: `*meordō` → `*meodō` (or earlier `*mirdō` → `*midō`)
171: 2. **Smoothing of breaking diphthong**: `*meo(r)dō` → `*mēdō`  
172: 3. **Weak tail**: `*mēdō` → `mēd`
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:189 (note keyword: smoothing)

- Nearby heading: #### Pathway B: Breaking applied, then smoothing + r-loss

```text
188: 
189: #### Pathway B: Breaking applied, then smoothing + r-loss
190: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:195 (note keyword: smoothing)

- Nearby heading: #### Pathway B: Breaking applied, then smoothing + r-loss

```text
194:       → *meodō (post-breaking r-loss in this specific cluster?)
195:       → *mēdō (smoothing of *eo → *ē before dental)
196:       → mēd
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:49 (note keyword: smoothing)

- Nearby heading: ## 1. Charge of this supplement

```text
48: 
49: 2. **Disagreement with Campbell §123 fn.2**: Campbell states "the eo of meord, leornian is from e by a **later change**" (implying smoothing happened after breaking). The user argues that the -eo- is instead an **archaism** preserved in compound, following the **Watkins principle** (archaisms survive in compounds even when lost in simplex forms). The compound **\*meord-gifa** may be the "smoking gun."
50: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:262 (note keyword: smoothing)

- Nearby heading: #### §404 (later reference to *meord* in paradigm section, from repo file):

```text
261: - The attested form *mēd* is the standard
262: - No discussion of smoothing or analogical leveling to explain méd vs. meord
263: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:264 (note keyword: smoothing)

- Nearby heading: #### §404 (later reference to *meord* in paradigm section, from repo file):

```text
263: 
264: **User's criticism**: Campbell calls the *eo* a "later change" (implying smoothing post-breaking to get *méd*). But the user argues *meord* is the **archaism** (preserved in compounds?), and *méd* is the innovative smoothed/analogically leveled form. Campbell has the chronology backwards.
265: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| HoggPhonology1992 | single available key for Hogg |
| Luick1914 | single available key for Luick |
| Kaluza1906 | single available key for Kaluza |
| Kilday2024 | single available key for Kilday |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Ringe2006 | surname mention only: Ringe |
| Ringe2017 | surname mention only: Ringe |
| RingeTaylor2014 | explicit year mention (2014) |
| Ringe1984 | surname mention only: Ringe |
| Campbell1959 | explicit year mention (1959) |

