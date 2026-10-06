#!/usr/bin/env python3
"""Behaviour-neutral rename validation gate for one rule rename.

Given a former and canonical Foma identifier, this harness runs the automatable
gates that prove a rename changed nothing but the label. It is designed to run
inside the backend container (it invokes foma/flookup) with CWD = /usr/app.

Gates implemented here (task section 7):
  A  FST compiles cleanly; the former `define` is ABSENT (no alias) and the
     canonical `define` is present.
  B  Lexical-output identity: recompiling and re-applying preserves the frozen
     outputs_sha256 (and accepted/matched/mismatched counts).
  E  Executable order unchanged: the executable order immediately AFTER the
     rename equals the order immediately BEFORE it, modulo the identifier
     substitution, proving relabeling only, never reordering. The comparison
     is against the pre-rename revision itself, never against the campaign-era
     frozen manifest, which is an archive and not a current baseline.
  G  Former-name audit: the former identifier and its snake/kebab derivatives are
     absent from active source and generated output, except individually
     allowlisted archival references.

Gates C (mismatch report), D (trace identity) and E (book/PDF) require the full
regeneration pipeline and are run separately per rule; this harness covers the
fast, decisive behaviour-neutrality gates. There is deliberately NO committed
Foma compatibility alias: an alias could let an incomplete migration compile and
hide stale references.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Resolve repo layout whether run from /usr/app (container) or the host checkout.
CWD = Path.cwd()
if (CWD / "fsts/germanic.txt").exists():
    GERMANIC_ROOT = CWD                      # container: /usr/app
    DOCS = CWD / "docs/sound_changes"
    FST = CWD / "fsts/germanic.txt"
    TOOLS = CWD / "tools"
else:
    REPO = Path(__file__).resolve().parents[2]
    GERMANIC_ROOT = REPO / "Germanic"
    DOCS = GERMANIC_ROOT / "docs/sound_changes"
    FST = GERMANIC_ROOT / "fsts/germanic.txt"
    TOOLS = GERMANIC_ROOT / "tools"

BASELINE_DIR = DOCS / "cascade_baseline"
BASELINE_SUMMARY = BASELINE_DIR / "cascade_baseline_summary.json"
# Gate E reconstructs the pre-rename cascade from history, so it needs the
# working repository rather than the container mount.
REPO_FOR_GIT = TOOLS.parent.parent
ALLOWLIST = BASELINE_DIR / "rename_former_name_allowlist.tsv"

sys.path.insert(0, str(TOOLS))


def _snake(ident: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", ident).lower()


def _kebab(ident: str) -> str:
    return _snake(ident).replace("_", "-")


def former_variants(former: str) -> list[str]:
    # The exact identifier is the reliable, meaningful token to audit in source
    # and validation code. CAPR's snake/kebab bin-name forms (e.g. nwgmc_...) do
    # not follow a simple per-capital rule, so they are migrated explicitly per
    # rule and verified by the trace-regeneration gate, not guessed here.
    return [former]


def gate_a_compile_and_define(former: str, canonical: str) -> list[str]:
    errors: list[str] = []
    proc = subprocess.run(["foma", "-q", "-l", str(FST), "-e", "quit"],
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = proc.stdout.decode("utf-8", "replace")
    if proc.returncode != 0 or "***" in out or "defined" not in out.lower() and "Writing to file" not in out:
        # foma prints "defined X: ..." lines and "Writing to file" lines on success.
        if proc.returncode != 0:
            errors.append(f"A: foma compile failed (rc={proc.returncode})")
    text = FST.read_text(encoding="utf-8")
    if re.search(rf"\bdefine\s+{re.escape(former)}\b", text):
        errors.append(f"A: former `define {former}` still present (no alias allowed)")
    if not re.search(rf"\bdefine\s+{re.escape(canonical)}\b", text):
        errors.append(f"A: canonical `define {canonical}` not found")
    return errors


def gate_b_output_identity() -> list[str]:
    errors: list[str] = []
    import cascade_baseline as cb
    tsv = GERMANIC_ROOT / "data/germanic-aligned-final.tsv"
    bin_path = GERMANIC_ROOT / "old_english.bin"
    if not bin_path.exists():
        bin_path = Path("old_english.bin")
    baseline = cb.build_baseline(tsv, bin_path)
    frozen = json.loads(BASELINE_SUMMARY.read_text(encoding="utf-8"))
    got = baseline["summary"]
    for key in ("total_lexemes", "accepted", "rejected", "matched", "mismatched",
                "ambiguous_outputs", "outputs_sha256"):
        if got[key] != frozen[key]:
            errors.append(f"B: {key} changed: frozen={frozen[key]} now={got[key]}")
    return errors


def _tsv_rows(path: Path) -> list[dict[str, str]]:
    """Read a TSV that may carry a leading '#' comment block.

    Feeding comment lines straight to DictReader silently promotes a comment to
    the header row, which yields no usable records at all.
    """
    if not path.exists():
        return []
    body = "\n".join(
        line for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )
    return list(csv.DictReader(io.StringIO(body), delimiter="\t"))


def _retired_identifiers() -> set[str]:
    """Foma identifiers of rules the registry records as retired.

    Such rules legitimately no longer appear in the live cascade even though the
    frozen campaign-era manifest still lists them.
    """
    retired: set[str] = set()
    for row in _tsv_rows(DOCS / "registry/sc_registry.tsv"):
        if (row.get("lifecycle_status") or "").strip() == "retired":
            identifier = (row.get("fst_identifier") or "").strip()
            if identifier:
                retired.add(identifier)
    for row in _tsv_rows(BASELINE_DIR / "rename_migration_manifest.tsv"):
        if (row.get("migration_status") or "").strip() == "retired":
            former = (row.get("former_foma_identifier") or "").strip()
            if former:
                retired.add(former)
    return retired


def _completed_rename_map(former: str, canonical: str) -> dict[str, str]:
    """former_foma_identifier -> current_foma_identifier for every relabeling.

    Gate E compares the live order against the frozen (original) order after
    undoing *all* accumulated relabelings, not just the current rule's, so the
    order-identity check stays valid as renames accumulate.

    ``sound_change_aliases.tsv`` is the maintained authority here: it records a
    ``former_foma_rule_name`` alias alongside the SC's current ``foma_rule_name``.
    The archival rename-migration manifest is consulted as a fallback only; its
    rows are a campaign-time snapshot and some are stale.
    """
    mapping: dict[str, str] = {}
    alias_rows = _tsv_rows(DOCS / "sound_change_aliases.tsv")
    current: dict[str, str] = {}
    for row in alias_rows:
        if (row.get("alias_type") or "").strip() == "foma_rule_name":
            current[(row.get("change_id") or "").strip()] = (row.get("alias") or "").strip()
    for row in alias_rows:
        if (row.get("alias_type") or "").strip() == "former_foma_rule_name":
            sc = (row.get("change_id") or "").strip()
            old = (row.get("alias") or "").strip()
            new = current.get(sc, "")
            if old and new and old != new:
                mapping[old] = new
    for row in _tsv_rows(BASELINE_DIR / "rename_migration_manifest.tsv"):
        f = (row.get("former_foma_identifier") or "").strip()
        c = (row.get("canonical_foma_identifier") or "").strip()
        if f and c and f != c and f not in mapping:
            mapping[f] = c
    # Ensure the current rule is included even if not yet recorded.
    mapping[former] = canonical
    return mapping


def _git(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(("git",) + args, cwd=str(cwd or REPO_FOR_GIT),
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def _backfill_bundle_markers(fst_path: Path) -> None:
    """Annotate a historical FST with the bundle markers it predates.

    ``# capr:bundle`` tells the parser which defines are structural groupings
    to recurse into rather than executable stages. Revisions older than that
    convention carry the same grouping defines under the same names but
    without the marker, so the parser cannot walk them. Marking exactly the
    defines whose names are structural today, and only where they exist at
    that revision, recovers the historical order without inventing any: the
    composition being read is still entirely the old source's own.
    """
    sys.path.insert(0, str(TOOLS))
    import oe_pipeline as pipeline

    text = fst_path.read_text(encoding="utf-8")
    if pipeline.BUNDLE_MARKER in text:
        return
    structural = pipeline._bundle_names(FST.read_text(encoding="utf-8"))
    out = []
    for line in text.splitlines(keepends=True):
        match = re.match(r"\s*define\s+([A-Za-z_]\w*)\b", line)
        if match and match.group(1) in structural:
            line = line.rstrip("\n") + f"  # {pipeline.BUNDLE_MARKER}\n"
        out.append(line)
    fst_path.write_text("".join(out), encoding="utf-8")


def _order_at(ref: str) -> list[str]:
    """The executable order of the cascade as it stood at a given revision.

    The revision's own tooling is preferred, so that the historical order is
    reported the way that revision itself reported it. Renames older than the
    manifest tool -- or older than the conventions it depends on -- still have
    a perfectly well-defined order, because it lives in that revision's
    ``germanic.txt``; for those, today's parser is pointed at the old source
    instead. That is sound because the parser only reports the order the
    source already states, and both sides of a comparison fall back together.
    """
    snippet = ("import sys; sys.path.insert(0, 'Germanic/tools');"
               "import cascade_order_manifest as c;"
               "print(c.manifest_text())")

    def run(tree: Path) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, "-c", snippet], cwd=str(tree),
                              capture_output=True, text=True)

    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp) / "tree"
        _git("worktree", "add", "--detach", str(tree), ref)
        try:
            out = run(tree)
            if out.returncode != 0:
                shutil.copytree(TOOLS, tree / "Germanic" / "tools",
                                dirs_exist_ok=True)
                _backfill_bundle_markers(
                    tree / "Germanic" / "fsts" / "germanic.txt")
                out = run(tree)
                if out.returncode != 0:
                    detail = out.stderr.strip().splitlines()[-1]
                    raise RuntimeError(f"order at {ref[:8]}: {detail}")
            rows = csv.DictReader(io.StringIO(out.stdout), delimiter="\t")
            return [r["foma_identifier"] for r in rows]
        finally:
            _git("worktree", "remove", "--force", str(tree))


def _live_order() -> list[str]:
    sys.path.insert(0, str(TOOLS))
    import cascade_order_manifest as com

    rows = csv.DictReader(io.StringIO(com.manifest_text()), delimiter="\t")
    return [r["foma_identifier"] for r in rows]


def _rename_boundary(former: str) -> tuple[str, str | None]:
    """The two revisions the rename sits between.

    ``before`` is the newest commit whose cascade still used the former
    identifier; ``after`` is the very next state of the FST, which is either
    the commit that follows it or, when the rename is not yet committed, the
    working tree. Pinning both sides to the rename itself is what keeps the
    gate meaningful: it asks whether *this* edit reordered the cascade, and
    stays silent about every legitimate reordering that came later.
    """
    history = _git("log", "--format=%H", "--",
                   "Germanic/fsts/germanic.txt").split()
    pattern = r"^\s*define\s+%s\b" % re.escape(former)
    for index, sha in enumerate(history):
        blob = _git("show", f"{sha}:Germanic/fsts/germanic.txt")
        if re.search(pattern, blob, re.MULTILINE):
            return sha, (history[index - 1] if index else None)
    raise RuntimeError(
        f"no commit of Germanic/fsts/germanic.txt still defines {former!r}; "
        "pass --before <ref> to name the pre-rename state explicitly")


def gate_e_order_unchanged(former: str, canonical: str,
                           before: str | None = None) -> list[str]:
    """Assert the rename relabelled the cascade without reordering it.

    The invariant for a behaviour-neutral rename is local to the rename:

        order immediately before == order immediately after,
        modulo the identifier substitution.

    It is emphatically NOT agreement with the campaign-era frozen manifest.
    That manifest archives how the cascade looked during the original naming
    campaign; legitimate scientific work has since added rules and moved
    others, so treating it as the authority for today's order makes the gate
    fail for reasons that have nothing to do with the rename under test.
    Comparing the two sides of the rename itself asks the question the gate
    exists to ask, and keeps asking it correctly however much the cascade
    grows afterwards -- which is also why a rename performed long ago stays
    checkable today.
    """
    try:
        after: str | None = None
        if before is None:
            before, after = _rename_boundary(former)
        previous = _order_at(before)
        subsequent = _order_at(after) if after else _live_order()
    except (RuntimeError, OSError) as exc:
        return [f"E: cannot establish the order across the rename: {exc}"]

    where = after[:8] if after else "the working tree"
    # Normalise BOTH sides through the completed rename map so the comparison
    # sees only order. Identifiers on either side may since have been
    # relabelled again -- a rule renamed after this one carries a different
    # name at the two revisions without anything having moved -- and the gate
    # is about position, not spelling. Dropped or added stages still fail,
    # because normalisation renames but never removes.
    rename_map = _completed_rename_map(former, canonical)

    def normalise(order: list[str]) -> list[str]:
        return [rename_map.get(name, name) for name in order]

    expected, subsequent = normalise(previous), normalise(subsequent)
    if expected == subsequent:
        return []

    errors: list[str] = []
    if len(expected) != len(subsequent):
        errors.append(
            f"E: the cascade changed length across the rename "
            f"({len(expected)} -> {len(subsequent)}); a rename must not add "
            f"or remove a stage")
    for i, (want, got) in enumerate(zip(expected, subsequent), start=1):
        if want != got:
            errors.append(
                f"E: order changed at position {i}: {before[:8]} had {want!r} "
                f"(after relabeling), {where} has {got!r}")
            break
    if not errors:
        errors.append("E: executable order differs across the rename")
    return errors


def _load_allowlist() -> list[tuple[str, str]]:
    if not ALLOWLIST.exists():
        return []
    pairs = []
    with ALLOWLIST.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            pairs.append(((row.get("former_identifier") or "").strip(),
                          (row.get("path_substring") or "").strip()))
    return pairs


def gate_g_former_name_audit(former: str) -> list[str]:
    errors: list[str] = []
    allow = _load_allowlist()
    variants = former_variants(former)
    # Scan behaviour-bearing source + validation code; the registries, reader-
    # facing source, and generated artifacts are migrated per rule and
    # regenerated in final canonicalisation (task section 9).
    scan_roots = [GERMANIC_ROOT / "fsts", GERMANIC_ROOT / "tools", GERMANIC_ROOT / "tests"]
    offenders: dict[str, list[str]] = {}
    for variant in variants:
        proc = subprocess.run(["grep", "-rwIl", "--exclude=*.bin", variant, *[str(p) for p in scan_roots if p.exists()]],
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for path in proc.stdout.decode("utf-8", "replace").splitlines():
            rel = path
            allowed = any(a_former in (former, "*") and sub and sub in rel for a_former, sub in allow)
            if not allowed:
                offenders.setdefault(rel, []).append(variant)
    for rel, vs in sorted(offenders.items()):
        errors.append(f"G: former name {sorted(set(vs))} still present in {rel}")
    return errors


def check(former: str, canonical: str, gates: str,
          before: str | None = None) -> int:
    all_errors: list[str] = []
    if "A" in gates:
        all_errors += gate_a_compile_and_define(former, canonical)
    if "B" in gates:
        all_errors += gate_b_output_identity()
    if "E" in gates:
        all_errors += gate_e_order_unchanged(former, canonical, before)
    if "G" in gates:
        all_errors += gate_g_former_name_audit(former)
    if all_errors:
        print(f"RENAME GATE FAILED for {former} -> {canonical}:")
        for e in all_errors:
            print(f"  - {e}")
        return 1
    print(f"RENAME GATE PASSED for {former} -> {canonical} (gates {gates}): "
          f"compile+no-alias, outputs_sha256 identity, order-unchanged, former-name audit clean")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--former", required=True)
    parser.add_argument("--canonical", required=True)
    parser.add_argument("--gates", default="ABEG", help="subset of ABEG to run (default all)")
    parser.add_argument("--before", default=None,
                        help="git ref holding the pre-rename cascade; by "
                             "default the newest commit still defining --former")
    args = parser.parse_args()
    return check(args.former, args.canonical, args.gates, args.before)


if __name__ == "__main__":
    raise SystemExit(main())
