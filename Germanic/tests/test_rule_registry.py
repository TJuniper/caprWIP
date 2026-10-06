#!/usr/bin/env python3
"""Coverage and coherence invariants for the authoritative rule registry.

Phase 2 of the historical-cascade-order project. These host-runnable tests bind
three artifacts together so no presentation layer can invent its own stage
boundaries and no executable rule can drift out of the registry:

* ``sound_change_inventory.tsv`` — per-rule inventory (real Foma anchors);
* ``sound_change_historical_staging_map.tsv`` — reader-facing SC-level registry;
* ``cascade_baseline/cascade_order_manifest.tsv`` — the actual executable order.

Run: cd Germanic/tests && python3 -m unittest test_rule_registry
"""
from __future__ import annotations

import csv
import importlib.util
import io
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"

_DEFINE_RE = re.compile(r"define\s+([A-Za-z][A-Za-z0-9_]*)")

# Every documented reader-facing SC's principal Foma rule is now composed
# inside the EnglishProtoToOE pipeline manifest. SC003 rhotacism, formerly in
# EarlyGermanicConsonantPipeline, was moved after MonosyllabicFinalZLoss (2026
# rhotacism-position correction: R/T vol.2 p.87; Crist 2002 §6), so no rule is
# expected to be absent from the manifest.
STAGING_RULES_OUTSIDE_PIPELINE: dict[str, str] = {}


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def _read_tsv_skip_comments(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


class InventoryFomaMappingTests(unittest.TestCase):
    def setUp(self):
        lines = [ln for ln in INVENTORY.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
        self.inv = list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))

    def test_every_inventory_row_has_a_foma_define(self):
        for row in self.inv:
            anchor = row.get("rule_source_anchor") or ""
            self.assertRegex(anchor, _DEFINE_RE,
                             f"{row.get('change_id')}: rule_source_anchor has no 'define <Ident>'")

    def test_foma_identifiers_are_unique_per_change(self):
        foma_to_changes: dict[str, list[str]] = {}
        for row in self.inv:
            m = _DEFINE_RE.search(row.get("rule_source_anchor") or "")
            if m:
                foma_to_changes.setdefault(m.group(1), []).append(row["change_id"])
        dups = {f: cs for f, cs in foma_to_changes.items() if len(cs) > 1}
        self.assertEqual(dups, {}, f"Foma identifiers mapped by >1 inventory row: {dups}")


class ManifestRegistryCoverageTests(unittest.TestCase):
    def setUp(self):
        with ORDER_MANIFEST.open(encoding="utf-8") as handle:
            self.manifest = list(csv.DictReader(handle, delimiter="\t"))
        inv_lines = [ln for ln in INVENTORY.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
        inv = list(csv.DictReader(io.StringIO("\n".join(inv_lines)), delimiter="\t"))
        self.inv_foma = {}
        for row in inv:
            m = _DEFINE_RE.search(row.get("rule_source_anchor") or "")
            if m:
                self.inv_foma[m.group(1)] = row["change_id"]

    def test_every_executable_rule_has_exactly_one_registry_row(self):
        """Every named rule in the executable order maps to an inventory row."""
        missing = [r["foma_identifier"] for r in self.manifest
                   if r["foma_identifier"] not in self.inv_foma]
        self.assertEqual(missing, [],
                         f"executable rules absent from the inventory registry: {missing}")

    def test_no_anonymous_inline_fragments_in_manifest(self):
        inline = [r for r in self.manifest if r["foma_identifier"].startswith("<inline:")]
        self.assertEqual(inline, [], "manifest should contain only named rules")


class StagingMapIdentityTests(unittest.TestCase):
    """The staging map is a generated view; its executable identity must come
    from the registry (sc_registry.tsv fst_identifier), never from
    rule_source_anchor. (Replaces the retired anchor-based repair tool.)"""

    def setUp(self):
        self.staging = _read_tsv_skip_comments(STAGING_MAP)
        registry = _read_tsv_skip_comments(
            SC_DIR / "registry" / "sc_registry.tsv")
        self.registry_ident = {r["sc_id"]: (r.get("fst_identifier") or "").strip()
                               for r in registry}

    def test_fst_identifier_column_is_not_the_sc_label(self):
        """fst_identifier must hold the real Foma identifier, never the SC label."""
        offenders = [r["sc_id"] for r in self.staging if r["fst_identifier"] == r["sc_id"]]
        self.assertEqual(offenders, [],
                         f"fst_identifier still equals the SC label for: {offenders}")

    def test_fst_identifier_matches_registry(self):
        for r in self.staging:
            self.assertIn(r["sc_id"], self.registry_ident,
                          f"{r['sc_id']} missing from the registry")
            self.assertEqual(r["fst_identifier"], self.registry_ident[r["sc_id"]],
                             f"{r['sc_id']}: staging Foma id disagrees with registry")

    def test_staging_foma_identifiers_are_unique(self):
        foma = [r["fst_identifier"] for r in self.staging]
        dups = {f for f in foma if foma.count(f) > 1}
        self.assertEqual(dups, set(), f"duplicate principal Foma rules in staging map: {dups}")


class StagingPipelineCrossCheckTests(unittest.TestCase):
    def setUp(self):
        self.staging = _read_tsv_skip_comments(STAGING_MAP)
        with ORDER_MANIFEST.open(encoding="utf-8") as handle:
            self.manifest_ids = {r["foma_identifier"] for r in csv.DictReader(handle, delimiter="\t")}

    def test_staging_rules_are_in_pipeline_except_documented(self):
        """Every staging Foma rule appears in the executable pipeline, except the
        explicitly documented rules that are composed elsewhere (SC003)."""
        outside = {r["sc_id"]: r["fst_identifier"] for r in self.staging
                   if r["fst_identifier"] not in self.manifest_ids}
        self.assertEqual(outside, STAGING_RULES_OUTSIDE_PIPELINE,
                         "unexpected staging rules absent from the pipeline manifest; "
                         "if intentional, document them in STAGING_RULES_OUTSIDE_PIPELINE")


if __name__ == "__main__":
    unittest.main()
