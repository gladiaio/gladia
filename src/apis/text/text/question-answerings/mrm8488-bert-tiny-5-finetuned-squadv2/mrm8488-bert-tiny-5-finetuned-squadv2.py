import json

def predict(context: str, question: str) -> str:
    """
    Using the given `context`, answer the provided `question`.

    :param context: context to use to answer the question
    :param question: question to answer
    :return: JSON formatted str containing both the answer and the confidence score.
    """

    from happytransformer import HappyQuestionAnswering

    happy_qa = HappyQuestionAnswering("BERT", "mrm8488/bert-tiny-5-finetuned-squadv2")
    result = happy_qa.answer_question(context, question)

    del happy_qa
    
    return json.dumps({'answer': result[0].answer, 'score': result[0].score})
