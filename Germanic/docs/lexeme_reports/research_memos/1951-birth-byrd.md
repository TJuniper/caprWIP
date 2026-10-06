# Research memo — 1951 birth / byrd

## Starting point

- **ID:** 1951
- **CONCEPT:** birth
- **COUNTERPART:** byrd
- **PROTO:** *búrdiz
- **PROTOFORM:** *búrdiz
- **DERIVATION_CLASS:** regular
- **NOTE:** Kroonen *burdi- f. > OE (ġe)byrd; using simplex without ge-

This is a `regular` row whose memo is required because the TSV `NOTE` is non-empty. The immediate question is not whether the FST can derive the row — the packet shows that it can — but whether the row should represent attested simplex **byrd**, prefixed **ġebyrd/gebyrd**, or some other project normalisation of Kroonen’s etymological entry [@Kroonen2013].

## Packet evidence assessment

**Authoritative/current**

- The live TSV row and the compact derivation trace are current evidence for what the project presently models: **\*búrdiz → byrd** with a successful OE output.
- The row note is current evidence that the project already knows Kroonen cites OE **(ġe)byrd** and that the current choice is the simplex counterpart.

**Useful background**

- The packet’s lexical-table hit from `old_english_wiktionary.tsv` is useful because it shows a repo-local source that surfaces only **ġebyrd** for “birth”.
- The `mismatch_dossier_mizdo` and supplement passages are useful background because they treat row 1951 as a control case showing that this lexeme does **not** share the breaking problem of *mizdō*.

**Stale or superseded**

- The `DEV_NOTES` hit at §17.13.2 (`*búrdiz → byrde` expected `byrd`) is explicitly archived “for future-warning”; it is diagnostic history, not current evidence about the lexeme.
- The English-sandbox rhotic note mentioning `*burdiz` is about English surface modelling, not the OE row, and should not be elevated into OE philology.

**Irrelevant or misleading if over-read**

- The packet’s Wiktionary hit is not enough on its own to force a change from **byrd** to **ġebyrd**; it is only one lexical table, and fuller repo evidence shows both simplex and prefixed OE forms.
- The comparative aside in the *mizdō* dossier is background only. It helps with “no breaking here”, but it is not the project’s primary derivation statement for row 1951.

## Additional repo research

Beyond the packet, I checked:

