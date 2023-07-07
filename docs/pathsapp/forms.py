from pathsapp import app_views
from flask import render_template, request, redirect
from flask_login import login_user, login_required, logout_user
from pathsapp.user import User

@app_views.route('/signin', methods=['GET', 'POST'])
def signin():
    """returns the sign in page"""
    if request.method == "GET":
        return render_template("signin.html")
    details = request.json
    userdetails = details.get("user")
    userdetails.pop("__class__")
    user = User(**userdetails)
    user.setme("access_token", details.get("access_token"))
    login_user(user)
    return redirect(f"/dashboard/{user.personality}")

@app_views.route("/vitalsign", methods=["GET", "POST"])
@login_required
def vitalsign():
    """returns vitalsign"""
    if request.method == "GET":
        return render_template("vitalsign.html")
    return render_template("vitalsign.html")

@app_views.route("/logout")
def logout():
    logout_user()
    return "logged out"
