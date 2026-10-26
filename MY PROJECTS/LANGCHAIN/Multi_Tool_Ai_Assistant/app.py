from flask import Flask, request, jsonify, render_template

from agent.graph import agent


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        question = data.get("message", "").strip()

        if not question:
            return jsonify({
                "response": "Please enter a message."
            })

        # Send user question to LangGraph agent
        response = agent.invoke(
            {
                "messages": [
                    ("user", question)
                ]
            }
        )

        # Get final AI response
        final_content = response["messages"][-1].content

        # Handle Gemini list-based response
        if isinstance(final_content, list):

            text_parts = []

            for item in final_content:

                if isinstance(item, dict):
                    if item.get("type") == "text":
                        text_parts.append(
                            item.get("text", "")
                        )

                elif isinstance(item, str):
                    text_parts.append(item)

            final_content = "\n".join(text_parts)

        return jsonify({
            "response": final_content
        })

    except Exception as e:

        return jsonify({
            "response": f"Error: {str(e)}"
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )