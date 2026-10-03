#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"
tlmgr_repo="${ASSEMBLY_DOCKER_TLMGR_REPOSITORY:-https://ftp.fau.de/ctan/systems/texlive/tlnet}"

assembled_md="${script_dir}/reader_facing_local_section_20.md"
assembled_pdf="${script_dir}/reader_facing_local_section_20.pdf"

cd "${repo_root}"

python3 Germanic/tools/adjudicate.py --refresh

python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_style.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_citations.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_foma_width.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_section_order.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_generated_prose.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_crossrefs.py
python3 Germanic/docs/sound_changes/reader_facing/check_reader_facing_chronology_evidence.py

python3 Germanic/tools/check_sound_change_heading_wrapping.py --markdown-path "${assembled_md}"

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
    pandoc Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_20.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --lua-filter=Germanic/tools/predicted_form_filter.lua \
      --lua-filter=Germanic/tools/reconstructed_form_filter.lua \
      --lua-filter=Germanic/tools/lex_form_filter.lua \
      --lua-filter=Germanic/docs/sound_changes/reader_facing/reader_facing_foma.lua \
      --include-in-header=Germanic/docs/sound_changes/reader_facing/reader_facing_pdf_header.tex \
      --number-sections \
      --table-of-contents \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_20.pdf
  "

echo "Generated ${assembled_md}"
echo "Generated ${assembled_pdf}"
echo "Generated ${script_dir}/reader_facing_manifest_coverage_08.md"
