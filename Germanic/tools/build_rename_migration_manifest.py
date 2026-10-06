#!/usr/bin/env python3
"""ARCHIVE — rename-migration campaign manifest (canonical-ontology relabel).

GENRE: ARCHIVE/FROZEN. This generator and its output TSV are a historical
snapshot of the rename-migration campaign. The frozen columns
(former_foma_identifier, former_display_name, former_hist_stage,
former_hist_scope, migration_commit) are immutable audit history. The
statuses and notes record the CAMPAIGN-TIME plan and are partly superseded:
e.g. the SC004 note "split decision pending" predates the completed SC004
component split, SC024/SC025 position references are campaign-time positions,
and SC025's second migration (-> EAFLongANasalRounding) has since landed.
Current identifiers, stages/scopes, and executable positions live in
registry/sc_registry.tsv and the executable model (oe_pipeline).

This builder is NOT run by adjudicate.py --finalize. Rewriting the frozen
archive requires an explicit --allow-archival-rewrite flag.

Original description: behaviour-neutral migration only. Each row pairs a
rule's former identifier / display / stage / scope with its canonical target
under the CAPR stage+scope ontology (PGmc -> PNWGmc -> PWGmc -> EAF -> OE for
stage; a separate hist_scope axis). Former fields are a FROZEN pre-migration
snapshot (FORMER below); the canonical targets are encoded in RENAMES below.

migration_status values: pending | completed | deferred | not_required
This generator is self-contained and reproducible: re-running never reads the
(mutating) live staging map for former values.
"""
from __future__ import annotations

import argparse
import csv
import io
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
DEFAULT_OUT = SC_DIR / "cascade_baseline/rename_migration_manifest.tsv"

# Frozen pre-migration snapshot of former (former_foma_identifier,
# former_display_name, former_hist_stage, former_hist_scope). Captured before any
# rename touched the live staging map, so regenerating the manifest after rules
# have migrated never corrupts the "former_*" columns.
FORMER: dict[str, tuple[str, str, str, str]] = {
    "SC003": ("PGmcRhotacism", "Rhotacism", "wgmc", "pan_wgmc"),
    "SC004": ("PWGmcAiMonophthongization", "PWGmc Ai Monophthongization", "pnwgmc_pwgmc_transition", "pan_wgmc"),
    "SC005": ("NWGmcAToUBeforeM", "NWGmc A To U Before M", "nwgmc", "pan_nwgmc"),
    "SC012": ("PWGmcLThVoicing", "PWGmc L Th Voicing", "pwgmc", "pan_wgmc"),
    "SC014": ("NWGmcUnstressedAiMonophthongization", "NWGmc Unstressed Ai Monophthongization", "nwgmc", "pan_nwgmc"),
    "SC015": ("NWGmcILowering", "NWGmc I Lowering", "nwgmc", "pan_nwgmc"),
    "SC016": ("OEWsPalatalGlide", "OE Ws Palatal Glide", "oe_ws", "west_saxon"),
    "SC017": ("NWGmcULowering", "NWGmc U Lowering", "nwgmc", "pan_nwgmc"),
    "SC018": ("NWGmcStressedMonosyllableORaising", "NWGmc Stressed Monosyllable O Raising", "nwgmc", "pan_nwgmc"),
    "SC019": ("NWGmcFinalLongORaising", "NWGmc Final Long O Raising", "nwgmc", "pan_nwgmc"),
    "SC020": ("PGmcFinalZDeletion", "PGmc Final Z Deletion", "wgmc", "pan_wgmc"),
    "SC021": ("NWGmcUnstressedORaising", "NWGmc Unstressed O Raising", "nwgmc", "pan_nwgmc"),
    "SC022": ("NWGmcMnDissimilation", "NWGmc Mn Dissimilation", "nwgmc", "pan_nwgmc"),
    "SC023": ("NWGmcNStemNLoss", "NWGmc N Stem N Loss", "nwgmc", "pan_nwgmc"),
    "SC024": ("NWGmcLongELowering", "NWGmc Long E Lowering", "nwgmc", "pan_nwgmc"),
    "SC025": ("NWGmcLongENasalRounding", "NWGmc Long E Nasal Rounding", "nwgmc", "pan_nwgmc"),
    "SC026": ("NWGmcNasalSpirantLengthening", "NWGmc Nasal Spirant Lengthening", "ingvaeonic", "north_sea_germanic"),
    "SC027": ("NWGmcNasalSpirantLoss", "NWGmc Nasal Spirant Loss", "ingvaeonic", "north_sea_germanic"),
    "SC028": ("NWGmcPreconsonantalXLoss", "NWGmc Preconsonantal X Loss", "nwgmc", "pan_nwgmc"),
    "SC041": ("PWGmcFinalBareALoss", "PWGmc Final Bare A Loss", "pwgmc", "pan_wgmc"),
    "SC042": ("PWGmcSurvivingBimoricOUnrounding", "PWGmc Surviving Bimoric O Unrounding", "pwgmc", "pan_wgmc"),
    "SC043": ("AngloFrisianBrightening", "Anglo Frisian Brightening", "af", "anglo_frisian"),
    "SC049": ("PGmcBAllophony", "PGmc B Allophony", "pgmc", "pan_germanic"),
    "SC050": ("SieversLawSyncope", "Sievers Law Syncope", "pwgmc", "pan_wgmc"),
    "SC064": ("NWGmcInStemNLoss", "NWGmc In Stem N Loss", "nwgmc", "pan_nwgmc"),
}

