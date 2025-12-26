from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake database
users = []
user_id = 1


@app.route("/")
def home():
    return redirect(url_for("list_users"))


# GET - Show all users
@app.route("/users")
def list_users():
    return render_template("users.html", users=users)


# GET - Show add user form
@app.route("/users/add")
def add_user_form():
    return render_template("add_user.html")


# POST - Add user
@app.route("/users/add", methods=["POST"])
def add_user():
    global user_id

    name = request.form["name"]
    email = request.form["email"]

    users.append({
        "id": user_id,
        "name": name,
        "email": email
    })

    user_id += 1
    return redirect(url_for("list_users"))


# GET - Show edit form
@app.route("/users/edit/<int:id>")
def edit_user_form(id):
    for user in users:
        if user["id"] == id:
            return render_template("edit_user.html", user=user)

    return "User not found"


# POST (PUT logic) - Update user
@app.route("/users/update/<int:id>", methods=["POST"])
def update_user(id):
    for user in users:
        if user["id"] == id:
            user["name"] = request.form["name"]
            user["email"] = request.form["email"]
            break

    return redirect(url_for("list_users"))



@app.route("/users/delete/<int:id>", methods=["POST"])
def delete_user(id):
    global users
    users = [user for user in users if user["id"] != id]
    return redirect(url_for("list_users"))


if __name__ == "__main__":
    app.run(debug=True,port=5001)
