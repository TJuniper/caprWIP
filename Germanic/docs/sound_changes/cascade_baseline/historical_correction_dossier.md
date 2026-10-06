# Correction dossier: rename / move / split / defer classes (Phase 6)

Consolidated, source-linked correction proposal for the audited early rules,
grouped by the six adjudication classes. This is the review checkpoint: no
production FST is reordered, renamed, split, or redefined by this commit series.
All judgements trace to `historical_audit_table.tsv`,
`historical_reconciliation.md`, `historical_partial_order.tsv`, and
`historical_cascade_proposal.md`.

**Overarching result:** the current executable order already satisfies every
supported historical edge (0 violations). No cascade move is proposed. The
corrections are relabelling, a scope narrowing, one split candidate, and one
deferral.

Rename migration footprint (for the four rename candidates): the four legacy
identifiers occur ~3168 times across 116 files, but only the FST source is
behaviour-bearing — `Germanic/fsts/germanic.txt` (35 refs incl. the sandbox
mirror) and `Germanic/tools/oe_full_trace_report.py` stage list. The rest are
regenerable trace snapshots, order-test summaries, reader-facing prose, book
assembly, and registries, all updated mechanically. Renames change no rule text,
so the expected computational risk is **behaviour-neutral** (frozen
`outputs_sha256` must be unchanged); the practical risk is reference-migration
completeness, mitigated by temporary aliases.

---

## Class 1 — right name, right position (no correction)

20 rules, verified against reader-facing prose and the partial order:

SC005, SC006, SC007, SC008, SC009, SC010, SC011, SC013, SC014, SC015, SC017,
SC019, SC021, SC022, SC023, SC024, SC025, SC028, SC041, and SC018.

Notes: SC018, SC022, SC025 carry confidence B in the registry (boundary-limited
positive chronology); their **position is not independently pinned** but no move
is warranted or proposed. SC041's `PWGmc` name is source-correct (Ringe & Taylor
pp.60–61 date final short-low-vowel loss to PWGmc).

---

## Class 2 — wrong name, right position (rename or metadata; no move)

### SC003 `PGmcRhotacism`
- Present: internal name asserts Proto-Germanic; medial `*z > *r`; pre-pipeline
  in `PGmcConsonantRules`.
- Proposed: rename to a West Germanic rhotacism identifier; keep position (the
  historical "after final-*z* deletion" relation is realised by scoping to
  non-final environments, not by ordering).
- Local CAPR evidence: `reader_facing/003-west-germanic-rhotacism.md`;
  `change_reports/full/003-pgmc-rhotacism.md`.
- Scholarly basis: Ringe & Taylor pp.52, 98, 102; Crist 2001 pp.104–106,
  Crist 2002 pp.1,4; Hogg p.37.
- Confidence: A. Granularity: single (implementation broader than strictly
  intervocalic — note only).
- Files: germanic.txt; oe_full_trace_report.py; inventory; staging map; aliases;
  reader-facing anchors `#rule-PGmcRhotacism`.
- Risk: behaviour-neutral rename.

### SC020 `PGmcFinalZDeletion`
- Present: name asserts Proto-Germanic; `*z > 0 / _ #`; position 17.
- Proposed: rename to a West Germanic final-*z* deletion identifier; keep
  position (SC019 < SC020 < SC040 both lexically forced, A).
- Evidence: `reader_facing/020-wgmc-final-z-deletion.md`; dossier 020.
- Basis: Hogg p.37; Crist 2002 p.1.
- Confidence: A (name/position); **open question**: exact scope (all-WGmc vs
  Ingvaeonic) and relation to SC003 rhotacism — flag for a joint scope audit.
- Files: as SC003.
- Risk: behaviour-neutral rename (scope decision is metadata, later).

### SC026 `NWGmcNasalSpirantLengthening` / SC027 `NWGmcNasalSpirantLoss`
- Present: names assert Northwest Germanic; the pair models one North Sea
  Germanic / Ingvaeonic nasal-loss development; positions 23–24.
- Proposed: rename both to North Sea Germanic / Ingvaeonic identifiers; keep the
  two-rule model split (defended) and keep positions (SC026 < SC027 lexically
  forced, A: fist/goose/youth).
- Evidence: `change_reports/full/026-027-nasal-spirant-corridor.md`.
- Basis: Campbell §121; Fulk §4.11; Luick §§299, 301.1; Sievers-Brunner §186.1;
  Ringe & Taylor pp.140–141.
- Confidence: B. Registry stage already `ingvaeonic`.
- Files: as SC003 (×2 identifiers).
- Risk: behaviour-neutral rename.

### SC012 `PWGmcLThVoicing` (metadata/scope, not rename-critical)
- Present: `hist_scope=pan_wgmc`, confidence A, "no staging issue"; `*θ>*d / *l _`.
- Proposed: narrow scope `pan_wgmc → north_wgmc`; downgrade confidence A → B;
  optionally qualify the `PWGmc` implication in prose. No move.
