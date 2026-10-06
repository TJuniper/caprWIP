# Hue: inherited vowel and j-created glide-chain proposal

Status: the user approved the complete package on 2026-10-04. Production
input/components and the strict baseline transition are implemented.
The final integrated suite passes 713 tests/6,259 subtests; protected
production controls pass 68 component, 13 staged and 14 corpus assertions.
The inspected 302-page combined book publishes hue in section6.82,
printed pp.185–187. The SC033 memo owns the complete publication closeout.
The specification and pre-adoption observations below preserve the
proposal's original decision context. No commit or push is authorized.

## Identity

- SC ids: SC010, SC033 and SC106; the necessary SC032 realization interface,
  not an independent adjudication of SC032's existing nine clauses.
- Executable identifiers: PWGmcJGemination, OEEwLongDiphthong,
  OEJWWSimplification and OEDiphthongLeveling. Names do not assign dates.
- Date / branch / base commit: 2026-10-04 / update /
  5e7421633b5d14c9ecf183d3a8bd1af0f0602cc4.
- Private recipes and fixtures: `oe_hue_recipes.json` and
  `oe_hue_fixtures.tsv` in the existing Anglo-Frisian literature dossier.

## Question

Hypothesis: hue's current e-input and long-eo proxy preserve its native
spelling but fail to model the preferred source account's inherited i,
j-created offglide reanalysis and long-io intermediate.

Confirmation requires the actual source comparison and an executable
complete chain, not merely matching hīew. Refutation would require evidence
that the current e-to-long-eo path is the defended historical account, or
an in-domain failure of the correctly implemented proposed chain. Compiler
failures and disagreement over uncertain phonemic analysis are distinct.

## Current state (before any production edits)

SC033 is an active support_stage, staging_row=no, without invented
historical stage, scope or confidence. Its released restriction removed
knee's singleton-w lengthening. The remaining operation sends e/i before
ww+j to long eo. SC106 subsequently simplifies the retained ww.
SC032's ordinary atomic/split realization clauses are still independently
pending adjudication.

Hue2332 has PROTO = PROTOFORM = *xéwją and target hīew. It enters as PGmc;
its explicit context is stressed and phonologically final. The current path
is *xéwją -> *xéwwją -> *xēowwją -> *xēowją -> ... -> hīew.
There is no earlier e-to-i raising operation in this path.

Consulted current owners: the SC033 knee adjudication, the SC010 w-gemination
admission account, the grouped 031-034 dossier, and hue's model, research
memo and source ledger. Historical admission and experiment records remain
historical; their original claims are not rewritten as new measurements.

## Diagnosis

The fresh SC033 evidence has exactly one live witness, hue2332:
`*x*é*w*w*j*ą` -> `*x*ēo*w*w*j*ą`. It is a live support-stage application,
not an independent witness proving the proxy's historical quantity or date.
Knee2085 is now a protected short-dative negative.

The completed inherited-i input-only trial covers all 387 selected OE rows.
Only hue's input changes; all native outputs remain identical, no row is
rejected or ambiguous, and the old seven mismatch IDs remain
1973, 2013, 2030, 2162, 2240, 2298 and 2300. Canonical artifacts are
unchanged. Two component, one staged and two corpus assertions distinguish
input correction from downstream correction. The incumbent SC033 still
turns the new i into long eo: this trial therefore does not establish the
complete preferred history.

The complete source-chain trial succeeds independently. Its measured
checkpoints are *xíwwją -> *xíuwją -> *xīowją -> ... -> *çīewj -> hīew.
All 19 component, four staged and eleven corpus assertions pass. It
preserves every selected final, with no rejection or ambiguity, the same
seven old mismatches, and unchanged canonical artifacts. Only hue's input
and pre-mutation history change; all eight recorded checkpoints for each
of the other 386 selected rows are identical. At the SC106 checkpoint
hue is already *xíuwją, so that compatibility operation no longer fires
on it. At mutation the two histories converge on *çīewj.

Persisted measurements: `oe_hue_inherited_i_result.json` and
`oe_hue_source_chain_result.json`. Both prove full-wrapper identity first
and preserve the declared recipe and protected-artifact checks.

Non-corpus component probes distinguish singleton iwj, nonpalatal iww,
unraised ewwj, awj, short io, ordinary inherited iu/eu/aeu and their split
short encodings. They are phonological-domain tests, not new attestations
or chronology witnesses. The mirth-shaped component is a source-class
comparison, not admission of a new corpus row or a full mirth paradigm.

## Literature

The current source ledger records the author-specific forms, asserted
stages, endings, arguments and CAPR normalization. Load-bearing held pages
were visually checked; printed pages, not PDF-sheet numbers, are cited.

