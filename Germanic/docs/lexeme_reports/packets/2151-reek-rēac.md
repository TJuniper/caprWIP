# Evidence packet — 2151 reek / rēac

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2151 | reek | rēac | *ráukiz | *ráukaz | reconstructed_oe | Retargeted 2026-04-30 from attested Anglian rēc (smoothing relic) to reconstructed West Saxon *rēac. The FST cascade already produces rēac from *ráukaz by regular development (R/T vol.2 §6.1: PGmc *au → OE ēa by breaking; preserved before velar in WS); the Anglian-only rēc requires smoothing ēa→ē / _velar (Hogg §5.93), which would regress the WS forms bēacen, hēah, ēage, sēah, tēah. Counterpart written without asterisk per project convention (asterisks confuse the FST cascade input). Etymon previously switched from i-stem *ráukiz to a-stem *ráukaz (Kroonen, p.c.; analogical replacement; cf. Ger. Rauch). See DEV_NOTES.md §17.22 (closure) and dossier-reek-2026.md. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

| REPORT_PATH | STATUS |
| :--- | :--- |
| pilot/reek.md | pilot |

## High-confidence evidence

### Compact derivation trace entry

```md
# reek
PROTO: *ráukaz
EXPECTED: rēac
OUTPUTS: rēac



### Proto-Germanic consonant inheritance

Proto Input: *ráukaz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *ráuka | **Old English**<br>OE Au Fronting: *ráeuka<br>OE Diphthong Leveling: *rēaka<br>PWGmc Final Bare A Loss: *rēak |



### Orthography & surface

Outcome: rēac

NOTE: Retargeted 2026-04-30 from attested Anglian rēc (smoothing relic) to reconstructed West Saxon *rēac. The FST cascade already produces rēac from *ráukaz by regular development (R/T vol.2 §6.1: PGmc *au → OE ēa by breaking; preserved before velar in WS); the Anglian-only rēc requires smoothing ēa→ē / _velar (Hogg §5.93), which would regress the WS forms bēacen, hēah, ēage, sēah, tēah. Counterpart written without asterisk per project convention (asterisks confuse the FST cascade input). Etymon previously switched from i-stem *ráukiz to a-stem *ráukaz (Kroonen, p.c.; analogical replacement; cf. Ger. Rauch). See DEV_NOTES.md §17.22 (closure) and dossier-reek-2026.md.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1437 (exact COUNTERPART)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1435: (Previously listed `*ráukaz → rēac` mismatched against attested Anglian
1436: `rēc`; on 2026-04-30 the cogset was retargeted to reconstructed-WS
1437: `*rēac`, which the FST already produces by regular development. The
1438: row is now a match in the new `reconstructed_oe` `DERIVATION_CLASS`.
1439: See §17.22 closure and `dossier-reek-2026.md`.)
```

#### Germanic/docs/DEV_NOTES.md:34264 (row ID)

- Nearby heading: #### §17.22.1.1  Proto-Germanic reconstruction

```text
34262:   - English: `reek` /riːk/ < \*ráukiz (row 707).
34263:   - German: `Rauch` /raux/ < \*ráukiz (row 706).
34264:   - Old English: `rēc` /reːk/ < \*ráukiz (row 2151, this row).
34265: 
34266: #### §17.22.1.2  Etymology and PIE connections
```

#### Germanic/docs/DEV_NOTES.md:34935 (row ID)

- Nearby heading: #### §17.22.11.3  Recompilation and testing

```text
34933:    ```bash
34934:    python3 tools/oe_mismatch_report.py
34935:    # Verify that row 859 (ID 2151) no longer appears in mismatch list.
34936:    ```
34937: 
```

#### Germanic/docs/DEV_NOTES.md:35561 (exact pair)

- Nearby heading: #### §17.22.13.6.3  FST test: \*ráukaz → rēac

```text
35559: ---
35560: 
35561: #### §17.22.13.6.3  FST test: \*ráukaz → rēac
35562: 
35563: **Input**: `ráukaz` (with a-stem ending -az, no i-trigger).
```

