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
from oe_input_context import CITATION_CONTEXT, InputContext
from oe_input_context import METADATA_FILENAME
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
    fixture_file = data.get("fixture_file", "oe_diagnostic_fixtures.tsv")
    if not isinstance(fixture_file, str) or not re.fullmatch(r"[a-z][a-z0-9_]*\.tsv", fixture_file):
        raise ValueError("fixture_file must be a local TSV filename")
    for field in ("baseline_fst_sha256", "baseline_corpus_sha256",
                  "baseline_context_sha256", "baseline_context_helper_sha256"):
        if field in data and (not isinstance(data[field], str)
                              or not re.fullmatch(r"[0-9a-f]{64}", data[field])):
            raise ValueError(f"invalid {field}")
    ids = set()
    for recipe in data["recipes"]:
        if not isinstance(recipe, dict):
            raise ValueError("recipe must be an object")
        required = {"id", "description", "definitions", "insert_after", "insert_rule", "replace",
                    "sources", "assumptions", "limitations"}
        if not required <= set(recipe) or set(recipe) - required - {
            "input_overrides", "component_checks", "input_replacement", "phonetic_symbols",
            "citation_context", "context_overrides", "staged_checks", "context_audit",
        } or not all(
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
        symbols = recipe.get("phonetic_symbols", [])
        if (not isinstance(symbols, list)
                or not all(isinstance(symbol, str) and len(symbol) == 1
                           and symbol.isalpha() for symbol in symbols)
                or len(symbols) != len(set(symbols))):
            raise ValueError(f"{name}: phonetic symbols must be unique single-codepoint letters")
        if re.search(r"\b(source|save|load|quit|system|clear|regex)\b", definitions):
            raise ValueError(f"{name}: definitions contain non-definition commands")
        input_replacement = recipe.get("input_replacement", "")
        if not isinstance(input_replacement, str) or (
            input_replacement and not re.fullmatch(r"AF[A-Za-z0-9]{1,12}", input_replacement)
        ):
            raise ValueError(f"{name}: invalid input replacement")
        context = recipe.get("citation_context")
        if context is not None and context != {
            "word_stress": "stressed", "phonological_finality": "final",
        }:
            raise ValueError(f"{name}: citation context must explicitly select a stressed final word")
        context_overrides = recipe.get("context_overrides", [])
        if not isinstance(context_overrides, list):
            raise ValueError(f"{name}: context overrides must be a list")
        context_ids = set()
        for override in context_overrides:
            if not isinstance(override, dict) or set(override) != {
                "row_id", "baseline_input", "word_stress", "phonological_finality",
            } or not all(isinstance(value, str) and value for value in override.values()):
                raise ValueError(f"{name}: invalid context override fields")
            identifier = override["row_id"]
            if not identifier.isascii() or not identifier.isdecimal() or identifier in context_ids:
                raise ValueError(f"{name}: invalid/duplicate context row ID")
            context_ids.add(identifier)
            InputContext(override["word_stress"], override["phonological_finality"])
        if (context is not None or context_overrides) and not input_replacement:
            raise ValueError(f"{name}: context encoding requires an input replacement")
        if input_replacement and context is None:
            raise ValueError(f"{name}: input replacement requires an explicit citation context")
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
        staged_checks = recipe.get("staged_checks", [])
        if not isinstance(staged_checks, list):
            raise ValueError(f"{name}: staged checks must be a list")
        for check in staged_checks:
            if not isinstance(check, dict) or not {
                "id", "stage", "side", "input", "expected", "evidence",
            } <= set(check) or set(check) - {
                "id", "stage", "side", "input", "expected", "evidence", "stop_after",
            } or not all(isinstance(value, str) and value for value in check.values()):
                raise ValueError(f"{name}: invalid staged check fields")
            if not re.fullmatch(r"[a-z][a-z0-9-]*", check["id"]) or check["id"] in check_ids:
                raise ValueError(f"{name}: invalid/duplicate staged check ID")
            check_ids.add(check["id"])
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", check["stage"]) or check["side"] not in {
                "before", "after",
            }:
                raise ValueError(f"{name}: invalid staged entry checkpoint")
            if "stop_after" in check and not re.fullmatch(
                    r"[A-Za-z][A-Za-z0-9]*", check["stop_after"]):
                raise ValueError(f"{name}: invalid staged stopping checkpoint")
            if not check["input"].startswith("*") or not all(
                char.isalpha() or char in "*-" for char in check["input"]
            ):
                raise ValueError(f"{name}: invalid staged input")
        audit = recipe.get("context_audit")
        if audit is not None and (
            not isinstance(audit, dict) or set(audit) != {"component", "probe"}
            or not all(isinstance(value, str) and value for value in audit.values())
            or audit["component"] not in {check["component"] for check in component_checks}
            or (context is None and not (
                data.get("baseline_context_sha256") and data.get("baseline_context_helper_sha256")
            ))
        ):
            raise ValueError(f"{name}: context audit requires a checked component and explicit context")
        if context is not None and audit is None:
            raise ValueError(f"{name}: context encoding requires an explicit context audit checkpoint")
        if name == "identity":
            if (composition_edits or overrides or component_checks or recipe["sources"]
                    or input_replacement or symbols or context is not None or context_overrides or staged_checks or audit):
                raise ValueError("identity recipe must make no scientific intervention")
        else:
            if not recipe["sources"] or not (composition_edits or overrides or component_checks or staged_checks):
                raise ValueError(f"{name}: scientific intervention must cite sources")
            if composition_edits:
                rule = recipe["insert_rule"]
                if not re.fullmatch(r"AF[A-Za-z0-9]{1,12}", rule) or not recipe["insert_after"]:
                    raise ValueError(f"{name}: missing/invalid relative insertion")
                if not re.fullmatch(r"(?:\s*define AF[A-Za-z0-9]{1,12}\s+\[[\s\S]*?\];)+\s*", definitions):
                    raise ValueError(f"{name}: expected short-name bracket definitions")
                declared = re.findall(r"\bdefine (AF[A-Za-z0-9]{1,12})\b", definitions)
                if any(
                    identifier == "AFContextRoot" or (
                        input_replacement and re.fullmatch(r"AFK\d{3}", identifier))
                    for identifier in declared
                ):
                    raise ValueError(f"{name}: definition collides with generated context wrappers")
                expected = {rule} | set(recipe["replace"].values())
                if input_replacement:
                    expected.add(input_replacement)
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
    for recipe in data["recipes"]:
        if recipe.get("context_audit") and recipe["context_audit"]["probe"] not in probe_ids:
            raise ValueError(f"{recipe['id']}: context audit probe missing")
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
    contextual = {row["row_id"]: row for row in oe_pipeline.load_rows(path)}
    ids = set()
    for row in selected:
        identifier = row.get("ID", "")
        if not identifier or identifier in ids:
            raise ValueError(f"missing/duplicate stable OE row ID: {identifier}")
        ids.add(identifier)
        normalized = oe_pipeline.normalize_proto(row["PROTOFORM"])
        if not normalized:
            raise ValueError(f"{identifier}: empty normalized selected input")
        rows.append({**contextual[identifier], "id": identifier,
                     "reconstruction": row.get("PROTO", ""),
                     "input_context": {
                         "word_stress": contextual[identifier]["word_stress"],
                         "phonological_finality": contextual[identifier]["phonological_finality"],
                     }})
    if [row["proto_norm"] for row in rows] != [row["proto_norm"] for row in contextual.values()]:
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
        context = InputContext(
            row.get("word_stress", CITATION_CONTEXT.word_stress),
            row.get("phonological_finality", CITATION_CONTEXT.phonological_finality),
        )
        row["fst_input"] = context.encode(row["proto_norm"])
    return [modified[row["id"]] for row in rows]


