import os

import numpy as np
from gladia_api_utils.triton_helper import TritonClient


def predict(text: str) -> str:
    """
    From a given, classify it between 1 (hate) and 5 (love).

    :param text: text to analyze
    :return: text score [1;5]
    """

    TRITON_SERVER_URL = os.getenv("TRITON_SERVER_URL", default="localhost:8000")
    MODEL_NAME = "sentiment-analyses_nlptown_bert-base-multilingual-uncased-sentiment_tensorrt_inference"
    MODEL_SUB_PARTS = [
        "sentiment-analyses_nlptown_bert-base-multilingual-uncased-sentiment_tensorrt_model",
        "sentiment-analyses_nlptown_bert-base-multilingual-uncased-sentiment_tensorrt_tokenize",
    ]

    client = TritonClient(
        TRITON_SERVER_URL,
        MODEL_NAME,
        current_path=os.path.split(__file__)[0],
        sub_parts=MODEL_SUB_PARTS,
        output_name="output",
    )

    in0 = np.array([text.encode("utf-8")])
    in0 = np.expand_dims(in0, axis=0)
    in0n = np.array(
        [str(x).encode("utf-8") for x in in0.reshape(in0.size)], dtype=np.object_
    )

    client.register_new_input(name="TEXT", shape=in0n.shape, datatype="BYTES")

    output = client(in0n)[0]

    return output.argmax()
