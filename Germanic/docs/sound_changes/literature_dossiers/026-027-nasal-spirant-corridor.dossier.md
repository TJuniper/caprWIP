# SC026-SC027 Nasal Spirant Corridor — literature dossier

> **Adjudication correction (SC026/SC027 nasal-spirant adjudication).** This
> dossier predates
> `Germanic/docs/sound_changes/audits/sc026-sc027-nasal-spirant-adjudication.md`,
> which supersedes it on three points.
>
> 1. **Consonantal domain.** The North Sea Germanic law applies before \*f, \*þ
>    and \*s only (Campbell §121, p. 47; Fulk §4.11; Sievers–Brunner §186.1;
>    none of the thirty-odd examples in Ringe & Taylor §5.1.1, pp. 139–41,
>    contains \*x). CAPR's `EnglishStarVoicelessFricative` wrongly included
>    \*x and has been replaced by `EnglishStarNSGmcSpirant`.
> 2. **\*nx belongs to an earlier, pan-Germanic change**, now SC103
>    `PGmcNasalLossBeforeX` (Campbell §119, p. 44; Fulk §4.1; Ringe vol. 1).
>    The diagnostic is comparative: the pan-Germanic change leaves no nasal in
>    any daughter (OHG *fūht*, *fūst*, *brāhta*), whereas the cognates of the
>    Ingvaeonic witnesses keep it (OHG *fimf*, *gans*, *ander*, *jugund*).
> 3. **`fist` is not a witness for SC026 or SC027.** PGmc \*funhsti- (Kroonen
>    p. 160) shows the long vowel in OHG *fūst*, Dutch *vuist* and German
>    *Faust*, so its nasal loss is pan-Germanic. It has been withdrawn from the
>    evidential core and from the chronology witness set, which is now `goose`
>    and `youth`. Where this dossier cites `fist` below, read SC103.
>
> The dossier's central conclusion — that the two CAPR rules articulate **one**
> historical sound change — is confirmed, and is now recorded in the registry
> (SC027 carries `canonical_change_id = SC026`). The `SC026 < SC027` ordering is
> an executable dependency, not a demonstrated historical relative chronology.


## Rule metadata

- change_ids: SC026; SC027
- display_names: NWGmc Nasal Spirant Lengthening; NWGmc Nasal Spirant Loss
- FOMA rules: `NWGmcNasalSpirantLengthening`; `NWGmcNasalSpirantLoss`
- current_orders: 26; 27
- chronology_cards:
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC026-nwgmc-nasal-spirant-lengthening.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC027-nwgmc-nasal-spirant-loss.md`
- representative lexemes / failures: `fist`, `goose`, `youth`
- aliases searched: nasal spirant law; Ingvaeonic nasal spirant law; loss of nasal before voiceless fricatives; nasal loss before spirants; compensatory lengthening before nasal loss; North Sea Germanic nasal loss; `*gans > gōs`; `*jugunþ > geoguþ`; `*funxstiz > fȳst`

## Historical problem

CAPR currently splits the corridor into two adjacent rules:

1. `SC026` adjusts the vowel in nasal + voiceless-fricative environments.
2. `SC027` then deletes the nasal before the spirant.

That split is computationally useful because the chronology cards show a tight reciprocal dependency. If `SC027` is moved earlier than `SC026`, or `SC026` later than `SC027`, the conditioning environment disappears too soon and the shared failure set reappears: `fist`, `goose`, and `youth` come out with the wrong vocalism.

The main historical question is whether the literature actually describes two separable rules of this kind. The answer from the handbooks is mostly **no**. Standard descriptions usually present one broader North Sea Germanic / Ingvaeonic process: nasal loss before voiceless fricatives, accompanied by nasalization and compensatory lengthening of the preceding vowel. CAPR's two-rule split therefore looks less like a standard named pair from the literature and more like a model articulation of a bundled historical development.

## CAPR formulation

The live transducer makes the split explicit:

```foma
define NWGmcNasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*æ} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*á} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*é} -> {*ḗ} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*í} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ó} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ú} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative
];

define NWGmcNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

Historically, the safest reading is:

1. the literature strongly supports the **bundle** "nasal disappears before voiceless fricatives, with compensatory lengthening and often nasalization of the preceding vowel";
2. CAPR turns that bundle into two ordered formal stages so the conditioning environment remains visible to the transducer;
3. the chronology cards then show that, once the process is split formally, only the order `SC026 < SC027` is viable in the present model.

## Source dossier

