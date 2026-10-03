# Unstressed \emph{*a}-raising before final \emph{*m}

## Historical discussion

Campbell notes that unstressed \emph{u} is especially well preserved before \emph{m}, with dat.pl. \emph{-um} and related endings as the clearest evidence [@Campbell1959, p. 156, §373]. Fulk likewise includes the development of early unstressed \emph{*o} to \emph{u} before \emph{m} among the similarities shared by North and West Germanic [@Fulk2018, p. 16, §5.2].

I restrict the change to unstressed vowels in inflectional material because the strongest evidence concerns noninitial unstressed material before final \emph{*m}.
Final \emph{*m} conditions the raising.

## SC005. Unstressed \emph{*a}-raising before final \emph{*m} (`PNWGmcAToUBeforeM`) {#rule-PNWGmcAToUBeforeM}

```foma
define PNWGmcAToUBeforeM Ctx([
    {*a} -> {*u} || EnglishStarVocalic EnglishStarConsonant+ _ {*m} ({*i})? ({*z})? .#.
]);
```

Here the witness word and the comparative evidence serve different purposes. If raising is delayed until after [SC017 PNWGmcULowering](#rule-PNWGmcULowering), PGmc [skúldramiz]{.recon} 'shoulders' yields [*sċoldrum*]{.pred} rather than expected OE *sċuldrum* 'shoulders'; earlier placements converge on the expected output. The scope of the change is established by inflectional evidence across multiple paradigm types: a-stem dative plural ON [*dǫgum*]{.iv lang=on sort=dogum role=evidence_form} 'days', OE [*dagum*]{.iv lang=oe sort=dagum role=evidence_form} 'days', OS [*dagun*]{.iv lang=os sort=dagun role=evidence_form} 'days', OHG [*tagum*]{.iv lang=ohg sort=tagum role=evidence_form} 'days', beside Gothic [*dagam*]{.iv lang=goth sort=dagam role=evidence_form} 'days'; strong-adjective dative singular ON [*góðum*]{.iv lang=on sort=godum role=evidence_form} 'good', OE [*gōdum*]{.iv lang=oe sort=godum role=evidence_form} 'good', OS [*gōdum*]{.iv lang=os sort=godum role=evidence_form} 'good', beside Gothic [*godamma*]{.iv lang=goth sort=godamma role=evidence_form} 'good' (OS also shows variant forms gōdumu and -un); and first-plural present ON [*berum*]{.iv lang=on sort=berum role=evidence_form} 'we carry', OHG [*berumēs*]{.iv lang=ohg sort=berumes role=evidence_form} 'we carry', beside Gothic [*baíram*]{.iv lang=goth sort=bairam role=evidence_form} 'we carry'. Across these sets, North/West Germanic shows unstressed \emph{-um} where Gothic preserves \emph{-am}. The derivation of *sċuldrum* 'shoulders' supplies a CAPR ordering witness for the relative chronology, but the cognate set for 'shoulder' does not contribute comparative evidence for the rule's historical scope.
