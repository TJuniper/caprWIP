# SC089: wire late unstressed raising to the fricative class

## Identity

- SC id: SC089; executable identifier: `OELateUnstressedAgSuffix`.
- Branch/base: `update`, `16196823`; post-SC043 baseline.

## Question

Will class-distinct g palatalization strand late suffix raising unless its
consumer recognizes the actual fricative rather than only the old ʤ proxy?

## Current state (before any edits)

Unadjudicated historical entry with no historical metadata or reader route.
After epenthesis, the executable fronts medial a to e before g,
palatalizes word-final g to ʤ and raises medial e beside that proxy.
No selected input is changed. Existing FST commentary cites Ringe–Taylor
§6.9.6 with sheet labels 349–350, not the actual printed pp.334–335.

## Diagnosis

The complete current population is honey2079 and withy2296. They are
live late raising applications, not evidence that all palatals cause the
same early mutation. The `p-coupled` assay changes the late g output to
ʝ and lets raising recognize ʝ alongside the retained stop proxy ʤ.
All 387 finals remain unchanged, including huniġ and wīþiġ.
Its word-final guard still excludes g before a back vowel.

## Literature

Existing CAPR owners: 052 hinge dossier, honey/withy lexical sources.
Ringe–Taylor 2014 pp.334–335, §6.9.6, explicitly gives the late
*-ag- > *-æg- > *-eg- > -ig- history, honey, and the back-vowel qualification.
Fulk 2018 pp.130–132 distinguishes the singleton fricative from gg/ng.
Ringe–Taylor p.204 supplies the separate postmutation merger.
CAPR keeps the incumbent narrow suffix implementation; its ʝ consumer
repair does not invent a new historical eligibility domain.

## Historical analysis

Stage/scope: `oe/english_specific`, confidence B for this qualified late
representation. Late palatal raising is not prehistoric i-mutation, so
keeping a distinct fricative here does not claim identical triggering in
those two laws. SC109's subsequent merger slot is technical serialization.
No new independently demonstrated exact-order edge is added.

## Verdict

REFORMULATE the class representation, retain the suffix conditioner and
make its source/reader ownership visible. Correct printed-page provenance.

Registry-verdict: SC089=REFORMULATE

## Propagation (only after verdict)

FST, registry/human notes and reader membership, this memo, 052 dossier,
new 089 reader and affected honey/withy discussion.
Regressions include raising positive, back-vowel negative, class consumers,
reader fidelity, complete corpus preservation and no native symbol leakage.
Baseline/fingerprint effect: none. Closeout records canonical finalization.

## Residue

The narrow word-final consumer is not an exhaustive treatment of the
entire historical suffix paradigm. No exact merger date follows from it.

## Batch closeout

SC089 finalization and propagation passed. The integrated suite passed
688 tests and 6178 subtests. The current-source protected assay
(`oe_adopted_palatal_result.json`) passes raising beside ʝ, late final-g
palatalization, the complete a-g chain and the back-vowel negative.
Honey/withy remain unchanged within all 387 preserved finals; native output
has no residual ʝ, selected inputs are unchanged, and protected artifacts
remain identical.

The full standard book build passed all gates. The inspected 297-page PDF's
printed p.113 contains the new reader, actual consumer definition, native
huniġ/wīþiġ and Ringe–Taylor's printed pp.334–335 (§6.9.6). The holding zone
is explicitly computational, not a newly dated historical merger. No
commit or push occurred.
