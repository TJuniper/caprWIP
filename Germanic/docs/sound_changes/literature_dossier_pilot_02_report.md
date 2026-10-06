# Literature dossier pilot 02 report

## Summary

This pilot covers **SC063 OE High Vowel Apocope**. I searched the local witnesses for Campbell1959, HoggPhonology1992, RingeTaylor2014, Fulk2018, Luick1914, SieversBrunner1965, Bulbring1902, and Kaluza1906, starting from Google Vision OCR where available and otherwise using the repository text witnesses.

Verified relevant discussion was harvested from **Luick1914, Campbell1959, HoggPhonology1992, RingeTaylor2014, and Fulk2018**. The matrix now contains **10 verified SC063 rows**, replacing the earlier pilot stub. The dossier file was created at `literature_dossiers/063-oe-high-vowel-apocope.dossier.md`, and the SC063 change-entry stub now points to it. No source was unavailable locally, though Brunner, Bülbring, and Kaluza were searched without yielding a clean dossier-ready quotation in this pass.

## Source search

Shared search terms:

1. OE High Vowel Apocope
2. Old English high vowel apocope
3. high vowel apocope
4. apocope of high vowels
5. loss of final i
6. loss of final u
7. final high vowel loss
8. final -i
9. final -u
10. apocope after heavy syllables
11. apocope after light syllables
12. Sievers' Law and apocope
13. heavy syllable apocope
14. final unstressed high vowels
15. Old English apocope
16. Campbell apocope
17. Hogg apocope
18. Ringe Taylor apocope
19. Fulk apocope
20. Brunner apocope
21. Luick apocope

Sources searched:

| Source | Local witness used | Result |
| --- | --- | --- |
| Luick1914 | `docs/references/luick_historische_grammatik.txt` | verified |
| Campbell1959 | `docs/references/campbell_old_english_grammar.txt` | verified |
| HoggPhonology1992 | `docs/references/hogg_vol1.txt` | verified |
| RingeTaylor2014 | `docs/references/ringe_taylor_linguistic_history_vol2.txt` | verified |
| Fulk2018 | `docs/references/fulk_comparative_grammar_early_germanic.vision.txt` | verified |
| SieversBrunner1965 | `docs/references/brunner_1965_altenglische_grammatik.vision.txt` | searched; no clean matrix row harvested |
| Bulbring1902 | `docs/references/bulbring_altenglisches_elementarbuch.txt` | searched; contents and syncope/apocope signals found, no clean matrix row harvested |
| Kaluza1906 | `docs/references/kaluza_historische_grammatik_englisch.txt` | searched; no clean matrix row harvested |

## Verified source discussions

1. **Luick1914** — `§§ 304-308`: older historical-grammar statement of `i/u` loss, trisyllabic conditioning, and explicit attribution to Sievers.
2. **Campbell1959** — `§§ 345-349`: classic OE handbook account of apocope conditioned by syllable weight and by the presence or absence of a following consonant.
3. **HoggPhonology1992** — `p. 120`: compact modern summary of apocope and its relation to medial syncope.
4. **RingeTaylor2014** — `§§ 6.8.1, 6.8.4`: clearest explicit chronology, placing apocope after general syncope and among the last prehistoric OE sound changes.
5. **Fulk2018** — `§ 5.6`: comparative statement of the heavy/light split, the trisyllabic equivalence rule, and Mercian `-u` retention exceptions.

## Conditioning and chronology findings

The pilot confirms a stable shared analysis:

1. final short `i` and `u` are lost after **heavy syllables**;
2. they are also lost in the key **trisyllabic** environments;
3. they are retained after a **simple light stressed syllable**;
4. medial syncope is related but distinct;
5. some morphologically specific `-u` forms remain exceptional.

The clearest chronology is:

1. earlier unstressed-vowel developments and i-umlaut;
2. general syncope;
3. high-vowel apocope;
4. final shortening and then post-apocope historical changes.

Ringe and Taylor are especially useful here because they explicitly place apocope after general syncope and label it one of the last prehistoric OE sound changes.

## Disagreements or complications

1. The rule is stable in outline, but the **trisyllabic branch** remains the most delicate part of the analysis.
2. The line between **apocope** and **medial syncope** matters structurally, not just terminologically.
3. Fulk's Mercian exceptions and Luick's trisyllabic alternations warn against flattening the rule into a single blanket deletion.
4. The live FOMA rule includes final-`x` and hiatus subclauses that are computationally sensible but more specific than the usual handbook presentation.

## Quotation and witness handling

Direct quotations were collected generously because this dossier is an internal research file rather than final volume prose. Each verified quotation is tied to a source key and a page-safe or section-safe locator.

Witness handling in this pilot:

1. **Campbell1959, HoggPhonology1992, RingeTaylor2014** used repository text witnesses with stable section or page anchors.
2. **Fulk2018** used the Google Vision OCR witness.
3. **Luick1914** used the local OCR/text witness already present in the repo.

Quotations from OCR-derived witnesses were lightly normalized for broken line wraps and spacing only; no substantive rewording was introduced. The two quotations most worth checking against page images before any final published quotation are **Luick1914** and **Fulk2018**. For dossier work, the generous quotation policy worked well and should be retained.

## Dossier format assessment

The dossier structure worked well for a more technical, order-sensitive rule. Adding **`witness_used`** and **`locator_confidence`** was a real improvement over pilot 01, because this task relied more heavily on OCR-derived and section-based witnesses than the SC043 dossier did.

The format now feels stable enough to scale, with one caveat: future dossiers on technical rules should continue to distinguish clearly between **basic conditioning**, **chronology**, and **exception/interaction** rows in the matrix, because those categories become more important as the rules get more computationally delicate.

## Next recommended task

**B. Implement the order-sensitivity runner skeleton.**

Two dossier pilots now show that the literature-dossier method is stable enough to support the broader sound-change project. The most useful next step is to build the computational order-sensitivity scaffold that can test the very kinds of exceptions and neighbor interactions this SC063 dossier highlights.
