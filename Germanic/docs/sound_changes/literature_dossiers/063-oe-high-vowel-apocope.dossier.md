# SC063 OE High Vowel Apocope — literature dossier

## Rule metadata
- change_id: SC063
- display_name: OE High Vowel Apocope
- FOMA rule: OEHighVowelApocope
- current_order: 63
- historical_stage: Old English
- pipeline_stage: Old English
- trace_occurrence_count: 65
- example_lexemes: beaver, beech, belly, bier, birth; additional trace slices show field, fist, flood, hand, hearth
- aliases searched: OE High Vowel Apocope; Old English high vowel apocope; high vowel apocope; apocope of high vowels; loss of final i; loss of final u; final high vowel loss; final -i; final -u; apocope after heavy syllables; apocope after light syllables; Sievers' Law and apocope; heavy syllable apocope; final unstressed high vowels; Old English apocope; Campbell apocope; Hogg apocope; Ringe Taylor apocope; Fulk apocope; Brunner apocope; Luick apocope; final high-vowel apocope; high-vowel apocope

## FOMA definition

```foma
define OEHighVowelApocope [
    # Disyllabic: long syllable (long vowel + consonant(s)) + final vowel
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    # Disyllabic: diphthong + consonant(s) + final vowel
    # LONG diphthongs are heavy (any C count). SHORT diphthongs are heavy only
    # with 2+ consonants; a short diphthong + single C is a LIGHT syllable (from
    # back-umlaut of a light stem, Campbell §345; DEV_NOTES §17.17).
    # E.g. *spéru → speoru (LIGHT, retain -u); *xérdō → heord (HEAVY, lose -u).
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    # Disyllabic: heavy closed syllable (short vowel + 2+ consonants) + final vowel
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    # Trisyllabic: long/diphthong + unstressed syllable + final vowel (Campbell §345)
    # Pattern: LongV/Diph + C+ + shortV + C+ + final_vowel
    # Example: heofon < *xemonų: *e*o + *β + *u + *n + *ų
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic with short-diphthong first syllable (from back-umlaut of a light
    # stem): trisyllabic apocope still fires regardless of stress-syllable weight
    # (Campbell §345). E.g. *xémonų → *xéomonų → heofon.
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic: short syllable + another syllable + final vowel (Campbell §345)
    # Pattern: shortV + C + shortV + C+ + final_vowel
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic with heavy-by-position first syllable (short V + 2+C) +
    # light second syllable + final high V (Campbell §345; DEV_NOTES §17.45.4).
    # E.g. *spénnilō → *spinnilu → *spinnil (then OELAdjacentSyncope + nn-degem → spinl).
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # R/T §6.6.1: vowel-hiatus contraction — word-final *i after long vowel
    # with no intervening consonant (e.g. root noun dat.sg. *kūi → cȳ)
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
    # Campbell §238/§346: final -u lost after /h/ (*x) regardless of weight.
    # Must fire before intervocalic h-loss would remove the conditioning.
    # E.g. *féxu → *féoxu → feoh (not feou).
    {*u} -> 0 || {*x} _ .#.,
    {*ų} -> 0 || {*x} _ .#.,
    {*i} -> 0 || {*x} _ .#.
];
```

## Working description

The live transducer deletes final high vowels `*i`, `*u`, and `*ų` in a large set of heavy disyllabic and trisyllabic environments. It also includes two especially order-sensitive extensions:

1. loss after vowel hiatus following a long vowel;
2. loss after final `*x`, which must precede later `h/x` loss.

In the compact trace, SC063 often turns fuller inflected or stem-final forms into the attested shorter Old English outputs: `*béβru > *béβr`, `*bōku > *bōk`, `*byrdi > *byrd`, `*flōdu > *flōd`, `*xéordu > *çéord`.

The literature strongly supports the basic weight-sensitive rule and its close relation to earlier general syncope. The main questions for later order-sensitivity work are not whether apocope exists, but exactly how the heavy/light and trisyllabic conditions should interact with exceptions such as Mercian `-u` retention and later analogical restoration.

## Chronological source dossier

