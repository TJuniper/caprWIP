# SC028 adjudication: the \*xs-cluster simplification

Registry-verdict: SC028=RETAIN/REORDER

**Date:** 2026-09-12
**Verdict:** RETAIN / REORDER, with restaging (the registry verdict vocabulary
has no RESTAGE token; the stage change is recorded in the stage columns)
**Rule:** `PNWGmcPreconsonantalXLoss` (identifier retained; rename deferred)
**Outcome:** executable structural description unchanged; name, stage, scope,
confidence, citation, cascade placement and chronology metadata all corrected.
**Corpus/output effect:** none. 386 rows, 379 matched, 7 pre-existing
mismatches, both frozen fingerprints byte-identical.

---

## 1. The claim actually under adjudication

The display name said "Preconsonantal \*x Loss" and the stage said Northwest
Germanic. Neither describes the executable rule, which is:

```foma
{*x} -> 0 || _ {*s} EnglishStarConsonant
```

That is not a general loss of \*x before a consonant. It deletes \*x only in
the cluster **\*xs followed by a further consonant**. The adjudication was
conducted against that structural description, not against the label.

In `fist` the rule receives \*fū́xstiz and returns \*fū́stiz:

```
EnglishProtoInput            *f*ú*n*x*s*t*i*z
PGmcNasalLossBeforeX (SC103) *f*ū*x*s*t*i*z
PNWGmcPreconsonantalXLoss    *f*ū*s*t*i*z
...                          fȳst
```

## 2. Corpus audit of every \*x cluster

All 386 selected rows were scanned for \*x followed by any consonant run.

| cluster | count | lexemes | behaviour |
|---|---|---|---|
| \*xst | 1 | `fist` | **simplified** — the sole positive witness |
| \*xt | 8 | `thought`, `fight`, `fright`, `knight`, `light`, `might`, `night`, `wight` | retained |
| \*xs (no following C) | 5 | `flax`, `fox`, `six`, `wax` | retained, giving OE `x` = [ks] |
| \*xs+V | 1 | `ox` (\*úxsô) | retained |
| \*xl, \*xw, \*xn, \*xr, \*xj, \*xz, \*xC-initial | 9 | `lade`, `laugh`, `lid`, `whale`, `who`, `neck`, `raven`, `hair`, `flea` | word-initial clusters, out of domain |

No corpus form is near the boundary of the rule other than the \*xs and \*xt
sets, and both behave as the sources require. The audit is therefore decisive
for the domain question in §5.

## 3. Campbell §461 was a false conflation

The reader chapter cited Campbell §461 and offered *flēam* and *hēla* as
examples of "the same broad development". Reading §461 directly shows that it
treats something else entirely: the reduction of initial \*x to a breathing, its
disappearance before *l*, *n*, *r*, *w* where the written *h* is only a
diacritic, and the West Germanic weakening of medial \*x to a breathing between
vowels and between a vowel and *l*, *m*, *n*, *r*, which was then lost early in
Old English [@Campbell1959, p. 186, §461]. Bülbring treats the same change
separately from the cluster rule, as loss of \*x between a vowel and a voiced
consonant with compensatory lengthening, giving *ȳmest*, *lǣne*, *nēalǣcan*,
*stȳle*, *betwēonum* and *ēorod* [@Bulbring1902, p. 215, §528].

That change is defined by a following **sonorant** and produces compensatory
lengthening. SC028 is defined by a following **\*s plus consonant** and produces
none. *flēam* and *hēla* instantiate the former and have no bearing on the
latter. The citation has been removed rather than salvaged.

The §461/§528 change is not currently implemented in CAPR, and no selected
corpus form requires it: every corpus form with \*x before a sonorant has it
word-initially. This is recorded as scientific-input debt, not adjudicated here.

The correct citation for SC028 is **Campbell §417**, with §416 and §464 as the
controls.

## 4. The sources on the change itself

Four independent handbook statements agree on the environment.

* **Campbell §417 p. 170:** "When a consonant follows, xs > s in OE", with
  *wæstm*, *wæsma*, Northumbrian *sesta* beside West Saxon *siexta*; but \*x is
  kept in *wrixlan*, "where l is vocalic".
* **Brunner §221.2 p. 184:** "Wenn auf hs andere Konsonanten (auch j) folgen,
  ist h ausgefallen", with *nēos(i)an*, *þīsl* beside older *þixl*, *wæsma*,
  *wæstm*, Northumbrian *sesta*; "jedoch bleibt x erhalten in wrixlan".
* **Bülbring §527 p. 215:** "Im Urengl. ist xs vor Konsonanten in der Regel zu
  s geworden", with *þisle*, *wæstm*, *wrislan*, *sester*, *sesta*, *ġeniosian*.
* **Ringe & Taylor pp. 157–158:** PGmc \*niuhsijaną > PWGmc \*niusjan > OE
  *nēosan*; \*sehstō > Northumbrian *sesta*; PNWGmc \*þihslu > OE *þīsl*;
  (post-)PWGmc \*wahstm > OE *wæstm*. Their formulation is that \*h was lost
  "possibly variably, possibly only in some dialects, when followed by two or
  more consonants".

