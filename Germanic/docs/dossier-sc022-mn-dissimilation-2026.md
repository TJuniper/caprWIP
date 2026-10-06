# Dossier: SC022 Germanic `mn`-dissimilation (`-mn- > -bn-/-βn-`) — 2026

Registry-verdict: SC022=REFORMULATE/RETAIN

**Scope:** the historical sound change modelled by CAPR SC022
`PNWGmcMnDissimilation`. Research only; **no production change**. This is the
sound-change companion to the lexical dossiers `dossier-stem-2026.md` and
`dossier-stem-consonant-variation-2026.md`, and to the computational probe
`audits/2216-stefn-shadow-rule-probe.md`. It does not repeat them.

Evidence labels: **ESTABLISHED / PROBABLE / POSSIBLE / UNRESOLVED / REJECTED**.
Every claim is tagged **[SOURCE]**, **[CAPR]**, **[INFERENCE]**, or **[OPEN]**.

## 1. Research question

What is the actual Germanic sound change (or set of changes) involving `m`
before `n` that CAPR represents as SC022 — its conditioning, chronology,
regularity, and comparative basis — and should the current `heaven` (`mV…n`)
environment and adjacent `mn` be one rule or historically distinct?

## 2. Current CAPR implementation (verified live)

- **SC022 `PNWGmcMnDissimilation`** (`germanic.txt:2151-2153`; cascade order
  22, between SC021 `PNWGmcUnstressedORaising` and SC023 `PNWGmcNStemNLoss`):
  ```foma
  {*m} -> {*β} || EnglishStarVocalic _ EnglishStarVocalic EnglishStarConsonant* EnglishStarNasal
  ```
  Output `{*β}`; surface `f` via `{*β} -> f` at OldEnglishOrthography
  (`germanic.txt:902`). Environment = **intervocalic `m`** with a later nasal
  (`heaven` shape). Cited: Fulk §6.14 (recte §6.11, p. 121), K-S s.v. Himmel.
- **Second, later rule `OENasalDissimilation`** (`germanic.txt:2668`):
  `{*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [V|.#.]`,
  cited K-S s.v. Himmel + Campbell §381. **[CAPR]** CAPR therefore already
  encodes the `mV…n` change **twice** (a PNWGmc `*m→*β` and an OE `*m→*f`),
  the second now largely bled by the first. This redundancy is itself an
  argument that the current segmental formulation is ad hoc (see §15).
- **Existing production applications:** exactly **one** corpus row triggers
  SC022 — `heaven` (2068, `*xémonų → *xéβunų → … → heofon`). **[CAPR]**

## 3. Source inventory (local corpus first)