### Luick 1914
- source_key: Luick1914
- locator: §§ 304-308
- witness_used: `docs/references/luick_historische_grammatik.txt`
- locator_confidence: section_safe
- terminology: `Urenglischer Schwund kurzer Vokale`; `i-, u-Schwund`; `Apokope`; `Sievers`
- quotation:

  > "Im Auslaut schwanden i und u unmittelbar nach langer Tonsilbe, und auch nach kurzer, wenn darauf noch eine andere Silbe folgte (nicht aber unmittelbar nach kurzer)."
  >
  > "Standen i und u nach langer Tonsilbe, auf welche noch eine andere folgte, so war diese Mittelsilbe entweder lang und nebentonig ... so daß Apokope eintrat ... oder sie war kurz ... kein Schwund eintrat."
  >
  > "Dieses Schwundgesetz, welches E. Sievers gefunden hat, ist sicher gemeinwestgermanisch, wenn es auch im Altsächsischen und Althochdeutschen durch Ausgleichungen stärker verwischt ist als im Altenglischen."

- paraphrase: Luick gives one of the clearest older formulations of the rule: final `i/u` are lost after heavy syllables and in the relevant trisyllabic environments, but not immediately after a short stressed syllable. He is also very useful for the dossier because he treats the trisyllabic split explicitly and ties the law to Sievers.
- conditioning: final `i/u` are lost after long stressed syllables and after short stressed syllables followed by another syllable; trisyllabic outcomes depend on the relative prominence of the second and third syllables
- chronology: Luick places the `i/u` loss after i-umlaut and before later prehistoric developments such as the older vowel-expansion processes discussed immediately afterward
- examples: `twām`, `þām`, `giest`, `dēd`, `flōd`, `word`, `werod`; trisyllabic contrast `strengþu` versus `heafodu`
- interaction with other changes: closely linked to medial-vowel loss, composition-fuge loss, syllabification of resonants, and later analogical leveling
- disagreements or cautions: the OCR witness is usable, but any direct publication-quality quotation from Luick should be checked against page images because line-break normalization was needed
- notes: OCR/text witness; quotations lightly normalized for broken line wraps and spacing, with no substantive wording changes

### Campbell 1959
- source_key: Campbell1959
- locator: §§ 345-349
- witness_used: `docs/references/campbell_old_english_grammar.txt`
- locator_confidence: section_safe
- terminology: early Old English loss of unaccented vowels; syncopation; loss in final unaccented syllables
- quotation:

  > "w and ȳ, whether originally short, or due to Gmc. reduction of older long vowels ... were lost in Prim. OE, in final unaccented syllables after a long accented syllable, or a short accented syllable and another syllable. They remained after a short accented syllable, or a long accented syllable followed by a short syllable."
  >
  > "When i and u of a final syllable are followed by a consonant, there is no loss."

- paraphrase: Campbell is still the most direct section-safe handbook statement of the weight-sensitive apocope rule. His adjacent sections are also useful because they separate pure final apocope from the compound and medial-syncopation contexts that can mimic it.
- conditioning: final high vowels are lost after heavy monosyllables and after the relevant trisyllabic patterns; they remain after simple light monosyllables and when a following consonant blocks pure final loss
- chronology: the rule belongs in Campbell's early OE loss of unaccented vowels and follows the preceding syncopation material
- examples: `word`, `weorod`, `fatu`, `hēafodu`, `ār`, `firen`, `giest`, `wine`, `dēm`, `nere`
- interaction with other changes: compounds and following-consonant environments can preserve vowels or shift the evidence into medial syncopation rather than final apocope
- disagreements or cautions: Campbell's older notation needs translation into the current rule inventory, but the conditioning itself aligns closely with the live transducer
- notes: repository text witness; no substantive normalization

### Hogg 1992
- source_key: HoggPhonology1992
- locator: p. 121
- witness_used: `docs/references/hogg_vol1.txt`
- locator_confidence: page_safe
- terminology: apocope; loss of unstressed vowels; syncope
- quotation:

  > "Apocope affected the high vowels /i/ and /u/ and occurred most regularly when they were preceded by a single heavy syllable ... But apocope also occurred in trisyllabic words if the first syllable was light, and therefore we find weorod 'troops' from *weorodu, compare heafodu 'heads' without apocope because the first syllable is heavy!"
  >
  > "The high vowels were also subject to syncope in medial positions after a heavy syllable."

- paraphrase: Hogg gives the best concise modern prose summary of SC063 and also keeps apocope and syncope conceptually adjacent. That pairing is especially useful for a dossier on a technical, order-sensitive rule.
- conditioning: final `i/u` apocope after heavy monosyllables and in the light-first-syllable trisyllabic pattern; medial syncope after heavy syllables
- chronology: Hogg presents vowel loss as earlier than the later large-scale reduction in the variety of unstressed vowels
- examples: `feti > fet`, `word` beside `scipu`, `weorod`, `heafodu`, `*yldira > yldra`
- interaction with other changes: apocope and syncope are distinct but neighboring processes in the early loss of unstressed vowels
- disagreements or cautions: Hogg is summarizing a fairly classical account here rather than opening major historiographical disputes
- notes: repository text witness; no substantive normalization

