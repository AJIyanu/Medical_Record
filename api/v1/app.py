#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from flask_jwt_extended import JWTManager, get_jwt, create_access_token
from flask_jwt_extended.exceptions import JWTDecodeError, NoAuthorizationError
from flask_jwt_extended  import create_access_token, set_access_cookies, get_jwt_identity
from jwt.exceptions import InvalidTokenError #NoTokenError
from datetime import timedelta, datetime, timezone

import os

from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'roseismysecretkey'
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_SECRET_KEY'] = 'roseismysecretekey'
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
jwt = JWTManager(app)
auth = None


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity(),
                                               additional_claims=get_jwt())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original response
        return response


@app.errorhandler(NoAuthorizationError)
def handle_no_token_error(error):
    response = {
        'error': 'NoTokenError',
        'message': 'No JWT token provided.'
    }
    return jsonify(response), 401


@app.errorhandler(JWTDecodeError)
def handle_jwt_decode_error(error):
    response = {
        'error': 'JWTDecodeError',
        'message': 'Failed to decode JWT token.'
    }
    return jsonify(response), 401

@app.errorhandler(InvalidTokenError)
def handle_invalid_token_error(error):
    response = {
        'error': 'InvalidTokenError',
        'message': 'Invalid access token.'
    }
    return jsonify(response), 401

app.register_error_handler(JWTDecodeError, handle_jwt_decode_error)
app.register_error_handler(InvalidTokenError, handle_invalid_token_error)


@app.before_request
def handle_before():
    """handles stuff before request is made"""
    nothing = ['/api/v1/status/', '/api/v1/unauthorized/',
               '/api/v1/forbidden/', '/api/v1/auth_session/login']
    if auth is None:
        return
    if auth.require_auth(request.path, nothing) is False:
        return
    if auth.authorization_header(request) is None:
        if auth.session_cookie(request) is None:
            abort(401)
    if auth.current_user(request) is None:
        abort(403)
    request.current_user = auth.current_user(request)
    return None


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def close_db(error):
     """ Close Storage """
     storage.close()

@app.errorhandler(401)
def not_authorized(error) -> str:
    """handling unauthorized shits"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """authorized but not aloowed"""
    return jsonify({"error": "Forbidden"}), 403






if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
