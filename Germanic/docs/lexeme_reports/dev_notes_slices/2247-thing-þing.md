---
row_id: 2247
concept: thing
counterpart: þing
proto: *θíngą
protoform: *θíngą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2247 thing / þing

## Current row state

- CONCEPT: `thing`
- COUNTERPART: `þing`
- PROTO: `*θíngą`
- PROTOFORM: `*θíngą`
- DERIVATION_CLASS: `regular`
- Live TSV row: row 2247 currently keeps `PROTO = PROTOFORM = *θíngą`, targets OE `þing`, and is classified as a regular derivation rather than as an exception or repaired input [Germanic/data/germanic-aligned-final.tsv:1229-1229].
- Existing row infrastructure: `coverage_audit.md` still lists row 2247 as `none` for packet, memo, and attached DEV_NOTES infrastructure, so the canonical row-based filename is the correct choice here [Germanic/docs/lexeme_reports/coverage_audit.md:391-391].
- Known-problems status: no row-specific entry was located in `oe_known_problems.tsv`, which matches the live row's regular status rather than an active exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Current implementation trace: the published derivation snapshot already returns the target without workaround — `PROTO: *θíngą`, `EXPECTED: þing`, `OUTPUTS: þing`, with the trace explicitly showing OE Heavy Syllable Nasal Apocope as the operative OE-stage change [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5193-5213].
- Comparative lexical baseline: Kroonen gives Proto-Germanic `*þinga- n. 'meeting, case, thing'` with OE `þing n. 'id.'`, which is compatible with the row's neuter singular input `*θíngą` and regular OE target [@Kroonen2013, p. 582].

## Development-note summary

No lexeme-specific mismatch dossier for `þing` survives in the live DEV_NOTES, and that absence should be stated plainly rather than padded into a fake controversy. The usable material for row 2247 is shared phonological support plus the live trace: the current project treats `*θíngą > þing` as a straightforward regular derivation, not as a repaired protoform, not as a counterpart-selection problem, and not as an unresolved exception [Germanic/data/germanic-aligned-final.tsv:1229-1229; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5193-5213].

The PROTO / PROTOFORM / COUNTERPART distinction is correspondingly simple here and should remain explicit. `PROTO = *θíngą` is the row's etymological and derivational headword; `PROTOFORM = *θíngą` is the same form because no alternate paradigm cell or stage-specific substitute has been adopted; `COUNTERPART = þing` is the ordinary OE reflex the current cascade already produces [Germanic/data/germanic-aligned-final.tsv:1229-1229]. Kroonen's dictionary entry supports the lexical equation at the stem level (`*þinga- ... OE þing`), but nothing in the current repo suggests any need to distinguish a different row-level proto input from the inherited lexeme itself [@Kroonen2013, p. 582].

The main DEV_NOTES support concerns the final vowel, not the stem consonants. The archived heavy-syllable apocope note records the project's empirical decision to delete final Proto-Germanic `*-ą` after heavy syllables, extending the better-known heavy/light split for final high vowels to the neuter singular nasal-vowel ending as a modeling inference rather than as a directly quoted handbook rule [Germanic/docs/DEV_NOTES.md:1595-1615]. DEV_NOTES is explicit about the distinction: Ringe and Taylor are quoted for the statement that short final `*i` and `*u` were lost after heavy syllables, and Hogg is cited for neuter strong nouns showing zero ending after heavy stems versus `-u` after light stems; DEV_NOTES then says that “Neither source explicitly extends this pattern to *-ą” and that the `*-ą` extension is what the model learned from the mismatch set [Germanic/docs/DEV_NOTES.md:1604-1612; @RingeTaylor2014, §6.8.1; @HoggPhonology1992, §3.3.2]. For row 2247 that is the critical project fact: `*θíngą` is treated as a heavy-stem neuter whose final nasal-vowel ending drops regularly in OE, yielding bare `þing`.

The row's shape fits that heavy-stem analysis cleanly. Elsewhere DEV_NOTES explicitly classifies stems of the `*-Vng` type as heavy, saying that a short vowel plus the `ng` cluster “yields a closed heavy syllable (*CVCC*), exactly parallel to *þing-, hring-, lang-, bend-, hand-* and the rest of the *-Vng/-Vnd/-Vnt* class” [Germanic/docs/DEV_NOTES.md:32586-32589]. That remark occurs in another lexeme's note, but it is directly reusable here because it states the precise prosodic property row 2247 depends on. The trace for row 2247 then shows the consequence in practice: once the stem is treated as heavy, OE Heavy Syllable Nasal Apocope removes final `*-ą`, and no further special repair is needed before orthographic surface `þing` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5200-5213].

The only other DEV_NOTES material worth carrying over is comparative and diagnostic rather than row-defining. In the later `nigon` / `niġon` g-palatalization dossier, Campbell's canonical examples for medial velar retention before a back vowel include both `nigon` and plural `þinga`: “Velar consonants, however, remained when there was a back vowel ... either before or after them, e.g. ... *wegas* ways, *nigon* nine, *þinga* g.p. things” [Germanic/docs/DEV_NOTES.md:43236-43240; @Campbell1959, §429]. That passage is not a derivation note for row 2247's singular target, because the singular reaches word-final `-ng` after apocope and does not present the medial `g` environment at issue. But it is still useful background for later report-writing because it shows that the project already treats the lexeme's inflected paradigm as an ordinary velar-retention case before back vowels, not as a palatalization anomaly [Germanic/docs/DEV_NOTES.md:43275-43285; @Campbell1959, §429].

