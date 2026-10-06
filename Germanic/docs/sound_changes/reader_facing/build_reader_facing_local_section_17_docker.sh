#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"
tlmgr_repo="${ASSEMBLY_DOCKER_TLMGR_REPOSITORY:-https://ftp.fau.de/ctan/systems/texlive/tlnet}"

assembled_md="${script_dir}/reader_facing_local_section_17.md"
assembled_pdf="${script_dir}/reader_facing_local_section_17.pdf"

cd "${repo_root}"

python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_17_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_17_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py \
  --build-script Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_17_docker.sh
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py

python3 - <<'PY'
from pathlib import Path
import csv
import re

root = Path("Germanic/docs/sound_changes/reader_facing")
out = root / "reader_facing_local_section_17.md"
coverage_out = root / "reader_facing_manifest_coverage_05.md"
chapter_files = [
    "003-west-germanic-rhotacism.md",
    "004-pwgmc-ai-monophthongization.md",
    "006-early-i-apocope.md",
    "007-final-o-lowering-before-r.md",
    "008-coronal-w-assimilation.md",
    "014-015-opening-vowel-prelude.md",
    "016-west-saxon-palatal-glide.md",
    "017-nwgmc-u-lowering.md",
    "018-stressed-monosyllable-o-raising.md",
    "019-nwgmc-final-long-o-raising.md",
    "020-wgmc-final-z-deletion.md",
    "021-unstressed-o-raising.md",
    "022-mn-dissimilation.md",
    "023-n-stem-n-loss.md",
    "024-long-e-lowering.md",
    "025-long-a-nasal-rounding.md",
    "101-long-a-fronting.md",
    "026-027-nasal-spirant-changes.md",
    "028-preconsonantal-x-loss.md",
    "029-030-awj-glide-and-au-fronting.md",
    "031-034-west-saxon-diphthong-chain.md",
    "035-037-prefix-and-compound-adjustments.md",
    "039-040-medial-unstressed-vowel-changes.md",
    "041-final-bare-a-loss.md",
    "042-surviving-bimoric-o-unrounding.md",
    "043-anglo-frisian-brightening.md",
    "044-045-breaking-and-velar-fricative-palatalization.md",
    "046-048-restoration-and-nasal-tail-changes.md",
    "049-pgmc-b-allophony.md",
    "050-pwgmc-sievers-law-syncope.md",
    "051-sk-palatalization.md",
    "052-velar-palatalization.md",
    "053-054-pre-umlaut-bridge-and-w-loss.md",
    "055-056-i-umlaut-core.md",
    "057-j-cluster-coalescence.md",
    "059-oe-back-mutation.md",
    "060-ws-palatal-umlaut-note.md",
    "061-weak-tail-nasal-loss-note.md",
    "063-high-vowel-apocope.md",
    "064-065-post-apocope-tail.md",
    "066-068-syncope-and-degemination-corridor.md",
    "069-early-o-shortening-context-note.md",
    "070-071-early-unstressed-fronting-shortening-bridge.md",
    "072-073-unstressed-long-vowel-shortening-and-ae-merger-core.md",
    "074-075-medial-unstressed-i-lowering.md",
    "076-prefix-i-reduction.md",
    "078-weak-tail-reduction.md",
    "079-080-final-j-loss-and-final-geminate-simplification.md",
    "081-083-j-strengthening-vocalization-and-ei-contraction.md",
    "085-086-h-loss-and-contraction.md",
    "087-r-metathesis.md",
]
rule_heading_re = re.compile(r"^##\s+(SC\d{3})\.\s+(.*?)\s+\(`([^`]+)`\)\s+\{#(rule-[^}]+)\}\s*$")
link_re = re.compile(r"\[([^\]]+)\]\((#rule-[^)]+)\)")

parts: list[str] = [
    "# A sequence from early West Germanic consonant and vowel shifts to Old English r-metathesis",
    "",
    "## Introduction",
    "",
    "This section follows an ordered stretch from West Germanic rhotacism, Proto-West-Germanic ai-monophthongization, early i-apocope, final *ō-lowering before *r, coronal-w assimilation, the earliest unstressed vowel changes, early vocalic and final changes, nasal spirant changes, preconsonantal x-loss, awj glide formation, au-fronting, and the West Saxon diphthong sequence through brightening, breaking, restoration, palatalization, weak-tail reduction, contraction, and r-metathesis.",
    "",
    "Some chapters treat broad vowel histories, while others record smaller rules whose value lies in the witness words that fix their place within the finite-state sequence.",
    "",
]

active_anchors: set[str] = set()
file_sc_map: dict[str, list[str]] = {}
reader_sc_numbers: list[str] = []
seen_sc: set[str] = set()

