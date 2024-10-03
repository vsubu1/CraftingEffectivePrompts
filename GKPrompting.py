
from langchain.llms import CTransformers

def GK_prompt(question):
   
    prompt = f"Explain the concept of {question} "

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
            model_type='llama',
            prompt=prompt,
            config={'max_new_tokens': 100,
            'temperature': 0.8})
    
    response=llm(prompt.format(question=question))

    return response

question = "gravity"

answer = GK_prompt(question)

print("answer :", answer)

