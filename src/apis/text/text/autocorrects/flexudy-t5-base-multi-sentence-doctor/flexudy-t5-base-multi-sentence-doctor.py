from transformers import AutoModelWithLMHead, AutoTokenizer


def predict(sentence: str) -> str:
    """
    Remove typos from the given string.

    :param sentence: sentence to correct
    :return: sentence corrected
    """

    model_name = "flexudy/t5-base-multi-sentence-doctor"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelWithLMHead.from_pretrained(model_name)

    input_text = f"repair_sentence: {sentence}</s>"

    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    outputs = model.generate(input_ids, max_length=32, num_beams=1)

    sentence = tokenizer.decode(
        outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True
    )

    return sentence
