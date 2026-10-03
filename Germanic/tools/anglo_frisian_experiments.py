#!/usr/bin/env python3
"""Read-only research experiments; execute Foma only in the backend container."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import oe_pipeline
from capr_runtime import check_build_manifest, layout
from sound_change_order_sensitivity import (
    batch_apply_down,
    build_variant_appendix,
    expand_pwgmc_changes,
    parse_english_proto_to_oe_order,
)


def load_recipes(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("recipes"), list):
        raise ValueError("unsupported experiment recipe schema")
    ids = set()
    for recipe in data["recipes"]:
        if not isinstance(recipe, dict):
            raise ValueError("recipe must be an object")
        required = {"id", "description", "definitions", "insert_after", "insert_rule", "replace",
                    "sources", "assumptions", "limitations"}
        if not required <= set(recipe) or set(recipe) - required - {"input_overrides", "component_checks"} or not all(
            isinstance(recipe[key], str) for key in required - {"sources", "replace"}
        ):
            raise ValueError("invalid experiment recipe fields")
        if not isinstance(recipe["replace"], dict) or not all(
            isinstance(key, str) and isinstance(value, str) for key, value in recipe["replace"].items()
        ):
            raise ValueError("replacement map must contain named components")
        name = recipe["id"]
        if not re.fullmatch(r"[a-z][a-z0-9-]*", name) or name in ids:
            raise ValueError(f"invalid/duplicate recipe ID: {name}")
        ids.add(name)
        definitions = recipe["definitions"]
        if re.search(r"\b(source|save|load|quit|system|clear|regex)\b", definitions):
            raise ValueError(f"{name}: definitions contain non-definition commands")
        overrides = recipe.get("input_overrides", [])
        if not isinstance(overrides, list):
            raise ValueError(f"{name}: input overrides must be a list")
        override_ids = set()
        for override in overrides:
            if not isinstance(override, dict) or set(override) != {
                "row_id", "baseline_input", "variant_input", "input_stage"
            } or not all(isinstance(value, str) and value for value in override.values()):
                raise ValueError(f"{name}: invalid input override fields")
            identifier = override["row_id"]
            if not identifier.isascii() or not identifier.isdecimal() or identifier in override_ids:
                raise ValueError(f"{name}: invalid/duplicate input override row ID: {identifier}")
            override_ids.add(identifier)
            if override["input_stage"] != "pgmc":
                raise ValueError(f"{name}: only PGmc input overrides support the full cascade")
            for field in ("baseline_input", "variant_input"):
                value = override[field]
                normalized = oe_pipeline.normalize_proto(value)
                if not value.startswith("*") or value[1:] != normalized or not normalized or not all(
                    char.isalpha() or char == "-" for char in normalized
                ):
                    raise ValueError(f"{name}: invalid {field} in input override")
            if override["baseline_input"] == override["variant_input"]:
                raise ValueError(f"{name}: input override must change the input")
        composition_edits = any(recipe[key] for key in ("definitions", "insert_rule", "insert_after", "replace"))
        component_checks = recipe.get("component_checks", [])
        if not isinstance(component_checks, list):
            raise ValueError(f"{name}: component checks must be a list")
        check_ids = set()
        for check in component_checks:
            if not isinstance(check, dict) or set(check) != {"id", "component", "input", "expected"} or not all(
                isinstance(value, str) and value for value in check.values()
            ):
                raise ValueError(f"{name}: invalid component check fields")
            if not re.fullmatch(r"[a-z][a-z0-9-]*", check["id"]) or check["id"] in check_ids:
                raise ValueError(f"{name}: invalid/duplicate component check ID")
            check_ids.add(check["id"])
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", check["component"]):
                raise ValueError(f"{name}: invalid component name")
            for field in ("input", "expected"):
                value = check[field]
                if not value.startswith("*") or not any(char.isalpha() for char in value) or not all(
                    char.isalpha() or char in "*-" for char in value
                ):
                    raise ValueError(f"{name}: invalid component {field}")
        if name == "identity":
            if composition_edits or overrides or component_checks or recipe["sources"]:
                raise ValueError("identity recipe must make no scientific intervention")
        else:
            if not recipe["sources"] or not (composition_edits or overrides or component_checks):
                raise ValueError(f"{name}: scientific intervention must cite sources")
            if composition_edits:
                rule = recipe["insert_rule"]
                if not re.fullmatch(r"AF[A-Za-z0-9]{1,12}", rule) or not recipe["insert_after"]:
                    raise ValueError(f"{name}: missing/invalid relative insertion")
                if not re.fullmatch(r"(?:\s*define AF[A-Za-z0-9]{1,12}\s+\[[\s\S]*?\];)+\s*", definitions):
                    raise ValueError(f"{name}: expected short-name bracket definitions")
                declared = re.findall(r"\bdefine (AF[A-Za-z0-9]{1,12})\b", definitions)
                expected = {rule} | set(recipe["replace"].values())
                if len(declared) != len(set(declared)) or set(declared) != expected:
                    raise ValueError(f"{name}: definitions must match relative edits")
        if not isinstance(recipe["sources"], list):
            raise ValueError(f"{name}: sources must be a list")
        for source in recipe["sources"]:
            if not isinstance(source, dict) or set(source) != {"key", "pages"} or not all(
                isinstance(source[key], str) and source[key] for key in ("key", "pages")
            ):
                raise ValueError(f"{name}: invalid source key/pages")
            for span in source["pages"].split(","):
                match = re.fullmatch(r"([1-9]\d*)(?:-([1-9]\d*))?", span)
                if not match or int(match[1]) > int(match[2] or match[1]):
                    raise ValueError(f"{name}: missing/invalid source pages")
    if "identity" not in ids:
        raise ValueError("identity control is required")
    probes = data.get("probes")
    if not isinstance(probes, list) or not probes:
        raise ValueError("intermediate probes are required")
    probe_ids = set()
    for probe in probes:
        if not isinstance(probe, dict) or set(probe) != {"id", "stage", "side"} or not all(
            isinstance(probe[key], str) and probe[key] for key in ("id", "stage", "side")
        ) or probe["side"] not in {"before", "after"}:
            raise ValueError("invalid intermediate probe")
        if not re.fullmatch(r"[a-z][a-z0-9_]*", probe["id"]) or probe["id"] in probe_ids:
            raise ValueError("invalid/duplicate intermediate probe ID")
        probe_ids.add(probe["id"])
    return data


def inserted_order(order: list[str], recipe: dict) -> list[str]:
    if not recipe["insert_rule"]:
        return list(order)
    anchor, rule = recipe["insert_after"], recipe["insert_rule"]
    if order.count(anchor) != 1 or rule in order:
        raise ValueError(f"{recipe['id']}: insertion anchor must be unique and new rule absent")
    index = order.index(anchor) + 1
    result = order[:index] + [rule] + order[index:]
    for original, replacement in recipe["replace"].items():
        if result.count(original) != 1 or replacement in result:
            raise ValueError(f"{recipe['id']}: replacement target must be unique and new name absent")
        result[result.index(original)] = replacement
    return result


def corpus_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        source = list(csv.DictReader(handle, delimiter="\t"))
    selected = [row for row in source if row.get("DOCULECT") == "Old_English"
                and row.get("PROTOFORM", "").strip()
                and row.get("COUNTERPART", "").strip() not in {"", "-"}]
    rows = []
    ids = set()
    for row in selected:
        identifier = row.get("ID", "")
        if not identifier or identifier in ids:
            raise ValueError(f"missing/duplicate stable OE row ID: {identifier}")
        ids.add(identifier)
        normalized = oe_pipeline.normalize_proto(row["PROTOFORM"])
        if not normalized:
            raise ValueError(f"{identifier}: empty normalized selected input")
        rows.append({"id": identifier, "concept": row["CONCEPT"], "reconstruction": row.get("PROTO", ""),
                     "proto": row["PROTOFORM"],
                     "proto_norm": normalized, "counterpart": row["COUNTERPART"]})
    if [row["proto_norm"] for row in rows] != [row["proto_norm"] for row in oe_pipeline.load_rows(path)]:
        raise ValueError("stable-ID corpus selection disagrees with oe_pipeline.load_rows")
    return rows


def apply_input_overrides(rows: list[dict[str, str]], recipe: dict) -> list[dict[str, str]]:
    modified = {row["id"]: dict(row) for row in rows}
    for override in recipe.get("input_overrides", []):
        identifier = override["row_id"]
        row = modified.get(identifier)
        if row is None:
            raise ValueError(f"{identifier}: input override row missing from selected OE corpus")
        if row["proto"] != override["baseline_input"]:
            raise ValueError(f"{identifier}: input override baseline disagrees with live selected input")
        if row["reconstruction"] != row["proto"]:
            raise ValueError(f"{identifier}: override currently requires PROTOFORM == PROTO; "
                             "separately staged inputs need explicit support")
        row["proto"] = override["variant_input"]
        row["proto_norm"] = oe_pipeline.normalize_proto(row["proto"])
    return [modified[row["id"]] for row in rows]


def probe_appendix(recipe: dict, probes: list[dict]) -> tuple[str, dict[str, str]]:
    original = [
        stage.inline_text if stage.kind == "inline" else stage.foma_identifier
        for stage in oe_pipeline.stages()
    ]
    order = inserted_order(original, recipe)
    lines, bins = [], {}
    for number, probe in enumerate(probes):
        stage = probe["stage"]
        if stage == "$inserted":
            stage = recipe["insert_rule"] or "PWGmcCoronalWAssimilation"
        stage = recipe["replace"].get(stage, stage)
        if order.count(stage) != 1:
            raise ValueError(f"probe stage missing or duplicated: {stage}")
        endpoint = order.index(stage) + (probe["side"] == "after")
        if endpoint == 0:
            raise ValueError(f"empty probe composition: {probe['id']}")
        name, filename = f"AFT{number:02d}", f"af_probe_{number:02d}.bin"
        lines.extend([f"define {name} " + "\n    .o. ".join(order[:endpoint]) + ";",
                      "clear stack", f"regex {name};", f"save stack {filename}"])
        bins[probe["id"]] = filename
    return "\n".join(lines), bins


def compile_isolated(source: Path, recipe: dict, probes: list[dict], directory: Path) -> dict[str, Path]:
    source_text = source.read_text(encoding="utf-8")
    for command, filename in re.findall(r"(?m)^\s*(save stack|source)\s+([^;\n]+)", source_text):
        path = Path(filename.strip())
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"unsafe {command} destination in source: {filename}")
        if command == "source":
            raise ValueError("new source includes require explicit isolated-copy support")
    base = parse_english_proto_to_oe_order(source)
    expanded = expand_pwgmc_changes(base, source)
    order = inserted_order(expanded, recipe)
    probe_text, bins = probe_appendix(recipe, probes)
    component_lines = []
    components = sorted({check["component"] for check in recipe.get("component_checks", [])})
    for number, component in enumerate(components):
        filename = f"af_component_{number:02d}.bin"
        component_lines.extend(["clear stack", f"regex {component};", f"save stack {filename}"])
        bins[f"component:{component}"] = filename
    script = directory / "experiment.foma"
    script.write_text(
        source_text + "\n" + recipe["definitions"] + "\n"
        + build_variant_appendix(order, source) + "\n" + probe_text + "\n"
        + "\n".join(component_lines) + "\nquit\n",
        encoding="utf-8",
    )
    result = subprocess.run(["foma", "-q", "-f", script.name], cwd=directory,
                            capture_output=True, text=True, timeout=600)
    log = result.stdout + "\n" + result.stderr
    if result.returncode or re.search(r"(?im)\b(error|syntax error|not defined)\b", log):
        raise RuntimeError("isolated Foma compilation failed:\n" + log[-6000:])
    outputs = {"final": directory / "old_english_variant.bin"}
    outputs.update({name: directory / filename for name, filename in bins.items()})
    missing = [str(path) for path in outputs.values() if not path.is_file() or path.stat().st_size == 0]
    if missing:
        raise RuntimeError(f"isolated compiler did not produce required bins: {missing}")
    return outputs


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def intermediate_outputs(bins: dict[str, Path], forms: list[str]) -> dict[str, list[list[str]]]:
    return {name: batch_apply_down(path, forms)
            for name, path in bins.items() if name != "final" and not name.startswith("component:")}


def check_component_predictions(recipe: dict, bins: dict[str, Path]) -> list[dict]:
    checked = []
    for check in recipe.get("component_checks", []):
        outputs = batch_apply_down(bins[f"component:{check['component']}"], [check["input"]])[0]
        if outputs != [check["expected"]]:
            raise ValueError(f"{check['id']}: component prediction {[check['expected']]!r} != {outputs!r}")
        checked.append({**check, "outputs": outputs})
    return checked


def check_fixture_predictions(report: dict, fixtures: list[dict[str, str]]) -> list[str]:
    rows = {row["id"]: row for row in report["rows"]}
    checked = []
    for fixture in fixtures:
        if fixture["recipe"] != report["recipe"]["id"]:
            continue
        identifier = fixture["fixture_id"]
        row = rows.get(fixture["row_id"])
        if row is None:
            raise ValueError(f"{identifier}: fixture row missing from experiment")
        state = row["intermediates"].get(fixture["probe"])
        if state is None:
            raise ValueError(f"{identifier}: fixture probe missing from experiment")
        for side in ("baseline", "variant"):
            expected = [fixture[f"{side}_prediction"]]
            if state[side] != expected:
                raise ValueError(f"{identifier}: {side} prediction {expected!r} != {state[side]!r}")
        checked.append(identifier)
    return checked


def run(recipe_data: dict, requested: str) -> dict:
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("execute experiments inside the backend container; host Foma is prohibited")
    if not shutil.which("foma") or not shutil.which("flookup"):
        raise RuntimeError("backend container lacks foma/flookup")
    for field, path in (("baseline_fst_sha256", runtime.germanic_fst),
                        ("baseline_corpus_sha256", runtime.corpus_tsv)):
        if field in recipe_data and recipe_data[field] != digest(path):
            raise ValueError("historical recipe baseline changed; preserve the recorded "
                             "experiment and prepare a new current-baseline recipe")
    manifest_errors = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if manifest_errors:
        raise RuntimeError("canonical build provenance is stale: " + "; ".join(manifest_errors))
    recipes = {recipe["id"]: recipe for recipe in recipe_data["recipes"]}
    if requested not in recipes:
        raise ValueError(f"unknown recipe: {requested}")
    protected = [runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
                 runtime.build_manifest, runtime.bin_dir / "old_english.bin"]
    protected.extend(runtime.bin_dir / name for name in oe_pipeline.expected_snapshot_bins())
    before = {str(path): digest(path) for path in protected}
    rows = corpus_rows(runtime.corpus_tsv)
    forms = [row["proto_norm"] for row in rows]
    variant_rows = apply_input_overrides(rows, recipes[requested])
    variant_forms = [row["proto_norm"] for row in variant_rows]
    baseline = batch_apply_down(runtime.bin_dir / "old_english.bin", forms)
    if any(len(outputs) != 1 for outputs in baseline):
        raise RuntimeError("baseline has missing/ambiguous outputs; experiment cannot proceed")
    with tempfile.TemporaryDirectory(prefix="capr_af_identity_") as temporary:
        bins = compile_isolated(runtime.germanic_fst, recipes["identity"], recipe_data["probes"], Path(temporary))
        identity = batch_apply_down(bins["final"], forms)
        if identity != baseline:
            changed = [row["id"] for row, old, new in zip(rows, baseline, identity) if old != new]
            raise RuntimeError(f"identity control disagrees with live production rows: {changed}")
        if requested == "identity":
            variant = identity
            intermediate = intermediate_outputs(bins, forms)
            component_checks = check_component_predictions(recipes[requested], bins)
        else:
            with tempfile.TemporaryDirectory(prefix="capr_af_variant_") as variant_temporary:
                variant_bins = compile_isolated(runtime.germanic_fst, recipes[requested],
                                                recipe_data["probes"], Path(variant_temporary))
                variant = batch_apply_down(variant_bins["final"], variant_forms)
                intermediate = intermediate_outputs(variant_bins, variant_forms)
                component_checks = check_component_predictions(recipes[requested], variant_bins)
        baseline_intermediate = intermediate_outputs(bins, forms)
    after = {str(path): digest(path) for path in protected}
    changed_artifacts = [path for path, checksum in before.items() if after[path] != checksum]
    if changed_artifacts:
        raise RuntimeError("canonical artifacts changed during isolated experiment: "
                           + "; ".join(changed_artifacts))
    report_rows = []
    for index, row in enumerate(rows):
        old, new = baseline[index], variant[index]
        report_rows.append({
            **row, "baseline_outputs": old, "variant_outputs": new,
            "variant_proto": variant_rows[index]["proto"],
            "variant_proto_norm": variant_rows[index]["proto_norm"],
            "input_changed": row["proto_norm"] != variant_rows[index]["proto_norm"],
            "baseline_match": old == [row["counterpart"]], "variant_match": new == [row["counterpart"]],
            "changed": old != new,
            "intermediates": {name: {"baseline": baseline_intermediate[name][index], "variant": outputs[index]}
                              for name, outputs in intermediate.items()},
        })
    return {
        "recipe": recipes[requested], "canonical_protected_hashes": before,
        "selected_rows": len(rows), "identity_equal": True, "canonical_artifacts_unchanged": True,
        "baseline_mismatch_ids": [row["id"] for row in report_rows if not row["baseline_match"]],
        "variant_mismatch_ids": [row["id"] for row in report_rows if not row["variant_match"]],
        "missing_output_ids": [row["id"] for row in report_rows if not row["variant_outputs"]],
        "ambiguous_output_ids": [row["id"] for row in report_rows if len(row["variant_outputs"]) > 1],
        "changed_ids": [row["id"] for row in report_rows if row["changed"]],
        "input_changed_ids": [row["id"] for row in report_rows if row["input_changed"]],
        "checked_component_fixtures": component_checks,
        "rows": report_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recipe", required=True)
    parser.add_argument("--recipes", type=Path, default=layout().docs_dir /
                        "sound_changes/literature_dossiers/anglo_frisian/oe_experiment_recipes.json")
    args = parser.parse_args()
    try:
        report = run(load_recipes(args.recipes), args.recipe)
        with args.recipes.with_name("oe_diagnostic_fixtures.tsv").open(
            encoding="utf-8", newline=""
        ) as handle:
            fixtures = list(csv.DictReader(handle, delimiter="\t"))
        report["checked_fixture_ids"] = check_fixture_predictions(report, fixtures)
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        parser.exit(2, f"experiment failed: {error}\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["missing_output_ids"] or report["ambiguous_output_ids"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
