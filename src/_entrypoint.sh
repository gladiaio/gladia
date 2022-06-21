#!/usr/bin/env bash

set -ef -o pipefail

source _activate_current_env.sh

micromamba run -n server $@