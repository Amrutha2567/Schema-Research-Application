import streamlit as st
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import openai
import os

# Load API Key
from dotenv import load_dotenv
load_dotenv(".config")

# Initialize OpenAI API
openai.api_key = os.getenv("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")

# Streamlit UI
st.title("Automated Scheme Research Tool")
st.write("Summarize government schemes and ask questions about them.")

# Input URL(s)
urls = st.text_area("Enter scheme article URL(s) (one per line):")
if st.button("Process URLs"):
    if urls.strip():
        url_list = urls.strip().split("\n")
        st.write("Processing URLs...")
        # Fetch content using LangChain's UnstructuredURLLoader
        try:
            loader = UnstructuredURLLoader(urls=url_list)
            documents = loader.load()
            st.success(f"Loaded {len(documents)} documents successfully!")
            # Further processing...
        except Exception as e:
            st.error(f"Error processing URLs: {e}")
    else:
        st.warning("Please enter at least one URL.")

# Add query functionality and display
query = st.text_input("Enter your query:")
if st.button("Ask Question"):
    if query.strip():
        # FAISS-based retrieval logic here
        st.write("Fetching answer...")
        # Display answer and source URL
    else:
        st.warning("Please enter a query.")
