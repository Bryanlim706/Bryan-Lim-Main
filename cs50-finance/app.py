import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# datetime import for buy route
from datetime import datetime, timezone

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    """Show portfolio of stocks"""

    group_by = db.execute(
        "SELECT stock, SUM(number_of_stock) AS total_number_of_stock "
        "FROM records "
        "WHERE username = (SELECT username FROM users WHERE id = ?) "
        "GROUP BY stock",
        session["user_id"]
    )
    # remove redundant row from finance.db records table
    for i, item in enumerate(group_by):
        if item["total_number_of_stock"] == 0:
            del group_by[i]

    stock_owned = []
    for item in group_by:
        stock_owned.append(item["stock"])

    number_of_shares_owned = []
    for item in group_by:
        number_of_shares_owned.append(int(item["total_number_of_stock"]))

    current_price_of_stock_i = []
    for item in group_by:
        current_price_of_stock_i.append(float((lookup(item["stock"]))["price"]))

    current_price_of_stock = []
    for item in current_price_of_stock_i:
        current_price_of_stock.append(usd(item))

    total_value_i = []
    for a, b in zip(number_of_shares_owned, current_price_of_stock_i):
        total_value_i.append(a * b)

    total_value = []
    for item in total_value_i:
        total_value.append(usd(item))

    combined_data_1 = list(zip(stock_owned, number_of_shares_owned,
                           current_price_of_stock, total_value))

    current_cash_balance = db.execute(
        "SELECT cash FROM users WHERE id=?", session["user_id"]
    )[0]["cash"]
    grand_total = float((db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"]))[
                        0]["cash"]) + float(sum(total_value_i))

    return render_template("index.html", combined_data_1=combined_data_1, current_cash_balance=usd(current_cash_balance), grand_total=usd(grand_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        stock_to_buy = (lookup(request.form.get("symbol")))
        cash_remaining = int(
            ((db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"]))[0])["cash"])

        # symbol blank/does not exist or number of shares not positive integer
        if not stock_to_buy:
            return apology("invalid stock symbol", 400)

        elif (not request.form.get("shares").isdigit()) or (int(request.form.get("shares")) < 1):
            return apology("invalid number of shares", 400)

        # cannot afford number of shares at current price
        elif (cash_remaining < (int(request.form.get("shares")) * float(stock_to_buy["price"]))):
            return apology("cannot afford the number of shares at the current price", 400)

        # update finance.db records table
        username = (db.execute("SELECT username FROM users WHERE id = ?",
                    session["user_id"]))[0]["username"]
        stock = stock_to_buy["symbol"]
        price = float(stock_to_buy["price"])
        time = (datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S")
        number_of_stock = int(request.form.get("shares"))

        db.execute("INSERT INTO records (username, stock, price, time, number_of_stock) VALUES (?, ?, ?, ?, ?)",
                   username, stock, price, time, number_of_stock)

        # update cash remaining
        cash_remaining = cash_remaining - (price * number_of_stock)
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", cash_remaining, session["user_id"]
        )

        # redirect to homepage
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    date_time = []
    date_time_i = db.execute("SELECT time FROM records")
    for item in date_time_i:
        date_time.append(item["time"])

    type = []
    type_i = db.execute("SELECT number_of_stock FROM records")
    for item in type_i:
        if item["number_of_stock"] > 0:
            type.append("Bought")
        else:
            type.append("Sold")

    stock = []
    stock_i = db.execute("SELECT stock FROM records")
    for item in stock_i:
        stock.append(item["stock"])

    price_when_bought_sold = []
    price_when_bought_sold_i = db.execute("SELECT price FROM records")
    for item in price_when_bought_sold_i:
        price_when_bought_sold.append(usd(item["price"]))

    number_of_shares_bought_sold = []
    number_of_shares_bought_sold_i = db.execute("SELECT number_of_stock FROM records")
    for item in number_of_shares_bought_sold_i:
        number_of_shares_bought_sold.append(abs(item["number_of_stock"]))

    combined_data = list(zip(date_time, type, stock, price_when_bought_sold,
                         number_of_shares_bought_sold))

    return render_template("history.html", combined_data=combined_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        quote = (lookup(request.form.get("symbol")))

        if not quote:
            return apology("invalid stock symbol", 400)

        else:
            return render_template("quoted.html", price=usd(quote["price"]), symbol=quote["symbol"])

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Ensure username was submitted and not blank
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted and not blank
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("password") == request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # Store username and hash if username is not already in database
        try:
            db.execute("INSERT INTO users(username, hash) VALUES (?, ?)",
                       request.form.get("username"), generate_password_hash(request.form.get("password")))
        except ValueError:
            return apology("username already exists", 400)

        return render_template("login.html")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    group_by = db.execute(
        "SELECT stock, SUM(number_of_stock) AS total_number_of_stock "
        "FROM records "
        "WHERE username = (SELECT username FROM users WHERE id = ?) "
        "GROUP BY stock",
        session["user_id"]
    )
    """Sell shares of stock"""
    if request.method == "POST":

        for item in group_by:
            if item["stock"] == request.form.get("symbol"):
                number_of_stocks = int(item["total_number_of_stock"])

        # check if fail to select stock, number of stock not a positive integer
        if not request.form.get("symbol"):
            return apology("no option selected", 400)

        elif (not request.form.get("shares").isdigit()) or (int(request.form.get("shares")) < 1):
            return apology("invalid number of shares", 400)

        # check if enough shares to sell
        elif (number_of_stocks < int(request.form.get("shares"))):
            return apology("not enough shares to sell", 400)

        # update finance.db records table
        stock_to_buy = (lookup(request.form.get("symbol")))
        cash_remaining = int(
            ((db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"]))[0])["cash"])

        username = (db.execute("SELECT username FROM users WHERE id = ?",
                    session["user_id"]))[0]["username"]
        stock = request.form.get("symbol")
        price = float(stock_to_buy["price"])
        time = (datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M:%S")
        number_of_stock = int(request.form.get("shares")) * -1

        db.execute("INSERT INTO records (username, stock, price, time, number_of_stock) VALUES (?, ?, ?, ?, ?)",
                   username, stock, price, time, number_of_stock)

        # update cash remaining
        cash_remaining = cash_remaining - (price * number_of_stock)
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", cash_remaining, session["user_id"]
        )

        return redirect("/")

    else:
        # provide options for stock input

        stocks = []
        for item in group_by:
            stocks.append(item["stock"])

        return render_template("sell.html", stocks=stocks)


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
