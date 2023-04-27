#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request, redirect, session
from views import app_views
from auth.auth import Auth
import json
from views.signinout import auth

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
