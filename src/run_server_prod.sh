python warm_up.py

API_SERVER_PORT_HTTP="${API_SERVER_PORT_HTTP:-8080}"
API_SERVER_WORKERS="${API_SERVER_WORKERS:-1}"

tritonserver \
  --http-port ${TRITON_SERVER_PORT_HTTP} \
  --grpc-port ${TRITON_SERVER_PORT_GRPC} \
  --metrics-port ${TRITON_SERVER_PORT_METRICS} \
  --model-repository=${TRITON_MODELS_PATH} \
  --exit-on-error=false \
  --model-control-mode=explicit \
  --repository-poll-secs 10 \
  --allow-metrics=false & uvicorn main:app --host 0.0.0.0 --port ${API_SERVER_PORT_HTTP} --workers ${API_SERVER_WORKERS}
