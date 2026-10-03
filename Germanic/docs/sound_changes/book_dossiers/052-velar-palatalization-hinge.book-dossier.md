# SC052: Velar Palatalization Hinge

## 1. Role in the book

`SC052` is the next mature unresolved palatalization-side candidate after the
promotion of `SC051`. It now sits between a left-edge feeder (`SC050`) and the
already promoted `SC055-SC056` umlaut core, making it one of the clearest
remaining hinge units in the sound-change half.

That does not mean the chapter shape is settled. The real question is whether
the book eventually wants:

1. a standalone `SC052` hinge report; or
2. a narrower `SC050-SC052` paired report.

## 2. Name and basic formulation

- **main change_id:** `SC052`
- **display_name:** `OE Velar Palatalization`
- **rule_name:** `OEVelarPalatalization`
- **current_order:** `52`
- **contextual left change:** `SC050` **Sievers Law Syncope** (`SieversLawSyncope`, order `50`)
- **contextual right change:** `SC055` **OE I Umlaut** (`OEIUmlaut`, order `55`)
- **related later question:** `SC057` **OE J Cluster Coalescence** (`OEJClusterCoalescence`, order `57`)
- **cards:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC050-sievers-law-syncope.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC052-oe-velar-palatalization.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC055-oe-i-umlaut.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC057-oe-j-cluster-coalescence.md`

Working formulation: `SC052` isolates the Old English palatalization of plain
velars `k/g` in the front-vocalic and `j`-adjacent environments that CAPR tests
locally. It is close to, but not the same as, the already promoted `SC051`
`sk`-palatalization rule.

## 3. Traditional description and literature

The literature dossier supports a stable middle position.

The standard grammars all support plain velar palatalization as a real Old
English development. They also keep it close to the wider palatalization zone
that includes `sk`-palatalization, while treating i-umlaut as a later and
larger vowel chapter. That is the strongest argument for `SC052` as a hinge:
the process is historically real and chapter-capable, but it lives between two
already promoted neighbors rather than replacing either of them.

The weakest source support concerns `SC050`. Specialist Sievers-law work shows
why the left-edge feeder is real, but it does not naturally turn Sievers-law
syncope into the same historical chapter as velar palatalization. So the live
question is mainly chapter architecture, not process reality.

## 4. Formal implementation

In CAPR, `OEVelarPalatalization` is a targeted consonant rule.

1. `*k` becomes palatal before front vowels, before `*j`, and in a few
   front-vowel-adjacent positions that preserve the modeled contrast.
2. `*g` likewise becomes palatal before front vowels, after front vowels at
   certain edges, and before `*j`.

`SC050` matters here only as feeder/context unless the chapter is later paired:
`SieversLawSyncope` deletes `*i` before `*j` after a consonantal environment,
which is exactly why the `stretch` relation is visible at all.

## 5. Place in the cascade

`SC052` sits in a structurally rich position.

1. It follows `SC050` **Sievers Law Syncope**.
2. It also follows the already promoted `SC051` **OE Sk Palatalization** in the assembled order.
3. It precedes the `SC053-SC054` pre-umlaut bridge.
4. It precedes the already promoted `SC055-SC056` **umlaut-core** report.
5. `SC057` remains a later unresolved palatalization-side question downstream.

This makes `SC052` more naturally a hinge chapter than a residual placeholder.

## 6. Order-testing evidence

The local network is stronger than ordinary scaffold material.

1. `SC050`'s later boundary is across `SC052`, with `stretch`.
2. `SC052`'s earlier boundary is across `SC050`, also with `stretch`.
3. `SC052`'s later boundary is across `SC055`, with `cow` and `lung`.
4. `SC050`'s earlier side is runner-limited and not a positive historical boundary.

So the real evidence is asymmetric but meaningful: `SC052` itself is anchored on
both sides, while `SC050` is only locally strong on the right.

## 7. Interpretation for the book

`SC052` is probably stronger than a residual scaffold.

The main uncertainty is not whether plain velar palatalization is real. It is
whether the book should present that reality as a standalone hinge chapter or as
part of a narrower `SC050-SC052` pair.

Whatever shape is chosen later, the report should avoid duplication in both
directions:

1. it should not repeat the already promoted `SC051` singleton as if all
   palatalization were one chapter;
2. it should not rewrite the already promoted `SC055-SC056` report as if the
   umlaut core were merely a continuation of `SC052`.

## 8. Relation to neighbouring changes

1. **SC050 Sievers Law Syncope** is the possible left feeder and the only serious candidate for a paired left edge.
2. **SC051 OE Sk Palatalization** is the already promoted neighboring palatalization singleton.
3. **SC055-SC056 Umlaut core** is the already promoted right context.
4. **SC057 OE J Cluster Coalescence** remains later unresolved palatalization-side material.

## 9. Remaining uncertainty

1. Standalone `SC052` versus a later `SC050-SC052` pair.
2. The role of `SC057` in any future palatalization-side architecture.
3. How much narrative weight the single `stretch` feeder witness should bear.
4. The risk of duplicating the promoted `SC051` report.
5. The risk of duplicating the promoted umlaut-core report.

## 10. Proposed book-section outline

1. **If promoted later as standalone `SC052`**
   1. Why plain velar palatalization deserves its own hinge chapter
   2. How it relates to but differs from `SC051`
   3. `SC050 < SC052 < SC055`
   4. Why the right edge matters for the umlaut core
   5. What remains unresolved with `SC057`
2. **If promoted later as `SC050-SC052`**
   1. A left-edge feeder and a palatalization hinge
   2. What `stretch` actually proves
   3. Why the pair still centers on `SC052`
   4. How the pair leads into the promoted umlaut core
   5. Why the chapter must still avoid duplicating `SC051`

## 11. P component specification: class, cutoff and representation

### Identity and falsifiable question

SOURCE-only research packet, 2026-10-03, branch `update`, base `67a18cfb`.
`--prepare` routes SC052 here; canonical OE/English-specific metadata and
the incumbent rule remain unchanged. The comparative authority is the
Anglo-Frisian synthesis §8.6. No canonical verdict is asserted.

Question: can the current k/g marker bundle distinguish productive initial
cutoff, fricative articulation/merger and stop-class assibilation? Confirmation
requires source-matched original-front positives, mutation-created negatives,
and separately staged fricative/stop inputs. A dotted spelling or common
`ʤ` output cannot confirm phonetic identity. Key/day remains a potentially
contradictory pair rather than an exception to suppress.

### Current state: literal incumbent components

For every clause below `FV = EnglishStarFrontVowel`. The source actually
contains two networks and separately composed k/g blocks, not one parallel
replacement rule. Stress-marked i is separately admitted as ḯ.

| Component | Literal incumbent condition/output | Source target / disposition |
|---|---|---|
| Initial k | `k -> ʧ || .#. _ FV` | Original qualifying front vowel/j history; **RETAIN control**, prefer cutoff before mutation; **DEFER any revised cutoff/date**. |
| Noninitial k | `k -> ʧ || _ [i\|ī]` and `_ ḯ`; `[i\|ī] _ FV` and `ḯ _ FV`; `[i\|ī] _ .#.` and `ḯ _ .#.` | Position-specific eligibility, not “all k adjacent to a front vowel”; **RETAIN**. |
| kk/j interface | `k k -> ʧ ʧ || _ j`, then `k -> ʧ || _ j` | Deterministic feeding handling; **RETAIN**, independent of a phonetic assibilation date. |
| g before front | `g -> ʤ || _ FV`; `g -> ʤ || FV _ FV` | Current before-any-front clause is broader than Ringe–Taylor's noninitial before-i/ī statement; **RETAIN control / DEFER class/context restriction**. |
| g after front | `g -> ʤ || FV _ .#.`; `g -> ʤ || FV _ [EnglishStarConsonant - j]` | Word-final/preconsonantal front conditioning, with j separate; **RETAIN control**, not proof of fricative-to-j merger. |
| gg/j interface | `g g -> ʤ ʤ || _ j`, then `g -> ʤ || _ j` | Geminate stop-class trigger pathway; **RETAIN deterministic control / DEFER historical marker split**. |
| ng | No separate ng rule: the g clauses operate on any matching g, including after n | Postnasal stop identity must be explicit; **DEFER independent ng conditioner/marker proposal**. |

