# SC001–SC020 historical chronology and staging audit (2026)

Branch: `sc001-sc020-chronology-audit`. Baseline (verified live, not assumed):
**380 accepted / 373 matched / 7 mismatched / 0 ambiguous**,
`outputs_sha256 = a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc`.
This task changes **no** FST behavior; the baseline is unchanged.

## Method and the state of prior work

The axes are kept strictly separate (stable SC id ≠ historical stage ≠ scope ≠
relative chronology ≠ FST/technical dependency ≠ cascade position ≠ pipeline
bundle ≠ reader chapter/order). This audit does **not** renumber sound changes
and does **not** reorder the cascade.

A prior historical-cascade-order project already produced the canonical
**staging map** (`sound_change_historical_staging_map.tsv`, dated 2026-07-31)
and the **audit table** (`cascade_baseline/historical_audit_table.tsv`), and the
reader-facing chapters and per-rule dossiers were already reconciled. The
behavior-neutral Foma renames (`PGmcRhotacism → EAFRhotacism`,
`PGmcFinalZDeletion → EAFFinalZDeletion`) were already applied, with the
historical display names kept distinct from the stable implementation
identifiers.

The one artifact left **stale** by that work is
`sound_change_inventory.tsv`, whose `historical_stage` / `display_name` /
`historical_scope` for SC003, SC012, SC016 and SC020 still reflect the
pre-reconciliation labels (e.g. SC003 and SC020 marked `Proto-Germanic`). This
audit verifies the prior adjudications against the primary sources and then
reconciles the inventory. Every determination below was checked against the
dossiers **and** against the local source witnesses.

## Per-rule audit (SC001–SC020)

Full machine-readable matrix: `sc001-sc020-chronology-audit.tsv` (same
directory). Summary of findings:

### SC001 — Proto Input (support stage)
- `define EnglishProtoInput pgrmWord` (germanic.txt:3279) is an input handoff,
  not a historical sound change. `entry_type=support_stage`,
  `include_in_volume=no` already. **Decision: keep as support stage; record
  explicitly.** Action: `support_stage_not_sound_change`. No change.