| Source (locator) | Local file | Contribution |
| :-- | :-- | :-- |
| Fulk 2018 §6.11 **"Further changes common to Germanic"**, p. 121 (+ n. 6) | `fulk_comparative_grammar_early_germanic.vision.txt:7332,7365,7403` | mn→(denasalized) as a **Common-Germanic** tendency; "hardly regular"; reverse `bn>mn` in NWGmc; heaven heteroclisis; `stefn/stemn` "rather insecure" |
| Polomé 1967, pp. 818–819 | `polome_1967_reflexes_ie_ms.txt:867` | Germanic `-mn- > *-bn-` (older); heaven parade case; `stefn:stemn` 'prow' doublet; later OHG `-mn->-mm-`; `*stab-` alt (n. 2) |
| Kroonen 2013 EDPG, p. 220 (heaven), p. 480 (voice) | `kroonen_etymological_dictionary_pgmc.vision.txt:12428,24696,1738` | heaven = **mn-stem** `*hemina-~*hemna-`, labial from oblique cluster; voice `*-mn- > *-bn-` |
| Kroonen 2011 *The PGmc n-stems*, §4.3.3; pp. 183, 286 | `kroonen_2011_n_stems.vision.txt:126,1770,1421,8286,12975` | mn-stem paradigmatic allomorphy; ON `himinn`/dat. `hifni` syncope; "vocalization of the m" |
| Kroonen 2006 "mn-stems: bottom and rime", *ABäG* 61, §§1–4, pp. 17–20 | `kroonen_2006_mn_stems_bottom_rime.txt:1,45` | PIE `*-Cmn- > *-Cn-` after labial; **nom vs oblique allomorphy → daughters generalize one allomorph** |
| Kluge–Seebold, s.v. *Himmel* | `kluge_seebold_etymologisches_woerterbuch.txt:42427` | from g. `*himena-`; OE `heofon`/OS `heban` "das m dissimilatorisch zu v (stimmhafter bilabialer Reibelaut) weiterentwickelt" |
| Campbell 1959 §484 (p. 195), §193.d (p. 75) n. 4, §381 (p. 135, "Suffix Confusion") | `campbell_old_english_grammar.txt:12570,5504,10326` | OE **secondary WS `fn>mn`**; `-in-/-en-` suffix confusion (heaven's suffix) |
| Ringe–Taylor 2014 vol. 2, p. 346 | `ringe_taylor_linguistic_history_vol2.txt:18934` | voice chain `*stebno > … > stefn > stemn` |
| Orel 2003, p. 371 | `orel_handbook_germanic_etymology.vision.txt:41239` | `*stamnaz *stamniz`; **Torp separates `*stabnaz`** (the `*stab-` alt) |
| Luick §75 (p. 103); Brunner §193.2 (p. 156); Bülbring §485 (p. 191) | resp. files | OE secondary WS `fn>mn` (Anglian keeps `fn`/`stæfn`) |

No local Nielsen or Voyles file was found. Bammesberger 1990 present but not
decisive here. Web search not required; local corpus settles the questions.

## 4. Terminology and phonetic interpretation

**[SOURCE]** Descriptions used:
- Fulk §6.11 (p. 121): "the first consonant [of `mn`] tends to **lose its
  nasality by dissimilation**."
- Kluge–Seebold s.v. Himmel: "das m **dissimilatorisch zu v (stimmhafter
  bilabialer Reibelaut)** weiterentwickelt" — i.e. `m → [β]`.
- Polomé pp. 818–819: `-mn- > *-bn-` (a stop `b`), later realised as spirant.
- Kroonen EDPG p. 480: "the change `*-mn- > *-bn-`."

**Answers.**
1. Articulatorily: the first nasal (`m`), before a following nasal, **loses
   nasality → a voiced labial obstruent** (denasalization/dissimilation).
   **ESTABLISHED.**
2. `b` vs fricative: sources reconstruct `*-bn-` (a stop; Polomé, Kroonen),
   but K-S explicitly gives the OE/OS outcome as `[v]/[β]` (bilabial
   fricative). Both a stop stage and a fricative outcome are in the
   literature. **ESTABLISHED (stop reconstruction) / ESTABLISHED (fricative
   outcome).**
3. **[CAPR]** CAPR's `{*β}` matches K-S's explicit "stimmhafter bilabialer
   Reibelaut" (= β) and is a defensible **surface-oriented** choice; it
   telescopes the reconstructed `*b`→`*β` step. It is a phonetic
   approximation, not a claim that no `*b` stage existed. **PROBABLE-adequate.**
4. **Rule name:** "Dissimilation" is source-supported (Fulk, K-S use
   "dissimilation"). But the label is partly a misnomer for the mechanism:
   modern accounts (Kroonen) treat it as **paradigmatic allomorphy** (oblique
   cluster) rather than a purely segmental dissimilation. **[OPEN]** — do not
   rename now (§15).

## 5. Adjacent `mn` (`-mn- > -bn-`)

**[SOURCE]** Secure/relevant examples of the cluster change:

| Input | Daughter reflexes | Morphology | Author invokes change? | Leveling? | Source |
| :-- | :-- | :-- | :-- | :-- | :-- |
| voice `*stebnō ~ *stemnō` (`< *stem-n-`) | Go `stibna`, OE `stefn`~`stemn`, OFri `stemme`, OS `stemna`, OHG `stimna` | ō/n-stem | yes (`*-mn->*-bn-`) | yes (branch-specific) | Kroonen EDPG p. 480; Ringe–Taylor p. 346 |
| 'name' `*naman-`/obl. `*namn-` | ON `nafn`, Go `namō` | mn-stem | yes | yes (ON `fn` vs Go `m`) | Fulk §6.11 n. 6 (p. 121) |
| 'collect' `*samn-` | ON `safna ~ samna`, `saman` | verb/adv | yes | yes | Fulk §6.11 n. 6 (p. 121) |
| 'even' `*ebna-` (Go `ibns`) | OE `efn ~ emn` | adj | (comparandum) | OE `fn~mn` | Fulk §6.11 n. 6 (p. 121) |
| stem/prow `*stamnaz~*stamniz` | ON `stafn`, OE `stefn`~`stemn`~`stefna`, OS `stamn`, OHG `stam` | a/i/n-stem | yes (Polomé) | yes | Polomé p. 819; Orel p. 371 |

**Environment:** post-vocalic `m` immediately before `n`. **Following `n`
specifically** (not any nasal) is the attested trigger in the cluster cases.
Preceding vowel is normal (clusters are intervocalic-of-the-word). **[SOURCE]**
**Regularity:** Fulk: "hardly regular," and the **reverse `bn > mn` is well
attested in NWGmc** (e.g. OE secondary WS `fn>mn`, §OE below). So the surface
distribution is bidirectional and lexically uneven. **PROBABLE (change real) /
UNRESOLVED (surface regularity).**

## 6. The `heaven` / `mV…n` type

**[SOURCE — decisive]** Kroonen EDPG p. 220 reconstructs heaven as an
**mn-stem**: PIE `*h₂ék-mōn`, gen. `*h₂k-mn-ós`, loc. `*h₂k-mén-i` → remodelled
Gmc paradigm **nom. `*hemō`, gen. `*hemnaz`, dat. `*hemeni`**, whence the two
stems `*hemina-` (→ Go `himins`, ON `himinn`) and **`*hemna-`** (→ OE `heofon`,
OS `heban`). The labial `heofon/heban` comes from the **oblique `-mn-`
cluster** (or syncope of `*hemina- > *hemna-`). ON `himinn` keeps nom `-min-`
but **dat. `hifni` < `*himnai`** shows the very same `-mn- > -fn-` in the
oblique (Kroonen 2011:1770; Polomé p. 818). Fulk §6.11 (p. 121) likewise files
`heofon/heban` under the `mn` change and notes the heteroclitic `l`-stem
`himil`. K-S s.v. Himmel: `*himena-` → OE `heofon` by the same dissimilation.

**Answers to Part-III questions.**
1. The historical structure is **`-mn-` (oblique/syncopated cluster)**, not a
   stable `mV…n`. **ESTABLISHED.**
2. The medial vowel is original in the **nom.** (`*hemina-`) but absent in the
   **oblique** (`*hemnaz`). **ESTABLISHED.**
3. Yes — **syncope/oblique zero-grade produced the `-mn-` cluster** that fed
   the change (Kroonen; ON `hifni`). **ESTABLISHED.**
4. **The apparent `mVn` rule is the surface reflex of mn-stem allomorphy.**
   **PROBABLE→ESTABLISHED.**
5. Fulk, Kroonen, K-S treat `heaven` as **the same development** as direct
   `mn > bn`. **ESTABLISHED.**
6. **[CAPR]** CAPR's `mV…n` environment is therefore a **segmental surface
   approximation** that catches heaven from its *vowel-retaining* input
   (`*xémonų`), not from the historical oblique cluster. **INFERENCE.**

## 7. One change or two?

