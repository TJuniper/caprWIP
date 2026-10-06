# Research memo — 2248 think / þenċan

## Starting point
- **ID:** 2248.
- **CONCEPT:** think.
- **COUNTERPART:** `þenċan`.
- **PROTO:** `*θánkijaną`.
- **PROTOFORM:** `*θánkijaną`.
- **DERIVATION_CLASS:** `regular`.
- **NOTE:** “Proto: *θankăz → *θankijăną (Kroonen *θankjan- 'to think'); OE þenċan (wk.v.).”

The live row is already a clean match in the current derivation cascade. The real memo task is to keep three levels separate: the broader etymological background involving `*þanka-/*þankaz`, the dictionary-style proto verb `*þankjan-` [@Kroonen2013], and the project’s actual input/output pair `*θánkijaną -> þenċan`.

## Packet evidence assessment
- **Authoritative/current:** the live TSV row; the packet’s compact trace with `EXPECTED: þenċan` and `OUTPUTS: þenċan`; and the local lexical-table support in `old_english_wiktionary.tsv` / `old_english_swadesh.tsv`, both of which treat `þenċan` as the OE citation form.
- **Useful background:** the packet’s `Kroonen2013` bibliography pointer and the compact sound-history trace showing palatalization plus i-umlaut on the way to `þenċan`.
- **Stale or superseded:** no row-specific stale derivation was surfaced in the packet; there is no sign here of an abandoned target or superseded TSV state.
- **Irrelevant or misleading:** the packet’s concept-name `DEV_NOTES` hits about `hycgan` as an OE weak class-III relic are not evidence for this row. They match the English gloss “think” but concern a different lexeme altogether. The other concept-name collisions on unrelated phonological topics are likewise diagnostic noise, not row evidence.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at `3939-3944` and `11578-11703`, to confirm that the class-III discussions are about `hycgan`, not `þenċan`.
- `Germanic/docs/dossier-leek-2026.md` at Campbell §438, because it explicitly cites `þencan` beside 3sg `þencþ` in the assibilation discussion.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` at `27213-27227`, where Kroonen gives dictionary-style `*þankjan-` with OE `þencan` [@Kroonen2013].
- `docs/references/ringe_vol1_pie_to_pgmc.txt` at `5399-5401` and `12303-12305`, where Ringe gives PGmc `*þankijaną` and OE `þenċan, þōhte, þōht` [@RingeTaylor2014].
- `docs/references/campbell_old_english_grammar.txt` at §438 and §762, to separate the `þencan` assibilation example from the separate class-III `hycgan` paradigm [@Campbell1959].
- `docs/references/hogg_vol1.txt` at `7814-7827`, which again confirms that the “think” verb in the weak-class-III discussion is `hycgan`, not `þenċan` [@HoggPhonology1992, p. 163].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` around the `ge-pencan` entry, which supplies abundant attestation for the `þencan/geþencan` lexeme family [@BosworthToller1898].
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- `Germanic/docs/lexeme_reports/pilot/` (checked; no existing pilot report for this lexeme).

## Reconstruction and early-stage forms
This row is straightforward so long as the levels are not collapsed:

1. **Cognate-set / derivational background:** the noun `*þanka-/*þankaz` ‘thought, thanks’ is etymologically related and explains why the row note mentions a noun-to-verb derivational relationship [@Kroonen2013].
2. **Dictionary-style proto verb:** Kroonen’s lemma is `*þankjan-`, i.e. the verbal stem without the project’s fully encoded infinitival ending [@Kroonen2013].
3. **Project input form:** TSV `PROTO` and `PROTOFORM` are both the fully encoded verbal input `*θánkijaną`, which is what the current FST actually derives.
4. **OE target form:** the row targets the OE infinitive/citation form `þenċan`.

So the note’s `*θankăz → *θankijăną` should be read as etymological background, not as a claim that the noun is the row’s direct derivational input. For the row itself, the operative reconstruction is simply `*θánkijaną > þenċan`.

## Old English philology
`þenċan` is the normalized OE citation form supported by the repo’s lexical tables and by Bosworth-Toller’s large `þencan/geþencan` evidence base [@BosworthToller1898]. The packet’s outcome is therefore philologically unproblematic at the headword level.

The main philological caution is lexical, not phonological: `þenċan` must not be conflated with `hycgan`. Campbell and Hogg cite `hycgan` as one of the residual OE weak class-III verbs [@Campbell1959; @HoggPhonology1992, p. 163]; that is a different lexeme from the ordinary weak verb `þenċan`.

Campbell §438 is still useful background: it shows that the `þencan` paradigm participated in the well-known assibilation / de-assibilation environment (`þencan` beside expected 3sg `þencþ`) [@Campbell1959]. But that does not create a row-level target problem. The row is about the infinitive `þenċan`, not about reconstructing a special finite paradigm cell.

## Project problem and solution
There is no live derivational mismatch here. The current project already derives `*θánkijaną -> þenċan`, and the row’s `regular` classification fits that state.

The only real project risk is documentary confusion:
- treating `*þankaz` as if it were the row’s direct input;
- treating Kroonen’s lemma `*þankjan-` as identical in function to the project’s fully encoded `*θánkijaną`;
- or importing `hycgan` weak-class-III evidence into the `þenċan` row because both gloss as “think.”

The solution is conservative: keep the row as a regular `*θánkijaną -> þenċan` case, and make the final report spell out the distinction between etymological background, project input, and OE target.

## Paradigm probe
No dedicated paradigm probe is required. This is not a paradigm-cell rescue, analogy case, or unresolved mismatch; the live infinitive input already yields the target form directly.

If a later final report wants to mention Campbell’s §438 alternation, an **optional** contrast between the infinitive and a 3sg present indicative cell could be informative, but it is not necessary for this memo or for the row’s current classification.

## Recommended final report
Recommend a short final report saying that row 2248 is a straightforward regular derivation `*θánkijaną -> þenċan`, while the note’s `*þankaz` material is only etymological background and the packet’s `hycgan` weak-class-III hits are irrelevant concept-name collisions. A brief sentence on Campbell’s `þencan` / `þencþ` assibilation context would be optional background, not the core claim.

## Data-change recommendations
- **TSV `PROTO`:** no change.
- **TSV `PROTOFORM`:** no change.
- **TSV `COUNTERPART`:** no change.
- **TSV `DERIVATION_CLASS`:** no change.
- **TSV `NOTE`:** **minor clarification recommended.** The current note is basically right, but it would be clearer if it explicitly marked `*þankaz` as etymological background and `*θánkijaną` / Kroonen `*þankjan-` as the verbal level relevant to the row.
- **`oe_known_problems.tsv`:** no change.
- **`DEV_NOTES` / dossier text:** no change required. The relevant repo materials are usable as-is once the memo makes clear that the class-III `hycgan` passages are only negative/control evidence for this row.
