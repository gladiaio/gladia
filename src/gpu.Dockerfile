#https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/
ARG GLADIA_DOCKER_BASE=nvcr.io/nvidia/tritonserver:22.03-py3

FROM $GLADIA_DOCKER_BASE

# add build options to setup_custom_envs
# can be -f to force rebuild of env if already exist
# -p 1 is set by default for stability purposes
# python3 setup_custom_envs.py --help
#
#Usage: setup_custom_envs.py [OPTIONS]

#Options:
#  -r, --rootdir TEXT            Build env recursively from the provided
#                                directory path
#  -p, --poolsize INTEGER        Parallelness if set to 0 will use all threads
#  -s, --simlink                 Will simlink gladia-api-utils from the local
#                                version of gladia-api-utils
#  -c, --compact_mode            Enable compact mode simlinking the default
#                                packages
#  -f, --force                   Force rebuilding venv
#  -b, --base                    Build the base for custom env
#  -t, --trash_cache             Trash the pipenv cache
#  -l, --local_venv_trash_cache  Trash the pipenv cache on cust venv
#  -d, --teardown_common_env     Tear common venv
#  -B, --build_all_env           Build all cust venv
#  -x, --clean_all_venv          Clean all cust venv
#  --help                        Show this message and exit.

ARG SETUP_CUSTOM_ENV_BUILD_MODE="--local_venv_trash_cache --force --simlink --compact_mode --poolsize 1 --base --build_all_env"
ARG SKIP_CUSTOM_ENV_BUILD="false"
ARG SKIP_ROOT_CACHE_CLEANING="false"
ARG SKIP_PIP_CACHE_CLEANING="false"
ARG SKIP_YARN_CACHE_CLEANING="false"
ARG SKIP_NPM_CACHE_CLEANING="false"
ARG SKIP_TMPFILES_CACHE_CLEANING="false"
ARG SKIP_NTLK_DL="false"
ARG GLADIA_API_UTILS_BRANCH="main"

ENV PIPENV_VENV_IN_PROJECT="enabled" \
    TOKENIZERS_PARALLELISM="true" \
    TRANSFORMERS_CACHE="/tmp/gladia/models/transformers" \
    PYTORCH_TRANSFORMERS_CACHE="/tmp/gladia/models/pytorch_transformers" \
    PYTORCH_PRETRAINED_BERT_CACHE="/tmp/gladia/models/pytorch_pretrained_bert" \
    NLTK_DATA="/tmp/gladia/nltk" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8" \
    distro="ubuntu2004" \
    arch="x86_64" \
    TRITON_MODELS_PATH="/tmp/gladia/triton" \
    TRITON_SERVER_PORT_HTTP=8000 \
    TRITON_SERVER_PORT_GRPC=8001 \
    TRITON_SERVER_PORT_METRICS=8002

# Update apt repositories
RUN apt-get install -y apt-transport-https && \
    apt-get clean && \
    apt-get update --allow-insecure-repositories -y


# Install Cmake
RUN apt install -y libssl-dev && \
    wget https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0.tar.gz && \
    tar -zxvf cmake-3.20.0.tar.gz > /dev/null && \
    cd cmake-3.20.0 && ./bootstrap > /dev/null && \
    make && \
    make install

COPY . /app

WORKDIR /tmp

RUN cd /tmp && \
    wget https://github.com/git-lfs/git-lfs/releases/download/v3.0.1/git-lfs-linux-386-v3.0.1.tar.gz && \
    tar -xvf git-lfs-linux-386-v3.0.1.tar.gz && \
    bash /tmp/install.sh

# Add Nvidia GPG key
RUN apt-key del 7fa2af80
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.0-1_all.deb

RUN dpkg -i cuda-keyring_1.0-1_all.deb

RUN sed -i 's/deb https:\/\/developer.download.nvidia.com\/compute\/cuda\/repos\/ubuntu2004\/x86_64.*//g' /etc/apt/sources.list

# env vars for micro-mamba
ENV MAMBA_ROOT_PREFIX="/opt/conda"
ENV MAMBA_EXE="/usr/local/bin/micromamba"
ENV MAMBA_DOCKERFILE_ACTIVATE=1
ENV MAMBA_ALWAYS_YES=true
ENV PATH=$PATH:/usr/local/bin/:$MAMBA_EXE

# Install micromamba
RUN wget -qO- "https://micro.mamba.pm/api/micromamba/linux-64/latest" | tar -xvj bin/micromamba
RUN mv bin/micromamba /usr/local/bin/micromamba
RUN micromamba shell init -s bash

# Script which launches commands passed to "docker run"
COPY _entrypoint.sh /usr/local/bin/_entrypoint.sh
COPY _activate_current_env.sh /usr/local/bin/_activate_current_env.sh
ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]

# Automatically activate micromaba for every bash shell
RUN echo "source /usr/local/bin/_activate_current_env.sh" >> ~/.bashrc && \
    echo "source /usr/local/bin/_activate_current_env.sh" >> /etc/skel/.bashrc

# Add python repository and install python3.7
RUN add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get install -y \
        python3.7 \
        python3.7-distutils \
        python3.7-dev

# Install dep pacakges
RUN apt-get update && \
    apt-get install -y \
        python3-setuptools \
        git-lfs \
        libmagic1 \
        libmysqlclient-dev \
        libgl1 \
        software-properties-common && \
    apt-get install -y \
        cmake

# Install terressact and its dependencies
RUN apt-get install -y \
        libleptonica-dev \
        tesseract-ocr  \
        libtesseract-dev \
        python3-pil \
        tesseract-ocr-all

WORKDIR /app

RUN micromamba create -f env.yaml
RUN micromamba run -n server /bin/bash -c "cd venv-builder/ && python3 create_default_envs.py"
RUN micromamba run -n server /bin/bash -c "cd venv-builder/ && python3 create_custom_envs.py"
SHELL ["/usr/local/bin/micromamba", "run", "-n", "server", "/bin/bash", "-c"]


# Clean caches
RUN if [ "$SKIP_ROOT_CACHE_CLEANING" = "false" ]; then [ -d "/root/.cache/" ] && rm -rf "/root/.cache/*"; fi && \
    if [ "$SKIP_PIP_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/pip*"; fi && \
    if [ "$SKIP_YARN_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/yarn*"; fi && \
    if [ "$SKIP_NPM_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/npm*"; fi && \
    if [ "$SKIP_TMPFILES_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/tmp*"; fi && \
    apt-get clean && \
    apt-get autoremove --purge

RUN mv /usr/bin/python3 /usr/bin/python38 && \
    ln -sf /usr/bin/python /usr/bin/python3

RUN mv /app/entrypoint.sh /opt/nvidia/nvidia_entrypoint.sh

EXPOSE 80

CMD ["micromamba", "run", "-n", "server", "/app/run_server_prod.sh"]
