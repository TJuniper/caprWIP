# SC051: OE Sk Palatalization

## 1. Role in the book

`SC051` is the clearest immediate candidate exposed by the
`SC049-SC052` palatalization/fronting split review. If promoted later, it would
be a narrow palatalization report rather than a promotion of the whole mixed
cluster.

That makes it a useful test case for the production layer. The question is not
whether Old English palatalization matters in general, but whether one
well-bounded rule with good two-sided card evidence can be promoted cleanly out
of a structurally mixed scaffold.

## 2. Name and basic formulation

- **change_id:** `SC051`
- **display_name:** `OE Sk Palatalization`
- **rule_name:** `OESkPalatalization`
- **current_order:** `51`
- **card:** `Germanic/docs/sound_changes/order_tests/chronology_cards/SC051-oe-sk-palatalization.md`

Working formulation: `SC051` captures the Old English palatalization of `sk`
to `sc` in the environments recognized by the handbook tradition and modeled in
CAPR, while leaving the adjacent plain-velar palatalization and later West
Saxon diphthongization rules outside the chapter's core.

## 3. Traditional description and literature

The literature dossier points in a stable direction.

Campbell, Hogg, Ringe and Taylor, Luick, Fulk, and Sievers-Brunner all support
the historical reality of OE `sk > sc`. They also agree on a basic structural
fact that matters for the book: `sk` palatalization belongs to a larger
palatalization complex, but it is still recognizable enough to isolate for
discussion.

That gives `SC051` a good historical footing. What it does **not** do is settle
the final chapter architecture automatically. The sources make it clear that
`SC051` can be described on its own, but they also show why any narrow report
must cross-reference the broader palatalization zone rather than pretending it
stands entirely alone.

## 4. Formal implementation

In CAPR, `OESkPalatalization` is a narrow rule about the OE treatment of `sk`.
In reader-facing prose, the useful point is simple:

1. back-vowel environments still preserve non-palatal behavior on the left edge;
2. palatalized `sc` then feeds later West Saxon vowel effects on the right.

That is enough formal detail for a later production report. A tiny rule excerpt
could be quoted if needed, but the book chapter should mainly explain the
process in historical terms rather than becoming a rule dump.

## 5. Place in the cascade

`SC051` sits in a promising location for a narrow chapter.

1. It follows `SC046` OE A Restoration.
2. It sits inside the broader `SC049-SC052` palatalization/fronting region.
3. It precedes `SC056` OE Ws Palatal Diphthongization.
4. It is adjacent to the already promoted `SC055-SC056` umlaut-core report,
   which means any eventual SC051 chapter will need cross-reference rather than
   duplication.

This placement gives the chapter a clear narrative role: it can explain one
palatalization rule before the book returns to the larger umlaut and
post-palatalization material nearby.

## 6. Order-testing evidence

The chronology card gives `SC051` unusually clean local support.

1. Earlier boundary: `SC046`, with `flask` and `wash`.
2. Later boundary: `SC056`, with `shaft`, `shear`, `sheath`, `sheep`, and
   `shield`.
3. Both boundaries are historically interpretable and fairly local.

That is exactly why `SC051` is stronger than the whole `SC049-SC052` scaffold:
the chapter can be motivated by two-sided evidence without claiming that every
neighbor in the mixed cluster is already chapter-ready.

## 7. Interpretation for the book

`SC051` may be strong enough to work as a standalone narrow report.

If promoted, that would clarify the surrounding scaffold rather than trying to
solve it all at once. `SC049` could remain residual, `SC050` and `SC052` could
stay under review, and `SC057` could remain a later palatalization-side
question.

The report should also cross-reference `SC056` without duplicating the promoted
`SC055-SC056` chapter. The book value of `SC051` is that it isolates one
palatalization law cleanly, not that it re-narrates the entire OE palatal and
umlaut system.

## 8. Relation to neighbouring changes

1. **SC046 OE A Restoration** is the left anchor and helps explain why the
   earlier card evidence is historically meaningful.
2. **SC050 Sievers-Law Syncope** and **SC052 OE Velar Palatalization** remain
   unresolved neighboring palatalization/fronting material.
3. **SC056 OE Ws Palatal Diphthongization** is the right anchor and the main
   later process that an SC051 chapter would need to mention.
4. **SC057 OE J Cluster Coalescence** remains later palatalization-side material
   still under review.

This is a good neighborhood for a narrow report, but not yet a license to turn
the whole region into one promoted multi-change chapter.

## 9. Remaining uncertainty

1. Should the eventual report be a standalone SC051 chapter or part of a later
   `SC051-SC052` unit?
2. How much of the broader palatalization system should the report summarize?
3. How explicitly should the report relate itself to `SC052`?
4. Could `SC057` later need integration or a stronger cross-reference?
5. How should the chapter relate itself to the already promoted umlaut-core
   report without redundancy?

## 10. Proposed book-section outline

