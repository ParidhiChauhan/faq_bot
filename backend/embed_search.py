import json
import numpy as np
import faiss

def load_faq():
    with open("data/faq_clean.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Dummy embedding generator (random vectors)
def get_embeddings(texts):
    np.random.seed(42)
    return np.random.rand(len(texts), 1536).astype("float32")

def build_faiss_index():
    faq_data = load_faq()
    questions = [item["question"] for item in faq_data]
    embeddings = get_embeddings(questions)

    index = faiss.IndexFlatL2(1536)
    index.add(embeddings)

    return index, faq_data

def search_index(index, query_vector, top_k=1):
    distances, indices = index.search(query_vector, top_k)
    return indices[0][0]
