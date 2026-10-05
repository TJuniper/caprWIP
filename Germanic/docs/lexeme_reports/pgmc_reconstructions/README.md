# PGmc reconstruction survey

This is research evidence for all Old English data points, not a second
corpus, historical-stage registry or approved input migration. The survey
now has complete Orel/Kroonen reading coverage and a citation-unit triage
of all393 rows. Explaining every disagreement remains ongoing; a reviewed
triage is not a collection of settled histories or an adoption decision.

## Ownership

- SOURCE: `sources.tsv` declares the reasonable held source universe,
  actual holdings, scope, edition/convention verification, exclusions and
  explicit consultation mode/priority/payoff.
- SOURCE: `forms.tsv` records diplomatic author forms or process evidence,
  exact printed pages, stages/cells, explained comparison notation, argument,
  verification and independent confidence.
- SOURCE: `coverage.tsv` records only actual row/source reviews and their
  evidence links, search basis and assessment. No row means no actual review.
- SOURCE: `review_targets.tsv` records finite non-core commitments, each
  with a selection basis and explicit reading-scope links; the two core
  populations are derived automatically.
- SOURCE: `reading_scopes.tsv` records the scheduled three-source screens,
  method readings and passages, with actual reading/verification distinct
  from planned population and page addresses.
- SOURCE: `reading_accountability/` retains the completed source-specific
  row-applicability manifests and bounded original-page check receipts.
  Each applicability manifest covers393 identities without manufacturing
  lexical consultations; these files also enter projection provenance.
  The Fulk selected-cell guard receipt preserves original inference
  provenance separately from later NOTE/sidecar checks. A surface-form
  guess is not a verified selected-cell identification.
- SOURCE: `analyses.tsv` owns evidence-linked row/unit, relationship,
  attribution, stage interpretation, justified analytical form and features.
- SOURCE: `comparisons.tsv` owns scoped cases, overlapping question/type
  tags, comparability and explanation status. Separate alignment status,
  cited basis and exact limits distinguish feature review from citation
  inventory. Tags are not settled causes.
- SOURCE: `rationales.tsv` owns typed, cited explanations and their premises
  and counterarguments, distinguishing source statements from our inferences.
  `reason_target` separates position support, descriptive bridges and
  explanations of divergence; controlled `conditioning_tags` identify
  cited class membership, never automatic matches of current strings.
- SOURCE: `commentary.md` owns the scientific synthesis and outstanding
  questions, not automatically approved corpus decisions.
- GENERATED: `corpus_inventory.tsv`, `source_coverage.tsv`,
  `reconstruction_ledger.md`, `survey_provenance.json`, `source_priorities.tsv`,
  `analytical_coverage.tsv`, `comparison_map.md` and `reading_progress.md`
  are projections through the canonical artifact graph.

All 393 OE row IDs remain in the population, including six research-only
rows. Current citation/input/stage/context/class fields are read from their
existing owners. Equality-stage resolution is an encoding convention,
not independent source agreement. Confidence does not assign a stage.
Shared evidence may link several rows, but each selected cell retains its
own review. Reconstructed stems, complete words and process statements
are not interchangeable evidence types.

Generated reading coverage contains the786 core targets, explicitly
scheduled non-core targets and every retained actual consultation, not
the bibliography-by-row Cartesian product. An unscheduled source has not
been reviewed or declared absent. A negative search needs an explicit
search basis; a scoped exclusion needs a reason.
Never turn a failed string search into evidence of author silence.
Verification gaps must remain visible. An indirect quotation retains its
quoted-author attribution without claiming the original was checked.

Printed-page strings contain numerals/roman folios, comma-separated ranges
and ASCII hyphens. PDF-sheet markers belong in locator/basis notes, never
in the citation-page field. Diplomatic forms are preserved verbatim.
Comparison normalization must be explained; Foma's symbol restrictions
are not a reason to alter a printed source form.

