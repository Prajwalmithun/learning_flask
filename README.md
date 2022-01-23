# Learning flask daily

# My Learning Logs

# Day 1 (Installing flask, creating and starting app)
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

@app.route("/")
def home():
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
@app.route("/not_allowed")
def not_allowed():
    return "<h1> This page is restricted for normal user</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("not_allowed"))
```
</details>

# Day 2 (About templates )

<details>
<summary> What are templates? What does it contains? </summary>

`templates` is a directory, which contains static files like HTML, CSS. 

And it also contains placeholders for dynamic values( for eg: using jinja expression to get values from flask to html files)

</details>

<details>
<summary> What is Template Library? Which template library is used in flask? </summary>

</details>

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

</details>

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
</details>


# Day3 (About creation and rendering the templates )

<details> 
<summary> Template inheritance ?  </summary>

Templates are like, writing a blueprint.
Rather than typing all the contents again and again, we are only typing the changed contents and inheriting the contents that is common across the web pages

</details>

<details> 
<summary> How to use templates in flask ? </summary>

<b>Creation of templates</b>
Under `templates` directory we can create templates in flask. for example base.html etc so child pages can inherit base.html

</details>

<details> 
<summary>What is base template , child . ? </summary>

Base template = like a master file, how entire website/webpages should look like. Purpose if for website uniformity (like theme in vague terms)

Child - webpages that inherit from the base template

base.html -> index.html
</details>


<details> 
<summary>How to over-ride child template ? like how to make child template show different content but the theme
should be same as base template. </summary>

<b>in base.html</b>

<title> {% block title %}{% endblock %} </title>

<body>
{% block content %}{% endblock %}  
</body>

<b>in child.html</b>
{% extends "base.html" %}
{% block title %}Welcome to child page {% endblock %}
{% block content%}

<h1>This is child!</h1>

{% endblock %} 

</details>


<details> 
<summary> What is Bootstrap ? </summary>

For styling, kind of advanced version of CSS
</details>

<details> 
<summary> How to use it ? or how to include in our project ? </summary>

</details>

# Day 4 (About methods GET, POST)
<details> 
<summary> GET and POST request </summary>

</details>
 
<details> 
<summary> How to use it in flask ? </summary>

<b>Import the package(request)</b> 

from flask import request

<b>Usage:</b>

Say this is the html file

<b>login.html</b>

```
<form>
	<p>Username</p> 
		<input type="text" name="nm">
	<p>Password</p>
		<input type="password" name="ps">
	<input type="submit" value="Login">	
	
</form>
```

<b>in day4.py</b> 

```
from flask import request

@app.route("/login")
def login():
	if request.method == "POST":
		username = request.form("nm")
		password = request.form("ps")
		return f"{username} {password}"
```
</details>

# Day 5 (About sessions)

<details> 
<summary> What are sessions ? </summary>

Kind of Data structure to hold temporary values. In python, session is a dictonary.

</details>


<details> 
<summary> How to use in flask </summary>
	1. importing session 
	
	`from flask import session`

	2. Adding a secret key 
	
	`app.secret_key = "some complex key"`
		
	rem: session is a dictonary. 
	
	3. Add a key to session dictonary and assign the value given by the user
	
	`session["username_key"] = request.form["nm"]`
	
	4. pass it to different routes

</details>


<details> 
<summary> Are sessions permanent ?  </summary>
No by default.

But we can make it permanent

</details>


<details> 
<summary> If they are temporary how to make them permanent ? </summary>

	1. importing datetime.timedelta
	
	`from datetime import timedelta`
	
	2. Fix some duration for the session 
	
	`app.permanent_session_lifetime = timedelta(days=1)`
	
	3. After getting the value from user (previous step3) make session permanent
	
	`session.permanent = True`

</details>

# Day 6 (About Flashing messages)

<details> 
<summary> What is message flashing ? </summary>

</details>

<details> 
<summary> How to use in flask ? </summary>

<b>in .html file</b>

```
{% with messages = get_falshed_messages() %}
	{% if messages %}
		{% for msg in messages %}
			<p>{{msg}}</p>
		{% endfor %}
	{% endif %}
{% endwith %}
```
<b>in .py file</b>

```
from flask import flash

flash("Login succesfull","info")
```

</details>

# Day 7 (About SQLAlchemy Database)

<details> 
<summary> What is SQLAlchemy ? SQL vs SQLAlchemy ? </summary>

SQLAlchemy is python library for creating communication between python program and database.

This library is used as Object Relational Mapper (ORM). ORM means to 
converts 

```
python classes -> table in RDBMS

function calls -> SQL statements 
```

SQL => Its query language 

SQLAlchemy => is python library for managing kind of sql database.


</details>

<details> 
<summary> How to install it ? </summary>

`pip3 install flask-sqlalchemy`

</details>

<details> 
<summary> How to connect to flask to database ? </summary>

1. Import the package
`from flask_sqlalchemy import SQLAlchemy`

2. Configure and create db object

```
# configuring SQLAlchemy 'users' -> name of the table in SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
```

```
# Creating db object
db = SQLAlchemy(app)
```

3. Creating the class(table)

```
# In this example users = tables, Column names = id(int, primary key), name(string), email(string) 

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    # for initilizing default values
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

</details>

<details> 
<summary> How to do operations on database (CRUD: Create, Update, Read, Delete ) ? </summary>

</details>






 





		
		



	
	 

 
















