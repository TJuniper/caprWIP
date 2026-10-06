# Historical chronology audit plan

## Purpose

The current CAPR cascade has been tested carefully for **relative computational
dependencies**, but the resulting sequence should not automatically be treated as
an absolute historical chronology.

The next phase will review the historical organization of the sound changes and
the structure of Version 1 of the book.

The audit must distinguish five different things:

1. **Historical stage**
   At what historical stage does scholarship place the change?

2. **Historical relative chronology**
   Which other changes must historically precede or follow it?

3. **FST dependency**
   Which ordering relations actually affect CAPR outputs?

4. **Current cascade position**
   Where has the rule been placed in the current implementation?

5. **Reader-facing book order**
   Where should the change be discussed in a historical account?

A pair of rules may commute computationally while scholarship nevertheless places
one substantially earlier than the other.

Therefore FST regression evidence establishes necessary computational orderings,
not automatically the complete historical chronology.

---

## Existing CAPR research archive

CAPR already contains **very extensive historical and chronological research**.
Do not begin any audit as though the literature review needs to be rebuilt from
scratch.

**The repository itself is the primary research archive for this audit.**

Relevant existing research layers include, but are not limited to:

* `Germanic/docs/sound_changes/change_reports/full/` — per-rule change reports
* `Germanic/docs/sound_changes/literature_dossiers/` — source-based dossiers
* `Germanic/docs/sound_changes/book_dossiers/` — book-chapter dossiers
* individual `reader_facing/*.md` sound-change discussions
* `reader_facing_one_direction_chronology_review_01.md`
* `reader_facing_chronology_evidence_audit_01.md`
* `reader_facing_chronology_evidence_qc_01_report.md`
* chronology cards and chronology-control material
* lexical model-entry evidence and derivational witnesses
* existing source-specific notes elsewhere in the repository
* bibliography records and already cited page/section references

The existing work already records substantial information about:

* historical classification;
* source attribution;
* relative chronology;
* one-sided vs two-sided chronology constraints;
* lexical witnesses;
* wrong-early and wrong-late outputs;
* FST dependencies;
* places where literature rather than corpus interaction motivates current
  placement.

Do **not** duplicate this work into a new parallel research system.

### Dossier workflow: inventory first

For each rule, the dossier workflow must begin:

1. **Inventory existing CAPR research.** Locate all repository artifacts
   relevant to the rule.
2. **Reconcile the existing research layers with one another.** Where layers
   agree, treat the claim as established. Where they disagree, report the
   disagreement before deciding which is right.
3. **Identify genuine gaps.** Contradictions, outdated conclusions, or questions
   the existing work leaves genuinely open.
4. **Only then consult external sources**, and only to resolve a specific
   open question.

New literature research must be **gap-driven**, not comprehensive by default.
If the repository already contains adequate source research for a point, cite
and reuse that work rather than repeating the search.

### Dossier section structure

Every sound-change dossier must include an opening section:

**§ Existing CAPR research** — list the relevant repository artifacts and
summarize what has already been established.

Then separate:

**§ Already established** — claims supported sufficiently by existing CAPR
research.

**§ Open questions** — questions that remain unresolved after reconciling
existing CAPR material.

**§ Additional research required** — external source work needed specifically
for those open questions.

The purpose of the historical-chronology phase is primarily to **synthesize,
reconcile, stage, and where necessary correct the substantial research already
done**, not to restart the research.

---

## Provisional historical backbone

For the English line, use the following broad staging framework:

```
PIE → PGmc → PNWGmc → PWGmc → Pre-OE → OE
```

with Proto-Anglo-Frisian (`PAF`) available as an optional analytical stage
between PWGmc and Pre-OE when a source or adopted reconstruction requires it.

The ontology must not overfit to Ringe & Taylor or any one Stammbaum.

Relevant analytical categories may also include:

* northern West Germanic;
* North Sea Germanic / Ingvaeonic;
* Anglo-Frisian;
* English-specific / Pre-OE;
* dialect-specific Old English developments.

