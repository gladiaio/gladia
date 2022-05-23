#!/usr/bin/env bash

# Force fail if the following exit with a none 0 status code
set -ef -o pipefail

# Activate the environment if $MAMBA_DOCKERFILE_ACTIVATE=1
if [[ "${MAMBA_DOCKERFILE_ACTIVATE}" == "1" ]]; then
  source _activate_current_env.sh
fi

exec bash -o pipefail -c "$@"
