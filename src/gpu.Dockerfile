#https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/
ARG GLADIA_DOCKER_BASE=nvcr.io/nvidia/tritonserver:22.03-py3

FROM $GLADIA_DOCKER_BASE

ARG SKIP_CUSTOM_ENV_BUILD="false"
ARG SKIP_ROOT_CACHE_CLEANING="false"
ARG SKIP_PIP_CACHE_CLEANING="false"
ARG SKIP_YARN_CACHE_CLEANING="false"
ARG SKIP_NPM_CACHE_CLEANING="false"
ARG SKIP_TMPFILES_CACHE_CLEANING="false"
ARG GLADIA_TMP_PATH="/tmp/gladia/"

ENV GLADIA_TMP_PATH=$GLADIA_TMP_PATH \
    MODEL_CACHE_ROOT="$GLADIA_TMP_PATH/models"

ENV TRANSFORMERS_CACHE=$MODEL_CACHE_ROOT"/transformers" \
    PIPENV_VENV_IN_PROJECT="enabled" \
    PYTORCH_TRANSFORMERS_CACHE=$MODEL_CACHE_ROOT"/pytorch_transformers" \
    PYTORCH_PRETRAINED_BERT_CACHE=$MODEL_CACHE_ROOT"/pytorch_pretrained_bert" \
    NLTK_DATA=$GLADIA_TMP_PATH"/nltk" \
    TOKENIZERS_PARALLELISM="true" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8" \
    distro="ubuntu2004" \
    arch="x86_64" \
    TRITON_MODELS_PATH=$GLADIA_TMP_PATH"/triton" \
    TRITON_SERVER_PORT_HTTP=8000 \
    TRITON_SERVER_PORT_GRPC=8001 \
    TRITON_SERVER_PORT_METRICS=8002 \
    PATH_TO_GLADIA_SRC="/app" \
    API_SERVER_WORKERS=1 \
    TORCH_HOME=$MODEL_CACHE_ROOT"/torch" \
    TORCH_HUB=$MODEL_CACHE_ROOT"/torch/hub"

RUN mkdir -p $TRITON_MODELS_PATH && \
    mkdir -p $GLADIA_TMP_PATH && \
    mkdir -p $MODEL_CACHE_ROOT && \
    mkdir -p $TRANSFORMERS_CACHE && \
    mkdir -p $PYTORCH_TRANSFORMERS_CACHE && \
    mkdir -p $PYTORCH_PRETRAINED_BERT_CACHE && \
    mkdir -p $NLTK_DATA && \
    mkdir -p $TRITON_MODELS_PATH \
    mkdir -p $PATH_TO_GLADIA_SRC

# Update apt repositories
# Add Nvidia GPG key
RUN apt-key del 7fa2af80
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.0-1_all.deb

RUN dpkg -i cuda-keyring_1.0-1_all.deb

RUN sed -i 's/deb https:\/\/developer.download.nvidia.com\/compute\/cuda\/repos\/ubuntu2004\/x86_64.*//g' /etc/apt/sources.list

RUN apt-get install -y apt-transport-https && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get update --allow-insecure-repositories -y && \
    apt install -y libssl-dev \
    libpng-dev \
    libjpeg-dev

COPY . $PATH_TO_GLADIA_SRC

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
# ENTRYPOINT ["/usr/local/bin/_entrypoint.sh"]

# Automatically activate micromaba for every bash shell
RUN echo "source /usr/local/bin/_activate_current_env.sh" >> ~/.bashrc && \
    echo "source /usr/local/bin/_activate_current_env.sh" >> /etc/skel/.bashrc && \
    echo "micromamba activate server" >> ~/.bashrc

# Add python repository and install python3.7
RUN add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get install -y \
        python3.7 \
        python3.7-distutils \
        python3.7-dev

# Install dep pacakges
RUN apt-get update && \
    apt-get autoclean && \
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
RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then micromamba run -n server /bin/bash -c "cd venv-builder/ && python3 create_custom_envs.py"; fi
SHELL ["/usr/local/bin/micromamba", "run", "-n", "server", "/bin/bash", "-c"]

ENV LD_PRELOAD="/opt/tritonserver/backends/pytorch/libmkl_rt.so"
ENV LD_LIBRARY_PATH="/opt/conda/envs/server/lib/":$MAMBA_ROOT_PREFIX"/envs/server/lib/"
ENV PATH_TO_GLADIA_SRC="/app"

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

ARG DOCKER_USER=root
ARG DOCKER_GROUP=root

# API_SERVER_PORT_HTTP is set as a build arg
# in order to manage the EXPOSE port param
ARG API_SERVER_PORT_HTTP=8080

RUN chown -R $DOCKER_USER:$DOCKER_GROUP $PATH_TO_GLADIA_SRC && \
    chown -R $DOCKER_USER:$DOCKER_GROUP $GLADIA_TMP_PATH

EXPOSE $API_SERVER_PORT_HTTP

RUN rm $MAMBA_ROOT_PREFIX/envs/server/lib/libcurl.so.4 && \
    ln -s /usr/lib/x86_64-linux-gnu/libcurl.so.4.6.0 $MAMBA_ROOT_PREFIX/envs/server/lib/libcurl.so.4

ENTRYPOINT ["micromamba", "run", "-n", "server"]

CMD ["/app/run_server_prod.sh"]
