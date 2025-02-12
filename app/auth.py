from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.user_store import users  # Import users

auth = Blueprint("auth", __name__)

class User(UserMixin):
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email

    @staticmethod
    def get_by_username(username):
        user = users.get(username)
        if user:
            return User(user["id"], user["username"], user["email"])
        return None

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.get(username)
        if user and check_password_hash(user["password_hash"], password):
            user_obj = User(user["id"], user["username"], user["email"])
            login_user(user_obj)
            return redirect(url_for("main.dashboard"))

        flash("Invalid username or password", "error")

    return render_template("auth/login.html")

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if username in users:
            flash("Username already exists!", "error")
        else:
            users[username] = {
                "id": str(len(users) + 1),
                "username": username,
                "email": email,
                "password_hash": generate_password_hash(password),
            }
            flash("Registration successful!", "success")
            return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
