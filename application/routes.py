from application import app, db
from flask import render_template, request, Response, flash, redirect
import json
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

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
    form = RegisterForm()
    return render_template("register.html", form=form, title="Register", register=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get("email") == "test@uta.com":
            flash("You are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "warning")
    return render_template("login.html", form=form, title="Login", login=True)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    id = request.form.get("courseID")
    title = request.form.get("title")
    term = request.form.get("term")
    return render_template("enrollment.html", data={
        "id": id,
        "title": title,
        "term": term,
    })

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    with open("courses.json", "r") as file:
        courseList = json.load(file)
        if idx is None:
            jdata = courseList
        else:
            jdata = courseList[int(idx)]
    return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/user")
def user():
    # User(userId=1, firstName="Alfred", lastName="Hithcock", email="alfred@hitchcock.com",
    #      password="abc1234").save()
    # User(userId=2, firstName="Miranda", lastName="Watson", email="miranda@watson.com",
    #      password="password00").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