#### Germanic/docs/DEV_NOTES.md:35572 (exact PROTOFORM)

- Nearby heading: #### §17.22.13.6.3  FST test: \*ráukaz → rēac

```text
35570: 
35571: **Internal derivation** (inferred):
35572: 1. **PGmc \*ráukaz** (input, a-stem).
35573: 2. **WGmc sound changes**:
35574:    - \*au → \*éa.
```

#### Germanic/docs/DEV_NOTES.md:35581 (exact pair)

- Nearby heading: #### §17.22.13.6.3  FST test: \*ráukaz → rēac

```text
35579:    - Result: **\*rēac**.
35580: 
35581: **Conclusion**: The FST produces **rēac** (with diphthong ēa, NOT monophthong ē) if the input is \*ráukaz (a-stem). This does NOT match attested OE **rēc** (monophthong).
35582: 
35583: **Follow-up question**: Could **rēac** → **rēc** by later smoothing (ēa → ē / _{velar})?
```

#### Germanic/docs/DEV_NOTES.md:35587 (exact pair)

- Nearby heading: #### §17.22.13.6.3  FST test: \*ráukaz → rēac

```text
35585: - However, smoothing of ēa → ē before -c is NOT universally attested in WS. Examples like **dēad** 'dead' (NOT **\*dēd**) and **rēad** 'red' (NOT **\*rēd**) show that ēa is preserved before dentals/velars in many WS words.
35586: 
35587: **Conclusion**: \*ráukaz → **rēac** → **rēc** by smoothing is POSSIBLE but would require a specific smoothing rule (**ēa → ē / _{c, g}**) in the FST. This rule is not currently implemented (as confirmed by **rēac** output).
35588: 
35589: ---
```

#### Germanic/docs/DEV_NOTES.md:35597 (exact pair)

- Nearby heading: #### §17.22.13.6.4  Summary of FST behavior

```text
35595: | **\*ráukiz**    | **rīeċ**   | **NO**                       | Regular WS i-umlaut; does NOT match rēc    |
35596: | **\*rōkiz**     | **rēċ**    | **YES**                      | Produces rēċ; MATCHES attested form        |
35597: | **\*ráukaz**    | **rēac**   | **NO**                       | Produces diphthong ēa; needs smoothing rule|
35598: 
35599: **Key finding**: The FST can produce **rēċ** (matching attestation) IF the protoform is changed from **\*ráukiz** to **\*rōkiz**.
```

#### Germanic/docs/DEV_NOTES.md:35723 (exact pair)

- Nearby heading: #### **New Option E: Add smoothing rule (ēa → ē / _{velar})**

```text
35721: #### **New Option E: Add smoothing rule (ēa → ē / _{velar})**
35722: 
35723: **Statement**: Keep protoform as **\*ráukaz** (a-stem, no i-trigger), let FST derive **rēac**, then add a smoothing rule **ēa → ē** before velars (c, g) to produce **rēc**.
35724: 
35725: **Justification**:
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

#### Germanic/docs/DEV_NOTES.md:575 (note keyword: breaking)

- Nearby heading: ### Research on blocking medial u → o in labial environments (2026-03-21)

```text
573: - `wuduwe` (WS, with back mutation)
574: - `widwe` (Anglian, syncopated)
575: - `weoduwe` (with breaking)
576: - `widuwana` (Ru.¹ gen.pl., Campbell §218)
577: 
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

#### Germanic/docs/DEV_NOTES.md:741 (note keyword: breaking)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
739: Campbell §353 and §628.5 explain that `*melukz` is a **consonant-stem** (root noun)
740: with paradigm variation:
741: - Nom.sg.: `*melukz` → `meoloc` (with breaking `e → eo`, no syncope)
742: - Gen./dat.sg.: `*milukiz/*miluki` → Anglian `milc` (with i-umlaut and syncope)
743: 
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

#### Germanic/docs/DEV_NOTES.md:1187 (note keyword: breaking)

- Nearby heading: ### The answer: Kroonen (2006), "Gemination and allomorphy in the Proto-Germanic mn-stems"

