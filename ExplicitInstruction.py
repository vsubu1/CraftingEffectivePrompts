import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Uses  https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

#Function to get the response back
def getLLMResponse(question):

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     
                    model_type='llama',
                    config={'max_new_tokens': 200,
                            'temperature': 0.01})
    
    
    #Template for building the PROMPT
    template = """
    Generate text for the {question}.
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

st.set_page_config(page_title="Write your question clearly:",
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Answer me")

form_input = st.text_area('Enter your question', height=50)

#Creating columns for the UI - To receive inputs from user

submit = st.button("Generate answer")

#When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(form_input))

