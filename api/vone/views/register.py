#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file, request
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
    hpid = str(res.cookies.get('hospital'))
    record.healthcare_id = hpid
    record.patient_id = data.get("patient_id")
    record.staff_id = str(res.cookies.get("session_id")).split('.')[1]
    record.symptoms = data.get("symptoms")
    record.diagnosis = data.get("diagnosis")
    record.prescription = data.get("prescription")
    record.testResult = data.get("prev-result")
    try:
        #record.save()
        return jsonify({"hosp_cookie_check": hpid})
    except Exception as e:
        return jsonify({"error": e})
