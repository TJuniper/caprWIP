# SC020 PGmc Final Z Deletion — literature dossier

## Rule metadata

- change_id: SC020
- display_name: PGmc Final Z Deletion
- FOMA rule: PGmcFinalZDeletion
- current_order: 20
- chronology_card: `Germanic/docs/sound_changes/order_tests/chronology_cards/SC020-pgmc-final-z-deletion.md`
- example_lexemes: `*rástōz > ræste`; broad/far later-side examples include `*bébruz > befer`, `*kwéðuz > cwedu`, `*félθuz > feld`, and export-layer echoes include `*sáiwiz > sǣ`
- aliases searched: PGmc Final Z Deletion; final z deletion; final -z deletion; final *z; word-final z; word-final *z; loss of final z; loss of final *z; deletion of final z; deletion of final *z; West Germanic z loss; final s / z; Proto-Germanic *z; unstressed final *z; word-final *-z; final *-az; final *-ōz; nominative singular z; nominative singular *-z; masculine nominative singular; neuter nominative accusative; r-stems; `*rástōz`; `*rastōz`; rest; ræste; rast; final ō raising and final z deletion; final *-ōz; z loss after long vowel; final z and West Germanic; Crist z loss; final z loss chronology; Verner's Law final z; rhotacism final z; final z before rhotacism; apocope final z

## FOMA definition

```foma
define PGmcFinalZDeletion [{*z} -> 0 || _ .#.];
define PGmcFinalZLoss PGmcFinalZDeletion;
```

The immediately adjacent implementation comment in `Germanic/fsts/germanic.txt` adds two important constraints that are not encoded inside the rewrite itself:

1. z-deletion must run **before** `PGmcRhotacism`, so word-final `*z` disappears rather than rhotacizing;
2. `NWGmcFinalLongORaising` must run **before** this rule so inherited final `*-ō` can raise while `*-ōz` remains sheltered by final `*z` until SC020.

## Working description

CAPR's SC020 deletes any word-final `*z` outright. The literature supports the underlying historical phenomenon, but usually in a more qualified way than the FOMA rule suggests.

The main literature picture is:

1. **a standard West Germanic development:** word-final `*z` in unstressed syllables was lost across West Germanic;
2. **a morphology-heavy change:** because word-final `*z` was common in inflectional endings, the change had large consequences for nominal morphology;
3. **a change distinct from rhotacism:** surviving `*z` later became `r`, but only after the deletion environments had already removed part of the inventory;
4. **a broader cluster, not one simple all-purpose rule:** some authors, especially Crist, separate the pan-West-Germanic final-unstressed loss from later or narrower Ingvaeonic `*z`-deletion environments.

So SC020 is not merely a CAPR cleanup operation. But neither is the exact FOMA rule a direct transcription of the handbook rule. The historical core is well established; the exact formal scope and its adjacency to SC019, SC040, SC042, or SC054 are CAPR-specific packaging.

## Search log

