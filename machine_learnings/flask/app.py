from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session management

# In-memory "database" of all registered users
users = []

# Home page
@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"], users=users)
    return render_template("home.html", username="Guest", users=users)
flask/app1.py
flask/app1.py

# Template greeting
@app.route("/hello/<name>")
def hello(name):
    return render_template("index.html", name=name)

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username  # Store in session
        if username not in users:
            users.append(username)
        return redirect(url_for("user_list"))
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    username = session.pop("username", None)
    return f"Logged out {username}. <a href='/login'>Login again</a>"


# List of all registered users
@app.route("/users") 
def user_list():    
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True,port=5005)
