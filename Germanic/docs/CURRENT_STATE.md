# Germanic project — current state (living entry point)

Keep this file tiny. Per-SC facts (status, verdicts, stages, memos) live only
in the canonical registry; do not duplicate them here.

## Current phase

Sequential per-SC adjudication of the sound-change cascade on branch
`sc001-sc020-chronology-audit`, one SC per instructed task.
The next SC is derived from the registry, never stated here:
`python3 Germanic/tools/adjudicate.py --next`

Method: `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` +
`Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md` are mandatory
for any sound-change history/chronology/staging/scope/FST-semantics work.

## Canonical sources

- `Germanic/docs/sound_changes/registry/sc_registry.tsv` — all SC metadata.
- `Germanic/docs/sound_changes/registry/chronology_edges.tsv` — all
  chronology relations and witnesses.
- `Germanic/docs/sound_changes/registry/sc_inventory_notes.tsv` — human
  inventory judgements only (`sc_inventory_annotations.tsv` is generated from
  it plus `germanic.txt` and the coverage census).
- Settled verdicts (generated view):
  `Germanic/docs/sound_changes/registry/settled_verdicts.md`.
- Navigation and the SOURCE/GENERATED/ARCHIVE map: `Germanic/docs/README.md`.

## Frozen baselines (must not change silently)

Recorded in
`Germanic/docs/sound_changes/cascade_baseline/cascade_baseline_summary.json`
and pinned by `Germanic/tests/test_cascade_baseline.py`:

- active original-380 identity fingerprint (`legacy_subset_sha256`):
  `04a24f4cd6ad61217a43ad47d5ac5f0d957a5f4f211559a7633d77dac852c409`
- selected-387 corpus fingerprint (`outputs_sha256`):
  `5d0330eabe0534101e3886ed17688d3eae08b7f67e4a9ec09df48a857218724f`

The immutable legacy380 archive still hashes to
`fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf`.
The SC056 adjudication explicitly migrates only gift's input by stable row ID;
all other legacy fields and every final output remain protected.

A fingerprint may change only as the explicit, row-level-diagnosed
consequence of an adjudication verdict (protocol step 13), never as a
routine refresh.

## Standard commands

- Next SC to adjudicate: `python3 Germanic/tools/adjudicate.py --next`
- Prepare an adjudication packet: `python3 Germanic/tools/adjudicate.py SCNNN --prepare`
- Executable evidence (container rebuild + live firing census + witness
  pre/post): `python3 Germanic/tools/adjudicate.py SCNNN --evidence`
- Control-plane refresh after ANY source edit (rule move, registry edit,
  prose edit): `python3 Germanic/tools/adjudicate.py --refresh`
- Finalize after SOURCE edits (control-plane refresh, then SC checks):
  `python3 Germanic/tools/adjudicate.py SCNNN --finalize`
- Full test suite: `cd Germanic/tests && python3 -m pytest -q`
- Debug-only: `python3 Germanic/tools/artifact_graph.py [--check|--refresh]`
  (the same graph `--refresh` drives)

## Instruction precedence

1. The current explicit user instruction.
2. `Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` (adjudication work).
3. `.github/copilot-instructions.md` (repo-wide conventions).
4. `docs/AGENTS.md` — a short routing rule pointing to the adjudication
   interface. An explicit user request to complete, commit and push an
   adjudication is itself the authorization for those operations.
5. Anything under `Germanic/docs/archive/` or `docs/archive/` is
   historical record, never instruction.
