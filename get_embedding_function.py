from langchain_ollama import OllamaEmbeddings

def get_embedding_function():
    """
    Get the embedding function using Ollama with Nomic model.
    Ensure Ollama is running locally before calling this function.
    """
    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        return embeddings
    except Exception as e:
        print(f"Error: Could not connect to Ollama. Make sure Ollama is running locally.")
        print(f"Details: {e}")
        raise