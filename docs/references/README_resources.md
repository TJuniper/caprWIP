# OCRed reference resources (quick index)

This file lists OCRed reference texts in `docs/references/` with quick hints for searching.

## Old English grammars and historical phonology

- `hogg_vol1.txt`  
  Hogg, *A Grammar of Old English*, Vol. 1: Phonology (1992).  
  Primary OE grammar. ~23,600 lines.

- `ringe_taylor_linguistic_history_vol2.txt`  
  Ringe & Taylor, *A Linguistic History of English*, Vol. 2: From Proto-Indo-European to Proto-Germanic (2014).  
  Primary reference for sound change chronology and PGmc→OE derivation. ~38,800 lines.

- `luick_historische_grammatik.txt`  
  Luick, *Historische Grammatik der englischen Sprache* (1914–40).  
  Major German-language OE/ME historical grammar. ~29,750 lines.

- `bulbring_altenglisches_elementarbuch.txt`  
  Bülbring, *Altenglisches Elementarbuch*, I: Lautlehre (1902).  
  Detailed OE phonology in German. ~15,690 lines.

- `kaluza_historische_grammatik_englisch.txt`  
  Kaluza, *Historische Grammatik der englischen Sprache* (1900–01).  
  Two-volume historical grammar of English. OCR from page images (720 pages); first ~800 lines are frontmatter/OCR artefacts, real content starts ~line 794. ~29,575 lines.

- `fulk_comparative_grammar_early_germanic.txt`  
  Fulk, *A Comparative Grammar of the Early Germanic Languages* (2018).  
  Modern comparative grammar covering phonology, morphology of all early Germanic languages. Good for cross-branch comparisons. ~34,884 lines.

## Proto-Germanic and Germanic etymological dictionaries

- `etymological_dictionary_of_proto_germanic_kroonen.txt`  
  Kroonen, *Etymological Dictionary of Proto-Germanic* (2013).  
  Standard PGmc etymological dictionary. ~54,000 lines.

- `orel_handbook_germanic_etymology.txt`  
  Orel, *A Handbook of Germanic Etymology* (2003).  
  Alternative PGmc etymological dictionary. Useful for cross-referencing Kroonen. Includes extensive bibliography references per entry. ~70,353 lines.

- `kluge_seebold_etymologisches_woerterbuch.txt`  
  Kluge (ed. Seebold), *Etymologisches Wörterbuch der deutschen Sprache* (24th ed., 2002).  
  Standard German etymological dictionary. Entries give cognates across Germanic and IE. Useful for OHG forms, dating, and bibliography. ~101,947 lines.

## Old English / Germanic lexica

- `aconciseanglosa01hallgoog.txt`  
  Hall, *A Concise Anglo-Saxon Dictionary* (2nd ed.).

- `anglosaxondictio00tolluoft.txt`  
  Bosworth-Toller (dictionary + supplement scans combined).

- `anglosaxonoldeng00wrig.txt`  
  Wright & Wülcker, *Anglo-Saxon and Old English Vocabularies*.

- `aneightcenturyl00librgoog.txt`  
  Hessels / early glossary material (Eighth-Century Latin-Anglo-Saxon Glossary).

## Old English primers and readers

- `sweet_anglo_saxon_primer.txt` / `.pdf`  
  Sweet, *An Anglo-Saxon Primer* (Oxford University Press).  
  Introductory grammar with notes and glossary. ~7,000 lines.

- `bright_anglo_saxon_reader.txt` / `.pdf`  
  Bright, *An Anglo-Saxon Reader* (4th ed., 1917).  
  Reader with notes, complete glossary, chapter on versification, and outline of OE grammar. ~27,700 lines.

## Articles and special studies

- `vine_2019_greek_stomylos.txt`  
  Vine, "Greek στωμύλος 'chatty': An anomalous ō-grade" (*Indo-European Linguistics* 7, 2019, 222–240).  
  Discusses the PIE \*stom-/\*stem- root ('mouth') with detailed treatment of ablaut grades and derivatives. Directly relevant to the stefn/stemn problem (see DEV_NOTES §Case 3 and notable_findings §5). ~826 lines.

