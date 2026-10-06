# Evidence packet — 2183 shoulder / sċuldrum

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2183 | shoulder | sċuldrum | *skuldrō | *skúldramiz | late_analogy | DatPl encoding: PROTOFORM is PGmc-proper *-amiz (inst.pl. branch of dat./inst. merger). See DEV_NOTES §17.41. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# shoulder
PROTO: *skúldramiz
EXPECTED: sċuldrum
OUTPUTS: sċuldrum



### Proto-Germanic consonant inheritance

Proto Input: *skúldramiz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>NWGmc A To U Before M: *skúldrumiz<br>PWGmc Early I Apocope: *skúldrumz<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *skúldrum | **Old English**<br>OE Sk Palatalization: *ʃúldrum |



### Orthography & surface

Old English Orthography: sċ*úldrum
Outcome: sċuldrum

NOTE: DatPl encoding: PROTOFORM is PGmc-proper *-amiz (inst.pl. branch of dat./inst. merger). See DEV_NOTES §17.41.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:39502 (row ID)

- Nearby heading: ### Proposed fix (two parts)

```text
39500:      no regressions on currently-working rows.
39501: 
39502: 3. **TSV row 2183 edit**: PROTOFORM `*skúldrō → *skúldrumiz`,
39503:    COUNTERPART `sċuldra → sċuldrum`. Documents this as masc.
39504:    a-stem DatPl, cell-consistent.
```

#### Germanic/docs/DEV_NOTES.md:39659 (exact pair)

- Nearby heading: ### Implementation log (2026-04-28)

```text
39657:     has no effect on any rule other than R2.
39658: 
39659: Verification: `*skúldramiz → sċuldrum` ✓ (P3 passes); other probes
39660: in progress.
39661: 
```

#### Germanic/docs/DEV_NOTES.md:39943 (row ID)

- Nearby heading: ### Plan

```text
39941: ### Plan
39942: 
39943: * Edit TSV row 2183:
39944:   - PROTOFORM `*skúldrō` → `*skúldru` (per R/T vol. 2 p. 142)
39945:   - COUNTERPART `sċuldra` → `sċuldor` (BT/Hall main headword)
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:10429 (exact COUNTERPART)

- Nearby heading: ## Mismatch Progress Log (2026-03-14)

```text
10427: | 2026-04-28 | 17 | -1 | 8917de42 | weasel: target retarget Anglian weosule → WS wesle (§17.37) |
10428: | 2026-04-28 | 16 | -1 | 7f8a289b | westene: target alignment with *wéstanē (§17.38) |
10429: | 2026-04-28 | 15 | -1 | 14565e33 | sċuldrum: DatPl *-amiz cascade (§17.41) |
10430: | 2026-04-28 | 15 | 0 | 97aab23e | OERMetathesis word-initial guard (rust → ledger; §17.42) |
10431: | 2026-04-28 | 14 | -1 | 400e41c8 | þrīe: TSV retarget þrī → þrīe early-WS (§17.43) |
```

#### Germanic/docs/DEV_NOTES.md:39387 (exact COUNTERPART)

- Nearby heading: ## §17.41 *skúldrō → sċoldor (expected sċuldra 'shoulder'): proposed fix

```text
39385: > **STATUS (2026-04-28): PROPOSED FIX, AUTHORISED IN PRINCIPLE BY LITERATURE — awaiting user green-light to apply.** The
39386: > paradigm survey (`dossier-shoulder-paradigm-survey-2026.md`)
39387: > identified **masc. a-stem DatPl `*skúldrumiz` ↔ `sċuldrum`**
39388: > as the unique cell-consistent lautgesetzlich match. Implementing
39389: > it requires (a) extending the FST proto-input alphabet to admit
```

#### Germanic/docs/DEV_NOTES.md:39496 (exact COUNTERPART)

- Nearby heading: ### Proposed fix (two parts)

```text
39494:    * `*búgun → bugon`: *u before *n, still lowers ✓
39495:    * `*jugunθ → ġeoguþ`: protected by NSL→*ū (separate mechanism) ✓
39496:    * `*skúldrum → sċuldrum`: *u before *m, no longer lowers ✓
39497:    * No existing TSV row has medial unstressed *u before *m
39498:      (DatPl morphology was not previously in the alphabet), so
```

#### Germanic/docs/DEV_NOTES.md:39503 (exact COUNTERPART)

- Nearby heading: ### Proposed fix (two parts)

```text
39501: 
39502: 3. **TSV row 2183 edit**: PROTOFORM `*skúldrō → *skúldrumiz`,
39503:    COUNTERPART `sċuldra → sċuldrum`. Documents this as masc.
39504:    a-stem DatPl, cell-consistent.
39505: 
```

#### Germanic/docs/DEV_NOTES.md:39520 (exact COUNTERPART)

- Nearby heading: ### Proposed fix (two parts)

```text
39518: 
39519:    The conservative non-i-mutated form `sculdrum` is the target
39520:    (cascade output `sċuldrum` matches modulo the palatal-sċ
39521:    diacritic per Hogg §3.50).
39522: 
```

#### Germanic/docs/DEV_NOTES.md:39524 (exact PROTOFORM)

- Nearby heading: ### Proposed fix (two parts)

```text
39522: 
39523:    **Encoding decision (2026-04-28, revised twice):** PROTOFORM is
39524:    the **PGmc-proper form `*skúldramiz`** — the **inst.pl.** branch
39525:    of the dat./inst. merger, with thematic *-a- and the *-amiz
39526:    inst. ending, before NWGmc *a→*u/_m raising.
```

#### Germanic/docs/DEV_NOTES.md:39592 (exact COUNTERPART)

- Nearby heading: ### Cascade complications already documented (still relevant)

```text
39590: 
39591: Earlier probes with the post-NWGmc-raising form `*skúldrumiz`
39592: showed `sċuldreme` instead of `sċuldrum`, due to:
39593: 
39594: (a) **Suffix *u fronting** in `ProtoToOEWeakTail` / English
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| shoulder | sċuldra | inh | template:inh | shoulder |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:8171 (concept name)

