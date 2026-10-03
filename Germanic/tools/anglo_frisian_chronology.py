#!/usr/bin/env python3
"""Check source-local research constraints, never production chronology."""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict, deque
from collections.abc import Sequence
from dataclasses import dataclass, fields
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TABLE = (
    ROOT / "Germanic/docs/sound_changes/literature_dossiers/anglo_frisian"
    / "historical_constraints.tsv"
)
RELATIONS = {"before", "not_after", "same_event", "distinct", "unresolved"}
SCOPES = {"common_stem", "daughter_only", "unresolved"}
EVIDENCE_TYPES = {"source_statement", "inference", "modelling_premise"}


@dataclass(frozen=True)
class Claim:
    claim_id: str
    model_id: str
    event_a: str
    event_b: str
    relation: str
    language: str
    event_a_scope: str
    event_b_scope: str
    event_a_spec: str
    event_b_spec: str
    layer: str
    source_key: str
    printed_pages: str
    evidence_type: str
    assumptions: str
    diagnostic: str
    sc_correspondence: str
    open_questions: str


def bibliography_keys(path: Path) -> set[str]:
    return set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", path.read_text(encoding="utf-8")))


def validate_claims(claims: list[Claim], known_keys: set[str]) -> None:
    if not claims:
        raise ValueError("constraint table contains no claims")
    seen: set[str] = set()
    optional = {"sc_correspondence", "open_questions"}
    for claim in claims:
        for field in fields(Claim):
            if field.name not in optional and not getattr(claim, field.name).strip():
                raise ValueError(f"{claim.claim_id or '<unnamed>'}: missing {field.name}")
        if claim.claim_id in seen:
            raise ValueError(f"duplicate claim_id: {claim.claim_id}")
        seen.add(claim.claim_id)
        if claim.relation not in RELATIONS:
            raise ValueError(f"{claim.claim_id}: unknown relation {claim.relation}")
        if {claim.event_a_scope, claim.event_b_scope} - SCOPES:
            raise ValueError(f"{claim.claim_id}: invalid explicit scope")
        if claim.evidence_type not in EVIDENCE_TYPES:
            raise ValueError(f"{claim.claim_id}: invalid evidence_type")
        if claim.source_key not in known_keys:
            raise ValueError(f"{claim.claim_id}: unknown source key {claim.source_key}")
        for span in claim.printed_pages.split(","):
            match = re.fullmatch(r"\s*([1-9]\d*)(?:[-–]([1-9]\d*))?\s*", span)
            if not match or int(match[1]) > int(match[2] or match[1]):
                raise ValueError(f"{claim.claim_id}: invalid printed pages {claim.printed_pages}")


def load_claims(path: Path, known_keys: set[str]) -> list[Claim]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        names = {field.name for field in fields(Claim)}
        if reader.fieldnames is None or len(reader.fieldnames) != len(names) or set(reader.fieldnames) != names:
            raise ValueError("constraint table header does not match the research schema")
        claims = []
        for line, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"constraint table line {line}: malformed TSV row")
            claims.append(Claim(**{key: value.strip() for key, value in row.items()}))
    validate_claims(claims, known_keys)
    return claims


def _path(graph: dict[str, list[tuple[str, Claim]]], start: str, target: str):
    queue = deque([(start, [start], [])])
    visited = {start}
    while queue:
        node, events, claims = queue.popleft()
        if node == target:
            return events, claims
        for neighbour, claim in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, events + [neighbour], claims + [claim]))
    return None


