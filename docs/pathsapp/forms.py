#!/usr/bin/env python3
""" Module of Index views
"""
from pathsapp import app_views
from datetime import datetime
import base64
from flask import render_template, request, redirect, url_for

@app_views.route('/signin', methods=['GET'])
def login():
    """returns the sign in page"""
    # if request.method == "GET":
    return render_template("signin.html")


@app_views.route("/vitalsign", methods=["GET"])
def vitalsign():
    """returns vitalsign"""
    if request.cookies.get('nin'):
        nin = request.cookies.get('nin')
        nin = base64.b64decode(nin).decode('utf-8')
        return render_template("vitalsign.html", nin=nin)
    return redirect(url_for("app_views.login"))


@app_views.route("/signup", methods=["GET"])
def register():
    if request.method == "GET":
        return render_template("signup.html")
    # user_data = request.json
    # if user_data['user']:# == "doctor":
    #     from pathsapp.register_function import register_doctor
    #     user_data["dob"] = datetime.strptime(user_data['dob'], "%Y-%m-%d")
    #     status = register_doctor(**user_data)
    # return status


@app_views.route("/logout")
def logout():
    return "logged out"
