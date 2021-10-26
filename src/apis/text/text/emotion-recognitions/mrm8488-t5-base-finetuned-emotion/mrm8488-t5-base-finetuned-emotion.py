from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def predict(text):
    
    tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")

    model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-emotion")

    input_ids = tokenizer.encode(text, return_tensors='pt')
    
    outputs = model.generate(input_ids)
    
    decoded = tokenizer.decode(outputs[0])
    output = decoded.replace("<pad>", "").replace("</s>", "").strip()

    print(type(output))
    return output