- `Germanic/data/oe_known_problems.tsv` — no entry for *búrdiz* / row 1951.
- `Germanic/data/old_english_wiktionary.tsv` — “birth” is listed as **ġebyrd** only.
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` — Kroonen gives PGmc **\*burdi-** and OE **(ge-)byrd** [@Kroonen2013].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` — Clark Hall has simplex **byrd** ‘birth’ and also prefixed/extended **byrd/byrdo/byrdu** material [@ClarkHall1960].
- `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt` — Bosworth-Toller has a simplex **byrd, e; f. I. birth** entry and a large **ge-byrd** entry covering ‘birth’, ‘origin’, ‘lineage’, ‘rank’, etc. [@BosworthToller1898].
- `docs/references/hogg_vol1.txt` — Kastovsky lists **byrd** among deverbal feminines from **beran ~ boren** [@Kastovsky1992, p. 358].
- `docs/references/campbell_old_english_grammar.txt` — Campbell cites **gebyrd / gebyrdu** in declensional discussion, showing prefixed forms are well established in the grammatical tradition [@Campbell1959].
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` — checked for OE `eo` before `rd`; the `beordor` example is useful only as a reminder that breaking evidence belongs with front-vowel inputs, unlike **byrd** [@RingeTaylor2014].

I found no pilot or full lexeme report for this lexeme; coverage files only show that row 1951 still needs one.

## Reconstruction and early-stage forms

The evidence needs three levels kept separate:

1. **Cognate-set proto / etymological headword:** Kroonen’s dictionary entry is **\*burdi-** f., a stem-level comparative headword [@Kroonen2013].
2. **Project input form:** the TSV uses **\*búrdiz**, i.e. a full nominative singular input suitable for the derivation pipeline.
3. **OE target form represented by the row:** the row currently targets simplex **byrd**, while the note records that Kroonen’s OE reflex is **(ġe)byrd**.

For memo purposes, there is no strong reason to change the TSV from **\*búrdiz** to a different input form. The packet’s own compact trace already gives a satisfactory regular pathway to **byrd**. By contrast, the *mizdō* dossier’s comparative wording (“u-lowering → *bordiz* → … → *byrd*”) is best treated as loose background prose rather than the authoritative derivational sequence for this row, since the live compact trace does not depend on that extra step.

## Old English philology

Repo-local dictionary evidence supports **both** a simplex and a prefixed OE noun:

- Clark Hall has **byrd** ‘birth’ as a simplex entry [@ClarkHall1960].
- Bosworth-Toller likewise has simplex **byrd, e; f. I. birth** [@BosworthToller1898].
- Kroonen gives OE **(ge-)byrd**, explicitly allowing the prefixed variant [@Kroonen2013].
- Bosworth-Toller’s separate **ge-byrd** entry shows that the prefixed form is not marginal: it is used for childbirth, nativity, lineage, rank, and related senses [@BosworthToller1898].
- Campbell’s grammar cites **gebyrd / gebyrdu**, confirming that the prefixed form is grammatically well established [@Campbell1959].

So the philological issue is **not** “packet says byrd, dictionaries say ġebyrd”; it is that the OE lexeme family includes both **byrd** and **gebyrd/ġebyrd**, while the row must choose one modelling target.

The row’s current **byrd** should be understood as a citation-form choice, not as an inflected paradigm cell. The archived `byrde` mismatch note is therefore historical debugging noise, not evidence that the row should target an oblique form. I found no repo-local basis to make dialect or manuscript-specific claims here, so the final report should avoid them.

## Project problem and solution

The project problem is a **headword-selection** problem inside an otherwise regular derivation:

- Comparative etymology and some lexical tables point to OE **(ġe)byrd**.
- Repo-local historical dictionaries also attest simplex **byrd**.
- The derivation engine already produces **byrd** cleanly.

Given that, the current project solution — keep **COUNTERPART = byrd** and preserve the prefixed alternative in the note — is defensible. It lets the OE row stay aligned with an attested simplex form and with the unprefixed Modern English reflex, while still acknowledging Kroonen’s broader OE reflex notation.

What is missing is not a new derivation class but a clearer explanatory note. The current note compresses stem-level proto, project input form, and OE reflex choice into one sentence.

## Paradigm probe

A paradigm probe is **not required**.

This is not a late-analogy or paradigm-cell case. The core issue is whether the row should model simplex **byrd** or prefixed **gebyrd**, not whether a hidden inflectional cell such as dat.sg. **byrde** or plural **byrdu/gebyrdu** must be substituted for the lemma. Existing repo evidence already shows that the live row’s nominative-style target **byrd** is intentional and attainable.

## Recommended final report

Recommend a **short** final lexeme report only: distinguish Kroonen’s stem-level **\*burdi-** from project input **\*búrdiz**, note that OE evidence includes both simplex **byrd** and prefixed **(ġe)byrd**, and explain that the project keeps attested simplex **byrd** as the modelling target while mentioning the prefixed variant in the note. Do not spend space on the archived `byrde` debug history except, at most, as a sentence marking it as superseded.

## Data-change recommendations

- **TSV PROTO:** no change recommended.
- **TSV PROTOFORM:** no change recommended.
- **TSV COUNTERPART:** no change recommended; keep **byrd**.
- **TSV DERIVATION_CLASS:** no change recommended; keep **regular**.
- **TSV NOTE:** **change recommended.** Rewrite it so it explicitly distinguishes Kroonen’s stem-level **\*burdi-**, the project input **\*búrdiz**, and the fact that the row intentionally keeps attested simplex **byrd** even though OE **(ġe)byrd** is also attested.
- **`oe_known_problems.tsv`:** no change recommended.
- **`DEV_NOTES`:** no change recommended; the relevant hit is archived diagnostic history only.
- **Dossier text:** no required change for row 1951, though the comparative aside in `mismatch_dossier_mizdo*.md` could be harmonized later with the live compact derivation wording if that dossier is revised.