The literal `FV` helper includes non-high vowels, stressed equivalents,
rounded front vowels and front-initial diphthongs. There is no provenance
tag saying “original front” versus “mutation-created front”; current
serialization supplies the productive cutoff. The output symbols ʧ/ʤ
collapse stages of articulation and later reflex representation. `g` at
this point is not a reliable declaration that every input is a voiced stop:
fricative allophony and geminate/postnasal stops require an input audit.

### Diagnosis: complete current firing census

The fresh serial `SC052 --evidence` run on 2026-10-03 rebuilt container
bins and checked equivalence over all 387 selected runnable rows.
SC052 changes **32/387**: **7 k rows**, **25 g rows**, disjoint here.
All thirty-two are also legacy-380 members; the 7/25 partition is unchanged.

```text
k (7): 1969 breeches; 1975 calf; 1976 chew; 1996 drench; 2171 seek;
2226 stretch; 2248 think.
g (25): 1943 begin; 1944 believe; 1945 belly; 1961 bow (verb);
1985 day; 2027 follow; 2037 gall; 2040 gift; 2041 give; 2049 guest;
2050 hail; 2069 hedge; 2079 honey; 2130 nail; 2147 rain;
2148 rainbow; 2163 rye; 2164 sail; 2191 singe; 2228 string;
2243 thane; 2267 wain; 2277 way; 2296 withy; 2305 yarn.
```

