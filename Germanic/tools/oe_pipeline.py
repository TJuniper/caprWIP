#!/usr/bin/env python3
"""Neutral shared model of the production Old English executable cascade.

ONE authority for executable order: the production composition in
``Germanic/fsts/germanic.txt``, rooted at the ``OldEnglish`` network (the
transducer saved as ``old_english.bin``).  This module parses that
composition recursively and exposes the complete physical execution
sequence — from the Proto-Germanic input filter to the Old English
surface — as an ordered list of :class:`Stage` objects.

Structural bundles are marked in the FST source itself with a
``# capr:bundle`` comment on their ``define`` line and are expanded
recursively; every other named member is a leaf stage.  A future nested
bundle therefore needs only the marker, not a parser special case.

Derived facts exposed here (and NOWHERE else as hand-maintained lists):

* ``exec_index``     — complete physical execution sequence (1-based);
* ``cascade_position`` — legacy-compatible SC position space used by the
  scientific records (the manifest numbering that starts inside
  ``EnglishProtoToOE`` and excludes the proto-input/PGmc prelude and the
  surface filter); ``None`` for prelude/surface stages;
* deterministic snapshot slugs and sandbox bin names;
* ``sc_id`` joined from the canonical semantic registry;
* ``rules_between()`` for crossed-rule analyses.

Consumers: cascade_order_manifest.py (generated TSV view),
generate_oe_sandbox.py (generated sandbox), oe_full_trace_report.py,
sc_evidence.py, rule_coverage_census.py, oe_bin_sync_check.py,
adjudicate.py, sc004_interaction_analysis.py.

Pure text parsing; needs neither foma nor Docker.
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Tuple

from capr_runtime import layout

sys.path.insert(0, str(layout().bin_dir))
from oe_input_context import (
    CITATION_CONTEXT, ContextEntry, METADATA_FILENAME, context_for_row, display_form,
    load_context_metadata, validate_context_rows,
)

ROOT_IDENTIFIER = "OldEnglish"
BUNDLE_MARKER = "capr:bundle"
SNAPSHOT_PREFIX = "old_english_sandbox_after_"

# Legacy-compatible cascade_position domain: a contiguous executable span,
# not a list of bundle names.  The numbered SC cascade starts at the first
# stage contained (at any nesting depth) in CASCADE_ENTRY_BUNDLE and ends
# just before the CASCADE_SURFACE_STAGE filter.  Every named stage inside
# that span is numbered contiguously regardless of how many nested
# structural bundles contain it.  The proto-input filter, the PGmc
# consonant prelude, and the surface filter are part of the physical
# execution sequence (exec_index) but outside this numbering.
CASCADE_ENTRY_BUNDLE = "EnglishProtoToOE"
CASCADE_SURFACE_STAGE = "OldEnglishSurface"

_IDENT_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")

# Compound morphological tokens kept whole in snapshot slugs.
_SLUG_TOKENS = ("PNWGmc", "PWGmc", "NWGmc", "PGmc", "EAF", "OE")
_SLUG_WORD_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z][a-z]*|[0-9]+|[a-z]+")


def snapshot_slug(identifier: str) -> str:
    """Deterministic snake_case slug for one Foma identifier."""
    words: List[str] = []
    i = 0
    while i < len(identifier):
        for token in _SLUG_TOKENS:
            if identifier.startswith(token, i) and not identifier[i + len(token):i + len(token) + 1].islower():
                words.append(token)
                i += len(token)
                break
        else:
            m = _SLUG_WORD_RE.match(identifier, i)
            if not m:
                raise ValueError(f"cannot slug {identifier!r} at index {i}")
            words.append(m.group(0))
            i = m.end()
    return "_".join(w.lower() for w in words)


def snapshot_bin_name(identifier: str) -> str:
    return f"{SNAPSHOT_PREFIX}{snapshot_slug(identifier)}.bin"


@dataclass(frozen=True)
class Stage:
    exec_index: int                 # 1-based complete physical sequence
    foma_identifier: str            # canonical Foma identifier ('' for inline)
    origin_block: str               # innermost bundle the member came from
    kind: str                       # 'named' or 'inline'
    inline_text: str = ""           # raw expression for inline members
    cascade_position: int | None = None  # legacy SC position space

    @property
    def slug(self) -> str:
        return snapshot_slug(self.foma_identifier)

    @property
    def snapshot_bin(self) -> str:
        return snapshot_bin_name(self.foma_identifier)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def _bundle_names(text: str) -> set[str]:
    names = set()
    for line in text.splitlines():
        if BUNDLE_MARKER not in line:
            continue
        comment = line.find("#")
        if comment < 0 or BUNDLE_MARKER not in line[comment:]:
            continue
        m = re.match(r"\s*define\s+([A-Za-z][A-Za-z0-9_]*)", line)
        if m:
            names.add(m.group(1))
    return names


_COMMENT_RE = re.compile(r"(?<!\.)#(?!\.)")  # a '#' that is not the .#. boundary


def _strip_comments(text: str) -> str:
    out = []
    for line in text.splitlines():
        m = _COMMENT_RE.search(line)
        out.append(line[:m.start()] if m else line)
    return "\n".join(out)


def _define_bodies(text: str) -> Dict[str, str]:
    """Map define name -> raw body (up to the ';' at bracket depth 0)."""
    bodies: Dict[str, str] = {}
    for m in re.finditer(r"\bdefine\s+([A-Za-z][A-Za-z0-9_]*)", text):
        name = m.group(1)
        depth = 0
        for i in range(m.end(), len(text)):
            ch = text[i]
            if ch in "([":
                depth += 1
            elif ch in ")]":
                depth -= 1
            elif ch == ";" and depth == 0:
                bodies[name] = text[m.end():i].strip()
                break
        else:
            raise ValueError(f"unterminated define {name}")
    return bodies


def _composition_members(body: str) -> List[str]:
    """Split one composition body into member expressions at depth 0."""
    body = body.strip()
    while (body.startswith("(") and body.endswith(")")) or (
            body.startswith("[") and body.endswith("]")):
        inner = body[1:-1]
        depth = 0
        balanced = True
        for ch in inner:
            if ch in "([":
                depth += 1
            elif ch in ")]":
                depth -= 1
                if depth < 0:
                    balanced = False
                    break
        if not balanced:
            break
        body = inner.strip()
    members: List[str] = []
    depth = 0
    start = 0
    i = 0
    while i < len(body):
        ch = body[i]
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        elif depth == 0 and body.startswith(".o.", i):
            members.append(body[start:i].strip())
            i += 3
            start = i
            continue
        i += 1
    members.append(body[start:].strip())
    return [m for m in members if m]


def parse_stages(fst_path: Path | None = None) -> List[Stage]:
    """Parse the complete production OE execution sequence from germanic.txt."""
    fst_path = fst_path or layout().germanic_fst
    raw = fst_path.read_text(encoding="utf-8")
    bundles = _bundle_names(raw)
    if ROOT_IDENTIFIER not in bundles:
        raise ValueError(
            f"root define {ROOT_IDENTIFIER!r} is not marked '# {BUNDLE_MARKER}' "
            f"in {fst_path}")
    bodies = _define_bodies(_strip_comments(raw))

    flat: List[Tuple[str, str, str, str, frozenset]] = []
    # (identifier, origin, kind, inline_text, ancestor bundle set)

    def expand(name: str, ancestors: frozenset) -> None:
        if name not in bodies:
            raise ValueError(f"bundle {name!r} has no define in {fst_path}")
        inner = ancestors | {name}
        for member in _composition_members(bodies[name]):
            if _IDENT_RE.match(member):
                if member in bundles:
                    expand(member, inner)
                else:
                    flat.append((member, name, "named", "", inner))
            else:
                flat.append(("", name, "inline", member, inner))

    expand(ROOT_IDENTIFIER, frozenset())

    # Numbered SC cascade span: from the first stage nested (at any depth)
    # inside CASCADE_ENTRY_BUNDLE up to (excluding) CASCADE_SURFACE_STAGE.
    entry_indices = [i for i, entry in enumerate(flat)
                     if CASCADE_ENTRY_BUNDLE in entry[4]]
    if not entry_indices:
        raise ValueError(
            f"cascade entry bundle {CASCADE_ENTRY_BUNDLE!r} has no expanded "
            f"members in {fst_path}")
    surface_indices = [i for i, entry in enumerate(flat)
                       if entry[0] == CASCADE_SURFACE_STAGE]
    if not surface_indices:
        raise ValueError(
            f"surface stage {CASCADE_SURFACE_STAGE!r} not found in {fst_path}")
    span_start = entry_indices[0]
    span_end = surface_indices[0]  # exclusive
    if span_end <= span_start:
        raise ValueError(
            f"surface stage {CASCADE_SURFACE_STAGE!r} precedes the cascade "
            f"entry bundle {CASCADE_ENTRY_BUNDLE!r} in {fst_path}")

    stages: List[Stage] = []
    cascade_pos = 0
    for i, (ident, origin, kind, inline_text, _ancestors) in enumerate(flat, start=1):
        pos = None
        if kind == "named" and span_start <= i - 1 < span_end:
            cascade_pos += 1
            pos = cascade_pos
        stages.append(Stage(exec_index=i, foma_identifier=ident,
                            origin_block=origin, kind=kind,
                            inline_text=inline_text, cascade_position=pos))
    return stages


@lru_cache(maxsize=None)
def _cached_stages() -> Tuple[Stage, ...]:
    return tuple(parse_stages())


def stages() -> List[Stage]:
    """The complete production OE execution sequence (cached)."""
    return list(_cached_stages())


def named_stages() -> List[Stage]:
    return [s for s in stages() if s.kind == "named"]


def stage_for(identifier: str) -> Stage:
    for s in stages():
        if s.foma_identifier == identifier:
            return s
    known = ", ".join(s.foma_identifier for s in named_stages())
    raise KeyError(f"{identifier!r} is not a stage of the production OE "
                   f"cascade. Known stages: {known}")


def exec_index(identifier: str) -> int:
    return stage_for(identifier).exec_index


def cascade_position(identifier: str) -> int | None:
    return stage_for(identifier).cascade_position


def previous_stage(identifier: str) -> Stage | None:
    idx = stage_for(identifier).exec_index
    prior = [s for s in named_stages() if s.exec_index < idx]
    return prior[-1] if prior else None


def next_stage(identifier: str) -> Stage | None:
    idx = stage_for(identifier).exec_index
    later = [s for s in named_stages() if s.exec_index > idx]
    return later[0] if later else None


# ---------------------------------------------------------------------------
# Composition structure (raw, unexpanded)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def _cached_composition_map(fst_path: Path) -> Dict[str, Tuple[str, ...]]:
    raw = fst_path.read_text(encoding="utf-8")
    bodies = _define_bodies(_strip_comments(raw))
    return {name: tuple(_composition_members(body))
            for name, body in bodies.items()}


def composition_members_of(identifier: str,
                           fst_path: Path | None = None) -> List[str]:
    """Raw depth-0 member expressions of one define (unexpanded).

    This is the ONE parser for production composition membership; tools
    must not re-parse germanic.txt with their own regexes.
    """
    comp = _cached_composition_map(fst_path or layout().germanic_fst)
    if identifier not in comp:
        raise KeyError(f"no define {identifier!r} in the production FST source")
    return list(comp[identifier])


def production_parent_chain(identifier: str, fst_path: Path | None = None,
                            root: str = ROOT_IDENTIFIER) -> List[str]:
    """Defines from ``identifier``'s direct parent up to ``root`` (inclusive),
    following the unique membership chain of the production composition."""
    fst_path = fst_path or layout().germanic_fst
    comp = _cached_composition_map(fst_path)
    reachable: set[str] = set()
    frontier = [root]
    while frontier:
        name = frontier.pop()
        if name in reachable or name not in comp:
            continue
        reachable.add(name)
        frontier.extend(m for m in comp[name] if _IDENT_RE.match(m))
    if identifier not in reachable:
        raise ValueError(f"{identifier!r} is not reachable from {root!r} "
                         "in the production composition")
    chain: List[str] = []
    current = identifier
    while current != root:
        parents = [name for name in reachable if current in comp.get(name, ())]
        if not parents:
            raise ValueError(f"{current!r} has no parent reachable from {root!r}")
        if len(parents) > 1:
            raise ValueError(
                f"{current!r} has multiple production parents: {sorted(parents)}")
        current = parents[0]
        chain.append(current)
    return chain


def rules_between(a: str, b: str, inclusive: bool = False) -> List[str]:
    """Named rules strictly between stages ``a`` and ``b`` in execution order
    (or including the endpoints with ``inclusive=True``)."""
    ia, ib = exec_index(a), exec_index(b)
    lo, hi = min(ia, ib), max(ia, ib)
    out = [s.foma_identifier for s in named_stages()
           if (lo <= s.exec_index <= hi if inclusive
               else lo < s.exec_index < hi)]
    return out


def are_adjacent(a: str, b: str) -> bool:
    """True iff named stage ``b`` executes immediately after named stage
    ``a`` (identity-based adjacency; never compare numeric positions)."""
    nxt = next_stage(a)
    return nxt is not None and nxt.foma_identifier == b


def first_numbered_stage() -> Stage:
    """The first stage of the numbered SC cascade (identity, not a number)."""
    for s in named_stages():
        if s.cascade_position is not None:
            return s
    raise RuntimeError("no numbered cascade stage found")


def run_before(bin_dir: Path, identifier: str, form: str) -> List[str]:
    """Form immediately BEFORE stage ``identifier`` (identity-based probe:
    applies the snapshot bin of the preceding named stage)."""
    prev = previous_stage(identifier)
    if prev is None:
        raise ValueError(f"{identifier!r} has no preceding named stage")
    return run_stage(bin_dir, prev.snapshot_bin, form)


def run_after(bin_dir: Path, identifier: str, form: str) -> List[str]:
    """Form immediately AFTER stage ``identifier`` (identity-based probe)."""
    return run_stage(bin_dir, stage_for(identifier).snapshot_bin, form)


def expected_snapshot_bins() -> List[str]:
    return [s.snapshot_bin for s in named_stages()]


# ---------------------------------------------------------------------------
# Semantic join (registry is the authority for SC <-> identifier mapping)
# ---------------------------------------------------------------------------

@lru_cache(maxsize=None)
def sc_ids_by_identifier() -> Dict[str, str]:
    registry = (layout().docs_dir / "sound_changes/registry/sc_registry.tsv")
    mapping: Dict[str, List[str]] = {}
    header: List[str] | None = None
    for line in registry.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        fields = line.split("\t")
        if header is None:
            header = fields
            continue
        row = dict(zip(header, fields))
        if row.get("lifecycle_status") != "active":
            continue
        ident = row.get("fst_identifier", "")
        if ident:
            mapping.setdefault(ident, []).append(row["sc_id"])
    return {ident: ";".join(sorted(ids)) for ident, ids in mapping.items()}


def sc_id(identifier: str) -> str:
    return sc_ids_by_identifier().get(identifier, "")


# ---------------------------------------------------------------------------
# Generated sandbox
# ---------------------------------------------------------------------------

def sandbox_text() -> str:
    """Deterministic generated Old English sandbox source.

    One cumulative trace checkpoint per named executable stage, saved as
    ``old_english_sandbox_after_<slug>.bin``.  The final checkpoint is the
    sandbox equivalent of the production Old English output.  Inline
    (anonymous) composition members are composed into the following
    checkpoint and are not separately snapshotted.
    """
    all_stages = stages()
    lines = [
        "# =========================================================================",
        "# GENERATED FILE — DO NOT EDIT.",
        "#",
        "# Stage-by-stage trace sandbox for the production Old English cascade.",
        "# Derived from the `OldEnglish` composition in fsts/germanic.txt by",
        "# Germanic/tools/generate_oe_sandbox.py (model: Germanic/tools/oe_pipeline.py).",
        "#",
        "# Regenerate: python3 Germanic/tools/generate_oe_sandbox.py",
        "# Verify:     python3 Germanic/tools/generate_oe_sandbox.py --check",
        "#",
        "# One cumulative checkpoint per named executable stage, in production",
        "# execution order; each checkpoint is saved as",
        "# old_english_sandbox_after_<slug>.bin in the foma working directory.",
        "# =========================================================================",
        "",
        "source fsts/germanic.txt",
        "",
    ]
    prev_define: str | None = None
    pending_inline: List[str] = []
    checkpoints: List[Tuple[str, str]] = []  # (define name, bin name)
    for s in all_stages:
        if s.kind == "inline":
            pending_inline.append(s.inline_text)
            continue
        define = f"S{s.exec_index:03d}{s.foma_identifier}"
        parts = ([prev_define] if prev_define else []) + pending_inline + [s.foma_identifier]
        pending_inline = []
        lines.append(f"define {define} " + "\n    .o. ".join(parts) + ";")
        checkpoints.append((define, s.snapshot_bin))
        prev_define = define
    lines.append("")
    for define, bin_name in checkpoints:
        lines.append("clear stack")
        lines.append(f"regex {define};")
        lines.append(f"save stack {bin_name}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Corpus + flookup helpers shared by the evidence tools
# ---------------------------------------------------------------------------

# Strip braces, stars, whitespace, slashes, parens — KEEP hyphens (compounds).
PROTO_STRIP_RE = re.compile(r"[{}*\s/()]")


def normalize_proto(raw: str) -> str:
    normalized = PROTO_STRIP_RE.sub("", raw or "")
    # Proto inventory uses θ; normalize þ to avoid false no_output buckets.
    return normalized.replace("þ", "θ")


def contexts_for_tsv(tsv_path: Path) -> dict[str, ContextEntry]:
    path = tsv_path.with_name(METADATA_FILENAME)
    if not path.exists() and tsv_path.resolve() != layout().corpus_tsv.resolve():
        return {}
    return load_context_metadata(path)


def evaluation_input(row: Dict[str, str]) -> str:
    if "fst_input" in row:
        return row["fst_input"]
    if "word_stress" in row or "phonological_finality" in row:
        raise ValueError("contextual row lacks its assembled evaluator input")
    return CITATION_CONTEXT.encode(row["proto_norm"])


def load_rows(tsv_path: Path) -> List[Dict[str, str]]:
    """Selected Old English corpus rows (attested counterpart present)."""
    rows: List[Dict[str, str]] = []
    contexts = contexts_for_tsv(tsv_path)
    with tsv_path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row.get("DOCULECT") != "Old_English":
                continue
            proto = (row.get("PROTOFORM") or "").strip()
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not proto or not counterpart or counterpart == "-":
                continue
            norm = normalize_proto(proto)
            if not norm:
                continue
            row_id = row.get("ID", "")
            context = context_for_row(row_id, proto, contexts)
            rows.append({
                "row_id": row_id,
                "concept": row.get("CONCEPT", ""),
                "proto": proto,
                "proto_norm": norm,
                "fst_input": context.encode(norm),
                "word_stress": context.word_stress,
                "phonological_finality": context.phonological_finality,
                "counterpart": counterpart,
            })
    validate_context_rows(contexts, {row["row_id"] for row in rows})
    return rows


def apply_down(bin_path: Path, form: str) -> List[str]:
    """Apply one transducer downward; deduplicated usable outputs only."""
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=(form + "\n").encode("utf-8"),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
    )
    outputs: List[str] = []
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        parts = raw.split("\t", 1)
        out = parts[1] if len(parts) == 2 else ""
        if out and out != "+?" and out not in outputs:
            outputs.append(out)
    return outputs


def run_stage(bin_dir: Path, bin_name: str, form: str) -> List[str]:
    """Apply one snapshot bin; keeps '+?' rejections visible."""
    proc = subprocess.run(
        ["flookup", "-i", str((bin_dir / bin_name).resolve())],
        input=(form + "\n").encode("utf-8"),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
    )
    outputs: List[str] = []
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        parts = raw.split("\t", 1)
        out = parts[1] if len(parts) == 2 else raw
        out = out or "+?"
        if out not in outputs:
            outputs.append(out)
    return outputs or ["+?"]