```text
1185: 3. Kluge's Law then geminated: `*bʰudʰ-n-ós` > `*buttaz`
1186: 4. This created allomorphic paradigms: nom. `*budmōn` ~ gen. `*buttaz`
1187: 5. The paradigm "remained intact until after the breaking up of Proto-Germanic" (2006:22)
1188: 6. Individual daughter languages resolved the allomorphy differently
1189: 7. OE generalized the geminate root to the nominative: `*budmōn` → `*buttmōn` → `*buttma-`
```

#### Germanic/docs/DEV_NOTES.md:1418 (exact COUNTERPART)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1416: **Pipeline:** PGmc → OE FST builds clean; ordered cascade of sound-change stages.
1417: **Coverage:** 379/386 OE matches (**98.2%**), **7 mismatches**, **0 no-output**.
1418: **Mismatch trajectory:** ~300 (Oct 2025) → 291 (Jan 2026) → 256 (Feb 7) → 103 (Mar 8) → 78 (Mar 10) → 14 (start of stress-tier branch) → 13 (Phase 2 of *ḗ tier) → 11 → 10 → 9 → 8 (2026-04-30) → **7 (2026-04-30, after rēc → \*rēac retarget)**.
1419: 
1420: **Intervention summary at close of research phase:**
```

#### Germanic/docs/DEV_NOTES.md:1491 (note keyword: breaking)

- Nearby heading: ## Project Status (as of 2026-03-10)

```text
1489: - **Stem-class corrections**: god (*gudą), door (dor target vs duru)
1490: 
1491: **Remaining work:** 78 mismatches (u-lowering exceptions, breaking, palatalization, consonant clusters, data alignment).
1492: See `docs/analysis/notable_findings.md` for flagged scholarly issues.
1493: 
```

#### Germanic/docs/DEV_NOTES.md:1710 (note keyword: breaking)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1708:   - `consonant_mismatch_other`: 40
1709:   - `final_vowel_missing`: 34
1710:   - `breaking_missing`: 19
1711:   - `breaking_extra_other`: 23
1712:   - `palatalization_missing`: 6
```

#### Germanic/docs/DEV_NOTES.md:1711 (note keyword: breaking)

- Nearby heading: ## A-Restoration Fix (2026-02-06)

```text
1709:   - `final_vowel_missing`: 34
1710:   - `breaking_missing`: 19
1711:   - `breaking_extra_other`: 23
1712:   - `palatalization_missing`: 6
1713:   - `fronting_missing_no_trigger`: 11
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

#### Germanic/docs/DEV_NOTES.md:35182 (exact COUNTERPART)

- Nearby heading: #### **H2: Analogical leveling from the verb \*rēocan 'to smoke'**

```text
35180: #### **H2: Analogical leveling from the verb \*rēocan 'to smoke'**
35181: 
35182: **Statement**: The noun **rēc** was influenced by the related strong verb **rēocan** 'to reek, emit smoke' (OE Class II, with ēo diphthong from PGmc \*eu). The verb's stem **rēoc-** (infinitive), **rēac** (past sg.), **rucon** (past pl.) shows ēo, NOT the au-reflex. Analogy from the verb's present stem (rēoc-) or past singular (rēac, with breaking ēa) might have pulled the noun toward monophthongal ē.
35183: 
35184: **Comparative evidence**:
```

#### Germanic/docs/DEV_NOTES.md:35190 (exact COUNTERPART)

- Nearby heading: #### **H2: Analogical leveling from the verb \*rēocan 'to smoke'**

```text
35188: **OE verb paradigm** (rēocan):
35189: - Infinitive: **rēocan** (< \*reukan-, ēo < \*eu).
35190: - Past sg. 3rd: **rēac** (< \*rauk, but with breaking ēa < \*a + back cons.).
35191: - Past pl.: **rucon** (< \*ruk-, ablaut).
35192: 
```

#### Germanic/docs/DEV_NOTES.md:35194 (exact COUNTERPART)

- Nearby heading: #### **H2: Analogical leveling from the verb \*rēocan 'to smoke'**

```text
35192: 
35193: **Mechanism**: If speakers associated the noun **rēc** with the verb **rēoc-**, they might have:
35194: 1. Reanalyzed the noun as derived from the past singular **rēac** (with ēa), then monophthongized to **ē**.
35195: 2. Leveled the noun to match the verb's infinitive vowel quality (ēo → ē by later smoothing).
35196: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:111 (note keyword: breaking)

