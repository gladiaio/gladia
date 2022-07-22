import os
import json
import numpy as np

from typing import List
from gladia_api_utils.triton_helper import TritonClient


def predict(text: str) -> List[dict]:
    """
    Apply NER on the given task and return each token within the sentence associated to its label.

    **Labels**:\n
    O : Outside of a named entity\n
    B-MISC : Beginning of a miscellaneous entity right after another miscellaneous entity\n
    I-MISC : Miscellaneous entity\n
    B-PER : Beginning of a person's name right after another person's name\n
    I-PER : Person's name\n
    B-ORG : Beginning of an organisation right after another organisation\n
    I-ORG : Organisation\n
    B-LOC : Beginning of a location right after another location\n
    I-LOC : Location\n

    :param text: sentence to search the named entities in
    :return: entities founded in the string
    """

    MODEL_NAME = "named-entity-recognition_dbmdz_bert-large-cased-finetuned-conll03-english_tensorrt_inference"
    MODEL_SUB_PARTS = [
        "named-entity-recognition_dbmdz_bert-large-cased-finetuned-conll03-english_tensorrt_model",
    ]

    client = TritonClient(
        model_name=MODEL_NAME,
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

    output = client(in0n)[0].decode('utf8')

    return json.loads(output)[0]
