#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file, request
from views import app_views
from auth.auth import Auth
import json
from views.signinout import auth


@app_views.route('/doctor/<userid>', methods=['GET'], strict_slashes=False)
def dashboard(userid):
    """loads doctor dashbord"""
    res = request
    cookie = str(res.cookies.get("session_id")).split('.')[0]
    email = str(res.cookies.get("email"))
    if not auth.validate_login(email, cookie):
        abort(403)
    doc = auth.get_staff(userid)
    return render_template("doctor.html", **doc)


@app_views.route("/findpatient", methods=["POST"], strict_slashes=False)
def find_patient():
    nin = request.form.get("NIN")
    if nin is not None and nin != "":
        data = auth.get_patient_data(nin)
        if "error" in data:
            return jsonify(data), 400
        data.update({
            "diseases": ["flu", "cold"],
            "medications": ["aspirin", "ibuprofen"],
                    })
        return jsonify(data), 200
    return jsonify({"error": "no nin found"}), 400
