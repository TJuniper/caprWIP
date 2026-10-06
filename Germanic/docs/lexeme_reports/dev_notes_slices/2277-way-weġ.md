---
row_id: 2277
concept: way
counterpart: weġ
proto: *wégaz
protoform: *wégaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2277-way-weġ.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2277-way-weġ.md
linked_dossier_or_analysis_files:
  - Germanic/docs/dossiers/g-palatalisation-conditioning.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2277 way / weġ

## Current row state

- CONCEPT: `way`
- COUNTERPART: `weġ`
- PROTO: `*wégaz`
- PROTOFORM: `*wégaz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Kroonen *wega- m. 'way, road' → OE weġ m.; wē is not attested as OE 'way'` [Germanic/data/germanic-aligned-final.tsv:1347-1347].
- Existing row infrastructure: both a packet and a research memo now exist for this row, but no standalone pilot file was found under `Germanic/docs/lexeme_reports/pilot/` [Germanic/docs/lexeme_reports/packets/2277-way-weġ.md:1-105; Germanic/docs/lexeme_reports/research_memos/2277-way-weġ.md:1-79].
- Current implementation status: the packet's compact trace already gives a clean regular derivation `*wégaz -> weġ`, with final `-z` deletion, final bare `-a` loss, and OE velar palatalisation as the decisive late step [Germanic/docs/lexeme_reports/packets/2277-way-weġ.md:17-43].
- Problem status: no `oe_known_problems.tsv` entry was found for this lexeme, so the live issue is documentary interpretation, not an unresolved FST failure [Germanic/docs/lexeme_reports/packets/2277-way-weġ.md:45-47; Germanic/docs/lexeme_reports/research_memos/2277-way-weġ.md:21-32].

## Development-note summary

Current DEV_NOTES support for row 2277 is real, but it is concentrated in the later palatalisation canvass rather than in an older standalone lexeme dossier. The secure current material says that `*wégaz -> weġ` is **already the correct Old English outcome**, because after weak-tail apocope the inherited `*g` is word-final after a front vowel; this places the row directly inside the handbook environment where final OE `ġ` is expected, not inside a long-vowel problem bucket [Germanic/docs/DEV_NOTES.md:43176-43201,43224-43244; @Campbell1959, §§428-429; @RingeTaylor2014, §6.4.1]. DEV_NOTES is therefore useful here not because it proposes a new repair, but because it explicitly retracts the earlier misreading that had treated this lexeme as if it ought to surface as unattested `wē`.

That earlier misreading must remain visible, but only as superseded diagnostics. In the 2026-01-02 mismatch note, the row still appeared on a "long-vowel missing" list as ``*wegăz → weġ (expected wē)`` [Germanic/docs/DEV_NOTES.md:2621-2624]. The later palatalisation note reverses that interpretation with equally explicit wording: ``*wégaz → weġ` 'way' — but here *-g* is word-final after weak-tail apocope, so palatalisation is **correct** (Campbell: dæġ, weġ)` [Germanic/docs/DEV_NOTES.md:43181-43182]. For this slice, that chronological reversal is the central project fact. The row is valuable precisely because DEV_NOTES moved from a false long-vowel expectation to a source-backed final-palatal analysis.

The three-way distinction also has to be stated plainly. `PROTO` is the row's comparative Proto-Germanic nominative-singular form `*wégaz`; `PROTOFORM` is the same form because the current cascade derives the row without paradigm substitution or alternate input; `COUNTERPART` is the project-normalized Old English citation form `weġ` [Germanic/data/germanic-aligned-final.tsv:1347-1347]. Kroonen's form `*wega-` is not a competing row target but a stem citation for the cognate set: `*wega- m. 'way, road' ... OE weg m. 'id.'` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29259-29262; @Kroonen2013]. That distinction matters because the stale `wē` expectation can look tempting if the Kroonen headword is misread as requiring contraction or long-vowel retargeting. The checked repo evidence does not support that move.