def encode_context(form: str, context: dict) -> str:
    return InputContext(context["word_stress"], context["phonological_finality"]).encode(form)


def apply_context_overrides(rows: list[dict[str, str]], recipe: dict) -> list[dict[str, str]]:
    if "citation_context" not in recipe:
        return rows
    overrides = {context["row_id"]: context for context in recipe.get("context_overrides", [])}
    missing = set(overrides) - {row["id"] for row in rows}
    if missing:
        raise ValueError(f"context override rows missing: {sorted(missing)}")
    result = []
    for row in rows:
        context = overrides.get(row["id"], recipe["citation_context"])
        if "baseline_input" in context and context["baseline_input"] != row["proto"]:
            raise ValueError(f"{row['id']}: context override baseline disagrees with selected input")
        result.append({
            **row, "input_context": {
                key: context[key] for key in ("word_stress", "phonological_finality")
            }, "word_stress": context["word_stress"],
            "phonological_finality": context["phonological_finality"],
            "fst_input": encode_context(row["proto_norm"], context),
        })
    return result


def complete_variant_order(recipe: dict) -> list[str]:
    original = [
        stage.inline_text if stage.kind == "inline" else stage.foma_identifier
        for stage in oe_pipeline.stages()
    ]
    order = inserted_order(original, recipe)
    if recipe.get("input_replacement"):
        if order.count("EnglishProtoInput") != 1:
            raise ValueError("input replacement target must occur exactly once")
        order[order.index("EnglishProtoInput")] = recipe["input_replacement"]
    return order


