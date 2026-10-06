# First-break batch plan 04

## Purpose

First-break testing is the computational layer that turns the runner into relative-chronology evidence for the eventual sound-change volume. Instead of exhaustively mapping every possible slot for every rule, the method finds the first earlier and later positions at which a baseline-matching Old English derivation breaks.

## Current evidence model

The workflow now has five evidence layers:

1. `order_sensitivity_first_break_pilot_03.tsv` — one row per change-direction result
2. `order_sensitivity_first_break_pilot_03_changes.tsv` — row-level changed outputs for tested variants
3. `order_sensitivity_first_break_pilot_03_failures.tsv` — only real breaks, where a previously matching row stops matching
4. `sound_change_order_sensitivity.tsv` — repo-facing summary of safe windows and failure counts
5. chronology evidence cards in `order_tests/chronology_cards/` — reusable prose-ready summaries for the book pipeline

## What counts as a boundary

A first-break boundary is a **real break**:

- baseline row matches expected = `yes`
- variant row matches expected = `no`

Changed-still-passing outputs are still recorded in the changes TSV because they often reveal nearby instability, but they do **not** stop the search. Technical or support-stage crossings must be flagged separately from historically interpretable boundaries.

## Chronology-card prose standard

Chronology cards must state the constraint in concrete derivational terms. Each boundary statement should include:

- the Proto-Germanic input;
- the expected Old English output;
- the incorrect variant output;
- the crossed rule responsible for the boundary;
- a short explanation of why the wrong form results.

Modern English glosses such as `belly` or `cow` are useful row identifiers, but they are not sufficient as chronology prose by themselves.

## Batch-driver workflow

The manifest-driven driver runs the existing first-break runner one direction at a time and records progress after each direction.

Example commands:

```bash
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/run_first_break_batch.py --dry-run'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/run_first_break_batch.py --only-status pending --limit 3 --resume'
docker compose exec -T backend sh -lc 'cd /usr/app && python3 tools/run_first_break_batch.py --manifest docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_batch_04_manifest.tsv --resume'
docker compose exec -T backend sh -lc "cd /usr/app && ls docs/sound_changes/order_tests/logs && tail -n 40 docs/sound_changes/order_tests/logs/SC055_earlier.log"
```

After a manual terminal batch completes cleanly, commit only the intended TSV / summary / chronology-card outputs.

## Eligibility limits

The current runner can test only rules that are individually named members of the parsed `EnglishProtoToOE` chain. It does **not** yet reorder inside bundled stages such as `PGmcConsonantRules` or `PWGmcChanges`.

For manifest classification:

- support stages are skipped
- technical markers are skipped
- orthography / surface stages are skipped
- non-explicit chain positions are skipped

Those stages can still matter interpretively, but they should not yet be treated as ordinary first-break targets.

## Completed first small batch

The first manual terminal batch is now complete for:

1. `SC041` PWGmc Final Bare A Loss
2. `SC042` PWGmc Surviving Bimoric O Unrounding
3. `SC044` OE Breaking

Those results have been folded into the first-break summary TSVs, the repo-facing order-sensitivity table, and dedicated chronology cards.

## Completed second batch

The next manual terminal batch is now complete for:

1. `SC046` OE A Restoration
2. `SC050` Sievers Law Syncope
3. `SC055` OE I Umlaut

Those results extend the chronology-card set into the SC043 / SC044 / SC048 restoration zone and into the SC052 / SC056 corridor around SC055. They also show that SC050 currently has an earlier runner-boundary result rather than a detected earlier historical break.

## Completed scaled batch

The scaled manual terminal batch is now complete for:

1. `SC045` OE Velar Fricative Palatalization
2. `SC047` OE Heavy Syllable Nasal Apocope
3. `SC048` OE Secondary Nasalization
4. `SC051` OE Sk Palatalization
5. `SC052` OE Velar Palatalization
6. `SC056` OE Ws Palatal Diphthongization
7. `SC059` OE Back Mutation
8. `SC072` OE Unstressed Long Vowel Shortening
9. `SC078` OE Weak Tail Reduction

These results greatly expand the chronology-card network and add several reciprocal or near-reciprocal constraints, especially SC044 / SC045, SC047 / SC048, SC052 / SC055, and SC055 / SC056.

## Consolidation / index pass

The scaled batch has now also been interpreted and folded into a consolidation pass for the chronology-card layer. This pass adds:

1. `order_tests/chronology_cards/README.md`
2. `order_tests/chronology_cards/chronology_card_index.tsv`
3. `order_tests/chronology_cards/chronology_card_consolidation_report.md`
4. `order_tests/next_batch_candidates.tsv`

The new index makes it easier to distinguish historical first-break boundaries, broad computational boundaries, and runner-bounded no-break results before these cards are reused in later chapter prose.

## Completed gap-filling batch

The gap-filling manual terminal batch is now complete for:

