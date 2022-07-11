import torch
from transformers import (
    AutoModelForQuestionAnswering,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
)


def load_model() -> (PreTrainedTokenizer, PreTrainedModel):
    """
    Load `deepset/bert-base-cased-squad2` tokenizer and model.

    :return: tuple containing both the tokenizer and the model
    """

    model_name = "deepset/bert-base-cased-squad2"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)

    return tokenizer, model


def predict(context: str, question: str) -> str:
    """
    Using the given `context`, answer the provided `question`.

    Note: The score is not provided in the return value.

    :param context: context to use to answer the question
    :param question: question to answer
    :return: answer of the question
    """

    tokenizer, model = load_model()

    inputs = tokenizer.encode_plus(
        question, context, add_special_tokens=True, return_tensors="pt"
    )
    input_ids = inputs["input_ids"].tolist()[0]

    answer_start_scores, answer_end_scores = model(**inputs, return_dict=False)

    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end])
    )

    return answer
