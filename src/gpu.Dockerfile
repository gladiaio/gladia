ARG GLADIA_DOCKER_BASE=docker.io/gladiaio/gladia-base:latest

FROM $GLADIA_DOCKER_BASE

ADD clean-layer.sh  /tmp/clean-layer.sh

COPY requirements.txt /tmp/gladia-requirements.txt

RUN for package in $(cat /tmp/gladia-requirements.txt); do echo "================="; echo "installing ${package}"; echo "================="; pip3 install $package; done

RUN pip uninstall -y gladia-api-utils

ARG GLADIA_API_UTILS_BRANCH=main
RUN pip3 install git+https://github.com/gladiaio/gladia-api-utils.git\@$GLADIA_API_UTILS_BRANCH

RUN pip3 uninstall -y botocore transformers
RUN pip3 install botocore transformers

RUN rm /tmp/clean-layer.sh

ENV PIPENV_VENV_IN_PROJECT="enabled"
ENV TOKENIZERS_PARALLELISM="true"
COPY . /app
WORKDIR /app

RUN python3 setup_custom_envs.py
EXPOSE 80

CMD ["sh", "-c", "echo $PWD && sh run_server_prod.sh"]
