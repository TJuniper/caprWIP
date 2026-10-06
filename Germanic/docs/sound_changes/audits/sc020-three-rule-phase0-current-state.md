# SC020 three-rule programme — Phase 0 current-state audit

Date: 2026-08-16. Branch `sc001-sc020-chronology-audit`, HEAD `326c590e`.
Scope: exact executable state of the Old English cascade with respect to final
`*z` before any decomposition of SC020. No historical reinterpretation and no
implementation is contained in this document.

Baseline reproduced from a fresh in-container compile
(`foma -q -l fsts/germanic.txt -e quit` then `python3 tools/cascade_baseline.py`):
`lexemes=380 accepted=380 rejected=0 matched=373 mismatched=7 ambiguous=0`,
`outputs_sha256=a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc`
— identical to the committed
`cascade_baseline/cascade_baseline_summary.json`. Note: the baseline tool's
default `--bin old_english.bin` reads whatever bin is present in the container
cwd; running it against a stale bin produces a spurious one-row divergence
(`stem *stámniz → stemn` instead of `stefn`). The canonical procedure is
compile-then-baseline, as in `tools/build_cascade_baseline_docker.sh`.

## 0.1 Executable rules touching final `*z` (Old English path)

The OE transducer is `OldEnglish` = `OldEnglishCore .o. OEEpentheticVowel .o.
… .o. OldEnglishRemoveStars .o. OldEnglishSurface`, where `OldEnglishCore` =
`EnglishProtoInput .o. EarlyGermanicConsonantPipeline .o. EnglishProtoToOE`
(`germanic.txt` lines 3281–3283, 3416–3430).

### Rules that delete or rewrite `*z`

| Foma rule | Definition | Environment | Composition site | Executable position | SC ID |
|---|---|---|---|---|---|
| `EAFRhotacism` | `{*z} -> {*r} \|\| EnglishStarVocalic _ ?` (line 1126) | post-vocalic, **non-final only** (right context `?` requires a following symbol; word-final `*z` is immune by scoping, not by ordering) | `EarlyGermanicConsonantPipeline` (line 1248), before `EnglishProtoToOE` | **before manifest position 1** — see manifest-scope caveat below | SC003 |
| `PWGmcCoronalWAssimilation` | `{*d} -> {*w}, {*z} -> {*w} \|\| _ {*w}` (line 1518) | `*zw → *ww` (R/T §3.1.1 pp. 56–57) | `EarlyEnglishLineChanges` | manifest position 5 | SC008 |
| `EAFFinalZDeletion` | `{*z} -> 0 \|\| _ .#.` (line 1169) | **unconditional word-final deletion** | `EnglishProtoToOE`, immediately after `PNWGmcFinalLongORaising` | manifest position 16 | SC020 |
| `OldEnglishRemoveStars` | `{*z} -> z` (line 916, one clause of many) | surface star-stripping | `OldEnglishRules` tail (line 3425) | post-core surface layer | — |

Alias: `define EAFFinalZLoss EAFFinalZDeletion;` (line 1170). The alias is
defined but **never composed**; only `EAFFinalZDeletion` executes.

Surface filter: `OldEnglishSurfaceConsonant` (line 773) does **not** include
`z`. Any derivation retaining `*z` to the surface layer is star-stripped to
literal `z` and then rejected by `OldEnglishSurface` — it surfaces as
no-output, never as a z-bearing form.

### Rules with `*z` in their environment (feed or are bled by SC020)

| Foma rule | Relevant clause | Interaction | Position | SC ID |
|---|---|---|---|---|
| `PNWGmcAToUBeforeM` | `{*a} -> {*u} \|\| V C+ _ {*m} ({*i})? ({*z})? .#.` (line 1554) | optional `*z` right-context for dat.pl. `*-amiz` | manifest position 2 | SC005 |
| `PWGmcEarlyIApocope` | `{*i} -> 0 \|\| σ́ C+ V C+ _ {*z} .#.` (second clause, line 1595) | deletes third-syllable `*-i-` before final `*z`, creating `*-mz` clusters later stripped by SC020 | manifest position 3 | SC006 |
| `PNWGmcFinalLongORaising` | `{*ō} -> {*u} \|\| V C+ _ .#.` (line 2134) | must precede SC020 so gen.sg. `*-ōz` is sheltered from raising by its `*z` (comment at lines 3117–3123) | manifest position 15 | SC019 |
| `EnglishWeakTailVowelStar` (line 1044) / `OEARestorationStrongOTail` (line 1967) | enumerate `*z`-final ending shapes | context classes used by breaking/A-restoration | — | — |

Documented ordering constraints in `germanic.txt` comments:

- SC019 before SC020: shelter `*-ōz` from final-long-ō raising (lines 3113–3123).
- SC020 before `OEMedUnstressedULowering`: otherwise word-final `*-uz` is
  treated as medial and wrongly lowered (comment at lines 3124–3129,
  DEV_NOTES §17.10.25).
- SC020 not composed in `EarlyGermanicConsonantPipeline`: composing z-loss at
  the head would strip `*-z` from `*-ōz` before raising (comment at lines
  1238–1247, DEV_NOTES §17.10.24). Rhotacism instead protects final `*z` by
  its own `_ ?` scoping.
- Downstream chain for z-loss-exposed `*-ō`: `PWGmcFinalBareALoss`
  (position 38) and `PWGmcSurvivingBimoricOUnrounding` (position 39).

### Manifest-scope caveat

