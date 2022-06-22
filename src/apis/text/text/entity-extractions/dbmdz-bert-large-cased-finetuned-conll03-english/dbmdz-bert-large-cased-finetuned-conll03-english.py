import os
import numpy as np

from transformers import AutoTokenizer
from gladia_api_utils.triton_helper import TritonClient


def softmax(x: [float]) -> [float]:
    """Apply sofmax on the vector `x`

    Args:
        x ([float]): vector of float to apply softmax on

    Returns:
        [float]: vector x after softmax
    """
    return np.exp(x) / np.sum(np.exp(x))


def predict(input_string: str) -> [dict]:
    """
    Extract the named entity from a given string

    :param input_string: string to extract the entities from
    :return: entities founded in the string
    """

    NONE_LABEL = "O"
    LABELS = [NONE_LABEL, "B-MISC", "I-MISC", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC"]
    MODEL_NAME = "ner_bert-large-cased-finetuned-conll03-english_base_traced"
    TOKENIZER_NAME = 'dbmdz/bert-large-cased-finetuned-conll03-english'
    TRITON_SEVER_URL = os.getenv("TRITON_SERVER_URL", default='localhost:8000')

    client = TritonClient(
        TRITON_SEVER_URL,
        MODEL_NAME,
        current_path=os.path.split(__file__)[0]
    )

    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME)

    input_ids = tokenizer(input_string, return_tensors="pt", max_length=256, padding="max_length").input_ids

    client.register_new_input(shape=(1, 256), datatype='INT32')
    outputs = client(input_ids.detach().numpy().astype(np.int32))[0]

    predictions = []
    for (idx, output), token in zip(enumerate(outputs), tokenizer.batch_decode(input_ids.permute(dims=(1,0)))):
        if token in ["[CLS]", "[SEP]", "[PAD]"]:
            continue
            
        label = LABELS[np.argmax(output)]

        if label == NONE_LABEL:
            continue
        
        pred = {
            'entity': label,
            'score': np.max(softmax(output)),
            'index': idx,
            'word': token
        }

        predictions.append(pred)

    del tokenizer
    
    return predictions
