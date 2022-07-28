from gladia_api_utils.triton_helper import (
    TritonClient,
    check_if_model_needs_to_be_preloaded,
    data_processing,
)
from torch import mm, tensor
from torch.nn.functional import normalize


def cos_sim(a: list, b: list):
    """
    For two given sentences embeddings a and b, computes the cosine similarity

    :param sentence_1: first sentence embeddings to compare
    :param sentence_2: second sentence embeddings to compare
    :return: tensor with similarity score (between 0 and 1)
    """
    return mm(
        normalize(tensor(a), p=2, dim=1),
        normalize(tensor(b), p=2, dim=1).transpose(0, 1),
    )


def predict(sentence_1: str, sentence_2: str) -> dict:
    """
    For two given sentences, say whether they are similar or not.

    :param sentence_1: first sentence to compare
    :param sentence_2: second sentence to compare
    :return: similarity score (between 0 and 1)
    """

    MODEL_NAME = "sentence-transformers_all-MiniLM-L6-v2_tensorrt_inference"
    MODEL_SUB_PARTS = [
        "sentence-transformers_all-MiniLM-L6-v2_tensorrt_model",
        "sentence-transformers_all-MiniLM-L6-v2_tensorrt_tokenize",
    ]

    client = TritonClient(
        model_name=MODEL_NAME,
        sub_parts=MODEL_SUB_PARTS,
        output_name="output",
        preload_model=check_if_model_needs_to_be_preloaded(MODEL_NAME),
    )

    sentence_1_preprocessed = data_processing.text_to_numpy(sentence_1)
    sentence_2_preprocessed = data_processing.text_to_numpy(sentence_2)

    client.set_input(name="TEXT", shape=sentence_1_preprocessed.shape, datatype="BYTES")
    sentence_1_embeddings = client(sentence_1_preprocessed)[0]

    client.set_input(name="TEXT", shape=sentence_2_preprocessed.shape, datatype="BYTES")
    sentence_2_embeddings = client(sentence_2_preprocessed)[0]

    cosine_scores = cos_sim(sentence_1_embeddings, sentence_2_embeddings)

    return {"score": cosine_scores.item()}
