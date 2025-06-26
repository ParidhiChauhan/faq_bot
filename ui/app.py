
import streamlit as st
from backend.faq_bot_llm import answer_query

st.set_page_config(page_title="Jupiter FAQ Bot", layout="centered")
st.title("🤖 Jupiter Help Centre Assistant")
query = st.text_input("Ask me anything related to Jupiter:")
if query:
    with st.spinner("Thinking..."):
        answer = answer_query(query)
    st.markdown(f"**Answer:** {answer}")
