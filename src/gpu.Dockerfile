ARG GLADIA_DOCKER_BASE=docker.io/gladiaio/gladia-base:latest

FROM $GLADIA_DOCKER_BASE

ADD clean-layer.sh  /tmp/clean-layer.sh

COPY requirements.txt /tmp/gladia-requirements.txt

RUN for package in $(cat /tmp/gladia-requirements.txt); do echo "================="; echo "installing ${package}"; echo "================="; pip3 install $package; done

#RUN pip3 install mmcv-full -f https://download.openmmlab.com/mmcv/dist/1.3.5/torch1.7.0/cu110/mmcv_full-latest%2Btorch1.7.0%2Bcu110-cp37-cp37m-manylinux1_x86_64.whl

RUN pip uninstall -y gladia-api-utils

ARG GLADIA_API_UTILS_BRANCH=main
RUN pip3 install git+https://github.com/gladiaio/gladia-api-utils.git\@$GLADIA_API_UTILS_BRANCH

RUN pip3 uninstall -y botocore transformers
RUN pip3 install botocore transformers

RUN rm /tmp/clean-layer.sh

ENV PIPENV_VENV_IN_PROJECT="enabled"

ENV TOKENIZERS_PARALLELISM="true"

ENV TRANSFORMERS_CACHE="/tmp/gladia/models/transformers"
ENV PYTORCH_TRANSFORMERS_CACHE="/tmp/gladia/models/pytorch_transformers"
ENV PYTORCH_PRETRAINED_BERT_CACHE=="/tmp/gladia/models/pytorch_pretrained_bert"

COPY . /app
WORKDIR /app

# add build options to setup_custom_envs
# can be -f to force rebuild of env if already exist
# -p 1 is set by default for stability purposes
ARG SETUP_CUSTOM_ENV_BUILD_MODE=" -p 1 "
RUN python3 setup_custom_envs.py $SETUP_CUSTOM_ENV_BUILD_MODE

# import omw
RUN python3 -c 'import nltk ;nltk.download("omw-1.4")'

EXPOSE 80

CMD ["sh", "-c", "echo $PWD && sh run_server_prod.sh"]
