#!/usr/bin/env python3
""" Module of Index views
"""
from pathsapp import app_views
from datetime import datetime
import json
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


@app_views.route("/signup", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("signup.html")
    user_data = request.json
    if user_data['user'] == "doctor":
        from register_function import register_doctor
        user_data["dob"] = datetime.strptime(json.loads(user_data['dob']), "%Y-%m-%d")
        register_doctor(**user_data)
    return "saved"


@app_views.route("/logout")
def logout():
    return "logged out"