The philological core is the familiar singular/plural contrast `weġ ~ wegas` rather than any special analogical rescue. DEV_NOTES' handbook canvass summarizes Campbell's rule as follows: final /g/ is palatal "word-finally after any front V (*weġ, dæġ, mǣġ*)" but remains velar when followed by a back vowel, including `wegas` [Germanic/docs/DEV_NOTES.md:43229-43240]. Campbell's own wording is the same in fuller form: "In final position, k and ȝ were palatalized after OE front vowels" and medially velars "remained when there was a back vowel (or back element of a diphthong) either before or after them, e.g. ... `wegas` ways, `nigon` nine" [docs/references/campbell_old_english_grammar.txt:11251-11314; @Campbell1959, §§428-429]. Hogg is reported in DEV_NOTES as giving the same result tautosyllabically: in `we.gas` the consonant belongs with the following `a` and stays velar, whereas in `weġ#` it is coda-final with the front vowel and palatal [Germanic/docs/DEV_NOTES.md:43254-43258; @HoggPhonology1992, ch. 7].

Ringe and Taylor point in the same direction and are especially helpful for keeping the row out of the `wē` trap. DEV_NOTES quotes their rule that "preconsonantal and word-final *g were palatalized by any preceding front vowel," while intervocalic *g palatalized only between front vowels [Germanic/docs/DEV_NOTES.md:43245-43252; @RingeTaylor2014, §6.4.1]. That rule matches the row exactly once `*wégaz` has passed through final `-z` deletion and weak-tail loss. The same consensus is condensed in the dossier statement that "Everyone cites the **same minimal pair** ... **OE *weġ* 'way' ... is palatal, but the plural *wegas* ... is velar**" [Germanic/docs/dossiers/g-palatalisation-conditioning.md:55-57]. For future work, this is the most economical philological anchor: singular `weġ` is not an oddity but the textbook positive control for final palatalisation.

The negative point must remain equally explicit. Nothing in the current row, packet, memo, or later DEV_NOTES canvass supports OE `wē` as the lexical target for 'way' [Germanic/data/germanic-aligned-final.tsv:1347-1347; Germanic/docs/lexeme_reports/research_memos/2277-way-weġ.md:43-61]. The memo is right to insist that the issue is not whether OE `weg`/`weġ` exists—it does—but how the project should normalize it and how to segregate stale diagnostics from live policy [Germanic/docs/lexeme_reports/research_memos/2277-way-weġ.md:43-61]. This slice should therefore preserve both claims together: `weġ` is the intended normalized OE singular, and `wē` belongs only to superseded debugging history.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-43176-43201

- Source heading: `§17.50.3 — Implementation result and a follow-on finding: *g palatalisation before back vowels`
- Source line or section hint: `lines 43176-43201`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `palatalisation`; `word_final_g`; `weak_tail_apocope`; `reversal_of_wē_diagnostic`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the clearest row-local DEV_NOTES statement and should be treated as the primary anchor for the slice. The note isolates `*wégaz → weġ` as one of the empirical probes used while auditing the overly broad *g-palatalisation rule, then states the row-specific conclusion in full: ``*wégaz → weġ` 'way' — but here *-g* is word-final after weak-tail apocope, so palatalisation is **correct** (Campbell: dæġ, weġ)` [Germanic/docs/DEV_NOTES.md:43179-43182]. That wording matters because it does two things at once: it affirms the current `COUNTERPART`, and it explains why the row is **not** evidence for suppressing palatalisation before back vowels. For row 2277 this fragment is current, direct, and index-worthy.

### DEV_NOTES:line-43224-43258

- Source heading: `§17.50.4.1 The handbook consensus`
- Source line or section hint: `lines 43224-43258`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `campbell`; `hogg`; `ringe_taylor`; `weġ_wegas_contrast`; `shared_philology`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `782`; `940`; `1579`

This section is shared rather than row-exclusive, but it is still one of the strongest pieces of support for 2277 because it assembles the handbook consensus around exactly the `weġ ~ wegas` contrast. DEV_NOTES summarizes Campbell: final /g/ is palatal in `weġ, dæġ, mǣġ`, but velar before a following back vowel such as `wegas`; it then gives Hogg's tautosyllabic account of the same alternation and quotes Ringe-Taylor's rule for word-final and preconsonantal *g palatalisation [Germanic/docs/DEV_NOTES.md:43229-43258]. For this row, the value of the fragment is that it turns the live target into a textbook control case rather than a one-off lexical assertion. It also provides the best place to cite the singular/plural distinction explicitly if future report prose needs to defend `weġ` against renewed pressure toward `wē`.

