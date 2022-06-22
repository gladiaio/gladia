from transformers import pipeline

def predict(text: str) -> str:
    """
    Generate the continuation of the sentence

    :param text: sentence to continue
    :return: continuation of the sentence
    """

    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

    res = generator(text, max_length=50, do_sample=True, temperature=0.9)

    del generator

    return res[0]['generated_text']
