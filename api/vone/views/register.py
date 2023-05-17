#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request, redirect, session
from views import app_views
from auth.auth import Auth
import json
from views.signinout import auth
from models.doctor import Doctor
from models.patient import Patient
from models.loginauth import PersonAuth
from datetime import datetime

from models.casefile import caseFile


@app_views.route("/doctor/savecasefile", methods=['POST'])
def save_casefile():
    """open a casefile and save it"""
    data = request.form
    #return jsonify(data), 200
    res = request
    cookie = str(res.cookies.get("session_id")).split('.')[0]
    email = str(res.cookies.get("email"))
    if not auth.validate_login(email, cookie):
        abort(403)
    record = caseFile()
    record.healthcare_id = str(res.cookies.get('hosp_code'))
    record.patient_id = "not a valid id" #data.get("patient_id")
    record.staff_id = str(res.cookies.get("session_id")).split('.')[1]
    record.symptoms = data.get("symptoms")
    record.diagnosis = data.get("diagnosis")
    record.prescription = data.get("prescription")
    record.testResult = data.get("prev-result")
    redir = str(res.cookies.get("session_id")).split('.')[1]
    session["check"] = "check"
    print('Session before redirect:', session)
    try:
        record.save()
        session['message'] = "Casefile saved succesfully"
        print('Session success before redirect:', session)
        return redirect("/status") #(f"/doctor/{redir}", code=302)
    except Exception:
        session["error"] = "Error saving casefile"
        print('Session error before redirect:', session)
        return redirect(f"/doctor/{redir}", code=302)

@app_views.route("/newperson", methods=['POST'], strict_slashes=False)
def newperson():
    """registers a new folk"""
    data = request.form
    try:
        del newuser
        del login
    except NameError:
        pass
    newuser = Patient(**data)
    login = PersonAuth(email=data.get('email'))
    login.person_id = newuser.id
    login.set_password(data.get("password"))
    newuser.dob = datetime.strptime(data.get("dob"), '%Y-%m-%d')
    newuser.nin = data.get('nin')
    newuser.save()
    login.save()
    return jsonify({"data": str(data), "user": newuser.to_dict()}), 200


@app_views.route('/states', strict_slashes=False)
def states():
    """returns a lists of states in json"""
    with open("states.json") as file:
        states = json.loads(file.read())
        statesjson = []
        for state in states:
            statesjson.append(state['states']['name'])
    return jsonify(statesjson)

@app_views.route('/lga/<state>', strict_slashes=False)
def lga(state):
    """returns a list of lga based on state"""
    with open('states.json') as file:
        states = json.loads(file.read())
        lgajson = []
        for st in states:
            if st['states']['name'] == state:
                for lgas in st['states']['locals']:
                    lgajson.append(lgas['name'])
                break
    print(lgajson)
    return jsonify(lgajson)
