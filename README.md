Scheme Research Application

1. Set Up Your Environment
Ensure you have Python and the required libraries installed.


```bash
pip install streamlit langchain openai faiss-cpu beautifulsoup4 requests python-dotenv
```

2. Prepare Your Files
Ensure the following files are in the same directory:

main.py (your Streamlit app script).

faiss.py (optional FAISS-related logic).


.env (containing your OpenAI API key).
```
OPENAI_API_KEY=your-api-key-here

```


3. Run the Streamlit App
In the terminal, navigate to the directory containing your main.py file and run:


bash
then run 
```
streamlit run main.py
```

4. Open in Browser
After running the above command, Streamlit will provide a local URL like this:

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
