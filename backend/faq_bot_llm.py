
import openai
from embed_search import build_faiss_index, get_embeddings, search_index

from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def answer_query(query):
    index, faq_data = build_faiss_index()
    query_embedding = get_embeddings([query])[0]
    top_indices = search_index(index, query_embedding)
    best_faq = faq_data[top_indices[0]]
    
    prompt = f"Q: {query}\n\nRelevant Info: {best_faq['question']} - {best_faq['answer']}\n\nAnswer in friendly tone:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful support assistant for a banking app."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

if __name__ == "__main__":
    user_query = input("Ask your question: ")
    print(answer_query(user_query))
