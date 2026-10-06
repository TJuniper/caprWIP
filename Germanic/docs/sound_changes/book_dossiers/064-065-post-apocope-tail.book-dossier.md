# SC064-SC065: Post-apocope Tail

## 1. Role in the book

`SC064-SC065` is the clearest remaining short candidate immediately after the
promoted `SC063` **High-vowel apocope** chapter. It tests whether a weakly
evidenced two-change bridge can later become a cautious report, or whether the
current pair is mainly a useful scaffold between the apocope chapter and the
already promoted `SC066-SC068` **Syncope and degemination corridor**.

That makes the dossier valuable even without promotion. The question is not
simply whether both rules are historically plausible; it is whether they form a
chapter together.

## 2. Name and basic formulation

- **change_ids:** `SC064`; `SC065`
- **display_names:** `NWGmc In Stem N Loss`; `OE Medial Syncope`
- **rule_names:** `NWGmcInStemNLoss`; `OEMedialSyncope`
- **current_orders:** `64`; `65`
- **cards:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC064-nwgmc-in-stem-n-loss.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC065-oe-medial-syncope.md`

Working formulation: CAPR currently treats the unit as the immediate
post-apocope tail. `SC064` removes stem-final `*n` after `*ī` in the narrow
`fright`-type environment that yields OE `fyrhte`, while `SC065` deletes a
medial `*i` in a narrow pre-dental environment after a heavy syllable. The pair
therefore combines one very narrow lexical bridge rule with one broader but
currently card-negative syncope rule.

## 3. Traditional description and literature

The literature dossier points to an uneven but still meaningful result.

The standard grammars strongly support the **broader late weak-tail setting**:
after the main apocope material, Old English and related West Germanic history
still shows medial-vowel loss, cluster pressure, and further tail cleanup
[@Campbell1959, §§345--349, 388--389; @HoggPhonology1992, p. 121;
@RingeTaylor2014, §§6.7.3--6.8.4; @Luick1914, §§304--306; @Fulk2018, §5.6].

What they do **not** strongly support is a chapter-sized traditional pair
consisting exactly of `SC064` plus `SC065`. `SC064` looks more like a narrow
lexical bridge than a standard grammar headline, and the best direct source
support for it comes from the inherited `*furht-*` family behind `fright`
[@Kroonen2013, p. 201]. `SC065` maps more naturally onto broad grammar
discussions of medial syncope, but CAPR's actual rule is narrower than the
handbook category, and its chronology card is still fully negative.

## 4. Formal implementation

Both CAPR rules are concise, but they are not equally book-facing.

1. `NWGmcInStemNLoss` deletes stem-final `*n` after `*ī` in the narrow environment that produces the `fright` / `fyrhte` line.
2. `OEMedialSyncope` deletes medial `*i` before a following dental (`*θ`, `*ð`, `*d`, `*t`) after a heavy syllable.

That means the formal implementation is already more specific than the ordinary
grammar labels. `SC064` is especially narrow and witness-driven. `SC065` is
best understood as one carved-out piece of a larger syncope tradition rather
than as the whole of Old English medial syncope.

## 5. Place in the cascade

This unit belongs in the cascade **after** `SC063` and **before**
`SC066-SC068`.

1. `SC063` provides the decisive apocope event that opens the late weak-tail zone.
2. `SC064-SC065` is the immediate tail after that event.
3. `SC066-SC068` then turns the broader late syncope-and-cleanup corridor into an already promoted chapter.
4. `SC072` remains an important later cross-link because it is the positive later boundary for `SC064`.

This is therefore a bridge position, not a replacement for either neighboring
promoted chapter.

## 6. Order-testing evidence

The order-testing evidence is sharply uneven.

1. `SC064` must follow `SC041` **PWGmc Final Bare A Loss**.
2. `SC064` must precede `SC072` **OE Unstressed Long Vowel Shortening**.
3. Both of those positive boundaries are carried by the same representative failure: `fright`, where shifting the rule yields `fyrhten` instead of expected `fyrhte`.
4. `SC065` has no positive first-break boundary in either direction.
5. The runner-boundary results on the `SC065` card must not be treated as historical constraints.

So the strongest order claim here is not "the pair forms a securely tested
two-rule chapter." It is narrower: `SC064` is a real but highly concentrated
bridge, while `SC065` remains structurally plausible but not positively anchored
by the current card evidence.

## 7. Interpretation for the book

At book level, the unit may prove more useful as a **bridge note** than as a
full chapter.

`SC064` is the stronger member because it has real chronology evidence and a
real inherited witness family behind that evidence. But it is still narrow
enough that a later `SC064`-only note is plausible.

`SC065` is the more traditional sort of handbook phenomenon, since medial
syncope is well established in the sources. Yet in CAPR it currently has no
positive first-break boundary and may end up reading better as residual context
for the already promoted `SC066-SC068` corridor than as a coequal co-headliner.

Source work therefore prepares the unit for human review, not for immediate
promotion.

## 8. Relation to neighbouring changes

1. **SC063 OE High Vowel Apocope** is the immediate promoted left context and remains the main reason this unit exists as a post-apocope tail at all.
2. **SC066-SC068 Syncope and Degemination Corridor** is the immediate promoted right context and remains the likeliest destination for any residual `SC065` narrative material.
3. **SC072 OE Unstressed Long Vowel Shortening** is the key later cross-link for `SC064`.
4. **SC041 PWGmc Final Bare A Loss** is the key earlier positive boundary for `SC064`.

## 9. Remaining uncertainty

1. The main architectural uncertainty is paired report versus `SC064`-only note.
2. `SC065` remains card-negative and cannot yet be treated as a positive chronology anchor.
3. `SC064` relies entirely on the `fright` witness family and therefore cannot yet carry broad historical prose on its own without caution.
4. The relation of `SC065` to the already promoted `SC066-SC068` corridor is still unresolved.
5. `SC064`'s relation to `SC072` is meaningful, but it should not be inflated into a broad chapter-defining network.

## 10. Proposed book-section outline

1. **If promoted later as a cautious paired report**
   1. Post-apocope tail after SC063
   2. Why `SC064` is real but narrow
   3. Medial syncope as the broader historical backdrop for `SC065`
   4. What the cards actually prove
   5. Why the pair remains modest beside SC066-SC068
2. **If narrowed later to `SC064` with `SC065` left residual**
   1. A narrow `fright`-based bridge after apocope
   2. `SC041 < SC064 < SC072`
   3. Why the witness is real but limited
   4. `SC065` as contextual lead-in to later syncope material
   5. Why the main syncope chapter remains SC066-SC068
