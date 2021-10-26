from happytransformer import HappyTextClassification
import json


def predict(text):
    happy_tc = HappyTextClassification("DISTILBERT", "distilbert-base-uncased", num_labels=2)    
    result = happy_tc.classify_text(text)
    #print(result)  # TextClassificationResult(label='LABEL_0', score=0.9998761415481567)
    return json.dumps({"label": "POSITIVE" if result.label == "LABEL_0"  else "NEGATIVE", "score": result.score})
