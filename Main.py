from flask import Flask, request, jsonify
from ai_engine import get_answer
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Kabiru AI API is running"

# 🌐 API endpoint
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question", "")
    answer = get_answer(question)

    return jsonify({
        "question": question,
        "answer": answer
    })

# 📲 WhatsApp bot
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get("Body")

    answer = get_answer(msg)

    resp = MessagingResponse()
    resp.message(answer)

    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
