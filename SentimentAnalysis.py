import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Function to get the response back
def getLLMResponse(question):
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
    
    
    #Template for building the PROMPT
    template = """
    What is the sentiment of the {question}.
    \n\nQuestion:
    
    """

    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["question"],
    template=template)

    #Generating the response using LLM
    response=llm(prompt.format(question=question))
    print(response)

    return response

st.set_page_config(page_title="Sentiment Analysis",
                    page_icon='📧',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Sentiment Analysis")

form_input = st.text_area('Enter your statement', height=50)

#Creating columns for the UI - To receive inputs from user

submit = st.button("Analyze Sentiment")

#When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(form_input))
