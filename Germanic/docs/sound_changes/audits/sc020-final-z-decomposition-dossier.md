# SC020 final-*z* deletion — decomposition dossier (2026)

Companion to `sc020-final-z-firing-audit.tsv` (114 corpus firings, derived from
the committed Old English sandbox checkpoints bracketing SC020:
`..._after_pnwgmc_final_long_o_raising.bin` → `..._after_eaf_final_z_deletion.bin`).

## The single question

Is current SC020 — `EAFFinalZDeletion  {*z} -> 0 || _ .#.` — **one** historical
sound change, or **one broad computational rule conflating two** historically
distinct changes (an early general/WGmc loss of final *z in unstressed endings,
and a later northern/Ingvaeonic loss of final *z in stressed/monosyllabic
words)?

## Empirical corpus result (the firing audit)

Of 380 corpus derivations, SC020 fires on **114**. Classified by the form at the
point of firing:

| environment | count | class |
|---|---:|---|
| polysyllabic, **unstressed** final `-Vz` ending (root stressed, ending unstressed) | 111 | `early_unstressed_final_z_loss` |
| polysyllabic, **stressed** final vowel + z | 0 | — (none occur) |
| **true monosyllables** — `*z` directly on a stressed lexical root | 3 | `later_northern_final_z_loss` (candidates) |

The 3 monosyllables are: **book** `*bōkz > bōk`, **goose** `*gánsz > gáns`,
**louse** `*lūsz > lūs`.

Every firing deletes a word-final `*z`; there are zero anomalies (no firing on a
form not ending in `*z`, no firing on a medial `*z` — medial `*z` rhotacizes via
SC003 instead).

## A. The early loss

- **Environment:** word-final `*z` in **unstressed** syllables (overwhelmingly
  inflectional endings: nom.sg. masc. a-stem `*-az`, i-stem `*-iz`, u-stem
  `*-uz`, gen.sg. `*-ōz`, etc.). The 111 corpus firings are exactly this class.
- **Historical stage:** **Proto-West Germanic.** Ringe & Taylor (vol. 2 §3.1.1,
  pp. 44–45): "it seems most reasonable to ascribe the loss of word-final *z in
  unstressed syllables to **PWGmc**." It is pan-WGmc (Crist 2002 §5 calls it the
  "first WGmc *z-deletion … old news"; possibly attested as early as Tacitus /
  the Frienstedt comb c. 250–300 AD — Fulk §7.8, citing the comb's `kaba` for
  `kamba`). The precise label is **Proto-West Germanic**, not the looser "West
  Germanic": R/T assign it to PWGmc explicitly, and it is pan-WGmc in scope.
- **Relation to SC019:** SC019 (final long `*-ō → *-u`) must precede SC020 so
  that `*-ōz` stays sheltered by its *z* while bare `*-ō` raises
  (`*rástōz > ræste`). Confirmed (A) by the corpus and the Foma ordering
  comment.
- **Relation to rhotacism:** the early loss **precedes** rhotacism (Crist 2001
  pp. 104–106; Crist 2002 §6): final `*z` is deleted before it could rhotacize,
  and original `*r` does not delete in these environments (`*miz, *wīz > OE mē,
  wē`, but `*hēr > OE her`), so deletion is sensitive to the original `*r`/`*z`
  contrast. Implemented in CAPR by **scoping** (rhotacism is non-final), not
  cascade ordering — which is correct.

## B. The later loss

The firing audit's 3 monosyllables fall **outside** the early unstressed-ending
rule, because their `*z` sits on a **stressed** syllable (the root itself).

- **Ringe & Taylor (vol. 2 §3.1.1, pp. 44–45)** draw exactly this distinction:
  the loss of `*-z` "in **stressed** syllables—i.e. **monosyllables**—… was not
  uniform throughout WGmc and was clearly a **late** change, probably
  **post-PWGmc** (see §3.3.1). The relative chronology suggests that those were
  **two historically separate sound changes** (so Crist 2001: 107–8)." R/T note
  the alternative (a single change with a long, dialect-variable
  implementation) but judge it **less likely** because `*z`-loss shows none of
  the morphological interference typical of long-drawn-out changes.
