# SC058 OE Nasal Dissimilation residual — literature dossier

## Rule metadata

- change_id: SC058
- display_name: OE Nasal Dissimilation
- FOMA rule name: `OENasalDissimilation`
- current_order: 58
- chronology_card: `Germanic/docs/sound_changes/order_tests/chronology_cards/SC058-oe-nasal-dissimilation.md`
- representative failures / examples:
  - none from positive first-break evidence
- local chronology summary:
  - no positive earlier break
  - earlier side reaches bundled `PWGmcChanges`
  - no positive later break
  - later side reaches the current `SC087` runner boundary
  - both sides are methodological/search limits, not historical chronology claims

## FOMA definition

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

## Working description

CAPR implements SC058 as a narrow medial nasal-dissimilation step: short-vowel
`m ... n` sequences can yield `f ... n` in a restricted Old English environment.
That explicit implementation is real in the model, but the chronology card is
negative in both directions and the source tradition is thin.

This dossier therefore exists mainly to document the thinness honestly. The
goal is not to manufacture a strong source-backed chapter. It is to show that
there is some scattered handbook support for comparable `mn`-type dissimilation
and a few lexical Old English outcomes, while also showing that the checked
sources do **not** present a major named OE law matching CAPR's exact rule.

## Search log

| Source file searched | Productive? | Evidence found | How it is used |
| --- | --- | --- | --- |
| `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` | yes | direct generic statement that `mn` loses nasality by dissimilation, with OE `heofon` and `fæstenn` among the examples | strongest direct but still broad support |
| `docs/references/ringe_taylor_linguistic_history_vol2.txt` | yes | `enetre` with "loss of the second *n by dissimilation", plus separate `heofon` and `festen` outcomes | lexical corroboration, not a chapter statement |
| `docs/references/campbell_old_english_grammar.txt` | partial | `heofon` and `fasten` appear, but under other vowel/suffix discussions rather than a nasal-dissimilation chapter | shows surrounding lexical material, not a direct law |
| `docs/references/hogg_vol1.txt` | partial | `heofon` appears under velar/back umlaut discussion, not as a named OE dissimilation rule | confirms lack of a direct handbook chapter |
| `docs/references/luick_historische_grammatik.txt` | partial | `enitre`, `samboren`, `heofon` appear as scattered lexical material under other developments | useful for residual corroboration only |

No productive checked source recovered a literal handbook heading or exact OE law
name equivalent to "OE Nasal Dissimilation".

## Source dossier

### Fulk 2018

- source_key: Fulk2018
- locator: §6.11
- witness_used: `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`
- locator_confidence: section_safe
- terminology: dissimilation in `mn`
- short quotation: "In the cluster mn, the first consonant tends to lose its nasality by dissimilation, though the results are hardly regular"
- paraphrase: This is the strongest direct source support recovered in the local files. Fulk explicitly states a Germanic/Northwest-Germanic tendency for `mn` to lose nasality by dissimilation and immediately warns that the results are irregular. He includes OE `heofon` and OE `fæstenn` among the examples. That makes the basic type historically real, but only as a scattered and uneven phenomenon rather than as a major OE textbook law. [@Fulk2018, §6.11]
- chronology: Fulk gives no SC058-style local boundary. The value of the source is that it confirms a real dissimilation tendency while also warning against over-regularization. [@Fulk2018, §6.11]
- examples: `heofon`; `fæstenn`
- cautions: this is broad Germanic support, not a chapter-sized Old English rule.

### Ringe and Taylor 2014

