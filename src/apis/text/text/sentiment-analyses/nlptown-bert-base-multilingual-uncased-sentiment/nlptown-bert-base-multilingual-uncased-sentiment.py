import os

from gladia_api_utils.triton_helper import (
    TritonClient,
    check_if_model_needs_to_be_preloaded,
    data_processing,
)


def predict(text: str) -> str:
    """
    From a given, classify it between 1 (hate) and 5 (love).

    :param text: text to analyze
    :return: text score [1;5]
    """

    MODEL_NAME = "sentiment-analyses_nlptown_bert-base-multilingual-uncased-sentiment_tensorrt_inference"
    MODEL_SUB_PARTS = [
        "sentiment-analyses_nlptown_bert-base-multilingual-uncased-sentiment_tensorrt_model",
        "sentiment-analyses_nlptown_bert-base-multilingual-uncased-sentiment_tensorrt_tokenize",
    ]

    client = TritonClient(
        model_name=MODEL_NAME,
        current_path=os.path.split(__file__)[0],
        sub_parts=MODEL_SUB_PARTS,
        output_name="output",
        preload_model=check_if_model_needs_to_be_preloaded(MODEL_NAME),
    )

    numpy_input = data_processing.text_to_numpy(text)

    client.set_input(name="TEXT", shape=numpy_input.shape, datatype="BYTES")

    output = client(numpy_input)[0][0]

    return output.index(max(output))