- Nearby heading: ### 2.2 Ringe & Taylor (2014), *A Linguistic History of English vol. II* — file `ringe_taylor_linguistic_history_vol2.txt`

```text
110: >
111: > After breaking had run its course, those stressed *æ* which were immediately followed by a single or geminate consonant or **sC-cluster** which was in turn followed by a back vowel became *a* (Luick 1914-40: 152-7, Campbell 1962: 60-2, Hogg 1992: 96-100 [2011: 93-9]). … If fronting could take place before /h/ … plus a back vowel, it should have occurred before any single nonnasal consonant plus a back vowel, even in such a form as *\*dagum* 'days' (dat. pl.), which must therefore have become *\*dægum*. Since the attested form in most OE dialects is *dagum*, it follows that retraction must have occurred subsequently to fronting—and subsequently to breaking …
112: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:304 (note keyword: breaking)

- Nearby heading: ### 2.12 `oe_sound_change_index.md`

```text
303: 
304: > Topic: general retraction / restoration of a; retraction after breaking; conditioning by single/geminate or sC + back vowel.
305: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:456 (note keyword: breaking)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
455: 
456: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut
457: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:57 (note keyword: breaking)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
56: | **OE FORMS** | WS **mēd** ; Anglian-leaning **meord** (dialectal doublet) |
57: | **Preservation locus** | **Dialectal doublet** — not a compound. The lautgesetzlich post-rhotacism + breaking output (*z → r*; *i → eo / _r+C*) is preserved as the Anglian-leaning simplex *meord*, while WS shows the post-z-loss outcome *mēd* (z-loss + comp. lengthening + lowering of long *ī to ē). |
58: | **Primary witnesses for meord** | (i) **BT Supplement** s.v. *meord*: OE Bede 4.17, Schipper 549.7 (form *meorde*, dat.sg.); (ii) **Bright's Anglo-Saxon Reader**, line 12498 of repo OCR — *"þæs him meorde wile ... eadge forgyldan"* (likely *Phoenix*); glossary marks "(dial.)"; (iii) **Hall's Concise** s.v. *meard*: lists *meord* as a real headword. |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:60 (note keyword: breaking)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
59: | **Lautgesetzlich output** | **meord** ✓ (FST currently produces this from `*mizdō`). |
60: | **Sound changes** | Pathway A (rhotacism + breaking): *mizdō → *mizd > *mird > *mird+ breaking → *meord. (Plus apocope.) The WS form *mēd* arises by a different pathway: sporadic z-loss before dentals (Kroonen EDPG p. 376) with compensatory lengthening, *mizd > *mīd > *mēd. |
61: | **DEV_NOTES reference** | §14.518–14.760 (leornian section); §17.24 (full investigation); §17.24.7 (correction trail). Dossiers: `mismatch_dossier_mizdo.md` (with correction banner) and `mismatch_dossier_mizdo_supplement.md` (with correction banner). |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:63 (note keyword: breaking)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
62: | **What was previously claimed (and is wrong)** | The original Case 1 (2026-04-25) claimed *meord* was preserved in a compound *\*meord-gifa*. **No such compound is attested anywhere in BT, BT Supplement, DOE, Hall, Bright, or any other source.** All compounds are uniformly *mēd-* (e.g. *mēd-gyfa*, *mēd-sceatt*). The compound was an agent confabulation. |
63: | **Methodological use** | A textbook case of dialectal-doublet preservation: WS shows the analogical/innovative outcome (or a different sound-change pathway), Anglian-leaning sources preserve the form expected from the regular sequence rhotacism + breaking. Parallel to §17.21 (swustor/swester). The TSV target may legitimately be *meord* if we adopt the dialect-relic-targeting pattern. |
64: | **Precedent / parallels** | §17.21 (swustor → swester, Anglian-relic target adopted); §17.20 (nafola, Anglian glossary witness); §17.16 (spere/speoru paradigm cell). Methodologically equivalent to those — but operating on **dialect** rather than **paradigm cell** or **compound** as the preservation locus. |
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:45 (note keyword: breaking)

