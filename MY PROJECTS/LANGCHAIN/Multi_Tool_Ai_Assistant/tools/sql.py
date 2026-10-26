from langchain_core.tools import tool
import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / "database" / "company.db"


@tool
def sql_query(query: str) -> str:
    """
    Execute a read-only SQL query on the company database.

    Use SELECT queries to retrieve employee information.
    """

    try:
        query = query.strip()

        # Allow only read-only queries
        if not query.lower().startswith("select"):
            return "Only SELECT queries are allowed."

        connection = sqlite3.connect(DB_PATH)
        cursor = connection.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()

        columns = [description[0] for description in cursor.description]

        connection.close()

        if not rows:
            return "No results found."

        result = [", ".join(columns)]

        for row in rows:
            result.append(", ".join(str(value) for value in row))

        return "\n".join(result)

    except Exception as e:
        return f"SQL query error: {str(e)}"