The validator does not infer scientific agreement from normalized strings,
and does not edit corpus fields, stage metadata, FSTs or fingerprints:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-core-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-analysis-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-three-source-complete
python3 Germanic/tools/pgmc_reconstruction_survey.py --require-feature-alignment-complete
python3 Germanic/tools/adjudicate.py --refresh
```

The first command reports validity and actual incompleteness. The composite
gate fails while a required row target, three-source passage/screen/method
or core analytical row remains unreviewed, not merely because a background source was
not read. Declared local verification gaps are not silently erased;
a reviewed survey with such limits is not wholly image-verified evidence.
The core-only gate requires both dictionaries, every population row's
actual disposition and reviewed core methods. It cannot be satisfied by
deleting a source, omitting a row or requiring only positive evidence;
it does not certify other sources or diplomatic image verification.
The analytical gate also requires core reading completion and all393
core triage dispositions, retaining every recorded core alternative.
Unknown cause, date, endorsement and non-comparable units are legitimate
explicit dispositions. It does not certify complete explanation, every
source argument, historical equivalence or scientifically preferred inputs.
Only the last command regenerates projections. Do not run separate
generators or hand-edit outputs.

## Active three-source dispatch

The approved next stage completes relevant Ringe2017, Fulk2018 and
RingeTaylor2014 reading before analytical closeout. After extraction it
requires feature/paradigm alignment of all393 core rows, substantive-case
explanation or exact remaining premises, the conditioning census and a
non-adopting consistency watchlist. The current analytical gate still
certifies citation-unit triage only.

All three relevant held-source passes are persisted: Ringe191, Fulk136
and Ringe-Taylor255 actual consultations. Each has393 independent
applicability dispositions; the1179 screens are not1179 grammar
negatives. All786 core reviews remain. Of20 scopes,19 are reviewed
and the Ringe-Taylor conventions scope retains its genuine verification
gap. The fully verified three-source gate therefore still refuses
completion; the held-text reading is finished with named limits, not
newly image-certified.

There are4269 evidence records,1379 actual consultations and4377
analytical positions, with404 comparisons and113 rationales. The RT
occurrence audit removed31 overlapping new extractions before integration;
genuine repeated forms at different positions/cells/stages remain.
The persisted occurrence, remap, passage, page and glyph-limit receipts
document that distinction. Only author attribution and appended notes
change in the three named inherited RT records; their forms, pages,
stages and verification remain intact.

Fifty-seven core rows now have individually reconciled, bounded alignment:
1933-1989. The remaining336 are unreviewed. The second tranche builds on
the35 preparatory dictionary decisions rather than treating that preparation
as finished all-source alignment. Each completed
alignment retains all available member positions and names its specific
remaining formation, reflex, representation or selected-cell premise;
none is a settled whole-word equivalence or established whole-case cause.
Ringe's ask-specific following-j reason and RT's bake following-i/lost-trigger
reason are position support, not a completed class census.

The second tranche reconciles all70 inherited positions for1941-1947
and1949, adds seven occurrence-backed quoted endpoints and four precise
process records to existing consultations, and records seven reasons.
The focused `beaver-colour-direction` case compares opposing derivational
directions and marks its explanatory connection as analyst inference, not
a direct Kroonen rebuttal of Orel or an established whole-word history
[@Orel2003, pp.40-41; @Kroonen2013, pp.56-57].
Its two focused positions reuse existing evidence; core evidence links
are deduplicated without dropping those distinct analytical units.

The amendments receipt preserves the old/new SOURCE annotations: Orel's
bier is literally WGmc, not an expanded PWGmc label; RT's starred Gothic
bag comparison is not an undated PGmc endpoint; Fulk's beaver example
concerns OE back mutation, separately from the explicit PGmc word and
starless index. Berry's Verner paradigm does not supply accented cells
[@Orel2003, p.38; @RingeTaylor2014, p.287;
@Fulk2018, pp.69,386; @Kroonen2013, pp.54-55].
`alignment-1941-1949-occurrences.tsv` records the seven literal source
spans and paragraph hashes; `alignment-1941-1949-amendments.tsv` records
the individually justified reporting corrections. Neither receipt changes
source confidence, diplomatic forms or scientific corpus owners.

The third tranche reconciles all74 inherited positions for1950-1957:
bind, birth, blood, board, bone, book, bore and bosom. Thirteen literal
occurrences and seven process records supplement existing consultations;
nine reasons separate position support, a premised bind representation
bridge and a bounded, analyst-inferred bone-origin comparison.
`alignment-1950-1957-occurrences.tsv` records exact text spans/hashes;
`alignment-1950-1957-amendments.tsv` preserves reporting corrections.
Book's three RT plural citations are explicitly PNWGmc, while Fulk's
plural is explicitly PGmc; Latin profession/loan examples and the selected
OE nominative remain distinct. Native corrupted signs remain unchanged
[@RingeTaylor2014, pp.138,208,227,286; @Fulk2018, pp.64,166-167].
Ringe's actual bone quotation changes its existing consultation from
discussion-only to evidence-found, not into a new consultation
[@Ringe2017, p.328]. Whole-row causes remain unestablished, and neither
bone's origin nor bind's specific written e has been selected as CAPR's
preferred history.

The fourth tranche reconciles all72 inherited positions for1958-1965:
both, bottom, bough, weak causative bow, strong preterite bow, bow noun,
bower and brand. Twenty literal quotations and four processes add24
evidence records, with nine reasons and two focused units reusing evidence.
Fulk's actual strong-present passage is one new consultation; existing
reviews are supplemented, not duplicated [@Fulk2018, pp.263-265].
The source amendment/occurrence receipts are
`alignment-1958-1965-amendments.tsv` and
`alignment-1958-1965-occurrences.tsv`.

The selected strong preterite is not the ring noun quoted by several
sources. The focused `bend-external-cognates` case distinguishes Ringe's
explicit absence claim from Kroonen's external/metathesized connections;
why Ringe excludes those comparisons remains unestablished
[@Ringe2017, p.324; @Kroonen2013, pp.61-62].
Present quantity/origin, weak finite cells, nominal homonyms and selected
preterite remain separate. The current lexical model's RT55 locator does
not support its class-II present claim; the pertinent discussion is39-40.
This is a non-adopting reporting question, not a silent model correction
[@RingeTaylor2014, pp.39-40,55,268,280,296,309].

The fifth tranche reconciles all73 inherited positions for1966-1973:
bread, break, breast, breeches, bride, bring, brook and buck. Twenty-four
literal quotations and four processes add28 evidence records to existing
consultations, with thirteen reasons and four focused positions reusing
evidence. Nine SOURCE annotations are corrected without changing inherited
forms, pages, verification or shared links. The receipts are
`alignment-1966-1973-amendments.tsv` and
`alignment-1966-1973-occurrences.tsv`.

The focused `breast-paradigm-derivation` case distinguishes Kroonen's
qualified single-paradigm hypothesis from Ringe's gender-supported
derivational preference, without claiming a direct rebuttal
[@Kroonen2013, pp.76,80; @Ringe2017, p.223].
The focused `buck-borrowing-direction` case retains opposed donor directions
and their different gemination/formation premises as bounded analyst
inference, not a selected etymology
[@Orel2003, pp.61-62; @Kroonen2013, p.82].
Fulk's expected break participle is an antecedent to the remodelled endpoint
he expressly accepts, not an author opposition. His relevant footnote is
printed290, on holding sheet307, not the earlier class-IV opening
[@Fulk2018, p.290; @Ringe2017, pp.211,272].
Strong dictionary headings, reconstructed weak pasts, actual finite cells,
PNWGmc plurals and pre-OE comparanda remain distinct. The commentary records
non-adopting breast citation-page and breeches input-stage reporting questions;
no model, corpus, stage sidecar, FST or scientific baseline is changed.

The sixth tranche reconciles all100 inherited positions for1974-1981:
burst, calf, chew, climb, comb, corn, cow and craft. Twenty-four literal
occurrence receipts and three process records add27 evidence records to
existing consultations; twelve reasons and four focused positions reuse
evidence. Twelve proved reporting annotations are corrected without
changing any inherited diplomatic/comparison string, page, verification,
confidence, kind or shared-row link. Receipts:
`alignment-1974-1981-amendments.tsv` and
`alignment-1974-1981-occurrences.tsv`.

`calf-greek-cognate-admissibility` contrasts Orel's admitted Greek womb
comparison with Kroonen's two explicit phonological objections
[@Orel2003, p.209; @Kroonen2013, p.278].
`cow-original-formation` contrasts Kroonen's original u-stem/graze account
with Ringe's acrostatic bovine account and unresolved northern stem
[@Kroonen2013, p.299; @Ringe2017, p.223].
Both explanatory relations are bounded analyst inference, not direct
rebuttal or settled whole-row causes. Neuter calf's singular *-az* does
not prove a masculine a-stem; identical Mercian genitive/plural *calfur*
receipts remain separate [@Fulk2018, pp.176-178;
@RingeTaylor2014, pp.205,231,385-386].
Cow's selected *cȳ* remains DAT.SG, even though RT's literal *cy* also
serves NOM.-ACC.PL [@RingeTaylor2014, p.318].
RT's feolan subgroup label is not a burst word, oakum is not comb, and
wizard/fire are not cow-family reconstructions
[@RingeTaylor2014, pp.202,318,347].
Climb preserves explicit PWGmc-only reconstructive restraint and Onions'
reported alternative [@RingeTaylor2014, pp.127-128; @Orel2003, pp.215-216].
The commentary records craft's dictionary-page and selected-input-stage
questions without changing the model or selecting a new history
[@Orel2003, p.220; @Kroonen2013, p.300].

The seventh tranche reconciles all122 inherited positions for1982-1989:
crop, cud, dale, day, deal, deed, deer and dew. Twenty-one literal
occurrence receipts and six process records add27 evidence records;
thirteen reasons and four focused positions reuse evidence. Seven proved
SOURCE annotations and eleven applicability-manifest fields have amendment
receipts, preserving both earlier screens as history:
`alignment-1982-1989-amendments.tsv` and
`alignment-1982-1989-occurrences.tsv`.
Actual omitted consultations are now recorded for Fulk/cud and Ringe/deer;
they are not393 invented negative reviews or a restarted book survey.

`deal-root-derivation` distinguishes Orel's divide-root account with
irregular initial from Kroonen's theoretical put-root account without
direct IE formation parallels [@Orel2003, p.67; @Kroonen2013, p.87].
`cud-e-cognate-admissibility` connects Ringe-Taylor's explicit exclusion of
e-based external cognates to his northern-WGmc u-raising premise, contrasting
Fulk's qualified possible gum/mastic example [@RingeTaylor2014, p.42;
@Fulk2018, pp.57-59]. Both causal relations are bounded analyst inference,
not direct rebuttal or adopted original histories.

Fulk explicitly relates both an iu/i-formation and an eu citation to
OE *dēor* 'beast'; his Finnish-loan claim must not be dismissed as an
unrelated precious-beast etymon [@Fulk2018, pp.12,73,81].
Ringe's independently quoted *diuriz* 'dear' is instead an i-stem
adjective, not an animal noun by string identity [@Ringe2017, p.315].
That formation/lexical-role bridge remains an exact research question.
The separate day/deed paradigm cells, uncertain plurals, reported
s-stem hypothesis, reconstructed OE intermediates, SEED comparator
and conditional DO hypotheses are preserved
[@Ringe2017, p.312; @Fulk2018, pp.129,177,253;
@RingeTaylor2014, pp.114-115,212,239,287,519-520].
The commentary retains non-adopting cud attestation/input and dew
formation questions; scientific owners and released glide history remain
unchanged.

The alignment follow-up corrects eight proved RT extractor clips against
their held paragraphs and preserves four genuinely corrupt native tokens
unchanged. `rt-token_boundary_review.tsv` records the distinction; added
`retained_*` fields in the occurrence receipt retain the original extractor
spans alongside the corrected whole-token spans. Beard's complete optional-z
stem is not an OCR restoration. Bake's omitted OE second singular *becst*
and the cited surrounding paradigm argument supplement its existing
consultation without adding a fake new review [@RingeTaylor2014, pp.180,232-233].

Ringe's bounded original checks resolve the former p.ix and trimoric
glyph limits. Fulk's original checks retain both *sit-j-anaⁿ* and
*setjanaⁿ*, without harmonizing their local dating assertions.
The commentary distinguishes the independently explicit PGmc fight
citations from the PWGmc citation and attestation grouping
[@Ringe2017, pp.ix,108,254,266,271,307,312;
@Fulk2018, pp.43,295].

The historical initial15-scope dispatch was supplemented by a completed Ringe
body-reading block, printed241-266, and its bounded endpoint/method review.
At that checkpoint there were16 scopes: four reviewed and12 pending reading/screening units.
The block adds49 diplomatic records and30 new actual consultations;
Ringe has34 actual reviews, not393 completed applicability screens.
Surface/underlying forms, other cells and conditional or later-stage
reconstructions remain separate [@Ringe2017, pp.242-243,249,252,254-256,262].
Ringe's transcription note is printedix; Fulk's reconstruction discussion
is printed11-12. Full source-convention reconciliation remains pending
[@Ringe2017, p.ix; @Fulk2018, pp.11-12].
Ringe-Taylor's Other conventions must acquire its verified printed roman
folio; PAGE14 is a navigation marker, not a citation.

`population_scope=all_rows` names the live393-row scope of a scheduled
screen/passage; it never says those rows have already been read or directly
mentioned. `named_rows` requires explicit IDs; `source_general` creates no
arbitrary row links. A pending page address identifies where reading starts,
not a claim that the entire relevant passage has been verified.

Completed scopes require actual search/reading assessment and printed
locators. A verification gap retains its specific limit and blocks the
fully reviewed three-source gate. That gate also requires all named sources,
their methods, screens covering the exact population, scheduled passages
and actual target consultations. An empty manifest cannot satisfy it.
Justified amendments must be recorded, not used to delete inconvenient
work. Source-wide relevance/completeness still needs scholarly review;
structural validation alone cannot prove that every useful passage was found.

The existing four-object `load()` API is preserved. Supplementary scopes
are loaded and validated separately. SQL exposes `reading_scopes`,
`scope_rows`, `scope_evidence` and `target_scopes`; membership in a pending
scope is scheduling, not completed review:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT source_key,status,count(*) AS scopes FROM reading_scopes GROUP BY source_key,status"
```

