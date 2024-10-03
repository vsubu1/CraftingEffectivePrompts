
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def temperature_control_prompt(question, temperature):
   
    prompt = f"Explain the concept of {question}."

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
            model_type='llama',
            prompt=prompt,
            config={'max_new_tokens': 100,
            'temperature': temperature})
    
    response=llm(prompt.format(question=question,temperature=temperature))

    return response

question = "What is the difference between happiness and joy?"
answer_low_temp = temperature_control_prompt(question, temperature=0.7)
answer_high_temp = temperature_control_prompt(question, temperature=2)

print("Answer (Low Temperature):", answer_low_temp)
print("Answer (High Temperature):", answer_high_temp)

