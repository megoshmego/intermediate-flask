Introduction to Authentication and Authorization in Flask

Authentication is the process of verifying the identity of a user, while authorization is the process of determining what a user is allowed to do. In this tutorial, we will be implementing authentication and authorization in a Flask application.

Setting up the environment
First, we'll install the required packages for our project, such as Flask, Flask-Login, and Flask-SQLAlchemy.

bash
Copy code
pip install Flask Flask-Login Flask-SQLAlchemy
Creating the User model
We'll create a simple User model for our application using Flask-SQLAlchemy.

python
Copy code
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
Setting up Flask-Login
We'll configure Flask-Login to handle user sessions.

python
Copy code
from flask_login import LoginManager

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
Creating the login view
We'll create a simple login view that authenticates users using the User model.

python
Copy code
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)
login_manager.init_app(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('protected'))
        else:
            flash('Invalid username or password.')

    return render_template('login.html')
Creating the protected view
We'll create a simple protected view that requires users to be logged in.

python
Copy code
from flask_login import login_required, current_user

@app.route('/protected')
@login_required
def protected():
    return f"Welcome, {current_user.username}!"
Implementing role-based authorization
We'll extend the User model to include roles and permissions.

python
Copy code
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    permissions = db.Column(db.String(255), nullable=False)

class UserRole(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('user_roles', lazy=True))
    role = db.relationship('Role', backref=db.backref('user_roles', lazy=True))
We'll create a decorator to check if a user has a specific permission.

python
Copy code
from functools import wraps
from flask_login import current_user

def has_permission(permission):
    def decorator(f):
        @wraps(f
