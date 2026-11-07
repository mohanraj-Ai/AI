import os
from dotenv import load_dotenv

import google.generativeai as genai

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import JinaEmbeddings

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================
# Load Embedding Model
# ==========================

embeddings = JinaEmbeddings(
    jina_api_key=JINA_API_KEY,
    model_name="jina-embeddings-v3"
)

# ==========================
# Load FAISS Database
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = os.path.join(BASE_DIR, "rag_db")

vector_db = FAISS.load_local(
    DB_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

# ==========================
# Retrieval Function
# ==========================

def retrieve(query):
    docs = vector_db.similarity_search(query, k=3)
    return docs

# ==========================
# Policy Agent
# ==========================

def policy_agent(state):

    damaged_parts = state["vision_output"]["damaged_parts"]

    question = f"""
Does the insurance policy cover repairing or replacing these damaged parts?

Damaged Parts:
{damaged_parts}

Explain whether they are covered or not according to the policy.
"""

    docs = retrieve(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an insurance claim expert.

Use ONLY the policy information below.

Policy Context:
{context}

Question:
{question}

Answer clearly with:
1. Covered Parts
2. Not Covered Parts
3. Reason
"""

    response = model.generate_content(prompt)

    state["policy_answer"] = response.text

    return state