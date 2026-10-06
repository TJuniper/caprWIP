# Research memo — 2008 fern / fearn

## Starting point

- **ID:** 2008
- **CONCEPT:** fern
- **COUNTERPART:** `fearn`
- **PROTO:** `*fárnaz`
- **PROTOFORM:** `*fárnaz`
- **DERIVATION_CLASS:** `regular`
- **NOTE:** `Proto: oblique *farnăn→*farnăz (m. a-stem nom.sg.; Kroonen)`

This is a `regular` row, but it still requires memo/report treatment because the TSV `NOTE` is non-empty.

## Packet evidence assessment

Authoritative/current packet material:

- The packet's TSV-row block is authoritative as a restatement of the live row data.
- The compact derivation trace is current project-behavior evidence: the present FST takes `*fárnaz` to `fearn` by ordinary OE developments.

Useful background:

- The `DEV_NOTES` hit is useful internal background because it confirms that the project already classifies row 2008 as a straightforward breaking case.
- `old_english_wiktionary.tsv` is a helpful supplementary lookup for the OE headword `fearn`.

Stale or diagnostic only:

- `Germanic/docs/analysis/arestoration_r_l_research.md` is correctly treated by the packet as diagnostic/background, not as row-level authority. It comes from a broader A-restoration audit and merely lists 2008 among rows whose `ea` is explained by breaking before `*rC`.

Irrelevant or potentially misleading:

- The missing manifest entry is not evidence either way.
- The packet's bibliography-key suggestion `Kroonen2013` is plausible, but the packet alone does not resolve the underlying stem/gender question.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/docs/DEV_NOTES.md` around the cited row list.
- `Germanic/docs/analysis/arestoration_r_l_research.md` around the cited affected-row discussion.
- `Germanic/data/oe_known_problems.tsv` (no entry for this lexeme).
- `Germanic/data/old_english_wiktionary.tsv` (`fern → fearn`).
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`, which gives `*farna- m. 'fern'` and cites OE `fearn, fern` [@Kroonen2013].
- `docs/references/legacy/orel_handbook_germanic_etymology.txt`, which instead has `*farnan sb.n.` with OE `fearn` [@Orel2003].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`, which gives the OE headword `fearn n.` [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, which attests `fearn` and inflected forms `fearnes`, `fearna`, `fearne` [@BosworthToller1898].
- `docs/references/hogg_vol1.txt`, `docs/references/ringe_taylor_linguistic_history_vol2.txt`, and `docs/references/kaluza_historische_grammatik_englisch.txt`, all of which support ordinary breaking to `ea` before `r + consonant` [@HoggPhonology1992; @RingeTaylor2014; @Kaluza1906].
- `Germanic/docs/lexeme_reports/pilot/` for any existing fern report; none exists.

## Reconstruction and early-stage forms

Three levels need to stay separate here:

1. **Comparative/cognate-set proto:** external reference works do not give exactly the same citation form. Kroonen has stem-style `*farna- m.` [@Kroonen2013], while Orel has `*farnan` as a neuter noun [@Orel2003].
2. **Project input form:** the live row uses `PROTO = PROTOFORM = *fárnaz`, i.e. a nominative-style PGmc form suitable for the deterministic derivation trace.
3. **OE target:** the row targets attested `fearn`.

For the current pipeline, `*fárnaz` is not a problem input. The project trace already gives the expected regular sequence `*fárnaz > *fárna > *fárn > *færn > fearn`, with final `ea` from breaking before `rC`.

The real issue is not the derivation but the wording of the note. `Proto: oblique *farnăn→*farnăz` compresses a stem/paradigm observation into a form that blurs the difference between a comparative citation stem and the actual PGmc form used as FST input.

## Old English philology

The OE target should be treated as **attested**, not reconstructed. Repo-local lexical sources consistently support `fearn` as the main OE headword: `old_english_wiktionary.tsv` has `fearn`, Clark Hall gives `fearn n.`, and Bosworth-Toller records `fearn` with inflected forms `fearnes`, `fearna`, and `fearne` [@ClarkHall1960; @BosworthToller1898].

Kroonen's comparative entry lists OE `fearn, fern` [@Kroonen2013], but the repo evidence checked here does not supply manuscript-level or dialect-specific grounds for retargeting the row from `fearn` to `fern`. The safer project statement is therefore that `fearn` remains the OE citation target, while `fern` is at most a comparative variant noted in the etymological dictionary.

The philological caution point is gender/stem labeling. Kroonen's masculine `*farna-` and Orel's neuter `*farnan` do not line up neatly with Clark Hall's `fearn n.`. That disagreement should be reported as source variation, not flattened into an unqualified claim that the lexeme is simply a masculine a-stem.

## Project problem and solution

This is not an OE-output problem. The row is correctly classed as `regular`, and the current FST already reaches `fearn` without any special repair.

The project problem is explanatory hygiene: the non-empty TSV note is trying to preserve a comparative-stem observation from Kroonen, but it currently does so in a way that obscures the distinction between:

- the comparative proto headword cited in dictionaries;
- the project's PGmc input form used for derivation; and
- the attested OE target.

The solution is to keep the row as a regular breaking case, but rewrite the eventual prose/note so that it says explicitly that the modeled input is `*fárnaz`, while external sources disagree somewhat on the lexeme's comparative stem/gender citation.

## Paradigm probe

No paradigm probe is required.

This row does not depend on selecting among competing OE paradigm cells or analogical PGmc inputs; the modeled input already derives the target regularly. Bosworth-Toller does provide useful attested cells (`fearnes`, `fearna`, `fearne`), but those are philological corroboration, not evidence that the report needs a probe-driven solution.

## Recommended final report

Keep the eventual `### Lexeme report` brief. It should describe 2008 as a regular `*rC` breaking case, state that `*fárnaz` yields `fearn` without special intervention, and add one short philological note that Kroonen's `*farna-` and Orel's `*farnan` reflect comparative stem/gender disagreement while the OE target remains attested `fearn`.

## Data-change recommendations

- **TSV `PROTO`:** no immediate change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `fearn` is still the best-supported OE headword in repo-local evidence.
- **TSV `DERIVATION_CLASS`:** no change recommended; `regular` is correct.
- **TSV `NOTE`:** **change recommended.** Rewrite it so it no longer presents Kroonen's comparative stem comment as though it were itself the project input history. A clearer note would say that the project input `*fárnaz` gives regular `fearn`, while Kroonen cites `*farna-` and other sources differ on stem/gender.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES` / dossier text:** no required change. The existing analysis note is acceptable as broad diagnostic background, though it should not be treated as the row's main philological authority.
