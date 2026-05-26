from flask import Flask, request, render_template_string
from script_writer import generate_script

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Director</title>
</head>
<body style="font-family:Arial; text-align:center;">
    <h1>🎬 AI Director</h1>
    <p>Create viral animated video ideas</p>

    <form method="POST">
        <input type="text" name="idea" placeholder="Enter video idea" size="50" required>
        <br><br>
        <button type="submit">Create Script</button>
    </form>

    {% if script %}
        <hr>
        <h3>Generated Script</h3>
        <pre style="text-align:left; max-width:800px; margin:auto;">{{ script }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    script = None
    if request.method == "POST":
        idea = request.form["idea"]
        script = generate_script(idea)
    return render_template_string(HTML, script=script)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)