from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# This tells Flask where to create the database file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vidyapatra.db"
db = SQLAlchemy(app)

# This is your database table defined as a Python class
# Each variable = one column in the table
class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    college = db.Column(db.String(100), nullable=False)
    stream = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    board = db.Column(db.String(50), nullable=False)

    # This converts one Paper object into a dictionary
    # So Flask can turn it into JSON
    def to_dict(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "college": self.college,
            "stream": self.stream,
            "year": self.year,
            "board": self.board,
        }

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# GET all papers from the database
@app.route("/papers")
def get_papers():
    papers = Paper.query.all()
    return jsonify([p.to_dict() for p in papers])

# POST a new paper to the database
@app.route("/papers/add", methods=["POST"])
def add_paper():
    data = request.get_json()
    new_paper = Paper(
        subject=data["subject"],
        college=data["college"],
        stream=data["stream"],
        year=data["year"],
        board=data["board"],
    )
    db.session.add(new_paper)
    db.session.commit()
    return jsonify(new_paper.to_dict()), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)