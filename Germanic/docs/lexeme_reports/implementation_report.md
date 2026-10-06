## Implementation report

The lexeme-report pilot infrastructure now consists of:

- `Germanic/docs/lexeme_reports/source_inventory.md`
- `Germanic/docs/lexeme_reports/report_schema.md`
- `Germanic/docs/lexeme_reports/missing_bibliography_keys.md`
- repo-local skill files under `Germanic/docs/agent_skills/`
- `Germanic/tools/oe_paradigm_probe.py`
- `Germanic/tools/oe_lexeme_report_coverage.py`
- pilot lexeme reports under `Germanic/docs/lexeme_reports/pilot/`

### What changed

The source inventory and schema files establish the evidence hierarchy, citation style, and per-entry markdown structure for the future `### Lexeme report` section. The new `oe_paradigm_probe.py` provides a repeatable way to compare small hand-specified sets of paradigm cells against the current OE FST and emit a Markdown table suitable for direct inclusion in pilot lexeme reports.

The infrastructure now also adopts a **selective-report policy**: the generated
report should include `### Lexeme report` only for OE rows with a non-empty
`NOTE`, a non-`regular` `DERIVATION_CLASS`, or an existing manual pilot/full
report. Ordinary `regular` rows with empty `NOTE` do not require generated
lexeme-report prose.

For delegated drafting work, the project now also requires **GPT-5.4**
(`gpt-5.4`) for Old English lexeme research memos and lexeme reports. The
packet-to-memo and memo-to-report stages are not considered suitable for
cheap/fallback agent models.

### Pilot entries completed

The following pilot report files have been drafted:

- `adder.md` (`regular`)
- `ban.md` (`late_analogy`)
- `berry.md` (`late_analogy`)
- `span.md` (`late_analogy`)
- `thistle.md` (`late_analogy`)
- `craft.md` (`early_analogy`)
- `bottom.md` (`early_analogy`)
- `fire.md` (`known_unmodelled`)
- `tap.md` (`known_unmodelled`)
- `buck.md` (`unexplained_unmodelled`)
- `reek.md` (`reconstructed_oe`)
- `cud.md` (`attested_variant`)

### Evidence used

The pilot reports were written from repo-local sources first:

- `Germanic/data/germanic-aligned-final.tsv`
- `Germanic/data/oe_known_problems.tsv`
- `Germanic/docs/DEV_NOTES.md`
- `docs/refs.bib`

Where the row notes already cited handbook or dictionary sources, the pilot reports use the repo's actual pandoc-style bibliography keys from `docs/refs.bib`, especially `[@Kroonen2013]`, `[@Orel2003]`, `[@RingeTaylor2014]`, `[@Campbell1959]`, `[@HoggGrammar1992]`, `[@SieversBrunner1965]`, `[@Fulk2018]`, `[@Stiles2012]`, `[@KlugeSeebold2011]`, `[@ClarkHall1960]`, and `[@Pokorny1959]`.

The selective-coverage side is audited by `Germanic/tools/oe_lexeme_report_coverage.py`,
which reads the live OE TSV and reports which rows require lexeme reports,
which required rows are already covered by manual pilot/full reports, and which
rows are intentionally outside coverage.

### What remains uncertain

- `oe_paradigm_probe.py` is intentionally small and hand-specified; it does not yet generate full paradigms automatically.
- The first pilot probe covers the key late-analogy and known-unmodelled analogy cases, but it still omits many cells explicitly.
- The pilot reports are deliberately concise. Several entries, especially `reek`, `thistle`, `cud`, and `fire`, could be expanded further once Nathan decides how dense the final prose should be.

### What should be reviewed before scaling up

Nathan should review:

1. Whether the current prose density is right for the eventual generated report.
2. Whether the pilot distinction between `PROTO`, `PROTOFORM`, and attested target is stated clearly enough.
3. Whether the current paradigm-probe output shape is the right one to embed directly in generated Markdown.
4. Which additional stem classes should be added next to `oe_paradigm_probe.py`.
5. Whether `reek` should remain the preferred reconstructed-WS pilot, or whether `strew` would better represent the dialect-smoothing dossier class.
