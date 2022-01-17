from distutils.log import debug
from flask import Flask, redirect, render_template, request, url_for, session, flash
from datetime import timedelta


app = Flask(__name__)
# for session
app.secret_key = "something secret for using session"

# for permanent session to how to hold the session values
app.permanent_session_lifetime = timedelta(days=1)

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

@app.route("/usr")
def user():
    #password = request.form["ps"]
    if "username" in session:
        usr = session["username"]
        return render_template("user.html",user=usr)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    
    if "username" in session:
    # deleting the key "username" from dictory called "session"
        session.pop("username", None)
        flash("You have been logged out!")
    else:
        flash("Please Login")
        # after clearing the session, we are redirecting the user to login page
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)