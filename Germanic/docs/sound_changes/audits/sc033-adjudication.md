# SC033: singleton quantity versus j-created glide realization

Status: complete; author-approved implementation, integrated verification
and inspected publication are recorded below.
The original diagnosis and private reports remain historical evidence.

## Identity

- SC id: SC033; executable identifier: `OEEwLongDiphthong`.
- Date / branch / base: 2026-10-03 / update / `671edc53`.
- Related controls: SC031, SC106, SC032, SC034 and SC044's w consumer.

## Question

Does the incumbent long-output operation conflate short diphthongization
before singleton w, long realization of an endingless offglide, and the
separate j-created hue path?

Source support for the actual common quantity, conditioning, scope and
input checkpoints would refute this diagnosis. Correct final spelling
alone would not.

## Current state (before any edits)

At the research baseline the canonical row was unadjudicated,
`ws_oe/west_saxon`, confidence A.
Four e/i/acute-e/acute-i plus w clauses all produce long ēo plus w under
`OEEwLongContext`. The latter admits vocalic and weak-tail continuations
and a final geminate. No input, target, context or baseline edit was
made during that initial diagnosis; the adopted disposition is below.

The grouped 031–034 dossier's current section16, the released component
ledger, current reader, hue model/ledger and archived SC033 chronology
card were consulted. The card's old chew/four population is not current.

## Diagnosis

Pre-adoption `SC033 --evidence` rebuilt the backend stage bins and verified
387-row production/sandbox equivalence. Exactly two selected rows fired:

| Row | Selected PGmc input | Before SC033 | After SC033 | Target |
| --- | --- | --- | --- | --- |
| knee2085 | *knéwą | *k*n*é*w*ą | *k*n*ēo*w*ą | cnēow |
| hue2332 | *xéwją | *x*é*w*w*j*ą | *x*ēo*w*w*j*ą | hīew |

Knee is a singleton live application. Its *ą survives through the
literal bare-*a loss and is deleted only at heavy-syllable nasal apocope,
after the long output has been assigned. The supplied endingless target
is therefore not derived through the endingless checkpoint discussed by
the sources. This is an ending/quantity interface, not evidence for
unrestricted prevocalic lengthening.

Hue's geminate is created by j-gemination after the earlier inherited-ww
reanalysis. SC106 later simplifies that representation; mutation consumes
the long ēo and gives īe. Its model already discloses that a separate early
e-to-i raising intermediate is not implemented.

The current breaking implementation already has e→eo and i→io clauses
before w, so a source-distinct singleton consumer need not be invented
again. However, `EnglishBreakingWContext` is unrestricted literal w and
does not implement the high-front-following exclusion described below.
The partial private assay records this as an incumbent defect, not a
historically correct positive.

Private recipe `sc033-singleton-short` removes singleton lengthening,
retains hue's j-created long proxy as a control and leaves the rest of
production untouched. It uses the complete derived wrapper and checks
all 387 rows. Its retained hue mapping is not a newly defended historical
law. Results and the row-level decision are recorded at closeout below.

Witness roles: knee/hue are live applications of the incumbent; chew,
four/you and dew/hew are unchanged early-reanalysis/SC032 controls;
hay/strew are the settled awj contrast. Hypothetical wi component inputs
test conditioning, not admissions. An old displacement changing final
quantity does not itself demonstrate a historical edge.

## Literature

Existing owners: 031–034 grouped dossier, current component ledger,
SC033 reader and hue model/ledger.

- Campbell 1959 pp.45–47, §120 distinguishes inherited geminates,
  j-created iwj versus awj, contraction and endingless products. His
  p.46 supplies the divergent retained-glide history and West Saxon
  hue reflex; pp.53–54, §§136–138 distinguish later realization.
- Ringe–Taylor 2014 pp.173–175 separates eu/iu tensing and endingless
  ew-derived diphthongs. Knee occurs on p.174.
- Ringe–Taylor pp.187–188, §6.2.4 states short e/i diphthongization before
  w, blocked when w is followed by a high front vocalic. Its inflected
  knee stem has no long mark. Printed p.187 was visually checked against
  the held PDF, not inferred from a PDF-sheet label.
- Ringe–Taylor p.387, §7.2.4 explicitly contrasts long endingless cnēo
  with short pre-ending cneow-. The same page prints PGmc *knewą for
  the singular, matching the final-vowel type of the selected input.
  It explains w in endingless cnēow as leveling and cautiously suggests
  long quantity could also have been leveled into inflected stems.
  That latter inference is qualified because decisive verse attestations
  are elusive. Printed p.387 was visually checked.
