from backend.embed_search import build_faiss_index, get_embeddings, search_index


# Dummy LLM-like response generator
def generate_answer(user_question, matched_faq):
    return f"🤖 Here's something that might help:\n\n**Q:** {matched_faq['question']}\n**A:** {matched_faq['answer']}"

def answer_query(user_query):
    index, faq_data = build_faiss_index()
    query_vector = get_embeddings([user_query])
    top_idx = search_index(index, query_vector)
    return generate_answer(user_query, faq_data[top_idx])

if __name__ == "__main__":
    user_query = input("Ask your question: ")
    print(answer_query(user_query))
