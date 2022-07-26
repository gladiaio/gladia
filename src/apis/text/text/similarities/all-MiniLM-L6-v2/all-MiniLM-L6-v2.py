def predict(sentence_1: str, sentence_2: str) -> dict:
    """
    For two given sentences, say whether they are similar or not.

    :param sentence_1: first sentence to compare
    :param sentence_2: second sentence to compare
    :return: similarity score (between 0 and 1)
    """

    from sentence_transformers import SentenceTransformer, util

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embedding1 = model.encode(sentence_1, convert_to_tensor=True)
    embedding2 = model.encode(sentence_2, convert_to_tensor=True)

    cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)

    return {"score": cosine_scores.item()}
