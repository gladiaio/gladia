def predict(sentence: str) -> str:
    """
    For a given sentence, predict the next word.

    :param sentence: sentence to continue
    :return: word predicted
    """

    from happytransformer import HappyWordPrediction

    happy_wp = HappyWordPrediction("ROBERTA", "roberta-base")

    result = happy_wp.predict_mask(f"{sentence} [MASK]")

    return {"prediction": result[0].token, "score": result[0].score}
