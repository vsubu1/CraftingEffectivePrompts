import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

  
#Function to get the response back
def getLLMResponse(text):

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})

    
    #Template for building the PROMPT
    template = """
    Extract only the legal entities and key terms from the  {text}.
    """

    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["text"],
    template=template)

     #Generating the response using LLM
    response=llm(prompt.format(text=text))
    print(response)

    return response

st.set_page_config(page_title="Extract legal entities and key terms", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Document Review</h1>", unsafe_allow_html=True)

#Creating columns for the UI - To receive inputs from user
statement = st.text_area('Enter your Statements', height=10)

submit = st.button("Generate")

#When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(statement))
