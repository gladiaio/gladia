from LanguageIdentifier import predict, rank
import json

def predict(text):
    output = list()
    for k,v in rank(text):
        output.append({'language': k, 'score': v})

    return json.dumps(output)
