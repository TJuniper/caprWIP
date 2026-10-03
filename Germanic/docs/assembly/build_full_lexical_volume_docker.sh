#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd -- "${script_dir}/../../.." && pwd)"
image="${ASSEMBLY_DOCKER_IMAGE:-pandoc/latex:latest}"
platform="${ASSEMBLY_DOCKER_PLATFORM:-linux/amd64}"
font_package="${ASSEMBLY_DOCKER_FONT_PACKAGE:-font-noto}"
build_log="${script_dir}/lexical_volume_alpha_01_build.log"

cd "${repo_root}"

python3 Germanic/tools/adjudicate.py --refresh

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
    pandoc Germanic/docs/assembly/lexical_volume_alpha_01.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --to=latex \
      --lua-filter=Germanic/tools/predicted_form_filter.lua \
      --lua-filter=Germanic/tools/reconstructed_form_filter.lua \
      --lua-filter=Germanic/tools/lex_form_filter.lua \
      --include-in-header=Germanic/docs/assembly/semantic_form_macros.tex \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      -o Germanic/docs/assembly/lexical_volume_alpha_01.tex
    pandoc Germanic/docs/assembly/lexical_volume_alpha_01.md \
      --standalone \
      --from=markdown+raw_tex+citations \
      --lua-filter=Germanic/tools/predicted_form_filter.lua \
      --lua-filter=Germanic/tools/reconstructed_form_filter.lua \
      --lua-filter=Germanic/tools/lex_form_filter.lua \
      --include-in-header=Germanic/docs/assembly/semantic_form_macros.tex \
      --metadata-file=Germanic/docs/assembly/full_volume_metadata.yaml \
      --bibliography=docs/refs.bib \
      --citeproc \
      --pdf-engine=xelatex \
      -o Germanic/docs/assembly/lexical_volume_alpha_01.pdf
  " 2>&1 | tee "${build_log}"

echo "Generated ${script_dir}/lexical_volume_alpha_01.tex"
echo "Generated ${script_dir}/lexical_volume_alpha_01.pdf"
echo "Generated ${build_log}"
