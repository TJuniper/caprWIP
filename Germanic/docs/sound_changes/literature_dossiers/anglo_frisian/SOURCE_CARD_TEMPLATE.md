# Source card template (Anglo-Frisian research area)

Copy this file to `source_cards/NN-author-year-shorttitle.md` and fill in
every section. Never delete a section; write "none" or "not discussed"
with a reason if the source has nothing.

## Hard rules

1. **Every substantive claim carries a printed page number** in the form
   `(p. 283)` or `(pp. 283–285)`, referring to the PRINTED folio as marked
   by `=== page NNN ===` in the committed reference text.
2. **Never attribute to an author a view they merely report.** Section
   "Author's own thesis" is for what the author argues. Views they
   summarize, describe or attack go in "Positions reported, not held".
3. **Never let author A's report of author B stand in as B's evidence.**
   If Laker says Stiles argued P, the card records "Laker (p. n) reports
   Stiles 1995 as arguing P" — not "Stiles argued P".
4. **Do not upgrade hedges.** If the author writes "probably", "it may be
   that", "I am inclined to think", the card says so. An author's admitted
   uncertainty must not become a CAPR fact.
5. **Relative chronology is written as ordered statements**, `X < Y < Z`
   meaning X precedes Y precedes Z, with the page and the argument that
   establishes each edge. Do not write "early" or "late" where the source
   supports an ordering.
6. **Absolute dates are recorded separately from relative order.** Never
   merge them into one sequence.

---

# <Author Year>, "<Title>"

## 1. Bibliographic identity

- **Citation:**
- **BibTeX key:**
- **Local reference file:** `docs/references/....txt`
- **Printed pages:**
- **Pages actually used for this card:**
- **Genre / venue character:** (research article, handbook chapter,
  polemic, survey — this affects how much independent evidential weight
  the source carries)

## 2. Author's own thesis

What this author themself argues, in their own terms. Two to six
sentences. Quote the thesis statement if there is one.

## 3. Positions reported, not held

Views the author summarizes, attributes to others, or attacks. Each with
whose view it is and where the author discusses it.

## 4. Languages and evidence actually used

Which of Old English, Old Frisian, Old Saxon, Dutch/coastal varieties,
North Germanic, runic material, place-names, loanwords, onomastics etc.
actually do argumentative work — as opposed to being mentioned. Note
which dialects within OE/OFris, since this frequently matters.

## 5. Proposed relative chronology

Separate sub-blocks for English and Frisian whenever the author supplies
separate chronologies. Use ordered statements.

### English
```
X < Y < Z
```
- edge `X < Y`: (page) (argument / diagnostic form)
- edge `Y < Z`: (page) (argument / diagnostic form)

### Frisian
(same form)

### Shared / undifferentiated stem
(changes the author places before any split)

## 6. Absolute chronology

Actual dates and termini, kept apart from §5. For each: the date, what is
dated (an object? an inscription? a sound change?), and how many
inferential steps separate the dated thing from the sound change.

## 7. Proposed shared innovations

Developments this author regards as genuinely common to English and
Frisian, with the page and the reason.

## 8. Proposed independent developments

Superficially similar OE/OFris developments this author regards as
parallel or independent, with the page and the reason.

## 9. Diagnostics

The actual lexical, runic or onomastic evidence doing the work. For each:

| Form | Comparandum | Page | Proposition it is meant to demonstrate |
|---|---|---|---|

Do not merely list examples. State what chronological proposition each
one is supposed to establish, and whether it does so uniquely or only
compatibly.

## 10. Tree-test implications

Apply the CAPR criterion in `../README.md`.

- **If this author's chronology is correct, which alleged Anglo-Frisian
  innovations can still occupy a shared ancestral node?**
- **Which apparent correspondences would necessarily have to be
  independent parallel changes under a tree model?**
- **Where does the author invoke wave/continuum/linkage in place of an
  ordering argument?** (Record this neutrally; it marks places where the
  source supplies no tree-usable edge, not places where the source is
  wrong.)

## 11. Uncertainty grading

Sort this source's claims into:

- **Firmly demonstrated** — the data compel the conclusion;
- **Author's preferred reconstruction** — consistent, but alternatives
  exist and the author knows it;
- **Plausible but non-unique inference** — the evidence is compatible
  with the claim and with others;
- **Explicitly unresolved** — the author says it is open.

## 12. Implementation-ready extracts (Frisian)

Only where the author supplies enough. For each proposed Frisian
development: input; output; conditioning; scope; approximate stage;
ordering constraints; evidence; uncertainty. This is preparation for a
future Frisian cascade, **not** an implementation.

## 13. Dependencies on sources CAPR does not hold

Which of this author's load-bearing claims rest on works not in the local
reference library. Cross-reference `../missing-direct-sources.md`.
