# SC098 research dossier: early apocope of word-final short high vowels in unstressed words (PWGmc)

Branch `sc001-sc020-chronology-audit`, corpus-maturation pass 01. Companion
to `corpus-maturation-01-candidate-adjudication.md` §2 (YOU / OE *ēow*).
Written **before** implementation, per the standing governance rules (rule
changes require dossier-recorded secondary-source backing **and** proven
computational correctness).

## 1. The historical phenomenon

Proto-West Germanic lost word-final short high vowels early — well before
the familiar Old English high-vowel apocope (SC063) and, crucially, before
i-umlaut (SC055) — in two distinct environments. The first, loss in third
and later syllables, is already implemented as SC006
(`PWGmcEarlyIApocope`). The second is the subject of this dossier:

> "Short high vowels were also lost after heavy syllables in unstressed
> words, but the loss was not uniform either lexically or dialectally. Thus
> OE and 'and' < \*andi exhibits very early loss of \*-i, but OHG enti does
> not; neither OE ymbe 'around' nor OHG umbi exhibits early apocope; OE iow
> 'you (dat. pl.)' definitely does (since it does not exhibit i-umlaut), but
> OHG iu might or might not; and so on. Forms without apocope probably
> escaped this change because they were proclitic (and so not phonologically
> word-final) ... But it is also likely that this early apocope was variable
> in any case." [@RingeTaylor2014, §3.1.4, pp. 57–58]

Ringe & Taylor use exactly this change to license the doublet they print for
the second-person plural pronoun:

> "PGmc \*izwiz 'you (dat. pl.)' (Goth. izwis) > \*iwwi > PWGmc \*iuwi ~
> \*iuw (see 3.1.4) > OE īow, OF iū, OS, OHG iu"
> [@RingeTaylor2014, §3.1.1, pp. 41–42]

