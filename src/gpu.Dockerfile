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
ARG PATH_TO_GLADIA_SRC="/app/"
ARG DOCKER_USER=root
ARG DOCKER_GROUP=root
ARG API_SERVER_PORT_HTTP=8080
ARG MAMBA_ALWAYS_SOFTLINK="true"
ARG CLEAN_LAYER_SCRIPT=$PATH_TO_GLADIA_SRC/tools/docker/clean-layer.sh
ARG VENV_BUILDER_PATH=$PATH_TO_GLADIA_SRC/tools/venv-builder/

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
    TORCH_HUB=$MODEL_CACHE_ROOT"/torch/hub" \
    MAMBA_ROOT_PREFIX="/opt/conda" \
    MAMBA_EXE="/usr/local/bin/micromamba" \
    MAMBA_DOCKERFILE_ACTIVATE=1 \
    MAMBA_ALWAYS_YES=true \
    PATH=$PATH:/usr/local/bin/:$MAMBA_EXE \
    PATH_TO_GLADIA_SRC=$PATH_TO_GLADIA_SRC \
    API_SERVER_PORT_HTTP=$API_SERVER_PORT_HTTP

RUN mkdir -p $TRITON_MODELS_PATH && \
    mkdir -p $GLADIA_TMP_PATH && \
    mkdir -p $MODEL_CACHE_ROOT && \
    mkdir -p $TRANSFORMERS_CACHE && \
    mkdir -p $PYTORCH_TRANSFORMERS_CACHE && \
    mkdir -p $PYTORCH_PRETRAINED_BERT_CACHE && \
    mkdir -p $NLTK_DATA && \
    mkdir -p $TRITON_MODELS_PATH && \
    mkdir -p $PATH_TO_GLADIA_SRC

COPY . $PATH_TO_GLADIA_SRC

# Update apt repositories - Add Nvidia GPG key
RUN apt-key del 7fa2af80 && \
    apt-get install -y apt-transport-https && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    sed -i 's/deb https:\/\/developer.download.nvidia.com\/compute\/cuda\/repos\/ubuntu2004\/x86_64.*//g' /etc/apt/sources.list && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update --allow-insecure-repositories -y && \
    apt install -y \
        libssl-dev \
        libpng-dev \
        libjpeg-dev \
        python3.8 \
        python3.8-distutils \
        python3.8-dev \
        python3-setuptools \
        git-lfs \
        libmagic1 \
        libmysqlclient-dev \
        libgl1 \
        software-properties-common \
        cmake \
        libleptonica-dev \
        tesseract-ocr  \
        libtesseract-dev \
        python3-pil \
        tesseract-ocr-all && \
    echo "== INSTALLING GITLFS ==" && \
    cd /tmp && \
    wget https://github.com/git-lfs/git-lfs/releases/download/v3.0.1/git-lfs-linux-386-v3.0.1.tar.gz && \
    tar -xvf git-lfs-linux-386-v3.0.1.tar.gz && \
    bash /tmp/install.sh && \
    rm /tmp/install.sh && \
    echo "== INSTALLING UMAMBA ==" && \
    wget -qO- "https://micro.mamba.pm/api/micromamba/linux-64/latest" | tar -xvj bin/micromamba && \
    mv bin/micromamba /usr/local/bin/micromamba && \ 
    micromamba shell init -s bash && \
    micromamba config set always_softlink $MAMBA_ALWAYS_SOFTLINK && \
    $CLEAN_LAYER_SCRIPT
  
# Automatically activate micromaba for every bash shell
RUN mv $PATH_TO_GLADIA_SRC/tools/docker/_activate_current_env.sh /usr/local/bin/ && \
    echo "source /usr/local/bin/_activate_current_env.sh" >> ~/.bashrc && \
    echo "source /usr/local/bin/_activate_current_env.sh" >> /etc/skel/.bashrc && \
    echo "micromamba activate server" >> ~/.bashrc

WORKDIR $PATH_TO_GLADIA_SRC

RUN micromamba create -f env.yaml && \
    $PATH_TO_GLADIA_SRC/tools/docker/clean-layer.sh

RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then \
        micromamba run -n server /bin/bash -c "cd $VENV_BUILDER_PATH && python3 create_custom_envs.py --modality '.*/apis/text/[a-zA-Z ]+/[a-rA-R].*'"; \
    fi  && \
    $CLEAN_LAYER_SCRIPT

RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then \
        micromamba run -n server /bin/bash -c "cd $VENV_BUILDER_PATH && python3 create_custom_envs.py --modality '.*/apis/text/[a-zA-Z ]+/[s-zS-Z].*'"; \
    fi  && \
    $CLEAN_LAYER_SCRIPT

RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then \
        micromamba run -n server /bin/bash -c "cd $VENV_BUILDER_PATH && python3 create_custom_envs.py --modality '.*/apis/video/.*'"; \
    fi  && \
    $CLEAN_LAYER_SCRIPT

RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then \
        micromamba run -n server /bin/bash -c "cd $VENV_BUILDER_PATH && python3 create_custom_envs.py --modality '.*/apis/image/[a-zA-Z ]+/[a-hA-H].*'"; \
    fi && \
    $CLEAN_LAYER_SCRIPT

RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then \
        micromamba run -n server /bin/bash -c "cd $VENV_BUILDER_PATH && python3 create_custom_envs.py --modality '.*/apis/image/[a-zA-Z ]+/[i-zI-Z].*'"; \
    fi && \
    $CLEAN_LAYER_SCRIPT

RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then \
        micromamba run -n server /bin/bash -c "cd $VENV_BUILDER_PATH && python3 create_custom_envs.py --modality '.*/apis/audio/.*'"; \ 
    fi && \
    $CLEAN_LAYER_SCRIPT

ENV LD_PRELOAD="/opt/tritonserver/backends/pytorch/libmkl_rt.so" \
    LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$MAMBA_ROOT_PREFIX/envs/server/lib/"

RUN echo "== ADJUSTING binaries ==" && \ 
    mv /usr/bin/python3 /usr/bin/python38 && \
    ln -sf /usr/bin/python /usr/bin/python3 && \
    echo "== ADJUSTING entrypoint ==" && \ 
    mv $PATH_TO_GLADIA_SRC/tools/docker/entrypoint.sh /opt/nvidia/nvidia_entrypoint.sh && \
    echo "== ADJUSTING path rights ==" && \ 
    chown -R $DOCKER_USER:$DOCKER_GROUP $PATH_TO_GLADIA_SRC && \
    chown -R $DOCKER_USER:$DOCKER_GROUP $GLADIA_TMP_PATH && \
    echo "== FIXING libcurl references ==" && \ 
    rm $MAMBA_ROOT_PREFIX/envs/server/lib/libcurl.so.4 && \
    ln -s /usr/lib/x86_64-linux-gnu/libcurl.so.4.6.0 $MAMBA_ROOT_PREFIX/envs/server/lib/libcurl.so.4 && \
    $CLEAN_LAYER_SCRIPT

EXPOSE $API_SERVER_PORT_HTTP

ENTRYPOINT ["micromamba", "run", "-n", "server"]

CMD ["/app/run_server_prod.sh"]

