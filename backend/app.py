from flask import Flask, request, jsonify, render_template
from backend.faq_bot_llm import answer_query

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question' field"}), 400
    question = data["question"]
    response = answer_query(question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
