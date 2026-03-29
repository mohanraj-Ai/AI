import json
import os
import google.generativeai as genai
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configure Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# 🔐 Google Sheets Setup (INIT ONCE)
scope = ["https://www.googleapis.com/auth/spreadsheets"]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "servicechatbot-490716-0b1c7269af34.json", scope
)

client = gspread.authorize(creds)

# Sheet IDs
LEAD_SHEET_ID = "1NnceFfm7XOB5wT_OzGQ8nJFmq0VB41IxWtQZOzi4u4A"
TRANSCRIPT_SHEET_ID = "1_MLgiRbPD08RaS3iBrhc6sKqFviMTjNLO1MxHauNJiY"


# 🔥 LEAD EXTRACTION USING GEMINI
def extract_lead(user_input):
    prompt = f"""
Extract customer details strictly.

Rules:
- Only extract if BOTH name and phone number are present
- Return JSON ONLY in format: {{"name": "...", "phone": "..."}}
- If not present, return exactly: N

Text: {user_input}
"""

    try:
        response = model.generate_content(prompt)
        result = response.text.strip()

        if result.startswith("{"):
            data = json.loads(result)

            if "name" in data and "phone" in data:
                return data

        return "N"

    except Exception:
        return "N"


# 🔥 ADD LEAD TO GOOGLE SHEET
def addLeadToGoogleSheet(dictionary):
    try:
        spreadsheet = client.open_by_key(LEAD_SHEET_ID)
        worksheet = spreadsheet.get_worksheet(0)

        values = [dictionary.get("name", ""), dictionary.get("phone", "")]

        worksheet.append_row(values)
        return "added"

    except Exception as e:
        print("Lead Error:", e)
        return "error"


# 🔥 ADD TRANSCRIPT TO GOOGLE SHEET
def addTranscriptToGoogleSheet(dictionary):
    try:
        spreadsheet = client.open_by_key(TRANSCRIPT_SHEET_ID)
        worksheet = spreadsheet.get_worksheet(0)

        values = [
            dictionary.get("chat_id", ""),
            dictionary.get("user_input", ""),
            dictionary.get("response", ""),
        ]

        worksheet.append_row(values)
        return "added"

    except Exception as e:
        print("Transcript Error:", e)
        return "error"
