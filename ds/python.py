from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load documents from URL
urls = ["https://example.com/scheme1", "https://example.com/scheme2"]
loader = UnstructuredURLLoader(urls=urls)
documents = loader.load()

# Generate embeddings for the documents using OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Create a FAISS index (vectorstore)
vectorstore = FAISS.from_documents(documents, embeddings)
