# Anglo-Frisian brightening

### Sound-change report

#### Historical formulation

SC043 is the early fronting usually called **Anglo-Frisian Brightening** or
**First Fronting**: Germanic low `a` develops to `æ`-type outputs outside nasal
environments. The core rule is stable in the handbook tradition even if the
wider English-Frisian shared-innovation framing has to be handled more
cautiously than the label itself may suggest [@Campbell1959, §131;
@HoggPhonology1992, p. 102; @RingeTaylor2014, pp. 157--158; @Fulk2018, §4.12].

#### Source tradition

Campbell gives the classical formulation of early `a > æ` outside nasal
environments and then treats later breaking and restoration as changes that
presuppose that fronted stage. Hogg makes the modern label pair explicit and is
also the most useful direct support for extending the fronting into unstressed
vowels. Ringe and Taylor sharpen the chronology further by arguing that
fronting must precede breaking and that later retraction must follow both.
Fulk gives the most compact bridge from the basic brightening rule to the later
Old English developments that partly conceal it. Toon supplies the traditional
relative ordering, reproducing Campbell's own chronological list while warning
against reading it as a strict linear sequence
[@Campbell1959, §§131, 139, 157--158, §255; @HoggPhonology1992, pp. 102, 105;
@Toon1992, p. 446;
@RingeTaylor2014, pp. 157--158, 168--169, 189--190; @Fulk2018, §§4.12--4.13].

#### CAPR implementation

CAPR formalizes SC043 with three coordinated clauses: an unstressed `*a > *æ`
rule outside nasal environments, a stressed `*á > *æ` rule with the same core
conditioning, and a long-final `*ā > *ǣ` clause. The first two are close to the
handbook rule in explicit transducer form. The long-final clause is more
model-specific: it is best read as an implementation choice tied to the
surviving-bimoric `*ō > *ā` pathway inherited from SC042, not as a direct
quotation from a single handbook statement.

#### Place in the cascade

SC043 sits in a tight local neighborhood: `SC042` PWGmc Surviving Bimoric O
Unrounding, `SC043` Anglo-Frisian Brightening, `SC044` OE Breaking, `SC045` OE
Velar Fricative Palatalization, and `SC046` OE A Restoration. That position
matters because brightening is both fed and later partly masked inside the same
cluster. It receives left-hand input from SC042, creates the front-vowel stage
needed by SC044, and is later partly reversed by SC046 in back-vowel
environments.

#### Order evidence

The chronology card fixes SC043 in a narrow local window. `SC042 < SC043` is
supported by **rest**: if brightening moves earlier across SC042, the derivation
loses the fronted/restored route and yields `rasta` rather than `ræste`.
`SC043 < SC044` is supported by **slay**: if brightening moves later than
breaking, the derivation yields `sleaan | slēaan` rather than `slēan`. The
wider local neighborhood also supports `SC043 < SC046`, while earlier links
such as `SC034 < SC043` and contextual `SC035 < SC043` are best treated as
orientation rather than as reasons to turn this report into a graph chapter.

#### Interpretation

For book purposes, SC043 is a pivot change. The literature establishes the
basic fronting rule and its relation to later breaking and restoration. CAPR
then makes that relation explicit in rule form, and the chronology card shows
that the current local ordering is not arbitrary inside the model. The report
should therefore present brightening as an enabling stage: it creates front-
vowel input for later Old English developments and is subsequently partly
obscured by restoration, so its historical importance often becomes clearest
through the later changes that still presuppose it.

#### Remaining cautions

The broader English-Frisian shared-innovation story should be handled
carefully: the existence of the fronting rule is well supported, but the
subgrouping narrative is less straightforward [@Campbell1959, §131;
@RingeTaylor2014, pp. 157--158]. The unstressed clause in CAPR is defensible
from the handbook tradition, yet it remains a modeling choice that should not
be mistaken for the whole historical claim [@HoggPhonology1992, pp. 102, 105].
Likewise, the long-final clause belongs to CAPR's representation of the
SC042-to-SC043 pathway and should be presented as a model-specific approximation
rather than as a simple handbook quotation.
