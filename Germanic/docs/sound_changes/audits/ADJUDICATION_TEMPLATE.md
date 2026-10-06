# SC adjudication template

Copy this file to `scNNN-adjudication.md` in this directory and fill in
every section. The sections force the reasoning steps of
`Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md`; keep entries concise
but never delete a section — write "none" or "n/a" with a reason.

## Identity

- **SC id:** SCNNN
- **Executable identifier:** (Foma `define` name; NOT a stage claim)
- **Date / branch / base commit:**

## Question

- **Hypothesis or suspected problem (falsifiable):**
- **What evidence would confirm it; what would refute it:**

## Current state (before any edits)

- **Existing historical characterization** (inventory + staging map rows,
  quoted):
- **Existing executable behavior** (rule text; environment; cascade
  position):
- **Selected-input assumptions** (which cell/citation form the corpus
  feeds; what is pre-encoded in the protoforms):
- **Existing verdicts/dossiers consulted:**

## Diagnosis

- **Complete firing census** (every lexeme the rule changes, both
  corpora; in-domain vs out-of-domain):
- **Principal witness traces** (form immediately before/after the rule;
  counterfactual skip/displacement where chronology is at issue):
- **Witness role classification** (per witness: live application /
  feeding / bleeding / counterfeeding-negative / counterbleeding-negative
  / out-of-domain artifact):

## Literature

- **Existing CAPR dossiers checked:**
- **Sources checked, with page numbers:**
- **Source-supported historical phenomenon** (exactly what the sources
  demonstrate):
- **CAPR modelling decisions** (explicitly NOT source claims):

## Historical analysis

- **Historical stage:**
- **Historical scope (geographical/genealogical):**
- **Relationship between historical phenomenon and executable proxy**
  (narrower proxy? overgeneration? exact match? why):
- **Chronology evidence** — list each edge and mark it
  `stage_entailed` or `independently_demonstrated`, with the witness
  and its role:

## Verdict

- **Verdict** (RETAIN / REFORMULATE / RESTRICT / SPLIT / RETIRE /
  REORDER / DEFER; state dimensions separately if needed, e.g.
  "REFORMULATE metadata / RETAIN executable rule"):
- **Machine-readable line** (must match the `verdict` column in
  `registry/sc_registry.tsv`; slash-join multiple tokens):

  `Registry-verdict: SCNNN=VERDICT`

- **Justification (2–5 sentences):**

## Propagation (only after verdict)

- **Affected files/registries:**
- **Regression tests added/updated** (positive AND negative controls):
- **Baseline/fingerprint effect** (expected none / changed — if changed,
  list exact rows, old/new derivations, and reason BEFORE refreezing):

## Residue

- **Unresolved uncertainty / deferred questions / author decisions
  required:**
