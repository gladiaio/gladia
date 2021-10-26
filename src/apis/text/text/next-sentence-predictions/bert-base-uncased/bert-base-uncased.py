from happytransformer import HappyNextSentence

def predict(sentence_1, sentence_2):
    happy_ns = HappyNextSentence("BERT", "bert-base-uncased")
    
    result = happy_ns.predict_next_sentence(
        sentence_1,
        sentence_2
    )

    return result

