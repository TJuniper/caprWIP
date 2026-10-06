### Lexeme report

#### Reconstruction and early-stage alternatives

This row already uses a paradigm cell as its `PROTOFORM`: `*fūri`, interpreted in the project note as an inherited dative singular. That means the report must distinguish three things clearly: the broader lexeme 'fire', the specific inherited oblique form used for the FST, and the attested Old English target `fȳre`. The row note is explicit that the inherited phonological development of `*fūri` gives `fȳr`; the extra final `-e` in the attested form is analogical, not a phonological reflex.

#### Chronological source dossier

- `Germanic/data/germanic-aligned-final.tsv`: the note states that `*fūri` triggers i-umlaut and then loses final `-i` after a heavy syllable, producing `fȳr`, while `fȳre` reflects later analogical restoration.
- `Germanic/docs/DEV_NOTES.md` revisits the row several times and explicitly treats `fire` as the paradigm example of an oblique-cell input whose inherited ending is later restored analogically in Old English.
- The background chronology belongs to the standard OE vowel history used elsewhere in the project [@RingeTaylor2014; @Campbell1959; @HoggGrammar1992].

#### Old English philology

The target `fȳre` is a genuine Old English form, but the report should not call it the direct phonological outcome of `*fūri`. The conservative inherited outcome is `fȳr`; `fȳre` is the attested form after analogical re-addition of `-e`.

#### Project problem and solution

This is a `known_unmodelled` case. The FST is doing the historical phonology correctly and therefore stops at `fȳr`. The attested target differs because the noun was remodeled after the inherited apocope had already taken place. The report should therefore say that the row is historically understood but intentionally not forced into a fake deterministic match.

#### Paradigm probe

### Paradigm probe — fire / fȳre

- PROTO: *fūri
- PROTOFORM: *fūri
- DERIVATION_CLASS: known_unmodelled
- Morphology source: Hand-specified pilot comparison for the dat.sg. row input and the documented nominative-like outcome.
- ProtoGate bypassed: no
- Generated cells: dat.sg.
- Omitted cells: The inherited citation-form template is not yet generated automatically in v1; the probe centers on the TSV dat.sg. input and the known-problems interpretation.
- Winning form unique: no

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| dat.sg. | *fūri | fȳr | no | TSV input; attested target has analogically restored -e. |
