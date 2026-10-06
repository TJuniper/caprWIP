"""Machine-checkable guardrails for the Germanic adjudication protocol.

These tests enforce generic invariants distilled from the SC021-SC023
adjudications (see Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md):

1. the protocol and template documents exist and keep their required
   structure (verdict vocabulary, mandatory sections);
2. historical stage is carried by canonical metadata, never inferred
   from an FST identifier prefix, and identifier-prefix/metadata
   divergence remains explicitly permitted;
3. retired rules stay retired across all live candidate/promotion and
   chronology machinery;
4. chronology edges asserting a real ordering always record witness
   lexemes, forms, and notes ("firing" alone is never evidence);
5. agent instructions point at the protocol and the current-state
   entry point rather than the frozen checkpoint.
"""

import csv
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
DOCS = GERMANIC / "docs"
SC_DOCS = DOCS / "sound_changes"

PROTOCOL = DOCS / "RESEARCH_ADJUDICATION_PROTOCOL.md"
TEMPLATE = SC_DOCS / "audits" / "ADJUDICATION_TEMPLATE.md"
CURRENT_STATE = DOCS / "CURRENT_STATE.md"
CANONICAL_STATE = DOCS / "CANONICAL_STATE.md"
COPILOT_INSTRUCTIONS = REPO_ROOT / ".github" / "copilot-instructions.md"

STAGING_MAP = SC_DOCS / "sound_change_historical_staging_map.tsv"
AUDIT_TABLE = SC_DOCS / "cascade_baseline" / "historical_audit_table.tsv"
RENAME_MANIFEST = SC_DOCS / "cascade_baseline" / "rename_migration_manifest.tsv"
CANDIDATES_ARCHIVED = SC_DOCS / "order_tests" / "next_batch_candidates.tsv"
SC_REGISTRY = SC_DOCS / "registry" / "sc_registry.tsv"
GRAPH_DIR = SC_DOCS / "order_tests" / "chronology_graph"
EDGES = GRAPH_DIR / "first_break_edges.tsv"
NODES = GRAPH_DIR / "first_break_nodes.tsv"

VERDICT_VOCABULARY = (
    "RETAIN",
    "REFORMULATE",
    "RESTRICT",
    "SPLIT",
    "RETIRE",
    "REORDER",
    "DEFER",
)

# FST identifier prefixes and the historical stage each one would naively
# imply. The whole point of the prefix-vs-stage guardrail is that this
# implication is NOT trustworthy; canonical metadata wins.
PREFIX_IMPLIED_STAGE = (
    ("PNWGmc", "pnwgmc"),
    ("NWGmc", "nwgmc"),
    ("PWGmc", "pwgmc"),
    ("PGmc", "pgmc"),
    ("EAF", "eaf"),
    ("OE", "oe"),
)

# Relation types that assert a genuine chronological ordering and
# therefore must carry witness evidence. Boundary/search-exhaustion rows
# (runner_limited_boundary, no_break_search_boundary) and purely
# technical rows are exempt from the lexeme requirement by design.
CHRONOLOGY_RELATION_TYPES = {
    "broad_far_chronology",
    "near_reciprocal_chronology",
    "one_sided_chronology",
    "reciprocal_chronology",
}


def read_tsv(path):
    with open(path, encoding="utf-8") as handle:
        rows = [
            row
            for row in csv.reader(handle, delimiter="\t")
            if row and not row[0].startswith("#")
        ]
    header = rows[0]
    return [dict(zip(header, row)) for row in rows[1:]]


def prefix_stage(identifier):
    for prefix, stage in PREFIX_IMPLIED_STAGE:
        if identifier.startswith(prefix):
            return stage
    return None


class ProtocolDocumentsTests(unittest.TestCase):
    def test_protocol_exists_with_required_content(self):
        self.assertTrue(PROTOCOL.is_file(), f"missing {PROTOCOL}")
        text = PROTOCOL.read_text(encoding="utf-8")
        for verdict in VERDICT_VOCABULARY:
            self.assertIn(verdict, text, f"protocol lost verdict term {verdict}")
        for phrase in (
            "FST identifier",
            "census",
            "counterfeeding",
            "Fingerprints are observations",
        ):
            self.assertIn(phrase, text, f"protocol lost required concept: {phrase}")

    def test_template_exists_with_required_sections(self):
        self.assertTrue(TEMPLATE.is_file(), f"missing {TEMPLATE}")
        text = TEMPLATE.read_text(encoding="utf-8")
        for section in (
            "Executable identifier",
            "Hypothesis",
            "firing census",
            "witness traces",
            "role classification",
            "Sources checked, with page numbers",
            "Historical stage",
            "Historical scope",
            "executable proxy",
            "stage_entailed",
            "Verdict",
            "Affected files/registries",
            "Regression tests",
            "fingerprint effect",
            "Unresolved uncertainty",
        ):
            self.assertIn(section, text, f"template lost required field: {section}")

    def test_entry_points_are_consistent(self):
        self.assertTrue(CURRENT_STATE.is_file(), f"missing {CURRENT_STATE}")
        current = CURRENT_STATE.read_text(encoding="utf-8")
        self.assertIn("RESEARCH_ADJUDICATION_PROTOCOL.md", current)
        self.assertIn("ADJUDICATION_TEMPLATE.md", current)
        canonical = CANONICAL_STATE.read_text(encoding="utf-8")
        self.assertIn("FROZEN HISTORICAL CHECKPOINT", canonical)
        self.assertIn("CURRENT_STATE.md", canonical)

    def test_agent_instructions_require_protocol(self):
        text = COPILOT_INSTRUCTIONS.read_text(encoding="utf-8")
        self.assertIn("RESEARCH_ADJUDICATION_PROTOCOL.md", text)
        self.assertIn("CURRENT_STATE.md", text)


