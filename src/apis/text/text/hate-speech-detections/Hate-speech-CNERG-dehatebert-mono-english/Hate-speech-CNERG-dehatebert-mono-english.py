import os

# from time import sleep
from warnings import warn

import numpy as np
import requests
from gladia_api_utils.triton_helper import TritonClient
from transformers import BertTokenizer

# import tritonclient.http as tritonclient


# from gladia_api_utils.triton_helper import download_triton_model


def predict(text: str) -> str:
    """
    Detect hate from a given text

    :param text: text to analyze
    :return: normal, hate-speech or offensive regarding the level of hate in the text
    """

    LABELS = ["hate-speech", "normal", "offensive"]
    MODEL_NAME = "hate-speech-detection_bert-base-uncased-hatexplain_base_traced"
    TOKENIZER_NAME = "Hate-speech-CNERG/bert-base-uncased-hatexplain"
    TRITON_SEVER_URL = os.getenv("TRITON_SERVER_URL", default="localhost:8000")

    client = TritonClient(
        TRITON_SEVER_URL, MODEL_NAME, current_path=os.path.split(__file__)[0]
    )

    tokenizer = BertTokenizer.from_pretrained(TOKENIZER_NAME)

    input_ids = tokenizer(
        text, return_tensors="pt", max_length=256, padding="max_length"
    ).input_ids

    client.register_new_input(shape=(1, 256), datatype="INT32")
    output = client(input_ids.detach().numpy().astype(np.int32))[0]

    out = LABELS[np.argmax(output)]

    del tokenizer

    return out
