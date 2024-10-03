from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Uses  https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

def MultiTunConversationalPrompt(prompt,example):
   
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',  
            model_type='llama',
            prompt=prompt,
            example=example,
            config={'max_new_tokens': 1000,
            'temperature': 0.3})

    response=llm(prompt.format(prompt=prompt, example=example))
    print(response)

# Example usage
prompt = "What is your name?"
example = "My name is John David"
prompt = "Where do you go now?"
example = "I am visiting Central Park in Manhattan"
prompt = "Continue the conversation by asking why does John wants to visit Central park"

answer = MultiTunConversationalPrompt(prompt,example)

print("Answer :", answer)
