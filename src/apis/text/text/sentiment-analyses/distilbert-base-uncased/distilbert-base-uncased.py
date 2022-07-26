def predict(text: str) -> dict:
    """
    For a given text, predict if it's POSITIVE or NEGATIVE

    :param text: text to analyze.
    :return: JSON formatted str containing the label (POSITIVE/NEGATIVE) with it score
    """

    from happytransformer import HappyTextClassification

    happy_tc = HappyTextClassification(
        "DISTILBERT", "distilbert-base-uncased", num_labels=2
    )
    result = happy_tc.classify_text(text)

    return {
        "label": "POSITIVE" if result.label == "LABEL_0" else "NEGATIVE",
        "score": result.score,
    }
