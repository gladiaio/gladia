from happytransformer import HappyQuestionAnswering
import json
def predict(context, question):
    
    happy_qa = HappyQuestionAnswering("ALBERT", "mfeb/albert-xxlarge-v2-squad2")
    result = happy_qa.answer_question(context, question)
    print(type(result))  # <class 'list'>
    print(result)  # [QuestionAnsweringResult(answer='January 10th, 2021', score=0.9711642265319824, start=16, end=34)]
    print(type(result[0]))  # <class 'happytransformer.happy_question_answering.QuestionAnsweringResult'>
    print(result[0])  # QuestionAnsweringResult(answer='January 10th, 2021', score=0.9711642265319824, start=16, end=34)
    print(result[0].answer)  # January 10th, 2021
    return json.dumps({'answer': result[0].answer, 'score': result[0].score})