# Chronology card corpus audit report

This report summarizes the first non-destructive audit pass over the ordinary chronology-card corpus defined in `chronology_card_corpus_audit_plan.md`. The audit was derived from the current card markdown text only; no sound-change computation, card rewriting, TSV regeneration, or graph/export regeneration was performed.

## Summary

1. **Total card count:** 70
2. **All 70 expected card files found:** yes
3. **Cards missing any expected section:** 0
4. **Cards with expanded-PWGmc supplementary notes:** 2 (SC031; SC033)
5. **Graph-candidate triage counts:** yes=27, maybe=32, no=11
6. **Cards marked `needs_review=yes`:** 32

## Highest-priority review cases

1. `SC015` (`SC015-nwgmc-i-lowering.md`) - broad_far_warning; runner_limited_warning; one_sided_historical_boundary; graph_candidate_policy_review
2. `SC023` (`SC023-nwgmc-n-stem-n-loss.md`) - broad_far_warning; runner_limited_warning; one_sided_historical_boundary; graph_candidate_policy_review
3. `SC024` (`SC024-nwgmc-long-e-lowering.md`) - broad_far_warning; runner_limited_warning; one_sided_historical_boundary; graph_candidate_policy_review
4. `SC033` (`SC033-oe-ew-long-diphthong.md`) - broad_far_warning; runner_limited_warning; one_sided_historical_boundary; graph_candidate_policy_review
5. `SC069` (`SC069-oe-early-o-shortening.md`) - broad_far_warning; runner_limited_warning; one_sided_historical_boundary; graph_candidate_policy_review
6. `SC087` (`SC087-oe-r-metathesis.md`) - broad_far_warning; runner_limited_warning; one_sided_historical_boundary; graph_candidate_policy_review
7. `SC020` (`SC020-pgmc-final-z-deletion.md`) - broad_far_warning; graph_candidate_policy_review
8. `SC036` (`SC036-oe-inter-stress-raising.md`) - broad_far_warning; graph_candidate_policy_review
9. `SC040` (`SC040-oe-med-unstressed-u-lowering.md`) - broad_far_warning; graph_candidate_policy_review

Retired `SC021` is excluded from the current highest-priority review list; its
card is now archival only.

## Scope confirmation

This audit pass remained non-destructive:

1. no chronology-card files were edited;
2. no default first-break TSVs were created or modified;
3. no graph/export files were created or modified;
4. no binaries, logs, or PDFs were created or modified;
5. the new audit TSV and this report act only as a reporting/checking layer over the existing cards.

## Notes on interpretation

`graph_candidate=yes` is intentionally conservative and is used only where the card text presents clear historical boundary evidence without relying on runner-limited or no-break framing. `graph_candidate=maybe` marks broad/far cases, one-sided historical cases, and other policy-sensitive relations that need manual review before any graph/export decision.

The current audit also confirms that expanded-PWGmc supplementary notes remain limited to `SC031` and `SC033`, consistent with the present narrow integration policy.