- Evidence: `reader_facing/012-lth-voicing.md`; `change_reports/full/012`;
  dossier 012.
- Basis: Ringe & Taylor pp.170–171 (northern WGmc); Campbell §414. The research
  layer explicitly rejects an unqualified pan-PWGmc conclusion.
- Confidence: B. Risk: metadata/prose only, behaviour-neutral.

### SC042 `PWGmcSurvivingBimoricOUnrounding` (prose)
- Present/proposed: keep name and position (feeds SC043); present as a narrow
  model-shaped feeder in prose, not a coequal chapter.
- Evidence: `change_reports/full/042`; Campbell §§131,157–158; Hogg pp.101,119;
  Ringe & Taylor pp.157–158, 189–190. Confidence B. Risk: prose only.

---

## Class 3 — right name, position diverges by documented dependency (prose only)

These sit at cascade positions that differ from their historical stage for
**computational** reasons. No move; the correction is trace/prose clarity that
stage ≠ order.

### SC016 `OEWsPalatalGlide`
- OE West Saxon (Campbell §44), but position 13 (before many NWGmc rules) because
  `*júką > ġeoc` needs glide insertion before SC017 u-lowering. Technical
  dependency, A. Prose/trace must state the stage is OE-WS.

### SC049 `PGmcBAllophony`
- PGmc/PWGmc `*b` stop/fricative allophony (Hogg pp.101–102; Ringe & Taylor
  p.121), but position 46 because `[β]` must surface only on singleton `*b` after
  SC010 j-gemination. FST dependency, A. Divergence already documented; keep.

### SC050 `SieversLawSyncope`
- Sievers' Law (Adamczyk 2001; Fulk §6.15), placed at 47 as a feeder into OE
  palatalization (SC051/SC052). FST dependency, B. Document the feeder role.

### SC018 `NWGmcStressedMonosyllableORaising`
- Name/stage right (Campbell §122); position boundary-limited (confidence B). No
  move; note the thin positive local chronology.

---

## Class 4 — wrong name, wrong position

**Empty.** No audited rule both misstates its stage *and* sits in an
order-violating position. SC003's early position is resolved by scoping, so it is
a rename-only case (Class 2), not a wrong-position case.

---

## Class 5 — wrong or uncertain granularity (split candidate)

### SC004 `PWGmcAiMonophthongization`
- Present: one FST composing `*ai>*ē /_#`, `*ai>*ā`, `*ái>*ā`.
- Finding: `definitely_conflated`. The word-final `*ē` merger is an early
  Northwest-Germanic vowel shift (Ringe & Taylor pp.40–41); the nonfinal `*ai>*ā`
  generalization is model-sharpened and less securely dated.
- Proposed: **split candidate** — separate the early NWGmc word-final component
  from the nonfinal generalization. No rename until the split is decided
  (renaming a conflated rule first would prejudge it).
- Evidence: `reader_facing/004-pwgmc-ai-monophthongization.md`;
  `change_reports/full/004`.
- Confidence: B. Lexical anchor: SC004 precedes OEInterStressRaising (A:
  *sáiwalō > sāwol).
- Files: germanic.txt (rule body), sandbox mirror, trace stage list, registries.
- Risk: **substantive** — a split changes intermediate forms and must be
  validated with the output baseline and witness review (Phase 7); it is a
  separate, review-gated task, not part of the rename increment.

---

## Class 6 — historically unresolved (defer)

### SC064 `NWGmcInStemNLoss`
- Registry-internal conflict: `hist_stage=nwgmc` but `v1_chapter=4` (OE);
  confidence C. Narrow witness-driven `*n`-loss after `*ī` (`*furht-` / `fright`
  → `fyrhte`; Kroonen p.201), operating in the OE post-apocope tail. Its position
  after OE high-vowel apocope is cross-source supported (Ringe & Taylor vol.2
  pp.71–72; Campbell §§472–473; Brunner §280; Fulk §7.34; Bammesberger §7.3.4).
- Proposed: **defer** the stage/name adjudication. Position is fine; the stage
  label is genuinely unresolved. No change now.

---

## Recommended first implementation increment (after approval)

1. The four behaviour-neutral renames (SC003, SC020, SC026, SC027) as one
   controlled identifier migration with temporary aliases, validated by
   `outputs_sha256` equivalence and full-cascade equivalence, then alias removal.
2. SC012 scope narrowing + confidence downgrade (metadata) and the
   SC016/SC042/SC049/SC050/SC018 prose/trace clarifications.
3. Separately and review-gated: the SC004 split and the SC064 stage adjudication.

**Stop for review here.** No production FST change is made by this task.

---

## Ontology update (supersedes the proposed names above)

