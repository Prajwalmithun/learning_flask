# Learning flask

# My Learning Logs

## Day 1
<details>
<summary> What is Flask? </summary>
Its a python micro-framework to develop web application.
</details>

<details>
<summary> What is framework vs micro framework?</summary>

<b>Web Framework</b> - Collection of libraries and modules, so a developer doesnt need to worry about low-level details like thread management, protocol etc

<b>Micro Framework</b> - Mimimalistic version of full fledged framework. But flask has extentions to parts where there are limitations.

</details>

<details>
<summary> How to install flask ? </summary>
Create virtualenvironment - why? to manage package dependencies

`# virtualenv venv`

Activate the virtual environment

`# source venv/bin/activate`

Install flask

`#pip3 install flask`

</details>

<details>
<summary> How to import Flask? </summary>

Add this line to the beginning of .py file

`from flask import Flask`

</details>

<details>
<summary> How to create app instance ? </summary>

After import flask we can create app instance 

`app = flask(__name__)`

</details>

<details>
<summary> How to run flask ? </summary>

Just like how we run normal python files

`python3 filename.py`

</details>

<details>
<summary> What are decorators ?</summary>
In python, decorators are function that take function as argument and returns another function.

Example

```
from flask import Flask

app = Flask(__name__)

@app.route()
def home("/"):
    return "This is home page"

if __name__ == "__main__":
    app.run(debug=True)
```

</details>

<details>
<summary> route() how to use and what it does ? </summary>

`route()` is a decorator in flask. 

<b>How to use it :</b>

```
@app.route("/")
def home():
    return "Home page"
```

<b>What it does:</b>

Adds endpoint to app object
</details>


<details>
<summary> redirect() and url_for() </summary>

`redirect()` : Flask function to redirect the users to specified URL 

`url_for()` : Flask function, for creating a URL to prevent the overhead of having to change URLs throughout the application.

<b>Usage</b>

```
@app.route(/not_allowed)
def not_allowed():
    return "<h1> This page is restricted for normal user</h1>"

@app.route(/admin)
def admin():
    return redirect(url_for("not_allowed"))
```
</details>

## Day 2

<details>
<summary> What are templates? What does it contains? </summary>

`templates` is a directory, which contains static files like HTML, CSS. 

And it also contains placeholders for dynamic values( for eg: using jinja expression to get values from flask to html files)

</detals>

<details>
<summary> What is Template Library? Which template library is used in flask? </summary>

</detals>

<details>
<summary> render_template() ? Syntax and Usage OR How to render html from flask and how to pass value from backend to frontend? </summary>

`render_template()` - function which renders frontend files(HTML, CSS) to user's web browser. 

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("templates/index.html")

@app.route("/<usr>")
def user(usr):
    return render_template("templates/display.html", content=usr, msg="Hello")
```

</detals>

<details>
<summary> How to write python code in html ?</summary>

We use <b>Jinja expressions</b> to write kindaa python code in templates/*.html files

<b>Example</b> 

display.html

```
<html>
<head> 
    <title> Displays your name </title>
</head>
<body>
    {% for x in range(10) %}
        <p> {{msg}} {{usr}}
    {% endfor %}
</body>
</html>
```
</detals>