- source_key: RingeTaylor2014
- locator: §§6.7.3--6.8.4; discussion around `enetre`
- witness_used: `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- locator_confidence: mixed_section_safe
- terminology: dissimilation; lexical OE outcomes
- short quotation: "loss of the second *n by dissimilation"
- paraphrase: Ringe and Taylor provide the clearest lexical corroboration that this kind of material still matters in Old English development. They derive `enetre` from `*anwintri` with loss of the second `*n` by dissimilation, and elsewhere they list `heofon` and `festen` as ordinary outcomes in the same general zone. That is useful evidence that comparable dissimilation survives into the same part of the system, but it still does not amount to a named OE chapter matching CAPR's exact `m > f` rule. [@RingeTaylor2014]
- chronology: the value here is lexical and comparative rather than chronological. The source does not give a positive first-break boundary for SC058. [@RingeTaylor2014]
- examples: `enetre`; `heofon`; `festen`
- cautions: these are scattered lexical witnesses, not a handbook law of SC058-sized scope.

### Campbell 1959 and Luick 1914

- source_keys: Campbell1959; Luick1914
- locator: Campbell on `heofon` / `fasten`; Luick on `enitre`, `samboren`, `heofon`
- witness_used:
  - `docs/references/campbell_old_english_grammar.txt`
  - `docs/references/luick_historische_grammatik.txt`
- locator_confidence: mixed_lexeme_safe
- short quotations:
  - Campbell: "So heofon is for older hefzen"
  - Luick: "`enitre` 'einjährig (aus *anwintri)"
- paraphrase: Campbell and Luick are useful mainly as negative controls. They do contain the relevant lexical material, but they treat it inside other chapters and suffixal/vocalic discussions rather than as a standalone nasal-dissimilation law. That is exactly the point this dossier needs to preserve: the source tradition knows the outcomes, but it does not elevate SC058 into a major handbook topic. [@Campbell1959; @Luick1914]
- chronology: neither source provides an SC058-like local chronology statement; both are better for confirming scattered lexical reality than for defining a chapter. [@Campbell1959; @Luick1914]
- examples: `heofon`; `fasten`; `enitre`; `samboren`
- cautions: these are supporting traces only.

### Hogg 1992

- source_key: HoggPhonology1992
- locator: back/velar umlaut discussion on `heofon`
- witness_used: `docs/references/hogg_vol1.txt`
- locator_confidence: page_safe
- short quotation: "Typical examples are: *sifon > siofon 'seven', *hefon > heofon ' heaven'"
- paraphrase: Hogg confirms the lexical reality of `heofon`, but he discusses it as part of umlautal vowel history rather than as a named nasal-dissimilation chapter. This is useful because it shows that even a major handbook source reaches the relevant lexeme without yielding a robust SC058-style law. [@HoggPhonology1992]
- chronology: no local chronology boundary for SC058 is supplied here. [@HoggPhonology1992]
- examples: `heofon`
- cautions: supporting lexical context only.

## CAPR formulation versus literature

The overlap between CAPR and the literature is real but limited.

1. CAPR explicitly implements a narrow Old English `m > f` dissimilation rule in
   a specific short-vowel environment.
2. The checked sources do recover comparable dissimilation behavior:
   irregular `mn`-type dissimilation in Fulk, `enetre` in Ringe and Taylor,
   and scattered lexical outcomes such as `heofon` and `fæstenn`.
3. The checked sources do **not** recover a strong named handbook chapter that
   corresponds neatly to CAPR's exact SC058 rule.
4. The current chronology card is negative on both sides, so the dossier should
   document thin support and methodological limits, not inflate SC058 into a
   chapter center.

## Chronology implications

1. The earlier side reaches bundled `PWGmcChanges` with no positive break. That is
   a runner limitation, not a historical left boundary.
2. The later side reaches the current `SC087` runner boundary with no positive
   break. That is likewise a search limit, not a historical right boundary.
3. The source tradition is consistent with keeping SC058 explicit but modest:
   there is enough scattered material to justify a real residual dossier, but not
   enough to treat the rule as a major source-backed law.
4. The honest final treatment is therefore the current one: retain SC058 as a
   short residual/context note and state clearly that both chronology sides remain
   boundary-limited.

## Dossier status

draft_complete
