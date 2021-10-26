from sentence_transformers import SentenceTransformer, util
import numpy as np

def predict(sentence_1, sentence_2):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    embedding1 = model.encode(sentence_1, convert_to_tensor=True)
    embedding2 = model.encode(sentence_2, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)

    return str(cosine_scores.item())