#!/usr/bin/env python3
""" Module of Index views
"""
import base64
# from datetime import datetime

from pathsapp import app_views
from flask import render_template, request, redirect, url_for
from flask import session, make_response

@app_views.route('/signin', methods=['GET'])
def login():
    """returns the sign in page"""
    redirect_route = session.pop("formal", None)
    if redirect_route:
        response = make_response(render_template("signin.html"))
        response.set_cookie("pwd", redirect_route)
        return response
    return render_template("signin.html")


@app_views.route("/vitalsign", methods=["GET"])
def vitalsign():
    """returns vitalsign"""
    if request.cookies.get('nin'):
        nin = request.cookies.get('nin')
        nin = base64.b64decode(nin).decode('utf-8')
        return render_template("vitalsign.html", nin=nin)
    current = request.path
    print(current)
    session["formal"] = current
    return redirect(url_for("app_views.login"))


@app_views.route("/signup", methods=["GET"])
def register():
    """returns signup page"""
    return render_template("signup.html")


@app_views.route("/casefile", methods=["GET"])
def casefile():
    """returns casefile page"""
    print("opening casefile")
    if request.cookies.get('nin'):
        nin = request.cookies.get('nin')
        nin = base64.b64decode(nin).decode('utf-8')
        return render_template("casefile2.html", nin=nin)
    current = request.path
    print(f'path from casefile {current}')
    session["formal"] = current
    return redirect(url_for("app_views.login"))



@app_views.route("/logout")
def logout():
    """log out user"""
    return "logged out"
