---
row_id: 2269
concept: warp
counterpart: wearp
proto: "*wárpą"
protoform: "*wárpą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2269 warp / wearp

## Current row state

- The live OE row currently reads `CONCEPT = warp`, `COUNTERPART = wearp`, `PROTO = *wárpą`, `PROTOFORM = *wárpą`, and `DERIVATION_CLASS = regular`. The row has no live TSV note, and its source-note field is only duplicated `Wiktionary etymology (template:inh)` provenance [Germanic/data/germanic-aligned-final.tsv:1316-1316].
- `PROTO` and `PROTOFORM` are identical in the current TSV, but they still need to be kept conceptually separate. `PROTO` is the comparative/project proto label for this short-form lexeme; `PROTOFORM` is the OE-facing derivational input the cascade consumes; `COUNTERPART` is the attested OE output `wearp` [Germanic/data/germanic-aligned-final.tsv:1316-1316].
- That distinction matters because the immediately adjacent row is a different lexeme slice: row `2270` keeps `PROTO = PROTOFORM = *wérpaną` and `COUNTERPART = weorpan`, with an explicit note that the infinitive row must be kept apart from `wearp` [Germanic/data/germanic-aligned-final.tsv:1318-1318]. This file therefore documents the short form `wearp`, not the infinitive `weorpan`.
- Repo-local lexical support is real but semantically mixed. `old_english_wiktionary.tsv` gives only the bare aligned pair `warp -> wearp` [Germanic/data/old_english_wiktionary.tsv:328-328], while Clark Hall is more precise: `wearp` is both the noun `'warp,' threads stretched lengthwise in a loom` and `pret. 3 sg. of weorpan` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47433-47435; @ClarkHall1960, s.v. "wearp"].
- The published derivation trace already reaches the target without a repair note: `PROTO: *wárpą`, `EXPECTED: wearp`, `OUTPUTS: wearp`, with `Anglo Frisian Brightening: *wærpą`, `OE Breaking: *wearpą`, and `OE Heavy Syllable Nasal Apocope: *wearp` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5540-5559].
- No row-specific packet, research memo, or pilot file was found for row `2269`. The only obvious nearby support files are for adjacent row `2270` (`warp / weorpan`), so they should not be treated as if they were direct documentation for the present `wearp` row.

## Detailed development-note summary

The surviving DEV_NOTES record for `wearp` is usable, but it is thinner and more mixed than the record for many note-bearing rows. No dedicated `warp / wearp` memorandum survives in `Germanic/docs/DEV_NOTES.md`. The strongest directly attachable anchor is a **shared audit table**, not a row-local essay: DEV_NOTES lists `| 2271 | *wárpą | wearp | breaking |` inside a larger inventory of `*-aCl-*` and `*-aCr-*` rows [Germanic/docs/DEV_NOTES.md:30628-30638]. That table is clearly relevant by lexeme, but it also shows obvious row-number drift, since the live TSV row is now `2269`, not `2271` [Germanic/data/germanic-aligned-final.tsv:1316-1316]. Any later use of that anchor therefore needs to cite the lexical content, not trust the historical row number blindly.

Even with that caveat, the current project reading is fairly coherent. The inventory classification `breaking` matches the live derivation trace exactly: the row starts from short-form `*wárpą`, not infinitival `*wérpaną`; Anglo-Frisian brightening gives `*wærpą`; OE breaking yields `*wearpą`; and heavy-syllable apocope removes the final nasal vowel, giving surface `wearp` [Germanic/docs/DEV_NOTES.md:30636-30636; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5540-5559]. In other words, the present row is not being rescued by an analogical substitute, a patched `PROTOFORM`, or a hidden paradigm-cell remap. The live TSV's `PROTO = PROTOFORM = *wárpą` is consistent with the current derivation machinery [Germanic/data/germanic-aligned-final.tsv:1316-1316].