### Ringe and Taylor 2014
- source_key: RingeTaylor2014
- locator: §§ 6.8.1, 6.8.4
- witness_used: `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- locator_confidence: section_safe
- terminology: apocope of short high vowels; relative chronology of sound changes
- quotation:

  > "After general syncope had run its course, short *i and *u were lost word-finally after a heavy syllable and after an unstressed syllable preceded by a stressed light syllable."
  >
  > "Apocope and the shortening of unstressed long vowels are the last prehistoric OE sound changes."

- paraphrase: Ringe and Taylor give the cleanest explicit chronology for SC063: apocope follows general syncope and belongs at the end of prehistoric Old English. Their section also organizes the examples morphologically, which is useful for later chapter drafting.
- conditioning: final short `i/u` are lost after heavy syllables and after light + unstressed + final-vowel trisyllabic sequences
- chronology: apocope follows general syncope and is among the last prehistoric OE sound changes
- examples: `mearc`, `heord`, `firen`, `gierd`, `word`, `byrg`, `giest`, `hand`, `cweorn`
- interaction with other changes: the chronology diagram puts apocope after general syncope and before the post-apocope changes of section 6.9
- disagreements or cautions: the repository witness gives clear section anchors, but the OCR/page markers do not align transparently with the printed pagination, so section locators are safer than page locators here
- notes: repository text witness; no substantive normalization

### Fulk 2018
- source_key: Fulk2018
- locator: § 5.6
- witness_used: `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`
- locator_confidence: section_safe
- terminology: later preliterary changes of medial and final vowels; retention of unstressed high vowels after light syllables but not heavy; syncope
- quotation:

  > "the pattern of retention of unstressed high vowels after light syllables but not heavy is plainer in WGmc. than elsewhere"
  >
  > "Again, a sequence of light syllable plus another of any weight is equivalent to a heavy syllable (§2.5) in regard to this change"
  >
  > "An exception to the rule is that, at least in OE, although a medial high vowel in an open syllable might be expected to have been syncopated after a heavy syllable, it is instead preserved before the inflection -u, as in OE (Mercian) ... lytelu ... and nētenu"

- paraphrase: Fulk is especially good for turning the traditional rule into a compact comparative statement. He also contributes one of the most useful exception notes for later order-sensitive implementation work: Mercian `-u` preservation in forms like `lytelu` and `nētenu`.
- conditioning: high vowels are retained after light syllables but not heavy; a light syllable followed by another syllable counts as equivalent to a heavy environment; some `-u` inflectional environments resist the expected loss
- chronology: Fulk treats the change as part of later preliterary changes of medial and final vowels; the same section places it after earlier WGmc vowel developments and before the later literary-period reduction story
- examples: `wine`, `bryd`, `egesa`, `hierde`, `sunu`, `hand`, `deofol`, `we(o)rod`, `lytelu`, `nētenu`
- interaction with other changes: Fulk explicitly links the OE pattern to i-umlaut chronology and to neighboring syncope processes
- disagreements or cautions: the OCR witness is good enough for dossier work, but any final published quotation should be checked against the PDF page image
- notes: Google Vision OCR witness; quotations lightly normalized for line-wrap cleanup and spacing only

## Thematic synthesis

### Names and terminology

The sources do not converge on one single label as neatly as they did for SC043. Modern English-language handbooks usually call the process **apocope** of final high vowels or simply discuss the **loss of unstressed high vowels**. Luick uses the older German labels **`i-, u-Schwund`** and **`Urenglischer Schwund kurzer Vokale`**, while Campbell embeds the rule in early OE loss of unaccented vowels rather than foregrounding a single named sound change. For chapter drafting, **OE High Vowel Apocope** is a good repository label, but the text should acknowledge that older scholarship often frames it under broader unstressed-vowel loss rather than as a standalone named rule.

### Conditioning

Across the verified source set, the main conditioning is highly stable:

1. final short `i` and `u` are lost after a **heavy syllable**;
2. they are also lost in **trisyllabic** forms where the first stressed syllable is light and followed by another unstressed syllable;
3. they are retained after a **simple light stressed syllable**;
4. medial syncope is related but distinct;
5. some inflectional environments, especially Mercian `-u`, can preserve a vowel that might otherwise be expected to disappear.

The most technically valuable refinements are:

1. Luick's and Campbell's emphasis that trisyllabic outcomes are not reducible to simple absolute-final deletion;
2. Fulk's statement that **light syllable + another syllable** behaves as equivalent to a heavy environment for this change;
3. Campbell's reminder that when the final high vowel is **followed by a consonant**, pure final apocope is not the right analysis.

### Chronology and ordering

The sources support a fairly stable local chronology:

1. i-umlaut and earlier unstressed-vowel developments;
2. early and general medial syncope;
3. final high-vowel apocope;
4. later shortening/reduction of unstressed long vowels and then the post-apocope literary-period developments.

More specifically:

1. Luick explicitly places the `i/u` loss **after i-umlaut**.
2. Ringe and Taylor explicitly place apocope **after general syncope**.
3. Ringe and Taylor further state that apocope is among the **last prehistoric OE sound changes**.
4. The live transducer's extra branches for final `*x` and vowel-hiatus contexts fit the general logic of "late, order-sensitive weak-tail reduction", though those special branches are more model-specific than the basic handbook rule.

Relative to nearby pipeline rules, the literature points to the following dossier-level expectations:

1. **preceding final-vowel losses**: earlier non-high-vowel loss belongs before SC063;
2. **nasal apocope**: distinct from SC063 and not treated as the same law in the handbook sources;
3. **weak-tail reduction**: SC063 is one major component of the weak-tail collapse, but not the whole story;
4. **j-loss**: forms like `*çindj > *çind` show why the apocope/j-loss boundary matters computationally;
5. **medial syncope**: closely adjacent and chronologically earlier;
6. **later unstressed-vowel reduction**: later than the main apocope event.

### Examples

Examples cited by the literature:

1. Luick: `giest`, `dēd`, `flōd`, `word`, `werod`, `strengþu`, `heafodu`
2. Campbell: `word`, `weorod`, `fatu`, `hēafodu`, `giest`, `wine`, `dēm`, `nere`
3. Hogg: `fet`, `word`, `scipu`, `weorod`, `heafodu`, `yldra`
4. Ringe and Taylor: `mearc`, `heord`, `firen`, `gierd`, `word`, `byrg`, `giest`, `hand`
5. Fulk: `wine`, `bryd`, `egesa`, `hierde`, `sunu`, `hand`, `we(o)rod`, `lytelu`, `nētenu`

Examples from the transducer trace:

1. `beaver`: `*béβru > *béβr > *béβer`
2. `belly`: `*bálgi > *bealgi > *bielʤi > *bielʤ`
3. `bier`: `*bǣru > *bǣr`
4. `birth`: `*búrdi > *byrdi > *byrd`
5. `flood`: `*flōdu > *flōd`
6. `hand`: `*xándu > *xánd`
7. `hearth`: `*xérdu > *çéord`
8. `harvest`: `*xærbistu > *çierβistu > *çierβist`

### Disagreements and open questions

1. The basic conditioning is stable, but the **trisyllabic branch** is the most delicate part of the rule and the most likely place for later order-sensitivity work.
2. The exact boundary between **apocope** and **medial syncope** is not merely terminological; it affects how paradigms are narrated and how the computational rules are staged.
3. Fulk's Mercian `-u` exceptions (`lytelu`, `nētenu`) and Luick's trisyllabic alternations suggest that the eventual order-sensitivity runner should pay special attention to inflectional categories rather than only phonological shapes.
4. The live transducer's explicit final-`x` and vowel-hiatus subclauses are reasonable but more granular than the standard handbook presentation; they may need a separate technical note in the eventual chapter.
5. Older sources vary between treating the rule as a self-contained law and folding it into a broader history of unstressed-vowel loss.

## Source desiderata

1. SieversBrunner1965: searched in the local Google Vision witness, but no dossier-ready section-safe quotation was harvested in this pass.
2. Bulbring1902: searched and identified as relevant in the contents, but not yet harvested into a clean source block.
3. Kaluza1906: searched without a clean dossier-ready extract in this pass.
4. Wright1925: likely useful for comparison if a third pass is needed on traditional OE school grammars.
5. A later dedicated check against page images would be prudent for Luick1914 and Fulk2018 before any final-volume direct quotation is chosen.

## Dossier status

pilot_complete
