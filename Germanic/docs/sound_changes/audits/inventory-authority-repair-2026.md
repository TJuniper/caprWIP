# Inventory authority repair (2026)

`Registry-verdict: ARCHITECTURE — sc_inventory_annotations.tsv reclassified SOURCE → GENERATED`

## 1. The problem

`registry/sc_inventory_annotations.tsv` was labelled `SOURCE (hand-edited)`.
That label was read as licence to maintain *every* column by hand, including
columns whose real authority is somewhere else. The file therefore became a
second authority for facts that `germanic.txt` and the coverage census already
own, and it went stale silently.

Measured at the moment of the repair, against the real authorities:

| Column | Rows wrong | Real authority |
| --- | --- | --- |
| `rule_source_anchor` (line numbers) | **90 of 100** | `germanic.txt` |
| `foma_definition_raw` | **22 of 100** | `germanic.txt` |
| `trace_occurrence_count` | **21 of 89 in census scope** | `rule_coverage_census.tsv` |

Nothing detected any of this, because nothing compared them. The line numbers
in particular were guaranteed to rot: inserting a single comment above any
definition invalidates every anchor below it.

## 2. Governing principle

> Human-authored sources contain human judgements.
> Machine facts are generated from their actual authority.

## 3. Authority map

| Truth | Authority | Accessed through |
| --- | --- | --- |
| Executable | `Germanic/fsts/germanic.txt` | `tools/executable_facts.py` |
| Order | `cascade_baseline/executable_model.tsv`, `cascade_order_manifest.tsv` | `tools/oe_pipeline.py` |
| Corpus firing | canonical trace → `cascade_baseline/rule_coverage_census.tsv` | `tools/rule_coverage_census.py` |
| Scholarly | `registry/sc_registry.tsv`, `registry/sc_inventory_notes.tsv`, `registry/chronology_edges.tsv` | hand-edited |

## 4. What moved

**Human, now in `registry/sc_inventory_notes.tsv` (SOURCE):**
`change_id`, `plain_description_draft`, `order_sensitivity_status`,
`illustrative_lexemes`, `notes`, `review_note`, `needs_human_review`.

**Machine, now generated into `registry/sc_inventory_annotations.tsv`
(GENERATED):** `trace_stage` (a rendering of the registry's `pipeline_stage`),
`rule_source_path`, `rule_source_anchor`, `foma_definition_raw`,
`appears_in_compact_trace`, `firing_count`, `firing_lexemes`,
`literature_status` (a rendering of the registry's `adjudication_status`).

## 5. Two decisions worth stating

**Line numbers are not data.** `rule_source_anchor` is now the stable anchor
`define Name`, with no line number in it, so inserting lines above a definition
cannot dirty a committed file. The current line is computed on demand:
`python3 Germanic/tools/executable_facts.py EAFNasalizedLowRounding`.

**Curated examples are not a firing census.** The old `example_lexemes` column
conflated "examples a human chose because they explain the change" with "the
corpus rows this rule currently fires on". These are now `illustrative_lexemes`
(human, editorial) and `firing_lexemes` (generated, exhaustive). They are never
interchangeable. The migration deliberately did **not** carry the old
`example_lexemes` values into `illustrative_lexemes`: they were firing
populations, so they belong to the census, and a human may now add genuinely
editorial examples where they help.

## 6. Chronology-edge witness semantics

The SC103→SC104 edge exposed a second smell: the validator required
`representative_lexemes` on every chronology edge, which pressures an agent to
invent a witness for a relation that is historically sound but has no current
corpus row. Validation now distinguishes:

* `evidence_basis=independently_demonstrated` — the edge claims a live lexical
  demonstration. Witness lexemes and forms are **required**, and every named
  lexeme is checked against the selected corpus. A fabricated witness fails.
* `evidence_basis=stage_entailed` — the direction follows from independently
  established stages. No lexeme is required, and none may be invented. `notes`
  are still required, because the relation must be explained.

## 7. Archive treatment

The pre-migration file is **not** copied to an archive path. It keeps its
existing path and name (so no consumer churns), changing only from SOURCE to
GENERATED, and its genuine human content was migrated into
`sc_inventory_notes.tsv`. Its pre-migration state is fully recoverable from Git
history. Retaining a frozen copy would recreate exactly the hazard this repair
removes: a stale mirror of machine facts sitting in an active-looking path.

## 8. Guardrails

`Germanic/tests/test_inventory_authority.py` fails if the problem returns:
human sources containing Foma definitions, source line numbers, executable
positions or firing counts; generated definitions drifting from `germanic.txt`;
generated firing counts drifting from the census; a generated file missing its
`GENERATED — DO NOT EDIT` banner; `--check` failing to detect a stale
projection; a fabricated or non-existent chronology witness. It also pins the
parser behaviour that a `;` inside a comment cannot truncate a definition.

## 9. Success test

Inserting ten blank lines above a definition in `germanic.txt` leaves every
generated view clean and requires **zero** edits to any human source. Changing
a rule body requires editing only `germanic.txt`. Adding a corpus row
regenerates firing counts and firing lexemes automatically.

## 10. Scientific impact

None. No Foma rule, corpus row, historical claim, stage, scope, confidence or
verdict changed. All 385 corpus outputs and both frozen cascade fingerprints
are byte-identical.