- Kroonen 2013 p.224 supplies hue's e-form reconstruction in the existing
  extraction ledger. Campbell's iwj-class comparison is not a quotation
  of a PGmc *hiwja reconstruction of hue.

The accounts motivate separate histories, not a knee-specific phonetic
condition. Published leveling must not be converted into noun-conditioned
lengthening, lexical diffusion or an unacknowledged analogical operation.

### Knee's paradigm and the opinio communis

The user specifically requested a paradigm-led reassessment rather than
an attempt to rescue the selected nominative. The checked handbooks agree
on the distinction that matters here, although not on every reconstructed
ending or the extent of later leveling:

| Account | Regular pre-ending stem | Endingless stem and later reshaping |
| --- | --- | --- |
| Campbell 1959 pp.232–233, §584 | The regular short-stem singular entries are genitive cneowes and dative cneowe. | Long cnēo(w) occupies the uninflected cells; w can be added from inflected forms, and long quantity can spread back to the obliques, producing cnēowes etc. His dative-plural -wum includes an analogical vowel and is not the proposed regular-cell witness. |
| Luick 1914–40 p.139, §134 | Explicitly gives cneowe(s), genitive/dative of cnēo, under short e-to-eo before w, unless i follows w. | The same page's note2 discusses transfer of nominative long quantity into obliques in the tree/servant class. His earlier p.118, §101 distinguishes the knee/tree endingless eo/eu sources and subsequent leveling; it is not the same detailed derivation as Ringe–Taylor's. |
| Hogg, held 2011 reprint pp.21–22, §2.33; p.86, §5.22 | Dative cneowe is explicitly the short-diphthong example, contrasted with long cnēowe 'know' (past subjunctive); p.86 calls pre-w diphthongization regular and names the knee dative. | Footnote7 on p.86 expressly identifies w in cnēo(w) as analogical, contrasting its long diphthong's endingless origin with short breaking in cneowe. |
| Ringe–Taylor 2014 pp.187–188,387, §§6.2.4,7.2.4 | Short cneow- before syllabic endings. | PGmc *knewą gives endingless cnēo; w is generalized from inflected forms. Long quantity in the inflected knee stem is cautiously inferred, with the metrical evidential limitation explicitly retained. |
| Fulk 2018 p.154, §7.12 | Distinguishes cases retaining medial w from endingless offglide formation in the wa-stem class. | Describes two-way paradigm leveling: the endingless long diphthong commonly spreads to inflected forms and their w to the uninflected. His explicit example is servant, not a new independent knee quantity attestation. |

Hogg's pp.21 and 86, Luick's p.139 and Fulk's p.154 were visually
checked against the held PDFs. In particular, Hogg's short cneowe
must not be confused with the adjacent long cnēowe, which is a form
of 'know', not an alternative citation of 'knee'. Campbell's printed
p.233 paradigm preserves the same distinction despite OCR corruption
of other letters.

The defensible opinio communis is therefore the regular opposition
between a long endingless form without inherited final w and a short
pre-ending cneow- stem, followed by paradigm leveling. This is not a
claim that all recorded obliques were short, that every author proves
the same complete early chronology, or that manuscript eo alone
establishes quantity. Ringe–Taylor's explicit qualification about the
metrical evidence must remain visible. Hogg's footnote uses *knewaz,
whereas Ringe–Taylor gives the neuter *knewą; those author spellings
must not be silently harmonized or used as interchangeable exact inputs.

### Existing CAPR treatment and the regular-cell alternative

The corpus already distinguishes a citation reconstruction from a selected
paradigm cell. The cow model selects the dative *kūi → cȳ while retaining
the nominative citation *kōz; night selects *náxti → niht beside the
nominative citation *náxtz; meed selects the attested dative meorde.
Shoulder selects dative plural sċuldrum and explicitly compares competing
singular histories. Hammer selects a genitive within the same a-stem
paradigm. These are modelling precedents, not independent historical
evidence for knee. Their legacy early_analogy/late_analogy labels do not
mean that the selected cell itself must undergo an analogical FST rule.

For knee, dative singular cneowe is the strongest first choice because
Hogg explicitly identifies both its cell and short quantity (2011
pp.21–22,86), independently agreeing with Campbell's paradigm (1959
p.233) and Luick's genitive/dative examples (1914–40 p.139).
Genitive cneowes is a second source-supported regular-cell control.
Neither choice licenses silently selecting a long cnēowe/cnēowes
oblique that has undergone the very quantity leveling under investigation.