`tools/cascade_order_manifest.py` deliberately covers only `EnglishProtoToOE`
(expanding `EarlyEnglishLineChanges` inline). `EarlyGermanicConsonantPipeline`
(`PGmcGmSimplification .o. EAFRhotacism`) executes **before** manifest
position 1 but is absent from `cascade_order_manifest.tsv`. In executable
order, rhotacism runs first and word-final `*z` survives it by rule scoping;
the prose claim "z-deletion must run before rhotacism" describes the
historical chronology, not the executable order.

### Non-OE rules (excluded from this audit's scope)

German: `GermanConsonantShift` (`{*z} -> {*r} / V _ V`, line 3616),
`GermanAzLoss` (`{*z} -> 0 / _ .#.`, line 3752), `GermanRemoveStars`
(line 3732), `GermanLongVowelRules` (`*z` in context, line 3682).
Dutch: `DutchSibilantRules` (`z -> r / V _ V`, `z -> 0 / _ .#.`, lines
3562–3563). Modern-English path only (not in `old_english.bin`):
`EnglishShortVowelContextual` (`{u} -> {ʊ}` before `{*z}`, lines 1334–1335,
composed via `EnglishLMEShortVowelSplit` in `EnglishOEToModern`).

## 0.2 Frozen before-state

- Baseline: 380 accepted / 373 matched / 7 mismatched / 0 ambiguous / 0 no-output.
- Fingerprint: `outputs_sha256 = a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc`.
- The seven mismatches (unchanged): buck `*búkkaz` → †bocc (bucc), fowl
  `*fúglaz` → †fogol (fugol), fire `*fūri` → †fȳr (fȳre), rust `*rústō` →
  †rost (rust), tap `*táppô` → †tappa (tæppa), wolf `*wúlfaz` → †wolf (wulf),
  wool `*wúllō` → †woll (wull).
- SC020 firing count: **114** (committed inventory
  `sc020-final-z-firing-audit.tsv`, 114 rows; every OE-row PROTOFORM ending in
  `z` fires exactly once; zero anomalies). Note: `sound_change_inventory.tsv`
  records `trace_occurrence_count = 113` for SC020; the per-lexeme firing
  audit remains the authoritative count.
- Rule order around SC020 (manifest positions): 14
  `PNWGmcStressedMonosyllableORaising` → 15 `PNWGmcFinalLongORaising` → **16
  `EAFFinalZDeletion`** → 17 `PNWGmcUnstressedORaising`; bare-a loss at 38,
  surviving-bimoric-ō unrounding at 39; rhotacism pre-manifest (see caveat).
- Registry state: SC020 = `eaf` stage, `pan_wgmc` scope, chapter 3 position 2,
  confidence B, `rename_completed_scope_unresolved` (staging map); SC003 =
  `eaf`/`pan_wgmc`, chapter 3 position 1.

## 0.3 Lexical population (read-only census of `germanic-aligned-final.tsv`)

380 Old English rows (non-empty PROTOFORM, COUNTERPART ≠ "-").

- **PROTOFORMs ending in `z`: 114** — identical to the SC020 firing set.
- **Ending in consonant + `z`: 7**
  - stressed monosyllables (4): book `*bōkz`, flea `*fláuxz`, goose `*gánsz`,
    louse `*lūsz`;
  - polysyllabic consonant-stem/athematic types (3): friend `*fríjōndz`,
    milk `*mélukz`, month `*mḗnōθz`.
- **Ending in vowel + `z`: 107** (the ordinary thematic class, e.g. beard
  `*bárdaz`).
- **Stressed monosyllables ending in `z`: 4** — exactly the four Cz-final
  monosyllables above. The corpus contains **no** monosyllabic `*-Vz` form
  (no `*maiz`/`*hiz`/`*þiz`/`*hwaz` type): any later stressed-monosyllable
  `*-z` loss (hypothesis C) currently has **zero selected lexical witnesses**.
- **Negative controls (z in non-final position, survives to rhotacism):**
  berry `*bázjas` → berġes, deer `*déuzą` → dēor, hoard `*xúzdą` → hord,
  learn `*líznōjaną` → liornian (also `*líznô`, `*líznōθi`), meed `*mízdai`
  → meorde — 7 rows, 5 lexemes; these are SC003's trace witnesses.
- **No corpus form retains final `z` to any later outcome**: SC020 currently
  consumes the entire final-z population.

### Classification correction against the committed firing audit

`sc020-final-z-firing-audit.tsv` (committed at `1e310d94`) classifies flea
`*fláuxz` as *polysyllabic / unstressed ending*. Structurally `*fláuxz` has a
single nucleus (`áu`) and is a **stressed monosyllable ending in consonant +
`z`**, parallel to `*bōkz`/`*gánsz`/`*lūsz`. The committed mono/poly split of
111 / 3 should therefore be read as 110 / 4 for the structural criterion, and
flea belongs to the same candidate class as book/goose/louse for Dossier A
(hypothesis A: early consonant-final/root-noun nominative `*-z`
loss/simplification). Friend/milk/month (consonant-stem nominatives in
`*-Cz`) are likewise candidate Dossier-A material even though polysyllabic.
The committed TSV is left unmodified as a historical artifact; the
decomposition dossiers must use the corrected census above.

## Implications for the three-rule hypothesis (domains only, no adjudication)

- Hypothesis A candidate domain (consonant + `z` nominatives): 7 forms
  (4 monosyllabic, 3 polysyllabic).
- Hypothesis B candidate domain (unstressed `*-Vz`): 107 forms.
- Hypothesis C candidate domain (later stressed-monosyllable `*-z` after
  vowel): 0 corpus forms; comparanda must come from sources.
- 7 + 107 = 114 = current SC020 firing total; every firing has exactly one
  candidate destination class.
