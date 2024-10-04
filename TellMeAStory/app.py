import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from utils import *


#Uses https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main


# Creating Session State Variable
if 'HuggingFace_API_Key' not in st.session_state:
    st.session_state['HuggingFace_API_Key'] =''

    
st.title("Tell me a story")

# Sidebar to capture the API keys
st.sidebar.title("Provide your Key")
st.session_state['HuggingFace_API_Key']= st.sidebar.text_input("What's your HuggingFace API key?",type="password")

#Creating columns for the UI - To receive inputs from user
col1, col2, col3 = st.columns([10, 10, 5])
with col1:
     story_style = st.selectbox('Story Style',
                                    ('Suspense', 'Thrillers', 'Adventure', 'Fantasy', 'Historical', 'Fiction', 'Horror', 'Mystery'),
                                       index=0)
with col2:
     age_group = st.selectbox('Age Group',
                                    ('Kids', 'Teenagers', 'Adult'),
                                       index=0)

submit = st.button("Generate")

#When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getResponse(story_style,age_group))