1. `SC049` PGmc B Allophony
2. `SC053` OE Post Velar W Loss
3. `SC054` OE W Loss Before I
4. `SC057` OE J Cluster Coalescence
5. `SC058` OE Nasal Dissimilation
6. `SC060` OE Ws Palatal Umlaut
7. `SC061` OE Weak Tail Nasal Loss
8. `SC064` NWGmc In Stem N Loss
9. `SC073` OE Unstressed AE Merger

These results fill most of the previously recommended mid / late gap set. They add several one-sided cards, two negative boundary cards (`SC053`, `SC058`), and two especially important reciprocal confirmations: `SC064` / `SC072` and `SC072` / `SC073`.

## Completed late-corridor batch

The late-corridor manual terminal batch is now complete for:

1. `SC065` OE Medial Syncope
2. `SC066` OE L Adjacent Syncope
3. `SC067` OE Dental Assimilation
4. `SC068` OE Preconsonantal Degemination
5. `SC069` OE Early O Shortening
6. `SC070` OE Unstressed Fronting Early
7. `SC071` OE Late O Shortening
8. `SC074` OE Med Unstressed I Lowering1
9. `SC075` OE Med Unstressed I Lowering
10. `SC076` OE Prefix I Reduction

These results fill the previously recommended late-corridor gap. They add three new reciprocal or near-reciprocal pairs (`SC066` / `SC068`, `SC070` / `SC071`, `SC074` / `SC075`), three fully negative boundary cards (`SC065`, `SC067`, `SC076`), and one broad/far earlier boundary (`SC069` across `SC023`) that must not be flattened into a local adjacency claim.

## Completed far-late batch

The far-late manual terminal batch is now complete for:

1. `SC079` OE J Loss After Heavy
2. `SC080` OE Final Geminate Simplification
3. `SC081` OE J Strengthening After Front Diphthong
4. `SC082` OE Intervocalic J Vocalization
5. `SC083` OE Unstressed EI Contraction
6. `SC085` OE H Loss
7. `SC086` OE Contraction
8. `SC087` OE R Metathesis

These results close the remaining explicit far-late corridor. They add four especially important reciprocal or near-reciprocal relations (`SC079` / `SC080`, `SC081` / `SC082`, `SC082` / `SC083`, `SC085` / `SC086`), and they also introduce three new broad/far earlier boundaries (`SC079` across `SC055`, `SC081` across `SC055`, `SC087` across `SC044`) plus four later search-limited outcomes (`SC080`, `SC083`, `SC086`, `SC087`) that must not be rewritten as historical adjacency claims.

## Completed upper-early batch

The upper-early manual terminal batch is now complete for:

1. `SC030` OE Au Fronting
2. `SC031` OE WW Simplification
3. `SC032` OE Diphthong Leveling
4. `SC033` OE Ew Long Diphthong
5. `SC034` OE Aw Long Diphthong
6. `SC035` OE Prefix A Reduction Early
7. `SC036` OE Inter Stress Raising
8. `SC037` OE Compound Linking Syncope
9. `SC039` OE WI Combinative U Umlaut
10. `SC040` OE Med Unstressed U Lowering

These results close the upper-early corridor immediately below the already interpreted `SC041` region. They add three especially important reciprocal or near-reciprocal relations (`SC030` / `SC032`, `SC031` / `SC034`, `SC039` / `SC040`), three new broad/far historical constraints (`SC033` later across `SC044`, `SC036` earlier across `SC019`, `SC040` later across `SC072`), and several non-historical / runner-limited outcomes (`SC031` earlier, `SC033` earlier, `SC035` earlier, `SC037` earlier, `SC037` later, `SC039` earlier) that must not be rewritten as ordinary historical adjacency claims.

## Completed lower-early batch

The lower-early manual terminal batch is now complete for:

1. `SC020` PGmc Final Z Deletion
2. `SC021` retired NWGmc Unstressed O Raising (archival only)
3. `SC022` Common Germanic Mn Dissimilation (executable holding-zone placement)
4. `SC023` Proto-Germanic Word-Final N Loss (formerly NWGmc N Stem N Loss)
5. `SC024` NWGmc Long E Lowering
6. `SC025` NWGmc Long E Nasal Rounding
7. `SC026` NWGmc Nasal Spirant Lengthening
8. `SC027` NWGmc Nasal Spirant Loss
9. `SC028` NWGmc Preconsonantal X Loss
10. `SC029` OE Awj Glide Formation

These results close the remaining explicit lower-early corridor immediately below the upper-early band. They add two especially important reciprocal or near-reciprocal relations (`SC026` / `SC027`, `SC029` / `SC030`), four broad/far historical later constraints (`SC020` later across `SC040`, `SC021` later across `SC040`, `SC023` later across `SC047`, `SC024` later across `SC056`), and three fully negative boundary cards (`SC022`, `SC025`, `SC028`). They also expand the runner-limited earlier set inside bundled `PWGmcChanges` with `SC021`, `SC022`, `SC023`, `SC024`, `SC025`, `SC026`, `SC028`, and `SC029`.

