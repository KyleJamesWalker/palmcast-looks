#!/usr/bin/env bash
# Collect packs into one themes directory and one transitions directory, which
# is the shape Palmcast's two flags take.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out="${OUT_DIR:-${root}/build}"

packs=("$@")
if [ ${#packs[@]} -eq 0 ]; then
  for dir in "${root}"/packs/*/; do packs+=("$(basename "${dir}")"); done
fi

rm -rf "${out}"
mkdir -p "${out}/themes" "${out}/transitions"

for pack in "${packs[@]}"; do
  src="${root}/packs/${pack}"
  if [ ! -d "${src}" ]; then
    echo "no pack named ${pack} in ${root}/packs" >&2
    exit 1
  fi
  for kind in themes transitions; do
    if compgen -G "${src}/${kind}/*.css" > /dev/null; then
      cp "${src}/${kind}"/*.css "${out}/${kind}/"
    fi
  done
done

echo "assembled ${#packs[@]} pack(s) into ${out}"
echo "  --theme-dir ${out}/themes --transition-dir ${out}/transitions"
