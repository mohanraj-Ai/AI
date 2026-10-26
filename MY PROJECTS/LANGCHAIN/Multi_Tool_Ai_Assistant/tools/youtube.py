from langchain_core.tools import tool
import requests
import os


@tool
def youtube_search(query: str) -> str:
    """
    Search YouTube for videos related to a query.
    """

    try:
        api_key = os.getenv("YOUTUBE_API_KEY")

        if not api_key:
            return "YOUTUBE_API_KEY is missing from .env"

        url = "https://www.googleapis.com/youtube/v3/search"

        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": 5,
            "key": api_key
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        items = data.get("items", [])

        if not items:
            return f"No YouTube videos found for: {query}"

        results = []

        for item in items:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            channel = item["snippet"]["channelTitle"]
            description = item["snippet"]["description"]

            results.append(
                f"Title: {title}\n"
                f"Channel: {channel}\n"
                f"Description: {description}\n"
                f"URL: https://www.youtube.com/watch?v={video_id}"
            )

        return "\n\n".join(results)

    except Exception as e:
        return f"YouTube search error: {str(e)}"