| Source / printed pages | Evidence and limitation |
| --- | --- |
| Orel 2003 pp.171-172 | Gives *xewjan, neuter, and probably derives it from *xawwanan. This is real e-form reconstruction evidence, not permission to relabel e as pre-PGmc. |
| Kroonen 2013 p.224 | Gives neuter stem *heuja-; probably derives it from *kēu-ió- by Dybo's law, with the earlier base *kieh₁-u-. Its e and stem citation are preserved separately from Orel's derivation and whole-form ending. |
| Ringe-Taylor 2014 p.250 | Explicitly gives PGmc *hiwją and the palatalized geminate/offglide chain to pre-OE long īow and WS long īew. Calls the development surprising and the phonemic analysis unclear. |
| Ringe-Taylor 2014 p.53 | Supplies the new/sew/mirth gemination comparison, while distinguishing phonetic geminates from phonemic /wj/. Does not establish a second independent j phoneme on each palatalized w. |
| Ringe 2017 pp.151-153 | Gives the early high-front-conditioned raising account; p.152 has PIE *néwios -> PGmc *niwjaz. Explains the inherited-i class, but does not quote a hue reconstruction here. |
| Fulk 2018 p.59 | Separates PGmc e/eu raising before i/j from later front umlaut. Supports inherited i, not a separately supplied whole-word hue reconstruction. |
| Fulk 2018 pp.71-72,126 | Questions traditional j-created geminate dismantling and w's supposed consonantal status; discusses alternative strew input and regularization of new. His general gemination discussion is not endorsement of every traditional glide arrow, and he supplies no replacement complete hue chain here. |
| Campbell 1959 pp.42,46,167 | Gives early high-front-conditioned raising, the contrasting awj/iwj outcomes, hīow/hīew and general West Germanic gemination. Supports the conventional class account and the selected WS target. |

The preferred account is not unanimous opinio communis at every arrow.
Early high-front raising and the inherited/j-created class distinction have
broad support; the precise dismantling and phonemic interpretation remain
disputed. Ringe-Taylor's explicit hue reconstruction and complete proposed
chain are preferred because they explain the selected case at stated stages,
with Campbell's class account as independent support. Fulk's objections
remain substantive; his discussion does not supply a comparably complete
alternative hue history that can be silently substituted.

CAPR normalizes h to x, prevocalic u to w where appropriate, and adds its
lexical acute. It does not harmonize stem *-ja-, Orel's whole-form *-jan
and Ringe-Taylor's *-ją as though the authors printed the same ending.
Palatalized ww / w are serialized as ww+j / w+j: this is a computational
conditioning carrier, not a resolution of the source's phonemic question.

## Historical analysis

The recommended realized-PGmc input already contains i. No later one-word
e-to-i law is proposed. PROTO and PROTOFORM remain distinct conceptual axes,
even when both adopt the same reconstruction; stage and confidence remain
independent.

The source distinguishes j-gemination, palatalized-glide reanalysis,
English long-diphthong realization and WS mutation. The proposed support
components expose those checkpoints without pretending that every boundary
has a uniquely established historical date or exclusive genealogical scope.
They do not select the complete Anglo-Frisian ancestral inventory.

Inherited raising precedes the PGmc input under the preferred account
(stage_entailed). Gemination feeds the j-created reanalysis, whose retained
palatal conditioning feeds realization and mutation under Ringe-Taylor's
working account (2014 pp.53,250). These dependencies do not justify a new
canonical strict chronology edge from output equality. Retain the present
serialization and independently pending SC032 relations.

## Verdict

Approved disposition: REFORMULATE the SC033 support encoding / SPLIT
reanalysis from its necessary long-io realization / RETAIN unchanged
SC010 gemination, ordinary SC032 clauses and the composed SC106 compatibility
operation. The canonical verdict line is owned by the SC033 memo;
the original knee restriction remains preserved as its completed history.

Recommended exact scientific package:

1. Hue2332: PROTO = PROTOFORM = *xíwją, target hīew, PGmc input stage,
   unchanged class, context and confidence. Preserve the e reconstructions
   as real author alternatives, not earlier forms inferred without evidence.
2. Keep the stable SC033 executable identity but replace its retained
   e/i-to-long-eo proxy with iww -> iuw before the palatal conditioning
   carrier j, including acute i. Singleton iwj, nonpalatal iww and ewwj
   are negatives. Do not revive knee lengthening.
3. Add a separately visible support identity, provisionally SC110 /
   OEJGlideIO, for iu/acute-iu -> long īo before w+j. Place it immediately
   before unchanged OEDiphthongLeveling. Keep all nine ordinary SC032
   bodies and their existing site. Register no fabricated historical
   stage/scope/confidence; derive executable positions normally.
4. Keep SC106's body and composition site. The candidate hue no longer
   feeds it; zero current firing is not proof of universal redundancy.
   Retain its compatibility role explicitly rather than silently deleting it.
