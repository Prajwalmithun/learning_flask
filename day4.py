from crypt import methods
from distutils.log import debug
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        password = request.form["ps"]
        #password = request.form["ps"]
        #return redirect(url_for("user",usr=user))
        return f"{user} {password}"
    
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    #password = request.form["ps"]
    return f"<h1> HI {usr} </h1>  "

if __name__ == "__main__":
    app.run(debug=True)