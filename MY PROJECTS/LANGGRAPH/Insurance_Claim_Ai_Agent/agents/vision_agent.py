import os
import json
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(ENV_PATH)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def vision_agent(state):

    image = Image.open(state["image_path"])

    prompt = """
You are an automobile insurance damage assessor.

Analyze the accident image.

Return ONLY JSON.

{
    "damaged_parts": [],
    "severity": "",
    "damage_summary": ""
}

Do not return markdown.
Do not return ```json.
Do not explain anything.
Return ONLY the JSON object.
"""

    response = model.generate_content([prompt, image])

    print(response.text)

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    state["vision_output"] = json.loads(text)

    return state