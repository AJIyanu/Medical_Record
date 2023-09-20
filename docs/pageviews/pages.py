#!/usr/bin/env python3
"""all routes here"""

import json
from datetime import timedelta

from flask_jwt_extended import (create_access_token, set_access_cookies,
                                jwt_required, get_jwt_identity, get_jwt)
from flask import render_template, request, redirect, make_response #, jsonify
from sqlalchemy.orm.exc import NoResultFound

from models import storage
from models.patient import Patient
from models.loginauth import PersonAuth
from . import app_view


@app_view.route("/signin", methods=["GET", "POST"])
def authorizelogin():
    """
    returns sign in page
    redirect to dashbord on successful log in
    sets jwt tokens
    """
    if request.method == "GET":
        return render_template("signin.html")
    print(request.form)
    email = request.form.get("email")
    try:
        user = storage.search("PersonAuth", email=email)[0]
    except NoResultFound:
        print("email not found")
        return render_template("signin.html",
                               error="incorrect username or password")
    try:
        user = user.login(request.form.get("pswd", "pwd"))
    except ValueError:
        print(f"password {request.form.get('pswd')} mismatch")
        return render_template("signin.html",
                               error="incorrect username or password")
    identity = user.get("id")
    print(user)
    payload = {
                "userType": request.form.get("user"),
                "instcode": request.form.get("instid", "patient")
                }
    access_token = create_access_token(identity=identity, additional_claims=payload)
    response = make_response(redirect(f"/dashboard/{user.get('personality')}"))
    set_access_cookies(response, access_token)
    return response

@app_view.route("/dashboard/<personality>", methods=["GET"])
@jwt_required()
def dashboard(personality):
    """renders template for users"""
    user_id = get_jwt_identity()
    personality = str.capitalize(personality)
    try:
        user = storage.search(personality, id=user_id)[0]
    except NoResultFound:
        return redirect("/signin.html")
    if get_jwt().get("userType") == "staff":
        try:
            vts = storage.search_by_order("VitalSign", patient_id=user_id)[:5]
        except NoResultFound:
            vts = []
        try:
            record = storage.search_by_order("Casefile", patient_id=user_id)[:10]
        except NoResultFound:
            record = []
        userdata = {}
        userdata['vitalsign'] = vts
        userdata['record'] = record
        userdata = json.dumps(userdata)
        return render_template("staff.html", user=userdata,
                               **user.to_dict())
    else:
        try:
            record = storage.search_by_order("Casefile", staff_id=user_id)[:10]
        except NoResultFound:
            record = []
        userdata = {}
        userdata['record'] = record
        userdata = json.dumps(userdata)
        return render_template("dashboard.html", user=userdata,
                               **user.to_dict())


@app_view.route("/signup", methods=["GET", "POST"])
def signuppage():
    """returns sign up page"""
    if request.method == "GET":
        return render_template("register.html")
    details = request.form
    try:
        exist = storage.search(PersonAuth, email=details.get('email', 'nill'))
        if exist:
            error = "email already exist, please use another"
            return render_template("register.html", error=error)
    except NoResultFound:
        try:
            exist = storage.search(Patient, _Person__nin=details.get("nin"))
            if exist:
                error = "nin supplied already exist, please use another"
                return render_template("register.html", error=error)
        except NoResultFound:
            pass
    user = Patient(**details)
    try:
        user.nin = details.get("nin")
    except ValueError as msg:
        return render_template("register.html", error=msg)
    user.save()
    auth = PersonAuth(email=details.get('email'), person_id=user.id)
    auth.set_password(details.get("password"))
    auth.save()
    return redirect("/signin")
    # return jsonify(received=details,
                #    processed={"person": user.to_dict(), "auth":auth.email})


@app_view.route("/logout", methods=["GET"])
def logmeout():
    """logs user out"""
    token = create_access_token(identity="invalid",
                                expires_delta=timedelta(seconds=2))
    response = make_response(redirect("/"))
    set_access_cookies(response, token)
    return response
