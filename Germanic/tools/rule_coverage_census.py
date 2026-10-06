#!/usr/bin/env python3
"""Machine-readable corpus-coverage census for the historical sound changes.

SCOPE (explicit design decision, 2026 pass 3): the census covers the
historical sound changes of the NUMBERED SC cascade (cascade_position 1-95
in the executable model) — registry rows with entry_type
historical_sound_change whose fst_identifier is a numbered stage. Historical
executable stages OUTSIDE the numbered span (e.g. SC002 PGmcGmSimplification
in the pre-cascade consonant prelude) are deliberately out of scope; this
matches the corpus-maturation pass-01 audit domain and the
cascade_position-keyed schema. A guard test pins this scope.

Executable identity comes from the registry (sc_registry.tsv sc_id ->
fst_identifier); the inventory view's rule_source_anchor is documentation
only. Membership and position come from oe_pipeline. For every rule in
scope the census records:

  * corpus_firing_count — how many selected corpus derivations the rule
    changes, read from the STAGE FIRING SUMMARY of the committed full trace
    report (docs/debug_snapshots/oe_full_trace_report.txt);
  * lexical_witnesses — the corpus lexemes it fires on;
  * coverage_status — one of:
        witnessed                   fires on at least one selected corpus row
        synthetic_only              historically genuine; zero corpus firings;
                                    validated by synthetic unit controls only
        historically_obscured       genuine but its corpus effect is masked by
                                    later developments (explicit override)
        disputed_or_research_issue  witnessing evidence is itself under
                                    adjudication (explicit override)

The project invariant is NOT "every rule fires": it is that every in-scope
historical rule's corpus-coverage status is explicit and understood
(corpus-maturation pass 01). Regenerate with:

    python3 Germanic/tools/rule_coverage_census.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import layout  # noqa: E402
from oe_full_trace_report import trace_provenance_problems  # noqa: E402

GERMANIC = layout().germanic_dir
FULL_TRACE = GERMANIC / "docs" / "debug_snapshots" / "oe_full_trace_report.txt"
INVENTORY = GERMANIC / "docs" / "sound_changes" / "sound_change_inventory.tsv"
SC_REGISTRY = (GERMANIC / "docs" / "sound_changes" / "registry"
               / "sc_registry.tsv")
OUTPUT = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
          / "rule_coverage_census.tsv")

# Zero-firing statuses that require adjudication rather than the
# synthetic_only default. Every entry must cite its adjudication.
STATUS_OVERRIDES: dict[str, tuple[str, str]] = {
    "SC021": (
        "disputed_or_research_issue",
        "Candidate witness galgu (Ruthwell Cross) examined and declined: "
        "R&T 2014 pp.62-63, 164 (Bammesberger 1990: 169 analogical "
        "alternative); corpus-maturation-01 adjudication §4.",
    ),
}


def load_firing_summary(text: str) -> dict[str, tuple[int, list[str]]]:
    marker = "=== STAGE FIRING SUMMARY ==="
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit("full trace report has no STAGE FIRING SUMMARY; "
                         "regenerate with tools/oe_full_trace_report.py --all")
    summary: dict[str, tuple[int, list[str]]] = {}
    current: str | None = None
    for line in text[idx + len(marker):].splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*): (\d+)$", line)
        if m:
            current = m.group(1)
            summary[current] = (int(m.group(2)), [])
            continue
        if current and " :: " in line:
            count, lexemes = summary[current]
            for chunk in line.split(", "):
                lex, _, _form = chunk.partition(" :: ")
                lexemes.append(lex.strip())
            summary[current] = (count, lexemes)
    return summary


def read_tsv(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def build_rows() -> list[dict[str, str]]:
    trace_text = FULL_TRACE.read_text(encoding="utf-8")
    # Fail closed: the committed full trace is upstream runtime evidence and
    # must be fresh (canonical provenance, hashes matching the live sources
    # and its own build manifest) before firing counts are projected from it.
    problems = trace_provenance_problems(trace_text)
    if problems:
        for problem in problems:
            print(f"CENSUS REFUSED (stale trace evidence): {problem}",
                  file=sys.stderr)
        raise SystemExit(
            "the committed full trace report is stale or noncanonical; run "
            "the runtime evidence step first (python3 Germanic/tools/"
            "adjudicate.py SCNNN --evidence, which rebuilds bins and "
            "regenerates the canonical trace), then re-run this census")
    firing = load_firing_summary(trace_text)
    # Executable positions come from the shared model (canonical Foma
    # identifiers throughout — the trace report uses the same identifiers,
    # so no alias table exists or is permitted here).
    manifest_pos = {s.foma_identifier: s.cascade_position
                    for s in oe_pipeline.named_stages()
                    if s.cascade_position is not None}
    # Executable identity: sc_id -> fst_identifier from the registry (the
    # ONE identity authority); rule_source_anchor is documentation only.
    registry_ident = {r["sc_id"]: (r.get("fst_identifier") or "").strip()
                      for r in read_tsv(SC_REGISTRY)}
    rows = []
    for inv in read_tsv(INVENTORY):
        if inv.get("entry_type") != "historical_sound_change":
            continue
        sc = inv["change_id"]
        foma = registry_ident.get(sc, "")
        if not foma:
            continue  # no executable identity in the registry
        if foma not in manifest_pos:
            continue  # explicit scope: numbered cascade only (see docstring)
        count, lexemes = firing.get(foma, (0, []))
        if count > 0:
            status, note = "witnessed", ""
        else:
            status, note = STATUS_OVERRIDES.get(
                sc, ("synthetic_only",
                     "Zero corpus firings; validated by synthetic unit "
                     "controls and the handbook sources."))
        rows.append({
            "sc_id": sc,
            "foma_identifier": foma,
            "cascade_position": str(manifest_pos[foma]),
            "corpus_firing_count": str(count),
            "lexical_witnesses": ", ".join(dict.fromkeys(lexemes)),
            "coverage_status": status,
            "note": note,
        })
    rows.sort(key=lambda r: int(r["cascade_position"]))
    return rows


HEADER = ["sc_id", "foma_identifier", "cascade_position",
          "corpus_firing_count", "lexical_witnesses", "coverage_status",
          "note"]

PREAMBLE = """\
# rule_coverage_census.tsv
# Machine-readable corpus-coverage census for the historical sound changes
# of the NUMBERED SC cascade (cascade_position 1-95); pre-cascade historical
# stages (e.g. SC002 PGmcGmSimplification) are deliberately out of scope.
# Executable identity comes from registry/sc_registry.tsv fst_identifier.
# Generated by Germanic/tools/rule_coverage_census.py from the committed full
# trace report; regenerate after any corpus or cascade change.
# Invariant: every in-scope historical rule's coverage status is explicit and
# understood. "Every rule must fire" is deliberately NOT an invariant.
"""


def census_text() -> str:
    """Render the census to text (fails closed on stale trace evidence)."""
    rows = build_rows()
    lines = [PREAMBLE + "\t".join(HEADER)]
    for r in rows:
        lines.append("\t".join(r[h] for h in HEADER))
    return "\n".join(lines) + "\n"


def main() -> None:
    text = census_text()
    OUTPUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUTPUT} ({len(text.splitlines()) - PREAMBLE.count(chr(10)) - 1} rules)")


if __name__ == "__main__":
    main()
