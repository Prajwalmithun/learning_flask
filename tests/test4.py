from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, request
from markupsafe import re

app = Flask(__name__)


@app.route("/form", methods=["POST", "GET"])
def met():
    if request.method == "GET":
        return render_template("forms.html")
    else:
        user = request.form["nm"]
        return f"<h1>{user}! You are logged in, What's app? </h1>"


if __name__ == "__main__":
    app.run(debug=True)