1. **Why SC051 is the first promotable unit inside the mixed palatalization scaffold**
2. **What OE `sk > sc` means in handbook terms**
3. **How `flask` and `wash` define the left edge**
4. **How `shaft`, `shear`, `sheath`, `sheep`, and `shield` define the right edge**
5. **Why `SC051` should stay narrower than the whole `SC049-SC052` cluster**
6. **How the chapter relates to SC052 and SC056**
7. **What remains unresolved in the surrounding palatalization/fronting region**

## 11. P-sk component packet: consonant change is not later vowel treatment

### Identity and question

SOURCE-only research packet, 2026-10-03, branch `update`, base `67a18cfb`;
prepared SC051 route, no new canonical decision. The comparative authority
is the Anglo-Frisian synthesis §8.6. The falsifiable question is whether
the current sk clauses represent one fully conditioned early sound change.
Source distinctions between initial extension and medial/final restrictions,
or a mismatch in back-vowel environments, would refute that identity claim
without refuting the existence of OE sk palatalization.

### Current state and literal incumbent

Prepared characterization: OE, English-specific, unadjudicated.
`OESkPalatalization` is five **serially composed** replacement blocks:

```text
s k -> ʃ || .#. _
s k -> ʃ || EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)
s k -> ʃ || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel
s k -> ʃ || _ j
s k -> ʃ || j _
```

Parenthesized foma context members are optional, not required. Consequently
the literal medial/final implementation is not equivalent to a prose
requirement for flanking consonants or boundaries. The initial block is
unconditional, including before back vowels. The marker ʃ represents an
eventual reflex, not a measured date for the source's [sc]/[sç] articulation
or subsequent sibilant outcome. Later sc-triggered vowel diphthongization
is a distinct SC056 question.

### Diagnosis: complete current firing census

Fresh serial `SC051 --evidence` on 2026-10-03, with healthy backend,
rebuilt stage bins and 387-row production/sandbox equality, changes
**18/387** selected rows:

```text
2014 fish; 2020 flesh; 2175 shaft; 2176 shame; 2177 shear;
2178 sheath; 2179 sheep; 2180 shield; 2181 shilling; 2182 shine;
2183 shoulder; 2184 shove; 2185 shovel; 2186 show; 2187 shower;
2253 thrash; 2317 show (iptv.2sg); 2318 show (3sg).
```

Fifteen are word-initial sk replacements; fish2014, flesh2020 and
thrash2253 are noninitial applications. These are literal class membership,
not fifteen independent observations of the early extension's date.
All eighteen belong to the frozen legacy-380 population too.
Sheath2178 passes `*skāθi > *ʃāθi`: the front vowel is created later
by mutation. Sheep2179 passes `*skǣp > *ʃǣp`; shield2180 passes
`*skéldu > *ʃéldu`. Wash2272 and flask2016 are unchanged here after
restoration. They are negative interface controls, not live applications.
An initial back-vowel preservation claim in the older scaffold above is
therefore not the literal initial rule.

### Literature and historical analysis

Direct OE specification comes from Ringe–Taylor: initial sk originally
before fronts; medial unless a back vowel follows; final unless a back vowel
precedes; initial generalization before all vowels by about 900; a separate
later sibilant realization and still later extension before r
[@RingeTaylor2014, p. 204]. This establishes distinct layers and
conditioned positions, not CAPR's exact five contexts as a single early event.
The current unconditional initial block can be a corpus proxy for the
generalized outcome; it cannot date that extension from sheep alone.

Hogg explicitly excludes sk from his investigation
[@Hogg1979, p. 112 n. 2]. Bremmer's Frisian sk nonpalatalization is
comparative evidence, not the specification of an OE rewrite
[@Bremmer2009, p. 30]. Laker's layered palatal analysis prevents equating
articulation with merger/assibilation [@Laker2007, pp. 167–168, 175–184].
The ordinary and later sc vowel histories have their own source constraints
[@RingeTaylor2014, pp. 215–217, 235; @Campbell1959, pp. 68–69].

### Recommendation, exact tests and boundary

**RETAIN incumbent as the outcome control; DEFER a production split or
restriction into early conditioning and later initial extension.**
Exact proposed diff: **none**. No new chronology edge is inferred from
the composite displacement relation to SC056.

Prerequisites:

1. Full 387-row identity/determinism assay, keeping all eighteen IDs
   and the seven existing mismatch rows visible.
2. Initial front-positive sheep2179/shield2180 versus initial
   back-vowel sheath2178/shoulder2183/shovel2185, with separate
   early-articulation and generalized-outcome checkpoints.
3. Medial/final positive fish2014/flesh2020/thrash2253 versus
   restored wash2272/flask2016 and a source-verified following-back
   fixture. Inspect foma optional contexts explicitly; do not
   silently turn a syntax repair into an approved scientific law.
4. Preserve ordinary shaft2175/shear2177/sheep2179 PD inputs and
   later sheath2178 mutation-product input. A PD success cannot date
   consonantal sk articulation or initial extension.

Each component/date/condition or marker change needs exact approval with
row-level consequences; corpus fixtures remain non-corpus, with no approved
admissions. No reader/registry/FST edit is made here; parent regenerates.
Residue: precise early-versus-generalized initial realization and direct
medial/final negative-input readiness, not an unsourced Frisian analogy.
