
from langchain.llms import CTransformers

def tree_of_thoughts(question):
   
    context=""
    prompt_with_context = f"{context}\n\nPrompt: {question}"

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',  #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
            model_type='llama',
            question=prompt_with_context,
            config={'max_new_tokens': 300,
            'temperature': 0.01})
    
    response=llm(prompt_with_context.format(question=question))

    return response

questions = [
        "Explain the concept of artificial intelligence.",
        "Discuss the applications of AI in real-world scenarios.",
        "What are the ethical considerations related to AI?"
    ]

answer = tree_of_thoughts(questions)

print("Answer :", answer)


