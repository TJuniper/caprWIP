# Missing direct sources — Anglo-Frisian pass

Audit performed as part of the Anglo-Frisian source-ingestion pass, before
any synthesis was written.

## Why this file exists

The nine sources ingested in this pass depend heavily on a smaller set of
earlier works, and they frequently disagree about what those earlier works
established. Where CAPR does not hold a work directly, the only honest
record is *"author A reports that author B argued P"*. That is a weaker
claim than *"B argued P"*, and much weaker than *"P"*.

The standing rule for this research area is therefore:

> A report by Laker, Kortlandt, Bremmer, Repanšek or Versloot of another
> scholar's argument is evidence about the reporting author's reading. It
> is **not** direct evidence from the scholar reported, and it may not be
> cited as such in any CAPR memo.

Nothing in this file blocks the *research architecture*. It blocks *final
adjudication* of the questions listed against each item.

## Method

Searched `docs/references/` for filename matches on each author, and
`docs/refs.bib` for bibliography keys, before the synthesis was written.
Local holdings that are adjacent but not substitutes are noted explicitly,
because an adjacent holding is the most likely route to an accidental
substitution.

### Acquisition recheck

The subsequent acquisition audit went beyond filename matches:

- Searched the 800 reference text files, including legacy extracts, for the
  requested titles and authors, and checked the bibliography separately.
- Inspected PDF metadata and the opening six sheets of all 67 reference
  PDFs and 574 PDFs recursively under Downloads. Title mentions in another
  author's references were not counted as direct holdings.
- Screened low-text PDFs separately. The anonymous 587-sheet scan
  `annas-arch-cc3a47d26264.pdf` was identified from its page images as
  Bammesberger's edited *Die Laryngaltheorie* (1988), not one of the
  requested Frisian volumes.
- Identified ambiguously named relevant articles directly: `abag-article-p165_8.pdf`
  is Laker 2007; `412645` is Cercignani 1980; `angl_1997_115_2_223` is
  Bammesberger's *herfest* article. None supplies a missing target.
- Checked relevant alternate-format filenames under Downloads; no matching
  EPUB, DjVu, text, or ZIP was found.

At that audit, the six priority works below were not identified as direct
holdings in the reference library or Downloads. Hogg 1979, Goblirsch 1991,
Bremmer 2009 and Nielsen 2001 have subsequently been downloaded and ingested;
their current status is recorded below.
The audit is not a claim about
unsearched directories elsewhere on the computer. The held Hogg PDF is
Volume 1, *Phonology*, first published in 1992 and reissued in 2011:
the filename's inclusion of Fulk does not make it the 1979 article or
Volume 2. The other held Stiles works and Fulk 2018 are likewise not
substitutes.

| Requested direct work | Acquisition locator |
|---|---|
| Stiles 1995, "Remarks on the 'Anglo-Frisian' Thesis" | *Friesische Studien II*, pp. 177–220 |
| Bremmer 2009, *An Introduction to Old Frisian: History, Grammar, Reader, Glossary* | Full book |
| Fulk 1998, "The Chronology of Anglo-Frisian Sound Changes" | *Approaches to Old Frisian Philology*, ABaG 49, pp. 139–154 |
| Hogg 1979, "Old English Palatalization" | *Transactions of the Philological Society*, pp. 89–113 |
| Goblirsch 1991, "Germanic ai and au in Anglo-Frisian" | ABaG 33, pp. 17–23 |
| Nielsen 2001, "Frisian and the Grouping of the Older Germanic Languages" | *Handbook of Frisian Studies / Handbuch des Friesischen*, pp. 512–523 |

## Status table

