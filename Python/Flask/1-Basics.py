from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "VerySecureKey1"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(seconds=50)

database = SQLAlchemy(app)

class users(database.Model):
    _id = database.Column("id", database.Integer, primary_key=True)
    name = database.Column(database.String(500))
    password = database.Column(database.String(20))

    def __init__(self, name, password):
        self.name = name
        self.password = password

@app.route("/")
def homePage():
    return '<div style="background-color: dodgerblue;"> This is the home page.</div>'

@app.route("/<name>")
def inputPage(name):
    return f"This is {name} page"

@app.route("/greeting/<name>")
def greetingPage(name):
    return f"Hello {name}!"

@app.route("/adminPage")
def adminPage():
    return "You are on the admin panel now."

@app.route("/admin/") # Trailing slash will allow user to access to the page either using trailing slash or without using it.
def admin():
    isAdmin = False
    if isAdmin:
        return redirect(url_for("adminPage"))
    else:
        return redirect(url_for("inputPage", name="not admin"))

@app.route("/template1")
def template1():
    return render_template("changed.html")

from time import sleep
@app.route("/template2/<input>")
def template2(input):
    return render_template("template2.html", content= input, function= sleep) # It's possible to give multiple inputs with creating different arguments in html file
    # Content does not have to be input. It's possible to pass any variable like list and use them in html code. 

@app.route("/base", methods=["POST","GET"])
def base():
    if request.method == "POST":
        session.permanent = True # Even if you close the web browser, session data will not be losed until lifetime passes.
        try:
            username = request.form["nm"] # We are requesting with a dictionary key, so we can have as much as key-value pair (form) we want
            password = request.form["pw"]
        except:
            flash("Please fill in both username and password boxes.")
        else:
            foundUser = users.query.filter_by(name = username).first()
            if foundUser:
                if password == users.query.filter_by(password = password).first().password:
                    session["user"] = username
                    session["password"] = password
                    flash(f"Logged in sucessfully. Welcome back {username}")
                else:
                    flash("Wrong password. Please try again.")
            else:
                user = users(username, password)
                database.session.add(user)
                database.session.commit()
                flash("Registered successfully. Welcome!")
        return redirect(url_for("user"))
            #return redirect(url_for("greetingPage", name= username))
    else:
        content = None
        registeredUsers = users.query.all()
        if "user" in session:
            content = session["user"]
        return render_template("base.html", username= content, registeredUsers=registeredUsers)

@app.route("/child")
def child():
    return render_template("child.html", username= None)

@app.route("/user")
def user():
    return render_template("userPanel.html")

@app.route("/logout")
def logout():
    if "user" not in session:
        flash("You are not logged in. You can use here to log in.")
    else:
        flash(f"You have been logged out {session['user']}!", "info")
        session.pop("user")
        session.pop("password")
    return redirect(url_for("base"))

@app.route("/removeAccount")
def removeAccount():
    if "user" not in session:
        flash("You must logged in to delete your account.")
        return redirect(url_for("base"))
    else:
        flash(f"Your account has been deleted permanently {session['user']}!", "info")
        users.query.filter_by(name = session["user"]).delete()
        database.session.commit()
        return redirect(url_for("logout"))

@app.route("/secondWebsite")
def secondWebsite():
    return render_template("secondWebsite.html")

# Blueprints allow us to reuse templates in different projects.

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
        app.run(debug= True) # Dynamic changes will be implemented as you save the file, if you are in debug mode