| Source file searched | Search terms used | Productive? | Evidence found | Notes |
| --- | --- | --- | --- | --- |
| `docs/references/campbell_old_english_grammar.txt` | `final z`, `rhotacism`, `*z later lost`, `meord`, `§ 123`, `§ 398`, `§ 404` | yes | concise standard grammar statement that `z` is later lost or changed to `r` | useful older handbook anchor, though not a standalone SC020 formulation |
| `docs/references/hogg_vol1.txt` | `rhotacism`, `final position generally lost`, `z yielded r`, `Verner's Law` | yes | clean statement that Germanic `z` rhotacizes intervocalically but is generally lost in final position | best compact non-Crist handbook statement recovered |
| `docs/references/crist_2001_conspiracy_in_historical_phonology.txt` | `*-z`, `after unstressed V`, `PWGmc stage`, `rhotacism`, `dagaz`, `sunuz` | yes | explicit statement of a PWGmc `*-z` deletion after unstressed vowel plus chronology before rhotacism | strong morphology-sensitive framing |
| `docs/references/crist_2002_z_loss_west_germanic.txt` | `word-final *z`, `unstressed syllables`, `rhotacism`, `Campbell p. 166` | yes | clearest direct statement of pan-WGmc word-final `*z` loss in unstressed syllables and its precedence over rhotacism | strongest SC020 witness |
| `docs/references/kilday_2024_crists_law_smiths_law_wizen.txt` | `*z-deletion in West Germanic`, `well-known West Germanic loss`, `rhotacism` | yes | recent synthesis distinguishing the already accepted WGmc final-unstressed loss from Crist's narrower Ingvaeonic deletions | useful modern framing, especially for what SC020 is not |
| `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt` | `mēd`, `anteconsonantal z`, `rhotacism`, `*-z` | no | useful on medial/anteconsonantal `z` material such as `mēd`, not on the pan-WGmc final-unstressed deletion itself | checked to avoid conflating medial and final `z` |
| `docs/references/ringe_taylor_linguistic_history_vol2.txt` | `word-final *-z`, `rhotacism`, `unstressed syllables`, `nominative singular` | no | no clean SC020-defining passage was recovered from the local witness | checked, not used |
| `docs/references/luick_historische_grammatik.txt` | `o > u im Auslaut; i,u vor z/r>e,o`, `auslaut`, `z`, `rhotazismus`, `a vor z` | no | useful only for neighboring final-vowel and `i/u`-before-`z/r` phenomena, not a clean direct SC020 statement | checked, not used as primary witness |
| `docs/references/brunner_1965_altenglische_grammatik.vision.txt` | `Rhotazismus`, `auslautendes z`, `Wegfall des z`, `*-az`, `*-ōz` | no | OCR remained too noisy to recover a safe final-`z` statement | checked, not used |
| `docs/references/kaluza_historische_grammatik_englisch.txt` | `final z`, `rhotacism`, `nominative singular`, `*-az` | no | no usable direct SC020 passage recovered | checked, not used |
| `docs/references/bulbring_altenglisches_elementarbuch.txt` | `final z`, `rhotacism`, `*-az`, `*-ōz` | no | no usable direct SC020 passage recovered | checked, not used |
| `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | `*rastō`, `*saiwiz`, `*dagaz`, `*bardaz` | no | lexical mapping only | checked for CAPR example control, not used as a primary historical witness |
| `docs/references/orel_handbook_germanic_etymology.vision.txt` | `*rastō`, `*saiwiz`, `*bardaz`, `*kambaz` | no | lexical mapping only | checked for CAPR example control, not used as a primary historical witness |
| `Germanic/docs/analysis/meord_med_chronological_review.md` | `mizdō`, `meord`, `z-retention`, `rhotacism` | no | internal note confirms the importance of keeping medial `z` issues separate from SC020 | CAPR-context check only |

## Chronological source dossier

### Campbell 1959

- source_key: Campbell1959
- full source title: *Old English Grammar*
- publication year: 1959
- locator: lines 4064-4067 in the local text witness
- terminology used by the source: `the voiced spirant z ... is later lost or changed to r`
- exact quotation: "the voiced spirant z, which arose from I-E s by Verner's law, and is later lost or changed to r"
- paraphrase of the source's claim: Campbell treats Germanic `z` as a historically prior segment whose later reflexes in OE are either deletion or rhotacized `r`.
- conditioning stated by the source: not isolated as a separate SC020 rule; the statement appears inside discussion of `i/u` lowering before `z`
- examples used by the source: `meord`, `leornian`, the pronouns `wé, gé, hé, mé, pé`, and prefixes `or-, tor-`
- chronology stated or implied by the source: `z` first conditions earlier vocalic developments and is only later lost or changed to `r`
- relation to other changes: explicitly tied to Verner's-law `z`, earlier vowel lowering before `z`, and later rhotacism
- cautions or disagreements: Campbell does not present a neat standalone "final `*z` deletion" chapter; the evidence mixes final and non-final outcomes
- usefulness for book prose: useful as a standard handbook anchor that the literature treats `z`-loss and rhotacism as later developments relative to other vocalic changes

### Bammesberger 1992

- source_key: Bammesberger1992
- full source title: *The Cambridge History of the English Language, Volume I*
- publication year: 1992
- locator: lines 2224-2227 in the local text witness
- terminology used by the source: `rhotacism`; `in final position it is generally lost`
- exact quotation: "Gmc /z/ yielded /r/ in intervocalic position in Old English ... but in final position it is generally lost."
- paraphrase of the source's claim: Bammesberger offers a compact positional summary: intervocalic `z` rhotacizes, but final `z` is lost.
- conditioning stated by the source: final position versus intervocalic position
- examples used by the source: the immediate illustration is the alternation behind the verb `choose`, not the CAPR `rest` example
- chronology stated or implied by the source: the two outcomes are positional reflexes of Germanic `z` after Verner's Law
- relation to other changes: tied directly to Verner's Law and to rhotacism
- cautions or disagreements: the statement is OE-facing and succinct; it does not spell out the pan-West-Germanic unstressed-syllable conditioning as fully as Crist does
- usefulness for book prose: strong compact support that final `z` loss is ordinary handbook material rather than a CAPR invention

### Crist 2001

- source_key: Crist2001
- full source title: *Conspiracy in Historical Phonology*
- publication year: 2001
- locator: lines 5101-5117 and 5420-5422 in the local text witness
- terminology used by the source: `*-z after unstressed V`; `PWGmc stage`; `rules eliminating *z by deletion`
- exact quotation: "This rule, which appears to have occurred at the PWGmc stage, had drastic consequences for noun morphology"; "rhotacism must have followed the three rules eliminating *z by deletion"
- paraphrase of the source's claim: Crist treats word-final `*-z` loss after unstressed vowel as a Proto-West-Germanic rule with major inflectional consequences, and he explicitly places rhotacism later.
- conditioning stated by the source: `*-z` after unstressed vowel, word-finally
- examples used by the source: `*dagaz`, `*gastiz`, `*sunuz`
- chronology stated or implied by the source: Proto-West-Germanic; earlier than rhotacism
- relation to other changes: strongly tied to nominal morphology and to the later rhotacism that merges surviving `z` with `r`
- cautions or disagreements: Crist's dissertation analyzes the disappearance of `z` as a cluster of several rules, not as one single uniform process
- usefulness for book prose: very useful for explaining why SC020 is both a sound change and a morphology-shaping event

### Crist 2002

- source_key: Crist2002
- full source title: *An Analysis of \*z Loss in West Germanic*
- publication year: 2002
- locator: lines 84-87, 99-106, and 216-223 in the local text witness
- terminology used by the source: `the first WGmc *z-deletion`; `word-finally in unstressed syllables`; `rhotacism`
- exact quotation: "Throughout WGmc, PGmc *z deletes word-finally in unstressed syllables"; "It might be tempting to suppose that rhotacism precedes the two z-deletions ... However, this cannot be the case"
- paraphrase of the source's claim: Crist distinguishes a pan-West-Germanic word-final unstressed `*z` loss from narrower Ingvaeonic deletion rules and argues explicitly that rhotacism must come later.
- conditioning stated by the source: word-final `*z` in unstressed syllables across West Germanic
- examples used by the source: broad nominal suffix material and the contrast between deleted `*z` in `*miz, *wīz`-type environments and surviving original `*r`
- chronology stated or implied by the source: earlier than rhotacism; separate from later Ingvaeonic `*z`-deletion rules
- relation to other changes: deeply tied to WGmc morphology, rhotacism, and other `z`-deletion environments
- cautions or disagreements: strongest source here, but still broader than CAPR's single unconditioned word-final deletion rule
- usefulness for book prose: the single most important source for distinguishing the standard historical phenomenon from CAPR's narrower implementation choices

### Kilday 2024

- source_key: Kilday2024
- full source title: *Crist's Law, Smith's Law, and English wizen*
- publication year: 2024
- locator: lines 18-24 in the local text witness
- terminology used by the source: `the well-known West Germanic loss of Proto-Germanic word-final *z in unstressed syllables`
- exact quotation: "In addition to the well-known West Germanic loss of Proto-Germanic word-final *z in unstressed syllables, Crist recognized two environments for deletion of *z in the Ingvaeonic languages"
- paraphrase of the source's claim: Kilday treats the ordinary WGmc final-unstressed loss as already established background and reserves Crist's more controversial contribution for the additional Ingvaeonic environments.
- conditioning stated by the source: word-final `*z` in unstressed syllables
- examples used by the source: `*miz`, `*wīz`, `*maiz` for the later Ingvaeonic deletion environments
- chronology stated or implied by the source: before rhotacism and before merger with original `*r`
- relation to other changes: explicitly separated from Ingvaeonic deletion rules and from later rhotacism/merger
- cautions or disagreements: this is a modern synthesis and not itself the original demonstration
- usefulness for book prose: useful for showing that the basic WGmc final-unstressed loss is now treated as ordinary background, not as a disputed novelty

## Comparative synthesis

1. **Do the sources agree on the existence of final `*z` loss?**  
   Yes. All productive sources treat the loss of at least some word-final `*z` material as real. Crist 2002 and Kilday 2024 are the clearest on the pan-West-Germanic word-final unstressed rule; Campbell and Hogg presuppose the same outcome in standard handbook form.

2. **Do they use the same terminology?**  
   No. The literature more often speaks of `word-final *z in unstressed syllables`, `*-z after unstressed V`, or simply `z` later being `lost or changed to r`. None uses the CAPR label **PGmc Final Z Deletion**.

3. **Is the change treated phonologically, morphologically, or both?**  
   Both. The phonological event is deletion of final `*z` in a specific environment, but Crist 2001 and 2002 stress that its consequences are heavily morphological because `*-z` is widespread in inflectional endings.

4. **Is it Proto-Germanic, West Germanic, North-West Germanic, or specifically Old English in the literature?**  
   The strongest literature places the core change at the **West Germanic / Proto-West-Germanic** level, not at Proto-Germanic proper and not as a specifically Old English innovation. OE handbooks describe the reflexes; Crist formulates the historical stage most explicitly.

5. **Do the sources distinguish final `*z` from final `*s`, rhotacized `*z`, or other sibilants?**  
   Yes. Campbell and Hogg frame the issue through Verner's-law `z`; Crist is explicit that deletion must precede rhotacism, precisely because original `r` does not delete in the same environments.

6. **Do they give examples comparable to `*rástōz > ræste / rast`?**  
   Not directly. The usual rule examples are inflectional forms such as `*dagaz`, `*gastiz`, and `*sunuz`, plus pronouns or adverbs like `*miz`, `*wīz`, and `*maiz`. The CAPR `rest` derivation is a model-specific representative example, not a standard handbook test case.

7. **Do they discuss interaction with final `*-ō > *-u`, final-vowel loss, or `ō`-stem morphology?**  
   Only indirectly. Crist 2001 emphasizes how important the rule is for noun morphology, but the productive SC020 sources recovered here do not explicitly stage the `rest` problem as `final *-ō` raising before `final *z` deletion. That interaction remains mainly a CAPR-local articulation.

8. **Do they discuss interaction with later OE med unstressed U lowering or other later corridor edges?**  
   No. None of the productive historical sources recovered here discusses SC040, SC041, SC042, or SC054 as later neighbors of final `*z` deletion.

9. **Do they support, complicate, or fail to discuss the SC019/SC020 computational boundary?**  
   They support it only indirectly. The literature strongly supports SC020 as a real historical event and supports keeping it after the stage where `*-ō` is still protected by final `*z`; but no productive source directly frames the `*rástōz > ræste` boundary as the handbooks do not use that exact derivational example for chronology.

10. **Do they support, complicate, or fail to discuss SC020's later broad/far boundaries with SC040/SC041/SC042/SC054?**  
    They mostly fail to discuss them. The later SC040/SC041/SC042/SC054 links are computationally real in CAPR, and the SC042/SC054 relations are confirmed by actual chronology cards, but the literature does not formulate those later corridor edges as explicit historical sequencing claims.

11. **Is SC020 a standard historical sound change, a CAPR-specific formalization, or a mixture?**  
    A mixture leaning strongly historical. The core event — West Germanic loss of word-final `*z` in unstressed syllables before rhotacism — is standard. CAPR's exact one-line rule, which deletes any word-final `*z` without explicit stress or morphological conditioning, is a convenient formal abstraction.

12. **What can safely be said in book prose?**  
    It is safe to say that West Germanic lost word-final `*z` in unstressed syllables before rhotacism, and that this had major consequences for nominal endings. It is also safe to say that CAPR models that broad development with a single deletion stage. It is **not** safe to claim that the literature itself states the precise SC019/SC020 adjacency on `rest` or the later SC020/SC040 and SC020/SC054 relations found by order-testing.

## Relation to CAPR implementation

SC020 is historically grounded but more tightly packaged in CAPR than in the handbooks.

1. **FOMA definition:** `PGmcFinalZDeletion` deletes any word-final `*z` unconditionally. The literature-backed core is narrower: the clearest standard statement is West Germanic loss of word-final `*z` in unstressed syllables.
2. **Current order:** SC020 stands at order 20, immediately after SC019 and before the wider final-syllable corridor seen later in the cascade.
3. **Chronology card:** the local card gives one reciprocal earlier boundary with SC019 on `rest` and one broad/far later boundary with SC040.
4. **Earlier CAPR boundary:** if SC020 is moved earlier or SC019 later across this local pair, the `rest` derivation breaks: PGmc `*rástōz` yields `rast` rather than expected OE `ræste`.
5. **Later CAPR boundary:** if SC020 is moved later across SC040, the failures are broad/far rather than local. The representative set is `beaver; bough; cud; field; flood`, and the card itself warns that this should not be narrated as tight adjacency.

The export layer and neighboring chronology cards add two further checked relations:

1. `SC020 -> SC042` is a **core local** edge from `SC042-pwgmc-surviving-bimoric-o-unrounding.md`, again defined by the single `rest` derivation.
2. `SC020 -> SC054` is a **core local** edge from `SC054-oe-w-loss-before-i.md`, defined by the single `sea` derivation.
3. `SC020 -> SC041` is **contextual broad/far** support, not a local pair.

These checked relations matter for prose restraint. SC019/SC020 is a genuine local reciprocal boundary. SC020/SC042 and SC020/SC054 are also real, but they are read from other cards and rest on one derivation each. SC020/SC040 and SC020/SC041 are broader computational limits, not close historical adjacency claims.

This means that the literature and the CAPR model line up best at the center of SC020:

- the literature supports a real WGmc final-`*z` loss before rhotacism;
- the CAPR rule captures that as one stage;
- the immediate `rest` boundary with SC019 is historically plausible but still model-local in its exact formulation;
- the later SC040/SC041/SC042/SC054 links help explain why SC020 acts as a bridge into the broader final-syllable system, but they should not be overread as if handbooks themselves gave that full adjacency map.

## Dossier status

- ready_for_book_dossier: partial
- remaining_gaps: recover a clean Brunner or Ringe/Taylor statement if one exists in the local witnesses; check whether any locally stored source discusses the `rest`-type interaction of `*-ōz` more directly; keep CAPR's unconditioned FOMA rule distinct from the literature's stress- and morphology-sensitive formulations
- recommended_next_step: draft the prose-ready early-corridor book dossier with SC020 treated as a bridge section rather than as an isolated standalone mini-chapter
