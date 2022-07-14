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
    mkdir -p $TRITON_MODELS_PATH \
    mkdir -p $PATH_TO_GLADIA_SRC

# Update apt repositories
# Add Nvidia GPG key
RUN echo "== INSTALLING NVIDIA DEB ==" && \
    apt-key del 7fa2af80 && \
    wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    sed -i 's/deb https:\/\/developer.download.nvidia.com\/compute\/cuda\/repos\/ubuntu2004\/x86_64.*//g' /etc/apt/sources.list && \
    apt-get install -y apt-transport-https && \
    apt-get autoclean && \
    apt-get clean && \
    apt-get update --allow-insecure-repositories -y && \
    apt install -y libssl-dev \
    libpng-dev \
    libjpeg-dev && \
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
    echo "== INSTALLING python3.7 ==" && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get install -y \
        python3.7 \
        python3.7-distutils \
        python3.7-dev && \
    echo "== INSTALLING deb packages ==" && \
    apt-get update && \
    apt-get autoclean && \
    apt-get install -y \
        python3-setuptools \
        git-lfs \
        libmagic1 \
        libmysqlclient-dev \
        libgl1 \
        software-properties-common \
        cmake && \
    echo "== INSTALLING libtesseract ==" && \
    apt-get install -y \
        libleptonica-dev \
        tesseract-ocr  \
        libtesseract-dev \
        python3-pil \
        tesseract-ocr-all

COPY . $PATH_TO_GLADIA_SRC

# Script which launches commands passed to "docker run"
COPY _entrypoint.sh _activate_current_env.sh /usr/local/bin/

# Automatically activate micromaba for every bash shell
RUN echo "source /usr/local/bin/_activate_current_env.sh" >> ~/.bashrc && \
    echo "source /usr/local/bin/_activate_current_env.sh" >> /etc/skel/.bashrc && \
    echo "micromamba activate server" >> ~/.bashrc

WORKDIR $PATH_TO_GLADIA_SRC

RUN micromamba create -f env.yaml && \
    if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then micromamba run -n server /bin/bash -c "cd venv-builder/ && python3 create_custom_envs.py"; fi

SHELL ["/usr/local/bin/micromamba", "run", "-n", "server", "/bin/bash", "-c"]

ENV LD_PRELOAD="/opt/tritonserver/backends/pytorch/libmkl_rt.so" \
    LD_LIBRARY_PATH="/opt/conda/envs/server/lib/":$MAMBA_ROOT_PREFIX"/envs/server/lib/"
   

# post install scripts
RUN echo "== CLEANING cache ==" && \ 
    if [ "$SKIP_ROOT_CACHE_CLEANING" = "false" ]; then [ -d "/root/.cache/" ] && rm -rf "/root/.cache/*"; fi && \
    if [ "$SKIP_PIP_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/pip*"; fi && \
    if [ "$SKIP_YARN_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/yarn*"; fi && \
    if [ "$SKIP_NPM_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/npm*"; fi && \
    if [ "$SKIP_TMPFILES_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/tmp*"; fi && \
    apt-get clean && \
    apt-get autoremove --purge && \
    echo "== ADJUSTING binaries ==" && \ 
    mv /usr/bin/python3 /usr/bin/python38 && \
    ln -sf /usr/bin/python /usr/bin/python3 && \
    echo "== ADJUSTING entrypoint ==" && \ 
    mv /app/entrypoint.sh /opt/nvidia/nvidia_entrypoint.sh && \
    echo "== ADJUSTING path rights ==" && \ 
    chown -R $DOCKER_USER:$DOCKER_GROUP $PATH_TO_GLADIA_SRC && \
    chown -R $DOCKER_USER:$DOCKER_GROUP $GLADIA_TMP_PATH && \
    echo "== FIXING libcurl references ==" && \ 
    rm $MAMBA_ROOT_PREFIX/envs/server/lib/libcurl.so.4 && \
    ln -s /usr/lib/x86_64-linux-gnu/libcurl.so.4.6.0 $MAMBA_ROOT_PREFIX/envs/server/lib/libcurl.so.4

EXPOSE $API_SERVER_PORT_HTTP

ENTRYPOINT ["micromamba", "run", "-n", "server"]

CMD ["/app/run_server_prod.sh"]
