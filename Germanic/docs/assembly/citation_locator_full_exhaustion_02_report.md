# Citation locator full-exhaustion 02 report

## Summary

- **Broad citations before:** 154 manifest rows at FE02 start.
- **Broad citations after:** 41 live broad source occurrences after source edits, manifest resynchronization, and rebuilt compact output.
- **Rows inspected:** 89 rows (all 50 Kroonen2013/Orel2003 rows from the FE02 queue, plus 39 carryover rows revisited during status-vocabulary cleanup and original-PDF spot checks).
- **Locators added:** 28.
- **Sentences split:** 0.
- **Citations removed:** 3.
- **Rows retained broad in the live queue:** 41.
- **Rows marked `source_verified_unlocalized` in the live queue:** 15.
- **Outputs regenerated:** yes (`lexical_volume_regular_compact_alpha_01.md`, `.tex`, `.pdf`).

A large part of the apparent drop from 154 to 41 came from resynchronizing the stale remaining-manifest against the current source layer and rebuilt compact Markdown. The pass still added 28 verified locators and removed 3 unsupported citations, but it also showed that the old 154-row queue was no longer a live count of current bare-source occurrences.

## Status vocabulary cleanup

This pass removed the old FE01 carryover vocabulary from the live manifest. In particular:

- old `general_background` rows were reclassified to either `retained_broad_general_background`, `claim_not_isolated`, or `headword_not_found_after_recheck` depending on what the direct recheck actually showed;
- rows whose passage had already been directly verified in FE01, but whose available witness still lacked a safe printed page, were reclassified to `source_verified_unlocalized` rather than being left under the misleading `general_background` label;
- old `headword_not_found` rows were normalized to `headword_not_found_after_recheck`;
- old `multi_page_discussion` rows were normalized to `retained_broad_multi_page_discussion`;
- old `verified_page_candidate` rows were either converted into real locators or removed from the live queue.

The final manifest is now synchronized to the actual live bare-source occurrences in the current source layer and rebuilt compact Markdown.

## Kroonen/Orel application pass

- **Kroonen rows inspected:** 33.
- **Kroonen locators added:** 16.
- **Kroonen citations removed:** 3 (`brand`, `flask`, `lap`, where the surviving Kroonen claims no longer supported the live sentence as written).
- **Kroonen rows retained broad after recheck:** 14, chiefly because the surviving clause still needs sentence splitting (`gold`, `youth`, `wolf`) or because the remaining broad issue now lies in another source after the Kroonen clause was localized.
- **Orel rows inspected:** 17.
- **Orel locators added:** 10.
- **Orel citations removed:** 0.
- **Orel rows retained broad after recheck:** 7, chiefly because of unresolved headword recovery (`gang`, `withy`) or because the surviving sentence still compresses too much material into one clause (`world`, `span`).

## Source-by-source results

| Source | Broad rows at start | Rows inspected | Locators added | Citations removed | Live broad rows after | Remaining blockers |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Kroonen2013 | 33 | 33 | 16 | 3 | 1 | Remaining live Kroonen-led broad issues are now mostly clause-isolation problems rather than page-recovery failures. |
| Orel2003 | 17 | 17 | 10 | 0 | 2 | `withy` still lacks a recoverable entry; `world` still needs a cleaner split before localization. |
| Campbell1959 | 12 | 0 direct FE02 row pass | 0 | 0 | 2 | Surviving Campbell broad rows are handbook-sentence isolation problems, not page-recovery failures. |
| RingeTaylor2014 | 24 | 0 direct FE02 row pass | 0 | 0 | 11 | The remaining Ringe-Taylor tail is mostly discussion-level material that needs sentence splitting rather than dictionary-style page hunts. |
| BosworthToller1898 | 16 | 15 cleanup rows | 0 | 0 | 8 | Several rows are now `source_verified_unlocalized`; better paginated witnesses or stronger original-PDF recovery would be needed to finish them. |
| ClarkHall1960 | 10 | 9 cleanup/original-PDF rows | 2 | 0 | 3 | Original-PDF recovery succeeded for `hedge`; the remaining Clark Hall tail still needs additional original-PDF page recovery. |
| KlugeSeebold2011 | 14 | 14 cleanup rows | 0 | 0 | 4 | The surviving Kluge rows remain blocked by unsafe or weak page architecture in the available witness. |

## Successful recoveries

