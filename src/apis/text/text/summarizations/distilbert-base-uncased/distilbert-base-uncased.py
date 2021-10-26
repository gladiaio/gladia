import torch
import numpy as np
import json
from transformers import AutoTokenizer, AutoModelWithLMHead

def predict(text, source_language, min_length, max_length):
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelWithLMHead.from_pretrained("distilbert-base-uncased")
    input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)
    outputs = model(input_ids, labels=input_ids)
    loss, prediction_scores = outputs[:2]
    summary_ids = torch.argmax(prediction_scores, dim=2)
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text