These are complete applications of the executable symbols, not a source-
validated census of distinct phonetic classes. All changed rows need
class/input review before a proposed restriction; none is declared a
new historical exception on the strength of this list.

| Stable witness | Actual local observation | Role / caveat |
|---|---|---|
| day1985 | `*dæg > *dæʤ` | Live marker change; nominative is not Hogg's dative/oblique fixture. |
| gift2040 | `*géfti > *ʤéfti` | Live initial marker; selected e is an early-raising input problem, not PD chronology. |
| stretch2226 | `*strækkjąn > *stræʧʧjąn` | Live deterministic geminate/j feeding; assert one result, not kʧj/ʧʧj ambiguity. |
| singe2191 | `*sángjąn > *sánʤjąn` | Live postnasal/g+j class; no fricative-to-j inference. |
| lung2114 | `*lúngannju` unchanged | Negative current palatalization; mutation downstream is a different operation. |
| cow1980 | Selected dative input `*kūi` has no initial front vowel | Negative cutoff control; not a diphthong-mutation witness. |

### Literature and historical analysis

Ringe–Taylor provide four position-specific conditions: initial k/g before
front vowels; noninitial before i/ī; intervocalic g between fronts but k
only with preceding i/ī; final/preconsonantal g after fronts but final k only
after i/ī. They separately describe initial palatal stops, later affrication,
fricative g, gg and ng [@RingeTaylor2014, pp. 203–204].
Their medial-g before-any-front mismatch with CAPR is real specification
residue, not authorization to impose a new rule from a table.

Verified Luick gives original-front versus mutation-created initial
conditioning, positional examples and a distinct chronology note
[@Luick1914, pp. 835–841, §637, especially pp. 836–838 and p. 841 n. 8].
His common-stem assignment is his historical proposal, not a stage inferred
from an FST prefix. Laker separates k, fricative g and gg/ng histories
[@Laker2007, pp. 167–168, 175–184]. These support a class inventory,
not a single inherited-palatalization adoption.

Hogg's unrounded key dative is stronger productive-cutoff evidence than
rounded kyn: a rounded result alone can bound cutoff before unrounding
rather than before mutation [@Hogg1979, pp. 100–103;
@Laker2007, pp. 167–168]. But day dative retains æ where new medial
j would cause mutation if already equivalent to inherited j.
Hogg discusses delayed merger and separate positional chronologies without
resolving the contradiction [@Hogg1979, pp. 102–110].
Ringe–Taylor's later merger account [@RingeTaylor2014, p. 204] is a
source-backed competing solution, not permission to present Hogg as
having endorsed it. **DEFER effective-new-j merger/cutoff reconciliation.**

SC045 has no live ɣ input firings in the fresh census; its x changes do not
validate this g history. SC057 gj/kj coalescence is a distinct inherited
cluster process, not the missing fricative merger. SC016/017's settled
orthographic boundary must not be reopened for marker convenience.

### Exact assays and recommendations

Exact production proposal: **none**. RETAIN incumbent k/g and deterministic
geminate interfaces as the baseline; DEFER class-specific production
decomposition, especially fricative/new-j trigger equivalence and ng.
No global inherited-palatalization conclusion or new canonical edge follows.

Required assays before a production recommendation:

1. Initial original-front positive (reuse calf1975/chew1976, keeping
   breaking/inherited-diphthong inputs explicit) versus cow1980,
   lung2114 and source key dative negative. Key is a source fixture,
   not a new approved corpus row; audit exact unrounded target/cell.
2. Day1985 nominative control plus source daege oblique fixture:
   compare inherited-j positive mutation against new medial-palatal
   nontrigger. Record both mutation and merger checkpoints. Do not
   manufacture a delayed-merger answer merely to pass the pair.
3. Geminate stop wicg fixture versus fricative daeg/segl fixtures;
   source-backed ng positive and back-vowel/postnasal negative.
   Verify allophony, selected stage and paradigm cells before compiling.
4. Stretch2226 must retain one deterministic kk/j result; seek2171
   and singe2191 must preserve intended cluster inputs. Plain singleton
   and inherited-j negatives must not enter SC057 accidentally.
5. Any new marker requires alphabet, consonant/vowel helper, mutation
   intervener, weight/reduction, cleanup, orthographic and API-no-leakage
   checks before a 387-row old/new comparison. A glyph match is not
   a phonetic identity assertion.

Approval is separate for each changed class/condition, event identity,
stage/scope/edge, selected input and representation interface. No corpus
addition is approved. Parent owns regeneration and reader synchronization.
Remaining uncertainty is exact class eligibility and timing, not whether
OE palatalization occurred; this packet does not promise its resolution.
