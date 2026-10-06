# Evidence packet — 2189 sieve / sife

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2189 | sieve | sife | *síbaz | *síbi | early_analogy | - | Kroonen 2013:429 gives only *sebjō- (ja-stem fem. 'kinship' > OE sibb); 'sieve' is absent. Consensus reconstruction PGmc *sibi- (neuter i-stem, orig. s-stem *sib-iz, PIE *seib-/*seip- 'to drip, strain', Pokorny IEW I 889–890, 894). Kluge/Seebold (s.v. Sieb) WGmc *sibi- n.; Brunner §288 Anm. (orig. s-stem absorbed into i-decl.); Campbell §§608–609 (short neut. i-stem, cf. spere, gedyre). Early Corpus Glossary form sibi (Campbell §444, archaic ⟨b⟩) confirms the *-i ending. Cannot be *sibja- (would feed WGG → OE **sibb, cf. OE sibb 'kinship' < *sibjō). Cannot be *sibaz a-stem (would give OE **sif). PROTOFORM corrected 2026-04-24 from *síbaz to *síbi per §17.15 three-agent research (Kroonen, Orel, Kluge, Brunner, Campbell, R/T, Hogg, Fulk, Pokorny). |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# sieve
PROTO: *síbi
EXPECTED: sife
OUTPUTS: sife



### Proto-Germanic consonant inheritance

Proto Input: *síbi

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>PGmc B Allophony: *síβi<br>OE Med Unstressed I Lowering1: *síβe |



### Orthography & surface

Outcome: sife
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10413 (exact pair)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10411: | 2026-04-24 | 33 | -1 | 0c6ab468 | strīeġan: OEJStrengtheningAfterFrontDiphthong (§17.10.36-q3) |
10412: | 2026-04-24 | 32 | -1 | 6a2bbda2 | cwedu: PROTOFORM *kwíθuz → *kwéðuz (§17.14) |
10413: | 2026-04-24 | 31 | -1 | 5fa587ab | sife: PROTOFORM *síbaz → *síbi (§17.15) |
10414: | 2026-04-24 | 30 | -1 | 75b8da0d | speoru: short-diphthong weight refactor; *spéru NApl (§17.17) |
10415: | 2026-04-25 | 29 | -1 | 9ccbe617 | þistles: paradigm-cell switch *þístilaz → GenSg (§17.18) |
```

#### Germanic/docs/DEV_NOTES.md:28618 (exact PROTOFORM)

- Nearby heading: ### §17.15.7  FST probe (pre-change)

```text
28616: All four candidate inputs (bare/with-*z, bare/acute) yield `sife`
28617: directly. No rule changes required. The TSV PROTOFORM encoding
28618: convention (acute on stressed vowel, no final *-z) selects **`*síbi`**
28619: as the canonical form.
28620: 
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:5374 (exact COUNTERPART)

- Nearby heading: ### Applying the Theory to Our Data

```text
5372: | live | \*libēþi | -b- | **labial** | **blocking** | lifeþ ✓ |
5373: | widow | \*widuwōn | -d-w- | coronal + **labial** | **blocking** | widuwe ✓ |
5374: | sieve | \*sibaz | -b- | **labial** | **blocking** | sife ✓ |
5375: 
5376: The pattern is striking: **every form that retained \*i has a velar or labial
```

#### Germanic/docs/DEV_NOTES.md:5413 (exact COUNTERPART)

- Nearby heading: # per Howell & Salmons (1997), but the current implementation does not do so.

```text
5411: |---------|-------|------------|-------------|------------|
5412: | fish | \*fiskăz | fesċ | **fisċ** | velar \*k |
5413: | sieve | \*sibăz | sef | **sife** | labial \*b |
5414: | liver | \*librō | lefer | **lifer** | labial \*b |
5415: | live (3sg) | \*libēþi | lefeþ | **lifeþ** | labial \*b |
```

#### Germanic/docs/DEV_NOTES.md:17460 (exact COUNTERPART)

- Nearby heading: #### 12. Fulk vs. Our Implementation of `*i → *e` (2026-04-12)

```text
17458: |-------|-----------|------|-----------------|----------|------------|-------------|----------|
17459: | `*libēθi` | `*l-i-b-ē-θ-i` | labial *b | **?** (not explicit) | blocked | `lifeþ` | `lifeþ` | ✓ |
17460: | `*sibăz` | `*s-i-b-ă-z` | labial *b | **?** (not explicit) | blocked | `sif` | `sife` | ✓ |
17461: 
17462: Both test cases show that our **stricter** coronal-only rule produces the correct OE forms.
```

#### Germanic/docs/DEV_NOTES.md:17470 (exact COUNTERPART)

- Nearby heading: #### 12. Fulk vs. Our Implementation of `*i → *e` (2026-04-12)

```text
17468: Our coronal-only coda restriction appears to be **empirically correct for OE**, even if it
17469: is **stricter than Fulk's explicit formulation**. Fulk only mentions *j and nasal+C as
17470: blockers, but the OE evidence (`lifer`, `sife`) suggests labials also block. This is
17471: consistent with Howell & Salmons (1997) who argue for a place feature hierarchy where
17472: labials block more strongly than coronals.
```

#### Germanic/docs/DEV_NOTES.md:28521 (exact COUNTERPART)

- Nearby heading: ## §17.15  sife PROTOFORM research (row 1003 fix)

```text
28519: affected since PGmc *\*kweðuz* is unique to this TSV row).
28520: 
28521: ## §17.15  sife PROTOFORM research (row 1003 fix)
28522: 
28523: ### §17.15.1  Problem
```

#### Germanic/docs/DEV_NOTES.md:28623 (exact PROTOFORM)

- Nearby heading: ### §17.15.8  TSV change

```text
28621: ### §17.15.8  TSV change
28622: 
28623: Row 1003 PROTOFORM: `*síbaz` → **`*síbi`**
28624: Row 1003 ALIGNMENT: `s ɪ v ( - - )` → `s ɪ v ( - )` (one final slot
28625: rather than two, matching the *spéru → spere* convention at row 1070
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| sieve | sife | inh | template:inh | sieve |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2324 (concept name)

- Nearby heading: ### KIT sweep (WIP)

```text
2322: - Fed the KIT bucket through the same dockered `flookup` harness (`python3 - <<'PY' …`) after filtering out diphthongs (`aɪ/eɪ/ɔɪ`). The remaining 35 entries are the genuine `{ɪ}` cases headed by `fish/give/six/will` alongside the `{ɪə}` + post-vocalic /r/ cohort (`beard/bier/deer/spear/ year`, etc.).
2323: - Updated `EnglishSandboxCoreVowelRules` so short `{*i}` finally drops its star and enters the plain alphabet, and extended `EnglishSandboxShortVowelSplit` with `{i}`→`{ɪ}` rewrites in closed syllables / word-final contexts. This keeps the KIT conditioning in the same stage as the `{*e}`/{`*u`} splits instead of leaving `{*i}` untouched.
2324: - The attested-form harness still lands at 179/376 successes (KIT bucket = 35) because the stubborn cases need post-vocalic /r/ smoothing (`{ɪ}`→`{ɪə}` before the new `EnglishSandboxPostVocalicRLoss`) or suffixal analogies (`sieve/singe/timber`). Logged them here so the next pass can target `{ɪə}` outputs without sacrificing the `{bəʊn}/{fʊt}` improvements we just landed.
2325: 
2326: ## 2025-12-04
```

#### Germanic/docs/DEV_NOTES.md:28526 (concept name)

- Nearby heading: ### §17.15.1  Problem

```text
28524: 
28525: Row 1003 in `germanic-aligned-final.tsv` had PROTOFORM `*síbaz`
28526: (masc. a-stem) with COUNTERPART `sife` 'sieve'. The FST correctly
28527: derives `*síbaz → sif` (a-stem neut./masc. nom.sg., with loss of
28528: final *-az), but the expected OE attested form is `sife` (with final
```

#### Germanic/docs/DEV_NOTES.md:28557 (concept name)

- Nearby heading: ### §17.15.3  Etymological consensus

```text
28555: | Brunner §288 Anm. | PGmc *sib-iz > i-decl. | orig. s-stem | absorbed into i-stem class (Brunner §263.2) |
28556: | Campbell §§608–609 | WGmc *sibi (short neut. i-stem) | i-stem neut. | grouped with *spere*, *gedyre*, *orlege* |
28557: | Kroonen 2013 | (no headword for 'sieve') | — | lists only *\*sebjō-* 'kinship' (p. 429, ja-stem, → OE sibb), *\*sēdla-* 'sieve' (p. 433, → ON sáld, unrelated root) |
28558: 
28559: **PIE root**: *seib-/*seip- 'to pour, drip, ooze, filter' (Pokorny IEW
```

#### Germanic/docs/DEV_NOTES.md:28572 (concept name)

- Nearby heading: ### §17.15.4  Why NOT *sibja- (ja-stem neut.)

```text
28570: peace' → OE sibb (fem. jō-stem, Kroonen 2013:429; Ringe & Taylor
28571: 2014 §3.2.4). The minimal pair OE *sibb* 'kinship' vs OE *sife*
28572: 'sieve' is a diagnostic:
28573: 
28574: - sibb ← *sibjō- → WGG *sibbjō → *sibbu → sibb  (geminate survives)
```

#### Germanic/docs/DEV_NOTES.md:28664 (exact pair)

- Nearby heading: ### §17.16.1  Problem

```text
28662: mismatches the target `spere`. This is the last `spere`-bucket
28663: `final_vowel_missing__weak_noun_like` case, directly parallel at
28664: the surface to §17.15 *sife* (`*síbaz` → `*síbi`).
28665: 
28666: ### §17.16.2  Research methodology
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2013 | author + year mention (Kroonen 2013) |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| Fulk2018 | single available key for Fulk |
| Orel2003 | single available key for Orel |
| Seebold1970 | single available key for Seebold |
| KlugeSeebold2011 | single available key for Kluge |
| Pokorny1959 | single available key for Pokorny |
| HowellSalmons1988 | single available key for Salmons |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |

