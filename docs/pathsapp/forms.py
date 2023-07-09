from pathsapp import app_views
from flask import render_template, request, redirect

@app_views.route('/signin', methods=['GET', 'POST'])
def login():
    """returns the sign in page"""
    # if request.method == "GET":
    return render_template("signin.html")


@app_views.route("/vitalsign", methods=["GET", "POST"])
def vitalsign():
    """returns vitalsign"""
    if request.method == "GET":
        return render_template("vitalsign.html")
    return render_template("vitalsign.html")

@app_views.route("/logout")
def logout():
    return "logged out"