- **Crist 2002 §§6–10** is more specific about the *secondary* deletion: it is
  **Ingvaeonic** and conditioned by a preceding **front vowel** —
  `*z > ∅ / {*i,*e} _ $`. §8 is categorical: "Non-final *z-deletion **never**
  occurs after back vowels in any WGmc language; not even one exception," and it
  "never occurs outside OE, OFris, OS" (i.e. Ingvaeonic), the lone OHG exception
  being the loan *mēta*. Crist's secondary rule must **precede rhotacism** and
  precede the Ingvaeonic `*ai > *a:` shift (his examples: `*wīz > OE wē`,
  `*miz > OE mē`, `*maiz`, `*twīn`, `*liznōn > leornian`).
- **Stage/scope of the later loss:** post-PWGmc, **northern West Germanic /
  Ingvaeonic**. This is established comparatively (it does **not** occur in OHG
  except by loan; it is shared by OE/OFris/OS), not merely asserted from the OE
  data — so "Ingvaeonic / northern WGmc" is the justified label, not a label
  chosen because only English shows it.
- **Mismatch with the corpus monosyllables (important):** CAPR's 3 monosyllabic
  firings are **back-vowel** (`ō`, `á`, `ū`), so they are **not** covered by
  Crist's front-vowel-conditioned secondary rule. Under the literature, a
  stressed monosyllabic `*-z` after a back vowel would be expected to survive to
  rhotacize (→ `*bōr`, `*gānr`, `*lūsr`), as it does in the `*huzda > hoard` /
  `ord` type (where the *z is followed by another consonant). CAPR's
  unconditional `_.#.` deletion removes them instead. This is the one place where
  the broad CAPR rule is **wider than any single documented historical law**:
  it sweeps the back-vowel monosyllables in with both the early unstressed rule
  and the front-vowel Ingvaeonic rule. (Whether OE bōc/gōs/lūs reflect a genuine
  late monosyllabic *-z loss that the handbooks do not condition on vowel
  quality, or analogical/morphological loss of the nom.sg. marker, is a real
  open question — see Unresolved.)

## C. Reassessment: ONE rule or TWO?

**CASE B — TWO RULES.** The current SC020 conflates two historically distinct
sound changes:

1. **Early / Proto-West-Germanic:** word-final `*z`-loss in **unstressed**
   syllables (the 111 corpus firings). Pan-WGmc, possibly early.
2. **Later / post-PWGmc (northern WGmc / Ingvaeonic):** loss of `*-z` in
   **stressed** syllables, i.e. **monosyllables** (the 3 corpus firings).
   Not uniform across WGmc; late (R/T §3.1.1, §3.3.1). Crist's specific
   formulation is front-vowel-conditioned and Ingvaeonic.

This is not an assumption: R/T state the two-change analysis explicitly and cite
Crist for it. The single-CAPR-rule alternative (one change with a long variable
period) is considered and rejected by R/T as less likely.

**Corpus consequence:** 111 firings belong to the early rule; 3 (book, goose,
louse) belong to the late monosyllable class. The split is empirically clean in
the corpus.

**Caveat recorded for Nathan:** the CAPR rule is unconditional (`_.#.`); it does
not itself encode the early (unstressed) vs late (stressed/monosyllabic)
distinction — the corpus separation is produced entirely by the *inputs*, not by
the rule. A genuine split would have to encode the stress/syllable conditioning
explicitly, and would still leave the back-vowel monosyllables (book/goose/louse)
requiring their own justification (see Unresolved).

## D. Proposed split architecture (NOT implemented)

Per the stable-identifier principle, **SC020 keeps the identity of the
earlier/core loss**; the later change gets a **new** stable ID. Do not renumber.

### SC020 (revised) — early/core final-*z* loss
- **stable ID:** SC020 (unchanged)
- **display name:** Proto-West-Germanic final unstressed *z*-deletion
- **Foma sketch:** `{*z} -> 0 || [unstressed final syllable] _ .#.` — i.e.
  restrict to *z in an unstressed word-final syllable (the exact stress encoding
  depends on CAPR's stress marks; the rule would target a final syllable whose
  vowel bears no primary-stress mark).
