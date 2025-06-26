
# Jupiter Help Centre FAQ Bot 🤖

This project scrapes FAQs from Jupiter's Help Centre and turns them into a friendly bot using semantic search + LLM.

## Features
- Scraping & preprocessing of FAQs
- Semantic search with FAISS + embeddings
- GPT-powered conversational responses
- Streamlit-based UI
- Jupyter notebook demo
- Multilingual + related suggestions (in progress)

## Setup
1. Clone repo
2. Set `OPENAI_API_KEY` in `config.py`
3. Run `pip install -r requirements.txt`
4. Run UI: `streamlit run ui/app.py`

## Example
Ask: *"How do I block my card?"* → Answered instantly by the bot!