- **Analysis A (one phonological tendency):** the first of two nasals
  denasalizes, whether adjacent (`mn`) or vowel-separated (`mV…n`).
  Supported by Fulk (both under one heading) and K-S. **PROBABLE.**
- **Analysis B (morphological/allomorphic unity):** both surface types reflect
  **inherited mn-stem allomorphy** (nom vocalized-`m` vs oblique `-mn-`
  cluster); the labial spread by leveling. Supported by Kroonen 2011/2006,
  Polomé. **PROBABLE→ESTABLISHED** and the deeper, more accurate account.
- **Analysis C (historically distinct):** adjacent `mn` and the heaven pattern
  are unrelated changes. **REJECTED** — no source separates them; every
  detailed account unifies them.

**Adjudication [INFERENCE, high confidence]:** heaven and adjacent-`mn` are the
**same historical change** (`-mn- > -bn-`), differing only in whether the
conditioning cluster survived directly (stem, ON `hifni`) or was leveled from
the oblique into a `mV…n` shape (OE `heofon`). Analysis B is primary, with A as
its surface description. **This means adding adjacent `mn` to SC022 is
historically *more* accurate, not a stretch.**

## 8. Comparative Germanic distribution

| Gloss | Gothic | Old Norse | Old English | Old Frisian | Old Saxon | OHG/German | Reflex pattern |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| heaven | `himins` (m) | `himinn` (m) / dat. `hifni` (fn) | `heofon` (f) | `himel` (l) | `heban` (b)/`himil` (l) | `himil`/`Himmel` (m) | m ~ f/b ~ l; oblique fn in ON |
| voice | `stibna` (b) | — | `stefn`~`stemn` | `stemme` (mm) | `stemna` (m) | `stimna`~`stimma` | b ~ f ~ m ~ mm |
| stem/prow | — | `stafn` (f) | `stefn`~`stemn`~`stefna` | `stevene` (v) | `stamn` (m) | `stam`(m) | f/v ~ m ~ m(m) |
| name | `namō` (m) | `nafn` (fn) | `nama` (m) | — | `namo` (m) | `namo` (m) | m ~ fn (ON) |
| even | `ibns` (bn) | `jafn` (fn) | `efn`~`emn` | — | `eban` | `eban` | bn ~ fn ~ mn |

**[INFERENCE]** The labial (b/β/f/v) appears sporadically across **all** older
branches (Go `stibna`; ON `stafn`, `nafn`, `hifni`; OE/OS heaven, stem, voice),
never uniformly — the hallmark of an **old cluster change plus independent
paradigm leveling**. Not a clean pan-Germanic *or* purely OE change. **PROBABLE.**

## 9. Paradigm allomorphy and leveling

**[SOURCE]** Kroonen 2006 §4 (p. 20): after Kluge's law "there must have been a
period … during which at least some n-stems had **two allomorphs: the
nominative stem without and oblique cases with a geminate** … **the daughter
languages have often generalized only one allomorph.**" The same allomorphic
logic governs mn-stems (Kroonen 2011 §4.3.3): nom with vocalized/full-grade
`m` vs oblique with the `-mn-` cluster (→ `-bn-`). ON preserves both
(`himinn`/`hifni`); OE/OS generalize the labial (`heofon`, `stefn`); Go/other
generalize the nasal.

**Adjudication [INFERENCE, high confidence]:** the "irregularity" is largely
**secondary** — the residue of a **regular prehistoric cluster change operating
on oblique `-mn-`**, later obscured by branch- and word-specific leveling.
**PROBABLE→ESTABLISHED.** CAPR may model a deterministic segmental
approximation, **but the book must state that it approximates leveled
allomorphy, not a surface-exceptionless law.**

## 10. Chronology

- **[SOURCE]** Fulk places the change under **"changes common to Germanic"**
  (§6.11, p. 121). Gothic `stibna` (voice) shows the labial → the cluster
  change is at least **late Proto-Germanic / Common Germanic**. **ESTABLISHED.**
