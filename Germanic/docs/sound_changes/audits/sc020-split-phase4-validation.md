# SC020 three-rule split — Phase 4 regression and historical-behaviour validation

Branch `sc001-sc020-chronology-audit`. Validates the Phase 3 implementation
(commits `d9fc82ae` FST + `b29add0a` registries) against the frozen Phase 0
before-state (`sc020-three-rule-phase0-current-state.md`) and the
adjudication memo (`sc020-three-rule-adjudication.md`).

## 1. Final-output invariant — PASS (fingerprint exactly unchanged)

Canonical baseline (`tools/cascade_baseline.py` in the backend container,
`cascade_order_manifest.py` on the host):

| metric | Phase 0 frozen | after split | verdict |
|---|---|---|---|
| lexemes | 380 | 380 | unchanged |
| accepted | 380 | 380 | unchanged |
| matched | 373 | 373 | unchanged |
| mismatched | 7 | 7 | unchanged (same identities) |
| ambiguous | 0 | 0 | unchanged |
| no-output | 0 | 0 | unchanged |
| `outputs_sha256` | `a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc` | `a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc` | **identical** |

The committed baseline artifacts under `cascade_baseline/` are byte-identical
to the pre-split state; no refreeze was needed or performed.

## 2. Intermediate-trace invariant — PASS (traces changed exactly as designed)

Full-corpus trace (`tools/oe_full_trace_report.py --all` against the
recompiled sandbox checkpoints):

- **SC096 `RootNounNomZLoss`** fires on exactly **4** lexemes — book
  `*bōkz`, flea `*fláuxz`, goose `*gánsz`, louse `*lūsz` — at the head of
  the pipeline (checkpoint `after_root_noun_nom_z_loss`, position 1).
- **SC020 `EAFFinalZDeletion`** (narrowed) fires on exactly **110**
  lexemes, including friend `*fríjōndz` (as contraction-created
  `*fríundz`, clause ii), milk `*mélukz`, and month `*mḗnōθz`
  (checkpoint `after_eaf_final_z_deletion`, position 17).
- **SC097 `MonosyllabicFinalZLoss`** fires on **0** corpus lexemes
  (adjudicated as genuine but presently unwitnessed); validated by
  synthetic unit examples (`hwaz → hwā`, `hiz → hī` with lengthening;
  `kūz`, `maiz`, `kōz` nucleus preserved) during Phase 3 scratch testing.
- **Negative controls:** medial `*z` destined for rhotacism still
  rhotacizes — `*déuzą → dēor`, `*bázjas → berġes`, `*xúzdą → hord`.
- **Friend ordering constraint:** `*fríjōndz` passes SC096 untouched
  (still uncontracted/polysyllabic at position 1), is contracted to
  `*fríundz` by `PWGmcIjContraction` (position 7), and loses its `*-z`
  under SC020 (position 17). The regenerated interaction matrix confirms
  `RootNounNomZLoss × PWGmcIjContraction = NONCOMMUTE` and
  `RootNounNomZLoss × EAFFinalZDeletion = commute` (clean partition).

## 3. Full accounting of former SC020 firings — PASS (114/114)

Per-lexeme table: `sc020-split-before-after-firing-table.tsv` (114 rows:
lexeme, selected input, old deleting rule, new deleting rule, form
before/after the new rule, before/after checkpoint bins, Phase 0 proposed
process, reconciliation note).

| fate | count | lexemes |
|---|---|---|
| SC096 RootNounNomZLoss | 4 | book, flea, goose, louse |
| SC020 EAFFinalZDeletion (narrowed) | 110 | all remaining former firings incl. friend, milk, month |
| SC097 MonosyllabicFinalZLoss | 0 | — (unwitnessed) |
| unaccounted / anomalies | 0 | — |

Reconciliation against the Phase 0 proposals
(`sc020-final-z-firing-audit.tsv`): book/goose/louse were proposed there
as `later_northern_final_z_loss` and flea as
`early_unstressed_final_z_loss` (on a polysyllabic misreading of the
`*áu` diphthong); all four were re-adjudicated to the root-noun process
by Dossier A and the adjudication memo §5, and the implementation matches
the adjudication, not the superseded Phase 0 guesses. The other 110 match
the Phase 0 proposal (`early_unstressed_final_z_loss` → SC020).

## 4. Test suite and machinery gates — PASS

- `cd Germanic/tests && python3 -m pytest -q` → **204 passed** (baseline
  204), including the new ordering-pair assertions
  (A < `PWGmcIjContraction`, B < C, SC018/SC019 raisers < C) and the
  updated SC020 stage guard (Proto-West Germanic per Dossier B).
- Cross-artifact consistency (`test_sc_chronology_cross_artifact.py`)
  green across audit matrix / inventory / staging map / order manifest.
- Registry coverage (`test_rule_registry.py`) green: every executable rule
  incl. SC096/SC097 has exactly one inventory row.
- `tools/oe_bin_sync_check.py` → "OE bin sync check OK" (all stage
  checkpoints, including the two new ones, present and fresh).
