import nltk
from nltk.stem import WordNetLemmatizer 

def predict(sentence):
    lemmatizer = WordNetLemmatizer()
    word_list = nltk.word_tokenize(sentence)
    lemmatized_output = [lemmatizer.lemmatize(w) for w in word_list]

    return lemmatized_output
