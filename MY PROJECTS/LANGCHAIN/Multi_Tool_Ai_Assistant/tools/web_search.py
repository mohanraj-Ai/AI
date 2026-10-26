from langchain_core.tools import tool
from ddgs import DDGS


@tool
def web_search(query: str) -> str:
    """
    Search the web and return relevant results.
    """

    try:
        results = DDGS().text(
            query,
            max_results=5
        )

        if not results:
            return f"No web results found for: {query}"

        output = []

        for result in results:
            title = result.get("title", "")
            body = result.get("body", "")
            url = result.get("href", "")

            output.append(
                f"Title: {title}\n"
                f"Summary: {body}\n"
                f"URL: {url}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Web search error: {str(e)}"