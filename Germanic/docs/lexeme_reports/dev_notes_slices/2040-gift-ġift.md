---
row_id: 2040
concept: gift
counterpart: ġift
proto: *géftiz
protoform: *géftiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt
current_status: historical_superseded
needs_literature_agent: no
---

# DEV_NOTES material — 2040 gift / ġift

This slice is retained as historical project evidence, not current row policy.
The approved SC056 adjudication supersedes its gift/sheath chronology argument
and selected e-input. Current source discussion is
`Germanic/docs/lexeme_reports/model_entries/2040-gift-ġift.model.md`;
the live input is now `*gíftiz`. The archival quotations below are unchanged.

## Current row state

- The live OE row currently reads `CONCEPT = gift`, `COUNTERPART = ġift`, `PROTO = *géftiz`, `PROTOFORM = *géftiz`, `DERIVATION_CLASS = regular`; the row note still cites only a generic Wiktionary etymology source, so the slice needs to preserve the stronger DEV_NOTES rationale explicitly rather than relying on the TSV note alone [Germanic/data/germanic-aligned-final.tsv:426-426].
- `PROTO` and `PROTOFORM` are identical here. The current row is therefore not using a special OE-facing substitute input or an analogical repair protoform; the same reconstructed `*géftiz` is both the comparative label and the derivational input for the regular OE target `ġift` [Germanic/data/germanic-aligned-final.tsv:426-426].
- The coverage audit now treats row `2040` as a settled regular row with no linked packet, no linked research memo, and issue status `none`; `oe_known_problems.tsv` likewise has no surviving entry for `gift`, `ġift`, or `*géftiz` [Germanic/docs/lexeme_reports/coverage_audit.md:256-256; Germanic/data/oe_known_problems.tsv:1-8].
- `report_manifest.tsv` is present, but row `2040` has no manifest entry there either; the manifest currently lists only pilot or exceptional report rows, which is consistent with `gift / ġift` no longer being tracked as an open reporting case [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- The current published derivation trace matches the live row exactly: `PROTO: *géftiz`, `EXPECTED: ġift`, `OUTPUTS: ġift`, with the relevant OE stages shown as `OE Velar Palatalization: *ʤéfti`, `OE I Umlaut: *ʤifti`, `OE High Vowel Apocope: *ʤift`, and orthographic outcome `ġift` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1724-1744].

## Development-note summary

Row `2040` does have dedicated DEV_NOTES material, and it is more than a generic comparator note. The surviving row-specific dossier is explicitly about whether regular `*geftiz/*géftiz` should yield `ġift` or `ġieft`. Its central claim is that the `*-iz` suffix is an actual i-umlaut trigger, so the root vowel is raised from `*e` to `*i` before West Saxon palatal diphthongization ever has a chance to act. DEV_NOTES states the point in unusually strong terms: “**i-umlaut of *e → *i is a Proto-Germanic phenomenon**,” not a late OE event, so for `*geftiz` the chronology is `*geftiz > *giftiz`, then initial palatalization, and then “WS palatal diphthongization: `*e → *ie` — **DOES NOT APPLY** (no `*e` present)” [Germanic/docs/DEV_NOTES.md:6476-6495]. That is the main substantive reason the live row now keeps `COUNTERPART = ġift` [Germanic/data/germanic-aligned-final.tsv:426-426].

The same DEV_NOTES block also preserves the attestation and variant-spelling cautions that the replacement slice needs to keep. On the regular-outcome side, DEV_NOTES quotes Orel's “**OE ift** 'gift, marriage gift',” Kluge-Seebold's “**ae. gift f.**,” Campbell's example list “**gift** gift ... `gefan (W-S giefan) give`,” and Campbell's Kentish compound `giftelic`; together those quotations support a short-vowel `gift/ift` outcome and make clear why `gift` and `giefan` must not be collapsed into one vocalic history [Germanic/docs/DEV_NOTES.md:6506-6529]. On the cautionary side, DEV_NOTES also preserves Bright's glossary form “**gyft (gift, gieft)**” and Sweet's `gieft-` forms, while immediately warning that Sweet's spelling was made “**rigorously uniform** throughout on an early West-Saxon basis,” i.e. normalized editorial West Saxon rather than straightforward diplomatic evidence [Germanic/docs/DEV_NOTES.md:6535-6559]. The conservative takeaway is therefore not that `gieft` is impossible, but that DEV_NOTES treats it as a variant, probably analogical or editorially normalized form, whereas `ġift` is the inherited and project-relevant regular outcome [Germanic/docs/DEV_NOTES.md:6556-6569,11331-11357].

