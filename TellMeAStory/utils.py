
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import streamlit as st

#https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
#Function to get the response back
def getResponse(story_style, age_group):

      #Proceed only if API keys are provided
    if st.session_state['HuggingFace_API_Key'] !="" :
        llm = CTransformers(model="TheBloke/Llama-2-7B-Chat-GGML",   
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
        st.write("Calling model...")
        response=llm(prompt.format(story_style=story_style,age_group=age_group))

        return (response)
    else:
        st.sidebar.error(" Please provide the API keys.....")
