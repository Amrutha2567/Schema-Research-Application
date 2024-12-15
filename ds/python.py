# from langchain.document_loaders import UnstructuredURLLoader
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS

# # Load documents from URL
# urls = ["https://example.com/scheme1", "https://example.com/scheme2"]
# loader = UnstructuredURLLoader(urls=urls)
# documents = loader.load()

# # Generate embeddings for the documents using OpenAIEmbeddings
# embeddings = OpenAIEmbeddings()

# # Create a FAISS index (vectorstore)
# vectorstore = FAISS.from_documents(documents, embeddings)


from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load documents from URLs
urls = ["https://example.com/scheme1", "https://example.com/scheme2"]
try:
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()
except Exception as e:
    print(f"Error loading documents: {e}")
    documents = []

# Split documents into smaller chunks for better embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = text_splitter.split_documents(documents)

# Generate embeddings for the documents using OpenAIEmbeddings
try:
    embeddings = OpenAIEmbeddings()  # Ensure your OpenAI API key is set
except Exception as e:
    print(f"Error initializing OpenAIEmbeddings: {e}")
    embeddings = None

if embeddings:
    # Create a FAISS index (vectorstore)
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    # Save the FAISS index for later use
    vectorstore.save_local("faiss_index")

    print("FAISS index created and saved successfully.")
