# Surviving bimoric \emph{*ō} unrounding

## Historical discussion

The handbooks do not isolate a large independent sound change under this label.
The surviving bimoric \emph{*ō} in the pathway to *ræste* ‘rest’ nevertheless
undergoes unrounding before
[SC043 EAFBrightening](#rule-EAFBrightening). Campbell, Hogg,
and Ringe and Taylor describe the surrounding fronting and restoration history
without naming this feeder separately [@Campbell1959, pp. 52, 60,
§§131, 157--158; @HoggPhonology1992, pp. 102, 105; @RingeTaylor2014, pp. 157--158,
189--190].

The sole witness establishes a local relation to brightening but supports no broader generalization.

## SC042. Unrounding of the surviving bimoric \emph{*ō} (`PWGmcSurvivingBimoricOUnrounding`) {#rule-PWGmcSurvivingBimoricOUnrounding}

```foma
define PWGmcSurvivingBimoricOUnrounding [
    {*ō} -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

The single *ræste* ‘rest’ derivation carries the chronology of bimoric \emph{*ō} > \emph{*ā}. Before [SC020 EAFFinalZDeletion](#rule-EAFFinalZDeletion) or after [SC043 EAFBrightening](#rule-EAFBrightening), PGmc [rástōz]{.recon} ‘rest’ yields [*rasta*]{.pred} rather than expected OE *ræste*. Unrounding must therefore follow final \emph{z}-loss and precede brightening, although only the relation to brightening is local.
