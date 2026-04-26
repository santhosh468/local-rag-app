import os
import shutil
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from get_embedding_function import get_embedding_function

DATA_PATH = "data"
CHROMA_PATH = "chroma"

def main():
    # 1. Load Documents
    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()

    # 2. Split Text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)

    # 3. Save to ChromaDB
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    
    db = Chroma.from_documents(
        chunks, get_embedding_function(), persist_directory=CHROMA_PATH
    )
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

if __name__ == "__main__":
    main()