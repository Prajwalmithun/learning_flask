from distutils.log import debug
from flask import Flask, redirect, url_for

# Creating an instance of the app
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is home page <h1> This is Inline HTML tag </h1>"

# Grab the value passed in URL and pass it to the function
@app.route("/<name>")
def user(name):
    return f"Hello {name}"

# This function, we can use for redirecting. Here we are redirecting 
# users who try to access /admin ==> / page for security
@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    # debug -> no need to restart the flask each time
    app.run(debug=True)




#### Day 1 Summary ####
# 1. using route() to publish/show the users what webpage to render or just the text
# 2. redirect() -> for redirecting users to different route(bascially diffrent webpage) 
# 3. Passing the value in URL and backends grabs it and publish again in the frontend
 