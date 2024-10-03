
from langchain.llms import CTransformers


def self_consistent_prompt(question):
   
    context=""
    prompt_with_context = f"{context}\n\nPrompt: {question}"

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin', 
            model_type='llama',
            question=prompt_with_context,
            config={'max_new_tokens': 200,
            'temperature': 0.01})
    
    response=llm(prompt_with_context.format(question=question))

    return response

question =  "Explain the concept of artificial intelligence."
answer = self_consistent_prompt(question)

print("Answer :", answer)

