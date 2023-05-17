!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, render_template, send_file, request, session
from views import app_views
from auth.auth import Auth
import json
from views.signinout import auth
from models.healthcare import H_Facilities


@app_views.route('/doctor/<userid>', methods=['GET'], strict_slashes=False)
def dashboard(userid):
    """loads doctor dashbord"""
    res = request
    cookie = str(res.cookies.get("session_id")).split('.')[0]
    email = str(res.cookies.get("email"))
    hosp = str(res.cookies.get("hospital"))
    hosp = H_Facilities.inst_by_code(hosp)
    if not auth.validate_login(email, cookie):
        abort(403)
    doc = auth.get_staff(userid)
    msg = session.get("message", None)
    err = session.pop("error", None)
    doc['message'] = msg
    doc['error'] = err
    doc['hosp_name'] = hosp.get("name")
    doc['hosp_type'] = hosp.get("__class__")
    doc['hosp_id'] = hosp.get("id")
    print(f"this is the session set {msg}, and {err}, {session.get('check')}")
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
