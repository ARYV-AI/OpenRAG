from flask import Flask, render_template, request
from src.generate import generateResponse

app = Flask(__name__)


def get_ai_response(query: str) -> dict:
    answer =  generateResponse(query)
    return {"answer": answer}


@app.route("/", methods=["GET", "POST"])
def index():
    query  = None
    answer = None
    sources = []
    error  = None

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if not query:
            error = "Please enter a question."
        else:
            try:
                result  = get_ai_response(query)
                answer  = result.get("answer", "")
            except Exception as exc:
                error = f"Something went wrong: {exc}"

    return render_template(
        "index.html",
        query=query,
        answer=answer,
        error=error,
    )

if __name__ == "__main__":
    app.run(debug=False)
