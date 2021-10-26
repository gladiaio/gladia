from happytransformer import HappyTextClassification
import json

def predict(text):
    happy_tc = HappyTextClassification(model_type="DISTILBERT",  model_name="distilbert-base-uncased-finetuned-sst-2-english")
    result = happy_tc.classify_text(text)
    #print(result)  # TextClassificationResult(label='POSITIVE', score=0.9998761415481567)
    return json.dumps({"label": result.label, "score": result.score})
