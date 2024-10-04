import streamlit as st
from dotenv import load_dotenv
from utils import query_agent

load_dotenv()

st.title("Summarize data")
st.header("Please upload your text file :")

# Get the text file name
file = st.file_uploader("Upload Text file",type="txt")

question = st.text_area("Enter the question to fetch details from the document")

button = st.button("Summarize and provide result")

if button:
    if file:
        
        if file.type=='text/plain':
            from io import StringIO
            stringio=StringIO(file.getvalue().decode('utf-8'))
            input_data=stringio.read()

            # Get Response
            answer =  query_agent(input_data,question)
            st.write(answer)