def context_lifted_order(recipe: dict, order: list[str]) -> tuple[list[str], str]:
    if not recipe.get("input_replacement"):
        return order, ""
    context_stage = recipe["context_audit"]["component"]
    if order.count(context_stage) != 1 or order[0] != recipe["input_replacement"]:
        raise ValueError("context entry must occur once after the input adapter")
    stop = order.index(context_stage)
    lifted, definitions = list(order), []
    for number in range(1, stop):
        name = f"AFK{number:03d}"
        definitions.append(
            f"define {name} [ [{{*ᵘ}}|{{*ᶜ}}|0] "
            f"[[EnglishStarAlphabet - [{{*ᵘ}}|{{*ᶜ}}]]* .o. {order[number]}] ];"
        )
        lifted[number] = name
    return lifted, "\n".join(definitions)


def probe_appendix(recipe: dict, probes: list[dict]) -> tuple[str, dict[str, str]]:
    order = complete_variant_order(recipe)
    rendered, _ = context_lifted_order(recipe, order)
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
        lines.extend([f"define {name} " + "\n    .o. ".join(rendered[:endpoint]) + ";",
                      "clear stack", f"regex {name};", f"save stack {filename}"])
        bins[probe["id"]] = filename
    return "\n".join(lines), bins


def staged_appendix(recipe: dict) -> tuple[str, dict[str, str]]:
    order = complete_variant_order(recipe)
    rendered, _ = context_lifted_order(recipe, order)
    lines, bins = [], {}
    compiled_suffixes = {}
    for number, check in enumerate(recipe.get("staged_checks", [])):
        stage = recipe["replace"].get(check["stage"], check["stage"])
        if order.count(stage) != 1:
            raise ValueError(f"staged entry checkpoint missing or duplicated: {stage}")
        start = order.index(stage) + (check["side"] == "after")
        stop = recipe["replace"].get(check.get("stop_after"), check.get("stop_after"))
        if stop is not None and order.count(stop) != 1:
            raise ValueError(f"staged stopping checkpoint missing or duplicated: {stop}")
        end = len(order) if stop is None else order.index(stop) + 1
        if start == 0 or start == len(order):
            raise ValueError(f"staged check requires a nonempty starred-input suffix: {check['id']}")
        if end <= start:
            raise ValueError(f"staged stopping checkpoint precedes entry: {check['id']}")
        interval = (start, end)
        if interval in compiled_suffixes:
            bins[f"staged:{check['id']}"] = compiled_suffixes[interval]
            continue
        filename = f"af_staged_{number:02d}.bin"
        compiled_suffixes[interval] = filename
        lines.extend([f"define AFS{number:02d} " + "\n    .o. ".join(rendered[start:end]) + ";",
                      "clear stack", f"regex AFS{number:02d};", f"save stack {filename}"])
        bins[f"staged:{check['id']}"] = filename
    return "\n".join(lines), bins


