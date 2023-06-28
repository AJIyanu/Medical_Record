#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from views import app_views
from models.loginauth import PersonAuth
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_jwt_extended import get_jwt



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
    access_token = create_access_token(identity=log_in.get('id'),
                                       additional_claims=payload)
    return jsonify({"user" :log_in, "access_token": access_token }), 200


@app_views.route('/dashboarddata', methods=['GET'], strict_slashes=False)
@jwt_required()
def dashboarddata():
    """retrieves data after successful login"""
    userid = get_jwt_identity()
    role = get_jwt().get('role')
    print(role)
    return jsonify(user=PersonAuth.jwt_auth(userid)), 200
