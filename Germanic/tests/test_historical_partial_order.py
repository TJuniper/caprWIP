#!/usr/bin/env python3
"""Archived Phase-3 structure and current canonical interaction constraints.

Host-runnable. Verifies the archived partial-order edges use controlled
vocabularies and are acyclic. Current independently supported interaction
edges come from the canonical registry, not the old proxy snapshot.
Since the 2026 rhotacism
move (EAFRhotacism composed after MonosyllabicFinalZLoss inside
EnglishProtoToOE) the executable cascade honours every evidence-backed
historical constraint by genuine ordering: no edge may rely on context-scoping
in lieu of cascade position, and no edge endpoint may escape the check by
sitting outside the position manifest.

Run: cd Germanic/tests && python3 -m unittest test_historical_partial_order
"""
from __future__ import annotations

import collections
import csv
import io
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
PARTIAL_ORDER = SC_DIR / "cascade_baseline/historical_partial_order.tsv"
CURRENT_EDGES = SC_DIR / "registry/chronology_edges.tsv"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"

TYPE_VALUES = {"historical_stage", "historical_relative_chronology",
               "fst_dependency", "technical_dependency"}
CONFIDENCE_VALUES = {"A", "B", "C"}
_DEFINE_RE = re.compile(r"define\s+([A-Za-z][A-Za-z0-9_]*)")
_SCOPING_NOTE = "not a cascade constraint"


def _load_edges() -> list[dict[str, str]]:
    lines = [ln for ln in PARTIAL_ORDER.read_text(encoding="utf-8").splitlines()
             if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


def _sc_to_position() -> dict[str, int]:
    inv_lines = [ln for ln in INVENTORY.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    sc2foma = {}
    for r in csv.DictReader(io.StringIO("\n".join(inv_lines)), delimiter="\t"):
        m = _DEFINE_RE.search(r.get("rule_source_anchor", "") or "")
        if m:
            sc2foma[r["change_id"]] = m.group(1)
    with ORDER_MANIFEST.open(encoding="utf-8") as handle:
        pos = {r["foma_identifier"]: int(r["position"]) for r in csv.DictReader(handle, delimiter="\t")}
    # Rules not composed inside EnglishProtoToOE are absent from the manifest
    # and map to position 0. Edge endpoints must NOT be position 0: see
    # test_edge_endpoints_have_manifest_positions.
    return {sc: pos.get(foma, 0) for sc, foma in sc2foma.items()}


class PartialOrderTests(unittest.TestCase):
    def setUp(self):
        self.edges = _load_edges()
        self.pos = _sc_to_position()

    def test_controlled_vocabularies(self):
        for e in self.edges:
            self.assertIn(e["type_of_edge"], TYPE_VALUES, f"bad type: {e}")
            self.assertIn(e["confidence"], CONFIDENCE_VALUES, f"bad confidence: {e}")

    def test_edges_reference_known_rules(self):
        for e in self.edges:
            self.assertIn(e["earlier_sc"], self.pos, f"unknown earlier_sc {e['earlier_sc']}")
            self.assertIn(e["later_sc"], self.pos, f"unknown later_sc {e['later_sc']}")

    def test_edge_endpoints_have_manifest_positions(self):
        """No edge endpoint may sit outside the executable-order manifest.
        A position of 0 would let a relation escape the ordering check."""
        missing = []
        for e in self.edges:
            for key in ("earlier_sc", "later_sc"):
                if self.pos[e[key]] == 0:
                    missing.append((e[key], e["earlier_sc"], e["later_sc"]))
        self.assertEqual(missing, [],
                         f"edge endpoints without a manifest position: {missing}")

    def test_cascade_edges_hold_in_current_order(self):
        """Check current independently supported interactions, not archived
        proxy edges or reciprocal displacement observations."""
        lines = [line for line in CURRENT_EDGES.read_text(encoding="utf-8").splitlines()
                 if not line.startswith("#")]
        current = [edge for edge in csv.DictReader(lines, delimiter="\t")
                   if edge["evidence_basis"] == "independently_demonstrated"
                   and edge["witness_role"] in {
                       "feeding", "bleeding", "counterfeeding_negative",
                       "counterbleeding_negative",
                   }]
        self.assertTrue(current)
        violations = []
        for edge in current:
            earlier, later = edge["source_change_id"], edge["target_change_id"]
            if edge["direction_basis"] == "earlier_boundary":
                earlier, later = later, earlier
            a, b = self.pos[earlier], self.pos[later]
            if not (0 < a < b):
                violations.append((earlier, later, a, b))
        self.assertEqual(violations, [],
                         f"current cascade violates supported historical edges: {violations}")

    def test_cascade_edges_are_acyclic(self):
        adj = collections.defaultdict(list)
        for e in self.edges:
            adj[e["earlier_sc"]].append(e["later_sc"])
        color = collections.defaultdict(int)  # 0 white, 1 gray, 2 black
        cycle = [False]

        def dfs(u):
            color[u] = 1
            for v in adj[u]:
                if color[v] == 1:
                    cycle[0] = True
                elif color[v] == 0:
                    dfs(v)
            color[u] = 2

        for node in list(adj):
            if color[node] == 0:
                dfs(node)
        self.assertFalse(cycle[0], "supported partial order contains a cycle")

    def test_no_scoping_note_edges_remain(self):
        """Since the rhotacism move, every historical relation is implemented
        by genuine cascade ordering. The legacy 'not a cascade constraint'
        scoping escape must not reappear."""
        for e in self.edges:
            self.assertNotIn(_SCOPING_NOTE, e["evidence"],
                             f"edge {e['earlier_sc']}->{e['later_sc']} claims a scoping "
                             "implementation; historical relations must be enforced by "
                             "executable ordering")


if __name__ == "__main__":
    unittest.main()
