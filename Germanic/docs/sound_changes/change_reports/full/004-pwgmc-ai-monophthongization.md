# EAF ai-monophthongization

### Sound-change report

> **Corrected PROTOFORM pass.** SC004 is the stressed/root change `*ái > *ā`
> only. The unstressed development `*ai > *ē` (final and nonfinal) is the
> separate, earlier SC014 `PNWGmcUnstressedAiMonophthongization`. Application
> analysis uses the Old-English-row `PROTOFORM` (the production input): under it
> `loam` (`*láimą`) is stressed and `whine` (`*xwḯnaną`) carries no `*ai`.
> Implemented on branch `historical-cascade-order` (split commit `f59b758d`,
> PROTOFORM correction `9c71aed3`).

#### Historical formulation

SC004 `EAFAiMonophthongization` is the monophthongization of stressed/root `*ái`
to `*ā` in the English line (later fronted to `ǣ` in the relevant OE
environments). In the trace it is visible across 24 stressed families such as
`soul`, `stone`, `bone`, `deal`, `ghost`, and `loam`. It is best understood as a
North Sea Germanic / Anglo-Frisian areal development, not as a single dated node.

#### Source tradition

Ringe and Taylor treat the monophthongization of `*ai` among the widespread
post-PNWGmc vowel developments of the English line [@RingeTaylor2014,
pp. 40--41, §6.1.5]; Fulk lists `ai`/`au` among the North/West-Germanic shared
innovations against Gothic [@Fulk2018, §5.2]; Campbell describes the
Anglo-Frisian `*ai > ā` (later fronted) as an English-line development
[@Campbell1959, §§133--134, §417]. Versloot 2017 (consulted directly) argues
that stressed/root `*ai` monophthongization spread in two areal waves through a
North Sea Germanic dialect continuum (c. AD 400--900), a diffusion rather than a
single inherited Proto-Anglo-Frisian node, with Old English among the broadest
monophthongizers. That source layer supports precisely the stressed side modelled
here; the unstressed side is SC014's evidence.

#### CAPR implementation

CAPR models the change as a single EAF-stage rule in the EAF corridor:

```foma
define EAFAiMonophthongization [
    {*ái} -> {*ā}
];
```

The rule targets the stressed diphthong `*ái` only (a distinct segment from
unstressed `*ai`), so it is independent of SC014. No nonfinal unstressed root
`*ai` remains in the corpus once PROTOFORM is used, so no `{*ai} -> {*ā}` branch
is required; the earlier unrestricted branch was an artefact of the PROTO-based
misclassification of `loam` and `whine`. The former bundled identifier
`PWGmcAiMonophthongization` is retained as a documented compatibility alias but
is not composed in any pipeline.

#### Place in the cascade

SC004 executes at cascade position 25, immediately after SC028
`PNWGmcPreconsonantalXLoss` and before SC029 `OEAwwjResolution` (the EAF
corridor). Its SC number stays SC004 even though its executable position no
longer follows numerical order.

#### Order evidence

First-break testing with the corrected stressed-only rule reproduces the one
historical boundary at order 33 across `SC036` OE Inter Stress Raising: delaying
SC004 past that stage makes PGmc `*sáiwalō` yield `sāwel` rather than expected OE
`sāwol` (371/372 match at the break). The current placement (pos 25) sits safely
before that boundary. The earlier side has no corpus break toward the head. The
formal crossing analysis (`sc004_sc014_interaction_report.md`) shows SC004's only
genuine dependency is on SC036; its other non-commutations are feeding artefacts
on non-corpus `EnglishProtoInput` forms.

#### Interpretation

SC004 is the later, areally diffused North Sea Germanic monophthongization of
stressed `*ai`. The EAF corridor is an operational modelling home for a change
whose real history is a dialect-continuum diffusion rather than a discrete node;
the SC036 `soul` boundary is its one usable chronological anchor.

#### Remaining cautions

The EAF stage is a modelling corridor, not a demonstrated discrete
Proto-Anglo-Frisian node; the prose should say so. Old English `ā` is fronted to
`ǣ` by later change in the relevant environments, so the surface reflex is not
always `ā`. `loam` is a stressed witness; `whine` is not an ai-monophthongization
case.
