# Anglo-Frisian source pass — protocol record

This record follows the adjudication template's sections but is not an
SC adjudication. The explicit instruction for this pass prohibits changes
to canonical identities, metadata, executable rules, and corpus inputs.

## Identity

- Subjects: comparative pre-OE/pre-Old-Frisian chronology; SC030/SC043
  identity and shared/independent palatalization remain open.
- Executable identifiers: unchanged; identifiers are not historical claims.
- Base: clean `8e7dfd30`; source-ingestion commits `7742ce49`, `cea4ba7a`;
  work resumed on 2026-10-01.

## Question

Can the alleged shared innovations occupy a common ancestral stem while
respecting the independently supported daughter chronologies?

The Anglo-Frisian node is required by CAPR's modelling topology. This
question tests assignments around that node, not its removal.

A daughter-specific change obligatorily preceding the alleged shared
innovation refutes that placement, conditional on the correctness of the
ordering and the daughter-specific scope. Compatible chains do not alone
prove that a shared event occurred.

## Current state

SC030 and SC043 remain separately represented in the canonical registry.
The prior SC029/SC030 memo had treated different surface distributions as
proof of distinct historical identities. This research-state inference is
reopened, not the executable behavior or registry verdict.

The original nine specialist sources are now held as local, ignored PDFs and
committed printed-page-preserving texts. Source cards distinguish direct
evidence from reports of works not held. `missing-direct-sources.md`
records the acquisition gaps.

Four subsequent acquisitions are committed in `40c6752e`: Hogg 1979,
Goblirsch 1991, Bremmer 2009 (the corrected 2011 reprint) and Nielsen 2001.
Their PDFs remain local and ignored; their searchable Vision texts preserve
printed pagination. Direct-source cards for these additions remain pending.

## Diagnosis

- Firing census and counterfactual traces: not performed in this source
  pass; no scientific implementation is being proposed.
- Selected corpus inputs and downstream outputs: unchanged.
- Proposed future witnesses are not live firing claims or corpus rows.
  Their readiness assessment is static, not proof of successful derivation.
- The scope check excludes the pre-existing untracked
  `Germanic/fsts/tmp_probe.foma`, which is not part of this pass.

## Literature

The nine source cards hold source-specific page citations; the synthesis
holds the proposition-by-proposition comparison. Central contrasts include
Campbell's competing diphthong/fronting histories
[@Campbell1939, pp. 90–91, 104], Kortlandt's shared and daughter chains
[@Kortlandt2008, pp. 267–271], Laker's unresolved *au* argument
[@Laker2007, pp. 177–180], and Versloot's alternative to the traditional
pre-OE reconstruction [@Versloot2025, pp. 103–106].

The tree criterion is CAPR's stipulated analytical method, not a claim
that all these authors subscribe to it.

## Historical analysis

Stage, scope, and confidence remain the canonical registry's unchanged
values. The research documents preserve alternative chronological edges;
none is promoted to `chronology_edges.tsv`. An author's numbered sequence,
a structural inference, and a lexical ordering diagnostic are distinguished.

## Verdict

No new registry verdict is issued. Final historical identity decisions are
deferred. SC030/SC043 remain separate provisionally; palatalization is not
adjudicated. No machine-readable `Registry-verdict:` assignment is added
because this document does not alter a registry decision.

## Propagation

Only reference texts, reference index/bibliography, research cards and
comparative dossiers, and explanatory portions of the existing memos are
in scope. The normal control-plane refresh reported `CONTROL PLANE CLEAN`;
runtime bins, full trace, and interaction matrix were fresh by their
recorded provenance.

The full relevant suite passed: 568 tests and 5,879 subtests. The added
research-state assertion protects the deferred SC030/SC043 identity, without
changing executable or registry assertions. Bibliography
sanity and chapter citation ranges passed. Tracked FST sources, corpus
data, canonical registries, and frozen baseline files remain identical
to the base. No rebaseline was performed.

## Residue

Stiles 1995 and Fulk 1998 remain missing priority direct sources. Hogg 1979,
Goblirsch 1991, Bremmer 2009 and Nielsen 2001 were acquired subsequently
and now have retained ignored PDFs and page-preserving Vision texts.
Their direct source-card and comparative review remains separate from
acquisition; earlier reported positions are not retroactively direct evidence.
Other claim-dependent Nielsen works and Siebs remain gaps.
Luick is held; selected fronting/diphthong passages are located at printed
pp. 130–132, §§118–120, but §637 and corrupted phonetic glyphs remain
unverified without page images. These gaps
must not be filled by silently attributing a reporting author's reading
to the original scholar.

A future Frisian implementation first needs adjudicated daughter histories,
settled input conventions, and a witness inventory whose intermediate
states distinguish the competing chronologies. This pass supplies research
architecture, not authorization to implement that cascade.
