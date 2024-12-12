from langchain.vectorstores import FAISS

# Assuming `vectorstore` is your FAISS object
faiss_index_path = "faiss_store_openai.pkl"

# Save the FAISS index
# Load the saved FAISS index from the specified local path
loaded_vector_store = FAISS.load_local(faiss_index_path)

print(f"FAISS index saved to {faiss_index_path}")
