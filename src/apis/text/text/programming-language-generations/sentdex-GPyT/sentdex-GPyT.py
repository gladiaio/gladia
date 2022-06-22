import torch

from transformers import AutoTokenizer, AutoModelWithLMHead, PreTrainedTokenizer, PreTrainedModel


def generate(code: str, tokenizer: PreTrainedTokenizer, model: PreTrainedModel, max_length: int = 100) -> str:
    """
    Takes input code, replaces newline chars with <N>,
    tokenizes, feeds through model, decodes, then reformat the newlines back in.

    :param code: code to continue
    :param tokenizer: tokenizer to use
    :param model: model to use
    :param max_length: maximum length to continue up to
    :return: generated code
    """

    new_line_token = "<N>"

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    converted = code.replace("\n", new_line_token)

    tokenized = tokenizer.encode(converted, return_tensors='pt').to(device)
    resp = model.generate(tokenized, max_length=max_length).to(device)

    decoded = tokenizer.decode(resp[0])
    reformatted = decoded.replace(new_line_token, "\n")

    return reformatted


def predict(code_snippet: str) -> str:
    """
    Generate the continuation of the provided `code_snippet`.

    :param code_snippet:
    :return:
    """

    model_name = "Sentdex/GPyT"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelWithLMHead.from_pretrained(model_name)

    out = generate(code_snippet, tokenizer, model)

    del model
    del tokenizer

    return out
