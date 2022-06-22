import torch

from transformers import AutoTokenizer, AutoModelForTokenClassification

def predict(text: str) -> [(str, str)]:
    """
    Apply NER on the given task and return each token within the sentence associated to its label.

    **Labels**:\n
    O : Outside of a named entity\n
    B-MISC : Beginning of a miscellaneous entity right after another miscellaneous entity\n
    I-MISC : Miscellaneous entity\n
    B-PER : Beginning of a person's name right after another person's name\n
    I-PER : Person's name\n
    B-ORG : Beginning of an organisation right after another organisation\n
    I-ORG : Organisation\n
    B-LOC : Beginning of a location right after another location\n
    I-LOC : Location\n

    :param text: sentence to search the named entities in
    :return: each token within the sentence associated to its label
    """

    tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")
    model = AutoModelForTokenClassification.from_pretrained("dbmdz/bert-large-cased-finetuned-conll03-english")

    label_list = [
        "O",       # Outside of a named entity
        "B-MISC",  # Beginning of a miscellaneous entity right after another miscellaneous entity
        "I-MISC",  # Miscellaneous entity
        "B-PER",   # Beginning of a person's name right after another person's name
        "I-PER",   # Person's name
        "B-ORG",   # Beginning of an organisation right after another organisation
        "I-ORG",   # Organisation
        "B-LOC",   # Beginning of a location right after another location
        "I-LOC"    # Location
    ]

    # Bit of a hack to get the tokens with the special tokens
    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))
    inputs = tokenizer.encode(text, return_tensors="pt")

    outputs = model(inputs)[0]
    predictions = torch.argmax(outputs, dim=2)

    del tokenizer
    del model

    return [(token, label_list[prediction]) for token, prediction in zip(tokens, predictions[0].tolist())]
