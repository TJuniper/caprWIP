# Anglo-Frisian research area

Research sub-area of `Germanic/docs/sound_changes/literature_dossiers/`.

## Adopted U increment and historical experiment boundary

The approved SC056/gift correction separates ordinary diphthongization before
mutation from the unchanged late approximation and selects Ringe's PGmc
gift input. Its controlling adjudication is
`../../audits/sc056-ordinary-palatal-diphthongization-adjudication.md`.
The gift lexical SOURCE now compares all checked reconstruction alternatives
and confidence qualifications. This does not adopt the D/apocope control
or settle the full Anglo-Frisian programme.

The six original recipes and 42 fixture assertions are records of the
pre-adoption baseline, not freshly rebased experiments. Their explicit
FST/corpus digests cause execution against changed production sources to
fail with an instruction to prepare a new current-baseline recipe.
Historical results remain intact; current production assertions live in
`Germanic/tests/test_sc056_adjudication.py`. Never silently reinterpret
the historical gift-input or ordinary-order experiment after adopting it.

Current production component controls use `oe_adopted_u_controls.json`,
recipe `u-adopted-controls`: ordinary simple-e positive, split/atomic eo and
high-i negatives, guest diphthong mutation, and retained late-clause controls.
They do not change the composition or corpus and remain distinct from the
historical recipes.

## Why this area exists

CAPR models each daughter language as an *ordered chain* of sound changes
running from its earliest relevant ancestor to the attested language. The
label "Anglo-Frisian" is inherited from a scholarly tradition that did not
work with that formalism, and it is applied in the literature to at least
four different kinds of claim. Before CAPR can decide questions such as
whether SC030 and SC043 are one change, or whether Old English and Old
Frisian palatalization is one innovation, the Frisian side of the
comparison must specify coherent daughter histories and their conditions.
Source-local partial chains are already recorded here; a single adjudicated
Frisian cascade does not yet exist.

This area holds the evidence architecture for that future adjudication. It
is **research state, not executable science.** Nothing here licenses a
change to the cascade.

CAPR's Anglo-Frisian ancestral node is a required part of its tree topology.
The unresolved questions concern its phonological state and the assignment
and conditioning of changes before and after it, not whether to remove it.
A failed common-stem assignment does not remove the node.

## The CAPR tree test

For this area the formal test of a shared innovation is:

> A change X shared by languages A and B counts as a genuine historical
> isogloss only if X can be placed on the common stem of A and B, before
> their split, without violating any securely established daughter-specific
> ordering edge.

The decisive configuration is:

> If X appears in both A and B, but in B a demonstrably B-specific change Y
> must precede X, while A does not share Y, then X cannot be a single
> inherited innovation of the common ancestor under the CAPR tree model.

When that configuration arises, at least one of the following must hold:

1. X happened independently in A and B;
2. the proposed relative chronology is wrong or insufficiently established;
3. Y is not really B-specific;
4. the apparent identity of X in A and B is false — they are similar
   outcomes of historically distinct changes.

"Wave", "dialect continuum", "Sprachbund", "linkage" and "diffusion" are
**not** admissible escape hatches from this test *in CAPR's own analysis*.
Several of the authors ingested here argue explicitly for wave or linkage
models — Versloot and Bremmer most strongly. Those views are recorded
faithfully in the source cards, because misreporting an author is a
research failure. But when the evidence is translated into CAPR, it is
tested against the ordered-tree formalism, because that is the only model
CAPR can execute.

## Four-way classification

Every feature traditionally called "Anglo-Frisian" is sorted into exactly
one of:

| Class | Meaning |
|---|---|
| **S — surface isogloss** | English and Frisian show similar outcomes. Says nothing yet about history. |
| **H — CAPR historical isogloss** | The same innovation can be placed on the shared stem without violating a secure daughter-specific edge. |
| **P — parallel innovation** | A secure daughter-specific edge forces the change to have happened twice. |
| **U — uncertain** | The established relative chronology does not decide between H and P. |

`S` records an observed correspondence, not a historical verdict. A candidate
may also fail to have genuinely identical outcomes on inspection.
The research question is how many proposed correspondences permit `H`.
Here `H` means compatibility with a specified chain, not proof of inheritance;
`P` is likewise conditional when its load-bearing daughter edge is disputed.

## Levels of claim

Throughout this area the following levels are kept typographically and
structurally distinct, because conflating them is the most common failure
mode in this literature:

1. **observation / data** — an attested form, a rune, a spelling;
2. **relative-chronology inference** — an ordering edge derived from it;
3. **absolute-date inference** — a calendar date or terminus;
4. **historical interpretation** — the author's narrative;
5. **CAPR tree consequence** — what follows under the formalism above.

Waxenberger's runic material is the sharpest case. An archaeologically
dated object gives a secure date for *the inscription*. It gives a date for
a *sound change* only through a chain of further inferences: the reading of
the rune, its phonetic interpretation, its phonemic status, and the
identification of that state with a particular change. The existence of a
fronted allophone [æ] is not the same event as the phonemicization of /æ/.

