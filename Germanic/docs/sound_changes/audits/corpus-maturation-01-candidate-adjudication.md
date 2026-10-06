# Corpus-maturation pass 01: candidate adjudication (WHO, YOU, HE, GALLOWS)

Branch `sc001-sc020-chronology-audit`. Scope: **Old English pipeline only**.

This memo adjudicates the four candidate lexical items of the first
deliberately limited corpus-maturation pass. It was written **before** any
corpus, FST, registry, or baseline artifact was changed, per the standing
governance rules:

1. no sound-change rule is added or modified without explicit secondary-source
   backing recorded in a new or modified dossier;
2. every proposed rule change must be **both** computationally correct
   (sandbox compile + full-corpus regression) **and** explicitly source-backed.

Guiding principle (author instruction): add words because they materially
improve CAPR as a model of English historical phonology — especially by
supplying real witnesses for otherwise unwitnessed sound changes or lexical
evidence that constrains relative chronology. Do not add artificial fixtures
merely to make rule counters non-zero.

Baseline policy: the existing 380-row corpus is a **frozen legacy subset**.
Its fingerprint
`a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc`
remains the invariant for that subset; the expanded corpus receives a new,
separately reported fingerprint.

---

## 1. WHO — OE *hwā* — verdict: **INCLUDE**

- **Lexical item / cell:** OE *hwā* 'who?', nom. sg. masc. of the
  interrogative pronoun; the direct ancestor of English *who*.
- **Selected reconstruction:** PGmc \*hwaz (corpus notation `*xwáz`).
- **Primary account (adopted):** Ringe & Taylor derive it through the later
  northern West Germanic loss of word-final \*-z in stressed monosyllables
  with compensatory lengthening: "PGmc \*hwaz 'who?' (Goth. ƕas) > PWGmc
  \*hwaz > OE, OF hwā; OS hwē, OHG wer" [@RingeTaylor2014, p. 86]. This is
  exactly the change implemented as SC097 `MonosyllabicFinalZLoss`
  (Dossier C of the three-rule programme). R&T explicitly reject Luick's
  unstressed-variant explanation for this class because it "does not account
  for OE mā and cū" [@RingeTaylor2014, p. 86].
- **Alternative account (recorded, not adopted):** Campbell treats OE *hwā*
  as the unaccented form \*hwa with "later lengthening by transference to
  stressed position" [@Campbell1959, §125, p. 49]; Brunner likewise
  ("Vielleicht ist auch ae. hwā ... durch nachträgliche Dehnung zu erklären")
  [@SieversBrunner1965, §137 Anm. 1, p. 129] and treats the whole *hē/wē/mē/hwā*
  class as generalization of unstressed z-less variants
  [@SieversBrunner1965, §182, p. 160]. CAPR adopts the R&T account, consistent with
  the accepted SC097 adjudication; the disagreement is recorded in the
  lexical entry.
- **Decisive shared datum:** on **either** account the vowel of *hwā* is
  never fronted. Campbell is explicit: "In the case of hwā, the form with
  West Gmc. lengthening (OE \*hwǣ) does not exist" [@Campbell1959, §125,
  p. 49]; Brunner: "doch kommen daneben keine Formen mit æ, ē vor"
  [@SieversBrunner1965, §137 Anm. 1, p. 129]; R&T print *hwā* directly
  [@RingeTaylor2014, p. 86].
- **Rules witnessed:** SC097 (first genuine corpus witness; currently
  synthetic-only).
- **Ordering constrained:** none new (SC097's position was fixed in the
  accepted three-rule adjudication).
- **Rule change required:** the current cascade wrongly yields *hwǣ* because
  the long-final clause of SC043 (`EAFBrighteningLongFinal`,
  `{*ā} -> {*ǣ} || _ .#.`) over-applies to this monosyllable. That clause
  was introduced solely for the surviving-bimoric pathway — unstressed final
  \*-ā of polysyllables from \*-ō [@RingeTaylor2014, §3.1 pp. 58–59; §6.8.3
  pp. 299–300] — and its own documentation says so. Narrowing it to
  polysyllables (requiring a preceding nucleus, exactly parallel to the
  guard on `PWGmcSurvivingBimoricOUnrounding`) restores its documented
  historical scope. See the modified SC043 book dossier
  (`book_dossiers/043-anglo-frisian-brightening.book-dossier.md`) for the
  source backing. **Computational validation:** sandbox compile passes;
  `xwáz → hwā`; 0/380 differences against the committed legacy baseline.

## 2. YOU — OE *ēow* — verdict: **INCLUDE**

- **Lexical item / cell:** OE *ēow*, acc./dat. pl. of the second-person
  pronoun (the two cells are fully syncretic in OE); ancestor of English
  *you*. West Saxon *ēow*; early WS and Northumbrian *īow*
  [@Campbell1959, §702, p. 283 note; R&T print *īow*].
