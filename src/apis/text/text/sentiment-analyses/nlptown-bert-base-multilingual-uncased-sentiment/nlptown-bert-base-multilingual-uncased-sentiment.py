import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification


def predict(text):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

    model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

    input_ids = tokenizer.encode_plus(text, return_tensors="pt")

    sequence_classifier = model(**input_ids)
    predict_softmax = torch.softmax(sequence_classifier[0], dim=1)

    predicted_idx = predict_softmax.argmax(dim=-1)

    #return ("positive" if predicted_idx >=3 else "negative") 
    return str(predicted_idx.item() + 1)
    