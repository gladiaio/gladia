# This script should never be called directly, only sourced: source _activate_current_env.sh

if [[ "${MAMBA_SKIP_ACTIVATE}" == "1" ]]; then
  return
fi

# Initialize the current shell
eval "$("${MAMBA_EXE}" shell hook --shell=bash)"

micromamba activate "${ENV_NAME}"
