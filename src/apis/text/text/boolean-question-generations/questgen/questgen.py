from pprint import pprint
import nltk
nltk.download('stopwords')
from Questgen import main
import json

def predict(text):
    qe= main.BoolQGen()
    payload = {
        "input_text": text
        }
    output = qe.predict_boolq(payload)
    return json.dumps(output)