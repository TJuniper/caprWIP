# SC031-SC034: West Saxon Diphthong Chain

## 1. Role in the book

The older outline below records an editorial scaffold proposal. The current
scientific question is the component identity of early glide reanalysis,
later English realization and their representation-dependent interfaces.
Sections 11–13 hold that research packet; chapter size does not decide
which law or historical stage to implement.

This region also matters structurally because it connects the earlier OE
fronting and diphthong zone to the already promoted `SC043` Anglo-Frisian
Brightening report. Even if the final chapter shape changes, the corridor is not
accidental.

## 2. Name and basic formulation

- **change_ids:** `SC031`; `SC032`; `SC033`; `SC034`
- **display_names:** `OE WW Simplification`; `OE Diphthong Leveling`; `OE Ew Long Diphthong`; `OE Aw Long Diphthong`
- **rule_names:** `OEWWSimplification`; `OEDiphthongLeveling`; `OEEwLongDiphthong`; `OEAwLongDiphthong`
- **executable order:** derived from `oe_pipeline.py`; the older
  order-test coordinates are archival, not current cascade positions
- **cards:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC031-oe-ww-simplification.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC032-oe-diphthong-leveling.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC033-oe-ew-long-diphthong.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC034-oe-aw-long-diphthong.md`

Working formulation: the scaffold currently gathers four connected diphthongal
developments in early Old English. The sources support the region, but they do
not yet prove that one unchanged four-change production report is the best final
chapter shape.

## 3. Traditional description and literature

Ringe and Taylor distinguish early glide reanalysis from the later English
realization of its products. Coronal assimilation supplies ww in four/you
before PWGmc Vww > Vuw; their general account also derives hawwan > hauwan.
English au then undergoes its own first-element and offglide developments
([@RingeTaylor2014, pp. 41–42, 65–66, 171–173]).
Campbell describes the English outcomes of the relevant West Germanic
glide sequences ([@Campbell1959, pp. 44–47]).

These sources support a connected corridor, not the historical identity or
uniform West Saxon date of all four executable definitions. The decisive
question is therefore component specification, not merely chapter size.
SC032's atomic and split-symbol clauses require separate source mappings;
SC033's already-English long-vowel output cannot simply be called an
early PWGmc intermediate. The comparative synthesis's sections 8–9 own
the research targets and cross-component state.

## 4. Formal implementation

CAPR's four rules divide the region more sharply than the handbooks do.

1. `OEWWSimplification` captures the reduction of `ww`-type sequences that feed
   later `ēaw`-type outputs.
2. `OEDiphthongLeveling` regularizes later diphthongal outcomes in a way that is
   useful inside the model, even if the handbooks do not isolate it as one
   separate named law.
3. `OEEwLongDiphthong` captures the long `ēow`-type side of the corridor.
4. `OEAwLongDiphthong` captures the long `ēaw`-type side that also links
   forward into the brightening context.

For book purposes, the main point is architectural rather than technical: CAPR
separates several related diphthong histories that the handbooks often describe
in a more bundled way.

**Internal reorder and context extension (corpus-maturation pass 01).**
`OEEwLongDiphthong` (SC033) is now composed **before** `OEWWSimplification`
(SC031) and `OEDiphthongLeveling` (SC032), and its context admits the
word-final geminate (`{*w} .#.`) alongside the prevocalic cases. The earlier implementation was motivated by Ringe and Taylor's
dating of geminate-`w` reanalysis to Proto-West Germanic: "PGmc *fedwōr 'four' ... > *fewwar > PWGmc
*feuwar" and "PGmc *izwiz 'you (dat. pl.)' ... > *iwwi > PWGmc *iuwi ~ *iuw
... > OE īow" [@RingeTaylor2014, §3.1.1, pp. 41–42]; cf. Campbell on West
Germanic *iuu > OE *iow/eow* [@Campbell1959, §120.2–3, pp. 44–47]. The
vocalization must therefore see the geminate before any degemination, and it
must reach word-final `*-ww` (R&T's apocopated PWGmc variant `*iuw`, the
form OE *ēow* continues). This supports the early feeder, not the
historical identity of its Vuw output with SC033's already-English ēo tier.
For every pre-existing corpus row the old and new
orders are output-equivalent (validated: 0/380 regression differences; the
reorder lies inside the recorded safe computational windows SC031 `14–33`
and SC033 `14–43`); the correction becomes empirically visible only with the
*you* lexeme. See `audits/corpus-maturation-01-candidate-adjudication.md`
§2–2a and `audits/sc098-dossier-unstressed-word-final-i-apocope.md`.

