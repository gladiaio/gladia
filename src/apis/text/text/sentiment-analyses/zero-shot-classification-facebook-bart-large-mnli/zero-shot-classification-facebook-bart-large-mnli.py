from transformers import pipeline
import numpy as np
import json

def predict(text):
    classifier = pipeline("zero-shot-classification")
    prediction = classifier(
        text,
        candidate_labels=["POSITIVE", "NEUTRAL", "NEGATIVE"],
    )

#    {'sequence': 'This is a course about the Transformers library',
#     'labels': ['education', 'business', 'politics'],
#    'scores': [0.8445963859558105, 0.111976258456707, 0.043427448719739914]}
    label = prediction['labels'][np.argmax(prediction['scores'])]
    score = np.amax(prediction['scores'])
    return json.dumps({"label": label, "score": score})

