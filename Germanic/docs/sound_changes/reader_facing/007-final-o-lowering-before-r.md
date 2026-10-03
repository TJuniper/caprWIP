# Final \emph{*ō}-lowering before \emph{*r}

## Historical discussion

Ringe and Taylor separate two points here: a broader shortening of vowels before word-final \emph{*r} in unstressed syllables (for which kinship \emph{*r}-stems such as PGmc \emph{*fadér} > PWGmc \emph{*fader} are a key diagnostic), and the specific \emph{*ō}-before-\emph{*r} development needed here [@RingeTaylor2014, pp. 58--59]. The direct lexical witnesses for \emph{*ō} in that environment are two independent etyma: PGmc [fedwōr]{.recon .iv lang=pgmc sort=fedwor role=evidence_form} 'four' with WGmc reflexes OE [*fēower*]{.iv lang=oe sort=feower role=evidence_form} 'four', OFris [*fiuwer*]{.iv lang=ofris sort=fiuwer role=evidence_form} 'four', OS [*fiuwar*]{.iv lang=os sort=fiuwar role=evidence_form} 'four'; and PGmc [watōr]{.recon .iv lang=pgmc sort=wator role=evidence_form} 'water' with OE [*wæter*]{.iv lang=oe sort=waeter role=evidence_form} 'water'.

The rule is historically secure but narrow: final or pre-final \emph{*ō} before word-final \emph{*r}. The clearest evidence remains concentrated in the `four` and `water` material.
No broader environment for \emph{*ō} is attested.

## SC007. Lowering of final bimoric \emph{*ō} before \emph{*r} (`PWGmcFinalOrLowering`) {#rule-PWGmcFinalOrLowering}

```foma
define PWGmcFinalOrLowering Ctx([
    {*ō} -> {*a} || _ {*r} .#.
]);
```

OE *wæter* ‘water’ reveals why lowering must precede [SC043 EAFBrightening](#rule-EAFBrightening). If [SC007 PWGmcFinalOrLowering](#rule-PWGmcFinalOrLowering) is delayed until afterwards, PGmc [wátōr]{.recon} ‘water’ yields [*water*]{.pred} rather than expected OE *wæter* ‘water’: brightening can affect the vowel only after lowering has created its input. Moving the change earlier within the tested range alters no output.

The witness thus supplies a terminus ante quem at brightening but no earlier boundary. Comparative support for the \emph{*ō}-before-\emph{*r} rule comes from the two lexical witnesses [fedwōr]{.recon .iv lang=pgmc sort=fedwor role=evidence_form} 'four' and [watōr]{.recon .iv lang=pgmc sort=wator role=evidence_form} 'water' and their WGmc reflexes; kinship \emph{*r}-stems belong to the broader pre-\emph{*r} shortening context, not to a direct \emph{*ō} > \emph{*a} control. Within CAPR, [*wæter*]{.iv lang=oe sort=waeter role=evidence_form} 'water' is the form that establishes ordering before brightening. No broader lowering of \emph{*ō} is attested.