## Completed early-corridor batch

The early-corridor manual terminal batch is now complete for:

1. `SC014` NWGmc Unstressed Ai Monophthongization
2. `SC015` NWGmc I Lowering
3. `SC016` OE Ws Palatal Glide
4. `SC017` NWGmc U Lowering
5. `SC018` NWGmc Stressed Monosyllable O Raising
6. `SC019` NWGmc Final Long O Raising

These results close the remaining explicit searchable early corridor below the lower-early band. They add three especially important reciprocal or near-reciprocal relations (`SC016` / `SC017`, `SC017` / `SC019`, `SC019` / `SC020`), one broad/far one-sided later constraint (`SC015` later across `SC036`), and two fully negative boundary cards (`SC014`, `SC018`). They also extend the runner-limited earlier set inside bundled `PWGmcChanges` with `SC014`, `SC015`, `SC016`, and `SC018`.

## Remaining eligible queued / pending rules

Remaining eligible explicit-chain rules now still in `queued` / `pending` status are:

1. Early corridor: none remaining in the explicit searchable band
2. Upper-early corridor: none remaining in the explicit searchable band
3. Late corridor: none remaining in the explicit searchable tail

## Recommended next step

Recommended next step: there is no longer another ordinary contiguous explicit-chain batch left in `Germanic/docs/sound_changes/order_tests/next_batch_candidates.tsv`.

If additional first-break coverage is wanted, the next step is either to consolidate and reuse the current chronology-card corpus or to extend the runner so it can probe bundled / non-explicit positions such as `PWGmcChanges`. The corpus-wide documentation checkpoint for the completed searchable explicit chain now lives at `Germanic/docs/sound_changes/order_sensitivity_first_break_consolidated_overview.md`.

## Narrative synthesis cautions

Keep these synthesis cautions in view:

1. The SC041 earlier boundary remains a broad computational limit rather than a narrow adjacency claim.
2. The SC014 / SC015 / SC016 / SC018 / SC021 / SC022 / SC023 / SC024 / SC025 / SC026 / SC028 / SC029 / SC035 / SC037 / SC039 / SC050 / SC053 / SC058 / SC065 / SC067 / SC076 earlier sides end at a runner boundary inside `PWGmcChanges`, so they should not be narrated as if historical earlier first-break boundaries had been found.
3. The SC014 / SC018 / SC022 / SC025 / SC027 / SC028 / SC049 / SC053 / SC056 / SC057 / SC058 / SC060 / SC061 / SC065 / SC067 / SC068 / SC069 / SC071 / SC075 / SC076 / SC080 / SC083 / SC086 later sides found no real break before the current SC087 search boundary, so they must not be rewritten as claims that those rules historically must precede `SC087`.
4. The SC087 later side is bounded by the current runner limit beyond order `86`, not by a discovered historical stage.
5. The SC031 earlier and SC033 earlier breaks cross bundled `PWGmcChanges`, and the SC037 later break crosses technical-marker `SC038`; these are real computational breaks but not ordinary historical chronology constraints.
6. The SC015 later boundary at `SC036`, the SC020 later boundary at `SC040`, the SC021 later boundary at `SC040`, the SC023 later boundary at `SC047`, the SC024 later boundary at `SC056`, the SC033 later boundary at `SC044`, the SC036 earlier boundary at `SC019`, the SC040 later boundary at `SC072`, the SC069 earlier boundary at `SC023`, the SC079 earlier boundary at `SC055`, the SC081 earlier boundary at `SC055`, and the SC087 earlier boundary at `SC044` are broad or far enough that they should be narrated as computational boundaries rather than as tight local adjacency claims.
7. The SC023 later, SC030 later, and SC032 earlier `+?` rows are no-output / failed derivations, not ordinary surface variants, and should be narrated carefully.
8. The SC061 earlier row also records loss of output (`+?`) rather than an ordinary surface variant and should be narrated carefully.
9. The SC073 later boundary should be keyed to `SC085` OE H Loss exactly as recorded in the TSV.

## Scaling note

The driver has now survived several manual terminal batches cleanly. Future terminal runs no longer need to stay at three rules per batch: a 6-10 rule batch is now a reasonable target when the selected rules are all eligible explicit-chain members and the user wants a longer run.

As before, heavy runs should be done manually from a normal terminal rather than inside Copilot.

## After a batch completes

Once a terminal batch run finishes cleanly, the follow-up workflow is:

1. inspect the summary, changes, and failures TSVs
2. update `sound_change_order_sensitivity.tsv`
3. generate or refresh chronology cards
4. write a batch report summarizing the new boundaries and caveats