The OE reflex continues the **apocopated** variant \*iuw: had the \*-i
survived to the OE period it would have triggered i-umlaut, and it did not
(R&T's own argument, pp. 57–58). West Saxon *ēow* beside early WS and
Northumbrian *īow* [@Campbell1959, §702, p. 283 note] shows the normal
WS/non-WS treatment of the resulting diphthong; the corpus targets the WS
citation form *ēow*.

## 2. Contrast with fully stressed disyllables

The change must not be generalized to stressed disyllables. R&T's regular
third-syllable law (SC006) explicitly spares them: final short high vowels
"clearly were not lost in fully stressed disyllables, since \*i survived
long enough to cause i-umlaut in OE even after an initial heavy syllable"
[@RingeTaylor2014, §3.1.4, p. 55]. Corpus examples that depend on this
survival include \*gastiz-type i-stems (OE *ġiest*) and \*fūri (OE *fȳr*),
whose umlaut requires the \*-i to persist to SC055. Any implementation of
the unstressed-word loss must therefore leave stressed disyllables
untouched.

## 3. Stage and relative chronology

1. **After PWGmc final \*-z loss (SC020).** In \*izwiz the \*-i only becomes
   word-final once the following \*-z is lost; R&T's printed sequence
   (\*izwiz > \*iwwi) has the z-loss already applied [@RingeTaylor2014,
   pp. 41–42; z-loss: pp. 44–45]. SC020 **feeds** SC098.
2. **PWGmc era, before the post-PWGmc northern developments.** R&T discuss
   the loss among the PWGmc Auslautgesetze (§3.1.4) and print the
   apocopated variant as a PWGmc form ("PWGmc \*iuwi ~ \*iuw"). It also
   preceded the monophthongization of unstressed \*au ("loss of \*-i in
   these endings preceded the monophthongization of unstressed \*au")
   [@RingeTaylor2014, p. 57]. Executable slot: immediately after SC020,
   before SC097 (post-PWGmc) and SC003 (rhotacism).
3. **Before i-umlaut (SC055).** This is R&T's dating evidence itself: OE
   *ēow* shows no umlaut [@RingeTaylor2014, pp. 57–58]. SC098 **bleeds**
   SC055 for this word.

## 4. Original implementation and its honest limits (superseded)

Original proxy (superseded by the SC031/SC098 context adjudication; composed in `EnglishProtoToOE` immediately after
`EAFFinalZDeletion`):

```foma
define PWGmcUnstressedWordFinalIApocope [
    {*i} -> 0 || {*w} {*w} _ .#.
];
```

Scoping rationale, recorded explicitly:

1. **The law is regular and prosodically conditioned.** Like Verner's law,
   it is governed by accent: word-final short high vowels dropped after
   heavy syllables in words that carried no word stress. R&T's apparent
   counterexamples are handled by their own proclisis account — proclitic
   forms "were not phonologically word-final" and so stood outside the
   law's environment [@RingeTaylor2014, pp. 57–58]. This project is
   neogrammarian: we adopt the proclisis account as the systematic
   explanation and reject R&T's residual hedge that the loss "was variable
   in any case" — sentence-level accent placement, not lexical diffusion,
   decides which sandhi variant each language continues. The PWGmc doublet
   \*iuwi ~ \*iuw is regular sentence sandhi (stressed vs. unstressed
   sentence forms), and OE continues the unstressed variant, as its lack
   of i-umlaut proves.
2. The corpus's protoform notation cannot currently carry word-level
   stresslessness: rows such as \*kūi and \*fūri are stressed words whose
   orthography happens to lack an acute (no stressed long ū/ō symbols),
   so a "word contains no acute" guard would wrongly sweep them in —
   \*fūri must keep its \*-i to umlaut to *fȳr*, while a general
   heavy-syllable formulation would equally destroy \*gastiz-type umlaut
   (§2).
3. The rule is therefore stated through a **proxy environment** (cf. the
   SC096 convention): final \*-i after the geminate \*ww produced by
   SC008, which in the present corpus is exactly coextensive with the
   law's unstressed-word domain — the \*izwiz-pronoun class for which R&T
   print the apocopated PWGmc doublet \*iuw and the umlaut-free OE reflex
   [@RingeTaylor2014, pp. 41–42, 57–58]. When future corpus additions
   bring in further unstressed-word lexemes covered by the law (e.g.
   *and* < \*andi), the proxy environment is to be widened so that it
   again matches the law's true domain.

This mirrors the precedent of SC096 (`RootNounNomZLoss`), where a regular
historical development whose true conditioning the notation cannot yet
express is implemented over an exactly coextensive proxy environment
rather than as a falsely general phonological law.

## 5. Interactions checked

1. **SC097 / SC003:** the rule's output ends in \*-ww; no final \*-z is
   created or destroyed, so the final-z corridor and rhotacism are
   unaffected.
2. **SC033/SC031 (downstream):** the surviving word-final geminate \*ww is
   vocalized by SC033 (`OEEwLongDiphthong`, extended to the word-final
   geminate context) before geminate simplification (SC031); see the
   modified `031-034-west-saxon-diphthong-chain.book-dossier.md`.
3. **SC055:** the trigger vowel is removed pre-umlaut, as the history
   requires (§3.3).

## 6. Computational validation

Sandbox compile of the full patched cascade in the backend container:

1. `ízwiz → ēow` (target: WS *ēow*);
2. `fédwōr → fēower` unchanged (the \*dw sibling of the Stiles class);
3. `xwáz → hwā`, `kūi → cȳ`, `fūri → fȳr`, `gastiz → ġiest` unchanged;
4. full regression of all 380 legacy protoforms against
   `cascade_baseline_outputs.tsv`: **0 differences** — the legacy-subset
   fingerprint `a72bdeb8…` is preserved.

## 7. Identifier allocation

`SC098` is the next free stable ID (SC096/SC097 allocated by the three-rule
programme; SC058 and SC077 are retired, not free). Proposed foma name:
`PWGmcUnstressedWordFinalIApocope`. Reader-facing name: "Early apocope in
unstressed words". Note: rule names are historic labels; numbering and
renaming across the cascade will be regularized later (author instruction).

## 8. Adopted context-aware reformulation

Sections 4–7 record the original proxy and its original validation, not
the current formalization. The coupled SC031/SC098 adjudication replaces
literal ww conditioning with the source-backed heavy-syllable,
sentence-unstressed, phonologically-final short-i/u condition
([@RingeTaylor2014, pp. 55, 57–58]).
Inherited/coronal-created short-Vww reanalysis now precedes that loss;
the loss no longer depends on retaining an obsolete consonantal spelling.
The separate homorganic uww quantity premise and later English realization
are explained in the SC031 memo and the 031–034 dossier
([@RingeTaylor2014, pp. 41–42, 65–66, 171–175; @Fulk2018, p. 117]).

`entry_context_metadata.tsv` selects row2326 as weak-final at SC098.
PROTO and PROTOFORM remain `*ízwiz`; root accent and selected sentence
stress are independent. All other selected forms use the explicit
strong-final citation convention. The full audit found 62 checkpoint
forms eligible in a hypothetical weak-final context, not a you-only
phonological domain. Proclitic finality is transported through unchanged
SC063 vowel clauses and then removed; annotations never become lexical
segments or displayed reconstructed forms.

The protected composed assay passes 49 component, seven staged and 28
intermediate controls. Weak-final and, proclitic ymbe, weak-final ēow,
stressed ġiest/fȳr and homorganic sċūwa test the condition and quantity
premises. The retained-i you result is model-only īei, not an attested
strong spelling ([@RingeTaylor2014, pp. 41–42, 55, 57–58, 66;
@Campbell1959, p. 283]).

The production evaluator reproduces all 387 previous finals and the same
seven mismatches. The explicitly approved baseline transition preserves
the previous selected387 snapshot and unchanged lexical/original380/
archival380 projections. Only the assembled evaluator input of row2326
changes. This is a context contract, not a lexeme-conditioned sound law.
The current decision is `sc098-context-apocope-adjudication.md`;
full publication and integrated propagation checks remain required.