## Contents

| File | Role |
|---|---|
| `source_cards/` | Source-specific direct readings; the holdings audit distinguishes completed reviews from work in progress. |
| `missing-direct-sources.md` | Cited-but-absent sources, with what each blocks. |
| `anglo-frisian-chronology.synthesis.md` | Cross-source, proposition-by-proposition comparison; the ordered pre-OE and pre-OFris chains; the four-way classification. **Authority for this area.** |
| `palatalization-research-note.md` | Shared-vs-independent palatalization, unadjudicated. |
| `future-lexical-witnesses.md` | Candidate discriminating witnesses. No corpus rows. |
| `research-pass.record.md` | Protocol record, unchanged executable scope, and deferred decisions. |
| `historical_constraints.tsv` | Research SOURCE: selected D/A/F/P/U/B premises in ten separately attributed alternatives; explicit gaps, not canonical edges. |
| `oe_diagnostic_fixtures.tsv` | Forty-two exact intermediate assertions across all six cases, reusing twenty-five live OE rows; bounded D/U variants and explicitly incumbent A/F/P/B diagnostics, not new corpus rows. |
| `node_state_candidates.tsv` | Relevant-class inventories for a conservative working cut and two separately attributed alternatives; no selected canonical node state. |

The host-runnable research checker is
`python3 Germanic/tools/anglo_frisian_chronology.py` (optionally
`--model <exact-model-id>`). It checks each alternative separately,
including strict cycles through weak constraints, proposed identity,
distinctness and transitive daughter-only predecessors of common-stem
events. It reports source pages, assumptions and conflicting paths.
Scope is explicit, never inferred from language or SC/network names.
It does not read or modify canonical positions, FSTs, bins or registries.

Exit codes: 0 = consistent under the stated local assumptions, 1 =
inconsistent, 2 = invalid input/provenance, 3 = incomplete. Even 0 tests
only the supplied claims, not a complete history or scholarly truth.
All ten current source-local models intentionally return 3: component conditioning
and some scope premises remain unresolved. The node-state table now records
relevant classes for three candidate cuts, not a selected full phoneme
inventory or a completed Frisian cascade. Research table changes must stay
aligned with the comparative synthesis; no automatic promotion to
production chronology follows.

The A alternatives distinguish Campbell's conventional strict serialization
from Ringe and Taylor's explicit temporal milestones: inherited-long fronting
well under way before ai contraction completes, with overlap allowed.
Milestone order is not silently converted into non-overlapping whole events
([@RingeTaylor2014, p. 170]).

Node-state rows distinguish author proposals from the conservative working
cut and explicitly mark unassigned classes. They are not scope assignments
in the production registry. A row's presence is neither an approved common
event nor evidence that every quantity or consonant class is specified.

`oe_experiment_recipes.json` is the research SOURCE for isolated recipes.
Run, after the normal container/provenance checks:
`docker compose exec -T backend python3 /usr/app/tools/anglo_frisian_experiments.py --recipe d-aei-ww`.
The other IDs are `identity`, `d-aei-ww-proxy-control`, `u-gift-input`,
`u-ordinary` and `u-ordinary-gift`.
The runner prints JSON containing all selected stable row IDs, final outputs,
baseline mismatches, intermediate states and protected-artifact hashes.
Optional `input_overrides` are private, source-cited PGmc replacements
matched by stable row ID and exact original input. They do not edit the TSV;
this bounded interface requires an original `PROTOFORM == PROTO` PGmc
input. Separately staged inputs need explicit support, not an inferred
default; later-stage substitutions into the full cascade are rejected. Reports
separate variant inputs and input-change IDs from changed final outputs.
Optional `component_checks` apply explicitly hypothetical star-symbol
sequences to individual networks in the same temporary build. These are
not full-cascade inputs, new lexical histories or corpus admissions.
They test a stated positive/negative match domain and fail on a different,
missing or ambiguous result.
Redirect reports to a session artifact/cache, not canonical tables.
All compilation is in container temporary directories and is automatically
cleaned up; every variant first passes full-corpus identity equivalence.
Do not run private assays concurrently with the full Germanic test suite:
its live evidence integration test rebuilds canonical runtime bins and
their manifest. The protected-artifact check correctly rejects that race;
run these operations serially rather than relaxing the check.
Recipe citations are checked against the bibliography by the host tests.

The first D subset exposes SC098's representation-dependent apocope proxy:
only you changes. The explicitly technical proxy control restores every
baseline output. The SC031–034 dossier records why neither result selects
history by score or licenses a production rule; other glide classes and
prosodic representation remain a separate readiness gate.

The probe set now supplies thirty-five checkpoints, including paired
before/after states for sixteen incumbent components across all six cases.
That permits exact all-row component censuses without
equating a network's atomic versus split-symbol clauses with one historical
law. The report remains private experiment evidence, not canonical coverage.
The runner also checks the applicable fixture predictions at execution time
and reports their IDs. A missing probe, different atomic boundary, missing
output or ambiguous intermediate fails the assertion rather than counting
as a historical success.

