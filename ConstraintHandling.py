import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

  
#Function to get the response back
def getLLMResponse(constraint, question):

    llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',     #https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.07})
    

    
    #Template for building the PROMPT
    template = """
    Given the following constraint:\n{constraint}\n\nExplain the concept of {question}.
    """

    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["constraint","question"],
    template=template)

     #Generating the response using LLM
    response=llm(prompt.format(constraint=constraint,question=question))
    print(response)

    return response

st.set_page_config(page_title="Generate Answer for the question based on the context", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>Generate Answer for the question based on the context </h1>", unsafe_allow_html=True)

#Creating columns for the UI - To receive inputs from user
context = st.text_area('Enter your context', height=10)
question = st.text_area('Provide an anbiguous question', height=20)

submit = st.button("Generate")

#When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(context,question))
