# Learning flask

# My Learning Logs

## Day 1
<details>
<summary> What is Flask? </summary>
Its a python micro-framework to develop web application.
</details>

<details>
<summary> What is framework vs micro framework?</summary>
Web Framework - Collection of libraries and modules, so a developer doesnt need to worry about low-level details like thread management, protocol etc

Micro Framework - Mimimalistic version of full fledged framework. But flask has extentions to parts where there are limitations.

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

if __name__ == __main__

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
