

from langchain.llms import OpenAI
from pypdf import PdfReader
from langchain.llms.openai import OpenAI
import pandas as pd
import re
from langchain.prompts import PromptTemplate

#Extract the detailes from the PDF files
def get_pdf_from_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


#Extract data from pdf
def extract_data_from_pdf(pages_data):

    template = """Extract the values :Patient name, Medical Conditions, Medications, Procedures, 
        Dates , Diagnosis , Fees from the data: {pages}

        Expected output: {{'Patient name': 'XXXX','Medical Conditions': 'XXXX','Medications': 'XXXX','Procedures': 'XXXX','Dates': 'XXXX','Diagnosis': 'XXXX', 'Fees':'$99.99'}}
        """
    prompt_template = PromptTemplate(input_variables=["pages"], template=template)

    llm = OpenAI(temperature=.7)
    full_response=llm(prompt_template.format(pages=pages_data))

    return full_response


# iterate over the pdf files uploaded
def create_docs(user_pdf_list):
    
    # define the structure for extracting data
    df = pd.DataFrame({'Patient name': pd.Series(dtype='str'),
                   'Medical Conditions': pd.Series(dtype='str'),
                   'Medications': pd.Series(dtype='str'),
                   'Procedures': pd.Series(dtype='str'),
                    'Dates': pd.Series(dtype='str'),
                   'Diagnosis': pd.Series(dtype='int'),
                   'Fees': pd.Series(dtype='int'),
                    })

    for filename in user_pdf_list:
        
        print(filename)
        raw_data=get_pdf_from_text(filename)

        llm_pdf_text=extract_data_from_pdf(raw_data)

        pattern = r'{(.+)}'
        match = re.search(pattern, llm_pdf_text, re.DOTALL)

        if match:
            extracted_values = match.group(1)

            # Convert the extracted text to a dictionary
            data_dict = eval('{' + extracted_values + '}')
            print(data_dict)
        else:
            print("No records found with matching criteria.")

        df=df._append([data_dict], ignore_index=True)
     
    df.head()
    return df