### Campbell 1959
- source_key: Campbell1959
- locator: § 121
- terminology: "Ingvaeonic languages"; rejection of the nasal consonant with compensatory lengthening and nasalization
- quotation: "mf, ns, nþ also reject the nasal consonant with compensatory lengthening and nasalization of the preceding vowel"
- paraphrase: Campbell gives the cleanest classical OE-handbook statement of the change. He treats it as a West Germanic development shared by the Ingvaeonic languages and describes the result as one process, not as two separately named rules.
- conditioning: `mf`, `ns`, `nþ`
- chronology: a West Germanic / Ingvaeonic change older than specifically Old English local reshaping
- examples: `gōs`, `ōþer`, `tōþ`, `fīf`, `mūþ`, `sīþ`, `ūs`
- cautions: Campbell's formulation is excellent for the core historical claim, but it does not itself motivate CAPR's separate `SC026` / `SC027` split.

### Hogg 1992
- source_key: HoggPhonology1992
- locator: runic-name discussion of `*ansuz` in the phonology chapter (OCR lines 4134-4137)
- terminology: Inguaeonic dialects; rounding, loss of the nasal, compensatory lengthening
- quotation: "`*a` before a nasal plus fricative became `/o:/` due to rounding, loss of the nasal and compensatory lengthening of the vowel"
- paraphrase: Hogg gives a compact modern restatement of the North Sea Germanic process through the well-known `*ansuz > ōs` example. The passage is narrower than Campbell and Fulk because it foregrounds the `a`-branch, but it is still useful because it makes the internal sequence explicit: vowel change plus nasal loss belong to one connected process.
- conditioning: `a` before nasal + fricative, especially the `ans`-type pattern
- chronology: treated as an early Inguaeonic development rather than as a late OE rule
- examples: `*ansuz > ōs`
- cautions: the passage is not a full handbook survey of all vowel classes, so it should support the corridor only as one illustrative formulation rather than as the whole evidential base.

### Ringe and Taylor 2014
- source_key: RingeTaylor2014
- locator: chapter 5, "The northern West Germanic dialects", pp. 140-141
- terminology: northern West Germanic developments shown through outcome lists rather than a special rule-name label
- quotation: "`*jugunþi` 'youth' ... > OE geoguþ"; "`*gans` 'goose' ... > OE gōs"; "`*funsaz` 'ready, eager' ... > OE fūs"
- paraphrase: Ringe and Taylor are especially helpful for stage assignment. They treat these outcomes as part of the northern West Germanic dialect developments, with Old English, Old Frisian, and Old Saxon sharing the innovation in varying degrees. This supports reading the corridor as earlier and broader than a narrowly OE-only change.
- conditioning: vowel + nasal before voiceless fricative; the examples show `ns`, `nþ`, and related environments
- chronology: pre-OE in the relevant sense; inherited into the later OE system rather than first created there
- examples: `youth`, `goose`, `ready`, `head of cattle`, `favor`, `company`
- cautions: Ringe and Taylor mostly list reflexes and stage distribution; they do not argue for a distinct two-step chronology of "lengthening first, nasal loss second".

### Fulk 2018
- source_key: Fulk2018
- locator: § 4.11; see also § 6.4
- terminology: North Sea Germanic loss of a nasal consonant before a voiceless fricative, with nasalization and compensatory lengthening
- quotation: "in North Sea Germanic a nasal consonant was lost before any voiceless fricative, with nasalization and compensatory lengthening of the preceding vowel"
- paraphrase: Fulk gives the clearest compact comparative-grammar formulation of the process. The language is strongly bundled: the handbook rule is not "nasal spirant lengthening" plus "nasal spirant loss", but one North Sea Germanic sound change whose outcome includes both loss and lengthening.
- conditioning: before any voiceless fricative; explicitly `mf`, `ns`, `nþ`
- chronology: North Sea Germanic, hence broader than Old English alone
- examples: `fīf`, `gōs`, `fūs`, `ōðer`; in unstressed material `geoguþ`
- cautions: Fulk is excellent for the historical core and for the stage label, but it confirms that CAPR's two-rule split is analytic rather than a standard handbook partition.

