import torch

from transformers import BertTokenizer, BertForSequenceClassification

def predict(text: str) -> str:
    """
    Detect hate from a given text

    :param text: text to analyze
    :return: normal, hate-speech or offensive regarding the level of hate in the text
    """

    labels = ["hate-speech", "normal", "offensive"]
    model_name = 'Hate-speech-CNERG/bert-base-uncased-hatexplain'

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model = BertForSequenceClassification.from_pretrained(model_name)
    model.to(device)

    tokenizer = BertTokenizer.from_pretrained(model_name)

    input = tokenizer(text, return_tensors="pt")

    input = input.to(device)

    outputs = model(**input)

    return labels[torch.argmax(outputs.logits, dim=1)]