The constructed PGmc cell candidates are *knéwai (dative) and *knéwas
(genitive), retaining *knéwą as the citation reconstruction. They combine
the inherited stem with the conventional a-stem endings; they are not
verbatim whole-word reconstructions quoted from Hogg or Campbell.
Fulk 2018 pp.146–147, §7.8 supports the *-as and *-ai analyses while
explicitly discussing competing explanations of the genitive ending.
His p.147 also weighs *-ē and *-ai explanations of the dative, preferring
*-ai for the West Germanic line while acknowledging wider uncertainties.
The proposed dative input follows that defended working analysis, not
a claim of unanimity about every inherited ending.
The selected-input stage must be recorded independently, as with the
existing corpus cell selections.

Private recipe sc033-oblique-cells tests these two cells through the
complete suffix after PGmc input encoding under the same singleton-short
counterfactual. Its persisted oe_sc033_oblique_cells_result.json passes
two component and two native-suffix assertions: encoded *knéwai gives
cneowe, and encoded *knéwas gives cneowes. These assertions begin after
EnglishProtoInput; they are not raw-input parser/admission tests.
The full-wrapper corpus identity is reproduced across all 387 rows.
The unchanged-input counterfactual still changes exactly the existing
knee row to short cneow; all other 386 finals and all protected artifacts
are unchanged, with no missing or ambiguous outputs.
No existing corpus input or target is overridden.
The general endingless interface diagnostics remain separate: changing
to a regular oblique cell would remove knee's selected endingless-target
obligation, not establish that every earlier ending rule is correct.
Source-backed case selection is preferable to adding a disguised
nominative w-restoration or lexical lengthening law.

## Historical analysis

The incumbent metadata is not yet a defended component assignment.
Ringe–Taylor's pre-w diphthongization is early English, not established
as a solely West Saxon long-vowel innovation by these passages. Its high
front exclusion and short quantity belong to its historical domain.
The long endingless history and the j-created path require separate
checkpoint/quantity arguments. Confidence in a secure process is distinct
from confidence in this implementation's dating or coverage.

The exact relative position of every component is not settled merely by
the current SC033 slot. No chronology edge is promoted from the private
experiment, old safe windows or matching final forms.

## Verdict

REFORMULATE the historical-law interpretation / RESTRICT the executable
domain to the retained j-created representation. The stable SC033 identity
is now an active support stage, not a claimed independent sound law.
Its unsupported historical stage/scope/confidence are removed rather than
invented for hue's incomplete compatibility path.

Registry-verdict: SC033=REFORMULATE/RESTRICT

The user explicitly authorized selecting a PGmc and Old English dative
singular for knee, implementing the necessary corrections and publishing
the detailed lexical account in its changed section. The selected pair is
*knéwai → cneowe; citation PROTO *knéwą remains. This removes the
analogically restored nominative w from the sound-law comparison without
adding grammatical, lexical or analogical conditioning to a sound law.
Ordinary short pre-w diphthongization remains at SC044, with its missing
high-front-following guard repaired.

### Measured partial counterfactual

`oe_sc033_singleton_short_result.json` passes eight component, three
staged and three corpus assertions. All 387 rows have unambiguous output;
only knee2085 changes, from cnēow to cneow. The seven old mismatch IDs
remain, with knee added. Hue's native hīew is unchanged, as are every
other selected final, every selected input and all protected artifacts.

At the knee checkpoint the private variant retains *k*n*é*w*ą through
SC033, then the existing breaking consumer gives *k*n*éo*w*ą. Nasal
apocope later removes the ending. This is a measured partial
counterfactual, not a claim that cneow is the correct endingless regular
reflex of PGmc *knewą.

The first run's artificial alphabet-filter identity rejected twenty
temporary au products. That was a technical error, not twenty historical
consequences. Replacing that filter with unrestricted identity removes
all rejections; the failed report is retained in the session workspace,
separate from the scientific result.

The singleton long mapping is not defended by the checked source account;
removing it alone is nevertheless not a complete implementation of the
endingless knee history. Retaining the same long result by a lexical
matcher would hide rather than solve this problem.

## Propagation (only after verdict)

The executed sc033-dative-candidate compares the full wrapper over all
387 rows, overrides only knee's selected PGmc input and implements the
two declared component corrections. Ten component and two staged checks
pass, including short e/i, acute notation, following short/long i and j
negatives, final-w behavior and the native hue control. Only knee's
input/output changes; no output is missing or ambiguous, and all protected
canonical artifacts remain unchanged during the private assay.
The persisted report preserves the old cnēow comparison target, so its
knee mismatch is the declared cell migration, not an unexplained failure.

