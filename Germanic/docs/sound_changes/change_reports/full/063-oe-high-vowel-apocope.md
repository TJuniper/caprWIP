# OE high vowel apocope

### Sound-change report

#### Historical formulation

SC063 is **OE High Vowel Apocope**: final high vowels `*i`, `*u`, and `*ų` are
lost after heavy syllables and in the relevant trisyllabic configurations, but
not simply after every short stressed syllable. The basic historical claim is
stable across the handbook tradition even though older scholarship often folds
it into a broader account of unstressed-vowel loss rather than treating it as a
single named law [@Luick1914, §§304--308; @Campbell1959, §§345--349;
@HoggPhonology1992, p. 121; @RingeTaylor2014, §§6.8.1, 6.8.4; @Fulk2018, §5.6].

#### Source tradition

Luick gives the clearest older formulation: final `i/u` disappear after heavy
syllables and in the relevant trisyllabic environments, but not immediately
after a short stressed syllable. Campbell offers the most compact section-safe
handbook description of final unaccented high-vowel loss, while Hogg keeps
apocope and medial syncope conceptually adjacent without collapsing them into
one process. Ringe and Taylor sharpen the chronology by placing apocope after
general syncope and among the last prehistoric Old English sound changes, and
Fulk adds a useful caution about inflectional exceptions such as Mercian `-u`
retention [@Luick1914, §§304--308; @Campbell1959, §§345--349;
@HoggPhonology1992, p. 121; @RingeTaylor2014, §§6.8.1, 6.8.4; @Fulk2018, §5.6].

#### CAPR implementation

CAPR makes the rule far more explicit than a handbook formulation. The live
implementation separates heavy disyllabic branches, long- and short-diphthong
handling, heavy-by-position branches, trisyllabic branches, vowel-hiatus after
long vowels, and final `*x`/`h` environments. The historical core is still the
classical one: weight-sensitive and trisyllabic loss of final high vowels. The
special hiatus and final-`*x` clauses are better read as technical refinements
inside the model than as the central historical claim
[@Campbell1959, §§238, 345--346; @RingeTaylor2014, §6.6.1].

#### Place in the cascade

SC063 belongs to a late weak-tail neighborhood that includes `SC054` OE W Loss
Before I, `SC055` OE I Umlaut, `SC063` OE High Vowel Apocope, and `SC072` OE
Unstressed Long Vowel Shortening. This placement matters because the rule must
come late enough to preserve umlaut-sensitive developments on the left, yet
still early enough to precede the last cleanup of unstressed long vowels on the
right. It is therefore one decisive weak-tail reduction, but not the whole late
weak-tail story by itself.

#### Order evidence

The chronology card gives SC063 a safe window of `56-71` and fixes the main
anchors on both sides. `SC055 < SC063` is the most important left boundary: if
apocope is moved earlier than i-umlaut, forms such as `cȳ` and `brȳd` collapse
to `cū` and `brūd` because the final high vowel disappears before it can
condition umlaut. `SC054 < SC063` is a narrower left-side anchor in the same
late cluster. On the right, `SC063 < SC072` is enforced by forms such as
`fyrhte`: if later unstressed-long-vowel shortening moves ahead of apocope, the
derivation yields `fyrht` instead. Taken together, the evidence shows that
SC063 is late, but not final, inside the weak-tail sequence.

#### Interpretation

For book purposes, SC063 should be presented as a decisive but not terminal late
weak-tail reduction. The literature strongly supports the classical rule: final
high vowels are lost after heavy syllables and in the relevant trisyllabic
patterns, and this process is closely related to but not identical with medial
syncope. CAPR then shows how much technical branching is needed to implement
that apparently simple rule across a large derivational corpus. The historical
chapter should therefore keep the core claim central and treat the detailed
formal branches as model-level elaboration rather than as separate historical
laws.

#### Remaining cautions

The line between apocope and medial syncope still needs careful handling in the
prose, because the neighboring processes are related but not identical
[@HoggPhonology1992, p. 121; @RingeTaylor2014, §6.8.1]. The trisyllabic branch is the
most delicate part of the rule, and Mercian `-u` retentions such as `lytelu`
and `nētenu` warn against overgeneralizing every branch of the implementation
[@Fulk2018, §5.6]. The special final-`*x` and vowel-hiatus clauses are useful
model refinements, but they should not be mistaken for the whole historical
claim [@Campbell1959, §§238, 345--346; @RingeTaylor2014, §6.6.1]. More broadly,
the chapter should avoid turning every FOMA branch into a separate historical
assertion.