The following consonant is therefore attested as \*t (*sesta*), \*m (*wæstm*),
\*j (*nēosan*) and \*l (*þīsl*), and Campbell and Brunner agree that a *syllabic*
sonorant does not trigger the change (*wrixlan*).

## 5. The consonantal domain

Of the five candidate formulations, the corpus and the sources select the same
one.

| hypothesis | verdict |
|---|---|
| **A. \*xsC > \*sC** | **accepted** |
| B. correct process, wrong scope/date | partly accepted — the date and scope were wrong, see §6 |
| C. specifically \*xst > \*st | rejected: *wæstm* has \*m, *nēosan* has \*j, *þīsl* has \*l |
| D. broader \*xs > \*s | rejected: `fox`, `six`, `wax`, `flax`, `ox` keep the \*x, and Campbell §416 shows it survived to cause breaking and then hardened to [ks] |
| E. not an independent change | rejected, see §7 |

The current executable structural description is thus **correct as written** and
has not been altered. The \*s in it is load-bearing in a second way: an earlier
CAPR formulation used a bare `_ CC` schema and overgenerated, deleting the first
element of geminate \*xx before \*j, where Old English has *hliehhan* with the
geminate intact [@Campbell1959, p. 186, §464].

The narrowing to \*xst that `fist` alone would suggest is **not** adopted,
because the comparative rule is demonstrably broader.

## 6. Stage, scope and confidence

**Not Proto-Germanic.** Gothic retains the \*h in *bi-niuhsjan* and *saihsta*
[@RingeTaylor2014, pp. 157–158; @Campbell1959, p. 170, §417]. This is the
single most important comparative fact in the adjudication.

**Distribution.** Campbell reports the loss from "all West Gmc. languages, and
in North Gmc.", citing ON *ísl*, ON *nýsa*, OS *weslon*, OS *wastum*, OS
*niustan*, OHG *niusen*, and OS/OHG *lastar*. That would support a Northwest
Germanic dating. Ringe and Taylor, treating the same material more closely,
prefer a shared **northern West Germanic** change on the strength of OS
*wastum*, *thisla* and *niusian*, and explicitly allow that the North Germanic
agreement is "a partly parallel change in the diverging NWGmc dialects". They
also record genuine counterevidence to full regularity: *þixl* competing with
*þīsl* in early Mercian, *eaxl* < \*ahslu, West Saxon *siexta*, and OHG *sehsto*
and *dihsala*.

**Verdict.** `hist_stage` moves from `pnwgmc` to `pwgmc`; `hist_scope` from
`pan_pnwgmc` to `north_wgmc`; stage labels to "Northern West Germanic".

**Confidence: B**, and the components are deliberately separated, because they
do not deserve the same rating.

| component | rating |
|---|---|
| that \*x was lost in \*xs before a consonant | A — four independent handbooks, converging examples |
| the structural domain \*xsC | A for \*t/\*m/\*j; the syllabic-sonorant exception is a real but understood residue |
| the subgroup and date | **B** — northern West Germanic per Ringe & Taylor, but parallel drift in the diverging Northwest Germanic dialects is explicitly left open by them, and the change is described as possibly variable and possibly dialect-limited |

The single stored value is B, which is the rating of the weakest component. The
existence of the change is not in doubt; the precision of its dating is.

`fist` itself cannot settle the date: its cognate set is West Germanic
throughout — OE *fȳst*, OFris *fēst*, OS and OHG *fūst*, Du. *vuist*, MDu.
*vuust*, G *Faust* [@Kroonen2013, p. 160; @Orel2003, p. 157] — with no Gothic or
Old Norse reflex. The stage is established from \*niuhsjan, \*sehstō and
\*þihslu, not from the CAPR witness.

## 7. SC028 is historically separate from SC103

Gothic decides this. Gothic underwent the Proto-Germanic nasal loss before \*x
(*þūhta*, *brāhta*, *þeihan*) but did **not** undergo the cluster simplification
(*bi-niuhsjan*, *saihsta*). One daughter therefore shows the first change
without the second, which is direct evidence that they are two changes and not
two facets of one.

The internal evidence points the same way. After SC103, `thought` has \*xt and
keeps its \*x, while `fist` has \*xst and loses it. If nasal loss and cluster
simplification were one development, the \*x of `thought` should have gone too.
The same contrast is attested independently of the nasal in OHG/OS *lastar* <
\*laxstra- against OE *leahtor* < \*laxtra-.

Hypothesis E is therefore rejected. The two rules stay separate.

## 8. Placement

The former placement — after the North Sea Germanic nasal-spirant law — was a
stage inversion, putting a northern West Germanic change after an Ingvaeonic
one. It survived only because SC028's input used to be thought of as created by
the nasal-spirant law, an assumption the SC103 adjudication removed.

Two source-based constraints are available, and only two.

