# Evidence packet — 2011 find / fundene

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2011 | find | fundene | *fínθaną | *fúnðanǭ | late_analogy | Paradigm-cell acc.sg.m. of strong past ptc, attested (Bosworth-Toller s.v. findan: "Beón i hergeata ww fundene, 414, 4 note"; cf. Hall s.v. tō-fundennes). Regular Verner *ð → *d, intervocalic *n triggers medial fronting *-an- → *-en-, bimoric *-ǭ → -e. Nom.sg. funden is analogical (Campbell §334, Luick §301,3, Brunner §366 Anm. 3). See DEV_NOTES §17.10.30–32. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# find
PROTO: *fúnðanǭ
EXPECTED: fundene
OUTPUTS: fundene



### Proto-Germanic consonant inheritance

Proto Input: *fúnðanǭ

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc Dental Hardening: *fúndanǭ<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Unstressed Fronting Early: *fúndænǭ<br>OE Unstressed Long Vowel Shortening: *fúndænæ<br>OE Unstressed AE Merger: *fúndene |



### Orthography & surface

Outcome: fundene

NOTE: Paradigm-cell acc.sg.m. of strong past ptc, attested (Bosworth-Toller s.v. findan: "Beón i hergeata ww fundene, 414, 4 note"; cf. Hall s.v. tō-fundennes). Regular Verner *ð → *d, intervocalic *n triggers medial fronting *-an- → *-en-, bimoric *-ǭ → -e. Nom.sg. funden is analogical (Campbell §334, Luick §301,3, Brunner §366 Anm. 3). See DEV_NOTES §17.10.30–32.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:7318 (row ID)

- Nearby heading: ### Resolution (2026-03-11) — FULLY LAUTGESETZLICH

```text
7316: **Changes made:**
7317: 
7318: 1. **TSV** (row 2011): Using true PGmc form `*funðanăz → funden`
7319: 
7320: 2. **FST** (`PWGmcDentalHardening`): New rule for `*ð → *d`
```

#### Germanic/docs/DEV_NOTES.md:25148 (row ID)

- Nearby heading: ### Why the previous "fix" wasn't really a fix

