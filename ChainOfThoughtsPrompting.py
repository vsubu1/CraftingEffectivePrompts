

from langchain.llms import CTransformers

#Uses https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main API

def chain_of_thoughts__prompting(prompts):
   
    prompt = f"Answer {prompts}."

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',  
            model_type='llama',
            prompts=prompts,
            config={'max_new_tokens': 250,
            'temperature': .5})
    
    response=llm(prompt.format(prompts=prompts))

    return response

    # Define a chain of thought with multiple prompts
prompts = [
        "I gave John 10 chocolates. ",
        "John gave 5 chocolates to his friend, David.",
        "John ate 2 chocolates. How many chocolates John has right now?"
    ]
answer = chain_of_thoughts__prompting(prompts)
print( answer)

