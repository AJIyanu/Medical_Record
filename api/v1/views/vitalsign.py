#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from views import app_views
from models.loginauth import PersonAuth
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_jwt_extended import get_jwt
from models.vitalsign import VitalSign
from models.permissions import Permissions



@app_views.route('/lastvitalsign', methods=['POST'], strict_slashes=False)
# @jwt_required()
def last_vital_sign():
    """gets the last vital sign for the patient"""
    details = request.json
#    role = get_jwt().get("role")
#    print(role)
#    if not Permissions.me(role).permission("vitalsign", "view"):
#        return jsonify(msg="not permitted"), 403
    record = VitalSign.pat_last_saved(details.get("patient_id"))
    return jsonify(record=record), 200
