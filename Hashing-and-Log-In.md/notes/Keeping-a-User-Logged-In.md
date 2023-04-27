Title: "Keeping a User Logged in"

Section Title: "Intermediate Flask"

Subsection Title: "Hashing and Logging In"

Key Concepts:

1. Flask Sessions: Flask sessions are used to persist information and add state on top of the HTTP protocol, which is stateless by default. They are crucial for remembering if a user is logged in or not.

2. User Authentication: Users are authenticated by checking their submitted credentials against stored user data in the database. The class method `user.authenticate` is used to achieve this.

3. Storing User ID in the Session: When a user logs in successfully, their user ID is stored in the session, which can then be used to determine if the user is logged in or not.

4. Displaying Content Based on User Status: Based on the presence of the user ID in the session, you can show or hide content in your templates or control access to certain routes.

5. Protecting Routes: You can add logic to your view functions to ensure that only logged-in users can access certain routes. If a user is not logged in, you can redirect them to a different page or show an error message.

6. Logging Out: To log a user out, you simply remove their user ID from the session using `session.pop('user_id')`. This will make the user appear as not logged in, and they will lose access to protected content.

7. Associating User with Models: To associate a user with a particular model (e.g., a comment or a post), you can use the user ID stored in the session. This allows you to show the correct content to users and implement features like allowing only the owner of a comment to delete it.

These concepts are essential for building an effective user authentication system and controlling access to content based on a user's login status. By using Flask sessions and the techniques discussed, you can create dynamic web applications that adapt to the user's authentication state.

Sure, here's a simple Flask application that demonstrates user registration, login, logout, and protected routes using Flask sessions.

1. Install required packages:

```bash
pip install Flask Flask-SQLAlchemy Flask-Bcrypt
```

2. app.py:

```python
from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth_demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=10)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session["user_id"] = user.id
            flash("Logged in successfully!", "success")
            return redirect(url_for("secret"))
        else:
            flash("Invalid credentials.", "danger")
    return render_template("login.html")


@app.route("/secret")
def secret():
    if "user_id" not in session:
        flash("You must be logged in to access this page.", "danger")
        return redirect(url_for("index"))
    return render_template("secret.html")


@app.route("/logout")
def logout():
    session.pop("user_id")
    flash("Logged out successfully!", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```

3. templates/index.html:

```html
{% for message_category, message in get_flashed_messages(with_categories=true) %}
<div class="alert alert-{{ message_category }}">{{ message }}</div>
{% endfor %}

{% if "user_id" in session %}
<a href="{{ url_for("logout") }}">Logout</a>
{% else %}
<a href="{{ url_for("register") }}">Register</a> |
<a href="{{ url_for("login") }}">Login</a>
{% endif %}
```

4. templates/register.html:

```html
{% extends "index.html" %}

{% block content %}
<h1>Register</h1>
<form method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <br>
    <input type="submit" value="Register">
</form>
{% endblock %}
```

5. templates/login.html:


