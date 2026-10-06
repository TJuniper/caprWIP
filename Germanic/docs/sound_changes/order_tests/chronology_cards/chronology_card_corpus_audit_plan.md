# Chronology card corpus audit plan

## 1. Ordinary chronology-card corpus

For this audit, the **ordinary chronology-card corpus** means the sound-change card files under:

`Germanic/docs/sound_changes/order_tests/chronology_cards/`

The corpus boundary should be defined conservatively as:

1. include markdown files in that directory whose filenames begin with `SC`;
2. exclude non-card documentation in the same directory such as:
   - `README.md`
   - `chronology_card_consolidation_report.md`
   - `chronology_card_quality_audit.md`

Using that rule, the current ordinary chronology-card corpus contains **70** card files.

Current card files:

```text
SC014-nwgmc-unstressed-ai-monophthongization.md
SC015-nwgmc-i-lowering.md
SC016-oe-ws-palatal-glide.md
SC017-nwgmc-u-lowering.md
SC018-nwgmc-stressed-monosyllable-o-raising.md
SC019-nwgmc-final-long-o-raising.md
SC020-pgmc-final-z-deletion.md
SC021-nwgmc-unstressed-o-raising.md
SC022-nwgmc-mn-dissimilation.md
SC023-nwgmc-n-stem-n-loss.md
SC024-nwgmc-long-e-lowering.md
SC025-nwgmc-long-e-nasal-rounding.md
SC026-nwgmc-nasal-spirant-lengthening.md
SC027-nwgmc-nasal-spirant-loss.md
SC028-nwgmc-preconsonantal-x-loss.md
SC029-oe-awj-glide-formation.md
SC030-oe-au-fronting.md
SC031-oe-ww-simplification.md
SC032-oe-diphthong-leveling.md
SC033-oe-ew-long-diphthong.md
SC034-oe-aw-long-diphthong.md
SC035-oe-prefix-a-reduction-early.md
SC036-oe-inter-stress-raising.md
SC037-oe-compound-linking-syncope.md
SC039-oe-wi-combinative-u-umlaut.md
SC040-oe-med-unstressed-u-lowering.md
SC041-pwgmc-final-bare-a-loss.md
SC042-pwgmc-surviving-bimoric-o-unrounding.md
SC043-anglo-frisian-brightening.md
SC044-oe-breaking.md
SC045-oe-velar-fricative-palatalization.md
SC046-oe-a-restoration.md
SC047-oe-heavy-syllable-nasal-apocope.md
SC048-oe-secondary-nasalization.md
SC049-pgmc-b-allophony.md
SC050-sievers-law-syncope.md
SC051-oe-sk-palatalization.md
SC052-oe-velar-palatalization.md
SC053-oe-post-velar-w-loss.md
SC054-oe-w-loss-before-i.md
SC055-oe-i-umlaut.md
SC056-oe-ws-palatal-diphthongization.md
SC057-oe-j-cluster-coalescence.md
SC058-oe-nasal-dissimilation.md
SC059-oe-back-mutation.md
SC060-oe-ws-palatal-umlaut.md
SC061-oe-weak-tail-nasal-loss.md
SC063-oe-high-vowel-apocope.md
SC064-nwgmc-in-stem-n-loss.md
SC065-oe-medial-syncope.md
SC066-oe-l-adjacent-syncope.md
SC067-oe-dental-assimilation.md
SC068-oe-preconsonantal-degemination.md
SC069-oe-early-o-shortening.md
SC070-oe-unstressed-fronting-early.md
SC071-oe-late-o-shortening.md
SC072-oe-unstressed-long-vowel-shortening.md
SC073-oe-unstressed-ae-merger.md
SC074-oe-med-unstressed-i-lowering1.md
SC075-oe-med-unstressed-i-lowering.md
SC076-oe-prefix-i-reduction.md
SC078-oe-weak-tail-reduction.md
SC079-oe-j-loss-after-heavy.md
SC080-oe-final-geminate-simplification.md
SC081-oe-j-strengthening-after-front-diphthong.md
SC082-oe-intervocalic-j-vocalization.md
SC083-oe-unstressed-ei-contraction.md
SC085-oe-h-loss.md
SC086-oe-contraction.md
SC087-oe-r-metathesis.md
```

## 2. Purpose of the audit