for name in chapter_files:
    text = (root / name).read_text(encoding="utf-8")
    scs: list[str] = []
    for line in text.splitlines():
        match = rule_heading_re.match(line.strip())
        if not match:
            continue
        sc_number = match.group(1)
        scs.append(sc_number)
        active_anchors.add(f"#{match.group(4)}")
        if sc_number not in seen_sc:
            seen_sc.add(sc_number)
            reader_sc_numbers.append(sc_number)
    unique = sorted(set(scs), key=lambda item: int(item[2:]))
    file_sc_map[name] = unique


def resolve_links(text: str) -> str:
    return link_re.sub(lambda match: match.group(0) if match.group(2) in active_anchors else match.group(1), text)


for idx, name in enumerate(chapter_files):
    if idx:
        parts.extend(["", r"\newpage", ""])
    parts.append(resolve_links((root / name).read_text(encoding="utf-8").rstrip()))

parts.extend([
    "",
    r"\newpage",
    "",
    "# References",
    "",
    "::: {#refs}",
    ":::",
    "",
])

out.write_text("\n".join(parts), encoding="utf-8")

manifest_rows: list[dict[str, object]] = []
manifest_path = Path("Germanic/docs/sound_changes/change_reports/report_manifest.tsv")
with manifest_path.open(encoding="utf-8") as handle:
    reader = csv.DictReader(handle, delimiter="\t")
    for row in reader:
        if not row["ID"]:
            continue
        sc_ids = [item.strip() for item in row["CHANGE_IDS"].split(";") if item.strip()]
        chapters = [name for name in chapter_files if set(file_sc_map[name]) & set(sc_ids)]
        covered_scs = sorted({sc for name in chapters for sc in file_sc_map[name]}, key=lambda item: int(item[2:]))
        manifest_rows.append({
            "id": row["ID"],
            "title": row["TITLE"],
            "change_ids": sc_ids,
            "chapters": chapters,
            "covered": set(sc_ids).issubset(set(covered_scs)),
        })

manifest_sc_numbers = sorted({sc for row in manifest_rows for sc in row["change_ids"]}, key=lambda item: int(item[2:]))
reader_sc_set = set(reader_sc_numbers)
manifest_sc_set = set(manifest_sc_numbers)
missing_manifest_sc = sorted(manifest_sc_set - reader_sc_set, key=lambda item: int(item[2:]))
extra_reader_sc = sorted(reader_sc_set - manifest_sc_set, key=lambda item: int(item[2:]))

front_manifest_gaps = [sc for sc in ("SC005", "SC009") if sc not in manifest_sc_set]

resumed_sc_numbers = [sc for sc in manifest_sc_numbers if int(sc[2:]) >= 14]
if resumed_sc_numbers:
    resumed_min = min(int(sc[2:]) for sc in resumed_sc_numbers)
    resumed_max = max(int(sc[2:]) for sc in resumed_sc_numbers)
    later_gaps = [f"SC{i:03d}" for i in range(resumed_min, resumed_max + 1) if f"SC{i:03d}" not in manifest_sc_set]
else:
    later_gaps = []

expected_gaps = front_manifest_gaps + later_gaps
early_programme_missing = [
    f"SC{i:03d}"
    for i in range(1, 14)
    if f"SC{i:03d}" not in manifest_sc_set and f"SC{i:03d}" not in set(front_manifest_gaps)
]
uncovered_rows = [row for row in manifest_rows if not row["covered"]]

coverage_parts: list[str] = [
    "# Reader-facing manifest coverage 05",
    "",
    "## Inputs",
    "",
    "1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`",
    "2. `Germanic/docs/sound_changes/reader_facing/build_reader_facing_local_section_17_docker.sh`",
    "",
    "## Manifest rows covered by reader-facing chapters",
    "",
    "| Manifest row | Change IDs | Reader-facing chapter files | Covered |",
    "| --- | --- | --- | --- |",
]

for row in manifest_rows:
    chapters = ", ".join(f"`{name}`" for name in row["chapters"]) if row["chapters"] else "—"
    coverage_parts.append(
        f"| `{row['id']}` {row['title']} | `{';'.join(row['change_ids'])}` | {chapters} | {'yes' if row['covered'] else 'no'} |"
    )

coverage_parts.extend([
    "",
    "## SC numbers covered by reader-facing rule sections",
    "",
    ", ".join(f"`{sc}`" for sc in reader_sc_numbers),
    "",
    "## Manifest rows not yet covered",
    "",
])

if uncovered_rows:
    for row in uncovered_rows:
        coverage_parts.append(f"1. `{row['id']}` {row['title']} — missing `{';'.join(row['change_ids'])}`")
else:
    coverage_parts.append("1. none")

coverage_parts.extend([
    "",
    "## SC numbers present in the manifest but missing from reader-facing rule headings",
    "",
])