### SC002 — Gm Simplification (*gm > *m)
- Verified genuinely Proto-Germanic, **not** assumed from the name. Kroonen
  (pp. 511, 101) gives *tauma-*, *drauma-* losing *g*, both marked DRV (with
  Verner's Law) — the *g is the Verner-voiced spirant [ɣ], lost before *m.
  No daughter language preserves *-gm-**, confirming a PGmc date. Action:
  `no_change`. Confidence A.

### SC003 — Rhotacism (PRIORITY)
- **What CAPR models:** medial `*z → *r` (`EAFRhotacism`,
  `{*z} -> {*r} || EnglishStarVocalic _ ?`); the right-context `?` blocks the
  word boundary, so final *-z is never rhotacized (it is deleted by SC020).
- **Historical stage:** **West Germanic, not Proto-Germanic.** Ringe & Taylor
  (vol. 2 §3.3.1 p. 98, and §2.3.1): "it can be proved that this 'rhotacism'
  occurred independently in Norse and in WGmc, and even in the latter group its
  application was not uniform." Crist (2002 §6) shows the WGmc/NGmc rhotacisms
  are **parallel, not shared** (the two branches preserve the *r/*z contrast
  through changes unique to each). Hogg (p. 37): Gmc *z → r intervocalically,
  "but in final position it is generally lost."
- **`EAFRhotacism` identifier:** the *display* name "West Germanic rhotacism"
  is correct; the internal `EAF`-prefixed identifier is a stable implementation
  name retained deliberately (renaming it would be churn without behavioral
  benefit). Documented as an alias.
- **SC020 < SC003 relation:** **historically defensible (confidence B).** Crist
  (2001 pp. 104–106; 2002): "rhotacism must have followed the rules eliminating
  *z by deletion." This is implemented by **scoping** (rhotacism is non-final),
  not by cascade position — correctly, because final *z is deleted before it
  could ever rhotacize.
- **Corpus forcing:** no corpus witness forces a *cascade reorder*; the
  SC003 < SC044 (OE Breaking) edge is a lexical terminus ante quem
  (`*líznōjaną > liornian`, not `lirnian`).
- **Do not move; do not rename the identifier.** Action: `metadata_only`
  (reconcile the stale inventory stage label).

### SC004 — Stressed *ai monophthongization (regression control)
- Already split from SC014 and adjudicated. Stressed/root `*ái > *ā`, North
  Sea Germanic / EAF operational corridor (Versloot 2017 two-wave, AD 400–900).
  Executes at cascade position 25 (after SC028 PNWGmcPreconsonantalXLoss) —
  position ≠ SC number, and that is fine. SC004 < SC036 (OEInterStressRaising)
  is a confirmed lexical edge (`*sáiwalō > sāwol`). No contradiction found.
  **Not reopened.** Action: `no_change`. Confidence B (analysis-dependent areal
  corridor).

### SC005 — NWGmc a-to-u before m
- Straightforward NWGmc vocalic change (Campbell §331(6)). The inventory flags
  that a NWGmc-labeled rule sits in the PWGmcChanges pipeline bundle — this is
  **harmless bundle placement**, not a historical error, and no executable
  dependency requires moving it. Preserve the supported edge **SC005 < SC017**
  (shoulders root vowel; Campbell §331(6)). Action: `no_change`. Confidence A.

### SC006–SC013 — PWGmc block (audited individually)
- **SC006** Early I Apocope, **SC007** Final Or Lowering, **SC008** Coronal W
  Assimilation, **SC009** Ij Contraction, **SC013** Dental Hardening (ð > d):
  all pan-WGmc, all `no_change`, all confidence A. No staging issues; not
  rubber-stamped — each checked against its dossier.
- **SC010 / SC011 — j-gemination before syllabic-j (verified, preserved):**
  OE *nett* requires `*natją > *nattją` — gemination (SC010) must precede
  syllabic-j resolution (SC011) (Ringe & Taylor vol. 2 p. 50). This
  **evidence-backed edge SC010 < SC011 is preserved.** (Also SC010 < SC049
  PGmcBAllophony, an fst_dependency: [β] surfaces only on singleton *b.)
- **SC012 — *lþ > ld* voicing (re-evaluated scope):** comparative evidence
  (Ringe & Taylor pp. 170–171; Campbell §414) supports *lþ > ld* most clearly in
  **northern West Germanic**, not as an unqualified pan-PWGmc development. Scope
  already corrected to `north_wgmc`, confidence lowered A → B, identifier
  renamed `PWGmcLThVoicing → EAFLThVoicing`. **Do not force it back to pan-PWGmc
  merely because its number sits among PWGmc rules.** Action: `metadata_only`
  (reconcile stale inventory stage/scope). Confidence B.

### SC014 — Unstressed *ai > *ē (regression control)
- Split from the former bundled SC004; NWGmc; executes at cascade position 1
  (the head of EarlyEnglishLineChanges) — position 1 vs SC number 14 is **not**
  an error. Unstressed *ai > *ē in final and nonfinal environments (R/T pp.
  37–41, §6.1.5). Bounded later by unstressed-long-vowel shortening (spanne).
  **Not reopened.** Action: `no_change`. Confidence A.

### SC015 — NWGmc I-lowering
- NWGmc i-lowering; ordered before SC017 u-lowering so the original high *u is
  visible. No staging issue. Action: `no_change`. Confidence A.

### SC016 — OE Ws Palatal Glide (ARCHITECTURAL CONTROL)
- **Historical stage = Old English / West Saxon** (Campbell §§171–172): glide
  insertion after an initial palatal before *u (yoke, young, youth).
- **Computational placement = earlier** (cascade position 12, inside the NWGmc
  region) because of a **demonstrated technical dependency** SC016 < SC017:
  `*júką > ġeoc` requires glide insertion before u-lowering, else `*ġoc`.
- The partial-order edge is **correctly classified `technical_dependency`, not
  historical chronology.** The reader-facing chapter (Ch. 4) already discloses
  this divergence explicitly ("computational dependency places SC016 … even
  though the cascade position precedes many Northwest Germanic changes").
- **Do NOT move the rule.** This is the canonical example of why historical
  stage and FST order must remain separate axes. Action: `metadata_only`
  (reconcile inventory). Confidence B.

### SC017 — NWGmc U-lowering
- Verified dependencies: SC005 < SC017 (historical, A) and SC016 < SC017
  (technical, A: geoc). Action: `no_change`. Confidence A.

### SC018 — Stressed monosyllable ō-raising
- Thin evidence; boundary-limited on both sides with no positive local
  chronology established (Campbell §122). **Confidence stays B — do not upgrade
  without evidence; the placement is unresolved but defensible.** Action:
  `no_change`.

### SC019 — Final long ō-raising
- NWGmc final bimoric `*-ō → *-u` (R/T pp. 30–31). Must fire **before** SC020 so
  that `*-ōz` (gen.sg.) stays sheltered by its *z* while bare `*-ō` (nom.sg.
  *gebō*) raises. Strong edge **SC019 < SC020** confirmed by the `*rástōz >
  ræste` history and the Foma ordering comment. Action: `no_change`.
  Confidence A.

### SC020 — Final *z deletion (PRIORITY)
See the dedicated mini-dossier below. **Historical stage = West Germanic, not
Proto-Germanic** (Crist 2002 §5: "Throughout WGmc, PGmc *z deletes word-finally
in unstressed syllables"; Campbell p. 166; Hogg p. 37; Kilday 2024). The single
computational rule (deletes *any* final *z) is broader than the literature's
unstressed-syllable conditioning, but is **safely scoped by the selected
PROTOFORM inputs** and does not overgenerate on the corpus. Scope (all-WGmc vs
a narrower Ingvaeonic subset) remains genuinely open (Crist distinguishes a
pan-WGmc rule from later Ingvaeonic deletions). `EAFFinalZDeletion` is retained
as a stable implementation identifier; the historical display name "West
Germanic final *z*-deletion" is correct. Action: `metadata_only` (reconcile
stale inventory). Confidence A (position) / B (scope).

## Final-*z*, rhotacism, and final-*s* — dedicated mini-dossier

These three affect final/sibilant material but are **distinct processes**; they
must not be conflated.

1. **What survives from PGmc.** PGmc had both `*s` (from PIE *s) and `*z`
   (from Verner's Law voicing of *s). They are distinct phonemes in PGmc.

2. **Which endings carry *s* vs *z*.** Thematic and many inflectional endings
   carried `*z` (e.g. masc. nom.sg. `*-az`, gen.sg. `*-ōz`/`-īnaz`). Final `*s`
   appears in a disjoint set of environments. The deletion at issue here
   concerns **final `*z`**, not final `*s`.

3. **Which deletion is common vs West Germanic.** The **word-final loss of `*z`
   in unstressed syllables is pan-West-Germanic** (Crist 2002 §5; Campbell p.
   166; Hogg p. 37; treated as established background by Kilday 2024). Crist's
   narrower contribution is a set of **later Ingvaeonic** `*z`-deletions (e.g.
   after front vowels `*i,*e`, and the *meord/heorde* problem cases), which are
   separate from and later than the pan-WGmc rule.

4. **Where rhotacism applies and does not.** Rhotacism (`*z > *r`) applies to
   **medial** `*z` (intervocalic, and in CAPR more broadly to medial VzC such
   as `*mízdō`); it does **not** apply word-finally, because final `*z` had
   already been deleted. Rhotacism is a **parallel innovation** in WGmc and
   NGmc, not a shared NWGmc change (R/T §3.3.1; Crist 2002 §6).

5. **Required ordering.** Final `*z`-deletion **precedes** rhotacism (Crist:
   "rhotacism must have followed the rules eliminating *z by deletion"). This
   is empirically forced: original `*r` does not delete in the relevant
   environments (`*miz, *wīz > OE mē, wē`, but `*hēr > OE her`), so deletion is
   sensitive to the original `*r`/`*z` contrast and must remove final `*z`
   before rhotacism could otherwise merge it with `*r`.

6. **What CAPR currently does.** SC020 `EAFFinalZDeletion` (`{*z} -> 0 || _ .#.`)
   deletes final `*z`; SC003 `EAFRhotacism` (`*z -> *r || EnglishStarVocalic _
   ?`) rhotacizes medial `*z`. The precedence of deletion over rhotacism is
   implemented by **scoping** (rhotacism's right context `?` excludes the word
   boundary), not by cascade ordering — which is correct, and matches the
   historical claim. SC019 < SC020 (raising before z-loss, sheltering `*-ōz`)
   and SC020 < SC040 (z-loss before medial u-lowering, `*bébruz > befer`) are
   both lexically supported.

**Stale prose check:** the only locus still claiming a PGmc stage for these is
`sound_change_inventory.tsv` (SC003/SC020 `historical_stage = Proto-Germanic`,
SC020 `display_name = PGmc Final Z Deletion`). The Foma comments, the staging
map, the audit table, and the reader-facing chapters are already correct. That
inventory staleness is reconciled in this audit; no other stale chronology
prose was found.

## SECURE NO-CHANGE ITEMS

SC001 (support stage, confirmed not a sound change), SC002 (PGmc, verified),
SC004 (EAF/NSGmc, split intact), SC005, SC006, SC007, SC008, SC009, SC010,
SC011, SC013, SC014, SC015, SC017, SC018 (B, uncertainty preserved), SC019.

## METADATA / READER-FACING CORRECTIONS

Behavior-neutral reconciliation of the stale `sound_change_inventory.tsv` to
match the already-adjudicated staging map / audit table / reader-facing state:

| SC | field | stale (inventory) | corrected |
|----|-------|-------------------|-----------|
| SC003 | historical_stage | Proto-Germanic | West Germanic (eaf corridor) |
| SC003 | historical_scope | pan-Germanic | pan_wgmc |
| SC012 | historical_stage | Proto-West Germanic | eaf / northern WGmc |
| SC012 | historical_scope | pan_wgmc | north_wgmc |
| SC020 | display_name | PGmc Final Z Deletion | West Germanic final *z*-deletion |
| SC020 | historical_stage | Proto-Germanic | West Germanic (eaf corridor) |
| SC020 | historical_scope | pan-Germanic | pan_wgmc |
| SC016 | review note | (vague) | clarify OE/West Saxon stage vs NWGmc cascade position is a documented technical dependency |

Foma identifiers `EAFRhotacism`, `EAFLThVoicing`, `EAFFinalZDeletion`,
`OEWsPalatalGlide` are **retained** as stable implementation names; the
historical display names differ and are documented. No Foma rename is performed
(the prior rename of the rule bodies is already done; only inventory labels are
reconciled).

## PROPOSED EXECUTABLE CHANGES

**None.** No historical evidence requires moving any SC001–SC020 rule in the
cascade. The one genuine stage-vs-position divergence (SC016) is a correct,
documented technical dependency and must **not** be moved. No `proposed_fst_move`
is recorded.

## UNRESOLVED QUESTIONS

- **SC018** stressed-monosyllable ō-raising: thin positive local chronology;
  confidence stays B. Placement defensible but not positively established.
- **SC020 scope:** all-WGmc vs a narrower Ingvaeonic subset for part of the
  deletion cluster remains open (Crist). The CAPR rule models the pan-WGmc core;
  the Ingvaeonic refinements are not separately modeled.
- **SC003 scope/uniformity:** the exact breadth of the rhotacism environment
  across WGmc daughters is non-uniform (R/T); CAPR's medial generalization is a
  defensible model, flagged but not resolved to finer grain.

These are recorded as open; the partial order is kept sparse and no false
precision is introduced.