The purpose of the audit is to check whether the existing ordinary chronology cards function as a coherent, reliable presentation layer for the **default** first-break chronology evidence.

The audit should make it easier to distinguish:

1. strong chronology relations that may be suitable for later graph/export use;
2. broader, farther, weaker, negative, reciprocal, technical, runner-limited, or supplementary evidence that is still valuable but should not be promoted automatically.

This is a presentation-layer audit, not a new computation phase.

## 3. Expected card schema

The ordinary cards are expected to use a stable structure built around these sections and fields:

1. title
2. `## Position at experiment time`
3. `## Earlier boundary`
4. `## Later boundary`
5. `## Chronology statement`
6. `## Caveats`
7. `## Source files`
8. optional supplementary notes

Within that structure, the audit should check for consistent use of fields such as:

1. `current_order`
2. `rule_name`
3. `safe computational window`
4. `status`
5. earlier/later break or boundary description
6. crossed stage
7. crossed stage type
8. failure count
9. representative failures
10. concrete failure example
11. interpretation

The only currently expected expanded-profile supplementary notes are the `## Expanded-PWGmc supplementary note` sections on:

1. `SC031-oe-ww-simplification.md`
2. `SC033-oe-ew-long-diphthong.md`

The audit should treat any other supplementary-note pattern as something to review, not as an automatically valid feature.

## 4. Evidence categories for later audit

The later audit should assign descriptive labels to card evidence without rewriting the cards automatically.

Suggested audit labels:

1. `local historical boundary`
2. `broad/far historical boundary`
3. `no-break boundary`
4. `non-historical / runner-limited boundary`
5. `reciprocal relation`
6. `supplementary expanded-profile note`
7. `missing or unclear evidence`
8. `possible graph candidate`
9. `not graph-worthy without further review`

These are **audit labels only**. They are not automatic edits, and they should not be treated as implicit approval to revise prose, cards, TSVs, or graphs.

## 5. Proposed later non-destructive audit TSV

Do **not** create this TSV in the current task. When the audit moves to a structured review phase, a later non-destructive TSV could use these columns:

1. `card_file`
2. `change_id`
3. `rule_name`
4. `current_order`
5. `status`
6. `earlier_boundary_present`
7. `earlier_boundary_type`
8. `earlier_crossed_stage`
9. `earlier_failure_count`
10. `earlier_representative_failures`
11. `later_boundary_present`
12. `later_boundary_type`
13. `later_crossed_stage`
14. `later_failure_count`
15. `later_representative_failures`
16. `reciprocal_relation_present`
17. `broad_far_warning_present`
18. `runner_limited_warning_present`
19. `expanded_pwgmc_note_present`
20. `source_files_present`
21. `graph_candidate`
22. `needs_review`
23. `notes`

That TSV should be read as a reporting layer over existing card text, not as a replacement for the cards or their source evidence.

## 6. Recommended audit sequence

The first audit pass should be inspection-only. It should report what the current ordinary card corpus contains, but it should not edit cards.

Suggested phases:

1. **Phase 1:** create the audit plan.
2. **Phase 2:** generate a non-destructive audit TSV from existing card text.
3. **Phase 3:** review broad/far, runner-limited, missing-field, and unclear cases.
4. **Phase 4:** decide graph/export policy.
5. **Phase 5:** only then revise cards or graph exports in small controlled batches.

This sequence keeps reporting, interpretation, policy, and editing separate.

## 7. Conservative scope rules

This audit plan is intentionally conservative.

At this stage:

1. no expanded-PWGmc computation should continue;
2. no later-direction expanded-profile tests should begin;
3. no bulk rewriting of ordinary cards should occur;
4. no default TSV replacement should occur;
5. no graph/export regeneration should occur;
6. no strengthened no-break-to-`SC004` evidence should be imported into ordinary cards at this stage.

The ordinary-card corpus should be stabilized as a presentation layer first. Only after that review should the project decide what deserves graph/export treatment.

## 8. Validation standard for this task

This task should remain documentation-only.

Validation should confirm:

1. the only repository change is `chronology_card_corpus_audit_plan.md`;
2. no generated TSVs were created or modified;
3. no graph/export files were created or modified;
4. no binaries, logs, or PDFs were created or modified;
5. no chronology-card content files were edited.