Feature-alignment and position-support versus inter-author explanation
accountability are implemented. They initially migrate every existing
citation-unit case as `alignment_status=unreviewed`, not as completed
feature research. Actual whole-population alignment follows the source
passes. A `bounded_limit` needs cited member evidence and the precise
remaining premise; `feature_aligned` cannot be certified by cell labels
alone. Position-support reasons cannot certify aggregate explanations;
equivalence bridges remain distinct from historical causes.
The new Ringe positions have reviewed citation units and source-supported
features; they do not close the existing393 core comparisons. A local
PGmc-sketch context is recorded without manufacturing an explicit dated
endpoint. The pending parent scopes retain the broader reading commitments.
Production choices, stages, FSTs and baselines remain unchanged; introduction,
PDF, acquisition and release are outside this batch.

The stronger alignment gate first requires the named three-source reading
programme. It then separately requires an aligned or precisely bounded
disposition for every core row. The earlier citation-triage gate retains
its narrower meaning. SQL exposes `alignment_evidence` and
`rationale_conditions`, as well as the explicit scalar depth fields:

```sh
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT reason_target,count(*) AS reasons FROM rationales GROUP BY reason_target"
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT alignment_status,count(*) AS cases FROM comparisons WHERE scope='core_triage' GROUP BY alignment_status"
```

