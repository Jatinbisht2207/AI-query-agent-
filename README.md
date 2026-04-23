# AutoStream AI Assistant 

An AI-powered conversational assistant that:
- Answers product queries using RAG (Retrieval-Augmented Generation)
- Detects user intent
- Captures leads via conversational flow
- Provides a clean chat UI using Streamlit

## Features
- Intent Detection (Greeting, Product, High Intent)
- RAG using FAISS + HuggingFace Embeddings
- Lead Capture Flow (Name → Email → Platform)
- Clean Chat UI (Streamlit)

## Tech Stack
- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Streamlit

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py