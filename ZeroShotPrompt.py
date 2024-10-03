

from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def zero_shot_prompt(question):
   
    prompt = f"Explain {question}."

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',  #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
            model_type='llama',
            prompt=prompt,
            config={'max_new_tokens': 250,
            'temperature': 0.01})
    
    response=llm(prompt.format(question=question))

    return response

question = "A triangle has three _____"
answer = zero_shot_prompt(question)

print("Answer :", answer)


