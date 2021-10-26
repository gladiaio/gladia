from happytransformer import HappyWordPrediction

def predict(sentence):
    happy_wp = HappyWordPrediction("ROBERTA", "roberta-base")
    result = happy_wp.predict_mask(f"{sentence} [MASK]")
    return result[0].token
