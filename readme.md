# 🧠 Local RAG Assistant: Privacy-First Document Intelligence

A Retrieval-Augmented Generation (RAG) application that allows you to chat with your local documents (PDFs, Markdown) with **100% data privacy**. This project uses Ollama to run Large Language Models (LLMs) locally, ensuring no data ever leaves your machine.

---

## 🚀 Key Features

* **Local Inference**: Utilizes Llama 3 via Ollama for zero-cost, private processing.
* **Semantic Search**: Uses ChromaDB and Nomic-Embed-Text for high-accuracy context retrieval.
* **Anti-Hallucination**: Strictly grounds AI responses in provided document context with source citations.
* **Custom Pipeline**: Built with LangChain to handle document loading, recursive chunking, and vector storage.

---

## 🛠️ Tech Stack

* **Orchestration**: LangChain
* **LLM**: Llama 3 (via Ollama)
* **Embeddings**: Nomic-Embed-Text
* **Vector Database**: ChromaDB
* **Language**: Python 3.11+

---

## 📂 Project Structure

```bash
local-rag-app/
├── data/                      # Put your PDF/Markdown files here
├── chroma/                    # Vector database (auto-generated)
├── get_embedding_function.py  # Embedding logic
├── populate_database.py       # Document ingestion script
├── query_data.py              # Main application loop
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 📦 Installation & Setup

### 1️⃣ Install Ollama

Download from: [https://ollama.com](https://ollama.com)

Pull required models:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

### 2️⃣ Clone the Repository & Setup Environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate the environment

# On Windows:
.\\.venv\\Scripts\\activate

# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### 3️⃣ Ingest Data

Place your PDFs in the `data/` folder and run:

```bash
python populate_database.py
```

---

### 4️⃣ Run the Application

Start the interactive query session:

```bash
python query_data.py
```

---

## 🧠 How it Works

### 🔹 Ingestion

Documents are loaded from the `data/` directory and split into **800-character chunks** with an **80-character overlap** to preserve semantic context at boundaries.

### 🔹 Embedding

Chunks are converted into mathematical vectors using the `nomic-embed-text` model.

### 🔹 Retrieval

When you ask a question:

* The query is converted into a vector
* The system finds the most relevant chunks in ChromaDB

### 🔹 Generation

* Retrieved chunks are provided as **context** to the Llama 3 model
* The model generates a response based only on that context
* Includes **source citations** to prevent hallucination

---