# This imports Flask — the web framework
from flask import Flask, render_template, jsonify

# This creates your Flask app
app = Flask(__name__)

# This is your paper data — same as your JS array before
# Soon this will come from a real database
papers = [
    {"subject": "Physics", "college": "St. Joseph's College", "stream": "science", "year": "2024", "board": "PUC"},
    {"subject": "Chemistry", "college": "Christ College", "stream": "science", "year": "2023", "board": "PUC"},
    {"subject": "Mathematics", "college": "St. Joseph's College", "stream": "science", "year": "2024", "board": "PUC"},
    {"subject": "Accountancy", "college": "MES College", "stream": "commerce", "year": "2023", "board": "PUC"},
    {"subject": "Business Studies", "college": "St. Joseph's College", "stream": "commerce", "year": "2024", "board": "PUC"},
    {"subject": "History", "college": "Jyoti Nivas College", "stream": "arts", "year": "2023", "board": "PUC"},
    {"subject": "STEM", "college": "Vedantha PU College", "stream": "engineering", "year": "2024", "board": "PUC"},
]

# This is a ROUTE — when someone visits your homepage, Flask runs this function
@app.route("/")
def home():
    return render_template("index.html")

# This is an API route — when the frontend asks for papers, Flask returns them as JSON
@app.route("/papers")
def get_papers():
    return jsonify(papers)

# This starts the server
if __name__ == "__main__":
    app.run(debug=True)