def compile_isolated(
    source: Path, recipe: dict, probes: list[dict], directory: Path, *, components_only: bool = False,
    diagnostic_stages: list[str] | None = None,
) -> dict[str, Path]:
    source_text = source.read_text(encoding="utf-8")
    for command, filename in re.findall(r"(?m)^\s*(save stack|source)\s+([^;\n]+)", source_text):
        path = Path(filename.strip())
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"unsafe {command} destination in source: {filename}")
        if command == "source":
            raise ValueError("new source includes require explicit isolated-copy support")
    source_text = context_source_text(source_text, recipe)
    probe_text, bins = ("", {}) if components_only else probe_appendix(recipe, probes)
    staged_text, staged_bins = ("", {}) if components_only else staged_appendix(recipe)
    bins.update(staged_bins)
    component_lines = []
    components = sorted({check["component"] for check in recipe.get("component_checks", [])})
    for number, component in enumerate(components):
        filename = f"af_component_{number:02d}.bin"
        component_lines.extend(["clear stack", f"regex {component};", f"save stack {filename}"])
        bins[f"component:{component}"] = filename
    allowed_stages = set(context_lifted_order(recipe, complete_variant_order(recipe))[0])
    for number, stage in enumerate(diagnostic_stages or []):
        if stage not in allowed_stages:
            raise ValueError(f"diagnostic stage is not in the derived candidate: {stage}")
        filename = f"af_diagnostic_{number:03d}.bin"
        component_lines.extend(["clear stack", f"regex {stage};", f"save stack {filename}"])
        bins[f"diagnostic:{number}"] = filename
    complete, definitions = context_lifted_order(recipe, complete_variant_order(recipe))
    if components_only:
        variant_text = definitions
    else:
        variant_text = (
            definitions + "\ndefine AFContextRoot " + "\n    .o. ".join(complete)
            + ";\nclear stack\nregex AFContextRoot;\nsave stack old_english_variant.bin\n"
        )
    script = directory / "experiment.foma"
    script.write_text(
        source_text + "\n" + recipe["definitions"] + "\n"
        + variant_text + "\n" + probe_text + "\n"
        + staged_text + "\n"
        + "\n".join(component_lines) + "\nquit\n",
        encoding="utf-8",
    )
    result = subprocess.run(["foma", "-q", "-f", script.name], cwd=directory,
                            capture_output=True, text=True, timeout=600)
    log = result.stdout + "\n" + result.stderr
    if result.returncode or re.search(r"(?im)\b(error|syntax error|not defined)\b", log):
        raise RuntimeError("isolated Foma compilation failed:\n" + log[-6000:])
    outputs = {} if components_only else {"final": directory / "old_english_variant.bin"}
    outputs.update({name: directory / filename for name, filename in bins.items()})
    missing = [str(path) for path in outputs.values() if not path.is_file() or path.stat().st_size == 0]
    if missing:
        raise RuntimeError(f"isolated compiler did not produce required bins: {missing}")
    return outputs


def context_source_text(source_text: str, recipe: dict) -> str:
    symbols = recipe.get("phonetic_symbols", [])
    if symbols:
        anchor = "define EnglishPalatalConsonant ["
        if source_text.count(anchor) != 1:
            raise ValueError("palatal alphabet anchor must occur exactly once")
        extension = " | ".join("{*" + symbol + "}" for symbol in symbols) + " | "
        source_text = source_text.replace(anchor, anchor + extension, 1)
    if not recipe.get("input_replacement"):
        return source_text
    anchor = "define EnglishStarAlphabet ["
    if source_text.count(anchor) != 1:
        raise ValueError("context alphabet anchor must occur exactly once")
    return source_text.replace(anchor, anchor + "\n    {*ᶜ} |", 1)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def intermediate_outputs(bins: dict[str, Path], forms: list[str]) -> dict[str, list[list[str]]]:
    return {name: batch_apply_down(path, forms)
            for name, path in bins.items()
            if name != "final" and not name.startswith(("component:", "staged:", "diagnostic:"))}


def check_component_predictions(recipe: dict, bins: dict[str, Path]) -> list[dict]:
    checked = []
    for check in recipe.get("component_checks", []):
        outputs = batch_apply_down(bins[f"component:{check['component']}"], [check["input"]])[0]
        if outputs != [check["expected"]]:
            raise ValueError(f"{check['id']}: component prediction {[check['expected']]!r} != {outputs!r}")
        checked.append({**check, "outputs": outputs})
    return checked


def check_staged_predictions(recipe: dict, bins: dict[str, Path]) -> list[dict]:
    checked = []
    for check in recipe.get("staged_checks", []):
        outputs = batch_apply_down(bins[f"staged:{check['id']}"], [check["input"]])[0]
        if outputs != [check["expected"]]:
            raise ValueError(f"{check['id']}: staged prediction {[check['expected']]!r} != {outputs!r}")
        checked.append({**check, "outputs": outputs})
    return checked


def audit_context_domain(recipe: dict, bins: dict[str, Path], intermediate: dict, rows: list[dict]) -> list[dict]:
    audit = recipe.get("context_audit")
    if not audit:
        return []
    states = intermediate[audit["probe"]]
    if any(len(state) != 1 for state in states):
        raise ValueError("context audit requires unambiguous checkpoint states")
    bare = [state[0].replace("*ᵘ", "").replace("*ᶜ", "") for state in states]
    component = bins[f"component:{audit['component']}"]
    stressed = batch_apply_down(component, bare)
    final = batch_apply_down(component, ["*ᵘ" + form for form in bare])
    nonfinal = batch_apply_down(component, ["*ᶜ" + form for form in bare])
    if stressed != [[form] for form in bare] or nonfinal != [[form + "*ᶜ"] for form in bare]:
        raise ValueError("context audit changed a stressed or nonfinal negative")
    if any(len(outputs) != 1 for outputs in final):
        raise ValueError("context audit has missing/ambiguous unstressed outputs")
    return [
        {"row_id": row["id"], "concept": row["concept"], "checkpoint_input": form,
         "unstressed_final_output": output[0],
         "selected_context": row["input_context"]}
        for row, form, output in zip(rows, bare, final) if output != [form]
    ]


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
                        ("baseline_corpus_sha256", runtime.corpus_tsv),
                        ("baseline_context_sha256", runtime.data_dir / METADATA_FILENAME),
                        ("baseline_context_helper_sha256", runtime.bin_dir / "oe_input_context.py")):
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
                 runtime.data_dir / METADATA_FILENAME, runtime.bin_dir / "oe_input_context.py",
                 runtime.build_manifest, runtime.bin_dir / "old_english.bin"]
    protected.extend(runtime.bin_dir / name for name in oe_pipeline.expected_snapshot_bins())
    baseline_dir = runtime.docs_dir / "sound_changes/cascade_baseline"
    protected.extend(sorted(baseline_dir.glob("cascade_baseline_outputs*.tsv")))
    protected.extend(sorted(baseline_dir.glob("cascade_baseline_summary*.json")))
    protected.extend(sorted(baseline_dir.glob("approved_*_migration.json")))
    protected.append(baseline_dir / "approved_input_migrations.tsv")
    protected.extend(runtime.docs_dir / "sound_changes/registry" / name for name in (
        "sc_registry.tsv", "chronology_edges.tsv", "sc_inventory_notes.tsv",
    ))
    before = {str(path): digest(path) for path in protected}
    rows = corpus_rows(runtime.corpus_tsv)
    forms = [oe_pipeline.evaluation_input(row) for row in rows]
    variant_rows = apply_context_overrides(apply_input_overrides(rows, recipes[requested]), recipes[requested])
    variant_forms = [oe_pipeline.evaluation_input(row) for row in variant_rows]
    baseline = batch_apply_down(runtime.bin_dir / "old_english.bin", forms)
    if any(len(outputs) != 1 for outputs in baseline):
        raise RuntimeError("baseline has missing/ambiguous outputs; experiment cannot proceed")
    with tempfile.TemporaryDirectory(prefix="capr_af_identity_") as temporary:
        control_only = not any(recipes[requested].get(field) for field in (
            "definitions", "insert_after", "insert_rule", "replace",
            "input_overrides", "input_replacement", "citation_context", "context_overrides",
        ))
        identity_recipe = recipes[requested] if control_only else recipes["identity"]
        bins = compile_isolated(runtime.germanic_fst, identity_recipe, recipe_data["probes"], Path(temporary))
        identity = batch_apply_down(bins["final"], forms)
        if identity != baseline:
            changed = [row["id"] for row, old, new in zip(rows, baseline, identity) if old != new]
            raise RuntimeError(f"identity control disagrees with live production rows: {changed}")
        if control_only:
            variant = identity
            intermediate = intermediate_outputs(bins, forms)
            component_checks = check_component_predictions(recipes[requested], bins)
            staged_checks = check_staged_predictions(recipes[requested], bins)
            context_audit = audit_context_domain(recipes[requested], bins, intermediate, variant_rows)
        else:
            with tempfile.TemporaryDirectory(prefix="capr_af_variant_") as variant_temporary:
                variant_bins = compile_isolated(runtime.germanic_fst, recipes[requested],
                                                recipe_data["probes"], Path(variant_temporary))
                variant = batch_apply_down(variant_bins["final"], variant_forms)
                intermediate = intermediate_outputs(variant_bins, variant_forms)
                component_checks = check_component_predictions(recipes[requested], variant_bins)
                staged_checks = check_staged_predictions(recipes[requested], variant_bins)
                context_audit = audit_context_domain(
                    recipes[requested], variant_bins, intermediate, variant_rows,
                )
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
            "variant_fst_input": oe_pipeline.evaluation_input(variant_rows[index]),
            "variant_input_context": variant_rows[index].get("input_context"),
            "input_changed": oe_pipeline.evaluation_input(row) != oe_pipeline.evaluation_input(variant_rows[index]),
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
        "checked_staged_fixtures": staged_checks,
        "context_domain_audit": context_audit,
        "rows": report_rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recipe", required=True)
    parser.add_argument("--recipes", type=Path, default=layout().docs_dir /
                        "sound_changes/literature_dossiers/anglo_frisian/oe_experiment_recipes.json")
    args = parser.parse_args()
    try:
        recipe_data = load_recipes(args.recipes)
        report = run(recipe_data, args.recipe)
        with args.recipes.with_name(
            recipe_data.get("fixture_file", "oe_diagnostic_fixtures.tsv")
        ).open(
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
