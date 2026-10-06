# SC004 historical options report and recommendation

> **Superseded in detail by the corrected PROTOFORM pass (commit `9c71aed3`).**
> The component evidence below (SC014 "zero corpus load"; loam/whine as
> unaccented SC004 cases) was computed from the cognate-set `PROTO` field. Under
> the production `PROTOFORM`, SC014 has two corpus witnesses (span, meed), loam
> is a stressed SC004 case, and whine is not an ai case. The Outcome-C
> recommendation (a two-rule historical split) still stands and is implemented;
> only the corpus attributions are corrected. See
> `sc004_component_application_report.tsv`. Retained as a historical research
> record.

Research only. Evaluates the three analytical outcomes for SC004
`PWGmcAiMonophthongization` and makes a definite recommendation. **No production
change is made** (task §10): the production rule is not replaced, no SC number is
assigned, nothing is moved or renamed, and SC064 is untouched.

Inputs: `sc004_component_dossier.md` (application report),
`004-sc004-component-reconciliation.dossier.md` (sources),
`sc004_split_candidate_and_proof.md` (equivalence),
`SC004-components-chronology.md` (component chronology).

## What is established vs what is a modelling choice

**Scholarship establishes** (subject to the Versloot 2017 `[verify]` flag):

- Word-final unstressed `*-ai > *-ē` (**A**) is an early, shared (Proto-)Northwest
  Germanic change, outcome `*ē` [@RingeTaylor2014, pp. 40--41; @Fulk2018, §5.2].
- The stressed / nonfinal `*ai/*ái > *ā` (**B+C**) is a later development, outcome
  `*ā` (OE `ā`, front `ǣ` by later fronting), characteristic of North Sea
  Germanic / Anglo-Frisian, of areal/wave character rather than a clean inherited
  node [@Campbell1959; @HoggGrammar1992; Versloot 2017 verify].
- A and B+C differ in **outcome, date, comparative scope, and mechanism**.
- **B and C are one development** (identical outcome `*ā`; the split is only the
  FST's stress marking).

**CAPR-derivational facts:**

- A has **0** corpus applications; B+C carries **all 26**.
- The one SC004 chronology boundary (SC036 `soul`) is a **Component C** event.
- The split A vs (B+C) is **behaviour-neutral** (proven equivalent).

**Modelling choice (not settled by scholarship):** which CAPR chronological
*stage* to assign a geographically diffused change, and whether a corpus-inert
but historically real change deserves its own SC number.

## Outcome A — one historical change (conditioned outcomes)

Tenable only if A and B+C are one change with conditioned reflexes and the
support imbalance is a documentation gap. **Rejected.** A and B+C have *different
outcomes* (`*ē` vs `*ā`), not one outcome with allophony, and the sources date
and locate them differently (early NWGmc inheritance vs later North-Sea-Germanic
areal diffusion). One `define` currently conceals two distinct mergers; the audit
table's `definitely_conflated` verdict is source-supported. This is not a single
change.

## Outcome B — two implementation components, one reader-facing change

Tenable if the A vs B+C distinction were computationally useful but *not
historically substantial*. **Rejected.** The distinction is historically
substantial on every axis (outcome, date, scope, mechanism). A single
reader-facing discussion would have to narrate two different mergers of different
ages as one, which the sources do not support. (Outcome B *is* the correct
analysis for **B vs C** internally — see below — but not for A vs B+C.)

## Outcome C — two historical changes  ✅ RECOMMENDED

A and B+C are demonstrably different in chronology, scope, mechanism, and source
tradition, so a **formal split into two historical changes** is warranted:

- **Change 1 — general `*ai/*ái > *ā`** (Components B+C). Keeps the legacy
  **SC004** identity: it carries every corpus witness, the existing reader
  chapter, and the SC036 `soul` boundary.
- **Change 2 — word-final unstressed `*-ai > *-ē`** (Component A). Gets a
  **provisional** research identifier; it is historically real but **corpus-inert**
  (0 lexemes), evidenced by inflectional endings only.

### B vs C stay one change

Do **not** split B from C. They are one development (stressed-root `*ai > *ā`)
divided only by the proto's stress marking; B's two lexemes (loam, whine) are
`early_analogy` with root `*ai` whose accent is absent from the proto. Internally
this is an Outcome-B situation (two Foma rewrites, one change) nested inside the
Outcome-C split of A vs (B+C).

### Proposed canonical assignments (proposal only — not applied)

| | Change 1 (keeps SC004) | Change 2 (provisional) |
| --- | --- | --- |
| research id | `SC004.general-ai-to-a` | `SC004.final-ai-to-e` |
| Foma rewrite | `[{*ai}->{*ā}] .o. [{*ái}->{*ā}]` | `{*ai} -> {*ē} \|\| _ .#.` |
| proposed Foma id | `EAFAiMonophthongization` | `PNWGmcFinalUnstressedAiRaising` |
| proposed display | North Sea Germanic *ai*-monophthongization | Proto-Northwest Germanic word-final *ai*-raising |
| proposed hist_stage | `eaf` (operational corridor for the areal change) | `pnwgmc` |
| proposed hist_scope | `north_sea_germanic` (Anglo-Frisian) | `north_wgmc` / pan-NWGmc (shared) |
| proposed confidence | B (later date/scope broad-far) | B (well-attested but corpus-inert) |
| book location | Chapter 3 (post-PWGmc / Anglo-Frisian) | Chapter 2 (PNWGmc), or a short note |
| corpus load | 26 | 0 |

Stage names are proposals under the canonical ontology; because SC004's stage is
being *resolved* here (not merely relabelled), assigning `EAF` to Change 1 is a
new analytic claim, not the mechanical rename the earlier phase excluded.

### Computational adjacency

The two changes may remain **computationally adjacent** in the cascade: the split
is behaviour-neutral, so `SC004FinalAiToE .o. SC004GeneralAiToA` composes in the
current SC004 slot with identical outputs and trace. Historically A precedes B+C,
which the composition order already reflects (A first). No reordering is required
or proposed; the general component's one boundary (SC036) sits later and is
consistent with its later historical placement.

## Recommendation (definite)

**Adopt Outcome C.** Split SC004 into two historical changes — a later North Sea
Germanic / Anglo-Frisian general `*ai/*ái > *ā` (retaining the SC004 identity and
all witnesses) and an earlier, corpus-inert Proto-Northwest Germanic word-final
`*-ai > *-ē` (provisional identifier) — while keeping B and C as one change and
keeping both changes computationally adjacent in the current slot.

Caveats and prerequisites before any implementation (a **separate**, review-gated
task):

1. Consult **Versloot 2017** directly and add it to `docs/refs.bib`; confirm the
   PNWGmc dating of A and the wave chronology / dating of B+C.
2. The `EAF` stage for Change 1 is a *modelling* home for an areally diffused
   change, not a claim of a discrete Proto-Anglo-Frisian node (consistent with
   CAPR's definition of EAF as an operational corridor).
3. Record Change 2's 0-corpus-load explicitly; it is retained for
   ending/comparative completeness, not on CAPR derivational evidence.

## Stop

This report is the deliverable. Per task §10 nothing is applied: the production
rule stands, no SC number is assigned, no cascade move or rename is performed, and
SC064 is untouched (queued for its own morphology-first audit).
