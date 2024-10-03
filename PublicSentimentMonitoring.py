from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Function to generate the response
def getLLMResponse(statement):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.3})
    
    #Template for PROMPT
    template = """
    What is the sentiment of the {statement}.
    \n\nStatement:
    """

    #building the PROMPT
    prompt = PromptTemplate(
    input_variables=["statement"],
    template=template)

    #GGetting the response from LLM
    response=llm(prompt.format(statement=statement))

    return response

# sample texts for  doing sentiment analysis
text_list = [
  "Excited to see the new government initiative on climate change!",
  "Disappointed with the budget allocation for healthcare. #HealthcareForAll",
  "Neutral about the recent policy changes. Waiting to see the impact.",
  "Feeling positive about the economic recovery. #EconomyGrowth",
]
# Process each statement from the text_list
i=1
for  statement in text_list:
     print("\n\n")
     print(f"{i}. Content: {statement}")
     print(f" Sentiment: {getLLMResponse(statement)}")
     i=i+1
 

