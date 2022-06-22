
def predict(sentence: str) -> str:
    """
    For a given sentence, predict the next word.

    :param sentence: sentence to continue
    :return: word predicted
    """

    from happytransformer import HappyWordPrediction

    happy_wp = HappyWordPrediction(model_type="ALBERT", model_name="albert-base-v2")

    result = happy_wp.predict_mask(f"{sentence} [MASK]")

    del happy_wp

    return result[0].token
