#!/usr/bin/env python3
"""Order-sensitivity runner for Old English baseline, validation, and pilot modes.

Order spaces (do not conflate):

* EXECUTABLE ORDER — the production composition in fsts/germanic.txt,
  exposed by the shared model (oe_pipeline.py). This is the chain the
  experiments actually manipulate; it is derived, never hand-listed here.
* INVENTORY ORDER — the archival order space frozen in
  registry/archival_orders.tsv (ARCHIVE; formerly the registry
  ``inventory_order`` column). Used only
  as coordinates for the archival experiment summaries and for
  inventory-vs-chain neighbor discrepancy notes; it does NOT drive which
  rules are adjacent in a variant.
* CHRONOLOGY-EXPERIMENT ORDER — the archival summary columns
  (``baseline_order``, ``first_break_order``, ``variant_order``,
  ``last_safe_order``) express movement steps in inventory-order
  coordinates. They are historical experiment bookkeeping, kept for
  compatibility with the committed first-break corpus.

The scientific experiment (focal SC, movement direction, order profile,
boundary tested) stays human-specified; the production chain it manipulates
comes exclusively from oe_pipeline.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

import oe_pipeline  # noqa: E402
from capr_runtime import check_build_manifest, layout  # noqa: E402
from oe_pipeline import apply_down, evaluation_input, load_rows  # noqa: E402


RESUME_STEPS_RE = re.compile(r"resume_steps=(\d+)")
LAST_SAFE_ORDER_RE = re.compile(r"last_safe_order=(\d+)")

FIRST_BREAK_DONE_RESULTS = {
    "first_break_found",
    "no_break_before_boundary",
    "compile_failure",
    "blocked_by_runner_limitation",
    "ambiguous_needs_review",
}

DEFAULT_ORDER_PROFILE = "default"
EXPANDED_PWGMC_ORDER_PROFILE = "expanded-pwgmc"

# The structural bundle expanded by the expanded-pwgmc order profile. Its
# component sequence is DERIVED from the live production composition via
# oe_pipeline; no hand-maintained component list exists here.
PWGMC_BUNDLE = "EarlyEnglishLineChanges"
EXPERIMENT_ROOT = "EnglishProtoToOE"


@dataclass(frozen=True)
class ChangeInfo:
    change_id: str
    display_name: str
    inventory_order: int  # archival inventory/chronology-experiment order space
    rule_name: str
    entry_type: str
    include_in_volume: str
    notes: str


@dataclass(frozen=True)
class NeighborInfo:
    change_id: str
    display_name: str
    inventory_order: int | None  # absent for post-archive registered stages
    rule_name: str
    entry_type: str


def repo_paths() -> Dict[str, Path]:
    """Canonical paths from the shared runtime layout (capr_runtime).

    The live bin is the production old_english.bin in the ONE authoritative
    runtime bin directory (host backend/ == container /usr/app). No
    candidate search, no Germanic/fsts fallback.
    """
    rt = layout()
    germanic_dir = rt.germanic_dir
    summaries_dir = germanic_dir / "docs" / "sound_changes" / "order_tests" / "summaries"
    return {
        "tools_dir": rt.tools_dir,
        "germanic_dir": germanic_dir,
        "repo_root": rt.repo_root,
        "inventory": germanic_dir / "docs" / "sound_changes" / "sound_change_inventory.tsv",
        "registry": germanic_dir / "docs" / "sound_changes" / "registry" / "sc_registry.tsv",
        "archival_orders": germanic_dir / "docs" / "sound_changes" / "registry" / "archival_orders.tsv",
        "germanic_txt": rt.germanic_fst,
        "sandbox_txt": rt.sandbox_fst,
        "aligned_tsv": rt.corpus_tsv,
        "live_bin": rt.bin_dir / "old_english.bin",
        "baseline_tsv": summaries_dir / "order_sensitivity_baseline_01.tsv",
        "identity_tsv": summaries_dir / "order_sensitivity_identity_variant_02.tsv",
        "adjacent_tsv": summaries_dir / "order_sensitivity_adjacent_pilot_01.tsv",
        "adjacent_changes_tsv": summaries_dir / "order_sensitivity_adjacent_pilot_01_changes.tsv",
        "first_break_tsv": summaries_dir / "order_sensitivity_first_break_pilot_03.tsv",
        "first_break_changes_tsv": summaries_dir / "order_sensitivity_first_break_pilot_03_changes.tsv",
        "first_break_failures_tsv": summaries_dir / "order_sensitivity_first_break_pilot_03_failures.tsv",
    }


def parse_args() -> argparse.Namespace:
    defaults = repo_paths()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        required=True,
        choices=("baseline", "identity-variant", "adjacent-pilot", "first-break", "validate-batch"),
    )
    parser.add_argument("--change", help="Target change_id for adjacent-pilot or first-break mode (e.g. SC043)")
    parser.add_argument("--direction", choices=("earlier", "later", "both"), default="both")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument(
        "--order-profile",
        choices=(DEFAULT_ORDER_PROFILE, EXPANDED_PWGMC_ORDER_PROFILE),
        default=DEFAULT_ORDER_PROFILE,
        help="Order profile for --mode first-break; default keeps bundled EarlyEnglishLineChanges.",
    )
    parser.add_argument(
        "--dry-run-order",
        action="store_true",
        help="Print the resolved first-break order profile and exit without compiling a variant.",
    )
    parser.add_argument("--inventory", default=str(defaults["inventory"]))
    parser.add_argument("--germanic", default=str(defaults["germanic_txt"]))
    parser.add_argument("--sandbox", default=str(defaults["sandbox_txt"]))
    parser.add_argument("--tsv", default=str(defaults["aligned_tsv"]))
    parser.add_argument("--bin", default=str(defaults["live_bin"]))
    parser.add_argument("--baseline-output", default=str(defaults["baseline_tsv"]))
    parser.add_argument("--identity-output", default=str(defaults["identity_tsv"]))
    parser.add_argument("--summary-output", default=str(defaults["adjacent_tsv"]))
    parser.add_argument("--changes-output", default=str(defaults["adjacent_changes_tsv"]))
    parser.add_argument("--first-break-output", default=str(defaults["first_break_tsv"]))
    parser.add_argument("--first-break-changes-output", default=str(defaults["first_break_changes_tsv"]))
    parser.add_argument("--first-break-failures-output", default=str(defaults["first_break_failures_tsv"]))
    parser.add_argument(
        "--allow-stale-bin",
        action="store_true",
        help="Debug only: skip the build-manifest freshness check for the canonical runtime bin.",
    )
    args = parser.parse_args()
    if args.mode in {"adjacent-pilot", "first-break"} and not args.change:
        parser.error("--change is required for --mode adjacent-pilot and --mode first-break")
    if args.order_profile != DEFAULT_ORDER_PROFILE and args.mode != "first-break":
        parser.error("--order-profile is currently supported only with --mode first-break")
    if args.dry_run_order and args.mode != "first-break":
        parser.error("--dry-run-order requires --mode first-break")
    return args


def registry_fst_identifiers(path: Path) -> Dict[str, str]:
    """Canonical SC id -> fst_identifier mapping from the semantic registry.

    sc_registry.tsv is the ONE authority for which executable FST rule a
    sound change denotes; the inventory view's rule_source_anchor is
    documentation only and is never used for executable identity.
    """
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    reader = csv.DictReader(lines, delimiter="\t")
    return {
        (row.get("sc_id") or "").strip(): (row.get("fst_identifier") or "").strip()
        for row in reader
    }


def archival_inventory_orders(path: Path) -> Dict[str, int]:
    """SC id -> archival inventory order from registry/archival_orders.tsv.

    This ARCHIVE/FROZEN file is the order space in which the first-break
    experiments were run. It is experiment bookkeeping, never current state,
    and is never resynchronized with the executable cascade.
    """
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    reader = csv.DictReader(lines, delimiter="\t")
    return {
        (row.get("sc_id") or "").strip(): int(row["inventory_order"])
        for row in reader
        if (row.get("inventory_order") or "").strip()
    }


def load_inventory(
    path: Path,
    fst_identifiers: Dict[str, str],
    inventory_orders: Dict[str, int],
) -> Tuple[Dict[str, ChangeInfo], List[ChangeInfo]]:
    by_id: Dict[str, ChangeInfo] = {}
    ordered: List[ChangeInfo] = []
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    reader = csv.DictReader(lines, delimiter="\t")
    model_rules = {s.foma_identifier for s in oe_pipeline.named_stages()}
    for row in reader:
            change_id = (row.get("change_id") or "").strip()
            # Archival experiment order space (registry/archival_orders.tsv);
            # this is INVENTORY order, not executable position. Rows outside
            # the archival order space are metadata-only.
            if change_id not in inventory_orders:
                continue
            inventory_order = inventory_orders[change_id]
            # sc_registry.tsv is the ONE identity authority. Rows without a
            # registry fst_identifier (support stages, technical markers,
            # surface orthography) stay as inventory metadata but cannot be
            # experiment targets.
            rule_name = fst_identifiers.get(change_id, "")
            if rule_name and rule_name not in model_rules:
                raise SystemExit(
                    f"{change_id}: registry fst_identifier {rule_name!r} is not "
                    "a stage of the executable model (oe_pipeline); fix "
                    "sc_registry.tsv or germanic.txt")
            info = ChangeInfo(
                change_id=change_id,
                display_name=(row.get("display_name") or "").strip(),
                inventory_order=int(inventory_order),
                rule_name=rule_name,
                entry_type=(row.get("entry_type") or "").strip(),
                include_in_volume=(row.get("include_in_volume") or "").strip(),
                notes=(row.get("notes") or "").strip(),
            )
            by_id[info.change_id] = info
            ordered.append(info)
    ordered.sort(key=lambda item: item.inventory_order)
    return by_id, ordered


def inventory_rule_lookup(ordered: Sequence[ChangeInfo]) -> Dict[str, NeighborInfo]:
    lookup = {
        item.rule_name: NeighborInfo(
            item.change_id,
            item.display_name,
            item.inventory_order,
            item.rule_name,
            item.entry_type,
        )
        for item in ordered
        if item.rule_name
    }
    lines = [line for line in repo_paths()["registry"].read_text(encoding="utf-8").splitlines()
             if line and not line.startswith("#")]
    for row in csv.DictReader(lines, delimiter="\t"):
        rule_name = row.get("fst_identifier", "").strip()
        if rule_name and rule_name not in lookup:
            lookup[rule_name] = NeighborInfo(
                row["sc_id"], row["display_name"], None, rule_name,
                row["entry_type"])
    return lookup


def placeholder_neighbor(rule_name: str, fallback_order: int) -> NeighborInfo:
    return NeighborInfo("", rule_name, fallback_order, rule_name, "blocked_by_runner_limitation")


def neighbors_for_change(change_id: str, ordered: Sequence[ChangeInfo]) -> Tuple[NeighborInfo | None, NeighborInfo | None]:
    for idx, item in enumerate(ordered):
        if item.change_id != change_id:
            continue
        earlier = ordered[idx - 1] if idx > 0 else None
        later = ordered[idx + 1] if idx + 1 < len(ordered) else None
        return (
            NeighborInfo(earlier.change_id, earlier.display_name, earlier.inventory_order, earlier.rule_name, earlier.entry_type) if earlier else None,
            NeighborInfo(later.change_id, later.display_name, later.inventory_order, later.rule_name, later.entry_type) if later else None,
        )
    raise KeyError(f"Change {change_id} not found in inventory")


def parse_english_proto_to_oe_order(germanic_path: Path) -> List[str]:
    """Live experiment order: the raw member sequence of the production
    EnglishProtoToOE composition, from the shared executable model."""
    order = oe_pipeline.composition_members_of(EXPERIMENT_ROOT, germanic_path)
    if not order:
        raise RuntimeError(
            f"{EXPERIMENT_ROOT} in {germanic_path} parsed to an empty rule list")
    return order


def pwgmc_bundle_components(germanic_path: Path) -> List[str]:
    """Current component sequence of the PWGmc structural bundle, derived
    from the live production composition (never hand-listed)."""
    components = oe_pipeline.composition_members_of(PWGMC_BUNDLE, germanic_path)
    if not components:
        raise RuntimeError(
            f"{PWGMC_BUNDLE} in {germanic_path} parsed to an empty rule list")
    return components


def validate_expanded_pwgmc_components(germanic_path: Path) -> None:
    """The bundle's components must be consecutive named stages of the
    executable model, so expanding it in place is order-preserving."""
    components = pwgmc_bundle_components(germanic_path)
    stage_names = [s.foma_identifier for s in oe_pipeline.named_stages()]
    try:
        start = stage_names.index(components[0])
    except ValueError as exc:
        raise RuntimeError(
            f"{PWGMC_BUNDLE} component missing from the executable model: {exc}"
        ) from exc
    if stage_names[start:start + len(components)] != components:
        raise RuntimeError(
            f"{PWGMC_BUNDLE} components are not consecutive in the executable "
            f"model: {components!r}")


def expand_pwgmc_changes(order: Sequence[str], germanic_path: Path) -> List[str]:
    validate_expanded_pwgmc_components(germanic_path)
    components = pwgmc_bundle_components(germanic_path)
    expanded: List[str] = []
    replaced = 0
    for rule in order:
        if rule == PWGMC_BUNDLE:
            expanded.extend(components)
            replaced += 1
            continue
        expanded.append(rule)
    if replaced != 1:
        raise RuntimeError(
            f"Expected exactly one {PWGMC_BUNDLE} entry in {EXPERIMENT_ROOT}, "
            f"found {replaced}")
    return expanded


def resolve_first_break_order_profile(
    live_order: Sequence[str],
    order_profile: str,
    germanic_path: Path,
) -> List[str]:
    if order_profile == DEFAULT_ORDER_PROFILE:
        return list(live_order)
    if order_profile == EXPANDED_PWGMC_ORDER_PROFILE:
        return expand_pwgmc_changes(live_order, germanic_path)
    raise ValueError(f"Unknown order profile: {order_profile}")


def ensure_expanded_pwgmc_outputs_are_separate(
    *,
    order_profile: str,
    dry_run_order: bool,
    first_break_output: Path,
    first_break_changes_output: Path,
    first_break_failures_output: Path,
) -> None:
    if order_profile != EXPANDED_PWGMC_ORDER_PROFILE or dry_run_order:
        return
    defaults = repo_paths()
    default_outputs = {
        defaults["first_break_tsv"].resolve(),
        defaults["first_break_changes_tsv"].resolve(),
        defaults["first_break_failures_tsv"].resolve(),
    }
    current_outputs = [
        first_break_output.resolve(),
        first_break_changes_output.resolve(),
        first_break_failures_output.resolve(),
    ]
    if any(path in default_outputs for path in current_outputs):
        raise SystemExit(
            "expanded-pwgmc order profile requires separate --first-break-output, "
            "--first-break-changes-output, and --first-break-failures-output paths; "
            "refusing to write expanded-profile results into the default first-break corpus."
        )


def print_order_profile(
    order: Sequence[str],
    order_profile: str,
    change: ChangeInfo,
    ordered_inventory: Sequence[ChangeInfo],
) -> None:
    inventory_by_rule = inventory_rule_lookup(ordered_inventory)
    if change.rule_name not in order:
        raise RuntimeError(f"{change.rule_name} is not in the resolved {order_profile} order profile")
    print(
        f"order_profile={order_profile} total_rules={len(order)} "
        f"target_change={change.change_id} target_rule={change.rule_name}"
    )
    for index, rule_name in enumerate(order, start=1):
        info = inventory_by_rule.get(rule_name)
        change_id = info.change_id if info else "-"
        display_name = info.display_name if info else rule_name
        marker = " target" if rule_name == change.rule_name else ""
        print(f"{index:03d}\t{change_id}\t{rule_name}\t{display_name}{marker}")


def format_outputs(outputs: Sequence[str]) -> str:
    return " | ".join(outputs) if outputs else "+?"


def result_key(row: Dict[str, object]) -> Tuple[str, str]:
    return (str(row["lexical_item"]), str(row["protoform"]))


def outputs_match_expected(outputs: Sequence[str], expected: str) -> bool:
    return expected in outputs


def baseline_note(outputs: Sequence[str], expected: str) -> str:
    if not outputs:
        return "no_output"
    if len(outputs) > 1 and expected in outputs:
        return "multiple_outputs_includes_expected"
    if len(outputs) > 1:
        return "multiple_outputs_missing_expected"
    if expected in outputs:
        return "exact_match"
    return "single_output_mismatch"


def evaluate_rows_rowwise(rows: Sequence[Dict[str, str]], bin_path: Path) -> List[Dict[str, object]]:
    return [
        build_evaluated_row(row, apply_down(bin_path, evaluation_input(row)))
        for row in rows
    ]


def evaluate_rows_batch(rows: Sequence[Dict[str, str]], bin_path: Path) -> List[Dict[str, object]]:
    outputs_by_row = batch_apply_down(bin_path, [evaluation_input(row) for row in rows])
    return [
        build_evaluated_row(row, outputs)
        for row, outputs in zip(rows, outputs_by_row)
    ]


def evaluate_rows(rows: Sequence[Dict[str, str]], bin_path: Path) -> List[Dict[str, object]]:
    return evaluate_rows_batch(rows, bin_path)


def validate_batch_outputs(rows: Sequence[Dict[str, str]], bin_path: Path) -> Dict[str, object]:
    rowwise_results = evaluate_rows_rowwise(rows, bin_path)
    batch_results = evaluate_rows_batch(rows, bin_path)
    mismatches: List[Dict[str, str]] = []
    for rowwise_row, batch_row in zip(rowwise_results, batch_results):
        if (
            rowwise_row["outputs_text"] == batch_row["outputs_text"]
            and rowwise_row["matches_expected"] == batch_row["matches_expected"]
            and rowwise_row["notes"] == batch_row["notes"]
        ):
            continue
        mismatches.append(
            {
                "lexical_item": str(rowwise_row["lexical_item"]),
                "protoform": str(rowwise_row["protoform"]),
                "rowwise_output": str(rowwise_row["outputs_text"]),
                "batch_output": str(batch_row["outputs_text"]),
                "rowwise_matches_expected": "yes" if rowwise_row["matches_expected"] else "no",
                "batch_matches_expected": "yes" if batch_row["matches_expected"] else "no",
            }
        )
    return {
        "rows": len(rows),
        "matching_rows": len(rows) - len(mismatches),
        "differing_rows": len(mismatches),
        "mismatches": mismatches,
    }


def summarize_evaluation(results: Sequence[Dict[str, object]]) -> Dict[str, int]:
    return {
        "total_rows_tested": len(results),
        "matches_expected": sum(1 for row in results if row["matches_expected"]),
        "fails_expected": sum(1 for row in results if not row["matches_expected"]),
        "no_output_rows": sum(1 for row in results if not row["outputs"]),
        "multi_output_rows": sum(1 for row in results if len(row["outputs"]) > 1),
    }


def write_baseline_tsv(results: Sequence[Dict[str, object]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "lexical_item",
        "protoform",
        "expected_counterpart",
        "current_outputs",
        "current_matches_expected",
        "notes",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in results:
            writer.writerow(
                {
                    "lexical_item": row["lexical_item"],
                    "protoform": row["protoform"],
                    "expected_counterpart": row["expected_counterpart"],
                    "current_outputs": row["outputs_text"],
                    "current_matches_expected": "yes" if row["matches_expected"] else "no",
                    "notes": row["notes"],
                }
            )


def write_tsv(fieldnames: Sequence[str], rows: Sequence[Dict[str, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(
            {
                field: str(row.get(field, ""))
                for field in fieldnames
            }
            for row in rows
        )


def read_tsv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def dedupe_preserving_order(items: Iterable[str]) -> List[str]:
    seen = set()
    deduped: List[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def batch_apply_down(bin_path: Path, forms: Sequence[str]) -> List[List[str]]:
    markers = [f"__ORDER_SENS_BOUNDARY_{index:04d}__" for index in range(len(forms))]
    if any(form in markers for form in forms):
        raise RuntimeError("Input forms unexpectedly collide with batch boundary markers")
    batched_input: List[str] = []
    for form, marker in zip(forms, markers):
        batched_input.append(form)
        batched_input.append(marker)
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=("\n".join(batched_input) + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    grouped_outputs: List[List[str]] = []
    current_outputs: List[str] = []
    marker_index = 0
    for raw_line in proc.stdout.decode("utf-8").splitlines():
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        input_form, output = (raw_line.split("\t", 1) + [""])[:2]
        if marker_index >= len(markers):
            raise RuntimeError("Batch flookup produced more boundary markers than expected")
        if input_form == markers[marker_index]:
            grouped_outputs.append(dedupe_preserving_order(current_outputs))
            current_outputs = []
            marker_index += 1
            continue
        if output and output != "+?":
            current_outputs.append(output)
    if marker_index != len(markers):
        raise RuntimeError(
            f"Batch flookup boundary mismatch: saw {marker_index} markers for {len(markers)} input forms"
        )
    if len(grouped_outputs) != len(forms):
        raise RuntimeError(
            f"Batch flookup output mismatch: expected {len(forms)} rows, got {len(grouped_outputs)}"
        )
    return grouped_outputs


def build_evaluated_row(row: Dict[str, str], outputs: Sequence[str]) -> Dict[str, object]:
    expected = row["counterpart"]
    return {
        "lexical_item": row["concept"],
        "protoform": row["proto"],
        "proto_norm": row["proto_norm"],
        "fst_input": evaluation_input(row),
        "expected_counterpart": expected,
        "outputs": list(outputs),
        "outputs_text": format_outputs(outputs),
        "matches_expected": outputs_match_expected(outputs, expected),
        "notes": baseline_note(outputs, expected),
    }


def build_variant_appendix(order: Sequence[str], germanic_path: Path) -> str:
    """Foma appendix defining the variant production network.

    Only the experimental segment (Variant{EXPERIMENT_ROOT}) is
    hand-manipulated; every enclosing production define up to the root is
    mirrored mechanically from the live composition via oe_pipeline, so the
    tool survives adding/removing rules outside the experimental segment
    without edits here.
    """
    lines = [
        "",
        "# Variant Old English order generated by sound_change_order_sensitivity.py",
        f"define Variant{EXPERIMENT_ROOT} (",
    ]
    for index, rule in enumerate(order):
        prefix = "    " if index == 0 else "    .o. "
        lines.append(f"{prefix}{rule}")
    lines.append(");")
    variant_names = {EXPERIMENT_ROOT}
    chain = oe_pipeline.production_parent_chain(EXPERIMENT_ROOT, germanic_path)
    for ancestor in chain:
        members = oe_pipeline.composition_members_of(ancestor, germanic_path)
        rendered = [f"Variant{m}" if m in variant_names else m for m in members]
        lines.append("")
        lines.append(f"define Variant{ancestor} " + "\n    .o. ".join(rendered) + ";")
        variant_names.add(ancestor)
    root = chain[-1]
    lines.extend(
        [
            "",
            "clear stack",
            f"regex Variant{root};",
            "save stack old_english_variant.bin",
            "",
        ]
    )
    return "\n".join(lines)


def compile_variant(
    germanic_path: Path,
    sandbox_path: Path,
    variant_id: str,
    order: Sequence[str],
) -> Tuple[str, Path | None, str]:
    with tempfile.TemporaryDirectory(prefix=f"{variant_id}_") as temp_dir:
        tmpdir = Path(temp_dir)
        tmp_germanic = tmpdir / "germanic.txt"
        tmp_sandbox = tmpdir / "old_english_sandbox.txt"
        shutil.copy2(germanic_path, tmp_germanic)
        shutil.copy2(sandbox_path, tmp_sandbox)
        with tmp_germanic.open("a", encoding="utf-8") as handle:
            handle.write(build_variant_appendix(order, germanic_path))
        manifest = tmpdir / "variant_manifest.txt"
        manifest.write_text("\n".join(order) + "\n", encoding="utf-8")
        proc = subprocess.run(
            ["foma", "-f", str(tmp_germanic.name)],
            cwd=tmpdir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        variant_bin = tmpdir / "old_english_variant.bin"
        if proc.returncode != 0 or not variant_bin.exists():
            log_tail = "\n".join((proc.stdout + "\n" + proc.stderr).splitlines()[-12:]).strip()
            return ("compile_failed", None, log_tail or "foma exited without producing old_english_variant.bin")
        persisted_bin = tmpdir / f"{variant_id}.bin"
        shutil.copy2(variant_bin, persisted_bin)
        final_copy = germanic_path.parent.parent / ".tmp_order_sensitivity"
        final_copy.mkdir(parents=True, exist_ok=True)
        retained_bin = final_copy / f"{variant_id}.bin"
        shutil.copy2(persisted_bin, retained_bin)
        return ("compiled", retained_bin, "")


def cleanup_retained_bins(path: Path) -> None:
    if not path.exists():
        return
    path.unlink()
    parent = path.parent
    if parent.name == ".tmp_order_sensitivity" and parent.exists() and not any(parent.iterdir()):
        parent.rmdir()


def swap_adjacent(order: Sequence[str], target_rule: str, movement: str) -> Tuple[List[str], str]:
    if target_rule not in order:
        raise KeyError(f"Rule {target_rule} does not appear in the live EnglishProtoToOE chain")
    idx = order.index(target_rule)
    if movement == "earlier":
        if idx == 0:
            raise ValueError(f"Rule {target_rule} cannot move one step earlier")
        neighbor_idx = idx - 1
    else:
        if idx + 1 >= len(order):
            raise ValueError(f"Rule {target_rule} cannot move one step later")
        neighbor_idx = idx + 1
    variant_order = list(order)
    variant_order[idx], variant_order[neighbor_idx] = variant_order[neighbor_idx], variant_order[idx]
    return variant_order, order[neighbor_idx]


def unique_preview(rows: Iterable[Dict[str, object]], field: str, limit: int = 5) -> str:
    values = sorted({str(row[field]) for row in rows if row.get(field)})
    return "; ".join(values[:limit])


def variant_target_order(base_order: int, direction: str, steps: int) -> int:
    return base_order - steps if direction == "earlier" else base_order + steps


def historically_interpretable(entry_type: str) -> str:
    return "yes" if entry_type in {"historical_sound_change", "uncertain"} else "no"


def upsert_tsv(
    output_path: Path,
    fieldnames: Sequence[str],
    scope_fields: Sequence[str],
    scope_values: Sequence[Tuple[str, ...]],
    new_rows: Sequence[Dict[str, str]],
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    existing: List[Dict[str, str]] = []
    if output_path.exists():
        with output_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            existing.extend(reader)
    scope_set = set(scope_values)
    merged = [row for row in existing if tuple(row[field] for field in scope_fields) not in scope_set]
    merged.extend(new_rows)
    merged.sort(key=lambda row: tuple(row.get(field, "") for field in fieldnames))
    write_tsv(fieldnames, merged, output_path)


def first_break_summary_fieldnames() -> List[str]:
    return [
        "change_id",
        "display_name",
        "rule_name",
        "baseline_order",
        "direction",
        "result",
        "first_break_variant_id",
        "first_break_order",
        "crossed_change_id",
        "crossed_display_name",
        "crossed_rule_name",
        "crossed_entry_type",
        "variants_tested_before_break",
        "compilation_status",
        "total_rows_tested",
        "baseline_matches",
        "variant_matches_at_break",
        "changed_output_count_at_break",
        "newly_failing_count_at_break",
        "representative_changed_lexemes",
        "representative_new_failures",
        "historically_interpretable",
        "notes",
    ]


def first_break_changes_fieldnames() -> List[str]:
    return [
        "variant_id",
        "change_id",
        "display_name",
        "direction",
        "variant_order",
        "crossed_change_id",
        "crossed_display_name",
        "crossed_rule_name",
        "crossed_entry_type",
        "lexical_item",
        "protoform",
        "expected_counterpart",
        "baseline_output",
        "variant_output",
        "baseline_matches_expected",
        "variant_matches_expected",
        "status_change",
        "likely_break_stage_or_note",
    ]


def first_break_failures_fieldnames() -> List[str]:
    return [
        "variant_id",
        "change_id",
        "direction",
        "variant_order",
        "crossed_change_id",
        "crossed_display_name",
        "crossed_rule_name",
        "crossed_entry_type",
        "lexical_item",
        "protoform",
        "expected_counterpart",
        "baseline_output",
        "variant_output",
        "failure_type",
        "note",
    ]


def find_first_break_summary_row(summary_output: Path, change_id: str, direction: str) -> Dict[str, str] | None:
    for row in read_tsv_rows(summary_output):
        if row.get("change_id") == change_id and row.get("direction") == direction:
            return row
    return None


def parse_resume_steps(notes: str) -> int:
    match = RESUME_STEPS_RE.search(notes or "")
    return int(match.group(1)) if match else 0


def parse_last_safe_order(notes: str, fallback: int) -> int:
    match = LAST_SAFE_ORDER_RE.search(notes or "")
    return int(match.group(1)) if match else fallback


def move_rule_steps(order: Sequence[str], target_rule: str, direction: str, steps: int) -> List[str]:
    moved = list(order)
    for _ in range(steps):
        moved, _ = swap_adjacent(moved, target_rule, direction)
    return moved


def clear_first_break_direction_outputs(
    change_id: str,
    direction: str,
    summary_output: Path,
    changes_output: Path,
    failures_output: Path,
) -> None:
    scope = [(change_id, direction)]
    upsert_tsv(summary_output, first_break_summary_fieldnames(), ("change_id", "direction"), scope, [])
    upsert_tsv(changes_output, first_break_changes_fieldnames(), ("change_id", "direction"), scope, [])
    upsert_tsv(failures_output, first_break_failures_fieldnames(), ("change_id", "direction"), scope, [])


def write_first_break_variant_outputs(
    evaluation: Dict[str, object],
    changes_output: Path,
    failures_output: Path,
) -> None:
    variant_scope = [(str(evaluation["variant_id"]),)]
    upsert_tsv(
        changes_output,
        first_break_changes_fieldnames(),
        ("variant_id",),
        variant_scope,
        evaluation["changed_rows"],
    )
    upsert_tsv(
        failures_output,
        first_break_failures_fieldnames(),
        ("variant_id",),
        variant_scope,
        evaluation["failure_rows"],
    )


def status_change_label(baseline_match: bool, variant_match: bool, baseline_output: str, variant_output: str) -> str:
    if baseline_match and not variant_match:
        return "newly_failing"
    if (not baseline_match) and variant_match:
        return "newly_passing"
    if baseline_match and variant_match:
        return "changed_still_passing"
    if baseline_output == "+?" and variant_output != "+?":
        return "no_output_to_output"
    if baseline_output != "+?" and variant_output == "+?":
        return "output_to_no_output"
    return "changed_still_failing"


def evaluate_variant_against_baseline(
    *,
    variant_id: str,
    change: ChangeInfo,
    display_name: str,
    direction: str,
    variant_order: int,
    crossed: NeighborInfo,
    variant_order_chain: Sequence[str],
    rows: Sequence[Dict[str, str]],
    baseline_results: Sequence[Dict[str, object]],
    germanic_path: Path,
    sandbox_path: Path,
) -> Dict[str, object]:
    baseline_map = {result_key(row): row for row in baseline_results}
    baseline_stats = summarize_evaluation(baseline_results)
    compilation_status = "compiled"
    compile_note = ""
    variant_bin: Path | None = None
    try:
        compilation_status, variant_bin, compile_note = compile_variant(
            germanic_path=germanic_path,
            sandbox_path=sandbox_path,
            variant_id=variant_id,
            order=variant_order_chain,
        )
        if compilation_status == "compiled" and variant_bin is not None:
            variant_results = evaluate_rows(rows, variant_bin)
        else:
            variant_results = []
    finally:
        if variant_bin is not None:
            cleanup_retained_bins(variant_bin)
    variant_stats = summarize_evaluation(variant_results) if variant_results else {
        "total_rows_tested": len(rows),
        "matches_expected": 0,
        "fails_expected": len(rows),
        "no_output_rows": len(rows),
        "multi_output_rows": 0,
    }
    changed_rows: List[Dict[str, str]] = []
    failure_rows: List[Dict[str, str]] = []
    if variant_results:
        for variant_row in variant_results:
            baseline_row = baseline_map[result_key(variant_row)]
            if baseline_row["outputs_text"] == variant_row["outputs_text"]:
                continue
            status_change = status_change_label(
                bool(baseline_row["matches_expected"]),
                bool(variant_row["matches_expected"]),
                str(baseline_row["outputs_text"]),
                str(variant_row["outputs_text"]),
            )
            likely_note = (
                f"Crossing {crossed.rule_name} produced no output."
                if variant_row["outputs_text"] == "+?"
                else f"Crossing {crossed.rule_name} changed the output."
            )
            changed_rows.append(
                {
                    "variant_id": variant_id,
                    "change_id": change.change_id,
                    "display_name": display_name,
                    "direction": direction,
                    "variant_order": str(variant_order),
                    "crossed_change_id": crossed.change_id,
                    "crossed_display_name": crossed.display_name,
                    "crossed_rule_name": crossed.rule_name,
                    "crossed_entry_type": crossed.entry_type,
                    "lexical_item": str(variant_row["lexical_item"]),
                    "protoform": str(variant_row["protoform"]),
                    "expected_counterpart": str(variant_row["expected_counterpart"]),
                    "baseline_output": str(baseline_row["outputs_text"]),
                    "variant_output": str(variant_row["outputs_text"]),
                    "baseline_matches_expected": "yes" if baseline_row["matches_expected"] else "no",
                    "variant_matches_expected": "yes" if variant_row["matches_expected"] else "no",
                    "status_change": status_change,
                    "likely_break_stage_or_note": likely_note,
                }
            )
            if baseline_row["matches_expected"] and not variant_row["matches_expected"]:
                failure_rows.append(
                    {
                        "variant_id": variant_id,
                        "change_id": change.change_id,
                        "direction": direction,
                        "variant_order": str(variant_order),
                        "crossed_change_id": crossed.change_id,
                        "crossed_display_name": crossed.display_name,
                        "crossed_rule_name": crossed.rule_name,
                        "crossed_entry_type": crossed.entry_type,
                        "lexical_item": str(variant_row["lexical_item"]),
                        "protoform": str(variant_row["protoform"]),
                        "expected_counterpart": str(variant_row["expected_counterpart"]),
                        "baseline_output": str(baseline_row["outputs_text"]),
                        "variant_output": str(variant_row["outputs_text"]),
                        "failure_type": "newly_failing",
                        "note": likely_note,
                    }
                )
    return {
        "variant_id": variant_id,
        "direction": direction,
        "variant_order": variant_order,
        "crossed": crossed,
        "compilation_status": compilation_status,
        "compile_note": compile_note,
        "variant_stats": variant_stats,
        "baseline_stats": baseline_stats,
        "changed_rows": changed_rows,
        "failure_rows": failure_rows,
        "real_break_found": bool(failure_rows),
    }


def run_adjacent_pilot(
    change: ChangeInfo,
    inventory_earlier: NeighborInfo | None,
    inventory_later: NeighborInfo | None,
    live_order: Sequence[str],
    rows: Sequence[Dict[str, str]],
    baseline_results: Sequence[Dict[str, object]],
    summary_output: Path,
    changes_output: Path,
    germanic_path: Path,
    sandbox_path: Path,
) -> List[Dict[str, str]]:
    summary_rows: List[Dict[str, str]] = []
    detail_rows: List[Dict[str, str]] = []
    stage_labels = {s.foma_identifier for s in oe_pipeline.named_stages()}
    for movement, inventory_neighbor in (("earlier", inventory_earlier), ("later", inventory_later)):
        variant_id = f"{change.change_id}_{movement}_adjacent"
        variant_order, chain_neighbor_rule = swap_adjacent(live_order, change.rule_name, movement)
        crossed = inventory_neighbor or placeholder_neighbor(chain_neighbor_rule, variant_target_order(change.inventory_order, movement, 1))
        evaluation = evaluate_variant_against_baseline(
            variant_id=variant_id,
            change=change,
            display_name=change.display_name,
            direction=movement,
            variant_order=variant_target_order(change.inventory_order, movement, 1),
            crossed=crossed,
            variant_order_chain=variant_order,
            rows=rows,
            baseline_results=baseline_results,
            germanic_path=germanic_path,
            sandbox_path=sandbox_path,
        )
        compilation_status = str(evaluation["compilation_status"])
        compile_note = str(evaluation["compile_note"])
        variant_stats = evaluation["variant_stats"]
        changed_rows = evaluation["changed_rows"]
        newly_failing = evaluation["failure_rows"]
        chain_vs_inventory_note = ""
        if inventory_neighbor and inventory_neighbor.rule_name != chain_neighbor_rule:
            chain_vs_inventory_note = (
                f"inventory neighbor {inventory_neighbor.rule_name} differs from live-chain neighbor {chain_neighbor_rule}"
            )
        elif inventory_neighbor and inventory_neighbor.rule_name not in stage_labels:
            chain_vs_inventory_note = f"inventory neighbor {inventory_neighbor.rule_name} is not a sandbox stage label"
        notes = [note for note in [compile_note, chain_vs_inventory_note] if note]
        if inventory_neighbor and inventory_neighbor.entry_type != "historical_sound_change":
            notes.append(f"swapped across non-historical neighbor {inventory_neighbor.change_id}")
        summary_rows.append(
            {
                "variant_id": variant_id,
                "change_id": change.change_id,
                "display_name": change.display_name,
                "movement": movement,
                "swapped_with_change_id": inventory_neighbor.change_id if inventory_neighbor else "",
                "swapped_with_display_name": inventory_neighbor.display_name if inventory_neighbor else chain_neighbor_rule,
                "compilation_status": compilation_status,
                "total_rows_tested": str(variant_stats["total_rows_tested"]),
                "baseline_matches": str(evaluation["baseline_stats"]["matches_expected"]),
                "variant_matches": str(variant_stats["matches_expected"]),
                "changed_output_count": str(len(changed_rows)),
                "newly_failing_count": str(len(newly_failing)),
                "newly_passing_count": str(sum(1 for row in changed_rows if row["status_change"] == "newly_passing")),
                "no_output_count": str(variant_stats["no_output_rows"]),
                "representative_changed_lexemes": unique_preview(changed_rows, "lexical_item"),
                "representative_new_failures": unique_preview(newly_failing, "lexical_item"),
                "notes": "; ".join(notes) if notes else "-",
            }
        )
        detail_rows.extend(
            {
                key: str(value)
                for key, value in row.items()
            }
            for row in changed_rows
        )
    summary_fieldnames = [
        "variant_id",
        "change_id",
        "display_name",
        "movement",
        "swapped_with_change_id",
        "swapped_with_display_name",
        "compilation_status",
        "total_rows_tested",
        "baseline_matches",
        "variant_matches",
        "changed_output_count",
        "newly_failing_count",
        "newly_passing_count",
        "no_output_count",
        "representative_changed_lexemes",
        "representative_new_failures",
        "notes",
    ]
    detail_fieldnames = [
        "variant_id",
        "change_id",
        "movement",
        "swapped_with_change_id",
        "swapped_with_display_name",
        "swapped_with_rule_name",
        "lexical_item",
        "protoform",
        "expected_counterpart",
        "baseline_output",
        "variant_output",
        "baseline_matches_expected",
        "variant_matches_expected",
        "status_change",
        "likely_break_stage_or_note",
    ]
    variant_scopes = [(row["variant_id"],) for row in summary_rows]
    upsert_tsv(summary_output, summary_fieldnames, ("variant_id",), variant_scopes, summary_rows)
    upsert_tsv(changes_output, detail_fieldnames, ("variant_id",), variant_scopes, detail_rows)
    return summary_rows


def run_first_break(
    change: ChangeInfo,
    live_order: Sequence[str],
    rows: Sequence[Dict[str, str]],
    baseline_results: Sequence[Dict[str, object]],
    ordered_inventory: Sequence[ChangeInfo],
    summary_output: Path,
    changes_output: Path,
    failures_output: Path,
    germanic_path: Path,
    sandbox_path: Path,
    direction_mode: str,
    resume: bool,
) -> List[Dict[str, str]]:
    if change.rule_name not in live_order:
        raise RuntimeError(f"{change.rule_name} is not in the live EnglishProtoToOE chain")
    inventory_by_rule = inventory_rule_lookup(ordered_inventory)
    summary_rows: List[Dict[str, str]] = []
    baseline_stats = summarize_evaluation(baseline_results)
    directions = ("earlier", "later") if direction_mode == "both" else (direction_mode,)

    for direction in directions:
        existing_summary = find_first_break_summary_row(summary_output, change.change_id, direction)
        if resume and existing_summary and existing_summary.get("result") in FIRST_BREAK_DONE_RESULTS:
            summary_rows.append(existing_summary)
            print(
                f"{change.change_id} {direction} already_complete "
                f"result={existing_summary.get('result','-')} "
                f"first_break_variant={existing_summary.get('first_break_variant_id','-')}"
            )
            continue
        if not resume:
            clear_first_break_direction_outputs(change.change_id, direction, summary_output, changes_output, failures_output)
            existing_summary = None
        steps_completed = parse_resume_steps(existing_summary.get("notes", "")) if resume and existing_summary else 0
        safe_order = parse_last_safe_order(existing_summary.get("notes", ""), change.inventory_order) if resume and existing_summary else change.inventory_order
        current_chain = move_rule_steps(live_order, change.rule_name, direction, steps_completed) if steps_completed else list(live_order)
        latest_evaluation: Dict[str, object] | None = None

        while True:
            try:
                next_chain, crossed_rule_name = swap_adjacent(current_chain, change.rule_name, direction)
            except ValueError:
                latest_crossed = (
                    latest_evaluation["crossed"]
                    if latest_evaluation is not None
                    else placeholder_neighbor("-", safe_order)
                )
                final_row = {
                    "change_id": change.change_id,
                    "display_name": change.display_name,
                    "rule_name": change.rule_name,
                    "baseline_order": str(change.inventory_order),
                    "direction": direction,
                    "result": "no_break_before_boundary",
                    "first_break_variant_id": "-",
                    "first_break_order": "-",
                    "crossed_change_id": latest_crossed.change_id,
                    "crossed_display_name": latest_crossed.display_name,
                    "crossed_rule_name": latest_crossed.rule_name,
                    "crossed_entry_type": latest_crossed.entry_type,
                    "variants_tested_before_break": str(steps_completed),
                    "compilation_status": "compiled" if steps_completed else "-",
                    "total_rows_tested": str(
                        latest_evaluation["variant_stats"]["total_rows_tested"] if latest_evaluation is not None else len(rows)
                    ),
                    "baseline_matches": str(baseline_stats["matches_expected"]),
                    "variant_matches_at_break": str(
                        latest_evaluation["variant_stats"]["matches_expected"]
                        if latest_evaluation is not None
                        else baseline_stats["matches_expected"]
                    ),
                    "changed_output_count_at_break": str(len(latest_evaluation["changed_rows"]) if latest_evaluation is not None else 0),
                    "newly_failing_count_at_break": str(len(latest_evaluation["failure_rows"]) if latest_evaluation is not None else 0),
                    "representative_changed_lexemes": unique_preview(latest_evaluation["changed_rows"], "lexical_item") if latest_evaluation is not None else "",
                    "representative_new_failures": unique_preview(latest_evaluation["failure_rows"], "lexical_item") if latest_evaluation is not None else "",
                    "historically_interpretable": "no",
                    "notes": f"reached {direction} boundary with no real break; last_safe_order={safe_order}",
                }
                upsert_tsv(
                    summary_output,
                    first_break_summary_fieldnames(),
                    ("change_id", "direction"),
                    [(change.change_id, direction)],
                    [final_row],
                )
                summary_rows.append(final_row)
                print(
                    f"{change.change_id} {direction} result=no_break_before_boundary "
                    f"variants_tested={steps_completed} last_safe_order={safe_order}"
                )
                break

            current_steps = steps_completed + 1
            current_variant_order = variant_target_order(change.inventory_order, direction, current_steps)
            crossed = inventory_by_rule.get(crossed_rule_name) or placeholder_neighbor(crossed_rule_name, current_variant_order)
            evaluation = evaluate_variant_against_baseline(
                variant_id=f"{change.change_id}_{direction}_order_{current_variant_order}",
                change=change,
                display_name=change.display_name,
                direction=direction,
                variant_order=current_variant_order,
                crossed=crossed,
                variant_order_chain=next_chain,
                rows=rows,
                baseline_results=baseline_results,
                germanic_path=germanic_path,
                sandbox_path=sandbox_path,
            )
            write_first_break_variant_outputs(evaluation, changes_output, failures_output)
            latest_evaluation = evaluation
            if evaluation["compilation_status"] != "compiled":
                final_row = {
                    "change_id": change.change_id,
                    "display_name": change.display_name,
                    "rule_name": change.rule_name,
                    "baseline_order": str(change.inventory_order),
                    "direction": direction,
                    "result": "compile_failure",
                    "first_break_variant_id": str(evaluation["variant_id"]),
                    "first_break_order": str(evaluation["variant_order"]),
                    "crossed_change_id": crossed.change_id,
                    "crossed_display_name": crossed.display_name,
                    "crossed_rule_name": crossed.rule_name,
                    "crossed_entry_type": crossed.entry_type,
                    "variants_tested_before_break": str(current_steps),
                    "compilation_status": str(evaluation["compilation_status"]),
                    "total_rows_tested": str(evaluation["variant_stats"]["total_rows_tested"]),
                    "baseline_matches": str(baseline_stats["matches_expected"]),
                    "variant_matches_at_break": str(evaluation["variant_stats"]["matches_expected"]),
                    "changed_output_count_at_break": str(len(evaluation["changed_rows"])),
                    "newly_failing_count_at_break": str(len(evaluation["failure_rows"])),
                    "representative_changed_lexemes": unique_preview(evaluation["changed_rows"], "lexical_item"),
                    "representative_new_failures": unique_preview(evaluation["failure_rows"], "lexical_item"),
                    "historically_interpretable": "no",
                    "notes": str(evaluation["compile_note"]) or "compile failure before first real break",
                }
                upsert_tsv(
                    summary_output,
                    first_break_summary_fieldnames(),
                    ("change_id", "direction"),
                    [(change.change_id, direction)],
                    [final_row],
                )
                summary_rows.append(final_row)
                print(
                    f"{change.change_id} {direction} variant={evaluation['variant_id']} "
                    f"status={evaluation['compilation_status']}"
                )
                break
            if evaluation["real_break_found"]:
                final_row = {
                    "change_id": change.change_id,
                    "display_name": change.display_name,
                    "rule_name": change.rule_name,
                    "baseline_order": str(change.inventory_order),
                    "direction": direction,
                    "result": "first_break_found",
                    "first_break_variant_id": str(evaluation["variant_id"]),
                    "first_break_order": str(evaluation["variant_order"]),
                    "crossed_change_id": crossed.change_id,
                    "crossed_display_name": crossed.display_name,
                    "crossed_rule_name": crossed.rule_name,
                    "crossed_entry_type": crossed.entry_type,
                    "variants_tested_before_break": str(current_steps),
                    "compilation_status": str(evaluation["compilation_status"]),
                    "total_rows_tested": str(evaluation["variant_stats"]["total_rows_tested"]),
                    "baseline_matches": str(baseline_stats["matches_expected"]),
                    "variant_matches_at_break": str(evaluation["variant_stats"]["matches_expected"]),
                    "changed_output_count_at_break": str(len(evaluation["changed_rows"])),
                    "newly_failing_count_at_break": str(len(evaluation["failure_rows"])),
                    "representative_changed_lexemes": unique_preview(evaluation["changed_rows"], "lexical_item"),
                    "representative_new_failures": unique_preview(evaluation["failure_rows"], "lexical_item"),
                    "historically_interpretable": historically_interpretable(crossed.entry_type),
                    "notes": (
                        "first real break found"
                        if historically_interpretable(crossed.entry_type) == "yes"
                        else f"first real break crosses non-historical stage {crossed.change_id or crossed.rule_name}"
                    ),
                }
                upsert_tsv(
                    summary_output,
                    first_break_summary_fieldnames(),
                    ("change_id", "direction"),
                    [(change.change_id, direction)],
                    [final_row],
                )
                summary_rows.append(final_row)
                print(
                    f"{change.change_id} {direction} variant={evaluation['variant_id']} "
                    f"status=compiled changed={len(evaluation['changed_rows'])} "
                    f"new_failures={len(evaluation['failure_rows'])} result=first_break_found"
                )
                break

            safe_order = current_variant_order
            steps_completed = current_steps
            current_chain = next_chain
            progress_row = {
                "change_id": change.change_id,
                "display_name": change.display_name,
                "rule_name": change.rule_name,
                "baseline_order": str(change.inventory_order),
                "direction": direction,
                "result": "in_progress",
                "first_break_variant_id": "-",
                "first_break_order": "-",
                "crossed_change_id": crossed.change_id,
                "crossed_display_name": crossed.display_name,
                "crossed_rule_name": crossed.rule_name,
                "crossed_entry_type": crossed.entry_type,
                "variants_tested_before_break": str(steps_completed),
                "compilation_status": str(evaluation["compilation_status"]),
                "total_rows_tested": str(evaluation["variant_stats"]["total_rows_tested"]),
                "baseline_matches": str(baseline_stats["matches_expected"]),
                "variant_matches_at_break": str(evaluation["variant_stats"]["matches_expected"]),
                "changed_output_count_at_break": str(len(evaluation["changed_rows"])),
                "newly_failing_count_at_break": str(len(evaluation["failure_rows"])),
                "representative_changed_lexemes": unique_preview(evaluation["changed_rows"], "lexical_item"),
                "representative_new_failures": unique_preview(evaluation["failure_rows"], "lexical_item"),
                "historically_interpretable": historically_interpretable(crossed.entry_type),
                "notes": (
                    f"in_progress resume_steps={steps_completed} last_safe_order={safe_order} "
                    f"last_tested_variant={evaluation['variant_id']}"
                ),
            }
            upsert_tsv(
                summary_output,
                first_break_summary_fieldnames(),
                ("change_id", "direction"),
                [(change.change_id, direction)],
                [progress_row],
            )
            summary_rows.append(progress_row)
            print(
                f"{change.change_id} {direction} variant={evaluation['variant_id']} "
                f"status=compiled changed={len(evaluation['changed_rows'])} "
                f"new_failures={len(evaluation['failure_rows'])}"
            )
    return summary_rows


def identity_status_note(live_row: Dict[str, object], variant_row: Dict[str, object]) -> str:
    if live_row["outputs_text"] == variant_row["outputs_text"]:
        return "identical"
    if live_row["matches_expected"] == variant_row["matches_expected"]:
        return "output_diff_same_match_state"
    return "output_diff_changes_match_state"


def run_identity_variant(
    live_order: Sequence[str],
    rows: Sequence[Dict[str, str]],
    baseline_results: Sequence[Dict[str, object]],
    output_path: Path,
    germanic_path: Path,
    sandbox_path: Path,
) -> Dict[str, int | str]:
    compilation_status, variant_bin, compile_note = compile_variant(
        germanic_path=germanic_path,
        sandbox_path=sandbox_path,
        variant_id="identity_variant_02",
        order=live_order,
    )
    if compilation_status != "compiled" or variant_bin is None:
        raise RuntimeError(compile_note or "identity variant did not compile")
    try:
        variant_results = evaluate_rows(rows, variant_bin)
    finally:
        cleanup_retained_bins(variant_bin)
    baseline_map = {result_key(row): row for row in baseline_results}
    identity_rows: List[Dict[str, str]] = []
    identical_rows = 0
    differing_rows = 0
    identity_matches = 0
    for variant_row in variant_results:
        baseline_row = baseline_map[result_key(variant_row)]
        identical = baseline_row["outputs_text"] == variant_row["outputs_text"]
        if identical:
            identical_rows += 1
        else:
            differing_rows += 1
        if variant_row["matches_expected"]:
            identity_matches += 1
        identity_rows.append(
            {
                "lexical_item": str(variant_row["lexical_item"]),
                "protoform": str(variant_row["protoform"]),
                "expected_counterpart": str(variant_row["expected_counterpart"]),
                "live_output": str(baseline_row["outputs_text"]),
                "identity_variant_output": str(variant_row["outputs_text"]),
                "live_matches_expected": "yes" if baseline_row["matches_expected"] else "no",
                "identity_variant_matches_expected": "yes" if variant_row["matches_expected"] else "no",
                "output_identical": "yes" if identical else "no",
                "status_note": identity_status_note(baseline_row, variant_row),
            }
        )
    fieldnames = [
        "lexical_item",
        "protoform",
        "expected_counterpart",
        "live_output",
        "identity_variant_output",
        "live_matches_expected",
        "identity_variant_matches_expected",
        "output_identical",
        "status_note",
    ]
    write_tsv(fieldnames, identity_rows, output_path)
    return {
        "total_rows_tested": len(identity_rows),
        "output_identical_rows": identical_rows,
        "differing_rows": differing_rows,
        "live_matches": sum(1 for row in baseline_results if row["matches_expected"]),
        "identity_matches": identity_matches,
        "output_path": str(output_path),
    }


def ensure_canonical_bin_fresh(bin_path: Path, allow_stale: bool) -> None:
    """Fail closed when the canonical runtime bin does not correspond to the
    current sources (build manifest contract). Explicit noncanonical --bin
    overrides are permitted but flagged as noncanonical provenance."""
    canonical = repo_paths()["live_bin"].resolve()
    if bin_path != canonical:
        print(f"NONCANONICAL BIN: {bin_path} is not the canonical runtime bin "
              f"({canonical}); results have debug provenance only.",
              file=sys.stderr)
        return
    if allow_stale:
        print("WARNING: --allow-stale-bin set; skipping build-manifest "
              "freshness check (debug provenance only).", file=sys.stderr)
        return
    problems = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    if problems:
        for problem in problems:
            print(f"STALE RUNTIME BINS: {problem}", file=sys.stderr)
        raise SystemExit(
            "canonical runtime bins do not match the current sources; rebuild "
            "them first (python3 Germanic/tools/adjudicate.py SCNNN --evidence "
            "or bash Germanic/tools/rebuild_oe_bins.sh), or pass "
            "--allow-stale-bin for a debug run.")


def main() -> None:
    args = parse_args()
    inventory_path = Path(args.inventory).expanduser().resolve()
    germanic_path = Path(args.germanic).expanduser().resolve()
    sandbox_path = Path(args.sandbox).expanduser().resolve()
    tsv_path = Path(args.tsv).expanduser().resolve()
    bin_path = Path(args.bin).expanduser().resolve()
    baseline_output = Path(args.baseline_output).expanduser().resolve()
    identity_output = Path(args.identity_output).expanduser().resolve()
    summary_output = Path(args.summary_output).expanduser().resolve()
    changes_output = Path(args.changes_output).expanduser().resolve()
    first_break_output = Path(args.first_break_output).expanduser().resolve()
    first_break_changes_output = Path(args.first_break_changes_output).expanduser().resolve()
    first_break_failures_output = Path(args.first_break_failures_output).expanduser().resolve()
    ensure_expanded_pwgmc_outputs_are_separate(
        order_profile=args.order_profile,
        dry_run_order=args.dry_run_order,
        first_break_output=first_break_output,
        first_break_changes_output=first_break_changes_output,
        first_break_failures_output=first_break_failures_output,
    )

    inventory_by_id, ordered_inventory = load_inventory(
        inventory_path, registry_fst_identifiers(repo_paths()["registry"]),
        archival_inventory_orders(repo_paths()["archival_orders"]))

    def focal_change(sc_id: str) -> ChangeInfo:
        if sc_id not in inventory_by_id:
            raise SystemExit(f"{sc_id}: not in the sound-change inventory")
        info = inventory_by_id[sc_id]
        if not info.rule_name:
            raise SystemExit(
                f"{sc_id}: no fst_identifier in sc_registry.tsv; the registry "
                "is the canonical SC -> FST identity authority, so this entry "
                "cannot be an order-sensitivity experiment target")
        return info

    live_order = parse_english_proto_to_oe_order(germanic_path)
    first_break_order = resolve_first_break_order_profile(live_order, args.order_profile, germanic_path)

    if args.mode == "first-break" and args.dry_run_order:
        change = focal_change(args.change)
        print_order_profile(first_break_order, args.order_profile, change, ordered_inventory)
        return

    ensure_canonical_bin_fresh(bin_path, args.allow_stale_bin)

    if args.mode == "validate-batch":
        rows = load_rows(tsv_path)
        batch_validation = validate_batch_outputs(rows, bin_path)
        print(
            "validate_batch "
            f"rows={batch_validation['rows']} "
            f"matching_rows={batch_validation['matching_rows']} "
            f"differing_rows={batch_validation['differing_rows']}"
        )
        for mismatch in batch_validation["mismatches"][:5]:
            print(
                "mismatch "
                f"lexical_item={mismatch['lexical_item']} "
                f"protoform={mismatch['protoform']} "
                f"rowwise={mismatch['rowwise_output']} "
                f"batch={mismatch['batch_output']}"
            )
        if batch_validation["differing_rows"]:
            raise SystemExit(1)
        return

    rows = load_rows(tsv_path)
    baseline_results = evaluate_rows(rows, bin_path)
    baseline_stats = summarize_evaluation(baseline_results)

    if args.mode == "baseline":
        write_baseline_tsv(baseline_results, baseline_output)
        print(
            "baseline "
            f"rows={baseline_stats['total_rows_tested']} "
            f"matches={baseline_stats['matches_expected']} "
            f"fails={baseline_stats['fails_expected']} "
            f"no_output={baseline_stats['no_output_rows']} "
            f"multi_output={baseline_stats['multi_output_rows']} "
            f"output={baseline_output}"
        )
        return

    if args.mode == "identity-variant":
        identity_stats = run_identity_variant(
            live_order=live_order,
            rows=rows,
            baseline_results=baseline_results,
            output_path=identity_output,
            germanic_path=germanic_path,
            sandbox_path=sandbox_path,
        )
        print(
            "identity_variant "
            f"rows={identity_stats['total_rows_tested']} "
            f"identical={identity_stats['output_identical_rows']} "
            f"differing={identity_stats['differing_rows']} "
            f"live_matches={identity_stats['live_matches']} "
            f"identity_matches={identity_stats['identity_matches']} "
            f"output={identity_stats['output_path']}"
        )
        if identity_stats["differing_rows"]:
            raise SystemExit(1)
        return

    change = focal_change(args.change)
    if args.mode == "first-break":
        run_first_break(
            change=change,
            live_order=first_break_order,
            rows=rows,
            baseline_results=baseline_results,
            ordered_inventory=ordered_inventory,
            summary_output=first_break_output,
            changes_output=first_break_changes_output,
            failures_output=first_break_failures_output,
            germanic_path=germanic_path,
            sandbox_path=sandbox_path,
            direction_mode=args.direction,
            resume=args.resume,
        )
        return

    earlier, later = neighbors_for_change(change.change_id, ordered_inventory)
    summary_rows = run_adjacent_pilot(
        change=change,
        inventory_earlier=earlier,
        inventory_later=later,
        live_order=live_order,
        rows=rows,
        baseline_results=baseline_results,
        summary_output=summary_output,
        changes_output=changes_output,
        germanic_path=germanic_path,
        sandbox_path=sandbox_path,
    )
    for row in summary_rows:
        print(
            f"{row['variant_id']} status={row['compilation_status']} "
            f"changed={row['changed_output_count']} "
            f"new_failures={row['newly_failing_count']} "
            f"variant_matches={row['variant_matches']}"
        )


if __name__ == "__main__":
    main()