- Nearby heading: ### Historical Background

```text
8169: > "We might account for the variation in *pixl* ~ *pisl* by suggesting that `*h`
8170: > was lost only when the cluster was word-final; but that makes it impossible
8171: > to account for *sesta* and *néosan*—and note further that *eaxl* 'shoulder'
8172: > < `*ahslu` is another counterexample. The best we can do is to conclude that
8173: > **`*h` was lost, possibly variably, possibly only in some dialects, when
```

#### Germanic/docs/DEV_NOTES.md:8205 (concept name)

- Nearby heading: ### Variability

```text
8203: R/T and Campbell both note the change was **variable**:
8204: - `pixl ~ pisl` both attested in OE
8205: - `eaxl` 'shoulder' < `*ahslu` shows preserved `*x`
8206: 
8207: However, for `*funxstiz` → `fȳst`, the attested OE form has NO `*x`, so
```

#### Germanic/docs/DEV_NOTES.md:31142 (concept name)

- Nearby heading: ##### §17.19.10.1.c PIE summary

```text
31140: directly (parallel to *ahslō- < *h₂eḱs-l-eh₂-, which Kroonen
31141: explicitly gives as a parallel: *ahslō-, ref line 2575: "*ahslō- f.
31142: 'shoulder, armpit'... Derived from PIE *h₂eḱs-i- with an l-suffix,
31143: cf. *nablan- 'navel'"; and *manla-, ref line 21048: "For the
31144: suffixation of l, compare *nablan- 'navel'").
```

#### Germanic/docs/DEV_NOTES.md:31326 (concept name)

- Nearby heading: ##### §17.19.10.2.e Comparison with parallel l-stems

```text
31324: | 'hawk'        | *habukaz           | *habukaz      | *xaƀukaz        | inherited           |
31325: | 'fork'        | *gabalō            | *gabulō       | *gaƀalō         | disputed            |
31326: | 'shoulder'    | *ahslō-            | *ahslō        | *axslō          | no medial — purely PIE |
31327: 
31328: (Sources: Kroonen 2013 *passim*, e.g. *naglaz* p.382, *fuglaz* p.158
```

#### Germanic/docs/DEV_NOTES.md:39383 (concept name)

- Nearby heading: ## §17.41 *skúldrō → sċoldor (expected sċuldra 'shoulder'): proposed fix

```text
39381: ---
39382: 
39383: ## §17.41 *skúldrō → sċoldor (expected sċuldra 'shoulder'): proposed fix
39384: 
39385: > **STATUS (2026-04-28): PROPOSED FIX, AUTHORISED IN PRINCIPLE BY LITERATURE — awaiting user green-light to apply.** The
```

#### Germanic/docs/DEV_NOTES.md:39386 (concept name)

- Nearby heading: ## §17.41 *skúldrō → sċoldor (expected sċuldra 'shoulder'): proposed fix

```text
39384: 
39385: > **STATUS (2026-04-28): PROPOSED FIX, AUTHORISED IN PRINCIPLE BY LITERATURE — awaiting user green-light to apply.** The
39386: > paradigm survey (`dossier-shoulder-paradigm-survey-2026.md`)
39387: > identified **masc. a-stem DatPl `*skúldrumiz` ↔ `sċuldrum`**
39388: > as the unique cell-consistent lautgesetzlich match. Implementing
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| HoggPhonology1992 | single available key for Hogg |

### Low-confidence candidates

_None_

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

