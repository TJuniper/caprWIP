# Research memo — 2326 you / ēow

## Starting point

- **ID:** 2326
- **CONCEPT:** you
- **COUNTERPART:** ēow
- **PROTO:** *ízwiz
- **PROTOFORM:** *ízwiz
- **DERIVATION_CLASS:** regular
- **NOTE:** Second-person plural pronoun, dat.(-acc.) pl. PGmc *izwiz (Goth. izwis) > *iwwi by coronal-w assimilation (SC008; Stiles 1985-6; R/T 2014: 41-42; Fulk §8.3 pp.204-205) > PWGmc *iuw with apocope in unstressed words (SC098, R/T 2014: 57-58): the absence of i-umlaut proves the *-i fell before umlaut. Geminate-w vocalization is PWGmc (*fewwar > *feuwar), so SC033 precedes degemination (SC031). WS ēow beside eWS/Nb īow: Campbell §702 p.283 note. Chronology witness: SC008 must precede rhotacism (SC003) — rhotacized *irwiz could never yield ēow.

This row was added in the corpus-maturation-01 pass (post-legacy-380). It is
the corpus's principal chronology witness: a basic-vocabulary item whose
derivation is only obtainable if SC008 precedes rhotacism (SC003) and if
SC033 precedes degemination (SC031). Full selection research:
`Germanic/docs/sound_changes/audits/corpus-maturation-01-candidate-adjudication.md` §2
and the SC098 dossier
`Germanic/docs/sound_changes/audits/sc098-dossier-early-apocope-unstressed-words.md`.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the compact derivation trace
`*ízwiz -> íwwiz -> íwwi -> íww -> ēoww -> ēow` (SC008, SC020, SC098, SC033,
SC031); the SC098 dossier; the adjudication note.

**Useful background:** Stiles's demonstration that the *zw > *ww coronal
assimilation is Northwest Germanic and feeds the West Germanic pronoun forms
[@Stiles1985]; Ringe & Taylor on *izwiz > *iwwi [@RingeTaylor2014,
pp. 41-42] and on early apocope in unstressed words with the doublet
*iuwi ~ *iuw [@RingeTaylor2014, pp. 57-58]; Fulk §8.3 [@Fulk2018,
pp. 204-205] on the 2pl pronoun; Campbell §702 [@Campbell1959, p. 283 note]
on WS ēow beside eWS/Nb īow.

**Stale or superseded:** none; the row and rule SC098 were authored together
in this pass.

## Reconstruction and early-stage forms

1. **Cognate-set proto:** PGmc dat.(-acc.) pl. *izwiz (Goth. izwis)
   [@RingeTaylor2014, pp. 41-42; @Fulk2018, §8.3 pp. 204-205].
2. **Project input form:** `*ízwiz` in project transcription.
3. **OE target form:** attested WS ēow, the dative-accusative plural that
   became the sole English 2pl object form and eventually the English word
   *you*.

Derivation, with the rule each step witnesses:

- *ízwiz > *íwwiz — coronal-w assimilation *zw > *ww (SC008)
  [@Stiles1985; @RingeTaylor2014, pp. 41-42].
- *íwwiz > *íwwi — unstressed word-final *-z loss (SC020).
- *íwwi > *íww — early apocope in unstressed (procliticizable) words
  (SC098) [@RingeTaylor2014, pp. 57-58]. The absence of i-umlaut in OE ēow
  proves the final *-i fell before umlaut; SC098 is an exceptionless
  prosodically conditioned law, with the attested doublet *iuwi ~ *iuw
  reflecting regular sentence sandhi.
- *íww > *ēoww — glide vocalization/diphthongization before geminate w
  (SC033); the parallel *fewwar > *feuwar shows this is PWGmc, so SC033
  precedes degemination.
- *ēoww > *ēow — geminate-w simplification (SC031). WS ēow beside eWS/Nb
  īow [@Campbell1959, §702 p. 283 note].

**Chronology consequences (the reason this row exists):**

- **SC008 → SC003:** rhotacized *irwiz could never yield ēow, so coronal-w
  assimilation must precede rhotacism. This edge is now lexically witnessed,
  not merely literature-supported.
- **SC020 → SC098:** apocope applies to the *-i exposed by final-z loss.
- **SC098 → SC055:** the apocopated form must exist before i-umlaut, or OE
  would show umlaut.
- **SC033 → SC031:** vocalization must see the geminate before it
  simplifies.

These are encoded in `historical_partial_order.tsv` and enforced by
`test_corpus_maturation_01.py`.

## Old English philology

WS ēow is the ordinary dat.-acc. 2pl pronoun [@ClarkHall1960;
@BosworthToller1898]. Selecting the dat.(-acc.) plural cell is lexically
motivated: it is the cell that survives into English as *you*; the
nominative gē continues a different stem shape.

## Project value

- First corpus witness for SC098 (new rule, dossier-backed).
- Adds you to the SC008 witness set (previously only four).
- Converts four ordering relations from literature-only to lexically
  witnessed status.

## Paradigm probe

Not required. The 2pl dat.-acc. cell is independently motivated, and the
contrasting cells (nom. gē < *jūz type) belong to a different stem.

## Recommended final report

A focused final report centred on the chronology payload: the five-rule
derivation, the SC008 → SC003 bleeding argument, and the SC098
apocope-before-umlaut argument.

## Data-change recommendations

- **TSV PROTO / PROTOFORM / COUNTERPART / DERIVATION_CLASS / NOTE:** no
  change recommended; the row was authored in this pass from the adjudicated
  sources.
- **`oe_known_problems.tsv`:** no change recommended.
