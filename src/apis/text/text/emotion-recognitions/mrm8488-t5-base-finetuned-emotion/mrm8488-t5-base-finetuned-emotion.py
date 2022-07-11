from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def predict(text: str) -> str:
    """
    From a given sentence, return the emotion detected in it

    :param text: sentence to analyse emotion from
    :return: emotion contained in the sentence
    """

    model_name = "mrm8488/t5-base-finetuned-emotion"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    input_ids = tokenizer.encode(text, return_tensors="pt")

    outputs = model.generate(input_ids)

    decoded = tokenizer.decode(
        outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True
    )

    del model
    del tokenizer

    return decoded
