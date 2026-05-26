from flask import Flask, request, render_template_string
from script_writer import generate_script
import traceback

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Director</title>
</head>
<body style="font-family:Arial; text-align:center; padding: 20px;">
    <h1>🎬 AI Director</h1>
    <p>Create viral animated video ideas</p>

    <form method="POST">
        <input type="text" name="idea" placeholder="Enter video idea" size="50" required>
        <br><br>
        <button type="submit">Create Script</button>
    </form>

    {% if error %}
        <hr style="border-color: red;">
        <h3 style="color: red;">⚠️ Application Error</h3>
        <pre style="text-align:left; max-width:800px; margin:auto; background: #fee; padding: 15px; border-radius: 5px; overflow-x: auto;">{{ error }}</pre>
    {% endif %}

    {% if script %}
        <hr>
        <h3>Generated Script</h3>
        <pre style="text-align:left; max-width:800px; margin:auto; background: #f9f9f9; padding: 15px; border-radius: 5px; white-space: pre-wrap;">{{ script }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    script = None
    error = None
    if request.method == "POST":
        try:
            idea = request.form["idea"]
            script = generate_script(idea)
        except Exception as e:
            # Captures the exact reason it failed
            error = traceback.format_exc()
            
    return render_template_string(HTML, script=script, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