def check_model(claims: list[Claim]) -> dict:
    """Report conditional consistency of exactly one already-validated model."""
    models = {claim.model_id for claim in claims}
    if len(models) != 1:
        raise ValueError("check_model requires exactly one nonempty source-local model")
    order: dict[str, list[tuple[str, Claim]]] = defaultdict(list)
    identity: dict[str, list[tuple[str, Claim]]] = defaultdict(list)
    scopes: dict[str, dict[str, list[Claim]]] = defaultdict(lambda: defaultdict(list))
    undirected: dict[str, set[str]] = defaultdict(set)
    incomplete = []
    for claim in claims:
        for event, scope in ((claim.event_a, claim.event_a_scope), (claim.event_b, claim.event_b_scope)):
            scopes[event][scope].append(claim)
        undirected[claim.event_a].add(claim.event_b)
        undirected[claim.event_b].add(claim.event_a)
        if claim.relation in {"before", "not_after", "same_event"}:
            order[claim.event_a].append((claim.event_b, claim))
        if claim.relation == "same_event":
            order[claim.event_b].append((claim.event_a, claim))
            identity[claim.event_a].append((claim.event_b, claim))
            identity[claim.event_b].append((claim.event_a, claim))
        if claim.relation == "unresolved":
            incomplete.append(f"{claim.claim_id}: unresolved relation")
        if claim.open_questions:
            incomplete.append(f"{claim.claim_id}: {claim.open_questions}")
    for event, assertions in scopes.items():
        if not (set(assertions) - {"unresolved"}):
            incomplete.append(f"{event}: unresolved scope")
    unseen = set(scopes)
    groups = 0
    while unseen:
        groups += 1
        pending = [unseen.pop()]
        while pending:
            for neighbour in undirected[pending.pop()] & unseen:
                unseen.remove(neighbour)
                pending.append(neighbour)
    if groups > 1:
        incomplete.append(f"{groups} disconnected event groups; linking chronology not established")

    issues = []
    recorded = set()

    def issue(kind: str, events: list[str], path: list[Claim], support: Sequence[Claim] = ()) -> None:
        relevant = {claim.claim_id: claim for claim in path + list(support)}
        signature = kind, frozenset(relevant)
        if signature in recorded:
            return
        recorded.add(signature)
        issues.append({
            "kind": kind,
            "event_path": events,
            "claim_path": [claim.claim_id for claim in path],
            "supporting_claims": list(dict.fromkeys(claim.claim_id for claim in support)),
            "sources": [
                {"claim_id": claim.claim_id, "key": claim.source_key, "pages": claim.printed_pages,
                 "assumptions": claim.assumptions}
                for claim in relevant.values()
            ],
        })

    for claim in claims:
        if claim.relation == "before":
            back = _path(order, claim.event_b, claim.event_a)
            if back is not None:
                issue("strict_cycle", [claim.event_a] + back[0], [claim] + back[1])
        elif claim.relation == "distinct":
            equal = _path(identity, claim.event_a, claim.event_b)
            if equal is not None:
                issue("identity_conflict", equal[0], equal[1], [claim])
    for event, assertions in scopes.items():
        if "daughter_only" in assertions and "common_stem" in assertions:
            issue("scope_conflict", [event], [], assertions["daughter_only"] + assertions["common_stem"])
        if "daughter_only" not in assertions:
            continue
        for target, target_scopes in scopes.items():
            if target == event or "common_stem" not in target_scopes:
                continue
            path = _path(order, event, target)
            if path is not None:
                issue("daughter_predecessor", path[0], path[1],
                      assertions["daughter_only"] + target_scopes["common_stem"])
    return {
        "model_id": claims[0].model_id,
        "status": "inconsistent" if issues else "incomplete" if incomplete else "consistent_under_assumptions",
        "coverage": "These source-local claims only; not a complete history or an inheritance verdict.",
        "assumptions": {claim.claim_id: claim.assumptions for claim in claims},
        "issues": issues,
        "incomplete": incomplete,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", type=Path, default=DEFAULT_TABLE)
    parser.add_argument("--bibliography", type=Path, default=ROOT / "docs/refs.bib")
    parser.add_argument("--model", help="One exact model ID; alternatives are never combined")
    args = parser.parse_args(argv)
    try:
        claims = load_claims(args.table, bibliography_keys(args.bibliography))
        models = sorted({claim.model_id for claim in claims})
        if args.model is not None:
            if args.model not in models:
                raise ValueError(f"unknown model: {args.model}")
            models = [args.model]
        results = [check_model([claim for claim in claims if claim.model_id == model]) for model in models]
    except (OSError, ValueError, csv.Error) as error:
        parser.error(str(error))
    print(json.dumps(results, indent=2, ensure_ascii=False))
    statuses = {result["status"] for result in results}
    return 1 if "inconsistent" in statuses else 3 if "incomplete" in statuses else 0


if __name__ == "__main__":
    raise SystemExit(main())
