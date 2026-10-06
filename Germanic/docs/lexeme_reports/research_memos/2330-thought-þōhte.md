# Research memo — 2330 thought / þōhte

## Starting point

- **ID:** 2330
- **CONCEPT:** thought
- **COUNTERPART:** þōhte
- **PROTO:** *θánxtē
- **PROTOFORM:** *θánxtē
- **DERIVATION_CLASS:** regular

This row was added during the nasal-vowel adjudication to supply the one
unwitnessed branch of that complex. The full selection research is in
`Germanic/docs/sound_changes/audits/sc025-sc104-nasalized-low-vowel-adjudication.md`
§12. This memo records the lexeme-level evidence behind it.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the compact derivation trace
`*θánxtē -> þōhte` with exactly two firing stages; Ringe's principal parts
[@Ringe2017, p. 281]; Fulk's statement of the Anglo-Frisian rounding, which
names this very form [@Fulk2018, §4.1, p. 55].

**Useful background:** Ringe's second, independent reconstruction of the same
preterite stem among the past participles showing pre-\*t devoicing
[@Ringe2017, p. 136]; the dictionaries for the paradigm [@ClarkHall1960;
@BosworthToller1898].

**Stale or superseded:** any statement that the low-vowel branch of the nasal
loss is witnessed only by the handbooks, and any statement that `fist` is the
only corpus witness of that rule.

## Reconstruction and early-stage forms

1. **Cognate-set proto:** PGmc \*þankijaną, \*þanhtē, \*þanhtaz 'think', with
   Go. þagkjan, þāhta; ON þekkja, þátti; OHG denken, dāhta, gidāht
   [@Ringe2017, p. 281]. The preterite stem is reconstructed a second time,
   independently, at [@Ringe2017, p. 136].
2. **Project input form:** `*θánxtē`. The dental fricative is written `θ`, the
   Proto-Germanic voiceless dorsal fricative is written `*x`, and the acute
   marks primary stress, exactly as in the existing `*θánkijaną` (think) and
   `*fúnxstiz` (fist).
3. **OE target form:** attested West Saxon *þōhte*, the preterite singular of
   *þenċan*.

The reconstruction is entered with the nasal intact because Ringe reconstructs
it that way in both passages. The nasal loss, the compensatory lengthening and
the nasalization are therefore derived by the cascade rather than assumed.

## Old English philology

*Þōhte* is the ordinary preterite singular of *þenċan* 'think' and is not in
doubt [@ClarkHall1960; @BosworthToller1898]. It is entered as a row separate
from the present stem `think` \*θánkijaną because the two stems have different
vowel histories and only the preterite passes through the nasal complex. Fulk
cites *þōhte* beside OFris. *thochte* as the paired Anglo-Frisian evidence that
the rounding is shared with Frisian and that its output did not merge with
inherited long \*ā [@Fulk2018, §4.1, p. 55].

## Project value

- Supplies the first corpus witness for the low-vowel branch of the nasal loss
  before the dorsal fricative; the previous sole witness, `fist` \*fúnxstiz,
  has \*u and never reaches the rounding rule at all.
- Demonstrates the feeding of the rounding rule by the nasal loss on an
  attested word, which allowed that ordering to be promoted from stage
  entailment to an independently demonstrated relation.
- Is a cleaner diagnostic than `fist`: the dorsal fricative survives to the
  surface as orthographic *h*, so the trace is not confounded with the later
  preconsonantal loss of that fricative, and the only vowel history in the word
  is the nasal loss followed by the rounding.
- Shows that the Ingvaeonic nasal-spirant law correctly does not apply, since
  the dorsal fricative is not one of the spirants that law governs.

## Paradigm probe

Relevant and deliberately used. The present stem of the same verb is already in
the corpus as `think` \*θánkijaną and shows none of this history; the preterite
cell is the one that carries it. The pairing is the point of the row rather
than an accident of cell selection.

## Recommended final report

A short final report is sufficient: a two-rule derivation, the paired
present-stem row, the three diagnostic non-firings, and the ordering it
demonstrates.

## Data-change recommendations

- **TSV PROTO / PROTOFORM / COUNTERPART / DERIVATION_CLASS / NOTE:** no change
  recommended; the row was authored from the adjudicated sources.
- **`oe_known_problems.tsv`:** no change recommended.
- **Recorded for a later pass:** the Proto-Germanic input filter is an
  enumerative cluster whitelist, and admitting this row required adding its
  coda cluster by hand. A form whose cluster is absent is rejected silently at
  the input boundary. This is logged in the adjudication memo as infrastructure
  debt.
