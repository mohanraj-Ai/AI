from langchain_core.tools import tool
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import os
import pickle


# Permission to read Gmail
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials.json")
TOKEN_FILE = os.path.join(BASE_DIR, "token.json")


def get_gmail_service():
    creds = None

    # Load previously saved login token
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)

    # If token is missing or expired, authenticate
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        # Save token for future use
        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    return build(
        "gmail",
        "v1",
        credentials=creds
    )


@tool
def gmail_search(query: str) -> str:
    """
    Search Gmail messages using Gmail search syntax.

    Examples:
    gmail_search("newer_than:7d")
    gmail_search("from:example@gmail.com")
    gmail_search("subject:interview")
    """

    try:
        service = get_gmail_service()

        results = service.users().messages().list(
            userId="me",
            q=query,
            maxResults=5
        ).execute()

        messages = results.get("messages", [])

        if not messages:
            return f"No Gmail messages found for: {query}"

        output = []

        for message in messages:

            msg = service.users().messages().get(
                userId="me",
                id=message["id"],
                format="metadata",
                metadataHeaders=[
                    "From",
                    "Subject",
                    "Date"
                ]
            ).execute()

            headers = msg.get("payload", {}).get("headers", [])

            sender = ""
            subject = ""
            date = ""

            for header in headers:

                name = header["name"]
                value = header["value"]

                if name == "From":
                    sender = value

                elif name == "Subject":
                    subject = value

                elif name == "Date":
                    date = value

            output.append(
                f"From: {sender}\n"
                f"Subject: {subject}\n"
                f"Date: {date}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Gmail error: {str(e)}"