## 5. Place in the cascade

`SC031-SC034` sits in a narratively useful place.

1. It follows `SC030` OE Au Fronting.
2. It precedes the prefix and compound adjustments at `SC035-SC037`.
3. It has forward links to `SC040`, `SC043`, and `SC044`.
4. It sits immediately upstream of the already promoted `SC043` report.

That means the corridor can already be narrated as a real middle zone in the
assembled half, even though its final chapter boundary remains open.

## 6. Order-testing evidence

The chronology cards justify dossiering the region, but not yet promoting it.

1. `SC031 < SC034`, and `SC034` after `SC031`, with `dew` and `hew`.
2. `SC032` follows `SC030` and precedes `SC040`, with no-output earlier
   failures such as `believe`, `bow`, `bread`, `dream`, and `flea`, and the
   later `head` boundary.
3. `SC033` precedes `SC044`, with `chew`, `four`, and `knee`.
4. `SC034` precedes `SC043`, with the `show` side of the corridor.
5. The earlier-side expanded-PWGmc notes for `SC031` and `SC033` are
   supplementary only, not default ordinary historical boundaries.

This is enough to make the region chapter-sized for preparatory work. It is not
yet enough to determine whether the final chapter should stay as four changes or
split around the `SC031`/`SC034` pair.

## 7. Interpretation for the book

The main book-level conclusion is straightforward.

The region is real and visible enough to justify full dossier preparation, but
whether it should become a whole-chain production report remains open.
`SC031`/`SC034` is the strongest local core. `SC032` and `SC033` may still
belong inside the same chapter, but they are also the most likely members to
end up as subordinate sections, bridge material, or residual notes if the unit
is later split.

That was an editorial uncertainty, not a scientific disposition. The current
next decision concerns exactly conditioned component histories and their
prosodic interfaces; chapter membership follows a separately approved account.

## 8. Relation to neighbouring changes

1. **SC030 OE Au Fronting** is the main left context for `SC032`.
2. **SC040 OE Med Unstressed U Lowering** is the right context for `SC032`.
3. **SC043 Anglo-Frisian Brightening** is the already promoted right-hand
   context for `SC034`.
4. **SC044 OE Breaking** is the right-hand context for `SC033`.
5. **SC035-SC037** remains later scaffold bridge material rather than part of
   this chapter.

The region is therefore well situated, but not closed off from the rest of the
book.

## 9. Remaining uncertainty

1. Should the eventual chapter remain a whole-chain `SC031-SC034` report?
2. Should it split later around the `SC031`/`SC034` reciprocal pair?
3. How much weight should be given to `SC032`'s no-output failures in book
   prose?
4. How much of `SC031` and `SC033`'s expanded-PWGmc notes belongs in the book,
   if any?
5. Does `SC033` belong partly with the later breaking context?
6. Is `SC032` central enough to keep full chapter status if a split happens?

## 10. Proposed book-section outline

### If promoted as a whole-chain report

1. **Why the West Saxon diphthong chain is a real region**
2. **The `SC031`/`SC034` reciprocal core**
3. **How `SC032` fits as a leveling bridge**
4. **How `SC033` fits as an `ēow`-side follower with a rightward breaking link**
5. **How the corridor leads into `SC043` and `SC044`**
6. **What remains uncertain about chapter shape**

### If later split around SC031-SC034

1. **`SC031` and `SC034` as the primary diphthong core**
2. **`dew` and `hew` as the narrow historical center**
3. **`SC032` as a later leveling or smoothing-side bridge note**
4. **`SC033` as a long-diphthong side note with cross-reference to breaking**
5. **Why the wider corridor still matters even if the production chapter narrows**

## 11. SC031-led component research packet

### Identity and question

SC031 `OEWWSimplification`, with SC032–034 as coupled context.
Branch `update`, base `67a18cfb`; no production verdict or rule change.
The falsifiable question is whether literal ww deletion and the English
long-diphthong proxies faithfully represent the separately sourced early
Vww reanalysis and later vowel history. Equal final outputs alone would
not confirm historical identity; inconsistent source-backed intermediates
or out-of-domain firings would refute the proposed mapping.

### Current state

The registry still classifies SC031–034 as `ws_oe`/`west_saxon`;
this packet does not change those incumbent values. SC031 rewrites ww > w
without a vowel/context restriction. The current derived sequence is
SC033, SC031, SC032, SC034. SC033 has already emitted the English long
eo tier before simplification on its live e/i paths; SC034 later handles
the surviving aw paths. SC029's awwj path is separate.

