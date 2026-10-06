---
row_id: 2229
concept: stud
counterpart: stōd
proto: *stōdą
protoform: *stōdą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2229 stud / stōd

## Current row state

- The live OE row has `CONCEPT = stud`, `PROTO = *stōdą`, `PROTOFORM = *stōdą`, `COUNTERPART = stōd`, and `DERIVATION_CLASS = regular`; the row carries only duplicated imported provenance strings rather than a project-authored lexical note [Germanic/data/germanic-aligned-final.tsv:1160-1160].
- `PROTO` and `PROTOFORM` currently coincide, but comparative sources cite the same lexeme in different lemma shapes: Kroonen gives `*stōda- n. 'flock'`, Orel gives `*stōdan sb.n.`, while the live row stores the OE-facing input as `*stōdą`. For this slice those are notation differences, not competing reconstructions [Germanic/data/germanic-aligned-final.tsv:1160-1160; @Kroonen2013, p. 481; @Orel2003, p. 379].
- The published derivation trace is an exact regular match: `PROTO: *stōdą`, `EXPECTED: stōd`, `OUTPUTS: stōd`, with the only overt OE-side step being `OE Heavy Syllable Nasal Apocope: *stōd` before surface orthography [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4888-4907].
- `oe_known_problems.tsv` has no entry for row `2229`, for `*stōdą`, or for `stōd`, so the row is not currently tracked as an OE exception or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- No packet or research memo stem was found for this row, so the canonical row-based filename `2229-stud-stōd.md` is the correct replacement working note.

## Detailed development-note summary

No dedicated `stud / stōd` dossier presently survives in `Germanic/docs/DEV_NOTES.md`. Direct row-relevant searching turns up no lexeme-specific note about the noun itself, no source dispute over the OE target, and no project-authored argument that the row needs anything beyond the regular cascade. The most important negative fact to preserve is therefore that the row is stable **without** a row-local DEV_NOTES case study behind it.

What *does* survive in DEV_NOTES is shared sound-change history for final PGmc `*-ą`, and that history is enough to explain why the live row behaves regularly. The archived 2026-02-06 note records an empirical discovery pass that extended heavy-syllable-conditioned apocope from short high vowels to final `*ą`: it explicitly says that Ringe/Taylor and Hogg describe the conditioning for `*i/*u`, that `Neither source explicitly extends this pattern to *-ą`, and that the model nevertheless found the same conditioning useful for `*-ą` [Germanic/docs/DEV_NOTES.md:1595-1615; @RingeTaylor2014, §6.8.1; @HoggPhonology1992, §3.3.2]. Row `2229` fits that older formulation neatly because `*stōd-` is a heavy stem with long `ō` plus final consonant.

Later DEV_NOTES chronology narrows the interpretive point that should now be carried forward. In the March 2026 rule-ordering work and in the later `heofon` diagnostic, DEV_NOTES treats `OEHeavySyllableNasalApocope` as the current rule `{*ą} -> 0 || OEAnyConsonant _ .#.` and contrasts `*ą` with `*ų`: `*ą` is said to be `denasalized to *a, then unconditionally lost in all positions`, whereas `*ų` still follows the heavy-syllable apocope described by Campbell [Germanic/docs/DEV_NOTES.md:10818-10820; Germanic/docs/DEV_NOTES.md:10884-10888; Germanic/docs/DEV_NOTES.md:13322-13330; @Campbell1959, §345]. For `*stōdą`, this later correction does not change the output, but it does change how the row should be described: the row no longer needs to be presented as a special empirical extension case, only as an ordinary final-`*ą` loss that happens also to occur after a heavy stem.

The comparative lexicography supports that conservative reading. Kroonen lists `*stōda- n. 'flock'` with OE `stōd n. 'stud, herd of horses'` among the reflexes [@Kroonen2013, p. 481]. Orel similarly gives `*stōdan sb.n.` with `OE stód id.` and the same herd-of-horses semantics [@Orel2003, p. 379]. Clark Hall's entry is equally plain: `stōd I. n. 'stud' (of horses)` [@ClarkHall1960, s.v. "stōd"]. Those sources back the live row well, but they do not create a richer DEV_NOTES history than the repo actually preserves.

The safest replacement note is therefore narrow. Row `2229` is a regular exact-match noun row whose usable DEV_NOTES support is shared rule-history about final `*-ą`, not a dedicated lexical memo. That is enough to preserve why the current row is credible, but still too thin for confident indexing as a row with its own substantive DEV_NOTES attachment.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:no-row-specific-hit-for-stud-stōd

- Source heading: no dedicated `stud / stōd` note survives in `DEV_NOTES.md`
- Source line or section hint: negative-result sweep; false-positive row-number collision at `line 2229`
- Fragment type: `unclear_needs_human_review`
- Status: `current_negative_result`
- Issue tags: `missing_row_specific_authority`; `shared_sound_change_only`; `do_not_overindex`
- Recommended next use: `keep_as_working_note_only`
- Shared with row IDs:

