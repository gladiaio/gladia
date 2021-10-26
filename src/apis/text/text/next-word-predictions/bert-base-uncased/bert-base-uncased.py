from happytransformer import HappyWordPrediction

def predict(sentence):
    happy_wp = HappyWordPrediction("BERT", "bert-base-uncased")
    result = happy_wp.predict_mask(f"{sentence} [MASK]")
    return result[0].token
