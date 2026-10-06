# Evidence packet — 2051 hair / hǣr

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2051 | hair | hǣr | *xḗrą | *xḗrą | regular | Wiktionary: PGmc *hērą > OE hǣr; *xazwăz 'grey' is wrong lexeme | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# hair
PROTO: *xḗrą
EXPECTED: hǣr
OUTPUTS: hǣr



### Proto-Germanic consonant inheritance

Proto Input: *xḗrą

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>NWGmc Long E Lowering: *xǣrą | **Old English**<br>OE Velar Fricative Palatalization: *çǣrą<br>OE Heavy Syllable Nasal Apocope: *çǣr |



### Orthography & surface

Old English Orthography: h*ǣr
Outcome: hǣr

NOTE: Wiktionary: PGmc *hērą > OE hǣr; *xazwăz 'grey' is wrong lexeme
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2623 (exact COUNTERPART)

- Nearby heading: ### OE diagnostics: mismatch closeness + diacritics (2026-01-02)

```text
2621: - **Diacritic mismatch traces** (`docs/debug_snapshots/oe_diacritic_mismatches_traces_2026-01-02.txt`) confirm these are orthography/diacritic alignment issues rather than phonology failures (e.g., `*tredăną → trēdan`, `*sturmăz → stōrm`, `*θurnuz → þōrn`, `*fadēr → fædēr`).
2622: - **Long-vowel missing probe narrowed** to 6 items (previously 7):
2623:   - Current list: `*kewwăną → ċeowwan (expected ċēowan)`, `*xazwăz → hærw (expected hǣr)`, `*xattuz → hatt (expected hōd)`, `*end → end (expected ān)`, `*slaxăną → sleaan (expected slēan)`, `*wegăz → weġ (expected wē)`.
2624:   - Traces in `docs/debug_snapshots/oe_long_vowel_missing_traces_2026-01-02d.txt`.
2625: 
```

#### Germanic/docs/DEV_NOTES.md:28646 (exact COUNTERPART)

- Nearby heading: ### §17.15.10  Citations

```text
28644: - Brunner, K. 1965. *Altenglische Grammatik*. §§182, 257 Anm. 1, 263.2, 288 Anm.
28645: - Campbell, A. 1959. *Old English Grammar*. §§407–409 (WGG), §§444, 608–609, 11554.
28646: - Clark Hall, J. R. *A Concise A-S Dictionary*, s.v. *hǣr-sife*.
28647: - Fulk, R. D. 2018. *Comparative Grammar of the Early Germanic Languages*. §5.9.
28648: - Hogg, R. 1992. *Grammar of Old English*, vol. 1, §§4.18–4.20.
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| hair | hǣr | inh | template:inh | hair |

#### old_english_swadesh.tsv

| NUMBER | ENGLISH | OLD_ENGLISH | IPA_RAW |
| :--- | :--- | :--- | :--- |
| 71 | hair | hǣr | /hæːr/ |

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:2547 (concept name)

- Nearby heading: ### OE diagnostics follow‑up: orthography + rhotacism (2025-12-22)

```text
2545: - Tracing those 7 (`bazją`, `deuzą`, `xazwăz`, `xuzdą`, `liznōjăną`, `mizdō`, `funxwstiz`) shows `EnglishZRhotacism` never fires; `ConsonantRules` leaves `{*z}` intact in every case.
2546: - Likely structural issue: `EnglishStarVocalic` (and other `EnglishStar*`) are defined before `GermanStar*` and appear to compile as literal symbols (foma logs show 1‑arc sets), so the rhotacism context never matches.
2547: - Even if the set is fixed, the current rule `V _ V` is historically too narrow: PGmc *z should rhotacize in post‑vocalic contexts like V‑z‑j/w/n/d‑V (berry, hair, learn, meed, hoard) before later glide/umlaut changes. Chronology: rhotacism must be early (before w‑glide changes and OE vowel rules).
2548: - `funxwstiz` (fist) is not a rhotacism case; it survives with a heavy `xʋst` cluster and fails the OE surface coda limit (needs separate cluster simplification / h‑loss logic).
2549: 
```

### Analysis and dossier hits

#### Germanic/docs/analysis/meord_med_chronological_review.md:235 (concept name)

- Nearby heading: ### 2.8 Campbell, *Old English Grammar* (1959)

```text
234: > usually remains, e.g. hord, reord, &c. (see § 123–4); but it is lost
235: > with compensatory lengthening in OE hād- hair (cf. ON haddr), mēd
236: > reward (beside meord), twīn linen (cf. Ger. zwirn); cf. OS līnon
```

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| HoggPhonology1992 | author + year mention (Hogg 1992) |
| Campbell1959 | author + year mention (Campbell 1959) |
| Fulk2018 | author + year mention (Fulk 2018) |
| ClarkHall1960 | single available key for Clark Hall |

### Low-confidence candidates

_None_

