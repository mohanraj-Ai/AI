import streamlit as st
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")
# Load knowledge file
with open("siva_motors_knowledge_file.json", "r", encoding="utf-8") as f:
    knowledge = json.load(f)

# Flatten knowledge for RAG
knowledge_texts = []
for item in knowledge:
    # Each item has keys: category, question, answer
    knowledge_texts.append(str(item.get("question", "")))
    knowledge_texts.append(str(item.get("answer", "")))

# Build TF-IDF vectorizer
vectorizer = TfidfVectorizer().fit(knowledge_texts)
knowledge_vectors = vectorizer.transform(knowledge_texts)

# RAG retrieval function
def retrieve_context(query, top_k=3):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, knowledge_vectors).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]
    context = "\n".join([knowledge_texts[i] for i in top_indices])
    return context

# Chatbot response function
def chatbot_response(user_input):
    # Quick keyword-based responses
    if "price" in user_input.lower():
        return "Basic service: ₹3,500. Full service: ₹7,000."
    if "service" in user_input.lower():
        return "We provide full car maintenance: engine, oil change, tire check, AC servicing, and more."

    # Retrieve RAG context
    context = retrieve_context(user_input)
    prompt = f"""
Customer Query: {user_input}

Use the following context to answer professionally and concisely:

{context}
"""

    # Start a Gemini chat session
    chat = model.start_chat(
        history=[{"role": "user", "parts": ["You are a helpful assistant for Siva Motors."]}]
    )
    response = chat.send_message(prompt)
    return response.text

# -------------------- Streamlit UI --------------------
st.title("Siva Motors Chatbot (RAG + Gemini AI)")

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

# Send button
if st.button("Send") and user_input.strip():
    reply = chatbot_response(user_input)
    st.session_state.history.append({"user": user_input, "bot": reply})
    user_input = ""  # Clear input

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")