- Nearby heading: ### OE target assessment

```text
44: 2. **Anglo-Frisian brightening**: \*a → \*æ before hh
45: 3. **Breaking**: \*æhh → \*eahh
46: 4. **i-Umlaut**: \*eahh → \*ieahh → hiehh (WS palatal diphthong umlaut)
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:48 (note keyword: breaking)

- Nearby heading: ### OE target assessment

```text
47: 
48: The form `hlæhhan` represents stage 2 only (brightening without breaking or
49: umlaut). It's not attested as a standard OE form in R/T. The TSV note says
```

#### Germanic/docs/analysis/four_complex_tsv_items.md:67 (note keyword: breaking)

- Nearby heading: ### Pipeline issues (2 independent problems)

```text
66: 
67: **Problem B: Breaking before palatalized geminate \*xx**
68: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:95 (note keyword: breaking)

- Nearby heading: ### 2.1 Streitberg, *Urgermanische Grammatik* (1896)

```text
94: \*z-retention before a voiced obstruent (and later rhotacism plus
95: breaking, though Streitberg does not spell out the OE-internal
96: breaking). He flags Sievers (PBrB. XVIII.409, not in the repo) as
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:96 (note keyword: breaking)

- Nearby heading: ### 2.1 Streitberg, *Urgermanische Grammatik* (1896)

```text
95: breaking, though Streitberg does not spell out the OE-internal
96: breaking). He flags Sievers (PBrB. XVIII.409, not in the repo) as
97: proposing an alternative account. **The doublet thus has a 130-year
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:117 (note keyword: breaking)

- Nearby heading: ### 2.3 Bülbring, *Altenglisches Elementarbuch* (1902)

```text
116: **Position.** Bülbring treats \*meord\* as the regular outcome via
117: **rhotacism (z→r) before breaking**. He does not, in the passages
118: located, separately discuss *mēd*; his framework is the rhotacism +
```

