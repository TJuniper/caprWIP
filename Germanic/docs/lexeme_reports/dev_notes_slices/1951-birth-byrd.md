---
row_id: 1951
concept: birth
counterpart: byrd
proto: *búrdiz
protoform: *búrdiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1951-birth-byrd.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1951-birth-byrd.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1951 birth / byrd

## Current row state

- CONCEPT: `birth`
- COUNTERPART: `byrd`
- PROTO: `*búrdiz`
- PROTOFORM: `*búrdiz`
- DERIVATION_CLASS: `regular`
- Live TSV note (abridged): Kroonen gives PGmc `*burdi-` and OE `(ġe)byrd`; the live row keeps the simplex target.

## Development-note summary

The live row is straightforward only if the comparator, the attested OE forms, and the one real project detour stay distinct. The comparative headword is Kroonen's stem-level `*burdi-`, with OE `(ge-)byrd` listed among the reflexes, but the row-specific FST input is the full nominative-style `*búrdiz`, and the live target is simplex `byrd`, not prefixed `gebyrd` [@Kroonen2013, p. 123]. The packet's compact derivation trace already shows that this input reaches `byrd` cleanly, so there is no current DEV_NOTES argument for reclassifying the row or changing the target.

The attested-OE side should not be flattened into a false either/or. Kroonen's `(ge-)byrd` makes the prefixed form part of the lexeme family, but repo-local dictionaries also attest simplex `byrd` directly. Clark Hall has `byrd ... f. birth`, and Bosworth-Toller likewise has `byrd, e; f. I. birth`, so the live row's simplex counterpart is philologically defensible rather than a convenience spelling [@ClarkHall1960, s.v. "byrd"; @BosworthToller1898, s.v. "byrd"]. Hogg also lists `byrd 'birth, burden' < beran ~ boren 'carry'` among OE deverbal feminines, which supports keeping the simplex noun visible in the derivational background even when prefixed forms are also common [@HoggPhonology1992].

At the same time, the prefixed comparator should remain explicit rather than silently discarded. Kroonen's entry gives OE `(ge-)byrd`, Bosworth-Toller has a substantial separate `ge-byrd` entry for childbirth, nativity, and lineage usage, and Campbell cites both `gebyrd` and `gebyrdu` in his discussion of the noun's declensional behavior [@Kroonen2013, p. 123; @BosworthToller1898, p. 313, s.v. "ge-byrd"; @Campbell1959, §§590, 609]. Later report prose should therefore keep the contrast visible: regular project outcome `*búrdiz -> byrd`, attested prefixed comparator `gebyrd/ġebyrd`, and current row policy "model the simplex, acknowledge the prefixed alternative in the note."

The only directly attached DEV_NOTES row fragment is not a philological reconsideration of the lemma but an archived debugging warning. In the failed naïve sweep, `*búrdiz` surfaced as `byrde` and was flagged under `final_vowel_extra`, with `byrd` as the expected outcome [DEV_NOTES:line-28172-28177]. That fragment is useful because it records the superseded detour precisely: the abandoned issue was stray final-vowel retention in one sweep, not a discovery that OE really required oblique `byrde`, not a case for prefixed `gebyrd`, and not a reason to reopen the row's `regular` status.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-28172-28177

- Source heading: `failed naïve sweep archived as a warning case`
- Source line or section hint: `lines 28172-28177`
- Fragment type: `superseded_analysis`
- Status: `superseded`
- Issue tags: `final_vowel_extra`; `old_expected_outcome`; `debug_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This archived fragment should be kept only as replacement-note chronology. It records that one naïve sweep produced `*búrdiz -> byrde` and therefore logged row 1951 under `final_vowel_extra`, with `byrd` as the intended comparator. The fragment is still worth indexing because it preserves the exact abandoned diagnosis later writers might otherwise rediscover. What it does **not** do is challenge the live lexical policy: it is a debugging note about a stale output shape, not evidence for retargeting the row to `byrde`, not evidence that the row should switch from simplex `byrd` to prefixed `gebyrd`, and not evidence for any non-regular derivation class.

## Superseded or diagnostic material

The main warning here is narrow. Row 1951 has no current DEV_NOTES debate over `byrd` versus `gebyrd`; the only attached row-specific note is the archived `byrde` bug. A separate English-sandbox note mentions `*burdiz` while discussing Modern English rhotic handling and the later `birth` reflex, but that passage is about non-OE surface modeling rather than this OE row's policy, so it should not be used as if it were a DEV_NOTES argument about the Old English lemma.

## Open questions for later work

- If the final lexeme report discusses the OE evidence, cite both simplex `byrd` and prefixed `gebyrd/ġebyrd` explicitly rather than implying that only one of them is attested.
- If the row note is ever rewritten, keep Kroonen's stem-level `*burdi-` separate from the live row input `*búrdiz`.
- If later writers mention `byrde`, label it as the stale failed-sweep output from [DEV_NOTES:line-28172-28177], not as an attested or preferred OE target.
