import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Uses https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

#Function to get the response back
def getLLMResponse(story_style, age_group):
   
    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',   
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
    
    
    #Template for building the PROMPT
    template = """
    Write a moral story based on the {story_style} for the {age_group} in 50 lines
    \n\nStory Text :

    """
    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["story_style","age_group"],
    template=template,)

    #Generating the response using LLM
    response=llm(prompt.format(story_style=story_style,age_group=age_group))
    print(response)

    return response


st.set_page_config(page_title="Generate Story",
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Generate a moral story")

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
    st.write(getLLMResponse(story_style,age_group))
