#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, make_response, redirect, request
from views import app_views
from auth.auth import Auth, Authpat
import json



auth = Auth()
patient = Authpat()


@app_views.route('/docsignin', methods=['POST'], strict_slashes=False)
def docsign_in():
    """validate log in and set cookies"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    code = request.form.get("institution_id")
    try:
        user, session = auth.log_in(email=email, pwd=pwd)
    except ValueError as msg:
        return jsonify({"error": str(msg)}), 403
    if user.get('personality') != "doctor":
        auth.delete_session(user.get('id'), email)
        return jsonify({"error": "You must be a doctor to sign in"}), 400
    resp = make_response(jsonify({"email": email, "userid": user.get('id')}))
    if code:
        if not auth.auth_inst(user.get('id'), code):
            auth.delete_session(user.get('id'), email)
            return jsonify({"error": "you are not autorized for this institution"}), 403
        resp.set_cookie('hospital', code)
    resp.set_cookie('session_id', f"{session}.{user.get('id')}")
    resp.set_cookie('email', email)
    return resp, 200


@app_views.route('/logout', methods=['GET'], strict_slashes=False)
def signout():
    """signs user out and return to sign in page"""
    res = request
    cookie = str(res.cookies.get("session_id")).split('.')[1]
    email = str(res.cookies.get("email"))
    if cookie and email:
        try:
            auth.delete_session(cookie, email)
        except KeyError as msg:
            return jsonify({"error": str(msg)})
    return redirect("/signin", code=302)



@app_views.route('/patsignin', methods=['POST'], strict_slashes=False)
def patsign_in():
    """validate log in and set cookies"""
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        user, session = auth.log_in(email=email, pwd=pwd)
    except ValueError as msg:
        return jsonify({"error": str(msg)}), 403
    resp = make_response(jsonify({"email": email, "userid": user.get('id')}))
    resp.set_cookie('session_id', f"{session}.{user.get('id')}")
    resp.set_cookie('email', email)
    return resp, 200
