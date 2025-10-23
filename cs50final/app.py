import os

from cs50 import SQL
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import json

# datetime import for buy route
from datetime import datetime, timezone

from helpers import apology, login_required, pre_apology

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    db.execute("UPDATE users SET cat_name = 'fitness, personal, work' WHERE cat_name IS NULL")

    name = db.execute("SELECT name FROM users WHERE id=?", session["user_id"])
    if len(name) == 0:
        name = [{"name":"hi"}]
    name = name[0]["name"]

    categories = db.execute("SELECT cat_name FROM users WHERE id=?", session["user_id"])
    categories = (categories[0]["cat_name"]).split(",")

    return render_template("home.html",categories=categories, name=name)

# Dynamic route for each category
@app.route('/category/<category_name>')
@login_required
def category_page(category_name):

    #data processing to generate all tasks for the category

    #admin insert

    #retrieve data from table and unjson it to python object
    all_goals = db.execute("SELECT goals FROM users WHERE id = ?", session["user_id"])
    if all_goals and all_goals[0]["goals"]:
        all_goals = json.loads(all_goals[0]["goals"])
    else:
        all_goals = []
    category_name = category_name.strip()

    # Filter goals by category
    filtered_goals = [goal for goal in all_goals if goal["category"] == category_name]

    #done columns at the bottom
    sorted_goals = sorted(filtered_goals, key=lambda goal: goal["status"] == "done")

    return render_template("category_page.html", category_name=category_name, goals=sorted_goals)

#get user input for add row to table
@app.route("/add_row", methods=["GET", "POST"])
@login_required
def add_row():
    if request.method == "POST":

        category_name = request.form.get("category_name")

        #retrieve data from table and unjson it to python object
        all_goals = db.execute("SELECT goals FROM users WHERE id = ?", session["user_id"])
        if all_goals and all_goals[0]["goals"]:
            all_goals = json.loads(all_goals[0]["goals"])
        else:
            all_goals = []
        category_name = category_name.strip()
        # Filter goals by category
        filtered_goals = [goal for goal in all_goals if goal["category"] == category_name]
        #done columns at the bottom
        sorted_goals = sorted(filtered_goals, key=lambda goal: goal["status"] == "done")

        return render_template("add_row.html", category_name=category_name, goals=sorted_goals)

#add user input from add row to database
@app.route("/added_row", methods=["GET", "POST"])
@login_required
def added_row():
    goal = request.form.get("goal")
    due_date = request.form.get("due_date")
    importance = request.form.get("importance")
    remarks = request.form.get("remarks")
    status = request.form.get("status")
    category_name = request.form.get("category_name")

    new_goal = {
    "goal": goal,
    "due_date": due_date,
    "importance": importance,
    "remarks": remarks,
    "status": status,
    "category": category_name
    }

    #update data in table
    all_goals = db.execute("SELECT goals FROM users WHERE id = ?", session["user_id"])
    if all_goals and all_goals[0]["goals"]:
        all_goals = json.loads(all_goals[0]["goals"])
    else:
        all_goals = []
    if new_goal not in all_goals:
        all_goals.append(new_goal)
    else:
        return pre_apology("similar goal already added", 400)
    db.execute("UPDATE users SET goals = ? WHERE id = ?", json.dumps(all_goals), session["user_id"])

    return redirect(url_for('category_page', category_name=category_name))

#delete row from database
@app.route("/delete_row", methods=["GET", "POST"])
@login_required
def delete_row():
    if request.method == "POST":
        category_name = request.form.get("category_name")
        goall = request.form.get("goal")
        due_date = request.form.get("due_date")
        importance = request.form.get("importance")
        remarks = request.form.get("remarks")
        status = request.form.get("status")
        all_goals = db.execute("SELECT goals FROM users WHERE id = ?", session["user_id"])

        if all_goals and all_goals[0]["goals"]:
            all_goals = json.loads(all_goals[0]["goals"])
        else:
            all_goals = []

        print("dueduededuehduedhuhdu")
        print(all_goals)
        print(goall)

        all_goals = [goal for goal in all_goals if not (
        goal["goal"] == goall and
        goal["due_date"] == due_date and
        goal["importance"] == importance and
        goal["remarks"] == remarks and
        goal["status"] == status and
        goal["category"] == category_name
        )]

        db.execute("UPDATE users SET goals = ? WHERE id = ?", json.dumps(all_goals), session["user_id"])

        return redirect(url_for('category_page', category_name=category_name))

#delete category from navbar
@app.route("/delete_category", methods=["GET", "POST"])
@login_required
def delete_category():
    if request.method == "POST":
        #update database
        category_to_delete = request.form.get("category_to_delete")

        categories = db.execute("SELECT cat_name FROM users WHERE id=?", session["user_id"])
        categories = (categories[0]["cat_name"]).split(",")
        categories.remove(category_to_delete)
        categories_joined = ",".join(categories)
        db.execute("UPDATE users SET cat_name = ? WHERE id= ?", categories_joined, session["user_id"])

        return redirect("/")


@app.route("/add_category", methods=["GET", "POST"])
@login_required
def add_category():
    if request.method == "POST":
        new_category = request.form.get("category")
        categories = db.execute("SELECT cat_name FROM users WHERE id=?", session["user_id"])
        categories = (categories[0]["cat_name"]).split(",")
        if new_category not in categories:
            categories.append(" " + new_category)
            categories_joined = ",".join(categories)
            db.execute("UPDATE users SET cat_name = ? WHERE id= ?", categories_joined, session["user_id"])

            name = db.execute("SELECT name FROM users WHERE id=?", session["user_id"])
            if len(name) == 0:
                name = [{"name":"hi"}]
            name = name[0]["name"]
            return render_template("home.html", categories=categories, name=name)
        else:
            return pre_apology("category name already used", 403)

    else:
        return render_template("add_category.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return pre_apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return pre_apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return pre_apology("invalid username and/or password", 404)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Ensure username was submitted and not blank
        if not request.form.get("username"):
            return pre_apology("must provide username", 400)

        # Ensure password was submitted and not blank
        elif not request.form.get("password"):
            return pre_apology("must provide password", 400)

        elif not request.form.get("password") == request.form.get("confirmation"):
            return pre_apology("passwords do not match", 400)

        # Store username and hash if username is not already in database
        try:
            db.execute("INSERT INTO users(username, hash, name) VALUES (?, ?, ?)",
                       request.form.get("username"), generate_password_hash(request.form.get("password")), request.form.get("display_name"))
        except ValueError:
            return pre_apology("username already taken", 400)

        return render_template("login.html")

    else:
        return render_template("register.html")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    if request.method == "POST":
        rows = db.execute(
            "SELECT * FROM users WHERE id = ?", session["user_id"]
        )
        # check if all input boxes are valid
        if not request.form.get("old_password") or not request.form.get("new_password") or not request.form.get("new_password_confirm"):
            return apology("please fill up all boxes required", 403)

        # check if old password is correct
        if len(rows) != 1 or not (check_password_hash(rows[0]["hash"], request.form.get("old_password"))):
            return apology("Old password is wrong", 403)

        # check if new passwords match
        elif request.form.get("new_password") != request.form.get("new_password_confirm"):
            return apology("Passwords do not match", 403)

        # check if old and new passwords are different
        elif request.form.get("old_password") == request.form.get("new_password"):
            return apology("Old and new passwords are the same", 403)

        # update password in users table of database
        db.execute("UPDATE users SET hash=? WHERE id=?", (generate_password_hash(
            request.form.get("new_password"))), session["user_id"])

        return render_template("passworded.html")

    else:
        return render_template("password.html")

