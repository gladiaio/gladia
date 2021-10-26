from transformers import AutoTokenizer, AutoModelWithLMHead
import torch
from icecream import ic

def generate(code, tokenizer, model, max_length=100):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    '''Takes input code, replaces newline chars with <N>, 
    tokenizes, feeds thru model, decodes, 
    then reformats the newlines back in'''
    newlinechar = "<N>"
    tokenizer = AutoTokenizer.from_pretrained("Sentdex/GPyT")
    model = AutoModelWithLMHead.from_pretrained("Sentdex/GPyT").to(device)

    converted = code.replace("\n", newlinechar)
    tokenized = tokenizer.encode(converted, return_tensors='pt').to(device)
    resp = model.generate(tokenized, max_length=max_length).to(device)

    decoded = tokenizer.decode(resp[0])
    reformatted = decoded.replace("<N>","\n")
    return reformatted


def predict(code_snippet):

    tokenizer = AutoTokenizer.from_pretrained("Sentdex/GPyT")
    model = AutoModelWithLMHead.from_pretrained("Sentdex/GPyT")
    

    return generate(code_snippet, tokenizer, model)