The fixture table records nine D assertions across eight existing
rows, including the separately labelled SC098 technical control, sixteen
incumbent A/F/P/U/B assertions, and seventeen new U input/order assertions.
The complete table uses twenty-five existing rows. Predictions
retain atomic Foma-symbol boundaries rather than flattening eu/iu into
unqualified IPA. Inputs and targets are copied from the live corpus; the
cited handbook pages support the tested change/context, not an independent
etymological adjudication of every selected input. The eight D rows have
identical PROTO/PROTOFORM at the existing PGmc input convention; cow/lung
use their separately recorded PGmc paradigm/stem inputs. No later intermediate
has been relabelled as a PGmc input. Strew is explicitly reconstructed OE,
not an attested positive, and gift's current input claim is expressly not
endorsed. Guest's incumbent ordering is a diagnostic of the known source/model
discrepancy, not a source-supported chronology. Additional dialect and
non-corpus fixtures remain readiness work. No corpus admission is proposed.

The U input-only trial privately uses Ringe's PGmc giftiz with the existing
acute-stress notation. The ordinary-first trials separate six ordinary
non-high-front mappings before mutation from the unchanged long-low-front
clause retained afterwards. That latter clause remains an explicitly
unadjudicated broad proxy, not a newly proved later-sc conditioner.
The original-input trial exposes gift alone; the combined trial preserves
all baseline finals while guest follows the source intermediate history.
Gift reconstruction disagreements and the original input's provenance must
be audited before a production proposal
([@Ringe2017, p. 135, pp. 151–153; @RingeTaylor2014, pp. 215–217, 220, 235;
@Campbell1959, pp. 68–69, 173–174]).

Hogg 1979, Goblirsch 1991, Bremmer 2009 and Nielsen 2001 are now held
with page-preserving reference texts. All thirteen specialist sources now
have direct cards and comparative integration. Acquisition or a later direct
review does not retroactively upgrade another author's report into direct evidence.
The central holdings audit records review status and the remaining
Stiles 1995 / Fulk 1998 gaps.

## Available-evidence programme

Stiles 1995 and Fulk 1998 are not expected to be acquired for this programme.
Their absence is a coverage limit, not a prerequisite for completing the
comparative work or the book. Do not repeatedly request or search for them.
The four held additions have now been directly reviewed; the comparison uses
all thirteen specialist works.

Claims must distinguish direct held evidence, a held author's report of an
unavailable work, and CAPR's own inference under explicit premises. Compare
the reports without pretending to have checked the originals. Where a
constraint has independent direct support, assess it on that support; where
an essential premise cannot be checked, defer that point rather than every
other feature.

Recommendations may defend retention, a directly supported change, an
explicit source-backed working reconstruction, or a localized DEFER.
Non-uniqueness must remain visible; it does not license unsupported sound
laws. Publication can give a complete account of the defended model and its
limits without claiming exhaustive assessment of unavailable alternatives.

Every proposed production scientific change requires separate user approval.
Research comparisons and isolated experiments do not change that requirement.

The six-case evidence assessment and component packets are now integrated
in sections 8–9 of the comparative synthesis and the existing routed
book dossiers: diphthong feeders, long vowels/ai, ordinary-a/au fronting,
breaking/restoration, palatal layers and mutation/diphthongization.
They distinguish defended working histories from canonical decisions,
record complete incumbent clause/census maps, and give exact retained or
deferred dispositions. The full-domain conditioning gaps, canonical
node-state selection and separately approved production variants remain
explicit future gates, not silently completed science. The packets do
not authorize rule or corpus changes.

### A note on Versloot 2025

Card 09 is unlike the others and should be read with that in mind. Versloot 2025
attacks the framework itself, calling it the "Standard Theory" and objecting
that it makes PGmc \*a the target of eight separate sound laws
[@Versloot2025, pp. 103–106].

CAPR's executable Old English cascade currently encodes that Standard
Theory. So this source is a live challenge to the present model rather than
a refinement of it. It is filed here as **research state only**. Nothing in
it has been adjudicated, and it licenses no change to the cascade; see the
standing prohibitions below.

## Single-authority rule

Source interpretation must not be duplicated inconsistently across
sound-change memos. `anglo-frisian-chronology.synthesis.md` is the
authority for the comparative chronology. Individual SC memos
(SC029/SC030, SC043, the palatalization rules) **point at it**; they do not
restate it. If a memo and the synthesis disagree, the synthesis is wrong or
the memo is stale — fix one of them, do not let both stand.

Historical explanatory comments in the unchanged registry still reflect
earlier adjudications. This source pass reopens their scholarly justification
in research prose only; it does not rewrite stage, scope, confidence, verdict,
or other canonical fields. Those comments must not override the research
dossier's explicit unresolved identity status.

## Standing prohibitions for this area

Documentation work here does not license, and has not performed:

- reordering FST rules;
- merging or splitting canonical SC identities;
- changing scope/stage/confidence fields to conform to one source;
- adding sound changes;
- rebaselining outputs;
- adding corpus vocabulary.
