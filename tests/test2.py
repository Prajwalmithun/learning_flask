from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", msg="Home Page")

@app.route("/login")
def login():
    return render_template("sign_in.html")

if __name__ == "__main__":
    app.run(debug=True)