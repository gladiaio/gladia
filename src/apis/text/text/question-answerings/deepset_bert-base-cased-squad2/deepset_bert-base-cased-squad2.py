from transformers import AutoTokenizer, AutoModelForQuestionAnswering

from unifai_api_utils.model_management import download_models
import torch

def load_model():
    """
    Load a model given a model name
    """
    urls = {
    "dee": {
            "url": "https://huggingface.co/deepset/bert-base-cased-squad2",
            "output_path": "models",
        }
    }

    model_path = download_models(urls)

    #model_path = Path(model_name)

    tokenizer = AutoTokenizer.from_pretrained("deepset/bert-base-cased-squad2")
    model = AutoModelForQuestionAnswering.from_pretrained("deepset/bert-base-cased-squad2")
    return tokenizer, model
    


def predict(context, question):

    tokenizer, model = load_model()

    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    answer_start_scores, answer_end_scores = model(**inputs, return_dict=False)

    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    return answer
