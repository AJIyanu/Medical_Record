#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from views import app_views
from models.loginauth import PersonAuth
from models.doctor import Doctor
from models.base_institution import Institution
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_jwt_extended import get_jwt, create_refresh_token
import base64


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
    refresh_token = create_refresh_token(identity=log_in.get('id'),
                                        additional_claims=payload)
    nin = base64.b64encode(log_in.get('_Person__nin').encode('utf-8')).decode('utf-8')
    response = jsonify(nin=nin, access_token=access_token, refresh_token=refresh_token)
    return response, 200


@app_views.route('/dashboarddata/<nin>', methods=['GET'], strict_slashes=False)
@jwt_required()
def dashboarddata(nin):
    """retrieves data after successful login"""
    userid = get_jwt_identity()
    role = get_jwt().get('role')
    inst_code = get_jwt().get("inst_code")
    institution = Institution.search_by_code(inst_code)
    user = PersonAuth.jwt_auth(userid)
    user['personality'] = user.get("personality").capitalize()
    if user['_Person__nin'] == nin:
        return jsonify(user=user, institution=institution, role=role), 200
    return(jsonify(error="you need to sign in"))


@app_views.route("/refresh", methods=['GET'], strict_slashes=False)
@jwt_required(refresh=True)
def refresh():
    """returns a new token on expiry"""
    identity = get_jwt_identity()
    payload = {
            "role": get_jwt().get("role"),
            "inst_code": get_jwt().get("inst_code"),
            "device": get_jwt().get("device")
            }
    access_token = create_access_token(identity=identity, additional_claims=payload)
    return jsonify(access_token=access_token)


@app_views.route("/logout", methods=["DELETE"])
@jwt_required(verify_type=False)
def logout():
    """Returns "Access token revoked" or "Refresh token revoked"""
    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]
    jwt_redis_blocklist.set(jti, "", ex=ACCESS_EXPIRES)
    return jsonify(msg=f"{ttype.capitalize()} token successfully revoked")
