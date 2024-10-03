import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

#Function to get the response back
def getLLMResponse(sentence,language):

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',    
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
    
    
    #Template for developing the PROMPT
    template = """
    Translate this sentense {sentence} from english to {language}.
    \n\nSentence in English:
    
    """

    #Creating the PROMPT
    prompt = PromptTemplate(
    input_variables=["sentence","language"],
    template=template)

    #Generate the response using LLM
    response=llm(prompt.format(sentence=sentence,language=language))
    print(response)

    return response

st.set_page_config(page_title="Translation from English to another language",
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Translate now ")

form_input = st.text_area('Enter the sentence in English', height=50)

#Creating columns for the UI - To receive inputs from user
col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    target_language = st.selectbox('Target Language',
                                    ('French', 'German', 'Japanese', 'Spanish',"Hindi"),
                                       index=0)


submit = st.button("Translate")

#When 'Generate' is clicked , translate the sentence
if submit:
    st.write(getLLMResponse(form_input,target_language))
