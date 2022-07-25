#!/bin/bash
#
# This scripts should be called at the end of each RUN command
# in the Dockerfiles.
#
# Each RUN command creates a new layer that is stored separately.
# At the end of each command, we should ensure we clean up downloaded
# archives and source files used to produce binary to reduce the size
# of the layer.
set -e
set -x

# Delete files that pip caches when installing a package.
rm -rf /root/.cache/*
rm -rf /tmp/pip*
rm -rf /tmp/yarn*
rm -rf /tmp/npm*
rm -rf /tmp/tmp*
rm -rf /tmp/mambaf*
rm -rf /tmp/git*
rm -rf /tmp/*.md

# Delete old downloaded archive files 
apt-get autoremove --purge -y
# Delete downloaded archive files
apt-get clean autoclean
# Ensures the current working directory won't be deleted
cd /usr/local/src/
# Delete source files used for building binaries
rm -rf /usr/local/src/*
rm -rf /var/lib/apt/lists/*

# Cleanup micromamba
find "$MAMBA_ROOT_PREFIX" -follow -type f -name '*.a' -delete
find "$MAMBA_ROOT_PREFIX" -follow -type f -name '*.pyc' -delete
find "$MAMBA_ROOT_PREFIX" -follow -type f -name '*.js.map' -delete

micromamba clean --all --yes
