# Introduction {.unnumbered}

## From sound law to derivation {.unnumbered}

Historical linguists ordinarily test an etymology by carrying a reconstructed form through the sound changes that separate it from its alleged reflex. Most such derivations remain implicit. A scholar knows that Proto-Germanic \emph{*p} yields Old English \emph{f}, that West Germanic \emph{*z} became \emph{r} under the appropriate conditions, and that one change must have preceded another because the reverse order produces the wrong form. For a single word this mental arithmetic presents little difficulty. Across hundreds of words and scores of interacting changes it becomes treacherous. Each step may look familiar while the derivation as a whole is false.

In computer-assisted phonological reconstruction (CAPR), I represent each sound law as a finite-state transducer and compose the transducers in the order argued for below. The resulting cascade applies every change without discretion: the same rule, with the same environment, reaches every eligible form. A proposed reconstruction either yields the Old English comparator or it does not. Moving a rule may repair one derivation and destroy another. Both results deserve attention, for a failure locates the point at which phonology ceases to suffice and philology must decide among analogy, borrowing, dialect mixture, uncertain attestation, or a faulty reconstruction.

No new principle is involved. The Neogrammarians already demanded exceptionless sound laws and an account of apparent exceptions [@OsthoffBrugmann1881]. Their formula was the \emph{Ausnahmslosigkeit der Lautgesetze}. Formalization merely enforces that demand mechanically: every eligible form bears the stated consequences. The computer cannot decide which reconstruction is historically defensible, but it prevents the investigator from forgetting what that reconstruction entails.

I apply this method to the development of Proto-Germanic and early West Germanic forms into Old English. Germanic makes a severe test. Its historical grammar rests on two centuries of philological labor, while Old English offers abundant but orthographically and dialectally varied testimony [@Campbell1959; @HoggGrammar1992; @RingeTaylor2014; @Fulk2018]. A computational account cannot plead scarcity of evidence. It must reproduce familiar developments, identify the evidence for their order, and explain why its input sometimes differs from the headword printed in an etymological dictionary.

## The formal claim {.unnumbered}

A sound change defines a relation between strings. For each etymology I supply a reconstructed input to an ordered series of such relations and compare the result with an Old English form. Kaplan and Kay demonstrated that the familiar rewrite rules of phonology admit a finite-state interpretation [@KaplanKay1994]; Foma gives that interpretation executable form [@Hulden2009]. A toy rule deleting final \emph{*z} may be written:

```foma
define ToyFinalZLoss [{*z} -> 0 || _ .#.];
```

The notation states a target, an output, and an environment. Actual rules also refer to segment classes, stress, syllable weight, word boundaries, and the output of earlier changes. A loose prose formulation can conceal choices that code must resolve. Does the rule affect every vowel or only short vowels? Does a following consonant block it? Does it apply before or after the loss of a final syllable? A transducer forces each question into the open.

Order gives the cascade its historical content. An early change may create the environment for a later one and thus feed it; alternatively, it may remove that environment and bleed it. A word affected by both changes can therefore establish their relative chronology. Other changes commute across the available lexicon: reversing them alters no output in the active dataset. Such a result does not prove simultaneity or historical indifference. It shows only that the present evidence fails to order them. Throughout this book I distinguish chronology compelled by the tested forms from placement adopted on the authority of the historical grammars.

Backward reconstruction requires a further restriction. An unrestricted inverse transducer will propose formally possible strings that no Germanic language could have inherited. I therefore restrict backward reconstruction with an inventory and a statement of permissible ancestral forms. Reconstruction always combines correspondences with a theory of what could count as a word in the \emph{Grundsprache}; this restriction states that theory rather than leaving it tacit.

## Inputs, targets, and success {.unnumbered}

I compare a selected earlier Germanic form with a selected Old English target. Neither selection is innocent. Dictionaries cite lexemes, but sound change operates on word-forms. The ancestor of an Old English plural, preterite, or oblique case may differ from the reconstructed lemma in precisely the material on which a later sound law acts. Kroonen and Orel provide indispensable lexical reconstructions, while the grammars often supply the paradigm history needed to choose the actual input [@Orel2003; @Kroonen2013; @RingeTaylor2014].

I therefore distinguish the citation reconstruction from the transducer input. The former identifies the etymon; the latter represents the paradigm cell or remodeled stem whose history is at issue. Where the two differ, the lexical entry states the difference and argues for it. This prevents a convenient input from masquerading as a received reconstruction. An unmotivated alteration made solely to secure the desired output would empty the exercise of historical meaning.

The distinction is concrete in Old English [*sċuldrum*]{.iv lang=oe sort=sculdrum} 'shoulders, dative plural'. Its inflectional history requires an input of the type [skúldramiz]{.recon .iv lang=pgmc display=*skúldramiz sort=skuldramiz} 'shoulders, reconstructed dative-plural input'; the singular headword represents a different paradigm cell.

The target also requires judgment. Old English spelling varies by date, dialect, manuscript, and editorial practice. The cascade may produce an internal phonological symbol that an orthographic transducer then maps to a normalized written form. A string match at this final stage cannot by itself establish an etymology; conversely, a superficial spelling mismatch need not disprove one. I treat phonological development and orthographic normalization as separate operations so that exact computation does not confuse notation with history.

Within these limits a successful derivation has three senses. It succeeds formally when the output string matches the target. It succeeds philologically when the chosen input and comparator are the proper forms to compare. It succeeds historically when the proposed path agrees with the wider Germanic evidence. The first kind of success is cheap. The argument of the book concerns the conjunction of all three.

## The evidence of failure {.unnumbered}

