import os
import uuid
import json
from flask import Flask, request, jsonify
import google.generativeai as genai
import functions

# Configure Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# Load knowledge file
with open("siva_motors_knowledge_file.txt", "r") as f:
    SYSTEM_PROMPT = f.read()

app = Flask(__name__)

# Store chat sessions
chat_sessions = {}


# Start chat
@app.route("/start", methods=["GET"])
def start():
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": ["You are a helpful assistant for Siva Motors."]},
            {"role": "model", "parts": [SYSTEM_PROMPT]},
        ]
    )

    chat_id = str(uuid.uuid4())
    chat_sessions[chat_id] = chat

    # Prevent memory overflow
    if len(chat_sessions) > 100:
        chat_sessions.pop(next(iter(chat_sessions)))

    return jsonify({"chat_id": chat_id})


# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    chat_id = data.get("chat_id")
    user_input = data.get("message")

    # Validate input
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    if chat_id not in chat_sessions:
        return jsonify({"error": "Invalid chat_id"}), 400

    chat = chat_sessions[chat_id]

    # Optional: Smart routing (faster responses)
    if "price" in user_input.lower():
        return jsonify({"response": functions.get_price_details()})

    if "service" in user_input.lower():
        return jsonify({"response": functions.get_service_details()})

    # Enhance prompt
    enhanced_input = f"""
Customer Query: {user_input}

Answer professionally based on Siva Motors knowledge.
Keep it short and helpful.
"""

    # Get Gemini response
    try:
        response = chat.send_message(enhanced_input)
        reply = response.text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Save transcript
    transcript = {"user_input": user_input, "response": reply, "chat_id": chat_id}

    try:
        functions.addTranscriptToGoogleSheet(transcript)
    except Exception:
        pass

    # Lead extraction
    messages = [
        {
            "role": "system",
            "content": """
Extract customer details strictly.

Rules:
- Only extract if BOTH name and phone number are present
- Return JSON: {"name": "...", "phone": "..."}
- If not present, return exactly: N
""",
        },
        {"role": "user", "content": user_input},
    ]

    try:
        lead = functions.get_completion_from_messages(messages)

        if lead.strip().startswith("{"):
            dict_lead = json.loads(lead)

            if "name" in dict_lead and "phone" in dict_lead:
                functions.addLeadToGoogleSheet(dict_lead)

    except Exception:
        pass

    return jsonify({"response": reply})


if __name__ == "__main__":
    app.run(port=8080, debug=True)