## Holding corrections and limitations

### Core dictionary extraction

Orel and Kroonen each have393 actual reviews. This completes the lexical
baseline, not exact selected-cell quotations or scientific explanations.
The page-cited commentary records their different e/i positions.

Orel's preface pp.xi-xiii treats reconstructions as full lexical words,
acknowledges idealized morphology and filters some prefixes/names/loans.
Preserve his barred `đ`, velar sign `ʒ`, quantities and parenthesized segments/endings.
Native PDF text can map `đ` to a pilcrow, and OCR can flatten it to `d`;
neither extraction is diplomatic authority. His indexes are leads, not
guaranteed folios: the light verb indexed at241 is actually on243.

Kroonen's preface pp.vii-viii explicitly warns of omitted established
lexemes/reflexes. His notation/entry structure pp.xii-xiii distinguishes
headwords, reconstructed citations, alternatives and deeper etymological
constructs. Preserve stem dashes and separate homonym labels. Read the
whole relevant discussion: the smear verb is reconstructed inside a noun
entry, and three's short-i headword is not its long-i nominative.
Do not assume a global PDF-sheet offset: printed64 is sheet102,
whereas printed92 is sheet132. The actual running head governs.

For each row, search its OE citation/case aliases, source-specific
reconstruction spellings, semantic entry and cross-references; use the
indexes to locate and then read the actual entries. Search aliases may
vary thorn/theta, h/x, quantity notation and dictionary suffixes, but
they never change the recorded author form. Distinguish desire from
boiling, being from weight, and different paradigm cells. An absent
exact string remains unchecked until a scoped search is actually reviewed.
The initial candidate-class batch is positive evidence, not permission
to fill remaining dictionary pairs with automatic negatives.