| Source | Held? | Priority | What it blocks |
|---|---|---|---|
| Stiles 1995, "Remarks on the 'Anglo-Frisian' Thesis" | **No** | **Critical** | The central chronological argument of the whole controversy |
| Bremmer 2009, *An Introduction to Old Frisian* | **Complete PDF parts and Vision text held** | Review next | A baseline pre-Old Frisian ordered chain |
| Fulk 1998, "The Chronology of Anglo-Frisian Sound Changes" | **No** | High | Direct, dedicated treatment of the exact question |
| Hogg 1979, "Old English Palatalization" | **PDF and Vision text held** | Review next | Direct-source review of the palatalization chronology Laker argues with |
| Nielsen 2001; other cited treatments | **2001 chapter PDF and Vision text held; other titles not held** | Review next | Independent assessment of the feature list |
| Goblirsch 1991 on Germanic *ai/*au in Anglo-Frisian | **PDF and Vision text held** | Review next | Direct-source review of the *au side of SC030/SC043 |
| Siebs, *Geschichte der friesischen Sprache* / Grundriss article | **No** | Medium | The classic pro-shared-palatalization position |
| Luick, relevant passages | **Partial** | Medium | §§118–120 located by printed headings; §637 and exact corrupted glyphs still unverified |

## Detail

### Stiles 1995, "Remarks on the 'Anglo-Frisian' Thesis"

**Not held in any form.** This is the most damaging absence in the pass.

Bremmer 2008, Laker 2007, Kortlandt 2008 and Repanšek 2012 all engage
Stiles's chronological argument, and they do not all report it identically.
Bremmer 2008 contains the fullest locally available report of it; that
report is recorded in the Bremmer source card, explicitly marked as
Bremmer's reading.

Stiles's argument is exactly of the form the CAPR tree test is designed to
consume — a claim about which ordering edges the traditional Anglo-Frisian
feature list can and cannot support. CAPR's Anglo-Frisian node is a fixed
modelling requirement; the open question is which innovations can precede
that node on the common stem. Final disputed placements must not be settled
from second-hand reports by authors who are in some cases arguing against
Stiles.

**Blocks:** final adjudication of every `U`-class feature in the synthesis;
in particular the SC030/SC043 identity question.

### Bremmer 2009, *An Introduction to Old Frisian*

**Now held in full:** seventeen local, ignored ebook PDF parts and
`docs/references/bremmer_2009_introduction_old_frisian.vision.txt`,
with markers i–xii and 1–238. The copyright page identifies the supplied
copy as the corrected 2011 reprint of the 2009 edition. The born-digital
text layer has materially faulty phonetic-font mappings, so every part
was processed with the established asynchronous Vision PDF runner.
Bremmer 2008 is a separate article, not a substitute for this handbook.

This is the standard student/reference handbook for Old Frisian and the
natural source for a baseline ordered pre-Old Frisian chain. The synthesis
dossier's Frisian chains are consequently assembled from specialist
articles, each of which addresses only part of the sequence. That is why
the Frisian chain in the synthesis is presented as *alternatives* rather
than as one sequence with gaps filled in.

**Review still required:** a complete pre-Old Frisian chain; therefore a
future Frisian CAPR implementation. Acquisition does not supply an adjudicated
chain or resolve contradictions between the handbook's proposed constraints.

### Fulk 1998, "The Chronology of Anglo-Frisian Sound Changes"

**Not held.**

**Adjacent holding that is not a substitute:** Fulk 2018, *A Comparative
Grammar of the Early Germanic Languages*
(`fulk_comparative_grammar_early_germanic.vision.txt`) is held. The separate
held Hogg grammar is Volume 1, *Phonology*, in its 2011 reissue, not
Hogg and Fulk's Volume 2. Neither held grammar is the 1998 paper, which is
dedicated to precisely the question this research area exists to answer.
Citing Fulk 2018 as though it were that paper would be exactly the
substitution this file forbids.

**Blocks:** confidence that the synthesis has canvassed the main
chronological positions.

### Hogg 1979, "Old English Palatalization"

**Now held as a local, ignored PDF:**
`docs/references/hogg_1979_old_english_palatalization.pdf`, TPS 77.1
(1979), pp. 89–113; bibliography key `Hogg1979`.
It is scanned, and its embedded OCR corrupts phonetic symbols. The established
asynchronous Google Vision PDF runner succeeded; the searchable text is
`docs/references/hogg_1979_old_english_palatalization.vision.txt`, with
printed-page markers 89–113 and documented image-verified repairs.
The earlier synchronous-image resource errors did not require a billing
change. Until source review is completed, the source
cards' reports of Hogg through Laker are still reports, not verified
readings of Hogg.

**Adjacent holding that is not a substitute:** Hogg 1992, *A Grammar of Old
English* vol. 1, is held and treats palatalization. The 1979 article is a
specific argument that Laker engages with directly; the handbook is not
that argument.

**Blocks:** the palatalization research note's assessment of which
pro-shared arguments actually fail.

### Nielsen

**Nielsen 2001 now held:** local ignored PDF and
`docs/references/nielsen_2001_frisian_and_grouping_older_germanic_languages.vision.txt`,
printed pp. 512–523, bibliography key `Nielsen2001`. The scan was processed
with the established asynchronous Vision PDF runner; the neighbouring
chapter's opening on p. 523 is excluded from Nielsen's text.
Other Nielsen works on Germanic dialect relations and on the
Anglo-Frisian feature list remain missing where cited. Which
specific Nielsen titles are load-bearing is recorded in the individual
source cards (§13 of each).

### Goblirsch on Germanic *ai/*au in Anglo-Frisian

**Now held as a local, ignored PDF:**
`docs/references/goblirsch_1991_germanic_ai_and_au_in_anglo_frisian.pdf`,
ABaG 33 (1991), pp. 17–23; bibliography key `Goblirsch1991`.
It is scanned, with materially unreliable embedded OCR. The established
asynchronous Google Vision PDF runner succeeded; the searchable text is
`docs/references/goblirsch_1991_germanic_ai_and_au_in_anglo_frisian.vision.txt`,
with printed-page markers 17–23 and documented image-verified repairs.
Direct review remains a separate task. Relevant specifically to the *au side of the SC030/SC043 question,
where Laker locates a genuinely unresolved argument. Acquisition alone does
not verify Laker's interpretation.

### Siebs

**Not held.** Laker 2007 (p. 165) cites Siebs as holding that palatalization
of *-k(k)-* and *-g(g)-* belongs to "der englisch-friesischen, das heißt der
kontinentalen Periode". CAPR knows this position only through Laker's
quotation.

### Luick — held; selected printed-page locators now established

`docs/references/luick_historische_grammatik.txt` is held (~29,750 lines).
Its page markers are of the form `--- PAGE n ---` and are **pdf sheet
numbers, not printed folios**. It also predates the marker convention used
by the newer extracts.

The continuation pass inspected the local text itself, not just reports of
Luick. Adjacent explicit printed headings establish these local locators:
sheet 177 = p. 129, 178 = p. 130, 179 = p. 131, 180 = p. 132.
This local mapping is not a claim that a single offset applies to the entire
legacy extraction.

Load-bearing direct passages:

- §118, p. 130: Luick calls fronting a common Anglo-Frisian process
  ("Offenbar liegt ein gemein-anglofriesischer Vorgang vor") and orders its
  beginnings after nasal-conditioned darkening [@Luick1914, p. 130, §118].
- §119, pp. 130–131: the first component of the diphthong participates in
  the fronting ("Hierauf nahm die erste Komponente an der Aufhellung des
  a-Lautes teil"); unrounding of the second component is placed in the
  seventh century [@Luick1914, pp. 130–131, §119].
- §120, pp. 131–132: Luick discusses the Frisian monophthong and proposes
  a regressive-assimilation account with "Vielleicht". That is a tentative
  alternative to Campbell's early contraction, not secure intermediate-state
  evidence [@Luick1914, pp. 131–132, §120].

The legacy extract corrupts several linguistic glyphs; no matching local PDF
was located. Consequently this pass uses the legible prose and printed
headings, **not** a reconstructed reading of the corrupted intermediate
diphthong. Exact quoted phonetic forms still require page-image confirmation.

Laker's report of palatalization "noch zur Zeit der anglofriesischen
Ge[meinschaft]" refers to §637 [@Laker2007, p. 165, n. 2]. That section was
not located in the held text. Its wording and printed-page locator remain
unverified; do not treat the §§118–120 lookup as verification of §637.

## Recommended acquisition order

1. **Stiles 1995** — unblocks the most.
2. **Bremmer 2009** — complete PDF parts and Vision text acquired; review
   the baseline handbook against which the partial Frisian
   chains can be assessed.
3. **Fulk 1998** — directly on topic.
4. **Hogg 1979** — PDF and Vision text acquired; complete direct review.
5. Acquire/identify the **Luick** page images and missing §637; selected
   §§118–120 printed-page locators are now established, but glyph-level
   confirmation and the palatalization passage remain outstanding.
6. **Goblirsch 1991** — PDF and Vision text acquired; complete direct review.
7. **Nielsen 2001** — chapter acquired; complete direct review. Other
   specifically load-bearing Nielsen treatments and Siebs still need acquisition.