The practical conclusion is conservative. Row 2247 has enough support to justify a replacement working note: live TSV confirmation, live trace confirmation, shared DEV_NOTES support for heavy-stem `*-ą` apocope, and a small amount of handbook-backed comparative context. What it does **not** have is a row-local DEV_NOTES argument, a packet, a memo, or a preserved chronology of competing fixes. This slice should therefore preserve the row as a well-behaved regular item with thin but adequate support, not inflate it into an indexed exception narrative [Germanic/docs/lexeme_reports/coverage_audit.md:391-391].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1591-1615

- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line or section hint: `lines 1591-1615`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current_with_archived_statistics`
- Issue tags: `heavy_stem`; `nasal_apocope`; `final_ą_loss`; `shared_phonology`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is the main project-history support for row 2247. DEV_NOTES says the project implemented deletion of final Proto-Germanic `*-ą` after heavy syllables and explicitly distinguishes that move from the handbook baseline: “Neither source explicitly extends this pattern to *-ą,” so the extension is presented as a modeling result rather than as a directly inherited textbook rule [Germanic/docs/DEV_NOTES.md:1604-1612]. The dated mismatch statistics are archival, but the structural claim remains live for `*θíngą > þing`: a heavy stem with final `*-ą` loses that ending in the OE cascade [Germanic/docs/DEV_NOTES.md:1595-1615; @RingeTaylor2014, §6.8.1; @HoggPhonology1992, §3.3.2].

### DEV_NOTES:line-32586-32589

- Source heading: `Heavy/light cutoff and *tang-*`
- Source line or section hint: `lines 32586-32589`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `prosodic_class`; `-Vng_stems`; `heavy_syllable`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment matters because it states the prosodic classification row 2247 needs in exactly the right terms. DEV_NOTES says that short vowel plus `ng` yields a closed heavy syllable and gives `*þing-` itself as one of the parallel type-stems [Germanic/docs/DEV_NOTES.md:32586-32589]. For `*θíngą`, that is the missing bridge between the shared apocope policy and the specific row: the lexeme belongs to the heavy `*-Vng` class, so final `*-ą` loss is expected once the project accepts the heavy-stem apocope extension.

### DEV_NOTES:line-43224-43240

- Source heading: `Scholarly conditioning of the OE *g palatalisation: source canvass`
- Source line or section hint: `lines 43224-43240`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `diagnostic_only`
- Issue tags: `paradigm_context`; `velar_retention`; `plural_þinga`
- Recommended next use: `use_if_paradigm_context_needed`
- Shared with row IDs: 2142

This fragment is only indirectly relevant, but it is worth preserving because it quotes Campbell's use of plural `þinga` as a textbook example of medial velar retention before a back vowel: “Velar consonants, however, remained when there was a back vowel ... either before or after them, e.g. ... *nigon* nine, *þinga* g.p. things” [Germanic/docs/DEV_NOTES.md:43236-43240; @Campbell1959, §429]. It should not be misread as the reason the singular row 2247 works; singular `þing` is governed primarily by heavy-stem apocope. Its value is diagnostic and paradigmatic: it shows that the same lexeme family was already being treated in DEV_NOTES as an ordinary non-palatal medial-`g` case in forms like `þinga`.

## Superseded or diagnostic material

- The archived heavy-syllable apocope note is partly superseded in presentation, but not in outcome. Its 2026-02-06 mismatch counts are historical and should not be reused as current repo statistics; what survives for row 2247 is the phonological decision that heavy-stem final `*-ą` deletes in the OE cascade [Germanic/docs/DEV_NOTES.md:1593-1603,1610-1615].
- The plural `þinga` material from the g-palatalization dossier is diagnostic only. It helps situate the lexeme's paradigm in the handbook tradition, but it is not the controlling explanation for singular `*θíngą > þing` [Germanic/docs/DEV_NOTES.md:43224-43240].
- No row-specific superseded protoform, alternate counterpart, or mismatch-repair history was located for row 2247. That absence is itself part of the row's status: this is a regular item with shared support, not a lexeme whose project history must be reconstructed from abandoned fixes.

## Open questions for later work

- If a later final lexeme report wants a firmer literature footing for the `*-ą` loss, check whether any handbook or article in the local library states heavy/light-conditioned neuter `*-ą` apocope more directly than the current DEV_NOTES inference; for now the project support is real but partly model-driven [Germanic/docs/DEV_NOTES.md:1604-1615].
- If later report work expands from the singular row to the paradigm, consider adding direct dictionary support for OE plural or oblique forms such as `þinga`, since Campbell's palatalization example shows that those forms are useful for explaining the lexeme's medial velar behavior [@Campbell1959, §429].
- If future indexing policy becomes stricter about shared-only fragments, row 2247 may still be better left unindexed unless additional row-local DEV_NOTES or memo material is created.
