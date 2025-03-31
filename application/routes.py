from application import app
from flask import render_template
import json

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False, index=True)

@app.route("/courses")
def courses():
    with open("courses.json", "r") as file:
        courseList = json.load(file)
    return render_template("courses.html", courses=courseList, course=True)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)