The existing chronology card retains archival experiment coordinates and
selected inputs. In particular, its older geminated hay input is not the
current selected *xáwją*. Its technical bundled-PWGmc boundary and the
reciprocal dew/hew displacement pair are not two independently dated
historical before-edges.

### Diagnosis: complete current SC031 census

Fresh `adjudicate.py SC031 --evidence` rebuilt the canonical container
stage bins and found six changes among 387 runnable rows. Stable IDs and
selected forms below are from the live TSV; readable states suppress
CAPR's repeated symbol-boundary asterisks without altering segments.

| ID | Lexeme / selected input | Before SC031 | After SC031 | Evidential role |
| --- | --- | --- | --- | --- |
| 1976 | chew, *kéwwaną* | *kēowwaną* | *kēowaną* | Live deletion after an already-long English-tier product; source component mapping still needed |
| 1989 | dew, *dáwwō* | *dáwwu* | *dáwu* | Live a-path and stored displacement witness with SC034 |
| 2029 | four, *fédwōr* | *fēowwar* | *fēowar* | Assimilation feeder, followed by the current telescoped realization |
| 2074 | hew, *xáwwaną* | *xáwwaną* | *xáwaną* | Live a-path; source hawwan > hauwan comparison and stored SC034 boundary |
| 2326 | you, *ízwiz* | *ēoww* | *ēow* | Assimilation/apocope feeder with final retained glide |
| 2332 | hue, *xéwją* | *xēowwją* | *xēowją* | j-conditioned control, not automatic evidence for ordinary Vww identity |

Hay 2061 is unchanged here, with *xáeują* on both sides. Strew 2227
belongs to the separate awwj context and its stored West Saxon target is
explicitly reconstructed, not an attested positive. The live census
establishes these operations, not six independent dates for one law.

### Literature and historical analysis

Source-supported chain: coronal assimilation < early Vww > Vuw reanalysis
< later English diphthong realization
([@RingeTaylor2014, pp. 41–42, 65–66, 171–173]).
The early feeder is broader than a West Saxon final outcome. Precisely
which inherited/j-created/quantity classes share each early component
still requires the source-faithful specification; it cannot be inferred
from the unconditional executable deletion.

CAPR's current decomposition is a representation choice. A coherent
variant should explicitly separate early au/eu/iu formation, retained
glide treatment and later English quantity/vocalism, while controlling
the distinct awwj/iwj paths. It must audit every SC032 clause rather than
move only SC030 or relabel SC033's output. The proposed historical target
is evidence-led; full-corpus equivalence would test its formalization,
not select it over a different history.

### Verdict and propagation

No canonical verdict is issued; no `Registry-verdict` line is added.
The isolated subset experiments below are now compiled; no new
displacement results are claimed. The stored card remains historical
experiment evidence, with its input/order limitations explicitly stated.
Rule source, registry values, chronology edges and corpus inputs are
unchanged. The packet and comparative ledger are research preparation;
individual component proposals and approvals remain necessary.

### Residue and required tests

Specify each early reanalysis member and later completion law with source
input, quantity, stress and conditioning. Then test identity wrappers,
all six live applications, hay/strew and nonmatching ww/j classes;
assert intermediates at the disputed components and all 387 final outputs.
Separate the seven known mismatches from any new effects. Reject missing
outputs or new ambiguity. Do not overwrite canonical bins, traces or
fingerprints with variant artifacts.

## 12. Isolated early-reanalysis experiment and the SC098 interface

These are research results, not an approved production split.
The runner mechanically derives the incumbent composition and mirrors
all enclosing production wrappers. An identity build matched all 387
live OE outputs. Compiler work and stage bins stayed in private container
temporary directories; source, corpus, sandbox, build manifest, live bin
and canonical stage-bin hashes were unchanged.

### Source-faithful subset and explicit placement premise

The `d-aei-ww` recipe inserts a/e/i + ww > au/eu/iu + w immediately after
coronal assimilation, before the subsequent j-gemination. The source
describes first-member glide reanalysis, the assimilation feeder and the
later English completion ([@RingeTaylor2014, pp. 41–42, 65–66, 171–173]).
The selected early insertion is a representative placement separating
inherited geminates from later palatal glide sequences, not a newly proven
total-order edge. Neither high homorganic uww/jj nor every quantity/stress
class is specified here. Current SC031–034 remain completion/proxy controls.

