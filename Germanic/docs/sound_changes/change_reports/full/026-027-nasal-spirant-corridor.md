# North Sea Germanic nasal-loss corridor

### Sound-change report

#### Historical formulation

SC026 and SC027 together represent the bundled North Sea Germanic /
Ingvaeonic development in which nasals are lost before voiceless fricatives,
with compensatory lengthening and often an intermediate nasalized stage in the
preceding vowel. That bundled process is the historical core supported by the
handbook tradition. CAPR's labels **NWGmc Nasal Spirant Lengthening** and
**NWGmc Nasal Spirant Loss** should therefore be read as an analytic split of
one broader development, not as two independently standard named laws
[@Campbell1959, §121; @Fulk2018, §4.11; @Luick1914, §301.1;
@SieversBrunner1965, §186.1].

#### Source tradition

Campbell, Fulk, and Sievers-Brunner give the clearest traditional formulation
of the bundled process: before voiceless fricatives, the nasal disappears and
the preceding vowel is lengthened, often with nasalization in the historical
description [@Campbell1959, §121; @Fulk2018, §4.11;
@SieversBrunner1965, §186.1]. Hogg is especially useful for the compact
`*ansuz > ōs` type, where rounding, nasal loss, and compensatory lengthening
are kept together as one connected development [@HoggPhonology1992]. Ringe and Taylor
help most with stage assignment: they treat forms such as `goose` and `youth`
as outcomes of a broader northern West Germanic development rather than as a
late isolated Old English innovation [@RingeTaylor2014, pp. 140--141]. Luick
adds the most useful internal phonological refinement by describing a long
nasalized-vowel stage that later loses its nasal quality and by distinguishing
the special `a`-branch without turning the process into separately named laws
[@Luick1914, §§299, 301.1].

#### CAPR implementation

CAPR makes the historical bundle explicit as two adjacent rules. `SC026`
adjusts vowel quality and quantity while the nasal + voiceless-fricative
conditioning environment is still present; `SC027` then deletes the nasal
before the spirant. That split is stricter than ordinary handbook prose, but it
is defensible as a model articulation of the same historical development: the
transducer needs the conditioning string to remain visible long enough for the
vowel effects to apply before the nasal is removed. The report should therefore
present the split as a formal clarification inside CAPR, not as direct proof
that the traditional literature recognized two separately named sound laws
[@Fulk2018, §4.11; @Luick1914, §301.1].

#### Place in the cascade

`SC026-SC027` sits after the early unstressed and boundary-limited Northwest
Germanic zone and before the early `x`-loss and glide/fronting entry zone. The
pair follows nearby left-side context such as `SC025`, but its strongest local
identity is internal: `SC026` and `SC027` form a tight reciprocal center. On
the right, `SC028` provides useful context, especially for forms such as
`fist`, because later `x`-loss and fronting material still help shape the final
Old English outcome. But that neighboring context should remain contextual
rather than being folded into this unit.

#### Order evidence

The chronology cards give the pair an unusually clear local result. `SC026`
cannot move later across `SC027`, and `SC027` cannot move earlier across
`SC026`. The shared failure set is `fist`, `goose`, and `youth`: if the nasal
is deleted too early or the vowel adjustment delayed too long, the model loses
the conditioning environment and restores the wrong vocalism. The positive
local claim is therefore straightforward: in the present system the corridor
requires `SC026 < SC027`.

#### Interpretation

For book purposes, this is the first strong paired report after the
singleton treatments because it shows how CAPR can sharpen a historically
bundled process into a formally ordered corridor without pretending that the
handbooks already drew the same line. The historical claim remains the bundled
North Sea Germanic / Ingvaeonic nasal-loss development. CAPR then makes the
internal sequencing explicit, and the chronology evidence shows that once this
modeling choice is made only one local order works. The chapter should
therefore present the pair as a disciplined bridge between handbook tradition
and formal implementation.

#### Remaining cautions

The cautions are as important as the positive result. The earlier side of
`SC026` remains runner-limited at bundled `EarlyEnglishLineChanges`, so the current
evidence does **not** identify an earlier historical boundary for the pair. The
later side of `SC027` is a no-break-before-boundary result through order `86`,
so the current evidence does **not** justify a claim that the corridor must
precede `SC087`. More broadly, CAPR's two-rule split is best treated as a
defensible model articulation rather than as proof of two separately named
historical laws. The stage label also needs care: CAPR files the pair as
`NWGmc`, whereas much of the literature frames it more broadly as North Sea
Germanic or Ingvaeonic [@RingeTaylor2014, pp. 140--141; @Fulk2018, §4.11].
Finally, `fist` is a valuable chronology example, but it is a multi-stage
derivation and should not be used as if this corridor alone explained the whole
Old English output.
