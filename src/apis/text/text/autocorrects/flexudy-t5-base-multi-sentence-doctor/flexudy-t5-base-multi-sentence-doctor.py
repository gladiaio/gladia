from transformers import AutoTokenizer, AutoModelWithLMHead

def predict(sentence):
    tokenizer = AutoTokenizer.from_pretrained("flexudy/t5-base-multi-sentence-doctor")

    model = AutoModelWithLMHead.from_pretrained("flexudy/t5-base-multi-sentence-doctor")

    input_text = f"repair_sentence: {sentence}</s>"

    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    outputs = model.generate(input_ids, max_length=32, num_beams=1)

    sentence = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

    return sentence
