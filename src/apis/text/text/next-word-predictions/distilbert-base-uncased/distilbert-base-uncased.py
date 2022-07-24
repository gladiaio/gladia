def predict(sentence: str) -> dict:
    """
    For a given sentence, predict the next word.

    :param sentence: sentence to continue
    :return: word predicted and score
    """

    from happytransformer import HappyWordPrediction

    happy_wp = HappyWordPrediction("DISTILBERT", "distilbert-base-uncased")

    result = happy_wp.predict_mask(f"{sentence} [MASK]")

    del happy_wp

    return {"prediction": result[0].token, "score": result[0].score}
