# SC049-SC050: Onset Allophony and Sievers-law Bridge

## 1. Role in the book

This unit is a small chronological bridge immediately before the promoted SC051 and SC052 reports. Its main editorial value is architectural: SC049 and SC050 are both ordinary FST changes, so both need explicit prose somewhere in the assembled sound-change half, but neither one should be absorbed into a non-contiguous production unit. At present this looks more like a modest bridge report than a major historical chapter.

## 2. Name and basic formulation

- **SC049:** PGmc B Allophony
  - **FOMA rule:** `PGmcBAllophony`
  - **Current role:** narrow `/b/ ~ [beta]` implementation rule with one live leftward chronology boundary across SC037
- **SC050:** Sievers Law Syncope
  - **FOMA rule:** `SieversLawSyncope`
  - **Current role:** small prosodic/morphophonological bridge whose live positive chronology relation is rightward, into SC052
- **Combined unit label:** Onset Allophony and Sievers-law Bridge
- **Present editorial judgment:** keep together provisionally because the changes are adjacent, but leave open a later split into two very short notes

## 3. Traditional description and literature

The literature does not treat SC049-SC050 as a natural chapter. SC049 is the weaker side. Hogg, Ringe and Taylor, and Luick support the underlying phonological point that OE and earlier West Germanic distinguish stop and fricative realizations of `b` by position [@HoggPhonology1992, p. 108; @RingeTaylor2014, p. 121; @Luick1914, p. 107]. That supports CAPR's rule as a real phonological distribution, but not as a large historical chapter with its own broad chronology. The one live chronology witness, `rainbow`, is therefore doing unusually large local work.

SC050 has stronger source backing. Adamczyk and Fulk both treat Sievers-law reflexes as real historical material visible in weak-verb and related paradigms, especially through heavy/light stem structure and the distribution of gemination [@Adamczyk2001; @Fulk2018, p. 28, sec. 6.15]. That makes SC050 easier to justify in book prose, but its function inside this part of the cascade is still limited: the live chronology card makes it mainly a feeder into SC052 rather than a coequal member of a palatalization chapter.

## 4. Formal implementation

In CAPR terms the two rules are compact and technical.

- **SC049 / `PGmcBAllophony`:** the rule converts `*b` to `*beta` after vowels and liquids, then restores stop `*b` before geminate `*bb`.
- **SC050 / `SieversLawSyncope`:** the rule deletes `*i` before `*j` after a consonant or palatal consonant.

Tiny live-rule excerpts are enough here:

```text
*b -> *beta || [Vowel | Liquid] _ ;
*i -> 0 || [Consonant | PalatalConsonant] _ *j ;
```

Those snippets capture the editorial asymmetry. SC049 reads like phonological surface management, while SC050 reads like a small morphophonological feeder into later palatal material.

## 5. Place in the cascade

SC049-SC050 belongs after the SC046-SC048 scaffold bridge and before the promoted SC051 sk-palatalization report. It also sits before the promoted SC052 velar-palatalization hinge report. The important constraint is chronological order: SC050's relation to SC052 should be handled by explicit cross-reference, not by folding SC050 into a non-contiguous SC050-SC052 chapter.

## 6. Order-testing evidence

- SC049 must follow SC037, with `rainbow`.
- SC049 has no positive later boundary; the later side is runner-bounded and should remain non-positive.
- SC050 must precede SC052, with `stretch`.
- SC050 has no positive earlier boundary; the earlier side is runner-bounded and should remain non-positive.
- There is no internal reciprocal pair here.

The evidence therefore supports adjacency in the assembled book, but not a strong claim that SC049 and SC050 form one tightly unified historical process.

## 7. Interpretation for the book

The most plausible book treatment is a short adjacent bridge report. SC049 is probably allophonic and implementation-heavy, so it likely deserves only brief prose explaining why the model needs it and why the `rainbow` boundary matters. SC050 has stronger traditional literature, but within this local chronological stretch it still functions primarily as a feeder toward SC052. Both changes need explicit prose because they are ordinary FST changes, yet the prose should stay concise and avoid promoting a practical adjacency into a false historical synthesis.

## 8. Relation to neighbouring changes

SC037 supplies the positive left boundary for SC049. SC051 is the immediate promoted right neighbor in the assembled half. SC052 is the already promoted report that SC050 feeds, so SC050 should point forward to it explicitly. The neighbouring reports matter more than any supposed internal SC049-SC050 unity.

## 9. Remaining uncertainty

- bridge report versus two very short notes
- how much weight to give the source tradition for SC049, which looks thinner and more allophonic than chapter-like
- how much Sievers-law background to include for SC050 before the prose starts duplicating SC052
- how to keep the eventual report concise while still giving both ordinary FST changes explicit prose

## 10. Proposed book-section outline

### Option A: short adjacent SC049-SC050 bridge report

1. Why this small bridge sits before SC051-SC052
2. SC049 as narrow `b`-allophony and compound-side implementation
3. SC050 as Sievers-law bridge and feeder into later palatalization
4. Order evidence and cautions
5. Forward cross-reference to SC052

### Option B: two very short notes kept in chronological order

1. SC049 note: allophonic `b` distribution, `rainbow`, and narrow chronology claim
2. SC050 note: Sievers-law reflex background, `stretch`, and forward cross-reference to SC052
3. Short bridge sentence explaining why the two notes remain adjacent in the assembled half