The only literal `2229` hit encountered during this pass is unrelated infrastructure text: "Next brace steps stay in the sandbox: feed `pgrmWord`, rebuild brace-aware surface filters, only then swap the finished automaton back into `server/fsts/germanic.txt`" [Germanic/docs/DEV_NOTES.md:2229-2229]. That is a line-number coincidence, not lexical evidence for `stud / stōd`, and it should be kept out of any row-level indexing decision.

### DEV_NOTES:line-1595-1623

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1595-1623`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `superseded_but_explanatory`
- Issue tags: `final_-ą`; `heavy_stem`; `shared_sound_change_history`
- Recommended next use: `cite_in_final_report_with_caution`
- Shared with row IDs:

This archived fragment is still the clearest surviving DEV_NOTES explanation for why rows like `*stōdą → stōd` stopped overproducing final `-a`. The note says that the experimental rule deleted proto `*-ą` after heavy syllables, that this was an `empirically-derived phonological finding`, and that `Neither source explicitly extends this pattern to *-ą`, even though the model found the same conditioning that governs final `*i/*u` useful for `*-ą` as well [Germanic/docs/DEV_NOTES.md:1595-1615; @RingeTaylor2014, §6.8.1; @HoggPhonology1992, §3.3.2]. For row `2229`, the fragment is historically relevant because `*stōd-` is unambiguously heavy, but later DEV_NOTES no longer treats heavy-stem conditioning as the whole story.

### DEV_NOTES:line-10818-10820

- Source heading: `The Fix`
- Source line or section hint: `lines 10818-10820`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `rule_order`; `final_-ą`; `pipeline_chronology`
- Recommended next use: `cite_in_final_report_with_caution`
- Shared with row IDs:

This later fragment states the current project rule more directly: `We already have OEHeavySyllableNasalApocope ... which does exactly what we need: {*ą} -> 0 || OEAnyConsonant _ .#.` and the required repair is to run it before `OESecondaryNasalization` [Germanic/docs/DEV_NOTES.md:10818-10820]. For `stōd`, this means the present exact-match trace depends on settled pipeline ordering, not on a row-local workaround.

### DEV_NOTES:line-13322-13330

- Source heading: `The key difference` / `Why the treatment differs`
- Source line or section hint: `lines 13322-13330`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current_but_indirect`
- Issue tags: `*ą_vs_*ų`; `final_vowel_loss`; `proto_vs_protoform`
- Recommended next use: `cite_in_final_report_with_caution`
- Shared with row IDs:

This is the clearest current prose for how the project now distinguishes final `*ą` from final `*ų`. DEV_NOTES says `OEHeavySyllableNasalApocope: {*ą} -> 0 || OEAnyConsonant _ .#.` and then explains that `*ą` is `denasalized to *a, then unconditionally lost in all positions`, while `*ų` is `denasalized to *u, then subject to heavy syllable rule (Campbell §345)` [Germanic/docs/DEV_NOTES.md:13322-13330; @Campbell1959, §345]. For row `2229`, that makes the live `PROTO`/`PROTOFORM` value `*stōdą` straightforward: the row's successful output depends on ordinary final-`*ą` loss, not on any special lexeme-specific exception handling.

## Superseded or diagnostic material

- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` preserves an older diagnostic overgeneration list that still had `*stōdą → stōda (exp. stōd)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:295-295]. That note is useful for project chronology, but it is diagnostic only; the current published trace already shows the problem resolved [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4888-4907].
- The 2026-02-06 DEV_NOTES fragment should now be treated as partially superseded in *conditioning*, not in outcome. It correctly captures why `stōd` improved, but later DEV_NOTES reframes final `*ą` loss as broader than heavy-stem contexts alone [Germanic/docs/DEV_NOTES.md:1595-1615; Germanic/docs/DEV_NOTES.md:13322-13330].
- Dictionary citation format should not be confused with live row fields. Kroonen's `*stōda-`, Orel's `*stōdan`, and the row's `*stōdą` all point to the same cognate set; the row does not preserve multiple competing protoforms just because the literature uses different citation shapes [Germanic/data/germanic-aligned-final.tsv:1160-1160; @Kroonen2013, p. 481; @Orel2003, p. 379].
- `coverage_audit.md` still records the row as uncovered regular material with no linked report infrastructure: `| 2229 | stud | stōd | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:380-380]. That is workflow diagnostics only, not source authority.

## Open questions for later work

- If later indexing wants to promote row `2229`, decide first whether shared final-`*ą` rule history is enough to justify an `index.tsv` row, or whether the lexeme should remain no-index until a packet or memo quotes the actual `*stōda- / stōd` dictionary evidence directly.
- If a later report cites the apocope history, keep the chronology explicit: the archived DEV_NOTES note framed `*stōdą` as part of a heavy-syllable discovery pass, while later DEV_NOTES treats final `*ą` loss more generally [Germanic/docs/DEV_NOTES.md:1595-1615; Germanic/docs/DEV_NOTES.md:13322-13330].
- If later report prose compares `PROTO`, `PROTOFORM`, and handbook lemma shape, keep the labels strict: live row `PROTO = PROTOFORM = *stōdą`, while comparative dictionaries often cite `*stōda-` or `*stōdan` for the same lexical family [Germanic/data/germanic-aligned-final.tsv:1160-1160; @Kroonen2013, p. 481; @Orel2003, p. 379].