### Other holdings

Kluge's held PDF is the 25th edition (2011), verified from its title
and edition-history pages. The older similarly named `.txt` identifies
the 24th edition, not the PDF. `kluge_seebold_2011_25th.txt` was extracted
from the held PDF using `pdftotext -layout`; it retains page breaks and
printed running heads. It requires ordinary glyph/page verification,
not an assertion that every extracted token is correct.

Hirt's held title is part I (1931), not evidence that the complete
three-part handbook is held. The Pokorny holding is a partial page
directory. Ringe-Taylor is held here as a text extract; missing local
images are explicitly distinguished from earlier dossier verification.
Generic Kylstra/Oxford filenames are aliases of identified sources.
The separately held Luehr thousand article is identified as Lühr1993,
Linguistica33, pp.117-136, and catalogued separately from the1998 EWA
contribution. Its scientific argument and forms still require review;
holding identification does not complete its corpus coverage.

No acquisition or whole-library OCR is authorized. Do not include private
correspondence as a published independent reconstruction source.

### Completed identity audit and remaining holding limits

The catalogue now distinguishes the actual seventh-edition Sweet1893
primer from the unheld Sweet1953 revision, and Toller1921's supplement
from the unheld BosworthToller1898 main dictionary. The excluded old
associations remain visible. This routes the same intended local reviews
to their real sources; it does not automatically retag or reverify old
scientific citations.

