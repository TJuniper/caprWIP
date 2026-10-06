# Evidence packet — 2298 wolf / wulf

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2298 | wolf | wulf | *wúlfaz | *wúlfaz | unexplained_unmodelled | DOCUMENTED EXCEPTION (per §17.10.34): Campbell §115 names wulf as exception to a-umlaut (regular outcome = **wolf, cf. OHG wolf). No lautgesetzlich PROTOFORM available: every paradigm cell with low *a/*ō triggers a-umlaut, every cell with high *i triggers i-umlaut (attested 'wulfe' from *wulfi has umlaut *levelled analogically* per Brunner §230 Anm., so lautgesetzlich outcome of *wulfi would be **wylfe). attested wulf is doubly irregular. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# wolf
PROTO: *wúlfaz
EXPECTED: wulf
OUTPUTS: wolf



### Proto-Germanic consonant inheritance

Proto Input: *wúlfaz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc U Lowering: *wólfaz<br>PGmc Final Z Deletion: *wólfa | **Old English**<br>PWGmc Final Bare A Loss: *wólf |



### Orthography & surface

Outcome: wolf

NOTE: DOCUMENTED EXCEPTION (per §17.10.34): Campbell §115 names wulf as exception to a-umlaut (regular outcome = *wolf, cf. OHG wolf). No lautgesetzlich PROTOFORM available: every paradigm cell with low *a/ō triggers a-umlaut, every cell with high *i triggers i-umlaut (attested 'wulfe' from *wulfi has umlaut *levelled analogically* per Brunner §230 Anm., so lautgesetzlich outcome of *wulfi would be *wylfe). attested wulf is doubly irregular.
```

### Matching oe_known_problems.tsv entries

| proto | status | category | reason | refs | added |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *wúlfaz | wontfix | u_lowering_near_labial | Same u-lowering near labials issue (R/T vol.2 §2.3.1 explicit example) | notable_findings#2 | 2026-04-25 |

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1432 (exact pair)

- Nearby heading: ## Project Status (as of 2026-04-30) — research phase complete

```text
1430: * `*rústō → rost` (expected `rust`) — `wontfix: u_lowering_near_labial`
1431: * `*táppô → tappa` (expected `tæppa`) — `exception: analogical_n_stem_levelling`
1432: * `*wúlfaz → wolf` (expected `wulf`) — `wontfix: u_lowering_near_labial`
1433: * `*wúllō → woll` (expected `wull`) — `wontfix: u_lowering_near_labial`
1434: 
```

#### Germanic/docs/DEV_NOTES.md:25952 (exact pair)

- Nearby heading: ### §17.10.34 Cluster: u-lowering "exceptions" (wulf, fugol, bucc, rust, wull) — paradigm-cell switch for 4/5

```text
25950: | `*fúglaz` | `fogol` | `fugol` |
25951: | `*rústō` | `orst` | `rust` |
25952: | `*wúlfaz` | `wolf` | `wulf` |
25953: | `*wúllō` | `woll` | `wull` |
25954: 
```

#### Germanic/docs/DEV_NOTES.md:26018 (exact pair)

- Nearby heading: #### Source audit — is there a lautgesetzlich rule that gives these?

```text
26016:    a-umlaut by env. (a).
26017: 3. There is **no consensus rule** that we could add to the FST to
26018:    produce `wulf` from `*wúlfaz` lautgesetzlich. Sources that propose
26019:    labial-conditioned blocking (Luick, scattered) explicitly call it
26020:    "irregular"; the systematic accounts (Stiles, Campbell, Brunner)
```

#### Germanic/docs/DEV_NOTES.md:26052 (row ID)

- Nearby heading: #### Chosen approach: paradigm-cell switch for 4/5 (per §17.10.32)

```text
26050: | Row | Old PROTOFORM → target | New PROTOFORM → target | Rationale |
26051: | --- | --- | --- | --- |
26052: | 2298 | `*wúlfaz → wulf` (analogical) | `*wúlfis → wulfes` (gen.sg., regular) | Stiles env. (a) |
26053: | 2030 | `*fúglaz → fugol` (analogical, parasite vowel) | `*fúglis → fugles` (gen.sg., regular) | Stiles env. (a); also avoids parasite-vowel cell |
26054: | 1973 | `*búkkaz → bucc` (analogical) | `*búkkis → bucces` (gen.sg., regular) | Stiles env. (a) |
```

#### Germanic/docs/DEV_NOTES.md:26636 (row ID)

- Nearby heading: ### §17.10.35 *wīθijaz → wīþ (expected wīþiġ): wrong suffix etymology

```text
26634:   2227 *stráwjaną        strewan        strewian        ✗ MISMATCH (R/T §6.1 case)
26635:   2288 *wíduwōn          widowe         widuwe          ✓ no *j; vowel-quality issue
26636:   2298 *wúlfaz           wolf           wulf            ✓ unrelated (u-lowering)
26637:   2308 *júgunθ           ġeoguþ         ġeoguþ          ✓ no *j after vowel
26638:   2317 *skáwô            sċēawa         sċēawa          ✓ no *j; Class II noun
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

#### Germanic/docs/DEV_NOTES.md:73 (exact COUNTERPART)

- Nearby heading: ### The problem

```text
71: 
72: - *fullăz → full (not ×foll; OHG fol)
73: - *wulfăz → wulf (not ×wolf; OHG wolf)
74: - *fuglăz → fugol (not ×fogol; OHG fogal)
75: - *bukkăz → bucc (not ×bocc; OHG boc)
```

#### Germanic/docs/DEV_NOTES.md:82 (exact COUNTERPART)

- Nearby heading: ### Summary of the scholarly literature

```text
80: ### Summary of the scholarly literature
81: 
82: **Bülbring (EB §116, pp.45-46)** provides the original hypothesis that both Luick and R/T engage with. He observes that OE u appears instead of expected o (from WGmc a-Umlaut, his §81d) "namentlich zwischen Labial und langem oder gedecktem l" — i.e. between a labial and ll or l+consonant: *full* 'full', *wulle* 'wool', *wulf* 'wolf'; also *fugol* 'bird', *bucca* 'buck', *múrnan* 'mourn'. He concedes that "meist steht jedoch der Hauptregel gemäß o" — usually the regular rule gives o — citing *wolcen, folgian, bolt, folc* as counterexamples. In his Anmerkung, Bülbring notes the agreement with OFris. and OS (afries. *ful, wulla, wulf*; as. *full, wulla, wulf, fugal*), which shows the phenomenon is "sehr alt" (very old). He remains agnostic on mechanism: "Ob wir darin Erhaltung des wg. u oder Wiederaufhebung der durch a-Umlaut herbeigeführten Veränderung erblicken müssen, läßt sich nicht mit Sicherheit entscheiden" — whether this reflects preservation of the original WGmc *u or reversal of a-Umlaut cannot be determined with certainty. He speculates that *u was lowered only partway ("etwa zu [ou] oder zu engem [o]") and then, under influence of its labial/velar environment, reverted to u, while in other words it continued to open [ɔ]. This "incomplete lowering + reversion" model is phonetically interesting but not formalizable as a categorical rule, since the same environments also show regular lowering.
83: 
84: **Luick (§78, Anm. 3)** engages directly with Bülbring's proposal and rejects it. He argues for paradigmatic leveling instead: doublet forms arose because paradigms had both u-preserving (high-vowel suffix) and u-lowering (non-high suffix) forms; near labials and gutturals, the u-forms were preferred. He explicitly cites the counterexamples that make Bülbring's phonological conditioning untenable: *wolcen, folc, folġian, folde, folm, bolla, bolt, bolster, molde, molcen, smolt* — all have labial or velar environments but regular lowering.
```

#### Germanic/docs/DEV_NOTES.md:93 (exact COUNTERPART)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
91: 
92: **Approach A: Use a u-stem or root-noun form.**
93: R/T notes that u-stems and root nouns regularly preserve *u because their paradigms have predominantly high-vowel suffixes (nom.sg. *-uz, acc.sg. *-ŷ, gen.sg. *-iz, dat.sg. *-i, nom.pl. *-iz, etc.). For example, *lustuz (u-stem nom.sg.) → OE lust with preserved u (R/T p.45). If *wulf-, *fugl-, or *bukk- were u-stems, we could use the nom.sg. in *-uz.
94: 
95: **What weighs against Approach A:**
```

#### Germanic/docs/DEV_NOTES.md:96 (exact COUNTERPART)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
94: 
95: **What weighs against Approach A:**
96: - Kroonen reconstructs *wulfa- (a-stem; p.598), *fugla- (a-stem), and *bukka(n)- (originally n-stem; p.98) — none as u-stems.
97: - There is no Gothic or comparative evidence for u-stem inflection of these words. Gothic wulfs is an a-stem, Gothic fugls is an a-stem.
98: - Using a u-stem nom.sg. would require us to posit a stem-class that is not attested in any daughter language. This would be philologically indefensible.
```

#### Germanic/docs/DEV_NOTES.md:97 (exact COUNTERPART)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
95: **What weighs against Approach A:**
96: - Kroonen reconstructs *wulfa- (a-stem; p.598), *fugla- (a-stem), and *bukka(n)- (originally n-stem; p.98) — none as u-stems.
97: - There is no Gothic or comparative evidence for u-stem inflection of these words. Gothic wulfs is an a-stem, Gothic fugls is an a-stem.
98: - Using a u-stem nom.sg. would require us to posit a stem-class that is not attested in any daughter language. This would be philologically indefensible.
99: 
```

#### Germanic/docs/DEV_NOTES.md:101 (exact COUNTERPART)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
99: 
100: **Approach B: Use the instrumental singular *-u of the a-stem.**
101: The a-stem instrumental singular ended in *-u (high vowel), which would block lowering: *wulfu → *wulfu (u preserved) → OE wulf.
102: 
103: **What weighs against Approach B:**
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

#### Germanic/docs/DEV_NOTES.md:148 (note keyword: a-umlaut)

- Nearby heading: ### Expert consultation: Stefan Schuhmacher (Vienna, 2026-03-20)

```text
146: Prof. Schuhmacher confirmed the scholarly consensus and provided additional clarifications:
147: 
148: **Terminology:** He prefers "Lowering of \*u" over "A-Umlaut" as more transparent.
149: 
150: **Scope:** "Such lowering affects **only stressed vowels**... I do not see that the lowering affects unstressed vowels such as the middle vowel in the word for 'widow'." This validates our implementation restricting lowering to stressed syllables.
```

#### Germanic/docs/DEV_NOTES.md:217 (note keyword: a-umlaut)

- Nearby heading: ### Related: effects of initial labials on vowels (Bülbring §§260-274)

```text
215: 
216: Note that Bülbring's "Dreizehntes Kapitel" (§§260-274) discusses a *separate* set of phenomena — the effects of initial labials (especially w) on following vowels and diphthongs. These include:
217: - **w + iu → wu** (§264): *widu → wudu 'wood' (via u/a-Umlaut *wiudu → wudu under w-influence)
218: - **weo → wo → wu** (§§265-268): late WS weorpan → wurpan, sweord → swurd
219: - **w + i → y** (§261): ni + witan → nytan (contraction contexts)
```

#### Germanic/docs/DEV_NOTES.md:620 (note keyword: a-umlaut)

- Nearby heading: #### 1. NWGmc U-Lowering ("A-Umlaut" / Lowering of *u)

```text
618: distinguish them clearly because they have different conditioning:
619: 
620: #### 1. NWGmc U-Lowering ("A-Umlaut" / Lowering of *u)
621: 
622: **Rule:** Stressed `*u → *o` before a non-high vowel (*a, *o, *ē) in the following syllable.
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

#### Germanic/docs/DEV_NOTES.md:5137 (note keyword: a-umlaut)

- Nearby heading: #### View 2: Lowering occurred in West Germanic (Bülbring's position)

```text
5135: > "\*nëstoz 'Nest' aus älterem \*nistoz, \*wëroz 'Mann' aus \*wiroz"
5136: 
5137: Bülbring calls this "a-Umlaut" — lowering of *i, u* before non-high vowels in the
5138: following syllable. He treats this as a WGmc phenomenon that took an earlier
5139: \*nistoz and produced \*nestoz.
```

#### Germanic/docs/DEV_NOTES.md:5243 (note keyword: a-umlaut)

- Nearby heading: #### Lloyd (1966): "Is There an a-Umlaut of i in Germanic?"

```text
5241: explanation that is both Neogrammarian and predictive.
5242: 
5243: #### Lloyd (1966): "Is There an a-Umlaut of i in Germanic?"
5244: 
5245: Albert L. Lloyd (University of Pennsylvania) argued that **no regular a-umlaut of
```

#### Germanic/docs/DEV_NOTES.md:26062 (exact PROTOFORM)

- Nearby heading: #### Chosen approach: paradigm-cell switch for 4/5 (per §17.10.32)

```text
26060: correspondingly updated from `*rustō` to `*rústaz`.
26061: 
26062: The cognate-set headword `*wúlfaz / *fúglaz / *búkkaz` is preserved
26063: in the PROTO column for rows 2298, 2030, 1973 — only the
26064: cell-specific PROTOFORM (which feeds the FST) changes. This matches
```

#### Germanic/docs/DEV_NOTES.md:26116 (exact PROTOFORM)

- Nearby heading: #### Implementation order

```text
26114:    row 2300 (NOTE expansion only). Per `skills/be-lautgesetzlich.md`
26115:    convention: PROTOFORM = cell-specific FST input; PROTO = cognate
26116:    headword (preserved as `*wúlfaz`/`*fúglaz`/`*búkkaz`; corrected to
26117:    `*rústaz` for row 2162).
26118: 3. Re-run `python3 tools/oe_mismatch_report.py`; verify count is 32
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:456 (note keyword: i-umlaut)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
455: 
456: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut
457: 
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:472 (note keyword: i-umlaut)

- Nearby heading: ## 7. R/T relative chronology of A-fronting, A-restoration, breaking, and i-umlaut

```text
471: (3) *a before single C / geminate / sC + back vowel
472:  ↓ I-umlaut (R/T §6.6)
473: (4) modifies remaining *æ but cannot un-restore *a
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:735 (note keyword: i-umlaut)

- Nearby heading: ## 11. Affected TSV rows

```text
734: | 2056 | `*xármaz` | `hearm` | breaking |
735: | 2057 | `*xárbistuz` | `hierfest` | breaking + i-umlaut |
736: | 2077 | `*xáldaną` | `healdan` | breaking |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:74 (exact COUNTERPART)

- Nearby heading: ### Case 2: *spéru (spear) — speoru

```text
73: | **PROTO** | `*spéru` (m./n., light u-stem or reformed i-stem; PIE *sperH-) |
74: | **OE SIMPLEX** | `spere` (nom.sg., attested widely: Maldon, Beowulf, Ælfric; non-umlauted) |
75: | **OE PLURAL** | `speru` (nominative/accusative plural, common; reformed form, analogically leveled away back umlaut) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:154 (note keyword: i-umlaut)

- Nearby heading: ### Case 6: *líznōn- (learn) — leornian

```text
153: | **Lautgesetzlich output** | `leornian` (from *e-grade root `*leznōn-`) (FST: ✓ correct with corrected proto) |
154: | **Previous FST output** | `liernian` (from incorrect *i-grade root `*liznōn-` + i-umlaut *eo → ie*) |
155: | **DEV_NOTES reference** | §14.518–14.760 (OE leornian 'to learn' — ie vs eo diphthong problem); major cross-reference in mismatch_dossier_mizdo.md (Campbell §123 fn.2 citation) |
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:168 (note keyword: i-umlaut)

- Nearby heading: ### Case 7: *fúwerō / *fūri (fire) — fȳre (dat.sg.) vs. fȳr (nom.sg.)

```text
167: | **PROTO** | `*fūri` (dat.sg., locative singular; singular = u-stem or ī-stem, feminine) |
168: | **OE SIMPLEX (NOM.SG.)** | `fȳr` (nom.sg., attested, showing i-umlaut of *ū → *ȳ*) |
169: | **OE SIMPLEX (DAT.SG.)** | `fȳre` (dat.sg., showing i-umlaut plus **analogically restored** final *-e*) |
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

#### Germanic/docs/analysis/meord_med_chronological_review.md:33 (exact COUNTERPART)

- Nearby heading: ## 1. Primary attestations

```text
32: | meorda  | gen.pl | Gregory's Dialogues 312.14 (var.)          | `anglosaxondictio00tolluoft.txt:56915` (OCR "meotda") |
33: | mēd     | nom.sg | widely in WS prose (Ælfric, Wulfstan, etc.) | BT s.v. *mēd* |
34: | mēde    | dat.sg | widely                                     | BT s.v. *mēd* |
```

#### Germanic/docs/analysis/notable_findings.md:230 (exact COUNTERPART)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
229: pp.27-33). However, a cluster of lexemes retains \*u where \*o is predicted:
230: \*fullaz → full (not ×foll), \*wulfaz → wulf (not ×wolf), \*fuglaz → fugol
231: (not ×fogol), \*bukkaz → bucc (not ×bocc), \*wullō → wulle (not ×wolle),
```

#### Germanic/docs/analysis/notable_findings.md:265 (exact COUNTERPART)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
264: 1. **U-stem paradigm forms** — philologically indefensible (Kroonen
265:    reconstructs \*wulfa-, \*fugla-, \*bukka(n)- as a-/n-stems)
266: 2. **Instrumental singular \*-u** — R/T reject this as implausible source
```

#### Germanic/docs/analysis/notable_findings.md:268 (exact COUNTERPART)

- Nearby heading: ## 2. NWGmc u-lowering exceptions near labials: a non-Neogrammarian pattern

```text
267:    of leveling
268: 3. **Root-noun analysis** — Gothic wulfs shows thematic inflection, ruling
269:    this out
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:366 (note keyword: a-umlaut)

- Nearby heading: ### Campbell §210 — concrete dialect contrast

```text
365: and liquids (`heofon, eofor, beofor, heorot`) but not generally before other
366: consonants; a-umlaut is mostly absent (`fela, helan, beran, nefa, sefa,
367: weras, wela`). In Anglian (l. 6337): "both u- and a-umlaut of e are general
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:755 (exact COUNTERPART)

- Nearby heading: ## 11. Dialect of the canonical OE literary texts

```text
754: | Corpus Glossary (Cp.) | Mercian (Anglian) | Hogg ll. 20880–20892 ("Corpus we find only /æa/ unsmoothed..."; treats CorpGl as Mercian alongside VP); Campbell ll. 6772–6779 |
755: | Beowulf and other major poetic codices | conventionally treated as a "general OE poetic koiné" with Anglian substrate features | Campbell §207 l. 6271 ("Instances of back umlaut of æ are practically unknown in W-S texts but they are quite a feature of the W-S transcripts of OE poems: Beow. alone has beadu- heapu-, eafora, eafod, eatol, heafo, geheaderod, heafola"); Campbell ll. 6262–6263 (LV, BH have name-elements `Headu-`, `Beadu-` "due to the use of poetical forms, ultimately derived from the Mercian area") |
756: 
```

#### Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:757 (exact COUNTERPART)

- Nearby heading: ## 11. Dialect of the canonical OE literary texts

```text
756: 
757: The standard textbook treatment of Beowulf's "poetic koiné" — i.e. that the
758: extant text is a late WS scribal copy of a poem with detectable Anglian
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:220 (exact COUNTERPART)

- Nearby heading: ### §4.1 Sources for the attested forms

```text
219:   past sg. and past ptcp. fully regular.
220: * **Bēowulf** has `bēag` (line 2956 etc.); **Genesis A**, **Beowulf**,
221:   **Andreas**, **Christ**, **Elene** all attest `bēag` in 1/3 sg.
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:304 (exact COUNTERPART)

- Nearby heading: ### §5.1 Sources for the attested forms

```text
303:   underlying stem is `sċuf-` ~ `sċof-` for those cells.
304: * **Beowulf** 215: "Guman ūt **scufon**" (3 pl. pret. — but with
305:   the lWS / Late-OE `-on` ending).
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:309 (exact COUNTERPART)

- Nearby heading: ### §5.1 Sources for the attested forms

```text
308: * The 1/3 sg. pret. `sċēaf` is well attested in the poetic and
309:   prose corpus (Beowulf, Maldon, Ælfric, etc.). The past ptcp.
310:   `sċofen` is attested in Boethius, Martyrology, Ælfric.
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:62 (exact COUNTERPART)

- Nearby heading: ### Local handbook evidence

```text
61: > "**genihtsumlīce gebugon** (uberes fructus ager attulit, Lk. 12,
62: > 16), Wlfst." (Wulfstan)
63: 
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:136 (exact COUNTERPART)

- Nearby heading: ### Verdict

```text
135: `tōbugon`) but only in the *Anglo-Saxon Chronicle* (10th–11th c.
136: annals), Ælfric (late WS, c. 990–1010), Wulfstan (early 11c.),
137: Gregory's Dialogues (late WS), the Old English Hexateuch, the *Battle
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:153 (exact COUNTERPART)

- Nearby heading: ### Local handbook evidence

```text
152: > "Rinc mænig, gūðfrec guma, An. 1119. **Guman ūt scufon**, **B.
153: > 215**." (*Beowulf*, line 215; West-Saxon poetic koine, MS late
154: > 10c.)
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

#### Germanic/docs/dossiers/widuwe-u-preservation.md:402 (note keyword: a-umlaut)

- Nearby heading: ### What NOT to do

```text
401:   middle vowel in the word for 'widow'") to argue against the rule
402:   itself. Schuhmacher there is talking about *A-Umlaut / stressed-
403:   `*u`-lowering*, not about Campbell §373; the latter is securely
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:505 (note keyword: a-umlaut)

- Nearby heading: ### Cited only via secondary / not directly opened in this round

```text
504:   The quote is informative but not load-bearing for this dossier:
505:   Schuhmacher is discussing A-Umlaut / stressed-`*u`-lowering, not
506:   Campbell §373 medial-unstressed lowering.
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:525 (note keyword: a-umlaut)

- Nearby heading: ### Not consulted in this round (and not needed)

```text
524:   *widuwō(n)- not in dispute.
525: * Stiles 2012, Howell & Salmons 1988, Cercignani — concern A-Umlaut
526:   / stressed lowering, not the medial-unstressed rule.
```

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| wolf | wulf | inh | template:inh | wolf |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:114 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
112: - Kroonen's reconstructions show these as thematic stems (*wulfa-, *fugla-), not root nouns.
113: - Gothic wulfs shows the thematic nom.sg. ending *-az, not a root-noun pattern.
114: - Root nouns are a small, archaic class (burg, brust, furh, hnut-); extending the analysis to common nouns like 'wolf' and 'fowl' would be speculative.
115: 
116: **Approach D: Use a derivational form with i-umlaut trigger.**
```

#### Germanic/docs/DEV_NOTES.md:132 (concept name)

- Nearby heading: ### Areal variation

```text
130: ### Areal variation
131: 
132: Luick (Anm. 1) and R/T both note that OE, OFris., and OS share the u-preserving forms, while OHG has regular lowered forms: OE/OS wulf vs. OHG wolf, OE/OS full vs. OHG fol. This is a NWGmc areal feature, not specifically OE. R/T goes further: for *wulfaz, even OF (!) shows wolf with lowering, which is unexpected if the u-preservation were a shared northern WGmc innovation.
133: 
134: ### Decision and implementation
```

#### Germanic/docs/DEV_NOTES.md:140 (concept name)

- Nearby heading: ### Decision and implementation

```text
138: **For future expert discussion:** The most promising angle might be Luick's observation about consonantal environment (near labials/gutturals + l). While neither Luick nor R/T accept this as a categorical rule, the statistical clustering might reflect a phonetic tendency — perhaps the acoustic similarity between labial/velar environments and the labial component of [u] made the lowered [o] variant phonetically less stable in those contexts. This would be a gradient/probabilistic effect rather than a Neogrammarian rule, and is therefore fundamentally not modelable in a deterministic FST. Bülbring's "incomplete lowering + reversion" model (§116 Anm.) is the most explicit formulation of this intuition, but the counterexamples (folc, bolla, etc.) preclude formalizing it.
139: 
140: **Additional citation (Brunner §68):** Brunner echoes Bülbring: "In einigen Wörtern steht, zumal in der Nachbarschaft von Labialen, statt des zu erwartenden o ein u, z. B. full voll, wulf Wolf, wulle Wolle, fugol Vogel, bucca Bock, cnucian stoßen, ufan oben..." ("In some words, especially in the neighborhood of labials, instead of the expected o, a u appears..."). His examples align with the pattern but provide no formal conditioning.
141: 
142: **Phonetic note:** Labial consonants share the [+round] feature with /u/. This articulatory compatibility may have created a phonetically favorable context for preserving the high back rounded vowel. However, as Bülbring and Luick both concede, this cannot be formalized as a categorical rule given the counterexamples.
```

#### Germanic/docs/DEV_NOTES.md:163 (concept name)

- Nearby heading: ### Expert consultation: Stefan Schuhmacher (Vienna, 2026-03-20)

```text
161: a u-stem variant remains unverified. See notable_findings.md §2 for details.
162: 
163: **OHG contrast:** "Franconian/Alemannic/Bavarian here consistently have /o/, i.e. 'Old High German' fol, wolf, fogal, boc."
164: 
165: **Key quote:** "It does hurt our Neogrammarian pride that what looks like a full-blown sound law (and not just a 'tendency') seems to have some exceptions."
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

### Analysis and dossier hits

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:77 (exact COUNTERPART)

- Nearby heading: #### Form A: `mēd` (monophthong, no /r/)

```text
76: - **Ælfric** (Catholic Homilies, Lives of Saints): *mēd* consistently
77: - **Wulfstan** (homilies): *mēd* consistently  
78: - **Prose Psalter** (WS): *mēd*
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:80 (exact COUNTERPART)

- Nearby heading: #### Form A: `mēd` (monophthong, no /r/)

```text
79: - **Late WS laws** (Cnut, Æthelred): *mēd*
80: - **Beowulf**: *mēd* (line 2134: *þā him wæs manna þearf / gōdra gūðrinca, þǣr him ȳðlāde / eft on mēd gefremede*) — though Beowulf's dialect is complex
81: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:347 (exact COUNTERPART)

- Nearby heading: ### 4.3 OE dictionaries

```text
346: - s.v. **mēd**: "f. meed, reward, recompense, price, compensation, pay, bribe"
347:   - Cites numerous examples from WS texts (Ælfric, Wulfstan, laws)
348:   - Notes etymology from PGmc `*mizdō`
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
| Lloyd1966 | author + year mention (Lloyd 1966) |
| HowellSalmons1988 | author + year mention (Salmons 1988) |
| Stiles2012 | author + year mention (Stiles 2012) |
| Kroonen2013 | default Proto-Germanic etymology key for Kroonen |
| HoggPhonology1992 | single available key for Hogg |
| Campbell1959 | single available key for Campbell |
| SieversBrunner1965 | single available key for Sievers |
| Luick1914 | single available key for Luick |

### Low-confidence candidates

| Key | Why it was selected |
| :--- | :--- |
| Kroonen2011 | surname mention only: Kroonen |
| Kroonen2006 | surname mention only: Kroonen |
| LloydSpringer1988 | explicit year mention (1988) |
| Cercignani1979 | surname mention only: Cercignani |
| Cercignani1980 | surname mention only: Cercignani |
| Stiles2017 | surname mention only: Stiles |
| Stiles1985 | surname mention only: Stiles |
| Stiles1986a | surname mention only: Stiles |
| Stiles1986b | surname mention only: Stiles |

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

