#!/usr/bin/env python3
"""Shared runtime-layout and runner abstraction for the Germanic tools.

One logical layout, two environment views (docker-compose bind mounts):

    logical resource            host view                  container view
    ------------------------    -----------------------    --------------
    repo root                   <repo>/                    (not mounted)
    Germanic source root        <repo>/Germanic/           /usr/app/
    FST sources                 <repo>/Germanic/fsts/      /usr/app/fsts/
    corpus data                 <repo>/Germanic/data/      /usr/app/data/
    docs                        <repo>/Germanic/docs/      /usr/app/docs/
    tools                       <repo>/Germanic/tools/     /usr/app/tools/
    runtime bin directory       <repo>/backend/            /usr/app/

The runtime bin directory is the foma working directory: the ONE
authoritative location for compiled ``.bin`` artifacts and for the build
manifest (``oe_build_manifest.json``).  Bins under ``Germanic/fsts/`` are
never authoritative.

Every Python tool should obtain paths from :func:`layout` instead of
reconstructing ``Path(__file__).parents[...] / "backend"`` (or other
stale pre-2026 container layouts) independently.

Foma-dependent work goes through an explicit runner:

* ``docker`` — run inside the backend container (default on the host);
* ``local`` — run foma directly (default inside the container, or on a
  host with foma when explicitly requested via ``--runner local`` or
  ``CAPR_RUNNER=local``).

Both runners consume the same logical pipeline model and source files.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

MIN_BIN_BYTES = 1024  # anything smaller is a degenerate/failed build
BUILD_MANIFEST_NAME = "oe_build_manifest.json"


@dataclass(frozen=True)
class RuntimeLayout:
    """Resolved logical resources for the current environment."""

    germanic_dir: Path      # Germanic source root (== /usr/app in container)
    repo_root: Path         # repo root on the host; == germanic_dir in container
    bin_dir: Path           # authoritative runtime bin directory
    is_container: bool

    @property
    def fsts_dir(self) -> Path:
        return self.germanic_dir / "fsts"

    @property
    def data_dir(self) -> Path:
        return self.germanic_dir / "data"

    @property
    def docs_dir(self) -> Path:
        return self.germanic_dir / "docs"

    @property
    def tools_dir(self) -> Path:
        return self.germanic_dir / "tools"

    @property
    def corpus_tsv(self) -> Path:
        return self.data_dir / "germanic-aligned-final.tsv"

    @property
    def germanic_fst(self) -> Path:
        return self.fsts_dir / "germanic.txt"

    @property
    def sandbox_fst(self) -> Path:
        return self.fsts_dir / "old_english_sandbox.txt"

    @property
    def build_manifest(self) -> Path:
        return self.bin_dir / BUILD_MANIFEST_NAME


def layout() -> RuntimeLayout:
    """Resolve the runtime layout for the current environment.

    Container detection: docker-compose mounts the backend code at
    /usr/app, so the Germanic dir and the backend code share a directory
    exactly when we are inside the container.
    """
    tools_dir = Path(__file__).resolve().parent
    germanic_dir = tools_dir.parent
    is_container = (germanic_dir / "compare_fst.py").is_file()
    if is_container:
        return RuntimeLayout(
            germanic_dir=germanic_dir,
            repo_root=germanic_dir,
            bin_dir=germanic_dir,
            is_container=True,
        )
    repo_root = germanic_dir.parent
    return RuntimeLayout(
        germanic_dir=germanic_dir,
        repo_root=repo_root,
        bin_dir=repo_root / "backend",
        is_container=False,
    )


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


# ---------------------------------------------------------------------------
# Runner abstraction
# ---------------------------------------------------------------------------

def default_runner(rt: RuntimeLayout | None = None) -> str:
    rt = rt or layout()
    return "local" if rt.is_container else "docker"


def container_command(inner: str) -> list[str]:
    """Wrap a shell command for the backend container (canonical layout)."""
    return ["docker", "compose", "exec", "-T", "backend", "sh", "-lc", inner]


def run_in_runner(inner: str, runner: str | None = None,
                  rt: RuntimeLayout | None = None,
                  **kwargs) -> subprocess.CompletedProcess:
    """Run a shell command in the runtime bin directory via the runner.

    ``inner`` is a shell command that assumes CWD is the runtime bin
    directory (/usr/app in the container).  With the ``docker`` runner it
    is executed inside the backend container; with the ``local`` runner it
    is executed directly with CWD = the resolved bin directory.
    """
    rt = rt or layout()
    runner = runner or default_runner(rt)
    if runner == "docker":
        if rt.is_container:
            raise RuntimeError("docker runner requested from inside the container")
        return subprocess.run(container_command(f"cd /usr/app && {inner}"),
                              cwd=rt.repo_root, **kwargs)
    if runner == "local":
        if not rt.is_container and shutil.which("foma") is None:
            raise RuntimeError(
                "local runner requested but foma is not on PATH; use the "
                "docker runner (default) instead")
        return subprocess.run(["sh", "-lc", inner], cwd=rt.bin_dir, **kwargs)
    raise ValueError(f"unknown runner {runner!r} (expected 'docker' or 'local')")


def compile_fst_source(source_rel: str, runner: str | None = None,
                       rt: RuntimeLayout | None = None) -> subprocess.CompletedProcess:
    """Compile one FST source (path relative to the bin dir, e.g. ``fsts/...``).

    Always appends ``-e quit`` — germanic.txt does not terminate on its own.
    """
    return run_in_runner(f"foma -q -l {source_rel} -e quit", runner=runner,
                         rt=rt, capture_output=True, text=True)


def foma_version(runner: str | None = None,
                 rt: RuntimeLayout | None = None) -> str:
    try:
        proc = run_in_runner("foma -v", runner=runner, rt=rt,
                             capture_output=True, text=True, timeout=60)
        return (proc.stdout or proc.stderr).strip().splitlines()[0]
    except Exception:
        return "unknown"


# ---------------------------------------------------------------------------
# Build manifest (explicit freshness contract; replaces mtime folklore)
# ---------------------------------------------------------------------------

def write_build_manifest(expected_bins: list[str],
                         runner: str | None = None,
                         rt: RuntimeLayout | None = None) -> Path:
    """Record what source state generated the current runtime bins.

    Foma compilation is byte-nondeterministic, so bin hashes are NOT part
    of the contract; source hashes are.  Semantic reproducibility is
    separately guaranteed by the corpus output fingerprints.
    """
    rt = rt or layout()
    manifest = {
        "generator": "Germanic/tools/capr_runtime.py write_build_manifest",
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "runner": runner or default_runner(rt),
        "foma_version": foma_version(runner=runner, rt=rt),
        "sources": {
            "germanic.txt": sha256_of(rt.germanic_fst),
            "old_english_sandbox.txt": sha256_of(rt.sandbox_fst),
            "germanic-aligned-final.tsv": sha256_of(rt.corpus_tsv),
        },
        "expected_bins": sorted(expected_bins),
    }
    rt.build_manifest.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    return rt.build_manifest


def check_build_manifest(expected_bins: list[str],
                         rt: RuntimeLayout | None = None) -> list[str]:
    """Return a list of freshness problems (empty == fresh).

    The authoritative check: current source hashes match the manifest, the
    manifest expects exactly the model's bins, and every expected bin
    exists and is nondegenerate.  mtimes are not consulted.
    """
    rt = rt or layout()
    problems: list[str] = []
    if not rt.build_manifest.is_file():
        return [f"missing build manifest {rt.build_manifest} — rebuild the bins "
                "(python3 Germanic/tools/adjudicate.py SCNNN --evidence, or "
                "bash Germanic/tools/rebuild_oe_bins.sh)"]
    manifest = json.loads(rt.build_manifest.read_text(encoding="utf-8"))
    current = {
        "germanic.txt": sha256_of(rt.germanic_fst),
        "old_english_sandbox.txt": sha256_of(rt.sandbox_fst),
        "germanic-aligned-final.tsv": sha256_of(rt.corpus_tsv),
    }
    for name, sha in current.items():
        recorded = manifest.get("sources", {}).get(name)
        if recorded != sha:
            problems.append(f"{name}: source sha256 {sha[:12]}… does not match "
                            f"build manifest ({str(recorded)[:12]}…) — bins are stale")
    recorded_bins = manifest.get("expected_bins", [])
    if sorted(expected_bins) != recorded_bins:
        problems.append("expected bin set differs from the build manifest — "
                        "the executable model changed since the last build")
    for bin_name in expected_bins:
        path = rt.bin_dir / bin_name
        if not path.is_file():
            problems.append(f"missing bin: {path}")
        elif path.stat().st_size < MIN_BIN_BYTES:
            problems.append(f"degenerate bin ({path.stat().st_size} bytes): {path}")
    return problems
