# SC057 OE J Cluster Coalescence — literature dossier

## Rule metadata

- change_id: SC057
- display_name: OE J Cluster Coalescence
- FOMA rule name: `OEJClusterCoalescence`
- current_order: 57
- chronology_card: `Germanic/docs/sound_changes/order_tests/chronology_cards/SC057-oe-j-cluster-coalescence.md`
- representative failures / examples:
  - `bow`
  - `follow`
  - `hedge`
  - `seek`
  - `singe`
  - PGmc `*báugijaną` -> expected OE `bīeġan`; moved-too-early output `bēaġan`
  - PGmc `*sōkijaną` -> expected OE `sēċan`; moved-too-early output `sōċan`
- local chronology summary:
  - `SC052 < SC057`
  - later side has no real break before the current runner boundary at `SC087`
  - the later no-break result is runner-bounded and must not be read as `SC057 < SC087`

## FOMA definition

```foma
define OEJClusterCoalescence (
    [{*g} {*j} -> {*ʤ}]
    .o. [{*k} {*j} -> {*ʧ}]
);
```

## Working description

CAPR isolates a narrow `gj/kj` coalescence step on the late palatalization side of
the Old English cascade. That explicit step is historically legible, but the
handbooks do not usually promote it as a chapter-sized law of its own. They
instead discuss the same material inside the broader neighborhood of velar
palatalization, palatal diphthongization, and front mutation.

That is the right scale for SC057. The dossier should support the existing short
singleton note, not inflate the rule into a coequal companion to the promoted
SC051, SC052, or SC055-SC056 chapters.

## Source dossier

### Campbell 1959

- source_key: Campbell1959
- locator: §170; §440
- witness_used: `docs/references/campbell_old_english_grammar.txt`
- locator_confidence: mixed_section_safe
- terminology: influence of initial palatal consonants; palatalization and assibilation
- short quotation: "`[sk]` is more prone to palatalization and assibilation than `[k]`."
- paraphrase: Campbell treats the whole palatal consonant zone as one historical neighborhood. In the same run of sections he gives forms such as `giefan`, `giest`, and `hierde`, and later states that `[sk]` is especially prone to palatalization and assibilation. That is good support for the broader fronting and palatalization environment behind SC057, but not for a separate handbook chapter called "OE J Cluster Coalescence". [@Campbell1959, §170; §440]
- chronology: Campbell's organization keeps palatal-consonant effects on the left side of the later i-mutation / umlaut discussions. That supports the broad historical neighborhood behind `SC052 < SC057`, while still leaving CAPR's exact local edge as a model result rather than a textbook boundary. [@Campbell1959, §170; §440]
- examples: `giefan`; `giest`; `hierde`
- cautions: Campbell supports the neighborhood, not an isolated SC057-sized chapter.

### Hogg 1992

- source_key: HoggPhonology1992
- locator: pp. 107--108; pp. 111--112
- witness_used: `docs/references/hogg_vol1.txt`
- locator_confidence: page_safe
- terminology: palatalisation; palatal diphthongisation; i-mutation
- short quotation: "the new palatal consonants appear to have had an effect on immediately following front stressed vowels"
- paraphrase: Hogg separates palatalization from later palatal diphthongization and illustrates the latter with forms such as `giefan` and `sceap`. He also notes that palatalisation is generally taken to precede i-mutation. That gives SC057 good neighborhood support in the palatalization/fronting region, but still as a narrow follower inside a larger complex rather than as a standard chapter center. [@HoggPhonology1992, pp. 112--113]
- chronology: Hogg's ordering makes the leftward tie to earlier palatalization historically intelligible and keeps the later vowel-side developments distinct. [@HoggPhonology1992, pp. 112--113]
- examples: `giefan`; `sceap`
- cautions: this is broad structural support, not a direct handbook statement of SC057 as an independent law.

### Ringe and Taylor 2014

- source_key: RingeTaylor2014
- locator: §6.4.1; §6.5.1; §§6.6.1--6.6.4
- witness_used: `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- locator_confidence: section_safe
- terminology: palatalization of velars; West Saxon diphthongization by initial palatals; front mutation
- short quotation: "After initial velars and *sk had been palatalized, any following stressed non-high front vowel was diphthongized in WS"
- paraphrase: Ringe and Taylor give the clearest concise statement of the historical neighborhood SC057 belongs to. They keep palatalized velars and `*sk` on the consonant side, then treat later palatal-triggered diphthongization and front mutation as related but distinct developments, with examples such as `giefan`, `scieppan`, and `scieran`. This is strong support for the broad region that also produces the card's `bīeġan` / `sēċan` behavior, but it still does not amount to a classical chapter named after SC057 itself. [@RingeTaylor2014, §6.4.1; §6.5.1; §§6.6.1--6.6.4]
- chronology: this source is the strongest historical support for the left edge of SC057. It makes `SC052` the relevant earlier palatalization-side anchor, while leaving SC057's exact local serialization as a CAPR articulation inside that broader sequence. [@RingeTaylor2014, §6.4.1; §6.5.1; §§6.6.1--6.6.4]
- examples: `giefan`; `scieppan`; `scieran`
- cautions: Ringe and Taylor support the neighborhood strongly, but not a standalone SC057 textbook law.

### Fulk 2018

- source_key: Fulk2018
- locator: p. 28; §4.7; §4.13
- witness_used: `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`
- locator_confidence: mixed_page_section_safe
- terminology: front mutation; diphthongization by initial palatal consonants
- short quotation: "diphthongization by initial palatal consonants (which precedes front umlaut but not breaking)"
- paraphrase: Fulk is especially useful as a cautionary framing source. He keeps front mutation and palatal-triggered diphthongization distinct, and he treats forms such as `giest` and `scieran` as products of that broader neighborhood. That supports CAPR's decision to keep SC057 explicit on the palatal side of the umlaut region, while also making clear that the source tradition does not elevate SC057 itself into a major named law. [@Fulk2018, p. 28; §4.7; §4.13]
- chronology: Fulk supports the general direction "earlier palatalization-side developments -> later front-umlaut material", which makes `SC052 < SC057` historically plausible without converting the runner-bounded later side into history. [@Fulk2018, §4.7; §4.13]
- examples: `giest`; `scieran`
- cautions: Fulk is best for scale and chronology restraint, not for a direct SC057 witness set.

## CAPR formulation versus literature

The literature supports SC057 unevenly but usefully.

1. The sources strongly support the broader palatalization/fronting neighborhood in
   which CAPR places SC057.
2. They do **not** isolate a major standalone handbook chapter corresponding
   exactly to CAPR's `OEJClusterCoalescence` rule.
3. CAPR's one real positive chronology result is the local edge `SC052 < SC057`.
   That is historically legible because the sources put SC057's material on the
   later side of earlier velar-palatalization developments.
4. The later side is different: the current no-break result reaches the runner
   boundary at `SC087`, and none of the source material licenses turning that
   methodological limit into a historical claim.

## Chronology implications

1. `SC052 < SC057` is the only positive chronology edge that should carry real
   historical weight here.
2. `SC052` should remain a cross-reference only. The sources support the same
   neighborhood, but they do not require a non-contiguous SC052-SC057 chapter.
3. The later no-break result remains runner-bounded and must not be paraphrased as
   `SC057 < SC087`.
4. The honest final treatment is therefore exactly the current one: keep SC057 as
   a short finished singleton note, not as a large palatalization chapter.

## Dossier status

draft_complete