- **Selected reconstruction:** PGmc \*izwiz dat. pl. (Goth. *izwis*;
  corpus notation `*ízwiz`).
- **Derivation (adopted, R&T):**
  1. \*izwiz > \*iwwiz — PWGmc assimilation of \*zw (and \*dw) to \*ww:
     "the intervocalic sequences \*zw and \*dw were assimilated to \*ww
     (Stiles 1985–6, NOWELE 6: 89–94) ... PGmc \*izwiz 'you (dat. pl.)'
     (Goth. izwis) > \*iwwi > PWGmc \*iuwi ~ \*iuw (see 3.1.4) > OE īow, OF
     iū, OS, OHG iu" [@RingeTaylor2014, §3.1.1, pp. 41–42]. = SC008
     `PWGmcCoronalWAssimilation`, whose comment already cites this word but
     which no corpus row exercises on the \*zw branch (*four* exercises only
     \*dw). Independently corroborated by Fulk: "In WGmc. ... \*izwiz
     results in \*iuwiz, either by change of \*-zw- to \*-ww- (so first
     Kluge 1908: 65; see Stiles 1985–6 ...)" [@Fulk2018, §8.3, pp. 204–205].
  2. \*iwwiz > \*iwwi — PWGmc loss of word-final \*-z after unstressed
     syllables [@RingeTaylor2014, pp. 44–45] = SC020 (Dossier B), printed by
     R&T already applied in the passage above.
  3. \*iwwi > \*iww — early apocope of the final short high vowel after a
     heavy syllable in an unstressed word: "Short high vowels were also lost
     after heavy syllables in unstressed words ... OE iow 'you (dat. pl.)'
     definitely does [exhibit early apocope] (since it does not exhibit
     i-umlaut)" [@RingeTaylor2014, §3.1.4, pp. 57–58]. **This change is not
     yet in the cascade**; it is added as **SC098** with its own research
     dossier (`audits/sc098-dossier-unstressed-word-final-i-apocope.md`).
  4. \*iww (R&T \*iuw) > OE *ēow* — vocalization of the geminate to a long
     diphthong plus glide, the same development CAPR implements as SC033
     `OEEwLongDiphthong` and which R&T place already in PWGmc (\*fewwar >
     PWGmc \*feuwar; \*iwwi > PWGmc \*iuwi) [@RingeTaylor2014, §3.1.1,
     pp. 41–42]; cf. Campbell on WGmc \*iuu > OE *iow/eow* sequences
     [@Campbell1959, §120.2–3, pp. 44–47]. This requires the word-final
     geminate to be reachable by SC033, i.e. SC033 must apply **before**
     geminate simplification (SC031) — see §2a below.
- **Rules witnessed:** SC008 (\*zw branch, first corpus witness), SC020,
  SC098 (new), SC033.
- **Ordering constrained (the chief value of this item):**
  1. **SC008 → SC003 (rhotacism):** if rhotacism applied first, post-vocalic
     \*z before \*w would give \*irwiz and the assimilation would be bled;
     OE *ēow* (not \*eorw-) is the lexical witness that coronal-w
     assimilation precedes rhotacism. Gains a `historical_partial_order.tsv`
     edge with a corpus witness and a focused regression test.
  2. **SC020 → SC098:** feeding — z-loss exposes the final \*-i that
     apocope then removes.
  3. **SC098 → SC055 (i-umlaut):** bleeding — R&T's own dating argument:
     *ēow* shows no umlaut, so the \*-i was gone before umlaut applied
     [@RingeTaylor2014, pp. 57–58].
  4. **SC033 → SC031:** the geminate \*ww must vocalize before geminate
     simplification, otherwise \*iww would degeminate to \*iw and never
     yield *ēow*; R&T's PWGmc dating of \*feuwar/\*iuwi makes the
     vocalization early relative to OE-era degemination
     [@RingeTaylor2014, pp. 41–42]. See §2a.
- **Rule changes required:**
  1. new SC098 (dossier: `sc098-dossier-unstressed-word-final-i-apocope.md`);
  2. SC033 context extended to word-final geminate (`{*w} .#.`) and SC033
     recomposed before SC031/SC032 (modified book dossier
     `031-034-west-saxon-diphthong-chain.book-dossier.md`).
  **Computational validation:** sandbox compile passes; `ízwiz → ēow`;
  `fédwōr → fēower` unchanged; 0/380 differences against the committed
  legacy baseline; the reorder lies inside the recorded safe computational
  windows of SC031 (`14–33`) and SC033 (`14–43`), and
  `historical_partial_order.tsv` contains no SC031/SC032/SC033 edges.

### 2a. SC033-before-SC031 reorder (historical correction, output-neutral)

