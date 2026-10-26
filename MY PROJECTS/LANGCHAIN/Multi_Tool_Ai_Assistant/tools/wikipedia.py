from langchain_core.tools import tool
import requests


@tool
def wikipedia_search(query: str) -> str:
    """
    Search Wikipedia and return a short summary.
    """

    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + requests.utils.quote(query)

        response = requests.get(
            url,
            headers={"User-Agent": "MultiToolAI Assistant/1.0"},
            timeout=10
        )

        if response.status_code != 200:
            return f"Wikipedia search failed. Status code: {response.status_code}"

        data = response.json()

        extract = data.get("extract")

        if not extract:
            return f"No Wikipedia summary found for: {query}"

        return extract

    except Exception as e:
        return f"Wikipedia search error: {str(e)}"