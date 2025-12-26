from flask import Flask, render_template, request, redirect, url_for
import os
from config.config import config
from flask_sqlalchemy import SQLAlchemy
from extension import db
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    return app

app=create_app()

class users(db.Model): 
    __tablename__='users'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),unique=True,nullable= False)
    create_at=db.Column(db.DateTime,default=datetime.now)





@app.route("/")
def home():
    return redirect(url_for("list_users"))



@app.route("/users")
def list_users():
    all_users = users.query.all()  
    return render_template("users.html", users=all_users)



@app.route("/users/add")
def add_user_form():
    return render_template("add_user.html")


@app.route("/users/add", methods=["POST"])
def add_user():

    name = request.form["name"]
    email = request.form["email"]
    new_user=users(name=name , email=email )
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for("list_users"))



@app.route("/users/edit/<int:id>")
def edit_user_form(id):
        edit_user=users.query.get(id)
        if edit_user is None:
            return "User not found" 
        return render_template("edit_user.html", user=edit_user)

    


@app.route("/users/update/<int:id>", methods=["POST"])
def update_user(id):
    user_update=users.query.get(id)
    if user_update is None:
        return "User not found"
    
        
    user_update.name= request.form["name"]
    user_update.email= request.form["email"]
    db.session.commit()
    return redirect(url_for("list_users"))



@app.route("/users/delete/<int:id>", methods=["POST"])
def delete_user(id):
    user_delete=users.query.get(id)
    if user_delete is None:
        return redirect(url_for("list_users"))
    db.session.delete(user_delete)
    db.session.commit()
    return redirect(url_for("list_users"))

if __name__ == "__main__":
    app.run(debug=True)