### DEV_NOTES:line-43346-43360

- Source heading: `§17.50.4.5 Regression watchlist`
- Source line or section hint: `lines 43346-43360`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `regression_watchlist`; `positive_control`; `front_vowel_word_final`; `verification_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `782`; `940`; `1579`

This fragment is not interpretive by itself, but it is strong verification history. The watchlist table includes `| 1882 | *wégaz | weġ | front-V _ # | palatal |`, placing the row among the forms that must remain positive controls after any *g-palatalisation change [Germanic/docs/DEV_NOTES.md:43351-43355]. That matters for slice purposes because it shows that later DEV_NOTES does not merely tolerate the row's outcome; it actively uses `*wégaz -> weġ` as a regression sentinel.

### DEV_NOTES:line-2621-2624

- Source heading: `OE diagnostics: mismatch closeness + diacritics (2026-01-02)`
- Source line or section hint: `lines 2621-2624`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `long_vowel_missing_probe`; `expected_wē`; `diagnostic_history`; `stale_target`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment should be preserved, but only as diagnostic history. DEV_NOTES briefly listed ``*wegăz → weġ (expected wē)`` among six remaining long-vowel misses [Germanic/docs/DEV_NOTES.md:2622-2624]. The later palatalisation canvass supersedes it, and the live TSV note now does the same by stating explicitly that `wē` is not attested as OE 'way' [Germanic/data/germanic-aligned-final.tsv:1347-1347]. The fragment is still worth keeping in the slice because it records the row's project chronology: the false `wē` expectation was not merely external speculation but an internal diagnostic stage later corrected by the handbook review.

## Superseded or diagnostic material

- The stale `expected wē` diagnosis should never again be cited as if it were row policy. It survives only as a January 2026 debugging snapshot and is directly contradicted by the later DEV_NOTES palatalisation canvass and by the live TSV note itself [Germanic/docs/DEV_NOTES.md:2621-2624,43179-43182; Germanic/data/germanic-aligned-final.tsv:1347-1347].
- Kroonen's `*wega-` is stem notation, not evidence for changing the row's `PROTO` or `PROTOFORM`. The row models the nominative-singular derivational input `*wégaz`, while Kroonen cites the wider noun stem `*wega- m. 'way, road'` with OE `weg m.` as its reflex [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29259-29262; @Kroonen2013].
- The dossier `Germanic/docs/dossiers/g-palatalisation-conditioning.md` is shared support, not a row-specific lexeme report. Its value here is nevertheless substantial because it preserves the minimal-pair formulation `weġ` vs. `wegas` and thus supplies the clearest portable explanation of why singular `weġ` is correct [Germanic/docs/dossiers/g-palatalisation-conditioning.md:55-57,455-456].
- No pilot report and no `oe_known_problems.tsv` entry were located for this lexeme. That absence is meaningful: the row is not being carried as a hidden exception, only as a normal lexeme that happened to pass through one stale diagnostic bucket [Germanic/docs/lexeme_reports/research_memos/2277-way-weġ.md:11-18,63-79].

## Open questions for later work

- Decide whether `index.tsv` should use row 2277 as a positive-control palatalisation anchor. The later DEV_NOTES material is strong enough for indexing if the project wants explicit exemplars of front-vowel + word-final `*g` [Germanic/docs/DEV_NOTES.md:43181-43182,43354-43354].
- If later editorial cleanup touches the TSV note, consider clarifying in one sentence that Kroonen's `*wega-` is stem notation while the row's actual derivational input remains nominative-singular `*wégaz`; the present note is basically sound but assumes the reader already knows that distinction [Germanic/data/germanic-aligned-final.tsv:1347-1347; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29259-29262].
- If a future final lexeme report is written, keep the normalization issue explicit: dictionary spelling `weg` and project-normalized `weġ` refer to the same OE lexeme, whereas `wē` should be mentioned only in a superseded-diagnostics paragraph [Germanic/docs/lexeme_reports/research_memos/2277-way-weġ.md:43-61].
