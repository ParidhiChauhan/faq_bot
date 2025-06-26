
import json
import re
from html import unescape

CATEGORIES = {
    "kyc": ["kyc", "verification", "aadhaar", "pan"],
    "payments": ["payment", "upi", "transaction", "transfer"],
    "rewards": ["reward", "cashback", "points"],
    "limits": ["limit", "spend", "withdrawal"],
    "cards": ["card", "debit", "block", "virtual"],
}

def load_faq():
    with open("data/faq_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def clean_text(text):
    text = unescape(text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def categorize(question, answer):
    q_lower = question.lower()
    for cat, keywords in CATEGORIES.items():
        if any(k in q_lower for k in keywords):
            return cat
    return "general"

def preprocess():
    faqs = load_faq()
    processed = []

    seen = set()
    for item in faqs:
        q, a = clean_text(item["question"]), clean_text(item["answer"])
        if q not in seen:
            seen.add(q)
            processed.append({
                "question": q,
                "answer": a,
                "category": categorize(q, a)
            })

    with open("data/faq_clean.json", "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    preprocess()