The two Howell/Salmons text extracts are byte-identical. The original
article and existing bibliography identify1997, pp.83-111;1988 remains
only a legacy key/filename, not a second publication.

Two genuinely additional held works are included: KlugeSeebold2002's
24th-edition text, with no established matching original or folio map,
and Kuiper1991's review, pp.105-120, appended to the MayrhoferIII scan.
Mayrhofer's three volumes are1992/1996/2001; Kuiper's review of early
fascicles is not Mayrhofer's dictionary argument or a review of the
completed three-volume work. Separate editions and reused files do not
provide independent author votes.

Pokorny's700 filenames are sheet identifiers:688 extracts are nonempty,
12 empty; visible printed502 is on sheet12 and1183 on sheet693.
The substantive holding begins around H/interjections, not page1;
no global page map or complete dictionary is certified. Stiles1985 is
only pp.89-94. Ringe1984's14-sheet scan ends at printed151, with a
conclusion/byline there; the cited publication extends to155, whose
remaining pages are not established as held. The bibliography's former
journal/page association is corrected, not substituted into old quotations.

Neri's held Ringe review is numbered1-12 and signed by its author;
the following Casaretto review is separate. Its publication date/venue
are not established by the detached holding, so the unsupported
Kratylos54(2009),156-160 association is withdrawn. Three other detached
articles retain explicit date/issue-verification limits. Bennett's curated
transcription has ellipses; the original PDF remains available for those
omitted passages. A title/edition audit never certifies reconstruction
conventions, entry extraction or whole-source negative searches.

## Prioritized consultation programme

All91 catalogue records are preserved:82 available and nine actual
exclusions;75 available identities are verified and seven have declared
metadata/holding limits. Availability is not a row-review obligation.
The superseded32,226-cell grid and31,749 unchecked checkpoint are historical
measurements of the old policy, not the current workload.

The current evidence has1457 diplomatic records and838 actual reviews:
786 core and52 other-source consultations. The completed dictionary
integration baseline of1408 records/808 reviews is preserved beneath
the Ringe body-reading supplement. Orel has393 positives, including
qualified family/component evidence; Kroonen has360 positives and33 bounded
negatives. These are not393/360 exact selected-cell agreements.
Kroonen's verification now records187 image-checked,503 text-checked and
one ledger-verified item after the spare metadata correction on printed465;
Orel's remainder is not universally image-checked prose.

| Priority / mode | Sources and bounded payoff |
| --- | --- |
| 0 / core_dictionary | Orel2003, Kroonen2013: complete393-row lexical baseline, now reviewed. |
| 1 / systematic_relevant | Ringe2017, Fulk2018, RingeTaylor2014: relevant indexed forms, methods, phonology/chronology and cell explanations; not393 arbitrary grammar negatives. |
| 2 / systematic_relevant | Bammesberger1990, Seebold1970, Kroonen2011: explicit nominal, verb-family and n-stem rosters drawn from unresolved cases. |
| 3 / systematic_relevant | KlugeSeebold2011, LloydSpringer1988: competing etymologies/loans for relevant Germanic families; EWA remains limited to the held volume. |
| 4 / case_triggered | Relevant phonology, numeral, formation, OE-history and subgroup specialists: named consequential questions only. |
| 5 / opportunistic | Mayrhofer, Beekes, Pokorny, Kuiper, attestation/background works and older-edition comparisons: consult exact relevant evidence, never blanket393-row treatment. |