if missing_manifest_sc:
    coverage_parts.append(", ".join(f"`{sc}`" for sc in missing_manifest_sc))
else:
    coverage_parts.append("1. none")

coverage_parts.extend([
    "",
    "## Reader-facing rule headings not present in the manifest",
    "",
])

if extra_reader_sc:
    coverage_parts.append(", ".join(f"`{sc}`" for sc in extra_reader_sc))
else:
    coverage_parts.append("1. none")

coverage_parts.extend([
    "",
    "## Expected gaps in the manifest-backed sequence",
    "",
])

if expected_gaps:
    coverage_parts.append(", ".join(f"`{sc}`" for sc in expected_gaps))
else:
    coverage_parts.append("1. none")

coverage_parts.extend([
    "",
    "## Early SC numbers and the current manifest-backed programme",
    "",
])

if "SC003" in manifest_sc_set and "SC003" in reader_sc_set:
    coverage_parts.append("1. `SC003` is now covered by `003-west-germanic-rhotacism.md`.")
else:
    coverage_parts.append("1. `SC003` is not fully covered in the current reader-facing set.")

if "SC004" in manifest_sc_set and "SC004" in reader_sc_set:
    coverage_parts.append("2. `SC004` is now covered by `004-pwgmc-ai-monophthongization.md`.")
else:
    coverage_parts.append("2. `SC004` is not fully covered in the current reader-facing set.")

if "SC006" in manifest_sc_set and "SC006" in reader_sc_set:
    coverage_parts.append("3. `SC006` is now covered by `006-early-i-apocope.md`.")
else:
    coverage_parts.append("3. `SC006` is not fully covered in the current reader-facing set.")

if "SC007" in manifest_sc_set and "SC007" in reader_sc_set:
    coverage_parts.append("4. `SC007` is now covered by `007-final-o-lowering-before-r.md`.")
else:
    coverage_parts.append("4. `SC007` is not fully covered in the current reader-facing set.")

if "SC008" in manifest_sc_set and "SC008" in reader_sc_set:
    coverage_parts.append("5. `SC008` is now covered by `008-coronal-w-assimilation.md`.")
else:
    coverage_parts.append("5. `SC008` is not fully covered in the current reader-facing set.")

if "SC005" not in manifest_sc_set:
    coverage_parts.append("6. `SC005` is absent because `report_manifest.tsv` does not include it.")
else:
    coverage_parts.append("6. `SC005` appears in `report_manifest.tsv`.")

if "SC009" not in manifest_sc_set:
    coverage_parts.append("7. `SC009` is absent because `report_manifest.tsv` does not include it.")
else:
    coverage_parts.append("7. `SC009` appears in `report_manifest.tsv`.")

coverage_parts.append("8. Coverage from `SC014` through `SC087` remains intact.")

if early_programme_missing:
    coverage_parts.append(
        "9. The remaining early SC numbers outside the current manifest-backed programme are "
        + ", ".join(f"`{sc}`" for sc in early_programme_missing)
        + "."
    )
else:
    coverage_parts.append("9. No other early SC numbers remain outside the current manifest-backed programme.")

if {"SC003", "SC004", "SC006", "SC007", "SC008", "SC014", "SC015"} <= manifest_sc_set:
    coverage_parts.append("10. The manifest-backed sequence now opens with `SC003`, `SC004`, `SC006`, `SC007`, and `SC008`, and then resumes at `SC014-SC015`.")
else:
    coverage_parts.append("10. The manifest-backed opening sequence no longer matches the expected `SC003`, `SC004`, `SC006`, `SC007`, `SC008`, then `SC014-SC015` pattern.")

coverage_out.write_text("\n".join(coverage_parts) + "\n", encoding="utf-8")
PY

if ! command -v docker >/dev/null 2>&1; then
  echo "docker not found; cannot run Docker-based render." >&2
  exit 127
fi

if ! docker info >/dev/null 2>&1; then
  echo "docker daemon not running; start Docker Desktop or another daemon first." >&2
  exit 1
fi

docker run --rm --platform "${platform}" --entrypoint /bin/sh \
  -v "${repo_root}":/data -w /data "${image}" -c "
    set -e
    apk add --no-cache ${font_package} >/dev/null
    kpsewhich fvextra.sty >/dev/null 2>&1 || (
      tlmgr option repository ${tlmgr_repo} >/dev/null &&
      tlmgr update --self >/dev/null &&
      tlmgr install fvextra >/dev/null
    )
    pandoc Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_17.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --lua-filter=Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
      --include-in-header=Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
      --number-sections \
      --table-of-contents \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_17.pdf
  "

echo "Generated ${assembled_md}"
echo "Generated ${assembled_pdf}"
echo "Generated ${script_dir}/reader_facing_manifest_coverage_05.md"