5. Use existing īo alphabet, weight, mutation and rendering support.
   Ordinary OEIUmlaut already sends long īo to long īe. No new marker,
   lexical exception, analogy mechanism or broad ending repair is proposed.

The private AFReal composite specializes the j-created input before calling
unchanged OEDiphthongLeveling. The production split above exposes that
same operation as a registered component; its equivalence and all readers'
definition fidelity must be checked during approved landing.

Proposed SC033 body:

```foma
define OEEwLongDiphthong [
    {*i} {*w} {*w} -> {*iu} {*w} || _ {*j},
    {*í} {*w} {*w} -> {*íu} {*w} || _ {*j}
];
```

Proposed independently visible realization body:

```foma
define OEJGlideIO [
    [{*iu}|{*íu}] -> {*īo} || _ {*w} {*j}
];
```

The resulting local composition is OEEwLongDiphthong ->
OEJWWSimplification -> OEJGlideIO -> OEDiphthongLeveling, with
the surrounding prefix/suffix unchanged. The old OEEwLongContext helper
can remain as an unused compatibility definition; it no longer conditions
SC033 and must not be mistaken for another composed historical operation.

## Propagation (only after adoption)

Update the SC033 current memo and registry descriptions, register the
distinct realization support, and revise the SC106 compatibility account
and directly affected SC032 interface. Preserve the completed knee
disposition and historical measurements. No independent SC032 verdict
or chronology-edge promotion is authorized by this proposal.

Synchronize hue's source ledger, research memo and detailed lexical model;
explicitly supersede the relevant SC010 admission claims; update the
grouped 031-034 dossier, comparative synthesis, affected readers and
Chapter4. Chapter3 changes only for an actual defended ancestral claim.
Regenerate through the adjudication interface and inspect the eventual
standard unbypassed book render. No new PDF is claimed now.

Research regression checks cover current source pins, preserved author
disagreements and Fulk's objection, report/fixture parity, all 387 finals,
all recorded non-hue checkpoints and hue's changed long-io intermediate.
After adoption, add exact production-component, registered-support,
consumer, reader-definition and approved-transition tests.
The focused research/runner/knee-transition checks currently pass
62 tests and 169 subtests. Canonical SOURCE-only refresh and the SC033
nonmutating propagation check pass; production inputs, FST, registries
and baseline files remain unchanged.

The baseline change is input-sensitive even with unchanged hīew:

| Projection | Current | Proposed, with measured unchanged outputs |
| --- | --- | --- |
| Selected387 evaluator | ffad47aefc01423953fc57784fe6a6f6cef31dcca9bbdbb7b36b06a63dc552bc | 47a901e9e4a7cd663b8eb574b87fe737382e8fc1b4f1bc8afc38701af0c96872 |
| Selected387 lexical | 76bb0ffda672c700cc5b1cfe95a0ec491047d65ccbfaff290209842fabf3d344 | 90789094b8d8889bb478dd6077de75e1d8e1cb66b7b6d347b63e73a83d039c47 |

These hashes were initially calculated read-only from the pre-hue baseline with only
hue's proto, normalized proto and evaluator input replaced. Hue is outside
the immutable original380 set. The active original380 projection remains
70bdaba537d8f6b6bb7d872d00eefbef75127d2d77689af7ba01b35a79ebce39;
the immutable legacy380 remains
fae656520e9ebf446854643907a1ba48a511877fc25b1fae39649d5b97e9a6cf.
Do not add hue to the original380 migration map or overwrite the knee
approval receipt and pre-SC033 archive.

The proposed minimal adoption interface extends the existing exact
selected-record transition validator with a distinct transition id and
explicit approval-file selection. The hue receipt would declare only
row2332's old/new input fields, unchanged target/output/multiplicity/context,
and the projections above; preserve separate pre-sc033-hue bytes and all
existing gift/context/knee/legacy archives. Existing approvals retain their
original schema and archive names. Fresh container evaluation, strict
undeclared-drift rejection, archive integrity and idempotence remain
mandatory. The approved receipt is `approved_hue_input_migration.json`;
the existing validator now accepts the distinct transition id without
altering earlier receipts, and the adjudication CLI selects it explicitly.

## Residue

The complete candidate was measured before the consolidated adoption
decision. The user's approval covers the exact input, both
support components and strict baseline transition together; it is not
permission for an ordinary-input-only landing with the acknowledged
long-eo proxy.

The precise phonemic analysis and Fulk's dismantling objection remain
qualified. Other SC032 components, SC034, SC105, bounded breaking rivals
and the complete ancestral inventory remain subsequent cases.
Project-wide author-form collection and an introduction discussion are
queued separately; hue's source ledger preserves the evidence now without
starting a new registry or broad corpus migration.
