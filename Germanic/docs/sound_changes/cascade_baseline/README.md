# Germanic cascade baseline (Phase 1)

This directory freezes a reproducible baseline of the current Old English
cascade, so that the historical-cascade-order reorder can later be proven
output-equivalent. It is descriptive only: it records what the cascade does
today and encodes no historical stage judgement.

## Why an output baseline (not a bin checksum)

Foma compilation is **byte-non-deterministic**: recompiling `germanic.txt`
produces `.bin` files with different checksums on every run, even from identical
source. The baseline is therefore anchored on **outputs**, not compiled
artifacts. The reproducibility marker is `outputs_sha256` in
`cascade_baseline_summary.json`, computed over the canonical
`proto_norm -> sorted-outputs` projection. Two independent recompiles produce
byte-different bins but the **same** `outputs_sha256`.

## Artifacts

- `cascade_baseline_outputs.tsv` — one row per Old English lexeme
  (`DOCULECT == Old_English` in `data/germanic-aligned-final.tsv`), recording the
  normalised proto input, acceptance, the full order-independent output set,
  output multiplicity, and whether the attested counterpart is produced.
- `cascade_baseline_summary.json` — aggregate counts plus `outputs_sha256`.
- `cascade_order_manifest.tsv` — the actual executable rule order flattened from
  the `EnglishProtoToOE` composition in `germanic.txt` (with the `PWGmcChanges`
  block expanded inline). Descriptive record of the current order only.

## Regenerating

```bash
bash Germanic/tools/build_cascade_baseline_docker.sh
```

This recompiles the production cascade in the backend container, recaptures the
output baseline, and regenerates the order manifest. `cascade_baseline_summary.json`
must be unchanged across runs; if `outputs_sha256` changes, the cascade behaviour
changed and that must be explained, not silently accepted.

The host-runnable invariants (`Germanic/tests/test_cascade_baseline.py`) verify
the artifacts are internally consistent and that the order manifest is an exact,
current projection of `germanic.txt`. The output-hash reproducibility contract is
exercised by the Docker wrapper because it requires the transducer.

## Current baseline snapshot

The original snapshot below is historical. The current selected corpus has
387 deterministic outputs, 380 matches and seven existing mismatches.
Approved gift, context, knee-cell and hue-input transitions preserve their
separate before-baselines and the immutable original380 archive.

Hue's approved PROTO = PROTOFORM = *xíwją retains hīew but changes
the input-sensitive selected387 projections. The exact receipt is
`approved_hue_input_migration.json`, applied only by:

```bash
python3 Germanic/tools/adjudicate.py SC033 --adopt-cell-baseline \
  --approval approved_hue_input_migration.json
```

The validated transition id `hue` names separate
`cascade_baseline_outputs_pre_sc033_hue.tsv` and
`cascade_baseline_summary_pre_sc033_hue.json` archives. The original knee
receipt and pre-SC033 archives are untouched; no hue mapping is added to
the original380 migration list because hue is outside that set. The
validator rejects all undeclared record, target, output, multiplicity and
context changes and verifies archive integrity. Routine refresh does not
adopt a baseline.

- 380 Old English lexemes, all accepted, 0 ambiguous outputs.
- 372 match the attested counterpart; 8 are pre-existing documented mismatches
  (`buck`, `fowl`, `fire`, `rust`, `stem`, `tap`, `wolf`, `wool`), tracked in
  `data/oe_known_problems.tsv`. These are not reopened by the reorder work.

These counts are a pre-reorder snapshot; the permanent contract is that the
reorder must not change the accepted-input set, the output sets, or the output
multiplicity, i.e. `outputs_sha256` must be preserved unless a change is an
individually reviewed scientific correction.