| Witness | After early reanalysis | Consequence in this experiment |
| --- | --- | --- |
| chew 1976 | *kéuwaną* | English completion converges on the incumbent *ċēowan* |
| dew 1989 | *dáuwō* | Completion converges on *dēaw*, with a different prosodic-tier intermediate |
| four 2029 | *féuwar* | Explicit source-supported early feeder; completion gives *fēower* |
| hew 2074 | *xáuwaną* | Explicit source-supported early au history; completion gives *hēawan* |
| you 2326 | *íuwiz* | SC098's ww-dependent apocope no longer fires; erroneous downstream *īei* |
| hue 2332 | unchanged *xéwją* | Later j-gemination creates ww; the separate incumbent path gives *hīew* |
| hay/strew 2061/2227 | unchanged awj | Their later j-created awwj resolution stays unaffected |

### Diagnosis, not a refutation of the historical target

Only you changed at the final output; the other 386 rows were identical.
The seven existing mismatches were preserved, with you as one additional
mismatch. No missing or ambiguous final output occurred.

This is not evidence against early glide reanalysis. SC098 literally
deletes final i after ww as a narrow stand-in for unstressed-word apocope.
Vocalizing the first w makes that representation-dependent proxy stop
recognizing the same word. The source's iuwi ~ iuw and lack of mutation
support the prosodic/apocope account, not a requirement to retain consonantal
ww until the English diphthong networks ([@RingeTaylor2014, pp. 41–42, 57–58]).

A second recipe, `d-aei-ww-proxy-control`, extends only that temporary
proxy's input recognition to the newly vocalized au/eu/iu + w sequences.
It restored all 387 baseline final outputs, with exactly the original seven
mismatches, zero missing outputs and zero ambiguity. You then passes
*íuwi > íuw* at that checkpoint and completes to *ēow*.
This controls the computational dependency; it does not establish an
exceptionless historical conditioner from those segments or encode
sentence stress.

### Readiness consequence

Do not reject the source history because the unadjusted recipe failed you;
do not adopt the broadened technical proxy because it restored the score.
Production decomposition must specify its other vowel/glide classes and
represent the relevant prosody, or explicitly adjudicate SC098's proxy
compatibility with that decomposition. SC098 is now a concrete interface
gate, not an approved new law or a licence for a lexeme-specific exception.
Its scientific changes would require a separate decision/approval packet.

The recipes and complete stable-ID/intermediate reports are available through
the research backend; they do not overwrite the archival chronology card or
canonical interaction matrix. This gives a discriminating intermediate
test and a genuine dependency diagnosis without admitting another OE row.

The initial research fixture table preserves nine exact intermediate
assertions across the eight existing row IDs above, including a separate
SC098-control assertion. Each was checked against the executed private
reports. It retains Foma atomic-symbol boundaries and labels strew as
reconstructed rather than attested OE. Those assertions are a bounded
test specification, not a completed full-domain D law or new corpus data.

## 13. Incumbent clause map and research disposition

This is a complete map of the current D clauses, not a newly proposed
historical rule set. Quantities, stress encodings and symbol boundaries
below are executable facts. Source mappings and output-equivalent controls
remain separately identified.

| Component | Literal incumbent input/output | Current condition | Research disposition |
|---|---|---|---|
| SC031 | w w → w | Unrestricted | Retain as incumbent control; not identified with earlier Vww vocalization |
| SC033 | e/i/é/í + w → ēo + w | Weak-tail or vocalic continuation, including a final geminate | Retain completion control; full historical split deferred |
| SC034 | a + w → ēa + w; á + w → ḗa + w | Following vocalic symbol or ô | Retain completion control; quantity/stress mapping must accompany a split |
| SC032 fronted-au atomic | aeu/áeu → ēa | Unrestricted | Coupled completion after SC030; cannot strand the input by moving fronting alone |
| SC032 eu atomic | eu/éu → ēo | Unrestricted | Long-tier realization; not automatically the same event as au completion |
| SC032 iu atomic | iu/íu → ēo | Unrestricted | Long-tier realization; SC098 prosodic dependency must remain compatible |
| SC032 e + u split | e u → eo; é u → éo | Unrestricted | Short/stress-preserving representation; no assumed equivalence to atomic eu |
| SC032 i + u split | i u → eo | Unrestricted; no parallel í clause | Independent input/tier audit; no unsupported extra stressed clause |
| SC029 context | a/á + w w j → au/áu + j | Explicit j sequence | Existing settled control, not automatically reopened |

