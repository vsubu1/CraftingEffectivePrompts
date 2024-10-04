
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

def query_agent(document, question):

    # Split text into chunks
    splitter = CharacterTextSplitter (chunk_size=200,chunk_overlap=0)

    texts= splitter.split_documents(document)

    embeddings=OpenAIEmbeddings()

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(texts, embeddings)
    db._collection.get(include=['embeddings'])

    retriever = db.as_retriever(search_kwargs={"k": 2})

    result = retriever.get_relevant_documents(question)
    return(result)