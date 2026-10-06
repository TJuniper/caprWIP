# SC026-SC027: Nasal Spirant Corridor

> **Adjudication correction (SC026/SC027 nasal-spirant adjudication).** This
> dossier predates
> `Germanic/docs/sound_changes/audits/sc026-sc027-nasal-spirant-adjudication.md`,
> which supersedes it on three points.
>
> 1. **Consonantal domain.** The North Sea Germanic law applies before \*f, \*þ
>    and \*s only (Campbell §121, p. 47; Fulk §4.11; Sievers–Brunner §186.1;
>    none of the thirty-odd examples in Ringe & Taylor §5.1.1, pp. 139–41,
>    contains \*x). CAPR's `EnglishStarVoicelessFricative` wrongly included
>    \*x and has been replaced by `EnglishStarNSGmcSpirant`.
> 2. **\*nx belongs to an earlier, pan-Germanic change**, now SC103
>    `PGmcNasalLossBeforeX` (Campbell §119, p. 44; Fulk §4.1; Ringe vol. 1).
>    The diagnostic is comparative: the pan-Germanic change leaves no nasal in
>    any daughter (OHG *fūht*, *fūst*, *brāhta*), whereas the cognates of the
>    Ingvaeonic witnesses keep it (OHG *fimf*, *gans*, *ander*, *jugund*).
> 3. **`fist` is not a witness for SC026 or SC027.** PGmc \*funhsti- (Kroonen
>    p. 160) shows the long vowel in OHG *fūst*, Dutch *vuist* and German
>    *Faust*, so its nasal loss is pan-Germanic. It has been withdrawn from the
>    evidential core and from the chronology witness set, which is now `goose`
>    and `youth`. Where this dossier cites `fist` below, read SC103.
>
> The dossier's central conclusion — that the two CAPR rules articulate **one**
> historical sound change — is confirmed, and is now recorded in the registry
> (SC027 carries `canonical_change_id = SC026`). The `SC026 < SC027` ordering is
> an executable dependency, not a demonstrated historical relative chronology.


## 1. Role in the book

SC026-SC027 is the clearest current corridor candidate for the next non-pilot promotion. It is the first attractive **paired** chapter after the two singleton promotions (`SC043` and `SC063`), and it already has the kind of local reciprocal order evidence that makes a short sound-change chapter narratively legible.

It is also a good candidate for a more structural reason. The pair shows one of the main advantages of the CAPR sound-change half: the book can explain how a traditional handbook development may appear in the model not as one monolithic sentence, but as two formally ordered operations whose relation can still be defended historically if it is presented carefully.

## 2. Name and basic formulation

- **change_ids:** `SC026`; `SC027`
- **display_names:** `NWGmc Nasal Spirant Lengthening`; `NWGmc Nasal Spirant Loss`
- **rule_names:** `NWGmcNasalSpirantLengthening`; `NWGmcNasalSpirantLoss`
- **current_orders:** `26`; `27`
- **cards:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC026-nwgmc-nasal-spirant-lengthening.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC027-nwgmc-nasal-spirant-loss.md`

Short formulation: CAPR currently treats the corridor as a two-stage handling of vowel + nasal + voiceless-fricative environments. `SC026` adjusts the vowel while the conditioning string is still present; `SC027` then deletes the nasal before the spirant. In the literature, however, the standard historical description is usually broader and more bundled: nasal loss before voiceless fricatives with compensatory lengthening and often nasalization of the preceding vowel.

## 3. Traditional description and literature

The literature dossier points in a consistent direction.

Campbell, Fulk, and Sievers-Brunner all give essentially the same core historical claim: in the Ingvaeonic or North Sea Germanic area, nasals before voiceless fricatives disappear and the preceding vowel is lengthened, often with an intermediate nasalized stage. Hogg gives a compact modern statement through the familiar `*ansuz > ōs` type. Ringe and Taylor are especially useful for stage assignment, because they treat the reflexes as part of the broader northern West Germanic developments rather than as an isolated Old English innovation. Luick is the most helpful source for internal refinement, since he distinguishes the general `V + n` before spirant pattern from the special `a`-branch without turning them into separately named laws.

The most important conclusion is negative: **"nasal spirant lengthening" is not the standard handbook name for an independent historical sound law.** The standard tradition usually describes one bundled process. That means later production prose should present CAPR's split as a modeling articulation of a historically unified development, not as two textbook laws that the sources already distinguished in exactly the same way.

## 4. Formal implementation

The FOMA implementation makes the split fully explicit:

```foma
define NWGmcNasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative
];

define NWGmcNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

For book purposes, the key point is not the full line-by-line rule inventory but the logic of the split. CAPR keeps the conditioning environment visible long enough for the vowel effects to apply, and only then removes the nasal. That is stricter and more explicit than most handbook prose, but it is not alien to the handbook tradition either: the traditional descriptions already bundle vowel lengthening, nasalization, and nasal loss into one connected change.

## 5. Place in the cascade

In the current assembled half, SC026-SC027 sits between the early unstressed / boundary-limited material and the glide-fronting entry zone.

1. On the left, `SC025` is nearby but does not currently form part of the same chapter logic.
2. In the middle, `SC026` and `SC027` form an unusually tight local pair.
3. On the right, scaffold `SC028` and the promoted `SC029-SC030` core now open the next seam toward preconsonantal `x` loss and early OE fronting material.

That right-hand neighborhood matters especially for `fist`: the reciprocal failure set is not just about the nasal-loss corridor in the abstract, but about preserving the right input for later developments as the word moves farther down the cascade.

## 6. Order-testing evidence

The chronology evidence is unusually clean.

1. `SC026` cannot move later across `SC027`.
2. `SC027` cannot move earlier across `SC026`.
3. The shared failure set is `fist`, `goose`, and `youth`.

The positive claim is therefore strong: the present model requires `SC026 < SC027`.

Two cautions matter just as much:

1. the earlier side of `SC026` is still runner-limited, so there is no independently established earlier historical left boundary yet;
2. the later side of `SC027` is a no-break-before-boundary result through order 86 and must **not** be rewritten into a claim that `SC027` is historically fixed before `SC087`.

This makes the pair ideal book material. The local reciprocal center is strong, but the book can still model good evidential discipline by refusing to overread the one-sided outer edges.

## 7. Interpretation for the book

If promoted later, this corridor would show how the sound-change half can handle a historically familiar but internally complex development.

The chapter would not say, "the handbooks posit two separate laws called SC026 and SC027." Instead it would say:

1. the historical tradition describes a bundled North Sea Germanic / Ingvaeonic process of nasal loss before voiceless fricatives with compensatory lengthening;
2. CAPR sharpens that bundle into two formal stages;
3. the chronology cards show that, once this modeling choice is made, only one local order works.

That is exactly the kind of explanatory bridge the production layer needs.

## 8. Relation to neighbouring changes

1. **SC025 NWGmc Long E Nasal Rounding** is left-side context only at present. It helps situate the corridor in the early NWGmc run, but the current sources do not require folding it into the same production chapter.
2. **SC028 NWGmc Preconsonantal X Loss** is the most important immediate right-side contextual rule, especially for forms like `fist`, but the chronology evidence for the corridor itself does not require widening the unit yet.
3. **SC029-SC030** belong to the next glide/fronting bridge and should remain background context unless later source work shows a cleaner larger chapter architecture.

So the present best guess is still that SC026-SC027 should remain a paired corridor if promoted, but that decision should stay explicitly provisional.

## 9. Remaining uncertainty

1. The present CAPR name pair is useful, but the production report will need a more book-facing historical label.
2. The literature is stronger for the bundled process than for the exact two-rule split.
3. The historical stage label is not perfectly settled: CAPR files the pair as `NWGmc`, while the handbooks often speak more broadly of North Sea Germanic or Ingvaeonic.
4. `fist` is a vivid chronology example, but it is also a multi-stage derivation and should not be presented as if this corridor alone explains the whole OE outcome.
5. A final human decision is still needed on whether the eventual production report should stay exactly paired or widen slightly to include adjacent explanatory context.

## 10. Proposed book-section outline

1. **The North Sea Germanic nasal-loss corridor**
2. **Traditional handbook description: one bundled process**
3. **Why CAPR splits the process into SC026 and SC027**
4. **Formal implementation and the preserved conditioning environment**
5. **Why `SC026 < SC027` is a real local requirement**
6. **What `fist`, `goose`, and `youth` show**
7. **How far the chronology cards can be read, and where they must stop**
8. **Relation to the neighboring `x`-loss and fronting material**
9. **Terminological and stage-label cautions**