- `polome_1967_reflexes_ie_ms.txt`  
  Polomé, "Notes on the Reflexes of IE /ms/ in Germanic" (*Revue belge de philologie et d'histoire* 45.3, 1967, 800–826).  
  Discusses IE nasal + s clusters in Germanic, with treatment of the \*stemn-/\*stibna problem. Directly relevant to the stefn/stemn problem. ~1,282 lines.

- `thorhallsdottir_1993_intervocalic_j.vision.txt`  
  Þórhallsdóttir, *The Development of Intervocalic \*j in Proto-Germanic* (Ph.D. dissertation, Cornell University, 1993; UMI 9410504). 293 scanned pages, no text layer; Google Vision OCR over 300 dpi renderings.  
  Page markers are the dissertation's own **printed** folios (printed N = PDF sheet N + 11; front matter as roman iii–ix). The specialist source for the hiatus-breaking consonants of the *verba pura*: Ch. 5 (pp. 114–137) is the direct authority for CAPR SC102, giving the phonological insertion of \*w before \*u (pp. 120, 126–127) and its analogical generalization through the Anglo-Frisian paradigm (pp. 130, 134, 136). Heavy diacritic load — verify any quoted form against the page image. ~293 pages.

- `lid_1952_nordiske_nominativ_an_stammer.vision.txt`  
  Lid, "Den nordiske nominativ singularis av maskuline an-stammer" (*Norsk Tidsskrift for Sprogvidenskap* 16, 1952, 237–240). Norwegian Nynorsk; 2-up scan, split on the detected gutter, Google Vision OCR.  
  Cited in CAPR for p. 238, where the Sámi loanword evidence (Sámi *mānno* etc.) is used to argue that Germanic \*ē (cf. Gothic *mēna*) had already become *ā* before the borrowing. Replaces the former indirect citation via Stiles 2017: 4. One OCR character (*å* for printed *ā*) was corrected against the page image and the correction is documented in the file header. ~258 lines.

## Anglo-Frisian / North Sea Germanic specialist literature

Ingested for the Anglo-Frisian chronology research pass. **Six** of the eight
were extracted with `pdftotext -layout` from reliable born-digital text
layers. **One — Campbell 1939 — required the Google Vision OCR route** and carries the
`.vision.txt` suffix. **One — Laker 2007 — required a deterministic
font-aware rebuild** and keeps the plain `.txt` suffix, since it is not OCR.

An initial screen that measured only characters-per-page passed all eight;
that screen was wrong, because it measured volume rather than accuracy. A
second screen on diacritic integrity caught both failures:

- **Campbell 1939** yields zero ae-ligatures, zero macrons and zero thorn
  across thirty pages of Old Frisian vowel history. Its text layer is itself
  machine-generated from the 1939 letterpress page and destroys exactly the
  characters that carry the content.
- **Laker 2007** is born-digital, but three of its fonts carry WordPerfect
  legacy encodings with *wrong* ToUnicode maps. The palatal dot of `ċ` is
  mapped to `k`, so both `pdftotext` and PyMuPDF render the article's central
  diagnostic `ċeapian` as `keapian` — an unpalatalized form, in a paper
  arguing that the form *is* palatalized. That is an active falsification, not
  merely a loss, and it is the clearest case in this library of why a text
  layer's existence is not evidence of its reliability.

  Vision was not the right fix here either: it reads the dot only about
  two-thirds of the time and misreads `æ` as `oe`/`a`. Instead the text was
  rebuilt **from the PDF's own glyph stream with its font labels**, applying
  each affected font's fixed substitution table. That is deterministic and is
  not OCR, so the file keeps the plain `.txt` suffix. Characters in the Times
  fonts are untouched, which is why genuine `k` (Luick, Laker, kontinentalen)
  survives correctly. Each substitution was established three ways: by font
  membership; by token-by-token alignment against an independent Vision OCR of
  the same pages; and, where doubt remained, by rendering the line at 500 dpi
  and reading it off the page. The restored forms are self-validating — they
  are OE lexemes with exactly the expected palatal spellings (`eċġ`, `seċġ`,
  `hryċġ`, `dīċ`, `rīċe`, `wīċ`, `ċeorl`, `wreċċa`, `styċċe`, `wiċċe`,
  `mēċe`, `fliċċe`), which a wrong table could not produce.

Three further files (Bremmer, Kortlandt, Repanšek) had a *recoverable*
defect: the John Benjamins house font emits combining macrons as a trailing
`U+00A4`, with `\` for schwa and dotless `ı` for `i` in Kortlandt. That
mapping is one-to-one and context-free, so it was repaired deterministically
(`mo¤na` → `mōna`, `æ¤` → `ǣ`, `*e¤\` → `*ēə`) and the repair was verified
against forms whose value is fixed by the surrounding prose. No judgement
call was involved and no OCR was needed.

Every file in this group uses the `=== page NNN ===` marker convention with
**printed folio numbers**, so memos can cite exact printed pages. Each file
opens with a header recording the citation, the extraction method, the
mechanically verified pdf-sheet-to-printed-folio offset, and an itemised
account of every sheet that did not self-confirm its folio (opening pages
with drop titles, full-page figures, blanks). Across the group 202 of 210
sheets confirmed their folio directly; all 8 exceptions are individually
classified in the file that contains them.

Research use of these sources is organised in
`Germanic/docs/sound_changes/literature_dossiers/anglo_frisian/`, whose
synthesis dossier is the single authority for the comparative English/Frisian
chronology.

- `campbell_1939_some_old_frisian_sound_changes.vision.txt`
  Campbell, "Some Old Frisian Sound-Changes", TPS 38.1 (1939), pp. 78-107.
  The classic statement of an Anglo-Frisian unity period; the baseline that
  later work argues with. 30 printed pages.

- `bremmer_2008_north_sea_germanic_at_the_cross_roads.txt`
  Bremmer, "North-Sea Germanic at the Cross-Roads: The Emergence of Frisian
  and Hollandish", NOWELE 54/55 (2008), pp. 279-308.
  Includes the fullest locally available report of Stiles 1995, which CAPR
  does not hold directly. 30 printed pages.

- `kortlandt_2008_anglo_frisian.txt`
  Kortlandt, "Anglo-Frisian", NOWELE 54/55 (2008), pp. 265-278.
  Explicit numbered relative chronologies. 14 printed pages.

- `laker_2007_palatalization_of_velars.txt`
  Laker, "Palatalization of Velars: A Major Link of Old English and Old
  Frisian", ABaeG 64 (2007), pp. 165-184.
  The hinge of the shared-versus-independent palatalization question.
  20 printed pages. Rebuilt font-aware from the glyph stream (see above);
  palatal `ċ`/`ġ` are correct. Laker prints `kapia` and `ċeapian` without
  macrons; that is faithful to the printed page, not an extraction loss.

- `repansek_2012_anglo_frisian_vowel_system.txt`
  Repansek, "Remarks on the Development of the 'Anglo-Frisian' Vowel System",
  NOWELE 64/65 (2012), pp. 77-90. 14 printed pages.

- `versloot_2017_proto_germanic_ai_in_north_and_west_germanic.txt`
  Versloot, "Proto-Germanic *ai in North and West Germanic", Folia
  Linguistica Historica 38 (2017), pp. 281-324. 44 printed pages.

- `versloot_2021_traces_of_a_north_sea_germanic_idiom.txt`
  Versloot, "Traces of a North Sea Germanic Idiom in the Fifth-Seventh
  Centuries AD", in Hines & IJssennagger-van der Pluijm (eds), *Frisians of
  the Early Middle Ages* (2021), pp. 339-374. Printed p. 352 is a full-page
  figure and p. 374 is blank. 36 printed pages.

- `waxenberger_2019_absolute_chronology_pre_oe_runic.txt`
  Waxenberger, "Absolute Chronology of Early Sound Changes Reflected in
  Pre-Old English Runic Inscriptions", NOWELE 72.1 (2019), pp. 60-77.
  Absolute, archaeologically anchored dates; to be kept methodologically
  distinct from handbook relative chronologies. 18 printed pages.

## Other references

- `oe_sound_change_index.md`  
  Quick index of frequently cited sound-change passages + exact `rg`/`sed` commands.

- `knob_email_2026-01-22.txt` / `README_knob.md`  
  Project-specific correspondence/notes.


## Missing direct sources (Anglo-Frisian pass)

These works are load-bearing in the literature ingested above but are **not**
held locally in any form. They are recorded here so that no memo silently
turns one author's report of another into that other author's evidence. The
full audit, including what each one blocks, is in
`Germanic/docs/sound_changes/literature_dossiers/anglo_frisian/missing-direct-sources.md`.

- **Stiles 1995**, "Remarks on the 'Anglo-Frisian' Thesis". *Highest
  priority.* Bremmer, Laker, Kortlandt and Repansek all engage his
  chronological argument; CAPR currently knows it only at second hand.
- **Bremmer 2009**, *An Introduction to Old Frisian*. The standard handbook
  chronology of Old Frisian; its absence is the main reason CAPR cannot yet
  state a baseline pre-Old Frisian chain.
- **Fulk 1998**, "The Chronology of Anglo-Frisian Sound Changes". Directly on
  the question at issue. (Fulk 2018, *A Comparative Grammar of the Early
  Germanic Languages*, is held, but is not a substitute.)
- **Hogg 1979**, "Old English Palatalization". Load-bearing for Laker.
  (Hogg 1992 is held and covers palatalization, but is not this argument.)
- **Nielsen**, the treatments cited by Stiles, Laker and Bremmer.
- **Goblirsch** on Germanic *ai/*au in Anglo-Frisian.
- **Siebs**, cited by Laker as a proponent of shared palatalization.

`luick_historische_grammatik.txt` is held, but its page markers are pdf
**sheet** numbers (`--- PAGE n ---`), not printed folios, so a folio offset
must be established before any Luick passage is cited by printed page in this
area.

## Not yet OCRed

- **Lloyd & Springer**, *Etymologisches Wörterbuch des Althochdeutschen*, Bd. 1 (1998).  
  Source PDF is a scan with no text layer; would need OCR. DJVU version also available.  
  Located in Downloads, not yet incorporated.
