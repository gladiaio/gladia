from transformers import pipeline

def predict(text):
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

    res = generator(text, max_length=50, do_sample=True, temperature=0.9)

    return res[0]['generated_text']
