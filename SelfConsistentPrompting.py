from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def token_control_prompt(question, max_new_tokens=100):
    prompt = f"Explain the concept of {question}."

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        prompt=prompt,
                        config={'max_new_tokens': max_new_tokens,
                                'temperature': 0.7})

    response = llm(prompt)

    return response

question = " Happiness "
answer_max_tokens = token_control_prompt(question, max_new_tokens=100)
answer_min_tokens = token_control_prompt(question, max_new_tokens=25)

print("Answer (Max tokens):", answer_max_tokens)
print("Answer (Min tokens):", answer_min_tokens)
