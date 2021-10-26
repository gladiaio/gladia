import inflect

def predict(word, count):
    p = inflect.engine()
    return p.plural(word, count)