1. `breeches / brēċ` — Kroonen locator added at **p. 78**.
2. `deed / dǣd` — Orel locator added at **p. 71**.
3. `fell / fell` — Kroonen locator added at **p. 135**.
4. `hedge / heġġ` — Clark Hall locator recovered from the original PDF at **p. 152**.
5. `horn / horn` — Kroonen form note localized at **p. 259**.
6. `spar / spearra` — Orel noun and form-note clauses localized at **p. 362**.
7. `think / þenċan` — Kroonen locator added at **p. 533** after rechecking the original OCR rather than trusting the old not-found label.
8. `token / tācn` — Kroonen moved from the old cross-reference candidate to the direct entry at **p. 506**.
9. `brand / brandes` — Orel localized at **p. 53**, and the unsupported Kroonen citation was removed.
10. `follow / fylġan` — Kroonen locator added at **p. 159**.
11. `gall / ġealla` — Kroonen locator added at **p. 165**.
12. `lap / lappa` — Orel localized at **p. 236**, and the unsupported Kroonen citation was removed.
13. `fire / fȳre` — Kroonen locator added at **p. 151**.
14. `bore` imperative / 3sg — both Kroonen finite-cell rows localized at **p. 85**.
15. `tap / tæppa` — both Orel clauses localized at **p. 402**.
16. `rust / rust` — Orel locator added at **p. 308**.

## Retained broad citations

### Genuine background

- `fern / fearn` (`RingeTaylor2014`) remains broad because the current sentence uses the handbook as overall derivational framing rather than for one page-bound claim.
- `way / weġ` (`HoggPhonology1992`) remains broad for the same reason: the cited handbook functions as supporting background to a claim already anchored elsewhere.

### Source verified but unlocalized

- `lead / lǣdan` (`BosworthToller1898`) remains `source_verified_unlocalized`: the entry content is verified, but the available local witness still lacks a safely recoverable printed page.
- `still / stillan` (`KlugeSeebold2011`) remains `source_verified_unlocalized` for the same reason.
- `dill / dile` (`ClarkHall1960`) likewise remains in this bucket pending additional original-PDF page recovery.

### Multi-page discussion

- `laugh / hliehhan` (`RingeTaylor2014`) remains `retained_broad_multi_page_discussion` because the surviving handbook citation summarizes a distributed comparative discussion rather than one isolatable page.

### Human-review problem

- `meed / meorde` (`RingeTaylor2014`; `Fulk2018`) remains `human_review_needed`: the remaining issue is analytical policy, not source lookup.

### Source still unsafe or not recovered

- `withy / wīþiġ` (`Orel2003`) remains `headword_not_found_after_recheck`; the local Orel witness still does not recover a dependable entry.

## Source-preparation failures

- **Bosworth-Toller**: a better paginated witness, or a more reliable OCR layer from the original PDF, is still needed for rows such as `lead`, `light`, `coat`, and `yarn`.
- **Clark Hall**: the original PDF helped for `hedge`, but further original-PDF page recovery is still needed for `dill`, `fast`, and `live`.
- **Kluge-Seebold**: the current local witness still lacks trustworthy page architecture for `still`, `will`, `lap`, and `thistle`.
- **Orel2003**: `withy` still needs either a better local witness or an alternate scanned witness.

## Human-review cases

- `CLMM01-0340` — `meed / meorde` (`RingeTaylor2014`): the remaining question is analytical policy, not locator recovery.
- `CLMM01-0341` — `meed / meorde` (`Fulk2018`): same blocker; this needs a comparator-policy decision rather than more source lookup.

## Safety checks

- No OCR line numbers were used as locators.
- No file offsets were used as locators.
- No search-result positions were used as locators.
- No unverified PDF image indexes were cited as printed pages.
- No invented page ranges were introduced.
- Every new locator added in FE02 has a matching row in `citation_locator_primary_source_evidence.tsv`.
- The rebuilt `lexical_volume_regular_compact_alpha_01.md` and the rewritten `citation_locator_remaining_master.tsv` now agree on the live broad-source count (**41**).

## Recommendation

**B. Do focused external-source research for listed blockers.**

The current live queue is no longer dominated by easy Kroonen/Orel dictionary pages. After this pass, the remaining blockers are mostly: (1) better paginated Bosworth-Toller / Clark Hall / Kluge witnesses, (2) a small Orel not-found tail such as `withy`, and (3) sentence-isolation work in handbook-style rows such as `RingeTaylor2014` and `Campbell1959`.
