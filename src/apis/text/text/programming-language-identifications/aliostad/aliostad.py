import os

import numpy as np
import tensorflow as tf
from unifai_api_utils.model_management import download_models
from tensorflow import keras

import data_helper
import defs

urls = {
    "aliostad": {
        "url": "https://huggingface.co/databuzzword/aliostad-programming-language-detection",
        "output_path": "models",
    }
}

def load_model():
    models_path = download_models(urls)

    model = keras.models.load_model(os.path.join(models_path["aliostad"]["output_path"], "save_tmp.h5"))
    graph = tf.compat.v1.get_default_graph()
    return model, graph


def predict(code_snippet):
    results = []

    characters_truncation_limit = 2 * 1024

    model, graph = load_model()
    
    x = data_helper.turn_text_to_vector(code_snippet, characters_truncation_limit, normalise_whitespace=True)
    x = np.expand_dims(x, axis=0)

    with graph.as_default():
        y = model.predict(x)
        result = model.predict_proba(x)

    for i in range(0, len(defs.langs)):
        if (y[0][i] > 0.5):
            results.append({"language": defs.langs[i], "score": round(100 * y[0][i])})
    
    return results

    




