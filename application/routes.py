from application import app
from flask import render_template, request
import json

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False, index=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="2025"):
    with open("courses.json", "r") as file:
        courseList = json.load(file)
    return render_template("courses.html", courses=courseList, course=True, term=term)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

@app.route("/enrollment", methods=["GET"])
def enrollment():
    id = request.args.get("courseID")
    title = request.args.get("title")
    term = request.args.get("term")
    return render_template("enrollment.html", data={
        "id": id,
        "title": title,
        "term": term,
    })