# Completed rule migrations: sc_id -> commit SHA (empty string until the SHA is
# recorded at final canonicalization). Presence here sets migration_status=completed.
COMPLETED: dict[str, str] = {
    "SC028": "2f74516b",
    # SC025 first migration (-> PNWGmcLongENasalRounding) completed in 0b4ffa59;
    # superseded by the e1-complex re-adjudication second migration (-> EAFLongANasalRounding), pending below.
    "SC024": "851f7531",
    "SC023": "aeea523b",
    "SC022": "10e55b8c",
    "SC019": "337d31b6",
    "SC018": "c94fb4a3",
    "SC017": "7013010d",
    "SC015": "3d5b8e16",
    "SC014": "83ecd998",
    "SC003": "d606d6dd",
    "SC020": "e71a5af3",
    "SC026": "76cbb304",
    "SC027": "02e6f081",
    "SC043": "1043597a",
    "SC012": "2910f28a",
    "SC005": "52f3fdd7",
}

# Canonical rename set (task section 3). Each entry:
#   canonical_foma_identifier, canonical_display_name, canonical_hist_stage,
#   canonical_hist_scope, migration_status, notes
# Former fields are loaded from the staging map at build time.
RENAMES: dict[str, dict[str, str]] = {}

# --- 3.1 Proto-Northwest Germanic rules: NWGmc* -> PNWGmc*, nwgmc->pnwgmc,
#         pan_nwgmc->pan_pnwgmc, reader "NWGmc ..." -> "Proto-Northwest Germanic ..."
_PNWGMC = {
    "SC005": "PNWGmcAToUBeforeM",
    "SC014": "PNWGmcUnstressedAiMonophthongization",
    "SC015": "PNWGmcILowering",
    "SC017": "PNWGmcULowering",
    "SC018": "PNWGmcStressedMonosyllableORaising",
    "SC019": "PNWGmcFinalLongORaising",
    "SC023": "PNWGmcNStemNLoss",
    "SC024": "PNWGmcLongELowering",
    "SC025": "PNWGmcLongENasalRounding",
    "SC028": "PNWGmcPreconsonantalXLoss",
}
for _sc, _canon in _PNWGMC.items():
    RENAMES[_sc] = {
        "canonical_foma_identifier": _canon,
        "canonical_display_name": "",  # derived: "NWGmc X" -> "Proto-Northwest Germanic X"
        "canonical_hist_stage": "pnwgmc",
        "canonical_hist_scope": "pan_pnwgmc",
        "migration_status": "pending",
        "notes": "PNWGmc convention: make Proto-Northwest Germanic explicit; body/order unchanged",
    }

RENAMES["SC022"] = {
    "canonical_foma_identifier": "PNWGmcMnDissimilation",
    "canonical_display_name": "Common Germanic Mn Dissimilation",
    "canonical_hist_stage": "pgmc",
    "canonical_hist_scope": "pan_germanic",
    "migration_status": "pending",
    "notes": "Foma identifier remains stable; Fulk 2018 p.121 §6.11 and Polomé 1967 pp.818-819 correct the historical scope from PNWGmc to Common Germanic.",
}

RENAMES["SC023"] = {
    "canonical_foma_identifier": "PNWGmcNStemNLoss",
    "canonical_display_name": "Proto-Germanic Word-Final N Loss",
    "canonical_hist_stage": "pgmc",
    "canonical_hist_scope": "pan_germanic",
    "migration_status": "pending",
    "notes": "Foma identifier remains stable; Ringe 2017 pp.101-103 correct the historical stage from PNWGmc to (pre-)Proto-Germanic general word-final *-n loss (sc023-adjudication.md); {*o-n}-only environment is a citation-form proxy.",
}

