import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from get_embedding_function import get_embedding_function

# Set your API Key (or use an environment variable)
os.environ["GOOGLE_API_KEY"] = "AIzaSyCeuAXHzN_OIxtAWzcY96BlzHxpZnBsNcI"

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}
---
Answer the question based on the above context: {question}
"""

st.set_page_config(page_title="Gemini RAG Assistant", page_icon="🚀")
st.title("🚀 Gemini-Powered RAG Intelligence")

query_text = st.text_input("Ask your documents a question:")

if query_text:
    with st.spinner("Fetching answer from Gemini..."):
        # 1. Search Database (Local)
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())
        results = db.similarity_search_with_score(query_text, k=3)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        
        # 2. Setup Gemini Model
        # Use 'gemini-2.5-flash' for the best balance of speed and intelligence
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", streaming=True)

        # 3. Generate and Stream Response
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)

        st.subheader("Response")
        response_placeholder = st.empty()
        full_response = ""

        # Stream the response word-by-word
        for chunk in model.stream(prompt):
            full_response += chunk.content
            response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)