"""Explicit Old English evaluation context, separate from lexical reconstruction."""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from foma import FST

WEAK_FINAL_MARK = "ᵘ"
WEAK_NONFINAL_MARK = "ᶜ"
CONTEXT_MARKS = (WEAK_FINAL_MARK, WEAK_NONFINAL_MARK)
METADATA_FILENAME = "entry_context_metadata.tsv"
FIELDS = (
    "row_id", "baseline_input", "word_stress", "phonological_finality",
    "checkpoint", "source_key", "printed_pages", "note",
)


@dataclass(frozen=True)
class InputContext:
    word_stress: str
    phonological_finality: str

    def __post_init__(self) -> None:
        if self.word_stress not in {"stressed", "unstressed"}:
            raise ValueError(f"unknown sentence stress: {self.word_stress!r}")
        if self.phonological_finality not in {"final", "nonfinal"}:
            raise ValueError(f"unknown phonological finality: {self.phonological_finality!r}")
        if self.word_stress == "stressed" and self.phonological_finality == "nonfinal":
            raise ValueError("stressed nonfinal context is outside the bounded OE interface")

    @property
    def marker(self) -> str:
        return (
            WEAK_NONFINAL_MARK if self.phonological_finality == "nonfinal"
            else WEAK_FINAL_MARK if self.word_stress == "unstressed"
            else ""
        )

    def encode(self, segmental_input: str) -> str:
        if not segmental_input or any(mark in segmental_input for mark in CONTEXT_MARKS):
            raise ValueError("expected a nonempty, unannotated segmental input")
        return self.marker + segmental_input


CITATION_CONTEXT = InputContext("stressed", "final")


@dataclass(frozen=True)
class ContextEntry:
    baseline_input: str
    context: InputContext
    source_key: str
    printed_pages: str


def load_context_metadata(path: Path) -> dict[str, ContextEntry]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != list(FIELDS):
            raise ValueError(f"{path}: invalid context metadata columns")
        entries = {}
        for line, row in enumerate(reader, 2):
            if any(not (row.get(field) or "").strip() for field in FIELDS):
                raise ValueError(f"{path}:{line}: incomplete context metadata")
            identifier = row["row_id"]
            if not identifier.isdecimal() or identifier in entries:
                raise ValueError(f"{path}:{line}: invalid or duplicate row ID {identifier!r}")
            if row["checkpoint"] != "SC098":
                raise ValueError(f"{path}:{line}: unsupported context checkpoint")
            if not re.fullmatch(r"[0-9]+(?:-[0-9]+)?(?:,[0-9]+(?:-[0-9]+)?)*",
                                row["printed_pages"]):
                raise ValueError(f"{path}:{line}: printed page numbers required")
            if any(mark in row["baseline_input"] for mark in CONTEXT_MARKS):
                raise ValueError(f"{path}:{line}: context annotation in reconstruction")
            entries[identifier] = ContextEntry(
                row["baseline_input"],
                InputContext(row["word_stress"], row["phonological_finality"]),
                row["source_key"], row["printed_pages"],
            )
    return entries


def context_for_row(
    row_id: str, segmental_proto: str, entries: dict[str, ContextEntry],
) -> InputContext:
    entry = entries.get(row_id)
    if entry is None:
        return CITATION_CONTEXT
    if entry.baseline_input != segmental_proto:
        raise ValueError(f"{row_id}: context evidence disagrees with selected input")
    return entry.context


def validate_context_rows(entries: dict[str, ContextEntry], row_ids: set[str]) -> None:
    missing = entries.keys() - row_ids
    if missing:
        raise ValueError(f"context metadata IDs absent from selected corpus: {sorted(missing)}")


def display_form(form: str) -> str:
    for mark in CONTEXT_MARKS:
        form = form.replace("*" + mark, "").replace(mark, "")
    return form


class ContextualLexicalFST:
    """A lexical view of one native network under explicitly selected contexts."""

    def __init__(self, fst: FST) -> None:
        self.native = fst
        self.networks: dict[InputContext, FST] = {}

    def network(self, context: InputContext) -> FST:
        if context not in self.networks:
            from foma import FST
            mark = context.marker
            prefix = f"0:{{{mark}}}" if mark else "0"
            adapter = FST(f"[[{prefix}] [[? - [{{ᵘ}}|{{ᶜ}}]]*]]")
            self.networks[context] = adapter.compose(self.native)
        return self.networks[context]

    def apply_up(self, form: str, context: InputContext = CITATION_CONTEXT):
        return self.network(context).apply_up(form)

    def apply_down(self, form: str, context: InputContext = CITATION_CONTEXT):
        return self.network(context).apply_down(form)


def board_context(metadata: dict[str, str] | None) -> InputContext:
    if metadata is None:
        return CITATION_CONTEXT
    if set(metadata) != {"checkpoint", "wordStress", "phonologicalFinality"}:
        raise ValueError("invalid board input-context fields")
    if metadata["checkpoint"] != "SC098":
        raise ValueError("unsupported board input-context checkpoint")
    return InputContext(metadata["wordStress"], metadata["phonologicalFinality"])


def lexical_fst(fst: FST, doculect: str) -> FST | ContextualLexicalFST:
    """Keep marks out of reconstructions without marginalizing selected contexts."""
    if doculect != "Old_English" or not set(CONTEXT_MARKS) <= fst.alphabet():
        return fst
    return ContextualLexicalFST(fst)


def lexical_apply_up(fst: FST | ContextualLexicalFST, form: str,
                     context: InputContext = CITATION_CONTEXT):
    if isinstance(fst, ContextualLexicalFST):
        return fst.apply_up(form, context)
    return fst.apply_up(form)


def lexical_apply_down(fst: FST | ContextualLexicalFST, form: str,
                       context: InputContext = CITATION_CONTEXT):
    if isinstance(fst, ContextualLexicalFST):
        return fst.apply_down(form, context)
    return fst.apply_down(form)
