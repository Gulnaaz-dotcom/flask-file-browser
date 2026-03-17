from flask import session, redirect, url_for, request, render_template
import hashlib

# USERNAME = "admin"
# PASSWORD = "admin@45"
## a55508996dada55e4725346ba2f57895daa78777a419d2ffa5b60d0e9457b0f1

USERNAME = "admin"
PASSWORD_HASH = "a55508996dada55e4725346ba2f57895daa78777a419d2ffa5b60d0e9457b0f1"

def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        if username == USERNAME and password_hash == PASSWORD_HASH:
            session["logged_in"] = True
            return redirect(url_for("root"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

def logout():
    session.clear()
    return redirect(url_for("login"))

def login_required(func):
    def wrapper(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
