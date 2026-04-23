import json
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_vector_store():
    with open("data.json", "r") as f:
        data = json.load(f)

    texts = [item["text"].strip() for item in data]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(texts, embeddings)

    return vectorstore


def get_answer(query, vectorstore):
    docs = vectorstore.similarity_search(query, k=3)

    query_lower = query.lower()
    filtered_docs = []

    for doc in docs:
        text = doc.page_content.lower()

        if "pro" in query_lower:
            if "pro" in text:
                filtered_docs.append(doc.page_content)

        elif "basic" in query_lower:
            if "basic" in text:
                filtered_docs.append(doc.page_content)

        elif any(word in query_lower for word in ["price", "pricing", "plan"]):
            filtered_docs.append(doc.page_content)

        elif "policy" in query_lower:
            if "policy" in text:
                filtered_docs.append(doc.page_content)

    # fallback if nothing matched
    if not filtered_docs:
        filtered_docs = [doc.page_content for doc in docs[:2]]

    return "\n\n".join(filtered_docs)


if __name__ == "__main__":
    vs = load_vector_store()
    result = get_answer("pricing", vs)
    print("RAG OUTPUT:\n", result)