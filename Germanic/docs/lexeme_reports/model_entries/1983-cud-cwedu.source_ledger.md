# Source extraction ledger — cud / cwedu

This ledger records the evidence used for the P3 rewrite from pilot material.

| Source | Form(s) given | Claim relevant to the entry | Citation key available? | Where this claim was found locally | Confidence / review note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TSV row 1983 and compact trace | `PROTO *kwíθuz`; `PROTOFORM *kwéðuz`; `*kwéðuz -> cwedu` | Establish the live selected input and the stale lexeme-level proto metadata that was not changed in this pass. | no | `Germanic/data/germanic-aligned-final.tsv`; `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md` | high |
| Pilot report and research memo | `cwedu`; `cwidu`; `cweodu`; `cwudu`; `cudu` | Confirm that the row is an attested-variant choice rather than a paradigm-cell rescue. | no | `Germanic/docs/lexeme_reports/pilot/cud.md`; `Germanic/docs/lexeme_reports/research_memos/1983-cud-cwedu.md` | high |
| Kroonen | `*kwedu-`, homonym 2; OE `cwidu`, `cweodu`, `c(w)udu` | Masculine u-stem citation; the homonym number is not a phonological segment. | yes — `Kroonen2013` | held PDF sheet355, printed p.315, image checked | high on extraction; selection judgment pending |
| Orel | `*kwedwō(n)`; OE `cwidu` | Feminine headword with different morphology, not an identical quotation of Kroonen's stem. | yes — `Orel2003` | held PDF sheet266, printed p.227, image checked | high on extraction; selection judgment pending |
| Ringe and Taylor | PWGmc `*kwidu`; OE `cwidu > cwudu > cudu`; late WS `cweodu` | i-starting WGmc chain and ordinary back umlaut; does not here supply an explicit PGmc form or derive i by leveling from cwedu. | yes — `RingeTaylor2014` | text PAGE338, printed p.323; running head and reconstruction index checked | high on text/stage; direct local image unavailable |
| Clark Hall | `cwudu (eo, i)` | Confirms the variant family but not selected bare-e cwedu in this headword. | yes — `ClarkHall1960` | held PDF sheet84, printed p.69, image checked | high on extraction; target-attestation review pending |

## Citation-locator pilot 01 note (historical; superseded)

- The earlier pilot recorded purported page locators for `Kroonen2013` (p. 355),
  `Orel2003` (p. 266), `RingeTaylor2014` (p. 338), and `ClarkHall1960`
  (p. 84).
- Those numbers were sheet/extract labels, not printed folios. The present
  source survey corrects them to315/227/323/69 respectively; the paired
  model now uses those printed-page citations.

## Current reconstruction audit

The structured evidence is in
`../pgmc_reconstructions/forms.tsv` and its paired coverage table.
The different dictionary formations, Ringe-Taylor's expressly WGmc input
and the missing independent bare-e attestation must not be harmonized
into a claimed consensus. Current corpus PROTO/PROTOFORM, target and
class remain unchanged. The replacement citation/input and target
disposition require the consolidated source-backed decision, not an
automatic correction inferred from the old model's successful output.

## Notes

- The live TSV `PROTO` field is stale (`*kwíθuz`) relative to the current analysis, but the user explicitly asked for review-or-upgrade work without TSV edits; the stale metadata is therefore recorded here and in the implementation report, not corrected in this pass.
- Existing local vision-backed reference files were sufficient; no additional Google Vision rescue was needed.
- The current survey removes the homonym number from the reconstructed
  phonological stem in prose; the original pilot's stronger extraction
  assurances should not be used as proof of the older account.
