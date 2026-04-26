import argparse
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from get_embedding_function import get_embedding_function
from langchain_chroma import Chroma

CHROMA_PATH = "chroma"

# This is the "brain" instructions for the AI
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def main():
    query_text = input("Enter your query (or 'quit' to exit): ")
    
    if query_text.lower() == "quit":
        return

    # 1. Search the Database
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())
    results = db.similarity_search_with_score(query_text, k=5)

    # 2. Prepare the context from the found documents
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    # 3. Fill the Prompt Template
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # 4. Feed the prompt to Ollama (Llama 3)
    print("\n--- Generating Response ---\n")
    model = OllamaLLM(model="llama3")
    response_text = model.invoke(prompt)

    # 5. Get the sources for citation
    sources = [doc.metadata.get("source", None) for doc, _score in results]
    
    # 6. Final Clean Output
    print(f"RESPONSE:\n{response_text}")
    print(f"\nSOURCES: {list(set(sources))}") # list(set()) removes duplicates

if __name__ == "__main__":
    main()