from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/c1")
def child1():
    return render_template("child1.html")

@app.route("/c2")
def child2():
    return render_template("child2.html")


if __name__ == "__main__":
    app.run(debug="True")