FROM docker.io/unifai/unifai-base AS dev

ADD clean-layer.sh  /tmp/clean-layer.sh

COPY requirements.txt /tmp/unifai-requirements.txt

RUN for l in $(cat /tmp/unifai-requirements.txt); do echo "================="; echo $l; echo "==============";pip3 install $l; done

RUN pip3 uninstall -y botocore transformers
RUN pip3 install botocore transformers

EXPOSE 80
WORKDIR /app

RUN rm /tmp/clean-layer.sh /tmp/kaggle.log

CMD ["sh", "-c", "echo $PWD && sh run_server_dev.sh"]

FROM scratch AS prod
COPY --from=dev / /
COPY . /app
WORKDIR /app
CMD ["sh", "-c", "echo $PWD && sh run_server_prod.sh"]
