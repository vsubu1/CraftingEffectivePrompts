
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import os


def mitigate_bias(question,max_tokens):
   
    prompt = f"Provide detaiils for {question}."

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',  #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
            model_type='llama',
            prompt=prompt,
            config={'max_new_tokens': max_tokens,
            'temperature': 0.01})
    
    response=llm(prompt.format(max_new_tokens=max_tokens))

    return response

max_tokens=100
question="Write a job description for a software engineer"
response = mitigate_bias(question,max_tokens)

print("Answer :", response)

