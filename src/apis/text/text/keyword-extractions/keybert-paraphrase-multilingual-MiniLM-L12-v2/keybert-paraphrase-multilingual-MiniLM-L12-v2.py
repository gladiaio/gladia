from keybert import KeyBERT
from sentence_transformers import SentenceTransformer


def predict(text):
    sentence_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    kw_model = KeyBERT(model=sentence_model)

    return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words=None)