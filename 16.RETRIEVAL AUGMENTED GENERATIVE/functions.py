import json

# Quick price response
def get_price_details():
    return "Basic service: ₹3,500. Full service: ₹7,000."

# Quick service response
def get_service_details():
    return "We provide full car maintenance: engine, oil change, tire check, etc."

# Save chat transcript (currently just prints)
def addTranscriptToGoogleSheet(transcript):
    print("Transcript saved:", transcript)
    # Later you can integrate with Google Sheets API if needed
    # Example: use gspread to write transcript dict to a sheet

# Save lead info (currently just prints)
def addLeadToGoogleSheet(lead):
    print("Lead saved:", lead)
    # Later: push lead info to Google Sheet

# Simulate extraction of customer name & phone from messages
def get_completion_from_messages(messages):
    """
    Messages: list of dicts with "role" and "content"
    Rule: only return JSON if BOTH name and phone number are present
    """
    for msg in messages:
        content = msg.get("content", "").lower()
        if "name" in content and "phone" in content:
            # Simulate extracted lead
            return '{"name": "John Doe", "phone": "9999999999"}'
    return "N"