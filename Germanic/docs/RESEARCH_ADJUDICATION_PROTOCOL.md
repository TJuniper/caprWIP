# Germanic sound-change adjudication protocol

**Status:** authoritative for all Germanic sound-change adjudication work
(historical stage, scope, chronology, FST semantics, interaction evidence,
witness selection). If any older instruction file conflicts with this
protocol for that work, this protocol governs; see "Instruction precedence"
at the end.

**Companion template:** every adjudication must fill in
`Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md` (copied to
`Germanic/docs/sound_changes/audits/scNNN-adjudication.md`).

This protocol distils the working method of the SC020–SC023 adjudications.
Its purpose is not to reproduce their conclusions but to reproduce the
method that allowed the evidence to overturn the starting hypothesis. A
future adjudication may legitimately conclude RETAIN, REFORMULATE,
RESTRICT, SPLIT, RETIRE, REORDER, or DEFER — whichever the evidence
supports.

---

## The procedure

### 1. Establish current authoritative state first

Read `Germanic/docs/CURRENT_STATE.md` and the canonical registries under
`Germanic/docs/sound_changes/registry/` (`sc_registry.tsv`,
`chronology_edges.tsv`, `sc_inventory_notes.tsv`; see
`registry/CONTROL_PLANE.md` for the full SOURCE/GENERATED/ARCHIVE map),
plus any existing adjudication memo for the rule under
`Germanic/docs/sound_changes/audits/`. Start with
`python3 Germanic/tools/adjudicate.py SCNNN --prepare`: it assembles the
packet and the registry-driven reading list — do not search the repository
for evidence documents. `sound_change_inventory.tsv`, the
staging map, and the chronology-graph files are GENERATED views — read
them freely, never hand-edit them; after editing SOURCE files run
`python3 Germanic/tools/adjudicate.py SCNNN --finalize`, which regenerates
every derived artifact and validates propagation. For a SOURCE-only edit
outside an SC adjudication (e.g. moving a rule, editing reader prose),
`python3 Germanic/tools/adjudicate.py --refresh` is the single
regeneration command — never pick individual generators by hand. Do not resurrect
superseded plans, retired rules, or old audit conclusions. Frozen
checkpoints (e.g. `docs/archive/CANONICAL_STATE.md`) are historical
records, not current state.

### 2. State the question falsifiably

Write down the suspected problem or scientific question as a claim that
evidence could confirm **or refute**, before gathering evidence. Example
(SC023): "the SC023 < SC047 edge may be an artifact of an over-broad
implementation firing on the out-of-domain verb `do`." The SC023 evidence
*refuted* this: the rule never fires on `do` at all; the edge is real but
counterfeeding. Expect and allow this outcome.

### 3. Diagnose executable behavior before editing anything

* Trace the relevant witnesses through the actual compiled cascade with
  `python3 Germanic/tools/adjudicate.py SCNNN --evidence` (it rebuilds the
  stage bins in the container, checks their freshness, and prints before/
  after forms), not from memory of what the rule "should" do. Do not run
  `foma`/`flookup` or trace scripts by hand for ordinary adjudication.
* Establish the selected input/protoform actually fed to the transducer.
* Inspect the form immediately before and immediately after the rule.
* When chronology is at issue, run the counterfactual: skip or displace
  the rule and observe what actually breaks and *why*.

### 4. Census all live firings

Never infer a rule's behavior from the single lexeme named on a
chronology card. `--evidence` enumerates every input the rule changes
across the full corpus; classify each firing as in-domain or
out-of-domain relative to the historical claim. (SC023: the card named 1 lexeme; the census
found 17 live firings, all in-domain — the apparent conflict was between
two different kinds of record, not in the rule.)

### 5. Keep the load-bearing concepts separate

Confusing any two of these caused real errors in past passes:

| Concept | Meaning |
|---|---|
| historical phenomenon | the change that actually happened in the language |
| historical stage & scope | when/where it happened (pgmc, pwgmc, …; pan-Germanic, WS-only, …) |
| CAPR executable rule / proxy | the Foma rule that models the corpus-visible fragment |
| selected-input convention | which paradigm cell / citation form the corpus feeds in, and what is pre-encoded in it |
| live application witness | a lexeme the rule actually changes |
| feeding/bleeding witness | a lexeme whose derivation requires the rule to precede/follow another because outputs interact |
| counterfeeding/counterbleeding negative witness | a lexeme the rule must NOT touch; ordering evidence comes from what survives (SC023: OE `dōn` keeps the secondary `-n` because the loss was dead) |
| stage-entailed chronology | ordering that follows from the stages themselves (a PGmc change trivially precedes an OE change) |
| independently demonstrated chronology | ordering positively shown by a derivation, not just entailed by stage labels |
| model-local executable ordering | where the rule sits in the executable cascade, which may legitimately diverge from historical stage (editorial holding zones exist) |

### 6. Literature: existing dossiers first, then sources

Check existing CAPR literature dossiers and the local source library
(`docs/references/`) before doing new research. When citing, state
exactly — with page numbers — what the source supports, and separately
state what is CAPR's own modelling decision. Do not launder a modelling
convenience into a historical claim by citation proximity.

### 7. Never infer stage or scope from an FST identifier

