### Lexeme report

#### Reconstruction and early-stage alternatives

This row is an `early_analogy` case, so the central distinction is between the cognate-set proto and the stage fed to the FST. The row preserves `PROTO = *kráftiz`, while `PROTOFORM = *kráftaz` is the project input. The note explains why: an inherited i-stem in `*-iz` would create an i-umlaut environment and predict an OE vowel in `e`, not the attested `æ`. The project therefore adopts an early analogical stem with a non-fronting ending, while keeping the citation etymology visible.

#### Chronological source dossier

- `Germanic/data/germanic-aligned-final.tsv`: the row note cites [@Kroonen2013] for a `kraftu-` noun and [@Orel2003] for `*kraftiz ~ *kraftuz`, then explains why the Old English reflex rules out a straight i-stem analysis.
- The sound-history logic behind the vowel argument follows the standard OE umlaut chronology in [@Campbell1959; @HoggGrammar1992; @RingeTaylor2014].

#### Old English philology

The target `cræft` is treated here as the ordinary Old English citation form. The philological issue is not attestation, dialect, or spelling variation, but rather which early Germanic stem configuration best explains the inherited OE vowel.

#### Project problem and solution

This is an `early_analogy` solution. The citation proto is kept for the cognate set, but it is not the right input for the FST if the goal is to model the OE form historically. Feeding `*kráftaz` into the cascade avoids the unwanted i-umlaut trigger and yields the expected `cræft`, while still making the older etymological disagreement transparent.