### Luick 1914
- source_key: Luick1914
- locator: § 301.1; compare preceding discussion at § 299
- terminology: "Die Folge Vokal+n ... vor stimmlosen Spiranten"; long nasalized vowel later losing nasal quality
- quotation: "Die Folge Vokal+n wurde vor stimmlosen Spiranten zu langem nasalierten Vokal, der später seine Nasalität aufgab"
- paraphrase: Luick is useful because he explicitly separates subcases without turning them into separate named laws. He first states the general development of vowel + `n` before voiceless spirants into a long nasalized vowel, then gives the special `a`-branch and its later `ō`-type development. This is closer than most sources to the kind of branching CAPR formalizes.
- conditioning: general `V + n` before voiceless spirants; special handling for `a` before nasals in closed syllables
- chronology: filed under Anglo-Frisian developments affecting both stressed and unstressed syllables
- examples: `*jugunþ > *juzūþ`; `*beranþ > *berāþ`; accusative plurals with historical `-ns`
- cautions: Luick sharpens the internal phonological description, but he still does not require CAPR's exact two-step split as separate historical claims.

### Sievers-Brunner 1965
- source_key: SieversBrunner1965
- locator: § 186.1; lexical reflex support at § 269
- terminology: loss of nasals before voiceless spirants under original nasalization and lengthening of the preceding vowel
- quotation: "Geschwunden sind die Nasale vor den stimmlosen Spiranten f, þ, s unter urspr. Nasalierung und Dehnung des vorangehenden Vokals"
- paraphrase: Sievers-Brunner gives a concise traditional grammar statement very close to Campbell's but in even more explicitly bundled form. The section also lists a broad OE reflex set. Elsewhere the grammar records forms like `fyst`, showing that the changed vowel is part of the ordinary inherited OE lexicon rather than an isolated etymological curiosity.
- conditioning: nasal before voiceless `f`, `þ`, `s`, with special `a > ō`
- chronology: shared with Old Frisian and Old Saxon; not a specifically late OE innovation
- examples: `fīf`, `gōs`, `ōþer`, `sōþ`, `tōþ`, `ūs`, `mūþ`, `ȳst`; `fyst` as a later lexical reflex
- cautions: like Campbell and Fulk, Sievers-Brunner gives one bundled sound law, not two separately named historical stages.

## CAPR formulation versus literature

The literature supports three strong claims:

1. nasal + voiceless-fricative sequences lose the nasal;
2. the preceding vowel is lengthened and often described as first nasalized;
3. the development belongs to a North Sea Germanic / Ingvaeonic layer, not to an isolated late OE innovation.

What the literature does **not** usually do is split the process into a rule called "nasal spirant lengthening" followed by another called "nasal spirant loss". That terminology appears to be CAPR-internal.

The split is still defensible as a model explanation, because it makes two useful things explicit:

1. vowel quality and quantity changes must be computed while the nasal + spirant conditioning string is still present;
2. the nasal deletion step should not erase that conditioning too early.

So the safest formulation for later prose is:

- historically, the handbooks describe a **single bundled process**;
- formally, CAPR models that process as **two ordered stages**;
- the book should not pretend that every CAPR branch or label is itself a separate traditional law.

## Chronology implications

The literature independently supports only a limited chronology claim: the vowel effects and nasal loss belong together, and the process is early enough to be inherited by Old English from a wider North Sea Germanic / Ingvaeonic background.

The chronology cards add a more specific model-level claim:

1. `SC026` cannot move later across `SC027`;
2. `SC027` cannot move earlier across `SC026`;
3. the shared failure set is `fist`, `goose`, `youth`.

This evidence is strong, but it should be interpreted carefully.

- The cards show that **if** CAPR splits the process, only `SC026 < SC027` works.
- They do **not** by themselves prove that the historical literature recognized two independently ordered sound laws of exactly that shape.
- The earlier side of `SC026` remains runner-limited at bundled `PWGmcChanges`, so no earlier historical left boundary is currently identified.
- The later side of `SC027` is a no-break-before-boundary result through order 86 and must not be rewritten as a positive historical claim that the rule must precede `SC087`.

## Open questions

1. Should the eventual production report use the title **Nasal Spirant Corridor**, or should it foreground a more traditional label such as **Ingvaeonic / North Sea Germanic nasal loss before voiceless fricatives**?
2. How strongly should the production prose emphasize that `SC026` is a CAPR-internal analytic split rather than a standard handbook name?
3. Is the repository's present `NWGmc` filing the best historical stage label, or should the chapter prose more openly say that the literature often frames the process as North Sea Germanic / Ingvaeonic?
4. How prominently should `fist` be used in the eventual chapter, given that its attested path also depends on later material such as preconsonantal `x` loss and umlaut-sensitive developments?
5. Should the eventual production report remain a paired `SC026-SC027` corridor, or would a slightly wider chapter around `SC028` explain examples like `fist` more naturally?
6. Do later chapter drafts need a small lexical aside from Kroonen or Orel for the etyma of `goose`, `youth`, and `fist`, or is the current handbook evidence already sufficient?

## Dossier status

draft_complete
