# SC023 adjudication — scope and stage of the n-stem *n*-loss

Registry-verdict: SC023=REFORMULATE/RETAIN

Status: adjudicated (this memo governs the outcome)
Scope: SC023 `PNWGmcNStemNLoss` only.
Verdict: **REFORMULATE the historical characterization (stage + narrative);
RETAIN the executable rule, the corpus, and the chronology edges unchanged.**

## 0. The question

The historical description of SC023 says the change is the feminine n-stem
nominative-singular development `*-ōn > *-ǭ`, but the executable FST is
segmental and morphologically unrestricted:

    define PNWGmcNStemNLoss [
        {*ō} {*n} -> {*ǭ} || _ .#.
    ];

The SC023 chronology card reports exactly one changed lexeme for the positive
rightward boundary SC023 < SC047 `OEHeavySyllableNasalApocope`: the verb
`do`. Since `do` is not a feminine n-stem, the suspicion was that the
SC023 < SC047 edge is an artifact of an over-broad implementation rather
than evidence for a historical ordering. This memo adjudicates that
suspicion. The result is the opposite of the suspected outcome, for a
reason the sources make explicit: the historical change behind SC023 is
**general phonology, not n-stem morphology** — but it is **(pre-)Proto-
Germanic, not Northwest Germanic**.

## 1. Phase-1 diagnosis: the `do` trace

Selected input (corpus row `do`): PGmc `*dōną`, expected OE `dōn`.

Full stage trace (per-stage sandbox bins, `oe_full_trace_report.py` stages):

    ProtoInput:                    *d*ō*n*ą
    ... (no rule changes the form through position 46) ...
    SC047 OEHeavySyllableNasalApocope:  *d*ō*n     (final *ą deleted)
    OldEnglishRemoveStars:         dōn

- Form immediately before SC023 (position 23): `*dōną`.
- What SC023 does to it live: **nothing** — the form ends in `*ą`, not
  `*ōn`, so the rule cannot match. `do` is not a live SC023 application.
- Counterfactual (SC023 moved after SC047): SC047 first strips `*ą`,
  creating a *secondary* word-final `*-ōn` in `*dōn`; the displaced SC023
  then fires (`*dōn > *dǭ`) and the derivation collapses to `+?`.
- Why the harness reports SC023 < SC047: the first-break runner detects
  exactly this counterfactual collapse. The constraint is real at the
  executable level; the question was whether it is historically
  meaningful. See §4: it is — as a **counterfeeding** ordering.

## 2. Phase-1 census: every live SC023 application

Direct stage-bin census over all 383 corpus rows (form after
`PNWGmcMnDissimilation` vs. after `PNWGmcNStemNLoss`); the legacy-380
subset contains the same firings. **17 rows change — and all 17 are weak
n-stem nouns cited in the stem form `*-ōn-`:**

| concept | input | before SC023 | after SC023 | class |
|---|---|---|---|---|
| flask | `*fláskōn` | `*fláskōn` | `*fláskǭ` | fem. ōn-stem |
| line | `*lḯnōn` | `*lḯnōn` | `*lḯnǭ` | fem. ōn-stem |
| list | `*lḯstōn` | `*lḯstōn` | `*lḯstǭ` | fem. ōn-stem |
| nightmare | `*márōn` | `*márōn` | `*márǭ` | fem. ōn-stem |
| nettle | `*nátilōn` | `*nátilōn` | `*nátilǭ` | fem. ōn-stem |
| adder | `*nḗdrōn` | `*nḗdrōn` | `*nḗdrǭ` | fem. ōn-stem |
| swallow | `*swálwōn` | `*swálwōn` | `*swálwǭ` | fem. ōn-stem |
| sun | `*súnnōn` | `*súnnōn` | `*súnnǭ` | fem. ōn-stem |
| side | `*sḯdōn` | `*sḯdōn` | `*sḯdǭ` | fem. ōn-stem |
| toe | `*táixōn` | `*táixōn` | `*táixǭ` | fem. ōn-stem |
| tongue | `*túngōn` | `*túngōn` | `*túngǭ` | fem. ōn-stem |
| wart | `*wártōn` | `*wártōn` | `*wártǭ` | fem. ōn-stem |
| weasel | `*wéslōn` | `*wéslōn` | `*wéslǭ` | fem. ōn-stem |
| widow | `*wíduwōn` | `*wíduwōn` | `*wíduwǭ` | fem. ōn-stem |
| heart | `*xértōn` | `*xértōn` | `*xértǭ` | weak n-stem (OE fem.; PGmc neuter remodeled) |
| whore | `*xōrōn` | `*xōrōn` | `*xōrǭ` | fem. ōn-stem |
| earth | `*érθōn` | `*érθōn` | `*érθǭ` | fem. ōn-stem |

