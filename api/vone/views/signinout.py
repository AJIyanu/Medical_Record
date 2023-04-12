#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, make_response, send_file, request
from views import app_views
from auth.auth import Auth, Authpat
import json
from models.healthcare import H_Facilities


auth = Auth()
patient = Authpat()


@app_views.route('/docsignin', methods=['POST'], strict_slashes=False)
def docsign_in():
    """validate log in and set cookies"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    code = request.form.get("institution_id")
    try:
        chk = auth.log_in(email=email, pwd=pwd, code=code)
        if chk:
            session = auth.create_session(email)
            user = auth.staff_id(email)
            cook = f"{session}.{user}"
            hosp = H_Facilities.find_me(code)
            resp = make_response(jsonify({"email": email, "userid": user}))
            resp.set_cookie('session_id', cook)
            resp.set_cookie("email", email)
            resp.set_cookie("hospital", code)
            resp.set_cookie("hosp_code", hosp)
            return resp, 200
    except ValueError as msg:
        return jsonify({"error": str(msg)}), 400
    return jsonify({"error": "wrong password or email"}), 400


@app_views.route('/patsignin', methods=['POST'], strict_slashes=False)
def patsign_in():
    """validate log in and set cookies"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    chk = patient.log_in(email=email, pwd=pwd)
    if chk:
        session = patient.create_session(email)
        user = patient.user_id(email)
        cook = f"{session}.{user}"
        jason = {email: user}
        resp = make_response(jsonify({"email": email, "userid": user}))
        resp.set_cookie('session_id', cook)
        resp.set_cookie('email', email)
        return resp, 200
    return jsonify({"error": "wrong password or email"}), 400
