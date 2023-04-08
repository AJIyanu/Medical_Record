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
    #record.staff_id = "2812ad2c-c3e7-438d-8d85-8d94fde374e1"
    record.healthcare_id = "c295ae81-ca73-4af0-a293-2e17f318d5f7"
    record.patient_id = "e41f2b35-4b48-4c8b-bf7d-1df7b6d26e92"
    record.staff_id = str(res.cookies.get("session_id")).split('.')[1]
    record.symptoms = json.dumps(data.get("symptoms"))
    record.diagnosis = data.get("diagnosis")
    record.prescription = data.get("prescription")
    record.testResult = data.get("prev-result")
    try:
        record.save()
        return jsonify({"email":email, "cookie": cookie})
    except Exception as e:
        return jsonify({"error": e})
