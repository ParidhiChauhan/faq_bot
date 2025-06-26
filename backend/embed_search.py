
import json
import faiss
import numpy as np
import openai

from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def load_faq():
    with open("data/faq_clean.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_embeddings(texts):
    response = openai.Embedding.create(
        input=texts,
        model="text-embedding-ada-002"
    )
    return [d["embedding"] for d in response["data"]]

def build_faiss_index():
    faq_data = load_faq()
    questions = [item["question"] for item in faq_data]
    embeddings = get_embeddings(questions)
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index, faq_data

def search_index(index, query_embedding, k=3):
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    return I[0]

if __name__ == "__main__":
    idx, _ = build_faiss_index()
    print("FAISS index built and ready.")
