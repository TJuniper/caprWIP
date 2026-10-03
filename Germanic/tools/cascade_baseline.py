#!/usr/bin/env python3
"""Freeze a reproducible output baseline for the Old English cascade.

Phase 1 of the historical-cascade-order project needs an authoritative record of
exactly what the current cascade accepts and produces, so that any later reorder
can be proven output-equivalent.  Foma compilation is byte-non-deterministic
(recompiling ``germanic.txt`` yields different ``.bin`` checksums), so the
baseline is anchored on **outputs**, not on compiled-artifact checksums.

For every Old English lexeme in the aligned dataset this tool records:

* the normalised proto input actually fed to the transducer;
* whether the transducer accepted the input;
* the full, order-independent set of surface outputs;
* the output multiplicity (how many distinct outputs);
* whether the attested counterpart is among the outputs.

It then emits a deterministic per-lexeme TSV and a summary JSON containing an
``outputs_sha256`` computed over the sorted ``proto_norm -> sorted-outputs``
mapping.  Two runs against two independent recompiles of the same source must
produce the same ``outputs_sha256``; that hash is the reproducibility marker
that replaces bin checksums.

Because it calls ``flookup``, this tool is designed to run inside the backend
container (where foma/flookup and the freshly compiled bins live).
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

# Matches the normalisation used by oe_mismatch_report.load_rows so the baseline
# feeds the transducer exactly what the existing reports feed it.
_PROTO_STRIP_RE = re.compile(r"[{}*\s/()]")


def normalize_proto(raw: str) -> str:
    normalized = _PROTO_STRIP_RE.sub("", raw or "")
    return normalized.replace("þ", "θ")


def load_oe_rows(tsv_path: Path) -> list[dict[str, str]]:
    """Load Old English lexeme rows (DOCULECT == Old_English) with normalised proto."""
    import csv

    rows: list[dict[str, str]] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "Old_English":
                continue
            proto = (row.get("PROTOFORM") or "").strip()
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not proto or not counterpart or counterpart == "-":
                continue
            norm = normalize_proto(proto)
            if not norm:
                continue
            rows.append({
                "row_id": row["ID"],
                "concept": (row.get("CONCEPT") or "").strip(),
                "proto": proto,
                "proto_norm": norm,
                "counterpart": counterpart,
            })
    return rows


def legacy_subset(records: list[dict], legacy_rows: list[dict],
                  migrations: list[dict]) -> list[dict]:
    """Resolve frozen identities, permitting only documented input migrations."""
    by_key = {}
    by_id = {}
    for record in records:
        key = (record["proto_norm"], record["counterpart"], record["concept"])
        if key in by_key or record["row_id"] in by_id:
            raise ValueError(f"duplicate baseline identity: {key}")
        by_key[key] = record
        by_id[record["row_id"]] = record
    approved = {}
    for migration in migrations:
        if set(migration) != {"row_id", "concept", "counterpart", "old_proto",
                              "new_proto", "adjudication_memo"} or not all(migration.values()):
            raise ValueError("invalid approved input migration")
        key = (normalize_proto(migration["old_proto"]),
               migration["counterpart"], migration["concept"])
        if key in approved or any(m["row_id"] == migration["row_id"] for m in approved.values()):
            raise ValueError("duplicate approved input migration")
        if migration["old_proto"] == migration["new_proto"]:
            raise ValueError("input migration must change the input")
        approved[key] = migration
    selected = []
    used = set()
    seen = set()
    for old in legacy_rows:
        key = (old["proto_norm"], old["counterpart"], old["concept"])
        if key in seen:
            raise ValueError(f"duplicate frozen identity: {key}")
        seen.add(key)
        migration = approved.get(key)
        if migration:
            if old["proto"] != migration["old_proto"]:
                raise ValueError(f"migration old input mismatch: {key}")
            current = by_id.get(migration["row_id"])
            if current is None or any(current[field] != migration[value] for field, value in (
                ("proto", "new_proto"), ("concept", "concept"), ("counterpart", "counterpart")
            )) or current["proto_norm"] != normalize_proto(migration["new_proto"]):
                raise ValueError(f"migration current identity mismatch: {key}")
            used.add(key)
        else:
            current = by_key.get(key)
            if current is None or current["proto"] != old["proto"]:
                raise ValueError(f"unapproved legacy input drift: {key}")
        for field in ("accepted", "output_count", "match", "outputs"):
            if current[field] != old[field]:
                raise ValueError(f"unapproved legacy {field} drift: {key}")
        selected.append(current)
    if used != set(approved):
        raise ValueError("migration does not resolve a frozen legacy identity")
    return sorted(selected, key=lambda r: (r["proto_norm"], r["counterpart"], r["concept"]))


def apply_batch(bin_path: Path, forms: list[str]) -> dict[str, list[str]]:
    """Apply the transducer to a batch of forms; return {form: sorted-unique-outputs}.

    A single flookup invocation processes all forms (one per line) for speed.
    ``+?`` (rejection) yields an empty output list for that form.
    """
    proc = subprocess.run(
        ["flookup", "-i", str(bin_path)],
        input=("\n".join(forms) + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    results: dict[str, set[str]] = {form: set() for form in forms}
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.rstrip("\n")
        if not raw.strip():
            continue
        parts = raw.split("\t", 1)
        inp = parts[0]
        out = parts[1] if len(parts) == 2 else ""
        if inp not in results:
            results.setdefault(inp, set())
        if out and out != "+?":
            results[inp].add(out)
    return {form: sorted(results.get(form, set())) for form in forms}


def build_baseline(tsv_path: Path, bin_path: Path) -> dict[str, object]:
    rows = load_oe_rows(tsv_path)
    # Deterministic input order for reproducibility.
    rows.sort(key=lambda r: (r["proto_norm"], r["counterpart"], r["concept"]))

    # One flookup call over all normalised protos.
    forms = [r["proto_norm"] for r in rows]
    outputs_by_form = apply_batch(bin_path, forms)

    records: list[dict[str, object]] = []
    accepted = rejected = matched = mismatched = ambiguous = 0
    for r in rows:
        outs = outputs_by_form.get(r["proto_norm"], [])
        is_accepted = bool(outs)
        is_match = r["counterpart"] in outs
        if is_accepted:
            accepted += 1
        else:
            rejected += 1
        if is_match:
            matched += 1
        else:
            mismatched += 1
        if len(outs) > 1:
            ambiguous += 1
        records.append({
            "row_id": r["row_id"],
            "concept": r["concept"],
            "proto": r["proto"],
            "proto_norm": r["proto_norm"],
            "counterpart": r["counterpart"],
            "accepted": "1" if is_accepted else "0",
            "output_count": str(len(outs)),
            "match": "1" if is_match else "0",
            "outputs": "|".join(outs),
        })

    # Reproducibility marker: hash the canonical proto->outputs projection.
    hasher = hashlib.sha256()
    for r in records:
        hasher.update((r["proto_norm"] + "\x1f" + r["outputs"] + "\x1e").encode("utf-8"))
    outputs_sha256 = hasher.hexdigest()

    # Archived inputs remain immutable; approved migrations select the same
    # original identities under their explicitly documented current inputs.
    legacy_subset_sha256 = ""
    legacy_subset_count = 0
    legacy_path = tsv_path.parent.parent / "docs/sound_changes/cascade_baseline/cascade_baseline_outputs_legacy380.tsv"
    if not legacy_path.exists():
        # container layout: /usr/app/data + /usr/app/docs
        legacy_path = Path("docs/sound_changes/cascade_baseline/cascade_baseline_outputs_legacy380.tsv")
    if legacy_path.exists():
        with legacy_path.open(encoding="utf-8") as handle:
            legacy_rows = list(csv.DictReader(handle, delimiter="\t"))
        migration_path = legacy_path.with_name("approved_input_migrations.tsv")
        with migration_path.open(encoding="utf-8") as handle:
            migrations = list(csv.DictReader(handle, delimiter="\t"))
        selected = legacy_subset(records, legacy_rows, migrations)
        legacy_hasher = hashlib.sha256()
        for r in selected:
            legacy_hasher.update((r["proto_norm"] + "\x1f" + r["outputs"] + "\x1e").encode("utf-8"))
            legacy_subset_count += 1
        legacy_subset_sha256 = legacy_hasher.hexdigest()

    summary = {
        "total_lexemes": len(records),
        "accepted": accepted,
        "rejected": rejected,
        "matched": matched,
        "mismatched": mismatched,
        "ambiguous_outputs": ambiguous,
        "outputs_sha256": outputs_sha256,
        "legacy_subset_count": legacy_subset_count,
        "legacy_subset_sha256": legacy_subset_sha256,
    }
    return {"summary": summary, "records": records}


def write_outputs(baseline: dict[str, object], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    records = baseline["records"]  # type: ignore[index]
    fields = ["row_id", "concept", "proto", "proto_norm", "counterpart", "accepted", "output_count", "match", "outputs"]
    tsv_lines = ["\t".join(fields)]
    for r in records:  # type: ignore[assignment]
        tsv_lines.append("\t".join(str(r[f]) for f in fields))
    (out_dir / "cascade_baseline_outputs.tsv").write_text("\n".join(tsv_lines) + "\n", encoding="utf-8")
    (out_dir / "cascade_baseline_summary.json").write_text(
        json.dumps(baseline["summary"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tsv", type=Path, default=Path("data/germanic-aligned-final.tsv"),
                        help="Aligned dataset TSV (default: %(default)s, resolved in CWD)")
    parser.add_argument("--bin", type=Path, default=Path("old_english.bin"),
                        help="Compiled OE transducer bin (default: %(default)s)")
    parser.add_argument("--out-dir", type=Path,
                        default=Path("docs/sound_changes/cascade_baseline"),
                        help="Directory for baseline artifacts (default: %(default)s)")
    parser.add_argument("--print-summary", action="store_true",
                        help="Print the summary JSON to stdout without writing files")
    args = parser.parse_args()

    baseline = build_baseline(args.tsv, args.bin)
    if args.print_summary:
        print(json.dumps(baseline["summary"], indent=2, ensure_ascii=False))
    else:
        write_outputs(baseline, args.out_dir)
        s = baseline["summary"]
        print(f"wrote baseline to {args.out_dir}")
        print(f"  lexemes={s['total_lexemes']} accepted={s['accepted']} rejected={s['rejected']} "
              f"matched={s['matched']} mismatched={s['mismatched']} ambiguous={s['ambiguous_outputs']}")
        print(f"  outputs_sha256={s['outputs_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
