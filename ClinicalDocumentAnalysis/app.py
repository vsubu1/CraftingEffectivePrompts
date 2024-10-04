import streamlit as st
from dotenv import load_dotenv
from utils import *
from  utils import create_docs

def main():
    load_dotenv()
    st.set_page_config(page_title="Clinical Document Extraction")
    st.title("Extract Clinical Documents")
    st.subheader("Extracting clinical documents")

    # Upload your clinical records in pdf format
    pdf = st.file_uploader("Upload the clinical documents here in PDF format", type=["pdf"],accept_multiple_files=True)

    submit=st.button("Extract Data")

    if submit:
        with st.spinner('Wait for it...'):
            df=create_docs(pdf)
            st.write(df.head())

            data_as_csv= df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download data as CSV", 
                data_as_csv, 
                "benchmark-tools.csv",
                "text/csv",
                key="download-tools-csv",
            )
        st.success("Hope , you got all clinical document details")

#main function is called
if __name__ == '__main__':
    main()


