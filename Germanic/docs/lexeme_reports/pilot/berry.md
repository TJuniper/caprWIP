### Lexeme report

#### Reconstruction and early-stage alternatives

The project distinguishes the headword `*bázją` from the FST input `*bázjas`. This is again a paradigm-cell case: the aligned row keeps the nominative singular as the cognate-set headword but uses the genitive singular as the form that most directly yields the Old English target. The row note also records a phonological constraint relevant to the dossier: `*rj` did not geminate in Proto-West Germanic, so the explanation has to come from paradigm choice rather than from a hidden gemination rule [@RingeTaylor2014].

#### Chronological source dossier

- `Germanic/data/germanic-aligned-final.tsv`: `NOTE` identifies gen.sg. `*bazjas (> berġes)` as the intended pathway and cites the non-geminating `*rj` background.
- The current project treatment follows the general historical framework of Proto-Germanic to Old English development in [@RingeTaylor2014; @HoggGrammar1992].

#### Old English philology

The target `berġes` is an inflected form, not a normalized citation headword. For that reason the report should present the Old English evidence as a paradigm survival rather than as a lemma-form identity claim.

#### Project problem and solution

This is a `late_analogy` row. The citation form `*bázją` runs through the current cascade to `bere`, not to `berġes`. The genitive singular `*bázjas` runs to `berġes`, so the project records the inherited headword and the winning inflectional input separately.

#### Paradigm probe

### Paradigm probe — berry / berġes

- PROTO: *bázją
- PROTOFORM: *bázjas
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for ja-stem citation vs. selected gen.sg. cell.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen.sg.
- Omitted cells: dat.sg. and plural cells omitted in v1; the pilot focuses on the nominative/genitive contrast discussed in the TSV note.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *bázją | bere | no | Citation proto. |
| gen.sg. | *bázjas | berġes | yes | Chosen gen.sg. cell in TSV. |
