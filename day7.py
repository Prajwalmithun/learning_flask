from crypt import methods
from distutils.log import debug
from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configuring SQLAlchemy 'users' -> name of the table in SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'

# optional config, just to make sure modification is not tracked.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# for session
app.secret_key = "something secret for using session"

# for permanent session to how to hold the session values
app.permanent_session_lifetime = timedelta(days=1)

# Creating db object
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    # for initilizing default values
    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def home():
    #flash("You are in home")
    return render_template("index.html")

@app.route("/login",methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        # for permanent session, because after closing browser, sessions will be deleted
        session.permanent = True
        
        # Cretating a dict called "session", key = "username", value = <value from html>
        session["username"] = user
        #password = request.form["ps"]
        #return redirect(url_for("user",usr=user))
        flash("Login Succesfull")
        return redirect(url_for("user"))
    
    else:
        if "username" in session:
            flash("Already Logged in!")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/usr", methods=["POST","GET"])
def user():
    email = None
    #password = request.form["ps"]
    if "username" in session:
        usr = session["username"]

        if request.method == "POST":
            email = request.form["h_email"]
            session["email"] = email
            flash("Email saved!")

        else:
            if "email" in session:
                email = session["email"]
                
        # publishing user.html and send values(email) to frontend
        return render_template("user.html",email=email)

    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    
    if "username" in session:
    # deleting the key "username" from dictory called "session"
        session.pop("username", None)
        session.pop("email",None)
        flash("You have been logged out!")
    else:
        flash("Please Login")
        # after clearing the session, we are redirecting the user to login page
    return redirect(url_for("login"))



if __name__ == "__main__":

    # create the db tables if the table doesnt exist in DB
    db.create_all()

    # run the app
    app.run(debug=True)