These categories should not automatically become proto-language nodes.

Historical stage and geographical/genealogical **scope** are separate dimensions.

---

## Provisional Version 1 chapter structure

The intended large-scale historical chapters are provisionally:

1. Proto-Germanic → Proto-Northwest Germanic
2. Proto-Northwest Germanic → Proto-West Germanic
3. Proto-West Germanic → Anglo-Frisian / later shared West Germanic developments
4. Anglo-Frisian / prehistoric English → Old English

The exact titles and boundaries remain open pending the rule-by-rule audit.

In particular, CAPR should be able to discuss scholarship that does not posit a
discrete Proto-Anglo-Frisian node.

Do not force every rule into these chapter titles before its historical dossier
has been reviewed.

---

## Source programme

Build historical notes from multiple traditions rather than using Ringe & Taylor
as the sole chronology.

Important sources include, where relevant:

* Ringe & Taylor
* Hogg
* Campbell
* Sievers–Brunner
* Luick
* Fulk
* Crist
* Lass
* Versloot
* Waxenberger
* other specialist literature required by individual changes

For each sound change, record:

* what each source calls the change;
* stage or scope assigned;
* examples;
* absolute dating evidence if any;
* relative chronology;
* qualifications or competing analyses;
* exact citation/page/section.

Many of these records will already exist in CAPR research files. Always check
for existing citations and notes before generating new ones. Add to existing
records rather than replacing them.

The reader-facing historical discussion should eventually be able to say
explicitly that different authors analyse a development differently, rather than
silently choosing one terminology.

---

## Rule-by-rule workflow

Do not audit the chronology through one large automated rewrite.

Review **one sound change at a time**.

For each sound change, first create an evidence dossier. Do not modify the rule
during the dossier stage.

Each dossier should record:

* stable internal rule identifier;
* current SC number;
* current reader-facing name;
* current FST position;
* current implied stage;
* actual transformation implemented;
* all lexical rows to which the rule applies;
* existing CAPR chronology witnesses;
* FST lower and upper ordering boundaries;
* historical stage according to the literature;
* historical relative chronology;
* comparative/attestation evidence;
* disagreements among sources;
* proposed chapter;
* proposed stage;
* proposed scope;
* confidence;
* recommended action.

Possible actions must remain distinct:

* no change;
* prose clarification only;
* reader-facing rename;
* stage-metadata correction;
* chapter reassignment;
* FST cascade move;
* split one implementation into multiple historical changes;
* combine or otherwise revise implementation.

Do not move a rule merely because its current internal identifier has an
historically inaccurate prefix.

---

## Confidence categories

### A — secure

Multiple independent authoritative sources agree and no significant contrary
analysis is known.

A change may be proposed confidently, but still report it before editing the FST.

### B — strong but analysis-dependent

The evidence is good, but the result depends on subgrouping, chronology, or
another theoretical choice.

Present alternatives. Do not silently treat the choice as consensus.

### C — unresolved

Evidence gives only partial chronology, sources disagree materially, or the
reconstruction is uncertain.

Leave the issue open and describe the uncertainty.

---

## Repository issues

Only describe an existing stage assignment as a repository **bug** when confidence
is very high.

A strong default threshold is:

* at least two independent authoritative scholarly sources;
* no known substantial contrary position relevant to the particular claim.

Otherwise keep the question in the chronology audit rather than asserting that
the current implementation is wrong.

---

## First pilot: final *z*-deletion

The first detailed audit should concern the current rule:

`PGmcFinalZDeletion` / SC020

because the present reader-facing text creates a possible historical contradiction:

* SC003 West Germanic rhotacism is described as following earlier West Germanic
  final-*z* loss;
* the current numbered/cascade presentation places final-*z* deletion at SC020;
* the transducer evidence for SC003 supplies an upper boundary but does not
  establish that SC003 must computationally precede SC020;
* the SC019–SC020 evidence establishes the local relation final long-*ō*
  raising → final-*z* deletion, but does not by itself fix the absolute
  placement of *z*-loss within the whole early cascade.

