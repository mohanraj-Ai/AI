import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

from tools.calculator import calculator
from tools.wikipedia import wikipedia_search
from tools.web_search import web_search
from tools.weather import weather
from tools.sql import sql_query
from tools.youtube import youtube_search
from tools.gmail import gmail_search


# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing from .env")


# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=api_key,
    max_retries=3,
)


# Available tools
tools = [
    calculator,
    wikipedia_search,
    web_search,
    weather,
    sql_query,
    youtube_search,
    gmail_search,
]


# Create LangGraph ReAct Agent
agent = create_react_agent(
    model=llm,
    tools=tools,
    prompt=(
        "You are a helpful multi-tool AI assistant. "
        "Use the available tools whenever they are relevant. "
        "When the user asks about their emails, Gmail, inbox, "
        "recent emails, interview emails, or messages, ALWAYS use "
        "the gmail_search tool instead of saying you cannot access "
        "personal information. "
        "For recent emails, use the Gmail query 'newer_than:7d'. "
        "For interview emails, search Gmail using an appropriate "
        "query such as 'interview'. "
        "Return the information obtained from the tool clearly."
    ),
)