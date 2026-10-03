# Anglo-Frisian ai-monophthongization

## Historical discussion

Inherited stressed \emph{*ái} yields \emph{*ā} in English. Ringe and Taylor
discuss this development separately from the earlier unstressed contraction.
The distinction between inherited long vowels and new \emph{*ā} requires
inherited-long fronting to have been well under way before contraction
completed; it does not prove that the two developments could not overlap
[@RingeTaylor2014, pp. 170–171]. Campbell gives the stricter conventional
sequence and places contraction before ordinary short-vowel fronting
[@Campbell1959, pp. 52–53]. Later i-mutation of the new long vowel is a
separate conditioned development, not that ordinary fronting
[@Campbell1959, p. 69].

Versloot proposes a wave account of the regional outcomes, but CAPR does
not adopt diffusion as a solution to the comparative tree problem.
His readings of early English and Frisian inscriptions are relevant
evidence independently of that mechanism, conditional on their provenance,
etymology and phonetic interpretation
[@Versloot2017, pp. 295–297, 318]. The required Anglo-Frisian ancestral node
is retained. Whether completed English contraction belongs after it is
distinct from the possibility of an earlier conditioned onset on the
common stem; the current operational corridor does not settle that question.

The live selected-corpus census has twenty-three applications, all carrying
stressed \emph{*ái}. Loam's selected \emph{*láimą} 'loam' is explicitly a
pre-Old-English model input, not an independent Proto-Germanic witness.
The raw corpus's additional roe reconstruction has no attested target and
is excluded from that census. The unstressed development \emph{*ai > *ē}
is the separate earlier change
[SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).

## SC004. Anglo-Frisian ai-monophthongization (`EAFAiMonophthongization`) {#rule-EAFAiMonophthongization}

```foma
define EAFAiMonophthongization [
    {*ái} -> {*ā}
];
```

The soul form fixes the relation to interstress raising. If the monophthongization is delayed until after that change, PGmc [sáiwalō]{.recon} 'soul' yields [*sāwel*]{.pred} rather than expected OE *sāwol* 'soul'. An earlier placement changes no output. This shows that [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The unstressed development \emph{*ai > *ē} in final and nonfinal syllables is a separate and earlier change; see [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).
