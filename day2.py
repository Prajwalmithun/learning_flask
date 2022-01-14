from distutils.log import debug
from flask import Flask, redirect, url_for, render_template

# Creating an instance of the app
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    # Passing the values from backend(flask) to frontend(html)
    return render_template("index.html", content=name, id=2, list=['bob', 'rob', 'cab'])


# Grab the value passed in URL and pass it to the function
## @app.route("/<name>")
## def user(name):
##    return f"Hello {name}"

# This function, we can use for redirecting. Here we are redirecting 
# users who try to access /admin ==> / page for security
## @app.route("/admin")
## def admin():
##    return redirect(url_for("user", name="Admin!!"))

if __name__ == "__main__":
    # debug -> no need to restart the flask each time
    app.run(debug=True)




### Day 2 - Summary ###
# 1. render_template() -> publish html to frontend 
# 2. how to pass values from backend to frontend using render_template()
# 3. templates -> directory where all the html files are present
# 4. index.html -> Also, how to write kinda of python code in html file 
# Example : This content is to be written in html file
# 
# {{% for x in range(10) % }}
#    <p> {{x}} </p>
# {{% endfor %}}