Regular sound change makes irregularity legible. If an inherited form refuses to pass through an otherwise successful cascade, the mismatch demands a name. Analogy may have replaced the expected reflex with a form drawn from another paradigm cell. Borrowing may have introduced the word after the relevant changes. A dialectal form may lie outside the modeled West Saxon path. The target may be late, corrupt, or normalized beyond what the manuscript evidence warrants. Finally, either the reconstruction or the rule may be wrong.

These possibilities should not be suppressed by narrow, lexeme-specific “sound laws.” A system that derives every target by multiplying exceptions has only encoded its answers. I instead distinguish several classes of non-regular result: attested variants, early and late analogy, reconstructed Old English comparators, known but unmodelled phonological and morphological developments, and unexplained exceptions. The categories are claims, not housekeeping labels. They identify where regular phonology ends and what additional history the evidence requires.

This treatment follows the original Burmish CAPR work, in which resistant forms often disclosed loans or mistaken cognate assignments. Old English shifts the balance toward morphology and analogy, but the methodological advantage remains the same. Failure concentrates inquiry. It tells us which assumption—input, target, environment, order, or lexical history—must bear the explanation.

## Evidence for relative chronology {.unnumbered}

The chronology chapters combine three kinds of evidence. First come the statements of the standard historical grammars. These establish the received description and often the broad order of developments [@Campbell1959; @HoggGrammar1992; @RingeTaylor2014; @Fulk2018]. Second come individual witness words. A derivation that succeeds under one order and fails under the reverse order supplies direct lexical evidence for that relation. Third come exhaustive order tests across the active dataset. These reveal whether an apparently decisive relation is local, whether other words contradict it, and how far a rule can move without disturbing any output.

Suppose that a consonant change creates the environment for a later vowel change. Under the received order both apply and the Old English target emerges. Reverse them and the vowel change misses its environment. The word then supports the priority of the consonant change. The converse case is equally informative: if an early rule creates a segment that a later rule would wrongly alter, the creating rule must follow the other. When reversal changes no output, the lexical evidence leaves the order open even if philological considerations still favor one placement.

A note on notation: a superscript dagger placed immediately before an italicized form marks a concrete predicted output generated by a counterfactual manipulation of the rule order (for example, moving a change earlier or later than argued). This dagger indicates that the marked form is a model prediction, not an independently attested historical form; reconstructions remain starred in the usual way.

Sims-Williams argues for mechanizing precisely this kind of reasoning [@SimsWilliams2018]. Computation does not replace the historical argument; it makes the extent of that argument measurable. A traditional chronology may prove correct but less tightly constrained than its customary presentation suggests. A relation described as local may in fact rest only on a broad terminus. Such negative results are salutary. They separate what the data demonstrate from what a convenient exposition merely presupposes.

## Rules and words {.unnumbered}

The book accordingly moves twice through the same history. Part I begins with the ordered rules. For each development it states the historical problem, gives the rule in formal notation, and examines the evidence for placement. The code appears because it is part of the claim, but the code-name is never an explanation. `OEIUmlaut`, for example, is only a rule name; its linguistic content lies in the stated environment, the historical discussion, and the words whose derivations depend upon it.

Part II begins with the words. Each entry identifies the reconstruction, the selected input, the Old English comparator, and the derivational class. A trace shows which rules altered the form; the accompanying prose explains the philological decisions that the trace cannot make. Short entries record ordinary derivations. Longer ones treat doubtful reconstructions, variant attestations, paradigm-cell selection, or analogy. The asymmetry is intentional: equal database rows do not warrant equal historical discussion.

The reader can thus move in either direction. A chronology chapter names the lexical witnesses that constrain a rule; their entries display the complete derivations. A lexical entry invokes a change; the corresponding chapter explains its formulation and place in the cascade. The index verborum provides a third route through the material, gathering reconstructed and attested forms by language.

## Reproducibility and disagreement {.unnumbered}

An executable derivation identifies the exact point of disagreement. One reader may accept a sound change but reject its environment; another may accept the rule and dispute its order; a third may object to the selected paradigm cell or to the normalization of the Old English target. Each objection addresses a recorded decision. Given the same inputs, rules, and order, the stated outputs follow. Reproducibility here concerns those consequences, not the surrender of philological judgment to an algorithm.

Prose can sound settled while concealing several incompatible derivations. Code is less accommodating. A rule that is too broad damages words it was never designed to explain; one that is too narrow leaves legitimate reflexes untouched. A reconstruction plausible in isolation may fail after three later changes. The resulting embarrassment is a virtue of the method. Applying every rule to the whole lexicon subjects local analyses to a global test.

The converse danger is false precision. A deterministic cascade may tempt the reader to mistake exact strings for exact history. Every result still depends on choices about segmentation, symbol inventory, reconstruction, morphology, dialect, chronology, and orthography. I therefore cite the philological sources, display the selected forms, preserve unresolved exceptions, and distinguish tested order from source-based order. Those choices remain accountable to philology.

## The argument {.unnumbered}

A book must advance an argument. Mine is that traditional rule-based reconstruction becomes clearer when every proposed derivation can be executed, every rule must face the whole lexicon, and every failure is reported. The Germanic-to-Old-English case shows both the power and the boundary of that claim. Much of the history admits a coherent ordered account. The residue does not disappear: it resolves into morphology, analogy, variation, borrowing, imperfect attestation, and a small number of genuine problems.

The sound-change chapters ask how tightly the lexical evidence constrains the cascade. The lexical chapters ask whether individual etymologies survive that cascade without philological sleight of hand. Neither inquiry suffices alone. A formal system that reaches the targets by hiding doubtful inputs is bad historical linguistics; elegant prose that never reproduces its derivations is an incomplete formal account. Executable derivations make those two standards answer to one another.