This resolves the apparent card/inventory conflict: the inventory's
`trace_occurrence_count = 17` counts these live, fully in-domain firings;
the chronology card's single lexeme `do` counts only the *displacement*
failure. There is no out-of-domain live application. The corpus therefore
already contains seventeen genuine weak-n-stem witnesses; no witness needs
to be invented and none needs to be removed.

The only other corpus inputs ending in `-n#` are `*sébun` 'seven',
`*nígun` 'nine', `*téxun` 'ten', `*xébun` 'heaven'. None is touched by
SC023 (final `-un`, not `-ōn`) — and §3 shows this is historically
required, not accidental.

## 3. What the sources actually support

**Ringe (2017: 101–103).** The loss is a *general phonological change*,
not an n-stem rule: "After the resolution of syllabic sonorants into *uR
and the change of word-final *-m to *-n, word-final *-n was lost with
nasalization of the preceding vowel in polysyllables. For forms ending in
PGmc *-ǭ this can be proved, since that word-final nasalized vowel has
distinctive reflexes in West Germanic (OHG -a, OE -e, etc.)" (p. 101).
His proof set spans *all* morphology: neuter a-stem nom.-acc. sg.
`*yugóm > *yugón > *juką` 'yoke', acc. sg. `*wúlnān > *wullǭ` 'wool',
acc. sg. masc. pronouns `*tón > *þanǭ`, and — decisively for the present
question — a **verb form**, 1 sg. pret. `*dedę̄ > *dedą̄ > *dedǭ` 'I did'
(pp. 101–102, 168–169). A change whose canonical witnesses include verbs
and pronouns is not feminine n-stem morphology.

**Stage.** Ringe places the change among "the earliest pre-PGmc sound
changes" (2017: 90, on the group including the final-nasal developments),
ordered before the loss of word-final coronal stops (chronology chart,
2017: 163). Reconstructed Proto-Germanic already shows its output:
`*juką`, `*wullǭ`, `*dedǭ`, and weak-noun nom. sg. `*tungǭ` (Goth.
`tuggo`, which proves the East Germanic branch shares it; R/T 2014: 58
give PNWGmc nom. sg. `*tungǭ`, `*hertô` > PWGmc `*tunga`, `*herta` > OE
`tunge`, `heorte`). R&T 2014: 54–55 add that nasalization of word-final
vowels "was contrastive in PGmc" and was lost only in PWGmc. The change
is therefore **(pre-)Proto-Germanic / Common Germanic at the latest** —
the former "Northwest Germanic" stage label was wrong, exactly parallel
to the SC022 stage correction.

**Numerals and 'heaven'.** Ringe (2017: 103): "It should follow that
'seven' and 'nine' ended in *-ų in PGmc, but they did not; they clearly
ended in *-un. This is the result of lexical analogy among numerals," and
`*tehun` 'ten' likewise retains `-n`. So PGmc `*sebun`, `*nigun`,
`*tehun` (and the `*hebun-` stem of 'heaven') stand outside the law's
surface effects in the reconstructed lexicon. The CAPR corpus cites these
four words with final `-un`, and a general `-Vn# > -Ṽ#` implementation
would wrongly strip their nasals.

**Fulk (2018: 170–171, §7.31).** Fulk reconstructs the weak nom. sg.
endings with the masc./fem. contrast trimoric `*-ô` vs. bimoric
(nasalized) fem. `*-ǭ`, and notes (p. 171 n. 2) that the loss of `*-n`
"may be due to sandhi conditions (Prokosch 1939: §84c)" — i.e. possibly
inherited PIE sandhi, hence if anything *earlier* than Ringe's dating,
and in no version Northwest Germanic. The masc. n-stem nom. sg. `*-ô`
never had a final `-n` to lose, which is why the rule's inapplicability
to masculines is a fact about the input endings, not a conditioning of
the change.

**Conclusion on the research question.** Final `*-ōn > *-ǭ` is one
surface case of the *general* (pre-)PGmc loss of word-final `*-n` with
nasalization in unstressed (polysyllabic) final syllables. It is not a
morphology-specific feminine n-stem rule; the feminine n-stem
nominative singular is simply the one morphological cell whose CAPR
citation forms still show the pre-change shape.

## 4. Adjudication of the model

