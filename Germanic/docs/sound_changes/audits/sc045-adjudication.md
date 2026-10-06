# SC045: separate voiceless palatal articulation from voiced-fricative merger

## Identity

- SC id: SC045; executable identifier: `OEVelarFricativePalatalization`.
- Branch/base: `update`, `16196823`; post-SC043 baseline.

## Question

Does the unwitnessed literal ɣ → j branch conflate voiced merger with the
actual x → ç population and lead the reader to infer one chronology?

## Current state (before any edits)

Registry: `oe/english_specific`, A, unadjudicated. Three x → ç and three
ɣ → j contexts occur before/after a front vowel or before j. The rule is
between breaking and restoration. Canonical inputs never fire the literal
voiced branch. Consulted the 042–048 dossier and SC045 chronology card.

## Diagnosis

The 24 live applications are hail, hair, hall, harm, harvest, have, haw,
hawk, hay, hazel, head, heart, hearth, heaven, hedge, helm, help, herd,
hew, hind, hold, laugh and hue. All are x applications, not voiced merger
witnesses. Fee/fight are displacement negatives: breaking has removed
the front-vowel context while preserving its velar-fricative trigger.
Moving palatalization earlier prevents the intended breaking. They do
not establish live voiced-g applications or direct feeding into SC045.
Six supplies only a more distant displacement constraint.

## Literature

Existing CAPR dossier: 042–048 region.
Ringe–Taylor 2014 pp.203–214 and Fulk 2018 pp.130–132 distinguish voiced
fricatives/stops and merger; Ringe–Taylor p.204 puts voiced merger after
mutation. Hogg 1979 pp.102–111 preserves the disagreement.
Breaking's conventional vowel context is discussed by Campbell 1959
pp.54–56 and Fulk 2018 pp.73–74.

CAPR retains the x implementation but removes the unused early voiced
shortcut. Literal ɣ now passes to the separately modeled voiced articulation
and postmutation merger, rather than being made j before restoration.

## Historical analysis

Stage/scope/secure x-law confidence retained; no new precise date is
inferred from the executable slot. The breaking/SC045 displacement
relations concern x and counterbleeding protection, not voiced merger.
No chronology edge is promoted from this component separation.

## Verdict

RESTRICT/SPLIT the early identity to voiceless articulation, retaining its
three literal x contexts and all corpus outputs. The voiced account belongs
to the separately adjudicated SC052/SC109 path.

Registry-verdict: SC045=RESTRICT/SPLIT

## Propagation (only after verdict)

FST, SC045 registry/human notes, 042–048 dossier and 044–045 reader.
Regressions check x positive, literal ɣ passthrough, unchanged 24-row
population, source-reader body fidelity and full corpus invariance.
Baseline/fingerprint effect: none. Finalization recorded at batch closeout.

## Residue

The retained voiceless proxy and its displacement witnesses do not settle
the onset of every h allophone or its exact historical chronology.

## Batch closeout

SC045 finalization and propagation passed. The integrated suite passed
688 tests and 6178 subtests; the current-source protected assay
(`oe_adopted_palatal_result.json`) passed the x positive and literal voiced
passthrough controls within its 31 component checks. All 387 finals and
selected inputs are preserved, with no missing/ambiguous output or protected
artifact changes.

The standard book build passed all gates. Inspection of printed p.77 in the
297-page PDF confirms the x-only definition and fee/fight displacement-negative
argument, including correction of the older opening sentence that still
implied a live subsequent change. No voiced chronology or new historical
edge is inferred from those negatives. No commit or push is authorized.