The catalogue owns each entry's explicit mode/payoff; the generated
`source_priorities.tsv` exposes all assignments, including exclusions.
The active three-source stage now has31 finite Ringe row targets in
`review_targets.tsv`, linked to their actual quotations and broader
pending reading scopes. Further target rosters must name the question, applicable source
scope and new information expected. Stop expansion if a reviewed screen
adds no consequential form, argument, counterargument or diagnostic.
Never infer that result from a failed search, source title or bibliography
presence. Existing contextual evidence remains available regardless of mode.

## Analytical layer and query boundaries

There are1515 evidence/row positions,393 core citation-unit cases, one
narrow representation case, one premised stem case and46 cited rationales.
The twelve initial worked
calibrations are adder, cud, drench, find, gift, hind, knee, man, three,
wash, world and hue. Core triage retains all alternatives, including
deeper/conditional/rejected proposals, and records insufficient evidence
where a dictionary has a bounded negative. Much of the remaining triage
is unit-level and deliberately `undetermined`; it is not an explanation
of every visible difference. Twenty-nine core cases have linked reasoning;
a position's cited argument does not necessarily explain the inter-author
difference, so several such cases still have `unestablished` explanations.

`ending` often describes word-versus-stem presentation, not competing
inflectional reconstruction. Other overlapping tags distinguish notation,
transcription error, inventory, vocalism, quantity, ablaut, consonantism,
stem class, gender, suffix, inflection, segmentation, chronological stage,
PGmc membership, lexical/cognate identity and historical analysis.
Tags on an undetermined case identify research questions, not settled
scientific disagreements or independently counted events.

Analyses preserve unknown stage/endorsement and source qualifications.
Dictionary context cannot establish a dated PGmc endpoint. An analytical
form reuses only the diplomatic form or its already explained comparison
notation; the feature JSON and evidence IDs retain its scope. Quantity,
optional material, segmentation and uncertain signs are never stripped.
Equivalence is scoped to unit, features, stage and explicit premises;
no transitive closure is inferred between differently premised cases.
The gift ʒ/g example establishes only representation of one citation,
not a stop/fricative reconstruction or equivalence with inherited i.
The spare example compares differently displayed weak-verb stems under an
explicit citation-segmentation premise, without assigning their date or
silently replacing either author's quoted form.

Queries construct validated tables in memory with Python's stdlib SQLite;
there is no editable database/service. In addition to the SOURCE tables
and live `corpus`, normalized bridges are `comparison_rows`,
`comparison_types`, `comparison_analyses`, `analysis_features`,
`evidence_rows`, `comparison_rationales`, `rationale_evidence` and
`rationale_analyses`. SQL is read-only; results are TSV.

```sh
# Reviewed vocalism questions and their explanatory certainty.
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT c.comparison_id,c.comparability,c.explanation_status FROM comparisons c JOIN comparison_types t USING(comparison_id) WHERE t.type='vocalism' ORDER BY c.comparison_id"

# Source positions that are explicitly later than the unspecified dictionary level.
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT a.row_id,f.source_key,f.printed_pages,a.analytical_form,a.stage_interpretation FROM analyses a JOIN forms f USING(evidence_id) WHERE a.stage_interpretation IN ('pwgmc','wgmc','proto_norse') ORDER BY a.row_id,f.evidence_id"

# Why a case is disputed, including source pages and inference/author attribution.
python3 Germanic/tools/pgmc_reconstruction_survey.py --query \
  "SELECT r.comparison_ids,r.basis_type,r.support_mode,r.statement,f.source_key,f.printed_pages FROM rationales r JOIN rationale_evidence re USING(rationale_id) JOIN forms f USING(evidence_id) WHERE r.basis_type IN ('loan_hypothesis','analogy','pie_reconstruction') ORDER BY r.rationale_id,f.evidence_id"
```

The atlas is the page-cited analytical view; the ledger remains the fuller
source argument/verification companion. The shorter introduction, new PDF,
next large extraction and any scientific adoption are separate work.