```text
25146: A 2026-04-22 migration (commit `c386dc0`, "phase 1d-β partial: TSV ă→a
25147: migration") bulk-migrated 1282 weak-tail cells `{*ă} → {*a}`, including
25148: row 2011. Before that migration the participle ending in row 2011 was
25149: `-ăz` (breve), which `PWGmcFinalBareALoss` (body `{*a} -> 0 || _ .#.`)
25150: does not match. That made the rule appear to work, but *only* because
```

#### Germanic/docs/DEV_NOTES.md:25157 (row ID)

- Nearby heading: ### Why the previous "fix" wasn't really a fix

```text
25155: and the migration, which was a legitimate simplification, exposed it.
25156: 
25157: We should *not* re-introduce the breve on row 2011. There is only one
25158: unaccented schwa-like low vowel at this stage, and we should spell it
25159: one way.
```

#### Germanic/docs/DEV_NOTES.md:25291 (row ID)

- Nearby heading: #### Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)

```text
25289: #### Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)
25290: 
25291: Replace the TSV PROTOFORM on row 2011 with an inflected cell in which
25292: the stem-final nasal is genuinely heterosyllabic. Candidate cells for
25293: the strong a-stem adjective/participle paradigm:
```

#### Germanic/docs/DEV_NOTES.md:25360 (row ID)

- Nearby heading: ### Decision

```text
25358: ### Decision
25359: 
25360: **Adopt Path α**: TSV PROTOFORM change on row 2011 from `*fúnðanaz` to
25361: `*fúnðanǭ` (strong adj. acc.sg.m.n.). Rule-level chronology and
25362: nasalisation unchanged for now. This is the most Lautgesetzlich option
```

#### Germanic/docs/DEV_NOTES.md:25380 (row ID)

- Nearby heading: ### Verification plan for Path α

```text
25378: 1. Revert the §17.10.28-inspired rule-body change (if any was applied).
25379:    Current rule body on line 2119 remains `_ {*n} .#.` from main.
25380: 2. Edit TSV row 2011: PROTOFORM `*fúnðanaz` → `*fúnðanǭ`.
25381: 3. Trace `*fúnðanǭ` — expect *a in `-an-` stays through heavy apocope
25382:    (because the following *ǭ is not yet gone at SecondaryNasalization
```

#### Germanic/docs/DEV_NOTES.md:25752 (exact pair)

- Nearby heading: ### §17.10.32 Case 4 — Path α implementation result: `*fúnðanǭ → fundene`

```text
25750: — end §17.10.31
25751: 
25752: ### §17.10.32 Case 4 — Path α implementation result: `*fúnðanǭ → fundene`
25753: 
25754: **Change applied** (TSV row 2011):
```

#### Germanic/docs/DEV_NOTES.md:25774 (exact COUNTERPART)

- Nearby heading: ### §17.10.32 Case 4 — Path α implementation result: `*fúnðanǭ → fundene`

```text
25772: 
25773: ```
25774: fúnðanǭ → fundene
25775: ```
25776: 
```

#### Germanic/docs/DEV_NOTES.md:25784 (exact COUNTERPART)

- Nearby heading: ### §17.10.32 Case 4 — Path α implementation result: `*fúnðanǭ → fundene`

```text
25782: 5. UnstressedLongVowelShortening: `*ǭ → *æ` (bimoric)
25783: 6. AEMerger: `*æ → *e`
25784: 7. OldEnglishRemoveStars: `f u n d e n e` → `fundene`
25785: 
25786: The medial fronting (the philologically important step — Campbell §334,
```

#### Germanic/docs/DEV_NOTES.md:25792 (exact COUNTERPART)

- Nearby heading: ### §17.10.32 Case 4 — Path α implementation result: `*fúnðanǭ → fundene`

```text
25790: `*-ǭ → -e`, e.g. `tunge`).
25791: 
25792: **Why target = `fundene`, not `funden`**
25793: 
25794: `fundene` is itself a directly attested Old English form: it is the
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10408 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10406: | 2026-04-15 | 38 | -1 | 6acac2a2 | weak class II 3sg: two-stage *ō shortening (§15.8) |
10407: | 2026-04-21 | 37 | -1 | dab140a9 | §17 refactor baseline confirmed post-prosodic-tier merge |
10408: | 2026-04-23 | 36 | -1 | aa241224 | findan: PP target switch → fundene (§17.10.31, Case 4 Path α) |
10409: | 2026-04-23 | 35 | -1 | 5e733bb3 | wīþiġ: PROTOFORM *wīθijaz → *wīθagą (§17.10.35, Campbell -ag- suffix) |
10410: | 2026-04-23 | 34 | -1 | 29f4e924 | hīeġ: OEAwwjResolution *aw(w)+*j → *au+*j (§17.10.36 stages 1–2) |
```

#### Germanic/docs/DEV_NOTES.md:25295 (exact PROTOFORM)

- Nearby heading: #### Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)

```text
25293: the strong a-stem adjective/participle paradigm:
25294: 
25295: - acc.sg.m. `*fúnðanǭ` — heavy acc.sg. ending `*-anǭ`. After
25296:   `OEHeavySyllableNasalApocope` deletes the final `*ǭ` (light-final
25297:   apocope after consonant cluster `*n*d*...`), only `*funden` remains.
```

#### Germanic/docs/DEV_NOTES.md:25313 (exact PROTOFORM)

- Nearby heading: #### Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)

```text
25311: produce the analogical outcome from the nom.sg. protoform.
25312: 
25313: **Recommendation:** use acc.sg.m. `*fúnðanǭ`. This requires a trace
25314: to confirm that `*ǭ` is present at the right stages and is stripped
25315: by heavy apocope, but it is mechanically parallel to the acc.sg.
```

#### Germanic/docs/DEV_NOTES.md:25361 (exact PROTOFORM)

- Nearby heading: ### Decision

```text
25359: 
25360: **Adopt Path α**: TSV PROTOFORM change on row 2011 from `*fúnðanaz` to
25361: `*fúnðanǭ` (strong adj. acc.sg.m.n.). Rule-level chronology and
25362: nasalisation unchanged for now. This is the most Lautgesetzlich option
25363: — it models exactly what Campbell §334 says happened — and requires no
```

#### Germanic/docs/DEV_NOTES.md:25381 (exact PROTOFORM)

- Nearby heading: ### Verification plan for Path α

```text
25379:    Current rule body on line 2119 remains `_ {*n} .#.` from main.
25380: 2. Edit TSV row 2011: PROTOFORM `*fúnðanaz` → `*fúnðanǭ`.
25381: 3. Trace `*fúnðanǭ` — expect *a in `-an-` stays through heavy apocope
25382:    (because the following *ǭ is not yet gone at SecondaryNasalization
25383:    time), fronts to *æ → *e at UnstressedAFronting, and emerges as
```

#### Germanic/docs/DEV_NOTES.md:25541 (exact PROTOFORM)

- Nearby heading: #### 8. Consequence for §17.10.29

```text
25539: 
25540: §17.10.29's decision to adopt Path α (paradigm-cell PROTOFORM
25541: substitution, using `*fúnðanǭ` acc.sg.m. or an equivalent oblique
25542: cell) is the only lautgesetzlich choice available to us. Path β
25543: (adding a structural secondary-nasalisation rule that would make
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| find | findan | inh | template:inh | find |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:86 (concept name)

- Nearby heading: ### Summary of the scholarly literature

```text
84: **Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.
85: 
86: **R/T (§2.3.1, pp.32-33 / our OCR pp.47-48)** agree these are genuine exceptions but reach a different conclusion about paradigmatic leveling. They find it "implausible" for a-stem nouns, arguing that the only case-forms with high-vowel suffixes are functionally marginal: inst.sg. *-u, dat.pl. *-umaz, inst.pl. *-umiz. They conclude: "We do not really know why *u failed to lower in these forms."
87: 
88: ### Could we use paradigm forms? (Why we decided not to)
```

#### Germanic/docs/DEV_NOTES.md:745 (concept name)

- Nearby heading: ### The milk problem: `*melukz` → `meoloc` (expected `meolc`)

```text
743: 
744: R/T §6.6.4 (p.253): "The usual WS form of 'milk' is `meolc < meoluc < *meluk`... 
745: However, in Anglian dialects we find Merc., North. `milc` 'milk'... It would seem 
746: reasonable to suggest that the form with *i* was generalized from the gen., dat. sg."
747: 
```

#### Germanic/docs/DEV_NOTES.md:789 (concept name)

- Nearby heading: ### The nettle problem: `*natilōn` → `nætele` (expected `netle`)

```text
787: R/T §6.7.4 (p.275-276): "The most obvious pattern is very specific: unstressed *i in
788: open syllables is often syncopated **next to l**. In addition to the forms mentioned
789: in the preceding paragraph, we find syncope in some inflected forms of `fetel` 'belt'
790: (though apparently not of `cytel, cetel` 'kettle'), in `netle ~ netele` 'nettle',
791: and in North. dat. sg. `cryple` 'cripple'..."
```

#### Germanic/docs/DEV_NOTES.md:4150 (concept name)

- Nearby heading: ### Critical finding: North. lifed as archaism

```text
4148: R/T vol.2 §7.1.5 (p.364) note:
4149: > "Except for late North. pres. indic. 3sg. **lifed**, which must be an **archaism** because the
4150: > verb has largely been remodelled as a class II weak verb in that dialect, we find only class II
4151: > pres. indic. 2, 3sg. and iptv. sg. forms"
4152: 
```

#### Germanic/docs/DEV_NOTES.md:4181 (concept name)

- Nearby heading: ### Are Anglian lifgu, lifgaþ, lifgende archaic?

```text
4179: > relics pres. indic. libis, libit, past libita presuppose a paradigm in which some forms were
4180: > identical with class I weak forms—i.e. exhibited a palatalized geminate. **The Anglian forms
4181: > are innovations**, and we must find a way to account for them..."
4182: 
4183: > "The only plausible source of /j/ in these verb forms is the source of /j/ in weak class II...
```

#### Germanic/docs/DEV_NOTES.md:6260 (concept name)

- Nearby heading: ### What to do

```text
6258: not predictable from the proto-form. Accept the mismatch.
6259: 
6260: **Option C: Find a different paradigm cell**
6261: Check whether any other case form both:
6262: - Had an ending that triggered umlaut
```

#### Germanic/docs/DEV_NOTES.md:25761 (exact COUNTERPART)

- Nearby heading: ### §17.10.32 Case 4 — Path α implementation result: `*fúnðanǭ → fundene`

```text
25759: | PROTO      | `*fúnðanaz`   | `*fúnðanǭ`     |
25760: | TOKENS     | `f u n d e n` | `f u n d e n e`|
25761: | OE target  | `funden`      | `fundene`      |
25762: 
25763: **FST grammar extension**: `pgrmWeakTailVowel` in `Germanic/fsts/germanic.txt`
```

#### Germanic/docs/DEV_NOTES.md:26040 (exact pair)

- Nearby heading: #### Chosen approach: paradigm-cell switch for 4/5 (per §17.10.32)

```text
26038: #### Chosen approach: paradigm-cell switch for 4/5 (per §17.10.32)
26039: 
26040: The strategy used for §17.10.32 (`*fúnðanǭ → fundene` instead of
26041: `*fúnðanaz → funden`) applies exactly here for 4/5 cases. The OE
26042: **gen.sg.** of these masculine a-stems has the suffix `*-is` (PIE
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:184 (concept name)

- Nearby heading: ### 2.3 Hogg / *Cambridge History of the English Language* vol. I — file `hogg_vol1.txt`

```text
183: 
184: > Class VI verbs should, because of the sound change of restoration of *a* (see §3.3.3.1), have varied between /a/ and /æ/ in the present tense and the past participle, but in West Saxon at least /a/ was generalised throughout the present and was normal in the past participle. Hence we find *faran* ~ *for* ~ *foron* ~ *færen* 'go'.
185: 
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:373 (concept name)

- Nearby heading: ## Summary and Conclusion

```text
372: 
373: 3. **The methodology is consistent**: We apply a "2D search" (proto-form cell × attested OE form) to find the longest unbroken chain of lautgesetzlich sound changes, and target *that* combination, even if it is not the most frequent nominative singular.
374: 
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:390 (concept name)

- Nearby heading: ### 2.13 Ringe & Taylor, *The Development of Old English* (vol. 2, 2014)

```text
389: 
390: > "Though the usual outcome is clearly r, we occasionally find loss of
391: > *z with compensatory lengthening of the preceding vowel, and it is
```

#### Germanic/docs/analysis/meord_med_chronological_review.md:990 (concept name)

- Nearby heading: ## 8. Flagged unsupported claims in earlier project notes

```text
989: 4. **`mismatch_dossier_mizdo.md` claim that "Hogg §2.66" specifically
990:    covers OE rhotacism** — the wording quoted matches what I find at
991:    `hogg_vol1.txt:2226`, but I cannot verify the section number
```

#### Germanic/docs/analysis/notable_findings.md:256 (concept name)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
255: - **R/T (vol.2 §2.3.1, pp.32-33):** Agree these are genuine exceptions.
256:   Find paradigmatic leveling "implausible" for a-stem nouns because the
257:   only paradigm cells with high-vowel suffixes (inst.sg. \*-u, dat.pl. \*-umaz)
```

#### Germanic/docs/analysis/notable_findings.md:746 (concept name)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
745: because of later morphologically motivated changes, affecting alternations
746: of the type fæt ~ fatu, we do find in Old English minimal pairs such as
747: fare 'journey' dat.sg.masc. vs. fare 'journey' dat.sg.fem." But he
```

#### Germanic/docs/analysis/notable_findings.md:1182 (concept name)

- Nearby heading: ### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

```text
1181: **On chronology:** "Now since the very 'sporadic' lowering of \*i certainly is
1182: not a sound law, it is **impossible to find any chronological relationship**
1183: with the almost exceptionless lowering of \*u."
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:550 (concept name)

- Nearby heading: ### Hogg vol. 1 (l. 20349–20352)

```text
549: 
550: > "(b) In Mercian and Kentish influenced texts, we regularly find this
551: > /ae/ raised to /e/, spelled <e>. This latter process is usually called
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:754 (concept name)

- Nearby heading: ## 11. Dialect of the canonical OE literary texts

```text
753: | Erfurt Glossary (Erf.) | continental copy of an English (Anglian) original | Hogg ll. 20856–20862; Campbell §225 |
754: | Corpus Glossary (Cp.) | Mercian (Anglian) | Hogg ll. 20880–20892 ("Corpus we find only /æa/ unsmoothed..."; treats CorpGl as Mercian alongside VP); Campbell ll. 6772–6779 |
755: | Beowulf and other major poetic codices | conventionally treated as a "general OE poetic koiné" with Anglian substrate features | Campbell §207 l. 6271 ("Instances of back umlaut of æ are practically unknown in W-S texts but they are quite a feature of the W-S transcripts of OE poems: Beow. alone has beadu- heapu-, eafora, eafod, eatol, heafo, geheaderod, heafola"); Campbell ll. 6262–6263 (LV, BH have name-elements `Headu-`, `Beadu-` "due to the use of poetical forms, ultimately derived from the Mercian area") |
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:109 (concept name)

- Nearby heading: ### Direct corpus attestations

```text
108: **None located.** Every pret. pl. token of `būgan` / `ābūgan` /
109: `onbūgan` / `gebūgan` etc. that I could find in the standard
110: lexicographic record (Bosworth-Toller, Toller's Supplement, Clark
```

#### Germanic/docs/dossiers/un-to-on-chronology.md:231 (concept name)

- Nearby heading: ### Hogg vol.1 §3.3.1.3 + §3.3.3.2

```text
230: > "/u/ had a strong tendency to lower, **especially when a consonant
231: > followed**, so we find, for example, **heofon 'heaven' in Early West
232: > Saxon rather than heofun**, although **if /u/ is in absolute
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Campbell1959 | single available key for Campbell |
| Luick1914 | single available key for Luick |
| BosworthToller1898 | single available key for Toller |

### Low-confidence candidates

_None_

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