#### Germanic/docs/analysis/notable_findings.md:1564 (exact PROTOFORM)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1563: **Resolution adopted.** Following Kroonen (p.c.), the PROTOFORM is
1564: switched from i-stem `*ráukiz` to a-stem `*ráukaz` (analogical
1565: replacement of the i-stem; the continental WGmc cognates Du. *rook*
```

#### Germanic/docs/analysis/notable_findings.md:1566 (exact PROTOFORM)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1565: replacement of the i-stem; the continental WGmc cognates Du. *rook*
1566: and Ger. *Rauch* are already a-stems). The FST output of *ráukaz is
1567: the regular `rēac`. To derive the attested *rēc* lautgesetzlich
```

#### Germanic/docs/analysis/notable_findings.md:1579 (exact PROTOFORM)

- Nearby heading: ## 10. OE rēc 'smoke': the missing WS rīec problem

```text
1578: The cognate-set siblings keep their own etyma per row (Du. rook,
1579: Eng. reek, Ger. Rauch all share the cognate headword *ráukaz).
1580: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:24 (note keyword: breaking)

- Nearby heading: # West Saxon vs. Anglian: dialect differences in Old English

```text
23: |---|---|---|
24: | Hogg, *A Grammar of OE*, vol. 1: Phonology | `docs/references/hogg_vol1.txt` | §3 (breaking, BM) ll. 5050–5780; ch. 6 (dialects) ll. 20330–21260 |
25: | Campbell, *Old English Grammar* (1959) | `docs/references/campbell_old_english_grammar.txt` | §§139–169 (breaking, retraction, second fronting) ll. 4360–4940; §§205–233 (BM, smoothing) ll. 6140–6920 |
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:25 (note keyword: breaking)

- Nearby heading: # West Saxon vs. Anglian: dialect differences in Old English

```text
24: | Hogg, *A Grammar of OE*, vol. 1: Phonology | `docs/references/hogg_vol1.txt` | §3 (breaking, BM) ll. 5050–5780; ch. 6 (dialects) ll. 20330–21260 |
25: | Campbell, *Old English Grammar* (1959) | `docs/references/campbell_old_english_grammar.txt` | §§139–169 (breaking, retraction, second fronting) ll. 4360–4940; §§205–233 (BM, smoothing) ll. 6140–6920 |
26: | Ringe & Taylor, *The Development of Old English* (2014) | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | §6.5 (PD + 2nd fronting) ll. 12450–12800; §6.9.2 (smoothing) ll. 17660–17850; §6.9.4 (back umlaut) ll. 18300–18500 |
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:194 (note keyword: breaking)

- Nearby heading: ### Negative environments

```text
193: - Dental-cluster environments: not smoothed; the WS/Anglian distinction
194:   there is governed by breaking and back mutation, not smoothing.
195: - Smoothing does *not* operate when the velar was lost before back vowels:
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:156 (note keyword: Anglian)

- Nearby heading: ## §3. The fault-line: `-un > -on` for stem-`u` verbs is analogical

```text
155:   Brunner §364.2 Anm. 4). For the two specific verbs we care about
156:   here, the early Anglian/Mercian witnesses simply do not contain
157:   a finite 3 pl. pret. token — the verb is unattested in those
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:227 (note keyword: breaking)

- Nearby heading: ### §4.2 Phonological assessment

```text
226: * **`bēag` ← `*baug`** (1/3 sg. pret.): pure `*au > *ǣa > ēa` (the
227:   monophthongisation/breaking sequence in OE; Campbell §131,
228:   Brunner §38–39). No competing analogical pressure on this cell:
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:399 (note keyword: breaking)

- Nearby heading: ### §7.1 *būgan* (row 1962)

```text
398: * Cascade clean-ness: requires only the regular `*au > ēa`
399:   monophthongisation/breaking sequence. No interaction with
400:   unstressed-vowel lowering, no interaction with stem-`u` harmony,
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

#### Germanic/docs/dossiers/un-to-on-chronology.md:255 (note keyword: breaking)

- Nearby heading: ### Ringe & Taylor §6.9.6, §6.9.4

```text
254: > class II weak verbs in early WS … and Kentish … suggests that **by
255: > 900 the contrast between the unstressed back vowels was breaking
256: > down in closed final syllables in Kentish and in all positions,
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:940 (note keyword: breaking)

- Nearby heading: ### B.5 Hogg, in CHEL Vol. 1 (1992 chapter)

```text
939: > [back mutation] involved exactly the same diphthongisation
940: > process [as breaking], except that in the later change only
941: > short vowels are diphthongised, i.e., /i/ > /io/, /e/ > /eo/,
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1708 (note keyword: breaking)

- Nearby heading: ### D.1 Open vs. closed syllable conditioning

```text
1707: 
1708: > "by 900 the contrast between the unstressed back vowels was breaking
1709: > down in **closed final syllables** in Kentish and in all positions,
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1960 (note keyword: breaking)

- Nearby heading: ### D.4 Synthesis and FST recommendation

```text
1959: **Surprising finding worth flagging.** The proposed change is *not*
1960: "making the FST tolerate widow at the cost of breaking strong verbs."
1961: It is "making the FST output the philologically correct early-OE
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| reek | rēc | inh | template:inh | reek |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1435 (exact pair)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1433: * `*wúllō → woll` (expected `wull`) — `wontfix: u_lowering_near_labial`
1434: 
1435: (Previously listed `*ráukaz → rēac` mismatched against attested Anglian
1436: `rēc`; on 2026-04-30 the cogset was retargeted to reconstructed-WS
1437: `*rēac`, which the FST already produces by regular development. The
```

#### Germanic/docs/DEV_NOTES.md:1439 (concept name)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1437: `*rēac`, which the FST already produces by regular development. The
1438: row is now a match in the new `reconstructed_oe` `DERIVATION_CLASS`.
1439: See §17.22 closure and `dossier-reek-2026.md`.)
1440: 
1441: **The research phase is closed.** Each remaining mismatch has a fully
```

#### Germanic/docs/DEV_NOTES.md:34229 (concept name)

- Nearby heading: ## §17.22  *ráukiz → rēc / rīeċ: the 'reek' (smoke) mismatch — palatalization and i-umlaut dialect variation

```text
34227: 
34228: *End of §17.21 supplement (§17.21.10-§17.21.12).*
34229: ## §17.22  *ráukiz → rēc / rīeċ: the 'reek' (smoke) mismatch — palatalization and i-umlaut dialect variation
34230: 
34231: **Date**: 2025-04-26 (this session).
```

#### Germanic/docs/DEV_NOTES.md:34232 (concept name)

- Nearby heading: ## §17.22  *ráukiz → rēc / rīeċ: the 'reek' (smoke) mismatch — palatalization and i-umlaut dialect variation

```text
34230: 
34231: **Date**: 2025-04-26 (this session).
34232: **Lexeme**: PGmc *ráukiz (m. i-stem) 'smoke, vapor, reek' → OE rēc (target) vs. FST rīeċ (current output).
34233: **Mismatch type**: Two phonological discrepancies: (1) vowel quality (ē vs. īe), and (2) palatalization (velar c vs. palatal ċ).
34234: **TSV row**: 859 (ID 2151), cognate family ID 198 ('reek').
```

#### Germanic/docs/DEV_NOTES.md:34234 (row ID)

- Nearby heading: ## §17.22  *ráukiz → rēc / rīeċ: the 'reek' (smoke) mismatch — palatalization and i-umlaut dialect variation

```text
34232: **Lexeme**: PGmc *ráukiz (m. i-stem) 'smoke, vapor, reek' → OE rēc (target) vs. FST rīeċ (current output).
34233: **Mismatch type**: Two phonological discrepancies: (1) vowel quality (ē vs. īe), and (2) palatalization (velar c vs. palatal ċ).
34234: **TSV row**: 859 (ID 2151), cognate family ID 198 ('reek').
34235: **Cross-references**: §17.16 (spere — oblique-cell methodology), §17.20 (tang — Anglian target precedent), §17.21 (swester — 2D cell × attested-form search).
34236: 
```

#### Germanic/docs/DEV_NOTES.md:34252 (concept name)

- Nearby heading: #### §17.22.1.1  Proto-Germanic reconstruction

```text
34250: 1. Kroonen reconstructs **\*rauki-** (i-stem base), which in masculine nominative singular would be **\*raukiz** (with the i-stem NomSg ending *-iz).
34251: 2. OE is cited as **réc** (with macron, indicating long ē), NOT rīec or rīeċ.
34252: 3. The derivation is from the strong verb **\*reukan-** 'to smoke' (cf. ON rjúka, OE rēocan 'to reek, emit smoke').
34253: 4. The Germanic distribution includes ON, OFris, OS, OHG, showing consistent *rauk- root across North and West Germanic.
34254: 
```

#### Germanic/docs/DEV_NOTES.md:34257 (row ID)

- Nearby heading: #### §17.22.1.1  Proto-Germanic reconstruction

```text
34255: **Orel *Handbook of Germanic Etymology*** (2003, p. 295 of `orel_handbook_germanic_etymology.txt`): not indexed in OCR sample, but Orel's coverage is consistent with Kroonen's reconstruction.
34256: 
34257: **TSV entry** (row 859, ID 2151):
34258: - PROTOFORM: `*ráukiz` (with acute accent marking stress on first syllable).
34259: - Target: `rēc` (OE).
```

#### Germanic/docs/DEV_NOTES.md:34260 (concept name)

- Nearby heading: #### §17.22.1.1  Proto-Germanic reconstruction

```text
34258: - PROTOFORM: `*ráukiz` (with acute accent marking stress on first syllable).
34259: - Target: `rēc` (OE).
34260: - Cognates in row family (ID 198, 'reek'):
34261:   - Dutch: `rook` /roːk/ < \*ráukiz (row 708).
34262:   - English: `reek` /riːk/ < \*ráukiz (row 707).
```

#### Germanic/docs/DEV_NOTES.md:34781 (row ID)

- Nearby heading: #### Option B: Target WS rīec, change TSV target

```text
34779: 
34780: **Scope**:
34781: - **TSV changes**: Change row 2151 (ID 859) target from `rēc` to `rīec`.
34782: - **Regressions**: None (FST behavior unchanged).
34783: - **Methodological consistency**: ✗ Contradicts §17.20/§17.21 precedent (which target Anglian, not WS).
```

#### Germanic/docs/DEV_NOTES.md:34911 (row ID)

- Nearby heading: #### §17.22.11.2  TSV changes

```text
34909: **File**: `Germanic/data/germanic-aligned-final.tsv`
34910: 
34911: **Row**: 859 (ID 2151, PROTOFORM `*ráukiz`, current target `rēc`).
34912: 
34913: **Change**: NONE (target is already correct). Optionally, update the NOTE field:
```

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:44 (note keyword: breaking)

- Nearby heading: ### The core problem

```text
43: 1. **Z-loss with rhotacism**: `*mizdō` → `*mirdō` (medial *z → *r in VzC context)
44: 2. **Breaking**: `*mirdō` → `*meordō` (breaking of *i → *eo before r+C)
45: 3. **Weak tail**: `*meordō` → `meord` (loss of final vowel in heavy ō-stem)
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:47 (note keyword: breaking)