**The executable restriction to `{*ō}{*n}` is a deliberate proxy, and it
is correct.** CAPR's selected protoforms are (post-change) PGmc citation
forms: the other outputs of the general law are already encoded in the
inputs (`*dōną`, `*wulfą`, `*sunų`, …), so implementing the full law
would be vacuous for them; and the four `-un#` inputs (seven, nine, ten,
heaven) must *not* undergo it, per Ringe's numeral-analogy retention. The
only inputs still showing a pre-change sequence are the seventeen weak
nouns, cited Kroonen/Ringe-style in the stem form `*-ōn-`. SC023 is thus
the corpus-visible fragment of the general law, functioning as
citation-stem → PGmc nom. sg. normalization (`*túngōn` → `*túngǭ`). No
FST change is needed; broadening the rule would be historically wrong for
the numerals, and narrowing it morphologically is unnecessary because the
firing population is already exactly the in-domain set (pinned by
regression test).

**`do` is a valid witness — but of counterfeeding, not of application.**
Because the historical change is general phonology, any secondarily
created word-final `*-ōn` would have undergone it *had it still been
active*. OE `dōn` (apocope output of `*dōną`) retains its secondary final
`-n`; therefore the loss was complete and inactive before the OE-period
`*ą`-apocope (SC047). This is the classical counterfeeding argument, and
it is exactly what the first-break runner detects mechanically. The
SC023 < SC047 edge is therefore retained — but it is **stage-entailed**
((pre-)PGmc ≪ OE) rather than a discovered tight local adjacency, and the
former reader-facing narration "SC023 must feed the later apocope" was
backwards: SC023 does not feed SC047 (live SC023 never touches `do`);
rather, SC047 must not feed SC023. The same reinterpretation applies to
the `do`-based one-sided SC023 < SC061 boundary recorded on the SC061
card. The SC023 < SC069 boundary is independent of `do`: it rests on the
seventeen in-domain witnesses (e.g. `*nḗdrōn` > `nǣdran` instead of
`nǣdre` if SC069 precedes SC023) and stands unchanged.

**Witness inventory.** Seventeen genuine weak-n-stem witnesses already in
the corpus (§2); `do` reclassified as the negative/counterfeeding
witness; no additions, no removals.

## 5. Verdict

- RETAIN the executable rule `PNWGmcNStemNLoss` byte-for-byte (stable
  identifier; not a stage claim — same convention as SC022).
- REFORMULATE the historical metadata: stage `pnwgmc` → `pgmc`
  (scope `pan_germanic`), canonical display name "Proto-Germanic
  Word-Final N Loss"; the change is the general (pre-)PGmc loss of
  word-final `*-n` with nasalization, of which the executable rule
  implements the `*-ōn` citation-form fragment.
- RETAIN all chronology edges; re-narrate the `do`-based SC023 < SC047
  (and SC061-side) evidence as stage-entailed counterfeeding.
- No corpus change, no FST change, no baseline change: legacy-380 and
  expanded-383 fingerprints are expected unchanged, and this was verified
  after the metadata propagation.

## 6. Files governed by this adjudication

- `Germanic/fsts/germanic.txt` — comment block above the rule corrected
  (behaviour-neutral; compiled binary identical).
- `sound_change_historical_staging_map.tsv`, `sound_change_inventory.tsv`,
  `sound_change_aliases.tsv`, `build_historical_audit_table.py` (+
  regenerated `historical_audit_table.tsv`, `rename_migration_manifest.tsv`).
- Chronology ledgers: SC023 card, `chronology_card_index.tsv`,
  `chronology_graph_nodes.tsv`, `first_break_nodes.tsv`,
  `first_break_edges.tsv`, `sound_change_order_sensitivity.tsv`
  (narrative/name fields only; counts and witnesses unchanged).
- Book/literature dossiers for the 018–025 holding zone (SC023 lines).
- Reader-facing `023-n-stem-n-loss.md` (rewritten: general law, 17 real
  witnesses, `dōn` as counterfeeding evidence).
- `Germanic/tests/test_sc023_adjudication.py` (firing population pinned to
  the 17 concepts; `do` invariance at the SC023 stage; numerals/heaven
  untouched; stage metadata assertions).

## 7. Sources

- Ringe, Don. 2017. *From Proto-Indo-European to Proto-Germanic*, 2nd ed.
  Oxford: OUP. Pp. 90, 101–103 (the law and its proof set), 163
  (chronology chart), 168–169 (`*dedǭ`).
- Ringe, Don & Ann Taylor. 2014. *The Development of Old English*.
  Oxford: OUP. Pp. 54–55 (PGmc contrastive final nasalization, lost in
  PWGmc), 58–59 (weak nom. sg. `*tungǭ`, `*hertô` > OE `tunge`,
  `heorte`).
- Fulk, R. D. 2018. *A Comparative Grammar of the Early Germanic
  Languages*. Amsterdam: Benjamins. Pp. 170–171 (§7.31 and n. 2, with
  Prokosch 1939: §84c on possible sandhi origin).
