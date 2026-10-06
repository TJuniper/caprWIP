# Citation locator final classification review 01 report

## Scope and outcome

This pass stopped open-ended locator tightening and audited the remaining broad-citation manifest against the current assembled compact volume. The immediate correction was a manifest/Markdown synchronization issue: three stale rows remained in `citation_locator_remaining_master.tsv` even though the corresponding citations were no longer broad in `lexical_volume_regular_compact_alpha_01.md`.

After removing those stale rows and refreshing every surviving manifest row from the current assembled Markdown, the manifest and generated volume now match exactly at **161** remaining broad citation occurrences.

## Broad-citation count before and after

| Measure | Count |
| :--- | ---: |
| broad citations before review | 164 |
| stale manifest rows removed in this pass | 3 |
| new locators added in this pass | 0 |
| citations removed from prose in this pass | 0 |
| broad citations after review | 161 |

## Manifest synchronization

- The current generated Markdown was rescanned with a wrapped-span parser that treats Pandoc citation spans across physical line breaks as single citation spans.
- The refreshed manifest count is **161**.
- The current generated Markdown broad-citation count is **161**.
- No broad citation present in the generated Markdown is now missing from the manifest.
- The three stale manifest rows removed in this pass were:
  - `CLMM01-0218` — `needle / nǣdl` / `Ringe2006`
  - `CLMM01-0279` — `youth / ġeoguþ` / `Campbell1959`
  - `CLMM01-0452` — `wolf / wulf` / `SieversBrunner1965`
- No prose, bibliography, or citation-bearing source files were changed in this pass, so the compact Markdown/TeX/PDF outputs did not need regeneration.

## Rows reviewed

| Measure | Count |
| :--- | ---: |
| rows reviewed in final inventory | 161 |
| locators added | 0 |
| citations removed | 0 |
| rows reclassified to `human_review_needed` | 10 |
| rows otherwise retained with final classification | 151 |

## Reclassifications by status

The pass did not restart a locator hunt. It instead tightened the classification layer where the residual problem is analytical rather than locational.

Rows reclassified to `human_review_needed`:
- `meed / meorde`: 8 rows
- `knob / cnobba`: 2 rows

These rows are review-sensitive because the remaining difficulty lies in paradigm-cell choice, branch selection, or reconstructed-vs-attested representation, not in recoverable printed-page anchors.

## Final status distribution

| Final status | Count |
| :--- | ---: |
| general_background | 59 |
| claim_not_isolated | 36 |
| headword_not_found | 33 |
| source_quarantined | 14 |
| multi_page_discussion | 6 |
| source_preparation_needed | 3 |
| human_review_needed | 10 |

## Remaining source-preparation problems

The remaining `source_preparation_needed` tail is still small and source-specific:

- `CLMM01-0023` — `fly / flēogan` / `BosworthToller1898`: A safer local witness or better page-labeled source preparation is needed before this citation can be tightened.
- `CLMM01-0158` — `dill / dile` / `ClarkHall1960`: The current Clark Hall witness only yielded the cross-reference-style `dile = dyle`, and this pass did not recover a safe printed-page anchor for that notice.
- `CLMM01-0325` — `live / lifeþ` / `BosworthToller1898`: A safer local witness or better page-labeled source preparation is needed before this citation can be tightened.

## Remaining human-review problems

The new `human_review_needed` bucket is deliberately narrow. It captures cases where further page-chasing would not resolve the real issue without first deciding how the entry itself ought to frame the evidence.

- `CLMM01-0338` — `meed / meorde` / `Crist2002`
- `CLMM01-0340` — `meed / meorde` / `RingeTaylor2014`
- `CLMM01-0341` — `meed / meorde` / `Fulk2018`
- `CLMM01-0343` — `meed / meorde` / `Kilday2024`
- `CLMM01-0345` — `meed / meorde` / `BosworthToller1898`
- `CLMM01-0346` — `meed / meorde` / `ClarkHall1960`
- `CLMM01-0347` — `meed / meorde` / `BosworthToller1898`
- `CLMM01-0348` — `meed / meorde` / `RingeTaylor2014`
- `CLMM01-0429` — `knob / cnobba` / `Kroonen2011`
- `CLMM01-0430` — `knob / cnobba` / `BosworthToller1898`

## Examples of broad citations deliberately retained

- `fire / fȳre`: the handbook trio `[@RingeTaylor2014; @HoggPhonology1992; @Campbell1959]` still supports a bundled inherited-vs-analogical explanation, but the sentence would need artificial atomization to attach clean per-source locators.
- `wolf / wulf`: the remaining broad `[@SieversBrunner1965]` sentence is a control-form argument about hypothetical `wylf / wylfe`; it stays broad because the current sentence still combines the control-form logic with the entry-level conclusion.
- `swan / swanes`: broad comparative family framing remains intentionally broad where the source functions as background rather than as a single page-bound claim.

## Remaining source-quarantine and headword tails

- `source_quarantined` remains a distinct bucket for witnesses such as `KlugeSeebold2011` where the local source still does not provide reliable page-labeled evidence.
- `headword_not_found` remains appropriate for the residual dictionary cases where the available witness still does not show the exact entry or form needed for a safe locator.

## Evidence and method confirmation

- No new locators were added in this pass, so `citation_locator_primary_source_evidence.tsv` was unchanged.
- Every locator added in earlier passes remains backed by the existing primary-source evidence log.
- No OCR line numbers, file offsets, search-result positions, or unverified PDF page indexes were used in this review.
- The synchronization fix relied only on the current generated Markdown plus the existing manifest metadata.

## Recommendation

**A. Locator work is now complete enough for PDF review.**

The remaining tail is now a classified mixture of honest broad background citations, genuine source-preparation blocks, quarantined sources, and a small human-review subset. Another broad locator pass would likely spend effort on prose atomization or analytical policy questions rather than on clean citation recovery.