**Begin by inventorying existing CAPR research** on:

* SC020 `PGmcFinalZDeletion`;
* SC003 rhotacism insofar as it presupposes earlier *z*-loss;
* SC019 final long-*ō* raising;
* any change reports, dossiers, chronology reviews, lexical witnesses, and
  source notes involving final *z*.

Produce an inventory of what CAPR already knows before doing any new literature
search. Use the first pilot partly to determine how much of the future
chronology audit can be accomplished by synthesizing existing research rather
than generating new research.

The pilot must then determine what historical development(s) the current
broad rule:

```
*z → 0 / _#
```

actually represents.

In particular investigate whether the literature distinguishes:

* an early pan-West-Germanic loss of final *z* in particular prosodic
  environments;
* later, geographically narrower *z*-loss;
* other final-*z* developments currently conflated by the implementation.

Do not move or split SC020 until every actual corpus application of the rule
has been inspected.

---

## Second pilot: rhotacism

After final-*z* deletion is understood, audit SC003 / `PGmcRhotacism`.

Known open questions include:

* its internal name appears historically too early;
* current prose itself calls it a later West Germanic development;
* historical relation to final-*z* deletion;
* whether the FST position needs changing or only the label/chapter/stage
  metadata.

Do not rename the stable internal Foma identifier merely for tidiness during the
research phase.

---

## Third pilot: *ai*-monophthongization

Then audit SC004 / `PWGmcAiMonophthongization`.

The current discussion distinguishes:

* an early Northwest Germanic word-final development;
* a broader generalization presently implemented by the rule.

Determine whether these belong to one historical change, different chronological
strata, or simply require more precise prose.

---

## New forms introduced by historical discussion

Adding historical discussion will inevitably introduce additional forms.

Use the existing semantic/index machinery consistently:

* reconstructed lexical evidence: `.recon .iv`;
* attested index-worthy evidence: `.iv`;
* model/internal stage only: `.recon`;
* counterfactual output: `.pred`;
* ordinary non-indexed lexical mention: `.lex` where appropriate.

Give new reader-facing lexical forms the required paragraph-level English glosses.

However, **a form cited in historical discussion does not automatically become a
transducer test item.**

Add it to computational test data only if it is deliberately being adopted as:

* a derivational witness;
* a chronology diagnostic;
* a regression case.

Comparative examples and historical evidence can remain prose/index evidence
without enlarging the FST dataset.

---

## Regression discipline for actual FST changes

When a rule is eventually moved, split, or materially changed:

* change one rule/change-set at a time;
* preserve a baseline of all current lexical outputs;
* run the full corpus after the change;
* inspect every output delta;
* distinguish expected consequences from regressions;
* stop if unexplained deltas appear.

Do not reorder several commuting rules merely to make the cascade look
historically tidy.

---

## Numbering

Keep existing SC numbers as stable legacy identifiers throughout the research
phase.

Do not repeatedly renumber rules while chronology is being revised.

Once the historical audit and chapter organization are stable, perform one
deliberate reader-facing renumbering pass so that the final SC sequence follows
book order.

Stable internal Foma identifiers may remain unchanged where renaming would add
risk without scholarly benefit.

---

## Chapter synthesis

Do not write the final chapter historical narratives before the rules assigned to
that chapter have been audited.

After the relevant sound changes are individually reviewed, synthesize:

* historical stage;
* competing scholarly reconstructions;
* major innovations;
* absolute and relative chronology;
* evidential basis;
* CAPR's modelling choices;
* remaining uncertainties.

The chapter narrative should make disagreements visible rather than smoothing
them away.

---

## Immediate next step

After this plan is committed, stop.

The next branch/task should begin with a **final-*z*-deletion dossier only**.

Do not simultaneously audit rhotacism, *ai*-monophthongization, or later rules.

The purpose of the first pilot is partly methodological: use it to establish the
dossier format and decide how historical chronology should interact with the
existing transducer before scaling the process to the rest of the cascade.
