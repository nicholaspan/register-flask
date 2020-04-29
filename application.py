import sqlite3 
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

DATABASE = "lecture.db"
# Default route: index.html
# Display all of the current registrants in lecture.db
@app.route('/')
def index():
    db = sqlite3.connect(DATABASE)
    rows = db.execute("SELECT * FROM registrants")
    return render_template("index.html", rows = rows)

@app.route('/register', methods=["GET",  "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        db = sqlite3.connect(DATABASE)
        db.execute("INSERT INTO registrants (name, email) VALUES (?, ?)", (name, email))
        db.commit()
        return redirect("/")