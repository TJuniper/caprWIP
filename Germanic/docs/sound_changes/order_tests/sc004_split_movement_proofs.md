# SC004 split — movement proofs and outputs validation

> **Superseded by the corrected PROTOFORM pass (commit `9c71aed3`).** The
> "25 vs 26" reconciliation and the loam/whine component attributions below were
> computed from the cognate-set `PROTO` field. The production input is the
> Old-English-row `PROTOFORM`, under which SC004 (stressed `*ái`) applies to 24
> corpus rows (23 attested + roe), SC014 (unstressed `*ai`) applies to 2 (span,
> meed), and whine/withy are not ai cases. See
> `sc004_component_application_report.tsv` and
> `sc004_sc014_interaction_report.md`. Retained as a historical research record;
> the outputs-preservation result (frozen `aaf19ba9…480e`) still holds.

Research record for the Outcome-C implementation. Tools:
`tools/sc004_split_experiment.py` (whole-cascade equivalence over
`EnglishProtoInput`) and `tools/sc004_outputs_check.py` (the decisive corpus
`outputs_sha256` test), both run in the backend container.

## Genuine-history placement (validated)

Modelling what the field genuinely holds:

- **SC014** = component A, word-final unstressed `*ai > *ē` (PNWGmc, early),
  placed at the **old SC004 head position**.
- **SC004** = the general component, `*ai/*ái > *ā` (EAF / North Sea Germanic,
  later), placed in the **EAF corridor: immediately after SC028
  `PNWGmcPreconsonantalXLoss`, before SC029 `OEAwwjResolution`**.
- The old SC014 `{*ăi} -> {*ē}` no-op is removed (a documented remnant, DEV_NOTES
  §17.12; `*ăi` occurs in 0 corpus rows).

### The decisive test: attested corpus outputs are preserved

`sc004_outputs_check.py --after PNWGmcPreconsonantalXLoss` (both B formulations):

```
experimental outputs_sha256 = aaf19ba9…480e
production   outputs_sha256 = aaf19ba9…480e
frozen       outputs_sha256 = aaf19ba9…480e
matched=372 mismatched=8 accepted=380   OUTPUTS PRESERVED: True
```

The genuine-history cascade produces **exactly** the frozen attested Old English
outputs. This is the meaningful invariant: the model still derives every attested
form correctly with the monophthongisation to `*ā` in its historically later
position.

### General component B: explicit non-final environment

Two formulations of the unstressed sub-rule were tested; **both** preserve
`outputs_sha256`. The **non-final** form is adopted for robustness (it does not
depend on SC014 having run immediately beforehand, per task §2):

```
B (unstressed): {*ai} -> {*ā} || _ ?      (non-final)
C (stressed):   {*ái} -> {*ā}
general SC004:  B .o. C
```

### Whole-cascade equivalence over `EnglishProtoInput` (documented exception)

`sc004_split_experiment.py` shows the moved general component is `test
equivalent` = TRUE only through **after `PNWGmcAToUBeforeM`** and FALSE from
`PWGmcEarlyIApocope` onward — i.e. it does **not** achieve whole-*language*
equivalence at the EAF position. This is the **expected signature of a genuine
chronological reorder**: the new cascade differs from the old bundled one on
*hypothetical, non-corpus* inputs where an intervening rule interacts with
`*ai/*ái`. On the **attested corpus** the two agree exactly (`outputs_sha256`
identical). Per the project's guidance, we model the genuine history and require
the attested outputs to hold; we do **not** force the general component back to an
early slot merely to obtain whole-language equivalence. The bundled analysis is
not restored.

The crossed-rule interactions (documented, corpus-neutral): the general
component's first non-commutation over `EnglishProtoInput` is with
`PWGmcEarlyIApocope`; further non-commutations occur among the PNWGmc raising /
lowering rules between the head and the EAF slot. None changes any attested
output.

## 25 vs 26 reconciliation

The component application report finds **26** corpus protoforms carrying
`*ai/*ái`; the inventory records **25** SC004 trace occurrences. The difference is
**`roe`** (`*ráixōn`, ID 2156): SC004 Component C applies (`*ráixōn → *rāxōn`),
but `roe` has **no attested Old English counterpart** (COUNTERPART = `-`), so the
inventory's attested-occurrence count excludes it. Both numbers are correct under
their definitions: 26 = corpus protoforms SC004 rewrites (incl. the unattested
`roe`); 25 = attested OE lexemes affected. This is stated, not silently chosen.

## Final placements adopted

| | Foma identifier | Rewrite | Executable position | hist_stage |
| --- | --- | --- | --- | --- |
| SC014 (A) | `PNWGmcUnstressedAiMonophthongization` | `{*ai} -> {*ē} \|\| _ .#.` | head (old SC004 slot) | pnwgmc |
| SC004 (B+C) | `EAFAiMonophthongization` | `[{*ai}->{*ā} \|\| _ ?] .o. [{*ái}->{*ā}]` | after SC028, before SC029 | eaf |

Executable and reader/SC-number order no longer coincide, which is expected.
