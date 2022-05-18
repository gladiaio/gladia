import numpy as np

from transformers import BertTokenizer
from gladia_api_utils.inference import Inferer, Engine


def predict(text: str) -> str:
    """
    Detect hate from a given text

    :param text: text to analyze
    :return: normal, hate-speech or offensive regarding the level of hate in the text
    """

    LABELS = ["hate-speech", "normal", "offensive"]
    MODEL_NAME = "hate-speech-detection_bert-base-uncased-hatexplain_base_traced"
    TOKENIZER_NAME = 'Hate-speech-CNERG/bert-base-uncased-hatexplain'

    client = Inferer(
        engine=Engine.TRITON,
        model_name=MODEL_NAME,
    )

    tokenizer = BertTokenizer.from_pretrained(TOKENIZER_NAME)

    input_ids = tokenizer(text, return_tensors="pt", max_length=256, padding="max_length").input_ids

    client.engine.register_new_input(shape=(1, 256), datatype='INT32')
    output = client(input_ids.detach().numpy().astype(np.int32))[0]

    return LABELS[np.argmax(output)]
