
def predict(text: str) -> [(str, float)]:
    """
    Extract keywords from a given sentence

    :param text: sentence to extract the keywords from
    :return: keywords founded in the sentence
    """

    from keybert import KeyBERT
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    kw_model = KeyBERT(model=model)

    out = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words=None)
    
    del model

    return out
