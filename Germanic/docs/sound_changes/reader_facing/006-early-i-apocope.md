# Early i-apocope

## Historical discussion

Sievers/Brunner treats the early loss of final \emph{*i} after unstressed syllables as established by the fact that these endings no longer trigger later i-umlaut in Old English, and Ringe and Taylor make the same point through the pathway to *geoguþ* ‘youth’ [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141]. Campbell's *dugup* 'troop' and *geogup* 'youth' examples belong to the same pattern [@Campbell1959, §332].

The ending vowel disappears in a weak suffixal environment early enough to block later umlaut. This anti-umlaut chronology distinguishes the change from later final-vowel losses.

## SC006. Early i-apocope (`PWGmcEarlyIApocope`) {#rule-PWGmcEarlyIApocope}

```foma
define PWGmcEarlyIApocope Ctx([
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
]);
```

The absence of umlaut in *geoguþ* ‘youth’ provides the historical argument for early deletion. The ordered derivation supplies a different test: if apocope is delayed until after [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong), PGmc [skáwōθi]{.recon} ‘shows’ yields [*sċēaweþ*]{.pred} rather than expected OE *sċēawaþ* 'shows'.

Early i-apocope must therefore precede the long-diphthong development. Moving it earlier within the tested range leaves every output unchanged; its early date rests on the anti-umlaut evidence, not on a lower boundary supplied by the witness words.