* **Lower bound.** Ringe and Taylor place the loss after the Proto-West Germanic
  syncope of \*-CijV-, which is what creates the \*sj of \*niuhsjan
  [@RingeTaylor2014, p. 157].
* **Upper bound.** They place it before breaking, since the undiphthongized
  vowels of *wæstm* and *þīsl* "can be accounted for only by supposing that
  these \*h were lost before breaking took place" [@RingeTaylor2014, p. 158].

The rule is now composed immediately after `PWGmcSyllabicJ`, which is the
tightest placement the sources license: directly after the syncope complex, far
before breaking, and inside the northern West Germanic region of the cascade
beside `EAFLThVoicing`. No finer local order against neighbouring rules is
claimed, and several placements within the window commute.

The move is **output-equivalent**: 386 accepted, 379 matched, 7 mismatched, and
both `outputs_sha256` and `legacy_subset_sha256` byte-identical to the
pre-adjudication state.

## 9. The SC103 → SC028 relation is stage-entailed, not demonstrated

This was tested rather than assumed. A counterfactual cascade was compiled with
SC028 composed before SC103 and `fist` was run through it.

```
production order:     *fúnxstiz -> fȳst
SC028-before-SC103:   *fúnxstiz -> fȳst      (unchanged)
```

The order **commutes**, and the reason is instructive. Deleting the \*x first
yields \*fúnstiz, in which the nasal now stands before \*s; the North Sea
Germanic nasal-spirant law covers \*ns and removes the nasal with compensatory
lengthening, arriving at the same \*fū́stiz by a different historical route. The
surface outcome is overdetermined.

`fist` is therefore a **firing witness** for SC028 but **not** a chronology
witness for SC103 → SC028. The edge is recorded as `stage_entailed` with no
representative lexeme, since the direction follows from the stages alone: SC103
is pan-Germanic, SC028 is post-Gothic. Claiming `independently_demonstrated`
here would have been fabricated evidence, and the guardrails introduced in the
authority pass would have been satisfied by a witness that does not in fact
demonstrate the interaction — exactly the failure mode those guardrails exist to
prevent.

The two stale harness boundary rows for SC028, which recorded only that no first
break was found from its old position, have been removed and replaced by this
edge.

## 10. Falsification and controls

| control | prediction | observed |
|---|---|---|
| `fist` \*xst | simplified | \*fū́xstiz > \*fū́stiz > *fȳst* |
| `thought` \*xt | untouched | \*θą̄xtē unchanged by SC028, OE *þōhte* |
| `fox`, `six`, `wax`, `flax`, `ox` \*xs with no following C | untouched | all retain \*x |
| `fight`, `night`, `light`, `might`, `knight`, `fright`, `wight` \*xt | untouched | all retain \*x |
| geminate \*xx before \*j | must not fire | not in the selected corpus; prevented structurally by the \*s |

Hypothesis D would have been falsified directly by `fox`, `six`, `wax`, `flax`
and `ox`, each of which would have lost its \*x wrongly. Hypothesis C would have
been falsified by *wæstm* and *nēosan* outside the corpus. Both tests were run
and both discriminate.

## 11. No lexeme was added

No new corpus row was created. A second witness was considered and rejected on
the project's own standard: the obvious candidates (*wæstm*, *nēosan*, *þīsl*,
*sesta*) would each test the rule usefully, but none of them is currently in the
selected corpus, and adding vocabulary to raise a firing count is precisely what
the corpus policy forbids. `fist` as the positive witness, the \*xs and \*xt sets
as negative controls, and the comparative material above are sufficient.

## 12. Recorded debt

* The Foma identifier `PNWGmcPreconsonantalXLoss` is now wrong on both counts:
  the change is not Northwest Germanic and it is not general preconsonantal \*x
  loss. The rename is deferred to an isolated behaviour-neutral pass so that it
  does not obscure the scientific diff of this one.
* The reader-facing filename still says `preconsonantal-x-loss`; it moves with
  the rename.
* The Campbell §461 / Bülbring §528 change (loss of \*x between a vowel and a
  voiced consonant, with compensatory lengthening) is not implemented. No
  selected corpus form needs it. Logged as scientific-input debt.

## 13. Summary of changes

| item | before | after |
|---|---|---|
| structural description | `{*x} -> 0 \|\| _ {*s} EnglishStarConsonant` | unchanged |
| display name | Proto-Northwest Germanic Preconsonantal X Loss | Northern West Germanic \*xs-Cluster Simplification |
| `hist_stage` | `pnwgmc` | `pwgmc` |
| `hist_scope` | `pan_pnwgmc` | `north_wgmc` |
| confidence | A | B (dating), with A for existence |
| citation | Campbell §461 (*flēam*, *hēla*) | Campbell §417, with §416 and §464 as controls; Brunner §221.2; Bülbring §527; R/T pp. 157–158 |
| placement | after the Ingvaeonic nasal-spirant law | immediately after `PWGmcSyllabicJ` |
| SC103 → SC028 | two stale harness boundary rows | one `stage_entailed` edge |
| `adjudication_status` | unadjudicated | adjudicated |
