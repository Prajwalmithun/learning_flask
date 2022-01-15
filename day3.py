from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", msg="Start")

@app.route("/user1")
def test():
    return render_template("user1.html")
    
if __name__ == "__main__":
    app.run(debug=True)