# Prefix i-reduction

## Historical discussion

Late weak-tail reduction affects unstressed prefixes as well as inflectional
endings and medial vowels. Fulk's discussion of prefix vowels accounts for OE
\emph{*be-} and \emph{*ne-} [@Fulk2018, p. 97, §5.7]. Hogg and Ringe and
Taylor place such weakening within the broader late history of unstressed
vowels [@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 298--332,
§§6.8.3--6.9.6].

The tested forms do not determine the rule's position relative to a neighboring
change.

## SC076. Reduction of prefixal \emph{*i} in unstressed position (`OEPrefixIReduction`) {#rule-OEPrefixIReduction}

```foma
define OEPrefixIReduction [
    {*i} -> {*ĕ} || .#. [{*b} | {*n}] _ [EnglishStarConsonant | EnglishPalatalConsonant] EnglishStarVocalic
];
```

The rule reduces unstressed prefixal \emph{*i} to a weaker vowel in the
\emph{bi-} and \emph{ni-} type prefixes before a consonant plus a following
vowel. The development accounts for later prefix spellings such as OE
\emph{*be-} and \emph{*ne-}.

If the rule is moved earlier or later within the tested sequence, no output differs from the expected one. The lexical evidence therefore does not place [SC076 OEPrefixIReduction](#rule-OEPrefixIReduction) before or after any specific neighboring change.

The handbooks attest late prefix-vowel weakening, but the precise placement
remains approximate. No lexical failure fixes it.
