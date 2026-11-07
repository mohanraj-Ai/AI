import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def decision_agent(state):

    prompt = f"""
You are an insurance claim officer.

Vision Output:
{state["vision_output"]}

Repair Cost:
{state["cost_estimation"]}

Policy Information:
{state["policy_answer"]}

Return ONLY valid JSON.

{{
    "claim_status":"",
    "approved_amount":"",
    "reason":""
}}

Do not return markdown.
Do not return ```json.
Do not explain anything.
Return ONLY the JSON object.
"""

    response = model.generate_content(prompt)

    print("\n===== GEMINI RESPONSE =====\n")
    print(response.text)
    print("\n===========================\n")

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    state["final_decision"] = json.loads(text)

    return state