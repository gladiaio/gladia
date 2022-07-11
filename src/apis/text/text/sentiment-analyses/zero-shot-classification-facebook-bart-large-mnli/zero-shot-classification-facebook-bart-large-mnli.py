import json

import numpy as np
from transformers import pipeline


def predict(text: str) -> str:
    """
    For a given text, predict if it's POSITIVE, NEUTRAL or NEGATIVE

    :param text: text to analyze.
    :return: JSON formatted str containing the label (POSITIVE/NEUTRAL/NEGATIVE) with it score
    """

    classifier = pipeline("zero-shot-classification")
    prediction = classifier(text, candidate_labels=["POSITIVE", "NEUTRAL", "NEGATIVE"])

    label = prediction["labels"][np.argmax(prediction["scores"])]
    score = np.amax(prediction["scores"])

    return json.dumps({"label": label, "score": score})
