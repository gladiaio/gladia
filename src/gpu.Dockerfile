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

ENV PIPENV_VENV_IN_PROJECT="enabled" \
    GLADIA_TMP_PATH="/tmp/gladia/" \
    MODEL_CACHE_ROOT=$GLADIA_TMP_PATH"/models" \
    TRANSFORMERS_CACHE=$MODEL_CACHE_ROOT"/transformers" \
    PYTORCH_TRANSFORMERS_CACHE=$MODEL_CACHE_ROOT"/pytorch_transformers" \
    PYTORCH_PRETRAINED_BERT_CACHE=$MODEL_CACHE_ROOT"/pytorch_pretrained_bert" \
    NLTK_DATA=$GLADIA_TMP_PATH"/nltk" \
    TOKENIZERS_PARALLELISM="true" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8" \
    MINICONDA_INSTALL_PATH="/opt/conda" \
    distro="ubuntu2004" \
    arch="x86_64" \
    TRITON_MODELS_PATH=GLADIA_TMP_PATH"/triton" \
    TRITON_SERVER_PORT_HTTP=8000 \
    TRITON_SERVER_PORT_GRPC=8001 \
    TRITON_SERVER_PORT_METRICS=8002 \
    PATH_TO_GLADIA_SRC="/app" \
    API_SERVER_PORT_HTTP=8080 \
    API_SERVER_WORKERS=1

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
RUN apt-get install -y apt-transport-https && \
    apt-get clean && \
    apt-get update --allow-insecure-repositories -y

# Install miniconda for python3.8 linux x86 64b
RUN wget "https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-x86_64.sh" && \
    chmod +x Miniconda3-py38_4.11.0-Linux-x86_64.sh && \
    ./Miniconda3-py38_4.11.0-Linux-x86_64.sh -b -p $MINICONDA_INSTALL_PATH && \
    echo ". $MINICONDA_INSTALL_PATH/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate" >> ~/.bashrc

# Install Cmake
RUN apt install -y libssl-dev && \
    wget https://github.com/Kitware/CMake/releases/download/v3.20.0/cmake-3.20.0.tar.gz && \
    tar -zxvf cmake-3.20.0.tar.gz > /dev/null && \
    cd cmake-3.20.0 && ./bootstrap > /dev/null && \
    make && \
    make install

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

SHELL ["/opt/conda/bin/conda", "run", "-n", "base", "/bin/bash", "-c"]

WORKDIR /app

# Install python packages
RUN for package in $(cat /app/requirements.txt); do echo "================="; echo "installing ${package}"; echo "================="; pip3 install $package; done && \
    pip3 install -e ./api_utils/ && \
    pip3 uninstall -y botocore transformers && \
    pip3 install botocore transformers && \
    pip3 install pipenv && \
    pip3 install nltk && \
    pip3 install api_utils/ && \
    sh /app/clean-layer.sh && \
    rm /app/clean-layer.sh

# Build custom envs
RUN if [ "$SKIP_CUSTOM_ENV_BUILD" = "false" ]; then cd /app/venv-builder && python setup_custom_envs.py -x -r /app/apis/ && python setup_custom_envs.py $SETUP_CUSTOM_ENV_BUILD_MODE; fi

# Clean caches
RUN if [ "$SKIP_ROOT_CACHE_CLEANING" = "false" ]; then [ -d "/root/.cache/" ] && rm -rf "/root/.cache/*"; fi && \
    if [ "$SKIP_PIP_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/pip*"; fi && \
    if [ "$SKIP_YARN_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/yarn*"; fi && \
    if [ "$SKIP_NPM_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/npm*"; fi && \
    if [ "$SKIP_TMPFILES_CACHE_CLEANING" = "false" ]; then rm -rf "/tmp/tmp*"; fi && \
    apt-get clean && \
    apt-get autoremove --purge

ENV PATH=$MINICONDA_INSTALL_PATH/bin:$PATH

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

ENTRYPOINT ["/bin/bash"]

CMD ["/app/run_server_prod.sh"]
