from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Perform mathematical calculations.

    Example:
    calculator("10 * 250")
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"