Identifiers like `PNWGmcMnDissimilation` (SC022, historically Common
Germanic) and `PNWGmcNStemNLoss` (SC023, historically Proto-Germanic)
are retained for executable stability after their historical metadata
changed. Stage and scope come from the canonical
`registry/sc_registry.tsv` (of which the staging map and inventory are
generated views), never from the name prefix. This invariant is
machine-checked
(`test_adjudication_protocol_guardrails.py`).

### 8. Never infer historical domain from the executable environment

A deliberately narrow proxy may represent a broader change: SC023's
`{*ō} {*n} -> {*ǭ} || _ .#.` implements only the corpus-visible fragment
of general word-final `*-n` loss, because other outputs of the law are
pre-encoded in the selected protoforms and the numerals'
analogically-retained `-n` must be protected. Conversely, an executable
rule may historically overgenerate. Compare environment and domain
explicitly; do not equate them.

### 9. "It changes in the harness" is not a chronology edge

Before promoting any interaction-harness result to a historical
ordering claim, establish *why* the lexeme changes and classify the
witness role using the table in step 5. A displaced rule eating a form
it never touches live (counterfeeding collapse, `+?` output) is
evidence of a very different kind from a live feeding relation, and an
out-of-domain firing is not historical evidence at all.

### 10. Explicit verdict before propagation

Record one verdict from the controlled vocabulary, with dimensions
stated separately where needed:

* **RETAIN** — rule and metadata stand as is
* **REFORMULATE** — restate the historical characterization/metadata
* **RESTRICT** — narrow the domain or conditioning
* **SPLIT** — decompose into genuinely distinct changes
* **RETIRE** — remove as an active historical change (keep archival record)
* **REORDER** — move the executable position
* **DEFER** — evidence insufficient; author decision required

E.g. SC023: "REFORMULATE metadata / RETAIN executable rule." SC021:
RETIRE (successors SC071/SC099/SC100). SC022: REFORMULATE stage only.

### 11. Propagate only after the verdict

Then, and only then, update: FST source, canonical registries,
inventories, chronology cards, graph/candidate files, batch-report
annotations, book/literature dossiers, reader-facing prose, and
regenerate legitimately downstream artifacts. Preserve archival records
(old batch reports, frozen checkpoints) with annotations rather than
rewriting their historical claims.

### 12. Regression tests for the scientific conclusion

Prefer paired positive and negative controls over string/fingerprint
pins: assert the witnesses that must change AND the near-neighbours
that must not (SC023 tests pin the 17 firings, `do`'s invariance, and
the untouched `-un` numerals). Metadata assertions should target the
canonical registries, not incidental prose.

### 13. Fingerprints are observations, not goals

The frozen corpus fingerprints (legacy-380 and expanded) are recomputed
observations of model output. Never distort a scientifically justified
correction to preserve a hash. If a legitimate correction changes a
fingerprint: STOP, identify exactly which rows and derivations changed
and why, report, and only then establish a new baseline as an explicit,
documented consequence of the adjudication. Conversely, a hash changing
during a "metadata-only" pass means something is wrong — diagnose, do
not refreeze.

### 14. Separate science from hygiene in the final report

Distinguish (a) scientific changes (verdict, metadata, rules, corpus),
(b) mechanical propagation of the verdict, and (c) incidental
rebuild/hygiene repairs encountered along the way (stale generated
artifacts, formatting fixes, build-blocking defects). All three occur;
readers must be able to tell which is which.

### 15. One SC at a time

Finish the assigned SC completely — adjudication, propagation, tests,
regeneration, validation, commit, push, report — then STOP. Do not
begin the next SC unless explicitly instructed.

---

## Worked example: SC023 (read `audits/sc023-adjudication.md`)

SC023 is the principal worked example because it exercises the
distinctions above:

1. **The initial suspicion was falsified, not confirmed.** The task
   hypothesized a spurious edge from an over-broad rule; tracing showed
   the rule never touches `do` live, and the census showed all 17
   firings are in-domain.
2. **A lexeme can be a valid chronology witness without being an
   application.** `do`/`dōn` is counterfeeding negative evidence: the
   secondary `-n` created by SC047 survives precisely because the old
   loss was dead.
3. **The historical phenomenon is broader than the executable proxy.**
   General (pre-)PGmc word-final `*-n` loss vs. the deliberate
   `{*ō}{*n}` citation-form fragment.
4. **Historical metadata can change while the FST identifier, rule
   bytes, and model output all remain unchanged.** Both corpus
   fingerprints were verified identical before and after.

SC021 shows the RETIRE path (an unwitnessed rule replaced by
source-backed successors), and SC022 shows stage reclassification with
identifier stability. But apply the *rules*, not the outcomes: the next
rule may deserve RETAIN, and saying so with evidence is a success.

---

## Instruction precedence

* This protocol and the template govern **Germanic sound-change
  adjudication** (historical stage/scope, chronology, FST semantics,
  interaction evidence, witness/corpus decisions).
* `.github/copilot-instructions.md` governs general repository
  conventions (build/test commands, container rules, reader-facing
  style) and points here for adjudication work.
* `docs/AGENTS.md` is a short routing rule pointing to the canonical
  adjudication interface. An explicit user instruction to implement,
  commit, and push an adjudication is itself the authorization to do so;
  no approval gate applies. (The retired generic debugging workflow is
  archived at `docs/archive/legacy-agent-workflow.md` and is never an
  instruction source.)
* Frozen checkpoints such as `Germanic/docs/CANONICAL_STATE.md` are
  historical records of a past freeze; they are never a source of
  current rule status. Start from `Germanic/docs/CURRENT_STATE.md`.