Current manifest order is SC031 `OEWWSimplification` (31) → SC032
`OEDiphthongLeveling` (32) → SC033 `OEEwLongDiphthong` (33). R&T date the
geminate-w vocalization to PWGmc itself (\*fewwar > PWGmc \*feuwar; \*iwwi >
PWGmc \*iuwi ~ \*iuw) [@RingeTaylor2014, §3.1.1, pp. 41–42], while general
degemination of residual \*ww belongs to the OE-era cleanup. The historically
correct relative order is therefore vocalization (SC033) before degemination
(SC031). The current inverted order was undetectable because no corpus row
had a word-final geminate: for every existing row the two orders are
output-equivalent (proven: 0/380 regression differences). *ēow* makes the
order empirically visible for the first time. This is a genuine historical
correction, not ad hoc scoping.

## 3. HE — OE *hē* — verdict: **OMIT this pass** (author may revisit)

- **Candidate reconstruction:** PGmc \*hiz > PWGmc \*hiz > OE *hē*
  [@RingeTaylor2014, p. 86].
- **Why omitted:**
  1. R&T themselves flag the analysis as non-unique: "This is the simplest
     formulation for OE, in which \*-iz always appears as -ē, though
     levelling of the alternation in the pronoun \*hi- ~ \*he- cannot be
     absolutely excluded as a source of nom. sg. masc. hē"
     [@RingeTaylor2014, p. 86 n. 24].
  2. On the sound-law reading, \*hiz > \*hī (SC097) requires a further
     OE-specific lowering of lengthened \*ī to *ē* (the *wē, gē, mē, þē,
     hē* class) that is **not modeled** in the cascade; the live cascade
     yields *hī*. Adding a new rule whose only corpus witness is a form R&T
     themselves consider two-ways ambiguous is exactly the forcing this
     pass prohibits.
  3. SC097's coverage need is already met by WHO, whose derivation is
     clean and unambiguous.
- Brunner's alternative (generalized unstressed variant, §182, p. 160)
  applies to this class too, reinforcing the ambiguity. Recorded as
  author-decision / future work; if the \*-iz > -ē lowering class (with
  *wē/gē/mē/þē* support) is ever added on its own dossier, HE becomes a
  natural second SC097 witness.

## 4. GALLOWS — early Northumbrian *galgu* — verdict: **EXCLUDE**

- **Candidate:** acc. sg. masc. *galgu* (Ruthwell Cross, RuthCr 40) as a
  witness for SC021 `PNWGmcUnstressedORaising` (\*-onų > \*-unų).
- **Why excluded:**
  1. R&T list *galgu* among "very few" n-stem u-vowel relics but immediately
     hedge: "masc. acc. galgu is not necessarily relevant; we must reckon
     with the possibility that its -u is connected with the usual OHG masc.
     acc. sg. ending -un ~ -on (Bammesberger 1990: 169)"
     [@RingeTaylor2014, pp. 62–63].
  2. On the sound-law side R&T describe the \*-onų > \*-unų raising
     hypothesis as making "phonetic sense; but ... too small a basis"
     [@RingeTaylor2014, p. 63].
  3. Weighing the alternatives for these n-stem forms, R&T conclude:
     "A decisive choice between those alternatives does not seem possible"
     and "I know of no proposal that solves all the problems convincingly"
     [@RingeTaylor2014, p. 164].
  4. The form is also a dialectally marked inflected relic (early
     Northumbrian, single attestation), not a natural corpus cell for the
     English lexical item *gallows*.
- **Consequence:** SC021 remains unwitnessed with coverage status
  `disputed_or_research_issue`; the reader-facing chapter
  (`021-unstressed-o-raising.md`) already documents the zero-firing status
  and gains a pointer to this adjudication.

## 5. Cross-cutting notes

1. **Not already represented:** grep of CONCEPT/COUNTERPART confirms no
   existing corpus row for *who*, *you*, *he*, or *gallows* under any cell.
2. **Chronology-witness principle (recorded for future passes):** YOU is a
   model case of an ordinary basic-vocabulary item that makes an otherwise
   metadata-only order relation (SC008 → SC003) empirically visible in the
   corpus. Future corpus maturation should prioritize such items.
3. **Coverage census:** this pass introduces a machine-readable rule-coverage
   census with statuses `witnessed / synthetic_only / historically_obscured /
   disputed_or_research_issue`. After implementation SC097 becomes
   `witnessed` (WHO); SC021 stays `disputed_or_research_issue` (GALLOWS
   excluded); SC008's \*zw branch becomes corpus-witnessed (YOU).
4. **Implementation order:** WHO first (single-clause SC043 narrowing), then
   YOU (SC098 + SC033 changes), each with smallest-trace-first validation,
   focused regression tests, then the full suite and book gates.
