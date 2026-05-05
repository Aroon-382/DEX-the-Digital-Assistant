from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

client = Groq(api_key="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")

conversation_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.json
    user_message = data.get("message")
    subject = data.get("subject", "General")

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    system_prompt = f"You are DEX the Discovery Bot, a friendly academic assistant. You specialize in {subject}. Keep answers clear, educational and fun!"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": system_prompt}] + conversation_history,
        max_tokens=1000
    )

    reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    return jsonify({"reply": reply})

@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True)