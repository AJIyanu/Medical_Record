#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file, request
from views import app_views
from auth.auth import Auth
import json
from views.signinout import patient as pat


@app_views.route('/patient/<userid>', methods=['GET'], strict_slashes=False)
def patdashboard(userid):
    """loads doctor dashbord"""
    res = request
    cookie = str(res.cookies.get("session_id")).split('.')[0]
    email = str(res.cookies.get("email"))
    if not pat.validate_login(email, cookie):
        abort(403)
    patient = pat.get_patient(userid)
    return render_template("patient.html", **patient)