class PrefixVersusStageTests(unittest.TestCase):
    def setUp(self):
        self.staging = read_tsv(STAGING_MAP)

    def test_metadata_stage_is_authoritative_not_prefix(self):
        """Prefix/metadata divergence must remain possible and preserved.

        If this test starts failing because the divergent set is empty,
        someone has probably 'corrected' canonical metadata to match FST
        identifier prefixes. That is exactly the error the protocol
        forbids: identifiers are stability handles, not stage claims.
        """
        divergent = set()
        for row in self.staging:
            implied = prefix_stage(row.get("fst_identifier", ""))
            stage = row.get("hist_stage", "")
            if implied and stage and implied != stage:
                divergent.add(row["sc_id"])
        self.assertTrue(
            divergent,
            "no prefix/metadata divergence left in the staging map; "
            "stage has likely been re-inferred from identifier prefixes",
        )
        # Known settled divergences from the SC022/SC023 adjudications.
        for sc_id in ("SC022", "SC023"):
            self.assertIn(
                sc_id,
                divergent,
                f"{sc_id} must keep its PNWGmc identifier with a non-pnwgmc "
                "canonical stage (adjudicated verdict)",
            )

    def test_frozen_audit_archives_are_archival_not_current(self):
        """The audit table and rename manifest are ARCHIVE/FROZEN snapshots.

        They must exist, carry the frozen-archive banner, and stay readable,
        but they are NOT required to agree with the current staging map:
        a future legitimate stage correction updates the registry (and its
        generated views) without rewriting the frozen archives. Current
        authority is the registry/model, never these files.
        """
        for path in (AUDIT_TABLE, RENAME_MANIFEST):
            self.assertTrue(path.exists(), path)
            head = "\n".join(
                line for line in
                path.read_text(encoding="utf-8").splitlines()[:15]
                if line.startswith("#"))
            self.assertIn("ARCHIVE", head, f"{path.name}: missing frozen-archive banner")
        audit = {r["sc_id"]: r for r in read_tsv(AUDIT_TABLE)}
        rename = {r["sc_id"]: r for r in read_tsv(RENAME_MANIFEST)}
        self.assertTrue(audit, "archive audit table unreadable/empty")
        self.assertTrue(rename, "archive rename manifest unreadable/empty")
        for row in audit.values():
            self.assertIn("proposed_hist_stage", row)
        for row in rename.values():
            self.assertIn("canonical_hist_stage", row)


class RetiredRuleGuardTests(unittest.TestCase):
    def retired_ids(self):
        return {
            row["sc_id"]
            for row in read_tsv(SC_REGISTRY)
            if row.get("lifecycle_status") == "retired"
        }

    def test_retirements_exist_and_include_sc021(self):
        retired = self.retired_ids()
        self.assertIn("SC021", retired)
        # The audit-table layer must agree with the registry on retirement.
        audit_retired = {
            row["sc_id"]
            for row in read_tsv(AUDIT_TABLE)
            if row.get("required_action") == "retired"
        }
        self.assertLessEqual(audit_retired, retired)

    def test_retired_rules_stay_out_of_live_machinery(self):
        retired = self.retired_ids()
        rename = {r["sc_id"]: r for r in read_tsv(RENAME_MANIFEST)}
        nodes = {r["change_id"]: r for r in read_tsv(NODES)}
        staging_ids = {r["sc_id"] for r in read_tsv(STAGING_MAP)}
        self.assertFalse(
            CANDIDATES_ARCHIVED.exists(),
            "next_batch_candidates.tsv has been resurrected in the live "
            "order_tests namespace; the candidate board is archived and the "
            "registry owns candidate/lifecycle status",
        )
        for sc_id in sorted(retired):
            self.assertNotIn(
                sc_id,
                staging_ids,
                f"{sc_id} is retired but still has an active staging-map row",
            )
            if sc_id in rename:
                self.assertEqual(rename[sc_id]["migration_status"], "retired", sc_id)
            if sc_id in nodes:
                self.assertEqual(nodes[sc_id]["lifecycle_status"], "retired", sc_id)

    def test_retired_rules_not_active_chronology_edges(self):
        retired = self.retired_ids()
        for row in read_tsv(EDGES):
            if row["relation_type"] in CHRONOLOGY_RELATION_TYPES:
                for endpoint in (row["source_change_id"], row["target_change_id"]):
                    self.assertNotIn(
                        endpoint,
                        retired,
                        f"retired rule {endpoint} still carries a live "
                        f"chronology edge {row['source_change_id']}->"
                        f"{row['target_change_id']}",
                    )


class ChronologyEdgeWitnessDisciplineTests(unittest.TestCase):
    def test_chronology_edges_record_witnesses(self):
        """An edge asserting real ordering must name its evidence.

        This blocks the failure mode where "this lexeme changes in the
        interaction harness" silently becomes a chronology claim with no
        recorded witness or interpretation.
        """
        for row in read_tsv(EDGES):
            if row["relation_type"] not in CHRONOLOGY_RELATION_TYPES:
                continue
            label = f"{row['source_change_id']}->{row['target_change_id']}"
            self.assertTrue(
                row["representative_lexemes"].strip(),
                f"{label}: chronology edge without witness lexemes",
            )
            self.assertTrue(
                row["representative_forms"].strip(),
                f"{label}: chronology edge without witness forms",
            )
            self.assertTrue(
                row["notes"].strip(),
                f"{label}: chronology edge without interpretive notes",
            )


if __name__ == "__main__":
    unittest.main()
