import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def predict(text: str) -> str:
    """
    From a given, classify it between 1 (hate) and 5 (love).

    :param text: text to analyze
    :return: text score [1;5]
    """

    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    input_ids = tokenizer.encode_plus(text, return_tensors="pt")

    sequence_classifier = model(**input_ids)
    predicted_idx = torch.argmax(sequence_classifier[0], dim=1)

    return str(predicted_idx.item() + 1)
