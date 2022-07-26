def predict(text: str) -> dict:
    """
    For a given text, predict if it's POSITIVE or NEGATIVE

    :param text: text to analyze.
    :return: JSON formatted str containing the label (POSITIVE/NEGATIVE) with it score
    """

    from happytransformer import HappyTextClassification

    happy_tc = HappyTextClassification(
        model_type="DISTILBERT",
        model_name="distilbert-base-uncased-finetuned-sst-2-english",
    )
    result = happy_tc.classify_text(text)

    return {"label": result.label, "score": result.score}