- **[SOURCE]** The *leveling* that fixes OE `heofon`/`stefn` is **NWGmc/OE- and
  OS-specific** (Go `himins`, ON `himinn` keep nom `m`). **ESTABLISHED.**
- **[CAPR/OPEN]** CAPR's label **`PNWGmc`** conflates the two: the underlying
  cluster change is older (PGmc/Common Gmc), while the OE surface outcome is
  later. **Is "PNWGmc" the correct stage label? → UNRESOLVED, leaning "too
  early-named vs the change / defensible for the OE outcome."** The label is
  imprecise but not clearly wrong for a rule that fixes the OE reflex.

## 11. Ordering vs brightening and i-umlaut

**[CAPR — from shadow probe]** With adjacent `mn`:
`*stámnaz → *stáβna → (EAFBrightening) *stæβna → … → stæfn`, and
`*stámniz → *stáβni → *stæβni → (OEIUmlaut) *steβni → stefn`.
So SC022 must precede **EAFBrightening** (else `*a` would be before a nasal and
resist fronting) and **OEIUmlaut**.
- **i-umlaut after:** trivially correct — i-umlaut is a late pre-OE/OE change.
  **ESTABLISHED.**
- **Brightening after mn-dissimilation:** needs the labial in place before AF
  brightening fronts `*a→*æ`. **[SOURCE-indirect]** Attested **Anglian `stæfn`**
  (Campbell §484 p. 195; Bülbring §485 p. 191, "Ru.¹ hat stemn neben stæfn")
  shows exactly a fronted `æ` before the labial cluster — consistent with
  brightening applying **after** denasalization. **PROBABLE** (indirect, since
  no source gives the explicit relative order). No direct ordering statement
  found — **[OPEN]** flag for confirmation.

## 12. The `*stab-` alternative

**[SOURCE]** Orel p. 371 reports **Torp** *separates* `*stabnaz` (to `*stab-`
'staff, post'; ON `stafr`, Skt `stabhnóti`) from `*stamnaz`; Polomé p. 819 n. 2
raises the same ("unless ON `stafn` … belong to `*stab-`"); Fulk §6.11 n. 6
(p. 121) calls the `stefn/stemn` etymology "rather insecure." Under `*stab-`,
the `f` of `stefn/stafn` would be **root-etymological**, not from `-mn-`.

**Status classification:** **serious but secondary / UNRESOLVED.** It is a
long-standing recorded alternative, not a fringe idea, and it is specifically
about the **stem/prow `f`-forms** — the exact forms row 2216 would target. It
does **not** threaten the sound change itself (heaven, voice `stibna` are
independent), but it **blocks labeling the row-2216 `stefn < *stamn-`
derivation ESTABLISHED**. **REJECTED as decisive against the sound change;
UNRESOLVED for the stem-word etymology.**

## 13. Regularity and productivity

**[SOURCE]** Fulk §6.11 (p. 121): "the results are hardly regular, and the
reverse change (of `bn` to `mn`) is well attested in NWGmc." Read **in context**
(a paragraph on paradigm-obscured cluster changes), "hardly regular" refers to
the **surface distribution across the lexicon** (leveling in both directions),
**not** to the impossibility of a regular underlying change. Combined with
Kroonen's allomorphy account (§9), the best-supported reading is: **a regular
prehistoric cluster change, obscured by later paradigm leveling and a
counter-directional OE `fn>mn`.** **PROBABLE.** Therefore a **deterministic
segmental CAPR approximation is defensible**, provided the book flags the
leveling.

## 14. Candidate historical formulations (abstract; no code)

