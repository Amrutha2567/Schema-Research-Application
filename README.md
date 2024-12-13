Scheme Research Application

1. Set Up Your Environment
Ensure you have Python and the required libraries installed.

Install Python (if not installed):
Download and install Python from python.org.
Make sure to check "Add Python to PATH" during installation.
Install Required Libraries:
Run the following command in your terminal or command prompt:

bash
Copy code
pip install streamlit langchain openai faiss-cpu beautifulsoup4 requests python-dotenv
2. Prepare Your Files
Ensure the following files are in the same directory:

main.py (your Streamlit app script).
faiss.py (optional FAISS-related logic).
.env (containing your OpenAI API key).
3. Run the Streamlit App
In the terminal, navigate to the directory containing your main.py file and run:

bash
Copy code
streamlit run main.py
4. Open in Browser
After running the above command, Streamlit will provide a local URL like this:

plaintext
Copy code
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
