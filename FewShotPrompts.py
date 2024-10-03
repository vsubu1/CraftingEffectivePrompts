
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def few_shot_prompt(prompt,example):
   
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',  #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
            model_type='llama',
            prompt=prompt,
            example=example,
            config={'max_new_tokens': 250,
            'temperature': 0.03})
    
    response=llm(prompt.format(prompt=prompt, example=example))

    return response

  # Provide a prompt and a few examples
prompt = "What is your name?"
example = "My name is John David"
prompt = "Continue the conversation by asking about his interests."

answer = few_shot_prompt(prompt,example)

print("Answer :", answer)

