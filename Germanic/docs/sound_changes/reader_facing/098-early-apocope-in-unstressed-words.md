# Early apocope in unstressed words

## Historical discussion

Alongside the regular loss of word-final short high vowels in third syllables ([SC006 PWGmcEarlyIApocope](#rule-PWGmcEarlyIApocope)), Ringe and Taylor identify a second, earlier apocope: "Short high vowels were also lost after heavy syllables in unstressed words" [@RingeTaylor2014, pp. 57--58, §3.1.4]. The two laws must not be conflated. Fully stressed disyllables kept their final \emph{*-i} long enough to cause i-umlaut — OE *ġiest* 'guest' < \emph{*gastiz} and *fȳr* 'fire' < \emph{*fūri} require exactly that survival [@RingeTaylor2014, p. 55, §3.1.4] — whereas words that carried no sentence stress lost the vowel already in Proto-West Germanic.

The conditioning is prosodic. Like Verner's law, the change is governed by accent: it applied in words unstressed in the sentence, and its apparent exceptions are systematic, not sporadic. Forms such as OE *ymbe* 'around' and OHG \emph{umbi} kept their final vowel because, as Ringe and Taylor observe, proclitics "were not phonologically word-final" and so stood outside the environment altogether [@RingeTaylor2014, pp. 57--58, §3.1.4]. Sentence-level accent placement therefore decides which sandhi variant each daughter language continues, and doublets across the family reflect the stressed and unstressed sentence forms of the same word — regular sandhi, not lexical diffusion.

The diagnostic witness is the second-person plural pronoun. Ringe and Taylor print the Proto-West Germanic form as a doublet: PGmc \emph{*izwiz} (Gothic \emph{izwis}) → \emph{*iwwi} (by [SC008 PWGmcCoronalWAssimilation](#rule-PWGmcCoronalWAssimilation) and the loss of final \emph{*z}, [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion)) → PWGmc \emph{*iuwi} ~ \emph{*iuw} [@RingeTaylor2014, pp. 41--42, §3.1.1]. Old English continues the apocopated, unstressed variant, and Ringe and Taylor's proof is the vocalism itself: "OE iow 'you (dat. pl.)' definitely does [show early apocope] (since it does not exhibit i-umlaut)" [@RingeTaylor2014, pp. 57--58, §3.1.4]. Had the \emph{*-i} survived, i-umlaut ([SC055 OEIUmlaut](#rule-OEIUmlaut)) would have fronted the diphthong; West Saxon *ēow* 'you' beside early West Saxon and Northumbrian *īow* 'you' shows the normal unumlauted development [@Campbell1959, §702, p. 283].

## SC098. Early apocope in unstressed words (`PWGmcUnstressedWordFinalIApocope`) {#rule-PWGmcUnstressedWordFinalIApocope}

```foma
define PWGmcUnstressedWordFinalIApocope [
    [ [{*i}|{*u}] -> 0 || .#. {*ᵘ} ?* [
        [EnglishStarLongVowel | EnglishStarLongDiphthong] EnglishStarConsonant*
        | EnglishStarShortVowel EnglishStarConsonant EnglishStarConsonant+
    ] _ .#. ]
    .o. [{*ᵘ} -> 0]
    .o. [
        [{*ᶜ}:0 [EnglishStarAlphabet - {*ᶜ}]* 0:{*ᶜ}]
        | [EnglishStarAlphabet - {*ᶜ}]*
    ]
];
```

Sentence stress and phonological finality are now explicit, independently
selected context. They do not alter the PGmc reconstruction, the selected
segmental input or its historical stage. The computational marks in the
rule distinguish weak-final context from weak-nonfinal context; they are
not reconstructed phonemes and are absent from displayed forms. Ordinary
evaluation explicitly chooses strong-final citation context. You selects
the independently source-discussed weak-final variant, not an unstressed
classification inferred from a pronoun label or missing acute.

The worked history is \emph{*izwiz} → \emph{*iwwiz} by assimilation →
\emph{*iuwiz} by [SC031 OEWWSimplification](#rule-OEWWSimplification) →
\emph{*iuwi} by final \emph{z}-loss → weak-final \emph{*iuw} by this
rule → OE *ēow*. The operation requires a heavy syllable and a
phonologically final short high vowel: long vowel/diphthong weight or a
short vowel followed by a closing consonant cluster, not literal
\emph{ww}. Its condition therefore survives glide reanalysis.
Loss of final \emph{z} still feeds it, and removal of \emph{i} bleeds
[SC055 OEIUmlaut](#rule-OEIUmlaut). Its PWGmc placement precedes the
later northern loss of stressed-monosyllabic final \emph{z}
([SC097 MonosyllabicFinalZLoss](#rule-MonosyllabicFinalZLoss))
([@RingeTaylor2014, pp. 41--42, 55, 57--58]).

The staged strong contexts retain the high vowel in the histories of
*ġiest* 'guest' and *fȳr* 'fire'. A weak-final and context yields *and* 'and', whereas
the proposed proclitic context retains the vowel in *ymbe* through the
later apocope corridor. The right-boundary annotation is removed only
after [SC063 OEHighVowelApocope](#rule-OEHighVowelApocope) has had the
opportunity to apply. These controls implement the defended exceptionless
account; they do not claim direct observation of prehistoric sentence
stress or lexical optionality ([@RingeTaylor2014, pp. 55, 57--58]).

The corresponding English realization of \emph{iu+w} belongs to
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling), not a late
vocalization of retained \emph{ww}. The model's retained-i counterfactual
produces an umlauted result after intervening w-loss; its exact terminal
spelling is a computational prediction, not an attested strong OE form.
The attested weak-final target and the source's mutation argument must
not be replaced by that counterfactual
([@RingeTaylor2014, pp. 41--42, 57--58, 173--175;
@Campbell1959, p. 283]).
