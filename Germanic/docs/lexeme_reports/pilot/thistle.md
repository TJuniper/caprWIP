### Lexeme report

#### Reconstruction and early-stage alternatives

This row separates the etymological headword `*θéstilaz` from the selected FST input `*θístilas`. The project note is explicit that the point is not merely vowel replacement: the nominative singular simplex without svarabhakti is not the manuscript target, while the broken nominative `þistel` belongs to a later OE phonological presentation layer that the current FST intentionally does not model for this cluster class. The genitive singular therefore gives the best conservative target form inside the inherited paradigm.

#### Chronological source dossier

- `Germanic/data/germanic-aligned-final.tsv`: `NOTE` identifies gen.sg. `þistles` as the paradigm-cell target and contrasts it with late West Saxon broken `þistel`.
- `Germanic/docs/DEV_NOTES.md` §17.18 records the row change to genitive singular and treats it as parallel to other consonant-cluster nouns whose inflectional stem is philologically cleaner than the normalized nominative.
- The background discussion of svarabhakti / parasitic vowels and cluster behavior is keyed in the row note to [@Campbell1959] and [@HoggGrammar1992]; the protoform choice also cites [@KlugeSeebold2011].

#### Old English philology

The target `þistles` is an attested inflectional stem form. The row note states that the only attested simplex nominative is the broken form `þistel`, whereas the project deliberately keeps the broader cluster-class policy aligned with unbroken poetic / early / Anglian-looking outcomes for comparable nouns. This is therefore a cell-based attested target, not a reconstructed nominative.

#### Project problem and solution

This is a `late_analogy` case. The citation-form path does not yield the selected OE target, while the genitive singular does. The solution is not to rewrite the etymology, but to distinguish `PROTO` from `PROTOFORM` and say openly that the inherited morphology is better preserved in the oblique singular.

#### Paradigm probe

### Paradigm probe — thistle / þistles

- PROTO: *θéstilaz
- PROTOFORM: *θístilas
- DERIVATION_CLASS: late_analogy
- Morphology source: Hand-specified pilot comparison for citation nom.sg. vs. selected gen.sg. cell.
- ProtoGate bypassed: no
- Generated cells: nom.sg., gen.sg.
- Omitted cells: Alternative *i-root nominative and other oblique cells omitted in v1; they should be added once the raising/epenthesis question is formalized.
- Winning form unique: yes

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|
| nom.sg. | *θéstilaz | þistl | no | Citation proto used for comparison. |
| gen.sg. | *θístilas | þistles | yes | Chosen genitive singular cell in TSV. |
