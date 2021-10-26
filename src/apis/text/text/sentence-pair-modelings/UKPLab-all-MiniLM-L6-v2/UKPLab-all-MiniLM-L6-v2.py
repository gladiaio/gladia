from sentence_transformers import SentenceTransformer

def predict(sentence):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    sentence_embeddings = model.encode([sentence])
    sentences = [sentence]
    output = list()
    for sentence, embedding in zip(sentences, sentence_embeddings):
        output.append({
            "Sentence":sentence,
            "Embedding": embedding
            })
    
    return output