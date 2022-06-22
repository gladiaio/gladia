import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def predict(context: str) -> [str]:
    """
    Generates paraphrases of the given sentence

    :param context: sentence to paraphrase
    :return: list of paraphrases
    """

    model_name = "ramsrigouthamg/t5-large-paraphraser-diverse-high-quality"

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
    model.eval()

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    text = f"paraphrase: {context}</s>"

    encoding = tokenizer.encode_plus(text, max_length=128, padding='max_length', return_tensors="pt")
    input_ids, attention_mask = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)

    beam_outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=128,
        early_stopping=True,
        num_beams=15,
        num_beam_groups=5,
        num_return_sequences=5,
        diversity_penalty=0.70

    )

    output = []

    for beam_output in beam_outputs:
        sent = tokenizer.decode(beam_output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        output.append(sent.replace("paraphrasedoutput: ", ""))
    del tokenizer
    del model
    del encoding
    del beam_outputs
    return output