RENAMES["SC024"] = {
    "canonical_foma_identifier": "PNWGmcLongELowering",
    "canonical_display_name": "NWGmc Long E1 Lowering",
    "canonical_hist_stage": "pnwgmc",
    "canonical_hist_scope": "pan_pnwgmc",
    "migration_status": "pending",
    "notes": "Foma identifier remains stable. Re-adjudicated by the e1-complex split (sc024-sc025-sc101-e1-complex-adjudication.md): SC024 now implements only the early pan-NWGmc stressed *e1 > *a lowering ({*e-acute} -> {*a}, unconditioned, position 12); the later Anglo-Frisian fronting formerly telescoped into this rule is the new SC101 EAFLongAFronting.",
}

RENAMES["SC025"] = {
    "canonical_foma_identifier": "EAFLongANasalRounding",
    "canonical_display_name": "EAF Long A Nasal Rounding",
    "canonical_hist_stage": "eaf",
    "canonical_hist_scope": "north_sea_germanic",
    "migration_status": "pending",
    "notes": "Second migration: intermediate identifier PNWGmcLongENasalRounding (completed 0b4ffa59) superseded by the e1-complex re-adjudication -- the rule now consumes the *a produced by SC024 ({*a} -> {*o} / _ nasal) at the EAF stage, North Sea Germanic scope, position 26 (before SC004).",
}

# --- 3.2 Early Anglo-Frisian corridor rules ---
RENAMES["SC003"] = {
    "canonical_foma_identifier": "EAFRhotacism",
    "canonical_display_name": "West Germanic rhotacism",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "pan_wgmc",
    "migration_status": "pending",
    "notes": "Former identifier PGmcRhotacism. Scope kept pan_wgmc; medial-*z* rhotacism scoped to non-final (order unchanged).",
}
RENAMES["SC020"] = {
    "canonical_foma_identifier": "EAFFinalZDeletion",
    "canonical_display_name": "West Germanic final *z*-deletion",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "pan_wgmc",
    "migration_status": "pending",
    "notes": "Former identifier PGmcFinalZDeletion. Scope provisional: pan-WGmc vs narrower (Ingvaeonic) UNRESOLVED; not settled by this rename.",
}
RENAMES["SC012"] = {
    "canonical_foma_identifier": "EAFLThVoicing",
    "canonical_display_name": "Northern West Germanic *lþ*-voicing",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "north_wgmc",
    "migration_status": "pending",
    "notes": "Former identifier PWGmcLThVoicing. Confidence A->B; pan-PWGmc attribution must not survive (R/T pp.170-171).",
}
RENAMES["SC026"] = {
    "canonical_foma_identifier": "EAFNasalSpirantLengthening",
    "canonical_display_name": "North Sea Germanic nasal-spirant lengthening",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "north_sea_germanic",
    "migration_status": "pending",
    "notes": "Former identifier NWGmcNasalSpirantLengthening. Traditional scholarly label: Ingvaeonic. Keep SC026<SC027, two-rule split.",
}
RENAMES["SC027"] = {
    "canonical_foma_identifier": "EAFNasalSpirantLoss",
    "canonical_display_name": "North Sea Germanic nasal-spirant loss",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "north_sea_germanic",
    "migration_status": "pending",
    "notes": "Former identifier NWGmcNasalSpirantLoss. Traditional scholarly label: Ingvaeonic.",
}
RENAMES["SC043"] = {
    "canonical_foma_identifier": "EAFBrightening",
    "canonical_display_name": "Anglo-Frisian brightening",
    "canonical_hist_stage": "eaf", "canonical_hist_scope": "anglo_frisian",
    "migration_status": "pending",
    "notes": "Former identifier AngloFrisianBrightening. Aligns identifier to EAF stage; conventional name retained in book.",
}

# --- Rules explicitly excluded from the rename migration (task section 4) ---
EXCLUDED: dict[str, tuple[str, str]] = {
    "SC004": ("deferred", "Conflates distinguishable developments; split decision pending (do not rename)."),
    "SC064": ("deferred", "Stage unresolved (hist_stage nwgmc vs chapter 4/OE, confidence C); do not rename."),
    "SC016": ("not_required", "OE West Saxon; early position is a documented FST dependency, not a stage claim."),
    "SC021": ("retired", "SC021 is retired; former PNWGmcUnstressedORaising has no live canonical rule. Successors are SC071, SC099, and SC100."),
    "SC041": ("not_required", "PWGmc name source-correct (R/T pp.60-61); no rename."),
    "SC042": ("not_required", "Model-shaped feeder; position-by-dependency; no rename."),
    "SC049": ("not_required", "PGmc *b allophony correct; late position is an FST dependency."),
    "SC050": ("not_required", "Eponymous SieversLawSyncope may keep no stage prefix; late position is a feeder."),
}

