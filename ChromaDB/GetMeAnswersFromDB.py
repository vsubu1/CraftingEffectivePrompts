from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings


# Load the input file
inputFile = TextLoader('Sample.txt')
documents = inputFile.load()


CHROMA_DATA_PATH = "chroma_data/"
EMBED_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "demo_docs"

client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

# Split the text into multiple chunks of size 10 with overalpping of 0 characters
text_splitter = CharacterTextSplitter (chunk_size=10,chunk_overlap=0)
chunks= text_splitter.split_documents(documents)

print("Printing Chunks")
print("---------------")
print(chunks)
print("")
print("")


# Tect embeddings encode documents into vectors.
# all-MiniLM-L6-v2 mode is one of the smallest pre-trained model fior similarity search
#Load the SentenceTransformerEmbeddings embeddings class using the pre-trained model
model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(chunks, model)
print(db._collection.get(include=['embeddings']))


retriever = db.as_retriever(search_kwargs={"k": 3})


print("printing retriever")
print("-------------------")
print(retriever)
print("")
print("")
docs = retriever.get_relevant_documents("What animals are present?")
print("Printing Results now for list of animals")
print("========================================")
print(docs)
print("")
print("")
docs = retriever.get_relevant_documents("What flowers are present?")
print("Printing Results now for list of flowers")
print("========================================")
print(docs)