- **environment:** word-final *z in unstressed syllables (inflectional endings)
- **historical stage:** Proto-West Germanic (pan-WGmc)
- **historical scope:** pan_wgmc
- **reader-facing chapter:** Ch. 2 (PWGmc→AF) — arguably Ch. 2 end
- **corpus witnesses:** the 111 unstressed-ending firings (beard `*-az`,
  beaver `*-uz`, belly `*-iz`, …)
- **relative chronology:** after SC019 (raising shelters *-ōz); before rhotacism
- **computational dependencies:** must precede SC003 rhotacism (scoping) and
  SC040 (medial u-lowering); must follow SC019.

### NEW rule — later northern final-*z* loss
- **stable ID:** the next **unused** stable SC id, chosen by CAPR convention (not
  by chronology). (The audit does not assign a number; Nathan chooses the free
  slot at implementation time.)
- **display name:** Northern West Germanic final *z*-deletion (stressed
  monosyllables)
- **Foma sketch:** `{*z} -> 0 || [stressed monosyllable] _ .#.` — *z in a
  stressed word-final syllable of a monosyllable. (If Crist's front-vowel
  conditioning is adopted, the environment is further narrowed to
  `{*i,*e} _ .#.`; the corpus's back-vowel cases then need separate handling.)
- **environment:** word-final *z in stressed monosyllables
- **historical stage:** post-PWGmc, northern West Germanic / Ingvaeonic
- **historical scope:** north_wgmc (Ingvaeonic)
- **reader-facing chapter:** Ch. 3 (post-PWGmc / northern developments)
- **corpus witnesses:** book `*bōkz`, goose `*gánsz`, louse `*lūsz`
- **relative chronology:** before rhotacism (Crist); before the Ingvaeonic
  `*ai > *a:` shift; later than the early SC020.
- **computational dependencies:** to be probed; must be ordered relative to
  rhotacism and to the `*ai` monophthongization.

## E. Revised rhotacism relation

The existing partial-order edge `SC020 < SC003` (rhotacism follows *z*-deletion;
B, via scoping) historically concerns the **early** deletion — it is the early
unstressed loss that clears final `*z` before rhotacism. Under the split:

- **early SC020 < SC003 rhotacism:** retained (Crist's "rhotacism must have
  followed the rules eliminating *z by deletion").
- **later northern loss vs rhotacism:** Crist places his secondary (front-vowel)
  deletion **before** rhotacism too ("must precede rhotacism, since original *r
  does not delete in this environment"). So the later rule is **also < SC003**,
  but for a distinct, narrower environment. The single blanket `SC020 < SC003`
  edge should therefore be understood as covering *both* deletions' precedence
  over rhotacism; if the split is implemented, the edge should be re-pointed at
  the **early** rule as the primary constraint and the later rule annotated
  separately. Neither requires a cascade move — both are implemented by scoping.

## Unresolved questions

1. **Back-vowel monosyllables (book, goose, louse):** Crist's secondary rule is
   front-vowel-only, so these are not covered by it. Is OE bōc/gōs/lūs (a) a
   genuine late monosyllabic final-*z* loss not conditioned by vowel quality,
   (b) analogical loss of the nom.sg. *-z marker in monosyllabic a-stems, or
   (c) something else? This needs a targeted check before the later rule's exact
   environment is fixed. (CAPR currently produces the correct OE outputs for all
   three, so this is a *historical-accuracy* question, not a *correctness* bug.)
2. **Whether CAPR should encode the front-vowel restriction** of Crist's
   secondary rule or a simpler monosyllable rule — pending #1.
3. **Choice of new stable SC id** for the later rule — deferred to Nathan.

## Recommendation change

SC020's audit recommendation is changed from `metadata_only /
implementation_needed=no` to **`rule_split_required /
implementation_needed=yes_after_author_review`**. The split is **not**
implemented here; no `germanic.txt` or `.bin` change is made.
