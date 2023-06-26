#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'roseismysecretkey'
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None


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
