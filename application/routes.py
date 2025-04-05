from application import app, db
from flask import render_template, request, Response, flash, redirect, url_for
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
def courses(term=None):
    if term is None:
        term = "Spring 2025"
    classes = Course.objects.order_by("objectID")
    return render_template("courses.html", courses=classes, course=True, term=term)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        userID = User.objects.count()
        userID += 1
        email = form.email.data
        password = form.password.data
        firstName = form.firstName.data
        lastName = form.lastName.data

        user = User(user_id=userID,
                    first_name=firstName,
                    last_name=lastName,
                    email=email)
        user.set_password(password)
        user.save()
        flash("You are successfully registered", "success")
        return redirect(url_for("index"))
    return render_template("register.html", form=form, title="Register", register=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()

        if user and user.get_password(password):
            flash(f"{user.first_name} logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "warning")
    return render_template("login.html", form=form, title="Login", login=True)

@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    courseID = request.form.get("courseID")
    courseTitle = request.form.get("title")
    user_id = 1

    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(f"You are already enrolled for {courseTitle}", "warning")
            redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id, courseID=courseID).save()
            flash(f"You are now enrolled in {courseTitle}", "success")

    term = request.form.get("term")
    classes = list(User.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'enrollment',
                'localField': 'user_id',
                'foreignField': 'user_id',
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1',
                'includeArrayIndex': 'r1_id',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'course',
                'localField': 'r1.courseID',
                'foreignField': 'courseID',
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'user_id': user_id
            }
        }, {
            '$sort': {
                'courseID': 1
            }
        }
    ]))

    return render_template("enrollment.html", classes=classes, enrollment=True, title="Enrollment")

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
