import sys

import numpy as np
from gladia_api_utils.triton_helper import (
    TritonClient,
    check_if_model_needs_to_be_preloaded,
    data_processing,
)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def predict(text: str) -> [(str, float)]:
    """
    Extract keywords from a given sentence

    :param text: sentence to extract the keywords from
    :return: keywords founded in the sentence
    """
    from keybert import KeyBERT
    from sentence_transformers import SentenceTransformer

    MODEL_NAME = "sentence-transformers_paraphrase-MiniLM-L6-v2_tensorrt_inference"
    MODEL_SUB_PARTS = [
        "sentence-transformers_paraphrase-MiniLM-L6-v2_tensorrt_model",
        "sentence-transformers_paraphrase-MiniLM-L6-v2_tensorrt_tokenize",
    ]

    client = TritonClient(
        model_name=MODEL_NAME,
        sub_parts=MODEL_SUB_PARTS,
        output_name="output",
        preload_model=check_if_model_needs_to_be_preloaded(MODEL_NAME),
    )

    # text = "Hello world!"
    text = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs. It infers a
         function from labeled training data consisting of a set of training examples.
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal).
         A supervised learning algorithm analyzes the training data and produces an inferred function,
         which can be used for mapping new examples.
      """

    text_preprocessed = data_processing.text_to_numpy(text)
    client.set_input(name="TEXT", shape=text_preprocessed.shape, datatype="BYTES")
    print(text_preprocessed, file=sys.stderr)
    str_embeddings = client(text_preprocessed)[0]

    print(str_embeddings, file=sys.stderr)

    count = CountVectorizer(
        ngram_range=(1, 1),
        stop_words=None,
        min_df=1,
    ).fit([text])
    words = count.get_feature_names_out()
    df = count.transform([text])

    print(count, file=sys.stderr)
    print(words, file=sys.stderr)
    print(df, file=sys.stderr)

    # Find keywords
    all_keywords = []

    word_embeddings = []
    for word in words:
        word_preprocessed = data_processing.text_to_numpy(word)
        client.set_input(name="TEXT", shape=word_preprocessed.shape, datatype="BYTES")
        word_embeddings.append(client(word_preprocessed)[0])
    word_embeddings = np.array(word_embeddings)

    # Select embeddings
    candidate_indices = df[0].nonzero()[1]
    print(candidate_indices, file=sys.stderr)
    candidates = [words[index] for index in candidate_indices]
    candidate_embeddings = word_embeddings[candidate_indices]
    print("-----", candidate_embeddings.shape, file=sys.stderr)
    candidate_embeddings = candidate_embeddings.reshape(51, -1)
    doc_embedding = np.array(str_embeddings).reshape(1, -1)

    print("------------------------------", doc_embedding.shape, file=sys.stderr)
    print(np.array(candidate_embeddings).shape, file=sys.stderr)

    top_n = 5
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    keywords = [
        (candidates[index], round(float(distances[0][index]), 4))
        for index in distances.argsort()[0][-top_n:]
    ][::-1]

    all_keywords.append(keywords)

    # model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
    # kw_model = KeyBERT(model=model)

    # out = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words=None)

    # del model

    return all_keywords
