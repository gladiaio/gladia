from transformers import pipeline

def predict(input_string):

    nlp = pipeline("ner")
    entities = nlp(input_string)
    
    return entities