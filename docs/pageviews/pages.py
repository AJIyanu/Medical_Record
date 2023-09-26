#!/usr/bin/env python3
"""all routes here"""

import json
from datetime import timedelta, datetime

from flask_jwt_extended import (create_access_token, set_access_cookies,
                                jwt_required, get_jwt_identity, get_jwt)
from flask import render_template, request, redirect, make_response, jsonify
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from models import storage
from models.patient import Patient
from models.doctor import Doctor
from models.loginauth import PersonAuth
from models.vitalsign import VitalSign
from models.casefile import caseFile
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
    if request.form.get("user") == "staff":
        if user.get("personality") == "patient":
            return render_template("signin.html",
                               error="Please use the patient log in page")
    else:
        if user.get("personality") == "doctor" or user["personality"] == "nurses":
            return render_template("signin.html",
                                   error="Please use the staff log in page")
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
        return redirect("/signin")
    if get_jwt().get("userType") == "staff":
        try:
            record = storage.search_by_order("Casefile", all=True,
                                             staff_id=user_id)[:10]
            records = []
            for rec in record:
                pat = rec.get("patient_id")
                pat = Patient.user_by_nin(pat)
                name = f"{pat.surname} {pat.firstname} {pat.middlename}"
                date = datetime.strptime(rec.get("updated_at"),
                                         '%Y-%m-%dT%H:%M:%S')
                date = date.strftime('%b %d, %Y')
                records.append({"date": date, "name": name,
                                "prescription": rec.get("prescription"),
                                "diagnosis": rec.get("diagnosis")})
        except NoResultFound:
            records = []
        userdata = {}
        userdata['record'] = records
        userdata = json.dumps(userdata)
        return render_template("staff.html", user=userdata,
                               **user.to_dict())
    else:
        try:
            nin = Patient.user_by_id(user_id).get("_Person__nin")
            record = storage.search_by_order("Casefile", all=True,
                                             patient_id=nin)[:10]
            records = []
            for rec in record:
                doc = Doctor.user_by_id(rec['staff_id'])
                name = f"{doc['surname']} {doc['firstname']}"
                date = datetime.strptime(rec.get("updated_at"),
                                         '%Y-%m-%dT%H:%M:%S')
                date = date.strftime('%b %d, %Y')
                records.append({"date": date, "name": name,
                                "prescription": rec.get("prescription"),
                                "diagnosis": rec.get("diagnosis")})
        except NoResultFound:
            records = []
        try:
            vts = storage.search_by_order("VitalSign", all=True, patient_id=user_id)[:10]
            # print(vts)
        except NoResultFound:
            vts = []
        userdata = {}
        userdata['vitalsign'] = vts
        userdata['record'] = records
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

@app_view.route("/vitalsign", methods=["POST", "GET"])
@jwt_required()
def vitalsign():
    """return the vitalsign page and register"""
    if request.method == "GET":
        return render_template("vitalsign.html")
    details = request.form
    if details.get("nin"):
        try:
            pat = Patient.user_by_nin(details.get("nin"))
        except NoResultFound:
            return jsonify(error="NN does not exist. Check and try again")
        print(pat.to_dict())
        name = f"{pat.surname} {pat.firstname} {pat.middlename}"
        pat_id = pat.id
        return jsonify(name=name, pat_id=pat_id)
    new_data = VitalSign(healthcare_id="0cdb0251-c77e-4b7e-a5e1-21ffc3c14b59",
                         staff_id=get_jwt_identity(), **details)
    try:
        new_data.save()
    except IntegrityError:
        return jsonify(error="IntegrityError")
    return jsonify(success="Data has been saved successfully")


@app_view.route("/casefile", methods=["POST", "GET"])
@jwt_required()
def casefile():
    """returns casefile page and process casfile data"""
    if request.method == "GET":
        return render_template("casefile.html")
    details = request.form
    if details.get("nin"):
        try:
            pat = Patient.user_by_nin(details.get("nin"))
        except NoResultFound:
            return jsonify(error="NN does not exist. Check and try again")
        # print(pat.to_dict())
        name = f"{pat.surname} {pat.firstname} {pat.middlename}"
        pat_id = pat.nin
        vts = storage.search_by_order("VitalSign", all=True, patient_id=pat.id)[:10]
        return jsonify(name=name, pat_id=pat_id, vitalsign=vts,
                       patientdata={"sex": pat.sex, "age": pat.dob})
    new_casefile = caseFile(healthcare_id="0cdb0251-c77e-4b7e-a5e1-21ffc3c14b59",
                            staff_id=get_jwt_identity(), **details)
    try:
        new_casefile.save()
    except Exception as msg:
        print(msg)
        return jsonify(error="not saved. check msg for error")
    return jsonify(success="saved successfully")
