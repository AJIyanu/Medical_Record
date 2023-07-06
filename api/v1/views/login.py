#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from views import app_views
from models.loginauth import PersonAuth
from models.doctor import Doctor
from models.base_institution import Institution
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_jwt_extended import get_jwt, set_access_cookies


personality = {
                "Doctor": Doctor
    }


@app_views.route('/authme', methods=['POST'], strict_slashes=False)
def siginin():
    """returns jwt auth"""
    details = request.json
    log_in = PersonAuth.find_me(details['email'])
    if log_in is None:
        return jsonify({"error": "email not registered"}), 401
    try:
        log_in = log_in.login(details['pwd'])
    except ValueError:
        return jsonify({"error": "password error, try forgot password"}), 401
    payload = {
                "role": details.get("role", "guest"),
                "device": details.get("device", "onetime")
              }
    if details.get("user") == "staff":
        role = details.get("role")
        try:
            code = details["hosID"]
            id = log_in['id']
            if not personality[role].validate_inst_code(id, code):
                return jsonify(error="You are not authorized for this institution")
            payload.update(inst_code=details.get("hosID"))
        except KeyError:
            pass
    access_token = create_access_token(identity=log_in.get('id'),
                                       additional_claims=payload)
    response = jsonify(user=log_in, access_token=access_token)
    set_access_cookies(response, access_token)
    return response, 200


@app_views.route('/dashboarddata', methods=['GET'], strict_slashes=False)
@jwt_required()
def dashboarddata():
    """retrieves data after successful login"""
    userid = get_jwt_identity()
    role = get_jwt().get('role')
    inst_code = get_jwt().get("inst_code")
    institution = Institution.search_by_code(inst_code)
    return jsonify(user=PersonAuth.jwt_auth(userid),
                   institution=institution), 200