The main philological complication is not the sound law but the **lexeme boundary**. `wearp` is genuinely ambiguous in OE reference works: Clark Hall explicitly gives both noun and verbal-preterite values under the same spelling [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47433-47435; @ClarkHall1960, s.v. "wearp"]. Bright's paradigm table likewise confirms that the same strong-verb paradigm includes `weorpan, wearp, wurpon, worpen` [docs/references/bright_anglo_saxon_reader.txt:2506-2507]. Ringe-Taylor makes the split even clearer at the reconstruction level: `PGmc *warp ' (s)he threw' ... > OE wearp`, while `PGmc *werpana 'to throw' ... > OE weorpan` [docs/references/ringe_taylor_linguistic_history_vol2.txt:10454-10455,10573-10574; @RingeTaylor2014]. This slice should therefore preserve a strict distinction among the three fields: `PROTO = *wárpą` and `PROTOFORM = *wárpą` belong to the **short-form** row, whereas `COUNTERPART = wearp` is the attested OE surface form that can function as a noun or as the 3sg preterite of `weorpan`.

That field distinction is especially important because adjacent row `2270` could easily be collapsed into this one if the spelling alone is followed. The project has already chosen not to do that: row `2270` keeps the infinitive `weorpan` under `*wérpaną`, while the present row keeps `wearp` under `*wárpą` [Germanic/data/germanic-aligned-final.tsv:1316-1318]. Nothing in the surviving DEV_NOTES material overturns that split. On the contrary, the row's thin DEV_NOTES record and the handbook evidence both point toward a conservative interpretation: keep `wearp` as the short-form row, keep `weorpan` as the infinitive row, and do not let later dialectal `warp/uarp` spellings or late-West-Saxon analogical background blur the boundary.