- Nearby heading: ### The core problem

```text
46: 
47: However, the TSV target is `mēd`, a monophthong with no breaking diphthong and no medial /r/.
48: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:82 (note keyword: breaking)

- Nearby heading: #### Form A: `mēd` (monophthong, no /r/)

```text
81: 
82: **Paradigm**: The oblique forms show **mēde** (gen./dat./acc.sg.) with no trace of /r/ or breaking diphthong in any cell.
83: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:25 (note keyword: breaking)

- Nearby heading: # Supplement to Mismatch Dossier: *mízdō 'reward, wage'

```text
24: >
25: > The "Kroonen footnote" attributed to web search at §3.2 ("breaking does not
26: > take place because *i precedes a single dental") **does not appear in Kroonen's
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:40 (note keyword: breaking)

- Nearby heading: ## 1. Charge of this supplement

```text
39: The original dossier (2026-04-25) concluded provisionally that:
40: - FST output `meord` is lautgesetzlich (via breaking of *i before r+C)
41: - Attested OE `mēd` is analogically smoothed
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:49 (note keyword: breaking)

- Nearby heading: ## 1. Charge of this supplement

```text
48: 
49: 2. **Disagreement with Campbell §123 fn.2**: Campbell states "the eo of meord, leornian is from e by a **later change**" (implying smoothing happened after breaking). The user argues that the -eo- is instead an **archaism** preserved in compound, following the **Watkins principle** (archaisms survive in compounds even when lost in simplex forms). The compound **\*meord-gifa** may be the "smoking gun."
50: 
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| HoggPhonology1992 | author + year mention (Hogg 1992) |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| SieversBrunner1965 | single available key for Sievers |
| Luick1914 | single available key for Luick |
| BrightCassidyRingler1971 | single available key for Bright |
| Streitberg1896 | single available key for Streitberg |
| KlugeSeebold2011 | explicit year mention (2011) |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Ringe2006 | explicit year mention (2006) |
| Ringe2017 | surname mention only: Ringe |
| RingeTaylor2014 | explicit year mention (2014) |
| Ringe1984 | surname mention only: Ringe |
| Campbell1959 | explicit year mention (1959) |
| Kroonen2011 | explicit year mention (2011) |
| Kroonen2006 | explicit year mention (2006) |