The production FST retains the same composition order and stable names:
OEEwLongContext is now w+j only; EnglishBreakingWContext excludes
i/í/ī/ḯ/j after w. No broad early-ending rewrite is landed.
SC044's other vowel/consonant contexts and historical adjudication status
are unchanged; this is its directly coupled conditioning repair, not an
independent resolution of the broader breaking chronology.

Corpus row2085 changes selected input *knéwą → *knéwai and comparison
cnēow → cneowe. Citation PROTO stays *knéwą; both input/citation stages
are explicitly pgmc, independently of confidence. Tokens, IPA, alignment,
source note and classification follow the dative. No non-OE sibling or
row identity changes. The classification is late_analogy, routing the
detailed new model entry into Late analogy and paradigm-cell selection;
the selected dative is itself regular. The old DEV_NOTES slice is
explicitly superseded, not rewritten to fabricate earlier agreement.

The exact input/target/output migration is SOURCE-owned by
approved_input_migrations.tsv and approved_cell_migration.json.
adjudicate.py SC033 --adopt-cell-baseline verifies every field of every
row against the explicit before/after declaration, preserves the old
baseline as *_pre_sc033.*, verifies the immutable legacy380 archive,
and forbids all undeclared output, context, identity or multiplicity drift.
Routine refresh cannot perform that adoption.

Expected active fingerprints, computed from the declared one-row
transition and independently reproduced from production before adoption:
- evaluator selected387: ffad47aefc01423953fc57784fe6a6f6cef31dcca9bbdbb7b36b06a63dc552bc;
- lexical selected387: 76bb0ffda672c700cc5b1cfe95a0ec491047d65ccbfaff290209842fabf3d344;
- active original380: 70bdaba537d8f6b6bb7d872d00eefbef75127d2d77689af7ba01b35a79ebce39.

The seven existing mismatches and all other 386 finals remain unchanged.
The immutable legacy380 and older gift/context transition archives are
not repointed or rewritten. Historical recipe/result pairs retain their
original source/corpus hashes; post-SC033 controls are distinct.

Owners updated together: this memo, grouped dossier/current synthesis
ledger, SC033/044 readers, Chapter4's glide paragraph, knee's detailed
model/ledger and hue's contrast. Source-to-book projection remains through
the canonical refresh/finalize graph.

### Verification and publication closeout

Production evidence now records one SC033 firing, hue2332; knee2085
does not enter its retained long-output component. The selected dative
follows *knéwai → *knéwē → *knéowē → *knéowe → cneowe.
All 387 selected rows have deterministic output: 380 match and the
seven existing mismatches remain. All other 386 finals are unchanged.
The adopted active fingerprints above were reproduced; the pre-SC033
baseline bytes and immutable legacy380 archive are preserved.

The integrated Germanic suite passed 700 tests and 6,200 subtests.
The subsequent serial protected post-SC033 production assay passed
49 component, nine staged and ten corpus assertions, with full-wrapper
identity across all 387 rows, no rejection or ambiguity and no
protected-artifact mutation. Historical recipe/result pins were not
replaced. After the final stem-typography correction, the focused
SC033/publication regression run passed 125 tests.

The standard unbypassed book build passed the semantic, citation,
gloss/predicted-form, index/parity, bibliography-locator and heading
gates, including all 18 index architecture negative fixtures. The
persisted combined draft contains 301 PDF pages. Knee is section9.9
in Chapter9, Late analogy and paradigm-cell selection, printed
pp.249–251; its selected trace, source comparisons, paradigm table,
confidence and classification were inspected in the actual PDF.
The corrected cneow- stem emphasis renders normally, without a stray
asterisk or unintended paragraph-wide italics.

The printed SC033 and SC044 discussions/definitions (pp.67,78),
Chapter4's knee paragraph (p.59), hue's contrast (pp.185–186), and
the native/reconstruction index entries (pp.294,297) were also
inspected. Short/long quantity signs, high-front blockers, cited
page locators and the new lexical placement are coherent. No new
vocabulary, commit or push is part of this closeout.

## Residue

The regular dative-cell selection and its exact migration are authorized.
This does not adjudicate the general endingless low-vowel/offglide
interface or implement paradigm leveling. The two broader private recipes
remain unexecuted diagnostics, not adopted historical chronology.
A generic early ending repair must be censused across all affected rows;
a leveled target must not be called a regular sound-law reflex.

Hue's omitted early raising remains an explicit local limitation.
The high-front exclusion in the w-breaking consumer is repaired.
SC032/034/105 and the broader breaking rivals remain unadjudicated here.
