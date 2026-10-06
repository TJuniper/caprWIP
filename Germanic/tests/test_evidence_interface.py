"""Regressions for the hardened adjudication evidence interface.

These pin the defects observed in the failed cheap-model SC024 attempt:
- the old generic docs/AGENTS.md workflow (Step 0-4 choreography, command
  tiers, per-message response format) must not be an active instruction
  source;
- `--prepare` must not invite manual foma/flookup/bin archaeology;
- `oe_full_trace_report.py` defaults must resolve in both the host and the
  container layout (never /usr/backend/...);
- `--evidence` must rebuild from `old_english_sandbox.txt`, use the one
  canonical bin location, and reject stale or degenerate stage bins;
- the SC024 evidence packet must be obtainable from the documented project
  environment with the single documented command.
"""

import contextlib
import importlib.util
import io
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
AGENTS = REPO_ROOT / "docs/AGENTS.md"
LEGACY = REPO_ROOT / "docs/archive/legacy-agent-workflow.md"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault(name, mod)
    spec.loader.exec_module(mod)
    return mod


adjudicate = _load("adjudicate")
trace_report = _load("oe_full_trace_report")
sc_evidence = _load("sc_evidence")


class AgentsRoutingTests(unittest.TestCase):
    """The old mandatory generic workflow is no longer auto-discoverable."""

    def test_agents_md_is_a_short_routing_rule(self):
        text = AGENTS.read_text(encoding="utf-8")
        self.assertLess(len(text), 4000, "docs/AGENTS.md must stay a short routing rule")
        self.assertIn("adjudicate.py", text)
        self.assertIn("authorization", text)
        for forbidden in ("Tier 3", "Tier 1", "STEP 0", "Step 0",
                          "Response format", "Hypothesis (1 sentence",
                          "three probe", "3 probe"):
            self.assertNotIn(forbidden, text,
                             f"legacy choreography {forbidden!r} resurfaced in docs/AGENTS.md")

    def test_legacy_workflow_is_archived_and_marked(self):
        self.assertTrue(LEGACY.is_file())
        text = LEGACY.read_text(encoding="utf-8")
        self.assertIn("ARCHIVED", text)
        self.assertIn("Tier 3", text)  # historical content preserved

    def test_no_active_doc_defers_to_legacy_tiers(self):
        for doc in (REPO_ROOT / ".github/copilot-instructions.md",
                    REPO_ROOT / "Germanic/docs/CURRENT_STATE.md",
                    REPO_ROOT / "Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md"):
            text = doc.read_text(encoding="utf-8")
            self.assertNotIn("Tier-3", text, f"{doc} still cites legacy approval tiers")
            self.assertNotIn("Tier 3", text, f"{doc} still cites legacy approval tiers")


class PrepareSurfaceTests(unittest.TestCase):
    """--prepare gives no low-level environment-archaeology commands."""

    def _prepare_output(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
            rc = adjudicate.prepare("SC024")
        self.assertEqual(rc, 0)
        return buf.getvalue()

    def test_prepare_has_no_manual_probe_commands(self):
        out = self._prepare_output()
        for forbidden in ("foma", "flookup", "oe_full_trace_report",
                          "docker compose exec"):
            self.assertNotIn(forbidden, out,
                             f"--prepare re-exposes low-level command {forbidden!r}")

    def test_prepare_points_at_evidence_and_finalize(self):
        out = self._prepare_output()
        self.assertIn("--evidence", out)
        self.assertIn("--finalize", out)


class TraceReportPathTests(unittest.TestCase):
    """Default paths resolve in the current layout (no /usr/backend ghosts)."""

    def test_defaults_resolve_to_existing_files(self):
        defaults = trace_report.default_paths()
        self.assertTrue(defaults["tsv"].is_file(), defaults["tsv"])
        self.assertTrue(defaults["fsts_dir"].is_dir(), defaults["fsts_dir"])
        self.assertTrue(defaults["bin_dir"].is_dir(), defaults["bin_dir"])
        # The compiled bin is an untracked runtime artifact (built by
        # `adjudicate --evidence`); require it only when a local runtime
        # build exists, so a clean CI checkout still validates the layout.
        if any(defaults["bin_dir"].glob("*.bin")):
            self.assertTrue(defaults["bin"].is_file(), defaults["bin"])

    def test_default_bin_dir_is_never_the_fsts_source_dir(self):
        defaults = trace_report.default_paths()
        self.assertNotEqual(defaults["bin_dir"].name, "fsts",
                            "fsts/ holds stale duplicate bins; never authoritative")


class EvidenceCommandTests(unittest.TestCase):
    """--evidence is deterministic: sandbox rebuild, canonical bins, explicit paths."""

    def test_cli_accepts_evidence_mode(self):
        doc = adjudicate.__doc__
        self.assertIn("--evidence", doc)
        self.assertTrue(callable(adjudicate.evidence))

    def test_rebuild_compiles_the_sandbox_via_the_shared_runner(self):
        # the stage-bin rebuild lives in the ONE artifact graph, and
        # --evidence forces that runtime node through the shared runner
        import artifact_graph
        graph_src = (Path(artifact_graph.__file__)).read_text(encoding="utf-8")
        self.assertIn('run_in_runner("foma -q -l fsts/old_english_sandbox.txt '
                      '-e quit"', graph_src)
        self.assertIn("write_build_manifest", graph_src)
        src = (Path(adjudicate.__file__)).read_text(encoding="utf-8")
        self.assertIn('force=frozenset({"runtime_bins"})', src)

    def test_runner_wraps_commands_for_the_canonical_container(self):
        from capr_runtime import container_command
        cmd = container_command("cd /usr/app && foma -q")
        self.assertEqual(cmd[:6],
                         ["docker", "compose", "exec", "-T", "backend", "sh"])
        self.assertIn("cd /usr/app && foma -q", cmd)

    def test_sandbox_source_rebuilds_the_full_cascade_too(self):
        lines = adjudicate.SANDBOX_FST.read_text(encoding="utf-8").splitlines()
        first_code = next(l for l in lines if l.strip() and not l.startswith("#"))
        self.assertEqual(first_code.strip(), "source fsts/germanic.txt")

    def test_census_uses_canonical_worker_and_min_mtime(self):
        src = (Path(adjudicate.__file__)).read_text(encoding="utf-8")
        self.assertIn("tools/sc_evidence.py", src)
        self.assertIn("--min-mtime", src)
        self.assertNotIn("/usr/backend", src)
        self.assertNotIn("fsts/old_english_sandbox_after", src)


class ScEvidenceWorkerTests(unittest.TestCase):
    """Container-side worker: stage lookup and fail-closed bin validation."""

    def test_registry_identifier_resolves_to_sandbox_stage(self):
        index, name, bin_name = sc_evidence.find_stage("PNWGmcLongELowering")
        self.assertGreater(index, 0)
        self.assertEqual(bin_name,
                         "old_english_sandbox_after_pnwgmc_long_e_lowering.bin")

    def test_canonical_rhotacism_identifier_resolves(self):
        # Canonical Foma identifier resolves directly; no alias table exists.
        index, name, bin_name = sc_evidence.find_stage("EAFRhotacism")
        self.assertEqual(name, "EAFRhotacism")
        self.assertEqual(bin_name, "old_english_sandbox_after_eaf_rhotacism.bin")

    def test_unknown_identifier_fails_loudly(self):
        with self.assertRaises(KeyError):
            sc_evidence.find_stage("NoSuchRule")

    def test_every_registry_fst_identifier_resolves_to_a_stage(self):
        """No registry rule can silently lack census coverage."""
        views = _load("generate_registry_views")
        for row in views.read_tsv(views.SC_REGISTRY):
            ident = row["fst_identifier"]
            if not ident or row["lifecycle_status"] != "active":
                continue
            sc_evidence.find_stage(ident)  # must not raise

    def test_missing_bin_is_fatal(self):
        with self.assertRaises(SystemExit):
            sc_evidence.validate_bin(Path("/nonexistent/x.bin"), None)

    def test_degenerate_tiny_bin_is_fatal(self):
        with tempfile.NamedTemporaryFile(suffix=".bin") as tmp:
            tmp.write(b"x" * 101)
            tmp.flush()
            with self.assertRaises(SystemExit) as ctx:
                sc_evidence.validate_bin(Path(tmp.name), None)
            self.assertIn("degenerate", str(ctx.exception))

    def test_stale_bin_predating_rebuild_is_fatal(self):
        with tempfile.NamedTemporaryFile(suffix=".bin") as tmp:
            tmp.write(b"x" * 4096)
            tmp.flush()
            old = time.time() - 3600
            os.utime(tmp.name, (old, old))
            with self.assertRaises(SystemExit) as ctx:
                sc_evidence.validate_bin(Path(tmp.name), time.time())
            self.assertIn("stale", str(ctx.exception))

    def test_fresh_bin_passes(self):
        with tempfile.NamedTemporaryFile(suffix=".bin") as tmp:
            tmp.write(b"x" * 4096)
            tmp.flush()
            size, _ = sc_evidence.validate_bin(Path(tmp.name), time.time() - 5)
            self.assertEqual(size, 4096)


def _docker_available():
    try:
        return subprocess.run(
            ["docker", "compose", "exec", "-T", "backend", "true"],
            cwd=REPO_ROOT, capture_output=True, timeout=20,
        ).returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


@unittest.skipUnless(_docker_available(),
                     "backend container not running (docker compose up -d)")
class EvidenceIntegrationTests(unittest.TestCase):
    """The documented command works end-to-end from the project environment.

    This is the regression for the failed SC024 attempt: one command, no
    path debugging, census from freshly rebuilt sandbox stage bins.
    """

    @classmethod
    def setUpClass(cls):
        proc = subprocess.run(
            [sys.executable, str(TOOLS / "adjudicate.py"), "SC024", "--evidence"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=1800,
        )
        cls.proc = proc

    def test_runs_cleanly(self):
        self.assertEqual(self.proc.returncode, 0,
                         f"stdout:\n{self.proc.stdout}\nstderr:\n{self.proc.stderr}")

    def test_reports_freshness_of_current_sources(self):
        self.assertIn("=== FRESHNESS ===", self.proc.stdout)
        self.assertIn("germanic.txt sha256:", self.proc.stdout)
        self.assertIn("old_english_sandbox.txt sha256:", self.proc.stdout)

    def test_census_uses_the_rebuilt_sandbox_stage_bins(self):
        out = self.proc.stdout
        self.assertIn("old_english_sandbox_after_pnwgmc_long_e_lowering.bin", out)
        self.assertIn("LIVE FIRING CENSUS", out)
        # the stale 101-byte fsts/ duplicates must never satisfy the census
        self.assertNotIn("EVIDENCE FAILED", out + self.proc.stderr)

    def test_census_contains_the_chronology_witnesses(self):
        out = self.proc.stdout
        for witness in ("sheep", "year"):
            self.assertIn(witness, out)
        self.assertIn("CHRONOLOGY WITNESS PRE/POST", out)


if __name__ == "__main__":
    unittest.main()