The remaining DEV_NOTES quotation involving `wearp` is best read as **background**, not as row policy. In a Campbell quotation about metathesis and later analogy, DEV_NOTES preserves the footnote sentence: `lW-S past tenses *bearn, earn* are due to late analogy of *wearp*, &c.` [Germanic/docs/DEV_NOTES.md:4890-4894; @Campbell1959, §155 n. 3]. That is worth retaining because it shows that `wearp` was salient enough in the grammatical tradition to act as an analogical model for other preterites. But it is not a development note saying that this row needs repair, retargeting, or reclassification. The row remains best described as a regular breaking-and-apocope outcome whose documentary complication is lexical ambiguity, not phonological failure.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-30628-30638

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `lines 30628-30638`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current_but_row_number_stale`
- Issue tags: `breaking`; `row_number_drift`; `wearp_vs_weorpan`; `shared_inventory`
- Recommended next use: `weak_index_anchor_if_any`
- Shared with row IDs: `2166`; `2167`; `2204`; `2272`; `2289`; others in the same audit

This is the main DEV_NOTES anchor that actually names the lexeme. The decisive line is `| 2271 | *wárpą | wearp | breaking |` [Germanic/docs/DEV_NOTES.md:30636-30636]. For present purposes it establishes that the project treated `wearp` as a regular **breaking-conditioned** outcome of `*wárpą`, not as a separate exception requiring analogical rescue. But the fragment also has a real limitation: the row number is stale relative to the current TSV's `2269`, so the line is best used as a lexical-content anchor rather than as a fully trustworthy row-ID anchor [Germanic/data/germanic-aligned-final.tsv:1316-1316]. It is therefore useful, but only cautiously, for future indexing.

### DEV_NOTES:line-4882-4894

- Source heading: `Campbell quotation on metathesis of r and late analogy`
- Source line or section hint: `lines 4882-4894`
- Fragment type: `source_preserving_background_quote`
- Status: `diagnostic_only`
- Issue tags: `wearp_as_analogical_model`; `late_ws`; `preterite_background`; `campbell_quote`
- Recommended next use: `quote_only_if_preterite_background_is_needed`
- Shared with row IDs: `2161`; `2270`; other `r`-metathesis / preterite-background discussions

This fragment preserves the most direct surviving DEV_NOTES quotation that mentions `wearp` outside the shared inventory. DEV_NOTES quotes Campbell's footnote: `lW-S past tenses *bearn, earn* are due to late analogy of *wearp*, &c. (based on the pl. *burnon, wurdon*)` [Germanic/docs/DEV_NOTES.md:4890-4894; @Campbell1959, §155 n. 3]. The value of the fragment is limited but real. It confirms that `wearp` was understood as a strong preterite model in OE grammatical history. What it does **not** do is redefine the current row's `COUNTERPART`, separate the noun from the preterite sense, or provide a fresh reason to change `PROTOFORM`.

### DEV_NOTES:line-33887-33901

- Source heading: `§17.21.10.2 Does breaking apply across /st/ + r?`
- Source line or section hint: `lines 33887-33901`
- Fragment type: `shared_phonology_background`
- Status: `current_but_indirect`
- Issue tags: `breaking`; `r_plus_c`; `adjacent_weorpan_example`; `campbell_hogg_background`
- Recommended next use: `cite_only_for_phonology_not_for_row_identity`
- Shared with row IDs: `2192`; `2270`; other breaking rows

This fragment does not name `wearp`, but it is still useful background for the row's phonology. DEV_NOTES summarizes Hogg and Campbell by saying that breaking applies before `/r/ + C`, with `*weorpan 'throw'` among the canonical examples [Germanic/docs/DEV_NOTES.md:33889-33899; @HoggPhonology1992, §§5.85ff; @Campbell1959, §§128-141]. That supports the phonological side of the live trace `*wærpą -> *wearpą -> wearp` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5551-5559]. But it remains indirect support only. The fragment concerns general breaking conditions and uses the infinitive `weorpan` as its illustrative lexeme, so it should not be cited as if it solved the separate row-identity question between `*wárpą / wearp` and `*wérpaną / weorpan`.

## Superseded or diagnostic material

- The most useful non-DEV_NOTES diagnostic file is the apocope investigation, which records the old failure state `*warpą -> wearpa (exp. wearp)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:296-299]. That passage should be preserved only as debugging history. Its value is that it confirms the project expected `wearp` all along; it does **not** support restoring `wearpa` or treating final `-a` as a real rival counterpart.
- Dialectal `warp`-type spellings should stay visible, but only under a diagnostic or variant label. `ws_vs_anglian_dialect_differences.md` cites `uarp warp` for the Franks Casket/Bewcastle material [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:751-751], and Ringe-Taylor likewise notes Northumbrian `warp, gewarp ...` beside expected `ear` forms [docs/references/ringe_taylor_linguistic_history_vol2.txt:10531-10535; @RingeTaylor2014]. That material is relevant to later dialect history, not to the normalized live `COUNTERPART = wearp`.
- The duplicated Wiktionary etymology source note in the TSV should not be mistaken for the row's full evidentiary basis. The stronger support for this slice comes from the derivation trace, Clark Hall's lexical split, Bright's paradigm, and the shared DEV_NOTES breaking inventory [Germanic/data/germanic-aligned-final.tsv:1316-1316; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5540-5559; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47433-47435; docs/references/bright_anglo_saxon_reader.txt:2506-2507].

## Open questions for later work

- If a full lexeme report is ever written, decide whether the English concept label `warp` should be glossed explicitly as the noun sense while still acknowledging that the same OE spelling also serves as the 3sg preterite of `weorpan` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47433-47435; docs/references/bright_anglo_saxon_reader.txt:2506-2507]. The current row tolerates that ambiguity, but a fuller report would probably need to spell it out.
- If `dev_notes_slices/index.tsv` is ever updated, the only plausible anchor is the shared breaking inventory at `30628-30638`, especially line `30636`; however, the stale row number means this is not a clean index anchor. The Campbell footnote at `4882-4894` is useful background but not strong enough as a primary index anchor.
- If later documentation revisits the `PROTO` / `PROTOFORM` distinction for this lexeme, keep the present separation sharp even though the strings coincide. `*wárpą` is the live short-form input for this row; `*wérpaną` belongs to the adjacent infinitive row; neither should be silently substituted for the other just because both ultimately relate to OE `weorpan` / `wearp` material [Germanic/data/germanic-aligned-final.tsv:1316-1318; docs/references/ringe_taylor_linguistic_history_vol2.txt:10454-10455,10573-10574].
