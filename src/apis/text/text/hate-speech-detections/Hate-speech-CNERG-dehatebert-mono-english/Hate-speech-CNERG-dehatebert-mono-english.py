#https://github.com/hate-alert/HateXplain/blob/master/manual_training_inference.py
from pydantic import BaseModel
import torch
from transformers import BertTokenizer, BertForSequenceClassification

def predict(text):
    # load model
    model = BertForSequenceClassification.from_pretrained('Hate-speech-CNERG/bert-base-uncased-hatexplain')
    tokenizer = BertTokenizer.from_pretrained('Hate-speech-CNERG/bert-base-uncased-hatexplain')

    # load model into gpu
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    label = torch.argmax(torch.nn.functional.softmax(outputs.logits,dim=1))

    if (label == 0):
        label = "hate-speech"
    elif (label == 2):
        label = "offensive"
    else:
        label = "normal"


    return label