Project history matters here because row `2040` briefly sat on the wrong side of a real chronology repair. When `OEIUmlaut` was moved before `OEWsPalatalDiphthongization` to fix `sċēaþ`, the grammar began outputting `ġift`; at that moment the TSV still expected `ġieft`, so DEV_NOTES first recorded `gift` as the new trade-off and only later issued a correction reversing the earlier `ġieft` idea [Germanic/docs/DEV_NOTES.md:11272-11303,11305-11359]. The important present-tense conclusion is that the later correction is not merely a preference note: it explicitly says that because the FST models regular sound change rather than analogical leveling, “the target should be the phonologically regular form `ġift`,” and the current published trace now agrees [Germanic/docs/DEV_NOTES.md:11348-11357; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1724-1744].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6476-6569

- Source heading: `Why ġift, NOT ġieft: I-Umlaut Chronology` / `Attestation Evidence` / `The Variant Spelling gieft` / `Resolution`
- Source line or section hint: `lines 6476-6569`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `i_umlaut`; `ws_palatal_diphthongization`; `regular_outcome`; `variant_spelling`; `attestation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2041`

This is the controlling row-specific DEV_NOTES fragment. It opens with the thesis sentence that “**i-umlaut of *e → *i is a Proto-Germanic phenomenon**,” then spells out the derivation `PGmc *geftiz` → “**I-umlaut: *e → *i**” → `PWGmc *giftiz` → palatalized `g` → no West Saxon palatal diphthongization because there is “**no `*e` present**” [Germanic/docs/DEV_NOTES.md:6478-6495]. The contrast with `*gebaną → giefan` is built into the same fragment and should be preserved in any later report, because it explains why two words with initial palatal `g` diverge: `giefan` keeps `e` long enough for West Saxon diphthongization, while `gift` loses that `e` to i-umlaut first [Germanic/docs/DEV_NOTES.md:6496-6504].

The attestation material inside the same block is equally important. DEV_NOTES preserves Orel's “**OE ift**,” Kluge-Seebold's “**ae. gift f.**,” and Campbell's “**gift** gift ... `gefan (W-S giefan) give`,” all of which point to `gift/ift` as the ordinary inherited reflex rather than to `gieft` as the default lexeme form [Germanic/docs/DEV_NOTES.md:6508-6521]. It then preserves the caution that `gieft` does surface in later scholarship, but only with interpretive warnings: Bright gives “**gyft (gift, gieft)**,” and Sweet prints `giefta`, `gieftum`, `gieft-hūs`, `gieft-līc` while also admitting that his spellings were made “**rigorously uniform** throughout on an early West-Saxon basis” [Germanic/docs/DEV_NOTES.md:6537-6547]. The fragment's own interpretation is therefore the safest one to retain: `gieft` may exist as a variant or analogical/editorially normalized West Saxon form, but for a regular-sound-change FST row the target should remain `ġift` [Germanic/docs/DEV_NOTES.md:6554-6569].

### DEV_NOTES:line-11305-11359

- Source heading: `Correction: *geftiz → ġift, not ġieft (2026-03-17)`
- Source line or section hint: `lines 11305-11359`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_target_correction`; `i_umlaut_ordering`; `analogy_vs_regularity`; `project_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2041, 2178`

This later correction is the clearest current policy statement for row `2040`. DEV_NOTES re-presents the contrastive chronology in rule-order form: “**Without i-umlaut trigger** (e.g., `*gebaną`) ... `WS palatal diphthongization: *e → *ie after ġ`,” but “**With i-umlaut trigger** (e.g., `*geftiz`) ... `i-umlaut: *e → *i` ... `WS palatal diphthongization: no effect`,” with the stated result “`ġift` with simple i” [Germanic/docs/DEV_NOTES.md:11309-11323]. It then anchors that chronology to the already repaired `sċēaþ` case: “This chronology is confirmed by the `*skaiθiz → sċēaþ` case documented above,” because that row only works if i-umlaut already applied before West Saxon palatal diphthongization [Germanic/docs/DEV_NOTES.md:11324-11329].

The correction is also careful about what is and is not secure. DEV_NOTES says that “Both forms exist in the historical record,” gives `gift` as Anglian/Kentish and “presumably `gieft`” for West Saxon, and immediately adds that the West Saxon form, “if it existed, would be analogical” to `giefan`/`giefu` rather than the regular phonological outcome [Germanic/docs/DEV_NOTES.md:11331-11339]. The decisive project-policy sentence follows from that caution: “Since our FST models regular sound changes (not analogical leveling), the target should be the phonologically regular form `ġift`, not the potentially analogical WS form `ġieft`” [Germanic/docs/DEV_NOTES.md:11348-11352]. That is the sentence that most directly justifies the live row as currently stored [Germanic/data/germanic-aligned-final.tsv:426-426].

### DEV_NOTES:line-11272-11303

- Source heading: `Implementation Result (2026-03-17)`
- Source line or section hint: `lines 11272-11303`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `intermediate_policy`; `trade_off`; `pre_correction_state`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2178`

