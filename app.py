from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    name = request.form.get("name")

    if name:
        return f"""
        <h1>Hello {name}!</h1>
        """

    return """
    <h1>What's your name?</h1>

    <form method="POST">
        <input type="text" name="name" placeholder="Your name">
        <button type="submit">Send</button>
    </form>
    """


if __name__ == "__main__":
    app.run(debug=True)