| Formulation | Historical accuracy | Coverage | Exceptions | Relation to heaven | Fits stem? | FST-representable? |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `m > b / _ n` (adjacent cluster) | high (the real change) | direct clusters (stem, voice, name, even) | leveled/`*stab-` cases | heaven only after positing oblique cluster | yes | yes (segmental) |
| `m > β / V _ V C* N` (current SC022) | low-historical / surface-only | heaven (vowel-retaining input) | doesn't cover clusters | is the heaven rule | no (misses `mn`) | yes (current) |
| **Union: `m > β / _ n` ⊕ current** | best available segmental | heaven **and** stem/voice | leveling still lexical | unifies both | yes | yes (shadow-tested) |
| Paradigm-sensitive (oblique-cluster) | highest | historically exact | needs morphological input | native | yes | **no** (CAPR is segmental, lacks paradigm cells) |

**[INFERENCE]** The **union** formulation (add post-vocalic `m > β / _ n` to the
existing heaven branch) is the best that CAPR's segmental architecture can do
while being historically *more* faithful than the status quo; the fully
accurate paradigm-sensitive account is not representable in CAPR's segmental
FST and would instead be handled by **selecting the right PROTOFORM per row**
(the standing CAPR method).

## 15. Implications for SC022 (adjudication)

1. **Is the current SC022 historical description correct?** **PARTLY /
   UNRESOLVED (high conf).** It captures a real change but describes it as an
   intervocalic-`m` dissimilation, whereas the history is an oblique `-mn-`
   cluster change leveled into `mV…n`.
2. **Is its environment too narrow?** **YES (high).** It misses the direct
   `-mn-` cluster (stem, voice), which is the *core* case.
3. **Is its environment historically misformulated?** **YES (medium-high).**
   `mV…n` is a surface generalization of a cluster change (§6).
4. **Should adjacent `mn` ultimately be added?** **YES (medium-high).**
   Historically accurate; shadow-tested clean (blast radius = 1 row; heaven
   unchanged). Contingent on §16.
5. **Should the current `mV…n` environment remain?** **YES (high).** It is
   needed to derive heaven from CAPR's vowel-retaining input; removing it would
   break `heofon`.
6. **Should SC022 be split into two sound changes?** **NO / UNRESOLVED
   (medium).** Historically they are one change; a split would misrepresent
   that. (CAPR's *existing* second rule `OENasalDissimilation` is redundant and
   is a candidate for consolidation, not a historical second change.)
7. **Should its name change?** **PROBABLE-YES (low-medium), later.**
   "MnDissimilation" is defensible but the mechanism is allomorphic; any rename
   is a downstream decision.
8. **Is `PNWGmc` correct?** **UNRESOLVED (medium).** The cluster change is
   older (Common Gmc, Fulk §6.11); the OE outcome is NWGmc-era. Defensible but
   imprecise.
9. **Is `*β` defensible internally?** **YES (high).** Matches K-S "bilabialer
   Reibelaut"; a reasonable telescoping of `*b→*β`.
10. **Does the dossier support eventual `*stámniz → stefn` for row 2216?**
    **QUALIFIED-YES / UNRESOLVED (medium).** The sound change is real and
    CAPR-modelable and the derivation is clean; but the **`*stab-` alternative**
    keeps the specific stem-word etymology from ESTABLISHED, and `stemn` (WS)
    vs `stefn` (base) vs `stæfn` (Anglian) as the *selected comparator* is a
    lexical decision (see the variation dossier).

## 16. Implications for row 2216

**[INFERENCE]** The sound change licenses `*stámniz → stefn` **mechanically**
(heaven already proves CAPR models `-mn-`-labialization; the shadow proves the
adjacent branch yields `stefn` uniquely with zero collateral). The **residual
scientific risks are lexical, not phonological**: (a) `*stab-` (is `stefn` even
from `*stamn-`?); (b) comparator choice (`stefn` base vs WS `stemn`, currently
selected). Both must be weighed by the implementation-planning task, not
resolved by the sound change alone.

## 17. Recommended sound-change-book treatment (content, not prose)

- **Main text:** a Common-Germanic change whereby, in the cluster `-mn-`, the
  `m` denasalizes to a voiced labial (`*-bn- > -βn-/-fn-`); illustrate with
  **heaven** (mn-stem: nom `*hemina-` vs oblique `*hemnaz`; ON `himinn`/`hifni`;
  OE `heofon`) as the existing worked example, and (cautiously) **stem** as the
  cluster case. Chronology: cluster change late PGmc/Common Gmc; OE outcome via
  NWGmc leveling.
- **Footnote:** paradigm allomorphy (Kroonen 2006/2011) as the mechanism;
  branch-specific leveling; the OE secondary WS `fn > mn` (Campbell §484) that
  reverses the surface in West Saxon.
- **Caution (main text or prominent note):** results are "hardly regular"
  (Fulk); CAPR models a **segmental approximation** of leveled allomorphy.
- **Caution / exclude from strong claims:** the **`*stab-`** alternative for
  `stefn/stafn` — flag as unresolved; do **not** present `stefn < *stamn-` as
  certain.
- **Exclude:** the OHG `-mn- > -mm-` (Stimme) as a *separate later* dialectal
  development, not this change.

## 18. Established conclusions

- **ESTABLISHED:** a Germanic change `-mn- > -bn-` (m denasalizes before n),
  with a voiced-labial outcome (`b`/`β`/`f`/`v`) (Polomé, Fulk, K-S, Kroonen).
- **ESTABLISHED:** heaven is an **mn-stem**; its labial derives from the oblique
  `-mn-` cluster (Kroonen EDPG p. 220; ON `hifni`).
- **ESTABLISHED:** heaven and adjacent-`mn` are **one** historical change
  (Analysis B/A); Analysis C **REJECTED**.
- **ESTABLISHED:** CAPR's `{*β}` output and the surface `f` are historically
  appropriate.
- **PROBABLE:** the change is a **regular prehistoric cluster change obscured by
  leveling**; "hardly regular" refers to surface distribution.
- **PROBABLE:** ordering — mn-dissimilation before AF brightening and i-umlaut
  (indirect support: Anglian `stæfn`).

## 19. Remaining uncertainties

- **UNRESOLVED:** the `*stab-` etymology for `stefn/stafn` (blocks ESTABLISHED
  status for the *stem-word* application).
- **UNRESOLVED:** exact stage label (`PNWGmc` vs PGmc/Common Gmc + NWGmc
  leveling).
- **UNRESOLVED:** explicit relative-ordering statement for
  denasalization-before-brightening (only indirect evidence found).
- **OPEN (CAPR):** consolidation of the redundant `OENasalDissimilation`
  (`*m→*f`) with SC022 (`*m→*β`); rule name; whether to reformulate SC022 around
  `m` before any nasal vs before `n` specifically (attested trigger is `n`).

## 20. Bibliography / exact locators

- Fulk, R. D. (2018). *A Comparative Grammar of the Early Germanic Languages*.
  §6.11 "Further changes common to Germanic", p. 121 (+ n. 6).
  [`fulk_comparative_grammar_early_germanic.vision.txt:7332,7365,7403`]
- Polomé, E. C. (1967). "Notes on the Reflexes of IE /ms/ in Germanic." *RBPh*
  45.3, pp. 818–819. [`polome_1967_reflexes_ie_ms.txt:867`]
- Kroonen, G. (2013). *EDPG*, p. 220 (`*hemina-~*hemna-`), p. 480 (`*stimno-`,
  `*-mn->*-bn-`). [`kroonen_etymological_dictionary_pgmc.vision.txt:12428,24696,1738`]
- Kroonen, G. (2011). *The Proto-Germanic n-stems*, §4.3.3, pp. 183, 286.
  [`kroonen_2011_n_stems.vision.txt:126,1770,1421,8286,12975`]
- Kroonen, G. (2006). "Gemination and allomorphy in the PGmc mn-stems: bottom
  and rime." *ABäG* 61: 17–25, §§1–4 (pp. 17–20).
  [`kroonen_2006_mn_stems_bottom_rime.txt:1,45`]