This fragment should be preserved because it records the intermediate state that made row `2040` look problematic again. After moving `OEIUmlaut` before `OEWsPalatalDiphthongization`, DEV_NOTES recorded the successful `sċēaþ` repair and then noted a new mismatch: “`*geftiz → ġift` (expected `ġieft` per TSV)” [Germanic/docs/DEV_NOTES.md:11272-11282]. The note is valuable because it shows the decision point honestly: keep the reorder because the `sċēaþ` fix is source-backed, but mark `gift` for further etymological checking rather than immediately assuming the FST had become wrong [Germanic/docs/DEV_NOTES.md:11283-11303].

As row-local policy, however, this block is superseded by the later correction. Its uncertainty survives in the old debug snapshot from 2026-03-11, which still shows `EXPECTED: ġieft`, `OUTPUTS: ġieft`, and the obsolete rule order where `WsPalatalDiphthongization` created `*ʤiefti` before `IUmlaut` left that diphthong untouched [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:5173-5208]. That older trace is useful evidence for how the row used to be modeled, but it should now be cited only as bug-history context, not as authority for the current target [Germanic/docs/DEV_NOTES.md:11305-11357; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1724-1744].

## Superseded or diagnostic material

- The pre-correction March 2026 state should not be discarded entirely. It explains why `ġieft` ever entered the row at all: with West Saxon palatal diphthongization placed before i-umlaut, the grammar mechanically produced `*ʤiefti > ġieft`, and the old trace snapshot records exactly that path [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:5173-5208]. What is superseded is not the existence of that older derivation, but its use as current row policy.
- DEV_NOTES `11272-11303` is likewise diagnostic rather than current. It accurately records the trade-off discovered when `sċēaþ` was fixed, but it still speaks from the moment before the project had decided whether `ġift` or `ġieft` was the right target [Germanic/docs/DEV_NOTES.md:11272-11303]. The later correction at `11305-11359` is the operative row-level conclusion.
- The live note should therefore preserve a distinction among three things: (1) the regular inherited outcome `ġift`, which is the current row target; (2) the historically or editorially visible variant `gift/gyft/gieft`, which DEV_NOTES discusses but does not install as the row's default; and (3) the obsolete internal project state where `ġieft` was temporarily treated as expected before the chronology was corrected [Germanic/docs/DEV_NOTES.md:6535-6569,11331-11357].

## Open questions for later work

- If a packet or final report is later written, decide whether the prose should cite headwords as plain `gift`/`gyft` and then explain project-normalized `ġift`, or whether normalized dotted `ġ-` should be used throughout with a short orthographic note [Germanic/docs/DEV_NOTES.md:6516-6521; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1741-1744].
- If `gieft` is mentioned at all, keep the wording conservative: DEV_NOTES only goes as far as variant/editorial or possibly analogical West Saxon status, not a secure claim that `gieft` is the ordinary inherited reflex for this row [Germanic/docs/DEV_NOTES.md:6537-6559,11333-11339].
- A later literature pass could still check the manuscript basis of `gieft` more directly, because this slice deliberately relies on quotations preserved in DEV_NOTES rather than on a fresh independent source audit. That would be refinement work, not a reason to unsettle the current regular-row target `ġift` [Germanic/docs/DEV_NOTES.md:6556-6569,11348-11357].
