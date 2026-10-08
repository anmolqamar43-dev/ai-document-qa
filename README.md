# AI-Powered Document Question Answering System

An AI-powered document question answering system built using **Python, FastAPI, Sentence Transformers, ChromaDB, Groq LLM, and Retrieval-Augmented Generation (RAG)**.

The system allows users to upload documents and ask questions about their content. It uses semantic search to retrieve the most relevant document chunks and then uses an LLM to generate a grounded answer based on the retrieved information.

---

## 📌 Project Overview

Traditional keyword-based search looks for exact words in documents. This project uses **semantic search**, which understands the meaning of text using vector embeddings.

The system follows this pipeline:

```text
Document
    ↓
Document Loader
    ↓
Text Chunking
    ↓
Sentence Transformer Embeddings
    ↓
ChromaDB Vector Database
    ↓
Semantic Search
    ↓
Top 3 Relevant Chunks
    ↓
RAG Prompt
    ↓
Groq LLM
    ↓
Answer + Sources
```

---

## 🎯 Objectives

The main objectives of this project are:

- Implement different prompt engineering techniques
- Compare zero-shot, few-shot, and role-based prompting
- Generate text embeddings
- Implement semantic search
- Store embeddings in a vector database
- Retrieve the top 3 relevant document chunks
- Implement Retrieval-Augmented Generation (RAG)
- Generate answers using an LLM
- Build a FastAPI backend
- Provide a simple web interface
- Display answers, sources, and retrieval distances

---

## ✨ Features

- 📄 Upload PDF, TXT, and Markdown documents
- ✂️ Automatic document chunking
- 🔢 Sentence Transformer embeddings
- 🗄️ ChromaDB vector storage
- 🔍 Semantic similarity search
- 📚 Top-3 relevant chunk retrieval
- 🧠 Retrieval-Augmented Generation
- 🤖 Groq LLM integration
- 💬 Interactive question answering
- 📖 Source and chunk information
- 📊 Retrieval distance display
- 🌐 FastAPI web interface
- 🛡️ Grounded responses using retrieved context

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API and web application |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| Groq | Large Language Model |
| pypdf | PDF text extraction |
| HTML | Web interface |
| CSS | Web interface styling |
| JavaScript | Frontend interaction |

---

## 📁 Project Structure

```text
ai-document-qa/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── document_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompts.py
│   ├── llm.py
│   └── rag.py
│
├── data/
│   ├── artificial_intelligence.txt
│   ├── machine_learning.txt
│   ├── embeddings.txt
│   ├── semantic_search.txt
│   └── rag.txt
│
├── static/
│   ├── index.html
│   ├── style
