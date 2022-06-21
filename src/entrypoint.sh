#!/bin/bash
# Gather parts in alpha order
shopt -s nullglob extglob
_SCRIPT_DIR="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"
declare -a _PARTS=( "${_SCRIPT_DIR}/entrypoint.d"/*@(.txt|.sh) )
shopt -u nullglob extglob

# Execute the entrypoint parts
for _file in "${_PARTS[@]}"; do
  case "${_file}" in
    *.txt) cat "${_file}";;
    *.sh)  source "${_file}";;
  esac
done

echo

# This script can either be a wrapper around arbitrary command lines,
# or it will simply exec bash if no arguments were given
if [[ $# -eq 0 ]]; then
  /usr/local/bin/micromamba run -n server /bin/bash
else
  /usr/local/bin/micromamba run -n server /bin/bash -c $@
fi