The canonical stage/scope ontology (`canonical_stage_scope_ontology.md`) now
governs the internal identifiers. The internal Foma prefix encodes the
chronological stage on the axis PGmc → PNWGmc → PWGmc → EAF → OE; geographical/
genealogical distribution is carried separately in `hist_scope`. The earlier
"West Germanic rhotacism" style names in this dossier were reader-facing
descriptions; the **internal identifiers** now adopt stage-prefixed canonical
forms. The full former→canonical mapping and per-rule status live in
`rename_migration_manifest.tsv`.

Canonical internal identifiers (superseding earlier proposals):

| SC | Former identifier | Canonical identifier | Reader-facing title |
| --- | --- | --- | --- |
| SC003 | `PGmcRhotacism` | `EAFRhotacism` | West Germanic rhotacism |
| SC020 | `PGmcFinalZDeletion` | `EAFFinalZDeletion` | West Germanic final *z*-deletion |
| SC012 | `PWGmcLThVoicing` | `EAFLThVoicing` | Northern West Germanic *lþ*-voicing |
| SC026 | `NWGmcNasalSpirantLengthening` | `EAFNasalSpirantLengthening` | North Sea Germanic nasal-spirant lengthening |
| SC027 | `NWGmcNasalSpirantLoss` | `EAFNasalSpirantLoss` | North Sea Germanic nasal-spirant loss |
| SC043 | `AngloFrisianBrightening` | `EAFBrightening` | Anglo-Frisian brightening |
| SC005, SC014, SC015, SC017, SC018, SC019, SC023, SC024, SC025, SC028 | `NWGmc…` | `PNWGmc…` | Proto-Northwest Germanic … |
| SC021 | `NWGmcUnstressedORaising` | retired | Former PNWGmc unstressed-o raising retired; successors are SC071/SC099/SC100 |
| SC022 | `NWGmcMnDissimilation` | `PNWGmcMnDissimilation` | Common Germanic Mn Dissimilation; stable executable identifier is not a stage claim |

`EAF` is an operational post-PWGmc/pre-OE corridor, not a claim of a discrete
Proto-Anglo-Frisian node; "Ingvaeonic" remains a scholarly alias for
`north_sea_germanic`, not a stage. SC004 and SC064 remain unrenamed (deferred);
SC016, SC041, SC042, SC049, SC050 remain unrenamed (not required — their
positions diverge from stage by documented dependency, to be explained in prose,
not converted).

---

## Migration completed (relabelling phase)

All 18 renames in `rename_migration_manifest.tsv` are `completed`, each as one
behaviour-neutral commit validated by the rename gate (A compile + no alias, B
`outputs_sha256` identity, E executable-order identity, G former-name audit) plus
the host test suite. Commit SHAs are recorded per row in the manifest
(`migration_commit`). No Foma compatibility alias was ever committed.

Order of migration: least-entangled EAF renames first (SC003, SC020, SC026,
SC027, SC043), then SC012 (which also left the PNWGmc×PWGmc interaction matrix on
becoming `eaf`), then the twelve PNWGmc renames (SC005, SC014, SC015, SC017,
SC018, SC019, SC021, SC022, SC023, SC024, SC025, SC028).

### Container audit (Section 8)

Two containers were historically mixed after the renames and were given neutral
architectural names (behaviour-neutral, contents/order unchanged):

- `PGmcConsonantRules` → `EarlyGermanicConsonantPipeline`
  (members: `PGmcGmSimplification` [pgmc], `EAFRhotacism` [eaf]).
- `PWGmcChanges` → `EarlyEnglishLineChanges`
  (members span pnwgmc → pwgmc → eaf, incl. `PNWGmcAToUBeforeM`, the pwgmc
  SC006–011/013 rules, `EAFLThVoicing`, and the SC004 transition rule).

`EAFLThVoicing` (SC012) and `EAFRhotacism` (SC003) executing inside PWGmc-/PGmc-
named containers is a documented technical position, not a stage claim; the
container names no longer assert homogeneous membership.

### `nwgmc` retained only for deferred SC064

Legacy stage `nwgmc` / scope `pan_nwgmc` remain in the registry **solely** for
the deferred `NWGmcInStemNLoss` (SC064), whose stage is unresolved (do not
rename). The interaction-matrix membership test therefore queries the earlier set
as `{nwgmc, pnwgmc}` so SC064 stays in scope.

### Trace-snapshot staleness finding (not a rename effect)

Regenerating `docs/debug_snapshots/oe_full_trace_report.txt` moved `stem` from
the `exact_match` bucket (373) to a mismatch bucket, giving 372 exact matches + 8
documented mismatches = 380 — exactly the frozen baseline
(`cascade_baseline_summary.json`). The previously committed snapshot was stale
(it predated `stem` becoming a documented mismatch). Gate B confirms every rename
preserved `outputs_sha256`, so this correction is orthogonal to the relabelling;
after normalising former→canonical identifiers, no other lexeme's derivation
differs.
