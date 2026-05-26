from flask import Flask, request, render_template_string
from script_writer import generate_script
import traceback

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Director</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        pre {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card p-4">
                <h2 class="text-center mb-3">🎬 AI Director</h2>
                <p class="text-center text-muted">
                    Generate viral animated video scripts using AI
                </p>

                <form method="POST">
                    <input class="form-control mb-3" 
                           type="text" 
                           name="idea" 
                           placeholder="Enter your video idea..." 
                           required>

                    <div class="d-grid">
                        <button class="btn btn-primary btn-lg">
                            Create Script
                        </button>
                    </div>
                </form>

                {% if error %}
                    <div class="mt-4 p-3 rounded bg-danger bg-opacity-10 border border-danger text-danger text-center">
                        <strong>Notice:</strong> OpenAI account quota exceeded. Add credits to activate generation.
                    </div>
                {% endif %}

                {% if script %}
                <hr>
                <h5 class="mt-3">Generated Script</h5>
                <pre>{{ script }}</pre>
                {% endif %}
            </div>
        </div>
    </div>
</div>
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
            error = traceback.format_exc()
            
    return render_template_string(HTML, script=script, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