FIELDS = [
    "sc_id", "former_foma_identifier", "canonical_foma_identifier",
    "former_display_name", "canonical_display_name",
    "former_hist_stage", "canonical_hist_stage",
    "former_hist_scope", "canonical_hist_scope",
    "migration_status", "migration_commit", "notes",
]


def _read_staging() -> dict[str, dict[str, str]]:
    lines = [ln for ln in STAGING_MAP.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return {r["sc_id"]: r for r in csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t")}


def _canonical_display(sc: str, former_display: str, entry: dict[str, str]) -> str:
    if entry.get("canonical_display_name"):
        return entry["canonical_display_name"]
    # PNWGmc convention: "NWGmc X" -> "Proto-Northwest Germanic X"
    if former_display.startswith("NWGmc "):
        return "Proto-Northwest Germanic " + former_display[len("NWGmc "):]
    return former_display


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for sc in sorted(set(RENAMES) | set(EXCLUDED), key=lambda s: int(s[2:])):
        former_id, former_disp, former_stage, former_scope = FORMER[sc]
        if sc in RENAMES:
            e = RENAMES[sc]
            status = "completed" if sc in COMPLETED else e["migration_status"]
            rows.append({
                "sc_id": sc,
                "former_foma_identifier": former_id,
                "canonical_foma_identifier": e["canonical_foma_identifier"],
                "former_display_name": former_disp,
                "canonical_display_name": _canonical_display(sc, former_disp, e),
                "former_hist_stage": former_stage,
                "canonical_hist_stage": e["canonical_hist_stage"],
                "former_hist_scope": former_scope,
                "canonical_hist_scope": e["canonical_hist_scope"],
                "migration_status": status,
                "migration_commit": COMPLETED.get(sc, ""),
                "notes": e["notes"],
            })
        else:
            status, note = EXCLUDED[sc]
            if status == "retired":
                canonical_id = ""
                canonical_display = ""
                canonical_stage = "retired"
                canonical_scope = "retired"
            else:
                canonical_id = former_id
                canonical_display = former_disp
                canonical_stage = former_stage
                canonical_scope = former_scope
            rows.append({
                "sc_id": sc,
                "former_foma_identifier": former_id,
                "canonical_foma_identifier": canonical_id,
                "former_display_name": former_disp,
                "canonical_display_name": canonical_display,
                "former_hist_stage": former_stage,
                "canonical_hist_stage": canonical_stage,
                "former_hist_scope": former_scope,
                "canonical_hist_scope": canonical_scope,
                "migration_status": status,
                "migration_commit": "",
                "notes": note,
            })
    return rows


ARCHIVE_BANNER = """\
# ARCHIVE / FROZEN — rename-migration campaign manifest snapshot.
# Not regenerated by adjudicate.py --finalize. former_* / migration_commit are
# immutable audit history; statuses and notes record the CAMPAIGN-TIME plan
# (e.g. the SC004 "split decision pending" note predates the completed SC004
# split, and SC024/SC025 position references are campaign-time positions).
# Current identifiers/stages/positions live in registry/sc_registry.tsv and
# oe_pipeline. Rewriting requires build_rename_migration_manifest.py
# --allow-archival-rewrite.
"""


def write_manifest(rows: list[dict[str, str]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(ARCHIVE_BANNER)
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--allow-archival-rewrite", action="store_true",
                        help="explicitly rewrite the FROZEN archival snapshot")
    args = parser.parse_args()
    if not args.allow_archival_rewrite:
        print("ARCHIVE: rename_migration_manifest.tsv is a frozen campaign "
              "snapshot and is not regenerated; pass --allow-archival-rewrite "
              "only for deliberate archival maintenance.", file=sys.stderr)
        return 1
    rows = build_rows()
    write_manifest(rows, args.out)
    print(f"wrote {args.out} ({len(rows)} rules)")
    if args.summary:
        from collections import Counter
        print("  status:", dict(Counter(r["migration_status"] for r in rows)))
        print("  renames pending:", [r["sc_id"] for r in rows if r["migration_status"] == "pending"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
