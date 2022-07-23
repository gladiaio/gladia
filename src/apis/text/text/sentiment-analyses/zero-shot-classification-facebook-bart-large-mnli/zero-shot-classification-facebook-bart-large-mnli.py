import numpy as np
from transformers import pipeline


def predict(text: str) -> dict:
    """
    For a given text, predict if it's POSITIVE, NEUTRAL or NEGATIVE

    :param text: text to analyze.
    :return: Dict formatted dict containing the label (POSITIVE/NEUTRAL/NEGATIVE) with it score
    """

    classifier = pipeline("zero-shot-classification")
    prediction = classifier(text, candidate_labels=["POSITIVE", "NEUTRAL", "NEGATIVE"])

    label = prediction["labels"][np.argmax(prediction["scores"])]
    score = np.amax(prediction["scores"])

    return {"label": label, "score": score}