- Kluge, F. & Seebold, E. *Etymologisches Wörterbuch*, s.v. *Himmel*.
  [`kluge_seebold_etymologisches_woerterbuch.txt:42427`]
- Campbell, A. (1959). *Old English Grammar*, §484 (p. 195), §193.d (p. 75)
  n. 4, §381 (p. 135). [`campbell_old_english_grammar.txt:12570,5504,10326`]
- Ringe, D. & Taylor, A. (2014). *TDOE* (vol. 2), p. 346.
  [`ringe_taylor_linguistic_history_vol2.txt:18934`]
- Orel, V. (2003). *HGE*, p. 371 (`*stamnaz *stamniz`; Torp `*stabnaz`).
  [`orel_handbook_germanic_etymology.vision.txt:41239`]
- Luick §75 (p. 103); Brunner (Sievers–Brunner) §193.2 (p. 156); Bülbring §485
  (p. 191) — OE secondary WS `fn>mn`.

Cross-references: `dossier-stem-2026.md`,
`dossier-stem-consonant-variation-2026.md`,
`audits/2216-stefn-shadow-rule-probe.md`. CAPR rule:
`Germanic/fsts/germanic.txt:2151-2153` (SC022) and `:2668`
(`OENasalDissimilation`).

## 21. Close-out re-adjudication (2026-09)

This close-out preserves the implemented literal adjacent-cluster rule and the
selected `*stámniz > stefn` derivation. It rechecks only the historical scope
and chronology metadata; it neither changes the FST nor treats `heofon` as a
direct application of SC022.

### Verdict

**RETAIN SC022 AS IMPLEMENTED; RECLASSIFY ITS HISTORICAL STAGE.** The source
record does not securely support a Proto-Northwest-Germanic or pan-NWGmc
innovation. Fulk places `mn` denasalization among the changes “common to
Germanic” and adduces a Gothic suffixal alternation as well as OE/OS
*heaven* evidence [@Fulk2018, p. 121, §6.11]. Polomé likewise dates
`-mn- > -bn-` to older Germanic, while stressing that later paradigm leveling
obscures the distribution [@Polome1967, pp. 818--819]. The secure historical
classification is therefore **late Proto-Germanic / Common Germanic**, with a
pan-Germanic innovation claim qualified by uneven daughter reflexes and later
analogical replacement.

The stable executable identifier `PNWGmcMnDissimilation` is retained as a
legacy CAPR identifier, not as a historical stage claim. The later NWGmc/OE
facts are the paradigmatic generalization or reversal of the cluster outcome:
Fulk explicitly notes the reverse `bn > mn` in NWGmc [@Fulk2018, p. 121,
§6.11], and Campbell documents secondary West Saxon `fn > mn`
[@Campbell1959, p. 195, §484].

### Heaven and stem

The evidence continues to distinguish the sound change from analogy. Old Norse
*himinn* beside dative *hifni* preserves the alternation in different
paradigm cells; OE *heofon* and Old Saxon *heban* instead generalize the
labial-bearing allomorph [@Polome1967, pp. 818--819; @Kroonen2011,
p. 183]. Thus selected `*xébun > heofon` begins after that analogical
generalization and is not a corpus firing of SC022. The literal adjacent
cluster in selected `*stámniz > stefn` remains a mechanically correct
working baseline, but its specific etymology remains qualified by the
documented `*stab-` alternative [@Polome1967, p. 819 n. 2; @Orel2003,
p. 371].

### Relative chronology

No new positive local ordering is added. The completed first-break search is
boundary-limited on both sides, so it remains negative computational evidence,
not a historical adjacency claim. The only broad chronology asserted here is
that the underlying Common-Germanic cluster development predates its
NWGmc/OE analogical reversals. The suggestive `stæfn` evidence is insufficient
to add a separate SC022 < Anglo-Frisian brightening edge: neither the primary
handbooks nor the present corpus supplies an explicit local ordering statement.
