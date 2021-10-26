from transformers import TextClassificationPipeline
from transformers import RobertaForSequenceClassification
from transformers import RobertaTokenizer

CODEBERTA_LANGUAGE_ID = "huggingface/CodeBERTa-language-id"

def predict(code_snippet):

    pipeline = TextClassificationPipeline(
        model=RobertaForSequenceClassification.from_pretrained(CODEBERTA_LANGUAGE_ID),
        tokenizer=RobertaTokenizer.from_pretrained(CODEBERTA_LANGUAGE_ID)
    )

    output = pipeline(code_snippet)

    outputs = []
    for elem in output:
        outputs.append({'language': elem['label'], 'score': elem['score']})
    
    return outputs