The early a/e/i inherited-ww subset has exact intermediate assertions and
executed all-row tests. Extending it to uww, jj, other quantities or all
j-created geminates is not justified by an unconditional ww-deletion
network. Ringe and Taylor's early and later histories must supply the
expanded domains; Campbell's glide descriptions must be checked against
the selected cell and source notation
([@RingeTaylor2014, pp. 41–42, 65–66, 171–173;
@Campbell1959, pp. 44–47]).

The present research disposition is therefore concrete: RETAIN each
incumbent network as the regression control; DEFER a full production
decomposition until its complete source domain and SC098 prosodic
representation are specified and individually approved. These are packet
recommendations, not canonical registry verdicts. No current code diff is
recommended merely because a technical proxy control restores the score.
The runnable subset remains useful evidence and is not discarded because
the larger proposal is not production-ready.

## 14. Expanded component census and exact intermediate controls

The protected identity, early-subset and technical-control experiments
now expose thirty-five checkpoints across all six research cases.
Each covers every selected OE row, preserves all protected canonical
artifact hashes and first proves final-output equivalence of the
unmodified composition. Paired incumbent D counts are:

| Component | Identity | Early a/e/i-ww subset | Subset plus technical apocope control |
|---|---:|---:|---:|
| SC031 literal ww simplification | 6 | 1 | 1 |
| SC032 leveling bundle | 27 | 32 | 32 |
| SC033 e/i+w long realization | 5 | 2 | 2 |
| SC034 a+w long realization | 6 | 4 | 4 |

Complete identity application IDs are:

- SC031: 1976, 1989, 2029, 2074, 2326, 2332.
- SC032: 1944, 1961, 1962, 1966, 1968, 1988, 1995, 2018, 2019,
  2022, 2028, 2032, 2033, 2061, 2063, 2094, 2097, 2102, 2116,
  2135, 2151, 2170, 2184, 2225, 2227, 2241, 2246.
- SC033: 1976, 2029, 2085, 2326, 2332.
- SC034: 1989, 2074, 2186, 2224, 2317, 2318.

Under both subset recipes SC031 retains only hue2332; SC033 retains
knee2085 and hue2332; SC034 retains show2186, straw2224 and
the two show cells2317/2318. SC032 additionally handles chew1976,
dew1989, four2029, hew2074 and you2326.
SC030 also gains dew/hew (18→20 applications), because their
earlier reanalysis now supplies its au input. These are altered proxy
application sites, not newly demonstrated historical chronology edges.

All 387 identity finals equal the incumbent output; the original seven
mismatches remain 1973, 2013, 2030, 2162, 2240, 2298 and 2300.
Only you2326 changes under the early subset. The technical apocope
control restores every baseline final with no missing or ambiguous
output. All nine D atomic-symbol fixture assertions pass; the research
table additionally has sixteen incumbent controls for A/F/P/U/B.
The source-domain and prosodic limits remain those stated in sections
12–13, not solved by unchanged scores
([@RingeTaylor2014, pp. 41–42, 57–58, 65–66, 171–173;
@Campbell1959, pp. 44–47]).

## 15. Implementation continuation: apocope proxy-domain control

Fresh SC031 evidence still has six applications: chew1976, dew1989,
four2029, hew2074, you2326 and hue2332. Hay is not a live simplification
witness. No production rule or canonical verdict has changed.

The updated private technical-control run preserves all 387 baseline
finals and its exact you-apocope assertion. It also compares the literal
match domains on a hypothetical component-local `*s*au*w*i` sequence:

| Network | Input | Output |
|---|---|---|
| Incumbent final-i proxy | `*s*au*w*i` | `*s*au*w*i` |
| Expanded representation control | `*s*au*w*i` | `*s*au*w` |

The sequence is not an attested lexeme, PGmc reconstruction or full-cascade
input. The comparison establishes a formal domain expansion: the extended
matcher also recognizes an already represented diphthong-plus-w, not just
literal ww. It does not establish that a particular historical word should
retain i, nor supply a historical chronology edge.

Consequently restoring you cannot certify this control as a pure,
historically justified compatibility repair. Complete source-domain and
prosodic analysis remains necessary before any SC098 proposal. The actual
source unstressed-word account and earlier reanalysis remain separately
supported phenomena [@RingeTaylor2014, pp. 41–42, 57–58, 65–66].
No stress condition is inferred from the hypothetical string or from an
FST identifier.
